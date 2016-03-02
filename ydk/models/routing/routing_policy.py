""" routing_policy 

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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.policy.policy_types import MatchSetOptionsRestrictedType_Enum

class DefaultPolicyType_Enum(Enum):
    """
    DefaultPolicyType_Enum

    type used to specify default route disposition in
    a policy chain

    """

    """

    default policy to accept the route

    """
    ACCEPT_ROUTE = 0

    """

    default policy to reject the route

    """
    REJECT_ROUTE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.routing._meta import _routing_policy as meta
        return meta._meta_table['DefaultPolicyType_Enum']



class RoutingPolicy(object):
    """
    top\-level container for all routing policy configuration
    
    .. attribute:: defined_sets
    
    	Predefined sets of attributes used in policy match statements
    	**type**\: :py:class:`DefinedSets <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets>`
    
    .. attribute:: policy_definitions
    
    	Enclosing container for the list of top\-level policy definitions
    	**type**\: :py:class:`PolicyDefinitions <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions>`
    
    

    """

    _prefix = 'rpol'
    _revision = '2015-05-15'

    def __init__(self):
        self.defined_sets = RoutingPolicy.DefinedSets()
        self.defined_sets.parent = self
        self.policy_definitions = RoutingPolicy.PolicyDefinitions()
        self.policy_definitions.parent = self


    class DefinedSets(object):
        """
        Predefined sets of attributes used in policy match
        statements
        
        .. attribute:: neighbor_sets
        
        	Enclosing container for defined neighbor sets for matching
        	**type**\: :py:class:`NeighborSets <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.NeighborSets>`
        
        .. attribute:: prefix_sets
        
        	Enclosing container for defined prefix sets for matching
        	**type**\: :py:class:`PrefixSets <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.PrefixSets>`
        
        .. attribute:: tag_sets
        
        	Enclosing container for defined tag sets for matching
        	**type**\: :py:class:`TagSets <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.TagSets>`
        
        

        """

        _prefix = 'rpol'
        _revision = '2015-05-15'

        def __init__(self):
            self.parent = None
            self.neighbor_sets = RoutingPolicy.DefinedSets.NeighborSets()
            self.neighbor_sets.parent = self
            self.prefix_sets = RoutingPolicy.DefinedSets.PrefixSets()
            self.prefix_sets.parent = self
            self.tag_sets = RoutingPolicy.DefinedSets.TagSets()
            self.tag_sets.parent = self


        class NeighborSets(object):
            """
            Enclosing container for defined neighbor sets for matching
            
            .. attribute:: neighbor_set
            
            	Definitions for neighbor sets
            	**type**\: list of :py:class:`NeighborSet <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.neighbor_set = YList()
                self.neighbor_set.parent = self
                self.neighbor_set.name = 'neighbor_set'


            class NeighborSet(object):
                """
                Definitions for neighbor sets
                
                .. attribute:: neighbor_set_name
                
                	name / label of the neighbor set \-\- this is used to reference the set in match conditions
                	**type**\: str
                
                .. attribute:: neighbor
                
                	list of addresses that are part of the neighbor set
                	**type**\: list of :py:class:`Neighbor <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.neighbor_set_name = None
                    self.neighbor = YList()
                    self.neighbor.parent = self
                    self.neighbor.name = 'neighbor'


                class Neighbor(object):
                    """
                    list of addresses that are part of the neighbor set
                    
                    .. attribute:: address
                    
                    	IP address of the neighbor set member
                    	**type**\: one of { str | str }
                    
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYDataValidationError('Key property address is None')

                        return self.parent._common_path +'/routing-policy:neighbor[routing-policy:address = ' + str(self.address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.address is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.routing._meta import _routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor']['meta_info']

                @property
                def _common_path(self):
                    if self.neighbor_set_name is None:
                        raise YPYDataValidationError('Key property neighbor_set_name is None')

                    return '/routing-policy:routing-policy/routing-policy:defined-sets/routing-policy:neighbor-sets/routing-policy:neighbor-set[routing-policy:neighbor-set-name = ' + str(self.neighbor_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.neighbor_set_name is not None:
                        return True

                    if self.neighbor is not None:
                        for child_ref in self.neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.routing._meta import _routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet']['meta_info']

            @property
            def _common_path(self):

                return '/routing-policy:routing-policy/routing-policy:defined-sets/routing-policy:neighbor-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.neighbor_set is not None:
                    for child_ref in self.neighbor_set:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.routing._meta import _routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.NeighborSets']['meta_info']


        class PrefixSets(object):
            """
            Enclosing container for defined prefix sets for matching
            
            .. attribute:: prefix_set
            
            	List of the defined prefix sets
            	**type**\: list of :py:class:`PrefixSet <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.prefix_set = YList()
                self.prefix_set.parent = self
                self.prefix_set.name = 'prefix_set'


            class PrefixSet(object):
                """
                List of the defined prefix sets
                
                .. attribute:: prefix_set_name
                
                	name / label of the prefix set \-\- this is used to reference the set in match conditions
                	**type**\: str
                
                .. attribute:: prefix
                
                	List of prefix expressions that are part of the set
                	**type**\: list of :py:class:`Prefix <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.prefix_set_name = None
                    self.prefix = YList()
                    self.prefix.parent = self
                    self.prefix.name = 'prefix'


                class Prefix(object):
                    """
                    List of prefix expressions that are part of the set
                    
                    .. attribute:: ip_prefix
                    
                    	The prefix member in CIDR notation \-\- while the prefix may be either IPv4 or IPv6, most implementations require all members of the prefix set to be the same address family.  Mixing address types in the same prefix set is likely to cause an error
                    	**type**\: one of { str | str }
                    
                    .. attribute:: masklength_range
                    
                    	Defines a range for the masklength, or 'exact' if the prefix has an exact length.  Example\: 10.3.192.0/21 through 10.3.192.0/24 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: 21..24.  Example\: 10.3.192.0/21 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: exact
                    	**type**\: str
                    
                    	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                    
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.ip_prefix = None
                        self.masklength_range = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.ip_prefix is None:
                            raise YPYDataValidationError('Key property ip_prefix is None')
                        if self.masklength_range is None:
                            raise YPYDataValidationError('Key property masklength_range is None')

                        return self.parent._common_path +'/routing-policy:prefix[routing-policy:ip-prefix = ' + str(self.ip_prefix) + '][routing-policy:masklength-range = ' + str(self.masklength_range) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.ip_prefix is not None:
                            return True

                        if self.masklength_range is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.routing._meta import _routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix']['meta_info']

                @property
                def _common_path(self):
                    if self.prefix_set_name is None:
                        raise YPYDataValidationError('Key property prefix_set_name is None')

                    return '/routing-policy:routing-policy/routing-policy:defined-sets/routing-policy:prefix-sets/routing-policy:prefix-set[routing-policy:prefix-set-name = ' + str(self.prefix_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.prefix_set_name is not None:
                        return True

                    if self.prefix is not None:
                        for child_ref in self.prefix:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.routing._meta import _routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet']['meta_info']

            @property
            def _common_path(self):

                return '/routing-policy:routing-policy/routing-policy:defined-sets/routing-policy:prefix-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.prefix_set is not None:
                    for child_ref in self.prefix_set:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.routing._meta import _routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.PrefixSets']['meta_info']


        class TagSets(object):
            """
            Enclosing container for defined tag sets for matching
            
            .. attribute:: tag_set
            
            	Definitions for tag sets
            	**type**\: list of :py:class:`TagSet <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.tag_set = YList()
                self.tag_set.parent = self
                self.tag_set.name = 'tag_set'


            class TagSet(object):
                """
                Definitions for tag sets
                
                .. attribute:: tag_set_name
                
                	name / label of the tag set \-\- this is used to reference the set in match conditions
                	**type**\: str
                
                .. attribute:: tag
                
                	list of tags that are part of the tag set
                	**type**\: list of :py:class:`Tag <ydk.models.routing.routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.Tag>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.tag_set_name = None
                    self.tag = YList()
                    self.tag.parent = self
                    self.tag.name = 'tag'


                class Tag(object):
                    """
                    list of tags that are part of the tag set
                    
                    .. attribute:: value
                    
                    	Value of the tag set member
                    	**type**\: one of { int | str }
                    
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.value is None:
                            raise YPYDataValidationError('Key property value is None')

                        return self.parent._common_path +'/routing-policy:tag[routing-policy:value = ' + str(self.value) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.value is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.routing._meta import _routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet.Tag']['meta_info']

                @property
                def _common_path(self):
                    if self.tag_set_name is None:
                        raise YPYDataValidationError('Key property tag_set_name is None')

                    return '/routing-policy:routing-policy/routing-policy:defined-sets/routing-policy:tag-sets/routing-policy:tag-set[routing-policy:tag-set-name = ' + str(self.tag_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.tag_set_name is not None:
                        return True

                    if self.tag is not None:
                        for child_ref in self.tag:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.routing._meta import _routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet']['meta_info']

            @property
            def _common_path(self):

                return '/routing-policy:routing-policy/routing-policy:defined-sets/routing-policy:tag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tag_set is not None:
                    for child_ref in self.tag_set:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.routing._meta import _routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.TagSets']['meta_info']

        @property
        def _common_path(self):

            return '/routing-policy:routing-policy/routing-policy:defined-sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.neighbor_sets is not None and self.neighbor_sets._has_data():
                return True

            if self.neighbor_sets is not None and self.neighbor_sets.is_presence():
                return True

            if self.prefix_sets is not None and self.prefix_sets._has_data():
                return True

            if self.prefix_sets is not None and self.prefix_sets.is_presence():
                return True

            if self.tag_sets is not None and self.tag_sets._has_data():
                return True

            if self.tag_sets is not None and self.tag_sets.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.routing._meta import _routing_policy as meta
            return meta._meta_table['RoutingPolicy.DefinedSets']['meta_info']


    class PolicyDefinitions(object):
        """
        Enclosing container for the list of top\-level policy
        definitions
        
        .. attribute:: policy_definition
        
        	List of top\-level policy definitions, keyed by unique name.  These policy definitions are expected to be referenced (by name) in policy chains specified in import/ export configuration statements
        	**type**\: list of :py:class:`PolicyDefinition <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
        
        

        """

        _prefix = 'rpol'
        _revision = '2015-05-15'

        def __init__(self):
            self.parent = None
            self.policy_definition = YList()
            self.policy_definition.parent = self
            self.policy_definition.name = 'policy_definition'


        class PolicyDefinition(object):
            """
            List of top\-level policy definitions, keyed by unique
            name.  These policy definitions are expected to be
            referenced (by name) in policy chains specified in import/
            export configuration statements.
            
            .. attribute:: name
            
            	Name of the top\-level policy definition \-\- this name  is used in references to the current policy
            	**type**\: str
            
            .. attribute:: statements
            
            	Enclosing container for policy statements
            	**type**\: :py:class:`Statements <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-05-15'

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
                	**type**\: list of :py:class:`Statement <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.statement = YList()
                    self.statement.parent = self
                    self.statement.name = 'statement'


                class Statement(object):
                    """
                    Policy statements group conditions and actions within
                    a policy definition.  They are evaluated in the order
                    specified (see the description of policy evaluation
                    at the top of this module.
                    
                    .. attribute:: name
                    
                    	name of the policy statement
                    	**type**\: str
                    
                    .. attribute:: actions
                    
                    	Action statements for this policy statement
                    	**type**\: :py:class:`Actions <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions>`
                    
                    .. attribute:: conditions
                    
                    	Condition statements for this policy statement
                    	**type**\: :py:class:`Conditions <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions>`
                    
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions()
                        self.actions.parent = self
                        self.conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions()
                        self.conditions.parent = self


                    class Actions(object):
                        """
                        Action statements for this policy
                        statement
                        
                        .. attribute:: accept_route
                        
                        	accepts the route into the routing table
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: igp_actions
                        
                        	Actions to set IGP route attributes; these actions apply to multiple IGPs
                        	**type**\: :py:class:`IgpActions <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions>`
                        
                        .. attribute:: reject_route
                        
                        	rejects the route
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'rpol'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.accept_route = None
                            self.igp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions()
                            self.igp_actions.parent = self
                            self.reject_route = None


                        class IgpActions(object):
                            """
                            Actions to set IGP route attributes; these actions
                            apply to multiple IGPs
                            
                            .. attribute:: set_tag
                            
                            	Set the tag value for OSPF or IS\-IS routes
                            	**type**\: one of { int | str }
                            
                            

                            """

                            _prefix = 'rpol'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.set_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/routing-policy:igp-actions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.set_tag is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.routing._meta import _routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/routing-policy:actions'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.accept_route is not None:
                                return True

                            if self.igp_actions is not None and self.igp_actions._has_data():
                                return True

                            if self.igp_actions is not None and self.igp_actions.is_presence():
                                return True

                            if self.reject_route is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.routing._meta import _routing_policy as meta
                            return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info']


                    class Conditions(object):
                        """
                        Condition statements for this
                        policy statement
                        
                        .. attribute:: call_policy
                        
                        	Applies the statements from the specified policy definition and then returns control the current policy statement. Note that the called policy may itself call other policies (subject to implementation limitations). This is intended to provide a policy 'subroutine' capability.  The called policy should contain an explicit or a default route disposition that returns an effective true (accept\-route) or false (reject\-route), otherwise the behavior may be ambiguous and implementation dependent
                        	**type**\: str
                        
                        .. attribute:: igp_conditions
                        
                        	Policy conditions for IGP attributes
                        	**type**\: :py:class:`IgpConditions <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions>`
                        
                        .. attribute:: install_protocol_eq
                        
                        	Condition to check the protocol / method used to install which installed the route into the local routing table
                        	**type**\: str
                        
                        .. attribute:: match_neighbor_set
                        
                        	Match a referenced neighbor set according to the logic defined in the match\-set\-options\-leaf
                        	**type**\: :py:class:`MatchNeighborSet <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet>`
                        
                        .. attribute:: match_prefix_set
                        
                        	Match a referenced prefix\-set according to the logic defined in the match\-set\-options leaf
                        	**type**\: :py:class:`MatchPrefixSet <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet>`
                        
                        .. attribute:: match_tag_set
                        
                        	Match a referenced tag set according to the logic defined in the match\-options\-set leaf
                        	**type**\: :py:class:`MatchTagSet <ydk.models.routing.routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet>`
                        
                        

                        """

                        _prefix = 'rpol'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.call_policy = None
                            self.igp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions()
                            self.igp_conditions.parent = self
                            self.install_protocol_eq = None
                            self.match_neighbor_set = None
                            self.match_prefix_set = None
                            self.match_tag_set = None


                        class IgpConditions(object):
                            """
                            Policy conditions for IGP attributes
                            
                            

                            """

                            _prefix = 'rpol'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/routing-policy:igp-conditions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.routing._meta import _routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions']['meta_info']


                        class MatchNeighborSet(object):
                            """
                            Match a referenced neighbor set according to the logic
                            defined in the match\-set\-options\-leaf
                            
                            .. attribute:: match_set_options
                            
                            	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                            	**type**\: :py:class:`MatchSetOptionsRestrictedType_Enum <ydk.models.policy.policy_types.MatchSetOptionsRestrictedType_Enum>`
                            
                            .. attribute:: neighbor_set
                            
                            	References a defined neighbor set
                            	**type**\: str
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'rpol'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.match_set_options = None
                                self.neighbor_set = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/routing-policy:match-neighbor-set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.match_set_options is not None:
                                    return True

                                if self.neighbor_set is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return True

                            @staticmethod
                            def _meta_info():
                                from ydk.models.routing._meta import _routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet']['meta_info']


                        class MatchPrefixSet(object):
                            """
                            Match a referenced prefix\-set according to the logic
                            defined in the match\-set\-options leaf
                            
                            .. attribute:: match_set_options
                            
                            	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                            	**type**\: :py:class:`MatchSetOptionsRestrictedType_Enum <ydk.models.policy.policy_types.MatchSetOptionsRestrictedType_Enum>`
                            
                            .. attribute:: prefix_set
                            
                            	References a defined prefix set
                            	**type**\: str
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'rpol'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.match_set_options = None
                                self.prefix_set = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/routing-policy:match-prefix-set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.match_set_options is not None:
                                    return True

                                if self.prefix_set is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return True

                            @staticmethod
                            def _meta_info():
                                from ydk.models.routing._meta import _routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet']['meta_info']


                        class MatchTagSet(object):
                            """
                            Match a referenced tag set according to the logic defined
                            in the match\-options\-set leaf
                            
                            .. attribute:: match_set_options
                            
                            	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                            	**type**\: :py:class:`MatchSetOptionsRestrictedType_Enum <ydk.models.policy.policy_types.MatchSetOptionsRestrictedType_Enum>`
                            
                            .. attribute:: tag_set
                            
                            	References a defined tag set
                            	**type**\: str
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'rpol'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.match_set_options = None
                                self.tag_set = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/routing-policy:match-tag-set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.match_set_options is not None:
                                    return True

                                if self.tag_set is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return True

                            @staticmethod
                            def _meta_info():
                                from ydk.models.routing._meta import _routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/routing-policy:conditions'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.call_policy is not None:
                                return True

                            if self.igp_conditions is not None and self.igp_conditions._has_data():
                                return True

                            if self.igp_conditions is not None and self.igp_conditions.is_presence():
                                return True

                            if self.install_protocol_eq is not None:
                                return True

                            if self.match_neighbor_set is not None and self.match_neighbor_set._has_data():
                                return True

                            if self.match_neighbor_set is not None and self.match_neighbor_set.is_presence():
                                return True

                            if self.match_prefix_set is not None and self.match_prefix_set._has_data():
                                return True

                            if self.match_prefix_set is not None and self.match_prefix_set.is_presence():
                                return True

                            if self.match_tag_set is not None and self.match_tag_set._has_data():
                                return True

                            if self.match_tag_set is not None and self.match_tag_set.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.routing._meta import _routing_policy as meta
                            return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYDataValidationError('Key property name is None')

                        return self.parent._common_path +'/routing-policy:statement[routing-policy:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.name is not None:
                            return True

                        if self.actions is not None and self.actions._has_data():
                            return True

                        if self.actions is not None and self.actions.is_presence():
                            return True

                        if self.conditions is not None and self.conditions._has_data():
                            return True

                        if self.conditions is not None and self.conditions.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.routing._meta import _routing_policy as meta
                        return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/routing-policy:statements'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.statement is not None:
                        for child_ref in self.statement:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.routing._meta import _routing_policy as meta
                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/routing-policy:routing-policy/routing-policy:policy-definitions/routing-policy:policy-definition[routing-policy:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.name is not None:
                    return True

                if self.statements is not None and self.statements._has_data():
                    return True

                if self.statements is not None and self.statements.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.routing._meta import _routing_policy as meta
                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition']['meta_info']

        @property
        def _common_path(self):

            return '/routing-policy:routing-policy/routing-policy:policy-definitions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.policy_definition is not None:
                for child_ref in self.policy_definition:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.routing._meta import _routing_policy as meta
            return meta._meta_table['RoutingPolicy.PolicyDefinitions']['meta_info']

    @property
    def _common_path(self):

        return '/routing-policy:routing-policy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.defined_sets is not None and self.defined_sets._has_data():
            return True

        if self.defined_sets is not None and self.defined_sets.is_presence():
            return True

        if self.policy_definitions is not None and self.policy_definitions._has_data():
            return True

        if self.policy_definitions is not None and self.policy_definitions.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.routing._meta import _routing_policy as meta
        return meta._meta_table['RoutingPolicy']['meta_info']


