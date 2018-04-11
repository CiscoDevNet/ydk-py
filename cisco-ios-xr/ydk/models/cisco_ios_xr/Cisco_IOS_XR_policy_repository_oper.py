""" Cisco_IOS_XR_policy_repository_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package operational data.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AddressFamily(Enum):
    """
    AddressFamily (Enum Class)

    Address Family

    .. data:: ipv4 = 0

    	IPv4 Address Family

    .. data:: ipv6 = 1

    	IPv6 Address Family

    .. data:: l2vpn = 2

    	L2VPN Address Family

    .. data:: ls = 3

    	LINKSTATE Address Family

    .. data:: af_none = 4

    	No Address Family

    .. data:: af_unknown = 5

    	Unknown Address Family

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")

    l2vpn = Enum.YLeaf(2, "l2vpn")

    ls = Enum.YLeaf(3, "ls")

    af_none = Enum.YLeaf(4, "af-none")

    af_unknown = Enum.YLeaf(5, "af-unknown")


class AttachPointDirection(Enum):
    """
    AttachPointDirection (Enum Class)

    Attach Point Direction

    .. data:: in_ = 0

    	Attach Point Direction IN

    .. data:: out = 1

    	Attach Point Direction OUT

    """

    in_ = Enum.YLeaf(0, "in")

    out = Enum.YLeaf(1, "out")


class Group(Enum):
    """
    Group (Enum Class)

    BGP Neighbor Group Type

    .. data:: address_family_group = 0

    	Address Family Group

    .. data:: session_group = 1

    	Session Group

    .. data:: neighbor_group = 2

    	Neighbor Group

    .. data:: neighbor = 3

    	Neighbor

    .. data:: error_group = 4

    	Error Group

    """

    address_family_group = Enum.YLeaf(0, "address-family-group")

    session_group = Enum.YLeaf(1, "session-group")

    neighbor_group = Enum.YLeaf(2, "neighbor-group")

    neighbor = Enum.YLeaf(3, "neighbor")

    error_group = Enum.YLeaf(4, "error-group")


class ObjectStatus(Enum):
    """
    ObjectStatus (Enum Class)

    Whether an RPL object is used/referenced

    .. data:: active = 0

    	The object is in use

    .. data:: inactive = 1

    	The object is referenced by another object, but

    	not used

    .. data:: unused = 2

    	The object is not used or referenced

    """

    active = Enum.YLeaf(0, "active")

    inactive = Enum.YLeaf(1, "inactive")

    unused = Enum.YLeaf(2, "unused")


class SubAddressFamily(Enum):
    """
    SubAddressFamily (Enum Class)

    Sub Address Family

    .. data:: unicast = 0

    	Unicast

    .. data:: multicast = 1

    	Multicast

    .. data:: label = 2

    	Label

    .. data:: tunnel = 3

    	Tunnel

    .. data:: vpn = 4

    	VPN

    .. data:: mdt = 5

    	MDT

    .. data:: vpls = 6

    	VPLS

    .. data:: rt_constraint = 7

    	RTConstraint

    .. data:: mvpn = 8

    	MVPN

    .. data:: flow = 9

    	FLOW

    .. data:: vpn_mcast = 10

    	VPN Multicast

    .. data:: evpn = 11

    	EVPN

    .. data:: saf_none = 12

    	No SAFI

    .. data:: saf_unknown = 13

    	Unknown

    """

    unicast = Enum.YLeaf(0, "unicast")

    multicast = Enum.YLeaf(1, "multicast")

    label = Enum.YLeaf(2, "label")

    tunnel = Enum.YLeaf(3, "tunnel")

    vpn = Enum.YLeaf(4, "vpn")

    mdt = Enum.YLeaf(5, "mdt")

    vpls = Enum.YLeaf(6, "vpls")

    rt_constraint = Enum.YLeaf(7, "rt-constraint")

    mvpn = Enum.YLeaf(8, "mvpn")

    flow = Enum.YLeaf(9, "flow")

    vpn_mcast = Enum.YLeaf(10, "vpn-mcast")

    evpn = Enum.YLeaf(11, "evpn")

    saf_none = Enum.YLeaf(12, "saf-none")

    saf_unknown = Enum.YLeaf(13, "saf-unknown")



class RoutingPolicy(Entity):
    """
    Routing policy operational data
    
    .. attribute:: limits
    
    	Information about configured limits and the current values
    	**type**\:  :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Limits>`
    
    .. attribute:: policies
    
    	Information about configured route policies
    	**type**\:  :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies>`
    
    .. attribute:: sets
    
    	Information about configured sets
    	**type**\:  :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets>`
    
    

    """

    _prefix = 'policy-repository-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-policy"
        self.yang_parent_name = "Cisco-IOS-XR-policy-repository-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("limits", ("limits", RoutingPolicy.Limits)), ("policies", ("policies", RoutingPolicy.Policies)), ("sets", ("sets", RoutingPolicy.Sets))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.limits = RoutingPolicy.Limits()
        self.limits.parent = self
        self._children_name_map["limits"] = "limits"
        self._children_yang_names.add("limits")

        self.policies = RoutingPolicy.Policies()
        self.policies.parent = self
        self._children_name_map["policies"] = "policies"
        self._children_yang_names.add("policies")

        self.sets = RoutingPolicy.Sets()
        self.sets.parent = self
        self._children_name_map["sets"] = "sets"
        self._children_yang_names.add("sets")
        self._segment_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy"


    class Limits(Entity):
        """
        Information about configured limits and the
        current values
        
        .. attribute:: maximum_lines_of_policy
        
        	Maximum lines of configuration allowable for all policies and sets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_lines_of_policy_limit
        
        	Number of lines of configuration for policies/sets currently allowed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_lines_of_policy_used
        
        	Current number of lines configured for all policies and sets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: maximum_number_of_policies
        
        	Maximum number of policies allowable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_number_of_policies_limit
        
        	Number of policies currently allowed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_number_of_policies_used
        
        	Current number of policies configured
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: compiled_policies_length
        
        	The total compiled length of all policies
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'policy-repository-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Limits, self).__init__()

            self.yang_name = "limits"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('maximum_lines_of_policy', YLeaf(YType.uint32, 'maximum-lines-of-policy')),
                ('current_lines_of_policy_limit', YLeaf(YType.uint32, 'current-lines-of-policy-limit')),
                ('current_lines_of_policy_used', YLeaf(YType.uint32, 'current-lines-of-policy-used')),
                ('maximum_number_of_policies', YLeaf(YType.uint32, 'maximum-number-of-policies')),
                ('current_number_of_policies_limit', YLeaf(YType.uint32, 'current-number-of-policies-limit')),
                ('current_number_of_policies_used', YLeaf(YType.uint32, 'current-number-of-policies-used')),
                ('compiled_policies_length', YLeaf(YType.uint32, 'compiled-policies-length')),
            ])
            self.maximum_lines_of_policy = None
            self.current_lines_of_policy_limit = None
            self.current_lines_of_policy_used = None
            self.maximum_number_of_policies = None
            self.current_number_of_policies_limit = None
            self.current_number_of_policies_used = None
            self.compiled_policies_length = None
            self._segment_path = lambda: "limits"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.Limits, ['maximum_lines_of_policy', 'current_lines_of_policy_limit', 'current_lines_of_policy_used', 'maximum_number_of_policies', 'current_number_of_policies_limit', 'current_number_of_policies_used', 'compiled_policies_length'], name, value)


    class Policies(Entity):
        """
        Information about configured route policies
        
        .. attribute:: route_policies
        
        	Information about individual policies
        	**type**\:  :py:class:`RoutePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies>`
        
        .. attribute:: unused
        
        	All objects of a given type that are not referenced at all
        	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.Unused>`
        
        .. attribute:: inactive
        
        	All objects of a given type that are not attached to a protocol
        	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.Inactive>`
        
        .. attribute:: active
        
        	All objects of a given type that are attached to a protocol
        	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.Active>`
        
        

        """

        _prefix = 'policy-repository-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Policies, self).__init__()

            self.yang_name = "policies"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("route-policies", ("route_policies", RoutingPolicy.Policies.RoutePolicies)), ("unused", ("unused", RoutingPolicy.Policies.Unused)), ("inactive", ("inactive", RoutingPolicy.Policies.Inactive)), ("active", ("active", RoutingPolicy.Policies.Active))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.route_policies = RoutingPolicy.Policies.RoutePolicies()
            self.route_policies.parent = self
            self._children_name_map["route_policies"] = "route-policies"
            self._children_yang_names.add("route-policies")

            self.unused = RoutingPolicy.Policies.Unused()
            self.unused.parent = self
            self._children_name_map["unused"] = "unused"
            self._children_yang_names.add("unused")

            self.inactive = RoutingPolicy.Policies.Inactive()
            self.inactive.parent = self
            self._children_name_map["inactive"] = "inactive"
            self._children_yang_names.add("inactive")

            self.active = RoutingPolicy.Policies.Active()
            self.active.parent = self
            self._children_name_map["active"] = "active"
            self._children_yang_names.add("active")
            self._segment_path = lambda: "policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/%s" % self._segment_path()


        class RoutePolicies(Entity):
            """
            Information about individual policies
            
            .. attribute:: route_policy
            
            	Information about an individual policy
            	**type**\: list of  		 :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.RoutePolicies, self).__init__()

                self.yang_name = "route-policies"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("route-policy", ("route_policy", RoutingPolicy.Policies.RoutePolicies.RoutePolicy))])
                self._leafs = OrderedDict()

                self.route_policy = YList(self)
                self._segment_path = lambda: "route-policies"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.RoutePolicies, [], name, value)


            class RoutePolicy(Entity):
                """
                Information about an individual policy
                
                .. attribute:: route_policy_name  (key)
                
                	Route policy name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: policy_uses
                
                	Information about which policies and sets this policy uses
                	**type**\:  :py:class:`PolicyUses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses>`
                
                .. attribute:: used_by
                
                	Policies that use this object, directly or indirectly
                	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy>`
                
                .. attribute:: attached
                
                	Information about where this policy or set is attached
                	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy, self).__init__()

                    self.yang_name = "route-policy"
                    self.yang_parent_name = "route-policies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['route_policy_name']
                    self._child_container_classes = OrderedDict([("policy-uses", ("policy_uses", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses)), ("used-by", ("used_by", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy)), ("attached", ("attached", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                    ])
                    self.route_policy_name = None

                    self.policy_uses = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses()
                    self.policy_uses.parent = self
                    self._children_name_map["policy_uses"] = "policy-uses"
                    self._children_yang_names.add("policy-uses")

                    self.used_by = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy()
                    self.used_by.parent = self
                    self._children_name_map["used_by"] = "used-by"
                    self._children_yang_names.add("used-by")

                    self.attached = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached()
                    self.attached.parent = self
                    self._children_name_map["attached"] = "attached"
                    self._children_yang_names.add("attached")
                    self._segment_path = lambda: "route-policy" + "[route-policy-name='" + str(self.route_policy_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/route-policies/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy, ['route_policy_name'], name, value)


                class PolicyUses(Entity):
                    """
                    Information about which policies and sets
                    this policy uses
                    
                    .. attribute:: directly_used_policies
                    
                    	Policies that this policy uses directly
                    	**type**\:  :py:class:`DirectlyUsedPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies>`
                    
                    .. attribute:: all_used_sets
                    
                    	Sets used by this policy, or by policies that it uses
                    	**type**\:  :py:class:`AllUsedSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets>`
                    
                    .. attribute:: directly_used_sets
                    
                    	Sets that this policy uses directly
                    	**type**\:  :py:class:`DirectlyUsedSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets>`
                    
                    .. attribute:: all_used_policies
                    
                    	Policies used by this policy, or by policies that it uses
                    	**type**\:  :py:class:`AllUsedPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses, self).__init__()

                        self.yang_name = "policy-uses"
                        self.yang_parent_name = "route-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("directly-used-policies", ("directly_used_policies", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies)), ("all-used-sets", ("all_used_sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets)), ("directly-used-sets", ("directly_used_sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets)), ("all-used-policies", ("all_used_policies", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.directly_used_policies = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies()
                        self.directly_used_policies.parent = self
                        self._children_name_map["directly_used_policies"] = "directly-used-policies"
                        self._children_yang_names.add("directly-used-policies")

                        self.all_used_sets = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets()
                        self.all_used_sets.parent = self
                        self._children_name_map["all_used_sets"] = "all-used-sets"
                        self._children_yang_names.add("all-used-sets")

                        self.directly_used_sets = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets()
                        self.directly_used_sets.parent = self
                        self._children_name_map["directly_used_sets"] = "directly-used-sets"
                        self._children_yang_names.add("directly-used-sets")

                        self.all_used_policies = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies()
                        self.all_used_policies.parent = self
                        self._children_name_map["all_used_policies"] = "all-used-policies"
                        self._children_yang_names.add("all-used-policies")
                        self._segment_path = lambda: "policy-uses"


                    class DirectlyUsedPolicies(Entity):
                        """
                        Policies that this policy uses directly
                        
                        .. attribute:: object
                        
                        	Policy objects
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies, self).__init__()

                            self.yang_name = "directly-used-policies"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('object', YLeafList(YType.str, 'object')),
                            ])
                            self.object = []
                            self._segment_path = lambda: "directly-used-policies"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies, ['object'], name, value)


                    class AllUsedSets(Entity):
                        """
                        Sets used by this policy, or by policies
                        that it uses
                        
                        .. attribute:: sets
                        
                        	List of sets in several domains
                        	**type**\: list of  		 :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets, self).__init__()

                            self.yang_name = "all-used-sets"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets))])
                            self._leafs = OrderedDict()

                            self.sets = YList(self)
                            self._segment_path = lambda: "all-used-sets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets, [], name, value)


                        class Sets(Entity):
                            """
                            List of sets in several domains
                            
                            .. attribute:: set_domain
                            
                            	Domain of sets
                            	**type**\: str
                            
                            .. attribute:: set_name
                            
                            	Names of sets in this domain
                            	**type**\: list of str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets, self).__init__()

                                self.yang_name = "sets"
                                self.yang_parent_name = "all-used-sets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('set_domain', YLeaf(YType.str, 'set-domain')),
                                    ('set_name', YLeafList(YType.str, 'set-name')),
                                ])
                                self.set_domain = None
                                self.set_name = []
                                self._segment_path = lambda: "sets"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets, ['set_domain', 'set_name'], name, value)


                    class DirectlyUsedSets(Entity):
                        """
                        Sets that this policy uses directly
                        
                        .. attribute:: sets
                        
                        	List of sets in several domains
                        	**type**\: list of  		 :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets, self).__init__()

                            self.yang_name = "directly-used-sets"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets))])
                            self._leafs = OrderedDict()

                            self.sets = YList(self)
                            self._segment_path = lambda: "directly-used-sets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets, [], name, value)


                        class Sets(Entity):
                            """
                            List of sets in several domains
                            
                            .. attribute:: set_domain
                            
                            	Domain of sets
                            	**type**\: str
                            
                            .. attribute:: set_name
                            
                            	Names of sets in this domain
                            	**type**\: list of str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets, self).__init__()

                                self.yang_name = "sets"
                                self.yang_parent_name = "directly-used-sets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('set_domain', YLeaf(YType.str, 'set-domain')),
                                    ('set_name', YLeafList(YType.str, 'set-name')),
                                ])
                                self.set_domain = None
                                self.set_name = []
                                self._segment_path = lambda: "sets"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets, ['set_domain', 'set_name'], name, value)


                    class AllUsedPolicies(Entity):
                        """
                        Policies used by this policy, or by policies
                        that it uses
                        
                        .. attribute:: object
                        
                        	Policy objects
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies, self).__init__()

                            self.yang_name = "all-used-policies"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('object', YLeafList(YType.str, 'object')),
                            ])
                            self.object = []
                            self._segment_path = lambda: "all-used-policies"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies, ['object'], name, value)


                class UsedBy(Entity):
                    """
                    Policies that use this object, directly or
                    indirectly
                    
                    .. attribute:: reference
                    
                    	Information about policies referring to this object
                    	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy, self).__init__()

                        self.yang_name = "used-by"
                        self.yang_parent_name = "route-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference))])
                        self._leafs = OrderedDict()

                        self.reference = YList(self)
                        self._segment_path = lambda: "used-by"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy, [], name, value)


                    class Reference(Entity):
                        """
                        Information about policies referring to this
                        object
                        
                        .. attribute:: route_policy_name
                        
                        	Name of policy
                        	**type**\: str
                        
                        .. attribute:: used_directly
                        
                        	Whether the policy uses this object directly or indirectly
                        	**type**\: bool
                        
                        .. attribute:: status
                        
                        	Active, Inactive, or Unused
                        	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference, self).__init__()

                            self.yang_name = "reference"
                            self.yang_parent_name = "used-by"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                ('status', YLeaf(YType.enumeration, 'status')),
                            ])
                            self.route_policy_name = None
                            self.used_directly = None
                            self.status = None
                            self._segment_path = lambda: "reference"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                class Attached(Entity):
                    """
                    Information about where this policy or set is
                    attached
                    
                    .. attribute:: binding
                    
                    	bindings list
                    	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached, self).__init__()

                        self.yang_name = "attached"
                        self.yang_parent_name = "route-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding))])
                        self._leafs = OrderedDict()

                        self.binding = YList(self)
                        self._segment_path = lambda: "attached"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached, [], name, value)


                    class Binding(Entity):
                        """
                        bindings list
                        
                        .. attribute:: protocol
                        
                        	Protocol to which policy attached
                        	**type**\: str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: proto_instance
                        
                        	Protocol instance
                        	**type**\: str
                        
                        .. attribute:: af_name
                        
                        	Address Family Identifier
                        	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                        
                        .. attribute:: saf_name
                        
                        	Subsequent Address Family Identifier
                        	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor IP Address
                        	**type**\: str
                        
                        .. attribute:: neighbor_af_name
                        
                        	Neighbor IP Address Family
                        	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                        
                        .. attribute:: group_name
                        
                        	Neighbor Group Name
                        	**type**\: str
                        
                        .. attribute:: direction
                        
                        	Direction In or Out
                        	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                        
                        .. attribute:: group
                        
                        	Neighbor Group 
                        	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                        
                        .. attribute:: source_protocol
                        
                        	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                        	**type**\: str
                        
                        .. attribute:: aggregate_network_address
                        
                        	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                        	**type**\: str
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        .. attribute:: instance
                        
                        	Instance
                        	**type**\: str
                        
                        .. attribute:: area_id
                        
                        	OSPF Area ID in Decimal Integer Format
                        	**type**\: str
                        
                        .. attribute:: propogate_from
                        
                        	ISIS Propogate From Level
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: propogate_to
                        
                        	ISIS Propogate To Level
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: route_policy_name
                        
                        	Policy that uses object in question
                        	**type**\: str
                        
                        .. attribute:: attached_policy
                        
                        	The attached policy that (maybe indirectly) uses the object in question
                        	**type**\: str
                        
                        .. attribute:: attach_point
                        
                        	Name of attach point where policy is attached
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding, self).__init__()

                            self.yang_name = "binding"
                            self.yang_parent_name = "attached"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('protocol', YLeaf(YType.str, 'protocol')),
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                ('group_name', YLeaf(YType.str, 'group-name')),
                                ('direction', YLeaf(YType.enumeration, 'direction')),
                                ('group', YLeaf(YType.enumeration, 'group')),
                                ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('instance', YLeaf(YType.str, 'instance')),
                                ('area_id', YLeaf(YType.str, 'area-id')),
                                ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                ('attach_point', YLeaf(YType.str, 'attach-point')),
                            ])
                            self.protocol = None
                            self.vrf_name = None
                            self.proto_instance = None
                            self.af_name = None
                            self.saf_name = None
                            self.neighbor_address = None
                            self.neighbor_af_name = None
                            self.group_name = None
                            self.direction = None
                            self.group = None
                            self.source_protocol = None
                            self.aggregate_network_address = None
                            self.interface_name = None
                            self.instance = None
                            self.area_id = None
                            self.propogate_from = None
                            self.propogate_to = None
                            self.route_policy_name = None
                            self.attached_policy = None
                            self.attach_point = None
                            self._segment_path = lambda: "binding"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


        class Unused(Entity):
            """
            All objects of a given type that are not
            referenced at all
            
            .. attribute:: object
            
            	Policy objects
            	**type**\: list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.Unused, self).__init__()

                self.yang_name = "unused"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('object', YLeafList(YType.str, 'object')),
                ])
                self.object = []
                self._segment_path = lambda: "unused"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.Unused, ['object'], name, value)


        class Inactive(Entity):
            """
            All objects of a given type that are not
            attached to a protocol
            
            .. attribute:: object
            
            	Policy objects
            	**type**\: list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.Inactive, self).__init__()

                self.yang_name = "inactive"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('object', YLeafList(YType.str, 'object')),
                ])
                self.object = []
                self._segment_path = lambda: "inactive"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.Inactive, ['object'], name, value)


        class Active(Entity):
            """
            All objects of a given type that are attached to
            a protocol
            
            .. attribute:: object
            
            	Policy objects
            	**type**\: list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.Active, self).__init__()

                self.yang_name = "active"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('object', YLeafList(YType.str, 'object')),
                ])
                self.object = []
                self._segment_path = lambda: "active"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.Active, ['object'], name, value)


    class Sets(Entity):
        """
        Information about configured sets
        
        .. attribute:: etag
        
        	Information about Etag sets
        	**type**\:  :py:class:`Etag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag>`
        
        .. attribute:: ospf_area
        
        	Information about OSPF Area sets
        	**type**\:  :py:class:`OspfArea <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea>`
        
        .. attribute:: extended_community_opaque
        
        	Information about Extended Community Opaque sets
        	**type**\:  :py:class:`ExtendedCommunityOpaque <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque>`
        
        .. attribute:: extended_community_seg_nh
        
        	Information about Extended Community SegNH sets
        	**type**\:  :py:class:`ExtendedCommunitySegNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh>`
        
        .. attribute:: extended_community_soo
        
        	Information about Extended Community SOO sets
        	**type**\:  :py:class:`ExtendedCommunitySoo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo>`
        
        .. attribute:: tag
        
        	Information about Tag sets
        	**type**\:  :py:class:`Tag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag>`
        
        .. attribute:: prefix
        
        	Information about AS Path sets
        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix>`
        
        .. attribute:: community
        
        	Information about Community sets
        	**type**\:  :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community>`
        
        .. attribute:: as_path
        
        	Information about AS Path sets
        	**type**\:  :py:class:`AsPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath>`
        
        .. attribute:: large_community
        
        	Information about Large Community sets
        	**type**\:  :py:class:`LargeCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity>`
        
        .. attribute:: esi
        
        	Information about Esi sets
        	**type**\:  :py:class:`Esi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi>`
        
        .. attribute:: extended_community_bandwidth
        
        	Information about Extended Community Bandwidth sets
        	**type**\:  :py:class:`ExtendedCommunityBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth>`
        
        .. attribute:: extended_community_rt
        
        	Information about Extended Community RT sets
        	**type**\:  :py:class:`ExtendedCommunityRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt>`
        
        .. attribute:: rd
        
        	Information about RD sets
        	**type**\:  :py:class:`Rd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd>`
        
        .. attribute:: mac
        
        	Information about Mac sets
        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac>`
        
        .. attribute:: extended_community_cost
        
        	Information about Extended Community Cost sets
        	**type**\:  :py:class:`ExtendedCommunityCost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost>`
        
        

        """

        _prefix = 'policy-repository-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Sets, self).__init__()

            self.yang_name = "sets"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("etag", ("etag", RoutingPolicy.Sets.Etag)), ("ospf-area", ("ospf_area", RoutingPolicy.Sets.OspfArea)), ("extended-community-opaque", ("extended_community_opaque", RoutingPolicy.Sets.ExtendedCommunityOpaque)), ("extended-community-seg-nh", ("extended_community_seg_nh", RoutingPolicy.Sets.ExtendedCommunitySegNh)), ("extended-community-soo", ("extended_community_soo", RoutingPolicy.Sets.ExtendedCommunitySoo)), ("tag", ("tag", RoutingPolicy.Sets.Tag)), ("prefix", ("prefix", RoutingPolicy.Sets.Prefix)), ("community", ("community", RoutingPolicy.Sets.Community)), ("as-path", ("as_path", RoutingPolicy.Sets.AsPath)), ("large-community", ("large_community", RoutingPolicy.Sets.LargeCommunity)), ("esi", ("esi", RoutingPolicy.Sets.Esi)), ("extended-community-bandwidth", ("extended_community_bandwidth", RoutingPolicy.Sets.ExtendedCommunityBandwidth)), ("extended-community-rt", ("extended_community_rt", RoutingPolicy.Sets.ExtendedCommunityRt)), ("rd", ("rd", RoutingPolicy.Sets.Rd)), ("mac", ("mac", RoutingPolicy.Sets.Mac)), ("extended-community-cost", ("extended_community_cost", RoutingPolicy.Sets.ExtendedCommunityCost))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.etag = RoutingPolicy.Sets.Etag()
            self.etag.parent = self
            self._children_name_map["etag"] = "etag"
            self._children_yang_names.add("etag")

            self.ospf_area = RoutingPolicy.Sets.OspfArea()
            self.ospf_area.parent = self
            self._children_name_map["ospf_area"] = "ospf-area"
            self._children_yang_names.add("ospf-area")

            self.extended_community_opaque = RoutingPolicy.Sets.ExtendedCommunityOpaque()
            self.extended_community_opaque.parent = self
            self._children_name_map["extended_community_opaque"] = "extended-community-opaque"
            self._children_yang_names.add("extended-community-opaque")

            self.extended_community_seg_nh = RoutingPolicy.Sets.ExtendedCommunitySegNh()
            self.extended_community_seg_nh.parent = self
            self._children_name_map["extended_community_seg_nh"] = "extended-community-seg-nh"
            self._children_yang_names.add("extended-community-seg-nh")

            self.extended_community_soo = RoutingPolicy.Sets.ExtendedCommunitySoo()
            self.extended_community_soo.parent = self
            self._children_name_map["extended_community_soo"] = "extended-community-soo"
            self._children_yang_names.add("extended-community-soo")

            self.tag = RoutingPolicy.Sets.Tag()
            self.tag.parent = self
            self._children_name_map["tag"] = "tag"
            self._children_yang_names.add("tag")

            self.prefix = RoutingPolicy.Sets.Prefix()
            self.prefix.parent = self
            self._children_name_map["prefix"] = "prefix"
            self._children_yang_names.add("prefix")

            self.community = RoutingPolicy.Sets.Community()
            self.community.parent = self
            self._children_name_map["community"] = "community"
            self._children_yang_names.add("community")

            self.as_path = RoutingPolicy.Sets.AsPath()
            self.as_path.parent = self
            self._children_name_map["as_path"] = "as-path"
            self._children_yang_names.add("as-path")

            self.large_community = RoutingPolicy.Sets.LargeCommunity()
            self.large_community.parent = self
            self._children_name_map["large_community"] = "large-community"
            self._children_yang_names.add("large-community")

            self.esi = RoutingPolicy.Sets.Esi()
            self.esi.parent = self
            self._children_name_map["esi"] = "esi"
            self._children_yang_names.add("esi")

            self.extended_community_bandwidth = RoutingPolicy.Sets.ExtendedCommunityBandwidth()
            self.extended_community_bandwidth.parent = self
            self._children_name_map["extended_community_bandwidth"] = "extended-community-bandwidth"
            self._children_yang_names.add("extended-community-bandwidth")

            self.extended_community_rt = RoutingPolicy.Sets.ExtendedCommunityRt()
            self.extended_community_rt.parent = self
            self._children_name_map["extended_community_rt"] = "extended-community-rt"
            self._children_yang_names.add("extended-community-rt")

            self.rd = RoutingPolicy.Sets.Rd()
            self.rd.parent = self
            self._children_name_map["rd"] = "rd"
            self._children_yang_names.add("rd")

            self.mac = RoutingPolicy.Sets.Mac()
            self.mac.parent = self
            self._children_name_map["mac"] = "mac"
            self._children_yang_names.add("mac")

            self.extended_community_cost = RoutingPolicy.Sets.ExtendedCommunityCost()
            self.extended_community_cost.parent = self
            self._children_name_map["extended_community_cost"] = "extended-community-cost"
            self._children_yang_names.add("extended-community-cost")
            self._segment_path = lambda: "sets"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/%s" % self._segment_path()


        class Etag(Entity):
            """
            Information about Etag sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Etag, self).__init__()

                self.yang_name = "etag"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Etag.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Etag.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Etag.Inactive)), ("active", ("active", RoutingPolicy.Sets.Etag.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Etag.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Etag.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Etag.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Etag.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "etag"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Etag.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Etag.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Etag.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Etag.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Etag.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Etag.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Etag.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Active, ['object'], name, value)


        class OspfArea(Entity):
            """
            Information about OSPF Area sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.OspfArea, self).__init__()

                self.yang_name = "ospf-area"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.OspfArea.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.OspfArea.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.OspfArea.Inactive)), ("active", ("active", RoutingPolicy.Sets.OspfArea.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.OspfArea.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.OspfArea.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.OspfArea.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.OspfArea.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "ospf-area"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.OspfArea.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.OspfArea.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Active, ['object'], name, value)


        class ExtendedCommunityOpaque(Entity):
            """
            Information about Extended Community Opaque
            sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityOpaque, self).__init__()

                self.yang_name = "extended-community-opaque"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive)), ("active", ("active", RoutingPolicy.Sets.ExtendedCommunityOpaque.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.ExtendedCommunityOpaque.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "extended-community-opaque"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Active, ['object'], name, value)


        class ExtendedCommunitySegNh(Entity):
            """
            Information about Extended Community SegNH sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySegNh, self).__init__()

                self.yang_name = "extended-community-seg-nh"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive)), ("active", ("active", RoutingPolicy.Sets.ExtendedCommunitySegNh.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.ExtendedCommunitySegNh.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "extended-community-seg-nh"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Active, ['object'], name, value)


        class ExtendedCommunitySoo(Entity):
            """
            Information about Extended Community SOO sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySoo, self).__init__()

                self.yang_name = "extended-community-soo"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.ExtendedCommunitySoo.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive)), ("active", ("active", RoutingPolicy.Sets.ExtendedCommunitySoo.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunitySoo.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.ExtendedCommunitySoo.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "extended-community-soo"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Active, ['object'], name, value)


        class Tag(Entity):
            """
            Information about Tag sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Tag, self).__init__()

                self.yang_name = "tag"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Tag.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Tag.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Tag.Inactive)), ("active", ("active", RoutingPolicy.Sets.Tag.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Tag.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Tag.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Tag.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Tag.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "tag"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Tag.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Tag.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Tag.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Tag.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Tag.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Tag.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Tag.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Active, ['object'], name, value)


        class Prefix(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Prefix, self).__init__()

                self.yang_name = "prefix"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Prefix.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Prefix.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Prefix.Inactive)), ("active", ("active", RoutingPolicy.Sets.Prefix.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Prefix.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Prefix.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Prefix.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Prefix.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "prefix"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Prefix.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Prefix.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Prefix.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Prefix.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Prefix.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Active, ['object'], name, value)


        class Community(Entity):
            """
            Information about Community sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Community, self).__init__()

                self.yang_name = "community"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Community.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Community.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Community.Inactive)), ("active", ("active", RoutingPolicy.Sets.Community.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Community.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Community.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Community.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Community.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "community"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Community.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Community.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Community.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Community.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Community.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Community.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Community.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Community.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Community.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Community.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Community.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Active, ['object'], name, value)


        class AsPath(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AsPath, self).__init__()

                self.yang_name = "as-path"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.AsPath.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.AsPath.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.AsPath.Inactive)), ("active", ("active", RoutingPolicy.Sets.AsPath.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.AsPath.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.AsPath.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.AsPath.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.AsPath.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "as-path"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.AsPath.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.AsPath.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.AsPath.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.AsPath.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.AsPath.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Active, ['object'], name, value)


        class LargeCommunity(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.LargeCommunity, self).__init__()

                self.yang_name = "large-community"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.LargeCommunity.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.LargeCommunity.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.LargeCommunity.Inactive)), ("active", ("active", RoutingPolicy.Sets.LargeCommunity.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.LargeCommunity.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.LargeCommunity.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.LargeCommunity.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.LargeCommunity.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "large-community"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.LargeCommunity.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.LargeCommunity.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Active, ['object'], name, value)


        class Esi(Entity):
            """
            Information about Esi sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Esi, self).__init__()

                self.yang_name = "esi"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Esi.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Esi.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Esi.Inactive)), ("active", ("active", RoutingPolicy.Sets.Esi.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Esi.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Esi.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Esi.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Esi.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "esi"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Esi.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Esi.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Esi.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Esi.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Esi.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Esi.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Esi.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Active, ['object'], name, value)


        class ExtendedCommunityBandwidth(Entity):
            """
            Information about Extended Community Bandwidth
            sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityBandwidth, self).__init__()

                self.yang_name = "extended-community-bandwidth"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")
                self._segment_path = lambda: "extended-community-bandwidth"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive, ['object'], name, value)


        class ExtendedCommunityRt(Entity):
            """
            Information about Extended Community RT sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityRt, self).__init__()

                self.yang_name = "extended-community-rt"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.ExtendedCommunityRt.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.ExtendedCommunityRt.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.ExtendedCommunityRt.Inactive)), ("active", ("active", RoutingPolicy.Sets.ExtendedCommunityRt.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.ExtendedCommunityRt.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityRt.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityRt.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.ExtendedCommunityRt.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "extended-community-rt"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Active, ['object'], name, value)


        class Rd(Entity):
            """
            Information about RD sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Rd, self).__init__()

                self.yang_name = "rd"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Rd.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Rd.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Rd.Inactive)), ("active", ("active", RoutingPolicy.Sets.Rd.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Rd.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Rd.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Rd.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Rd.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "rd"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Rd.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Rd.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Rd.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Rd.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Rd.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Rd.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Rd.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Active, ['object'], name, value)


        class Mac(Entity):
            """
            Information about Mac sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Mac, self).__init__()

                self.yang_name = "mac"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.Mac.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.Mac.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.Mac.Inactive)), ("active", ("active", RoutingPolicy.Sets.Mac.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.Mac.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Mac.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.Mac.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.Mac.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "mac"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.Mac.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Mac.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.Mac.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.Mac.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Mac.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Mac.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Mac.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Active, ['object'], name, value)


        class ExtendedCommunityCost(Entity):
            """
            Information about Extended Community Cost sets
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:  :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:  :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Unused>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Inactive>`
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Active>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityCost, self).__init__()

                self.yang_name = "extended-community-cost"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("sets", ("sets", RoutingPolicy.Sets.ExtendedCommunityCost.Sets_)), ("unused", ("unused", RoutingPolicy.Sets.ExtendedCommunityCost.Unused)), ("inactive", ("inactive", RoutingPolicy.Sets.ExtendedCommunityCost.Inactive)), ("active", ("active", RoutingPolicy.Sets.ExtendedCommunityCost.Active))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.sets = RoutingPolicy.Sets.ExtendedCommunityCost.Sets_()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityCost.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityCost.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.active = RoutingPolicy.Sets.ExtendedCommunityCost.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")
                self._segment_path = lambda: "extended-community-cost"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Sets_(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of  		 :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("set", ("set", RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set))])
                    self._leafs = OrderedDict()

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  (key)
                    
                    	Set name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:  :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy>`
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:  :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['set_name']
                        self._child_container_classes = OrderedDict([("used-by", ("used_by", RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy)), ("attached", ("attached", RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('set_name', YLeaf(YType.str, 'set-name')),
                        ])
                        self.set_name = None

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")
                        self._segment_path = lambda: "set" + "[set-name='" + str(self.set_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set, ['set_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of  		 :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("reference", ("reference", RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference))])
                            self._leafs = OrderedDict()

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\: str
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\: bool
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:  :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('used_directly', YLeaf(YType.boolean, 'used-directly')),
                                    ('status', YLeaf(YType.enumeration, 'status')),
                                ])
                                self.route_policy_name = None
                                self.used_directly = None
                                self.status = None
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference, ['route_policy_name', 'used_directly', 'status'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("binding", ("binding", RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding))])
                            self._leafs = OrderedDict()

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\: str
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:  :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\: str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\: str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:  :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:  :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\: str
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\: str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\: str
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\: str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\: str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('protocol', YLeaf(YType.str, 'protocol')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('proto_instance', YLeaf(YType.str, 'proto-instance')),
                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ('saf_name', YLeaf(YType.enumeration, 'saf-name')),
                                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                                    ('neighbor_af_name', YLeaf(YType.enumeration, 'neighbor-af-name')),
                                    ('group_name', YLeaf(YType.str, 'group-name')),
                                    ('direction', YLeaf(YType.enumeration, 'direction')),
                                    ('group', YLeaf(YType.enumeration, 'group')),
                                    ('source_protocol', YLeaf(YType.str, 'source-protocol')),
                                    ('aggregate_network_address', YLeaf(YType.str, 'aggregate-network-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('instance', YLeaf(YType.str, 'instance')),
                                    ('area_id', YLeaf(YType.str, 'area-id')),
                                    ('propogate_from', YLeaf(YType.int32, 'propogate-from')),
                                    ('propogate_to', YLeaf(YType.int32, 'propogate-to')),
                                    ('route_policy_name', YLeaf(YType.str, 'route-policy-name')),
                                    ('attached_policy', YLeaf(YType.str, 'attached-policy')),
                                    ('attach_point', YLeaf(YType.str, 'attach-point')),
                                ])
                                self.protocol = None
                                self.vrf_name = None
                                self.proto_instance = None
                                self.af_name = None
                                self.saf_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.group_name = None
                                self.direction = None
                                self.group = None
                                self.source_protocol = None
                                self.aggregate_network_address = None
                                self.interface_name = None
                                self.instance = None
                                self.area_id = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.route_policy_name = None
                                self.attached_policy = None
                                self.attach_point = None
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding, ['protocol', 'vrf_name', 'proto_instance', 'af_name', 'saf_name', 'neighbor_address', 'neighbor_af_name', 'group_name', 'direction', 'group', 'source_protocol', 'aggregate_network_address', 'interface_name', 'instance', 'area_id', 'propogate_from', 'propogate_to', 'route_policy_name', 'attached_policy', 'attach_point'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Unused, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Inactive, ['object'], name, value)


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\: list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object', YLeafList(YType.str, 'object')),
                    ])
                    self.object = []
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Active, ['object'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

