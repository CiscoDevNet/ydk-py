""" Cisco_IOS_XR_policy_repository_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package operational data.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AddressFamily(Enum):
    """
    AddressFamily

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
    AttachPointDirection

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
    Group

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
    ObjectStatus

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
    SubAddressFamily

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

    .. data:: saf_none = 11

    	No SAFI

    .. data:: saf_unknown = 12

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

    saf_none = Enum.YLeaf(11, "saf-none")

    saf_unknown = Enum.YLeaf(12, "saf-unknown")



class RoutingPolicy(Entity):
    """
    Routing policy operational data
    
    .. attribute:: limits
    
    	Information about configured limits and the current values
    	**type**\:   :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Limits>`
    
    .. attribute:: policies
    
    	Information about configured route policies
    	**type**\:   :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies>`
    
    .. attribute:: sets
    
    	Information about configured sets
    	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets>`
    
    

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
        self._child_container_classes = {"limits" : ("limits", RoutingPolicy.Limits), "policies" : ("policies", RoutingPolicy.Policies), "sets" : ("sets", RoutingPolicy.Sets)}
        self._child_list_classes = {}

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
        
        .. attribute:: compiled_policies_length
        
        	The total compiled length of all policies
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_lines_of_policy_limit
        
        	Number of lines of configuration for policies/sets currently allowed
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_lines_of_policy_used
        
        	Current number of lines configured for all policies and sets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_number_of_policies_limit
        
        	Number of policies currently allowed
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_number_of_policies_used
        
        	Current number of policies configured
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: maximum_lines_of_policy
        
        	Maximum lines of configuration allowable for all policies and sets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: maximum_number_of_policies
        
        	Maximum number of policies allowable
        	**type**\:  int
        
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.compiled_policies_length = YLeaf(YType.uint32, "compiled-policies-length")

            self.current_lines_of_policy_limit = YLeaf(YType.uint32, "current-lines-of-policy-limit")

            self.current_lines_of_policy_used = YLeaf(YType.uint32, "current-lines-of-policy-used")

            self.current_number_of_policies_limit = YLeaf(YType.uint32, "current-number-of-policies-limit")

            self.current_number_of_policies_used = YLeaf(YType.uint32, "current-number-of-policies-used")

            self.maximum_lines_of_policy = YLeaf(YType.uint32, "maximum-lines-of-policy")

            self.maximum_number_of_policies = YLeaf(YType.uint32, "maximum-number-of-policies")
            self._segment_path = lambda: "limits"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.Limits, ['compiled_policies_length', 'current_lines_of_policy_limit', 'current_lines_of_policy_used', 'current_number_of_policies_limit', 'current_number_of_policies_used', 'maximum_lines_of_policy', 'maximum_number_of_policies'], name, value)


    class Policies(Entity):
        """
        Information about configured route policies
        
        .. attribute:: active
        
        	All objects of a given type that are attached to a protocol
        	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.Active>`
        
        .. attribute:: inactive
        
        	All objects of a given type that are not attached to a protocol
        	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.Inactive>`
        
        .. attribute:: route_policies
        
        	Information about individual policies
        	**type**\:   :py:class:`RoutePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies>`
        
        .. attribute:: unused
        
        	All objects of a given type that are not referenced at all
        	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.Unused>`
        
        

        """

        _prefix = 'policy-repository-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Policies, self).__init__()

            self.yang_name = "policies"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"active" : ("active", RoutingPolicy.Policies.Active), "inactive" : ("inactive", RoutingPolicy.Policies.Inactive), "route-policies" : ("route_policies", RoutingPolicy.Policies.RoutePolicies), "unused" : ("unused", RoutingPolicy.Policies.Unused)}
            self._child_list_classes = {}

            self.active = RoutingPolicy.Policies.Active()
            self.active.parent = self
            self._children_name_map["active"] = "active"
            self._children_yang_names.add("active")

            self.inactive = RoutingPolicy.Policies.Inactive()
            self.inactive.parent = self
            self._children_name_map["inactive"] = "inactive"
            self._children_yang_names.add("inactive")

            self.route_policies = RoutingPolicy.Policies.RoutePolicies()
            self.route_policies.parent = self
            self._children_name_map["route_policies"] = "route-policies"
            self._children_yang_names.add("route-policies")

            self.unused = RoutingPolicy.Policies.Unused()
            self.unused.parent = self
            self._children_name_map["unused"] = "unused"
            self._children_yang_names.add("unused")
            self._segment_path = lambda: "policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/%s" % self._segment_path()


        class Active(Entity):
            """
            All objects of a given type that are attached to
            a protocol
            
            .. attribute:: object
            
            	Policy objects
            	**type**\:  list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.Active, self).__init__()

                self.yang_name = "active"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.object = YLeafList(YType.str, "object")
                self._segment_path = lambda: "active"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.Active, ['object'], name, value)


        class Inactive(Entity):
            """
            All objects of a given type that are not
            attached to a protocol
            
            .. attribute:: object
            
            	Policy objects
            	**type**\:  list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.Inactive, self).__init__()

                self.yang_name = "inactive"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.object = YLeafList(YType.str, "object")
                self._segment_path = lambda: "inactive"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.Inactive, ['object'], name, value)


        class RoutePolicies(Entity):
            """
            Information about individual policies
            
            .. attribute:: route_policy
            
            	Information about an individual policy
            	**type**\: list of    :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.RoutePolicies, self).__init__()

                self.yang_name = "route-policies"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"route-policy" : ("route_policy", RoutingPolicy.Policies.RoutePolicies.RoutePolicy)}

                self.route_policy = YList(self)
                self._segment_path = lambda: "route-policies"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.RoutePolicies, [], name, value)


            class RoutePolicy(Entity):
                """
                Information about an individual policy
                
                .. attribute:: route_policy_name  <key>
                
                	Route policy name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: attached
                
                	Information about where this policy or set is attached
                	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached>`
                
                .. attribute:: policy_uses
                
                	Information about which policies and sets this policy uses
                	**type**\:   :py:class:`PolicyUses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses>`
                
                .. attribute:: used_by
                
                	Policies that use this object, directly or indirectly
                	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy, self).__init__()

                    self.yang_name = "route-policy"
                    self.yang_parent_name = "route-policies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached), "policy-uses" : ("policy_uses", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses), "used-by" : ("used_by", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy)}
                    self._child_list_classes = {}

                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                    self.attached = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached()
                    self.attached.parent = self
                    self._children_name_map["attached"] = "attached"
                    self._children_yang_names.add("attached")

                    self.policy_uses = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses()
                    self.policy_uses.parent = self
                    self._children_name_map["policy_uses"] = "policy-uses"
                    self._children_yang_names.add("policy-uses")

                    self.used_by = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy()
                    self.used_by.parent = self
                    self._children_name_map["used_by"] = "used-by"
                    self._children_yang_names.add("used-by")
                    self._segment_path = lambda: "route-policy" + "[route-policy-name='" + self.route_policy_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/route-policies/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy, ['route_policy_name'], name, value)


                class Attached(Entity):
                    """
                    Information about where this policy or set is
                    attached
                    
                    .. attribute:: binding
                    
                    	bindings list
                    	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached, self).__init__()

                        self.yang_name = "attached"
                        self.yang_parent_name = "route-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding)}

                        self.binding = YList(self)
                        self._segment_path = lambda: "attached"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached, [], name, value)


                    class Binding(Entity):
                        """
                        bindings list
                        
                        .. attribute:: af_name
                        
                        	Address Family Identifier
                        	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                        
                        .. attribute:: aggregate_network_address
                        
                        	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                        	**type**\:  str
                        
                        .. attribute:: area_id
                        
                        	OSPF Area ID in Decimal Integer Format
                        	**type**\:  str
                        
                        .. attribute:: attach_point
                        
                        	Name of attach point where policy is attached
                        	**type**\:  str
                        
                        .. attribute:: attached_policy
                        
                        	The attached policy that (maybe indirectly) uses the object in question
                        	**type**\:  str
                        
                        .. attribute:: direction
                        
                        	Direction In or Out
                        	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                        
                        .. attribute:: group
                        
                        	Neighbor Group 
                        	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                        
                        .. attribute:: group_name
                        
                        	Neighbor Group Name
                        	**type**\:  str
                        
                        .. attribute:: instance
                        
                        	Instance
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor IP Address
                        	**type**\:  str
                        
                        .. attribute:: neighbor_af_name
                        
                        	Neighbor IP Address Family
                        	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                        
                        .. attribute:: propogate_from
                        
                        	ISIS Propogate From Level
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: propogate_to
                        
                        	ISIS Propogate To Level
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: proto_instance
                        
                        	Protocol instance
                        	**type**\:  str
                        
                        .. attribute:: protocol
                        
                        	Protocol to which policy attached
                        	**type**\:  str
                        
                        .. attribute:: route_policy_name
                        
                        	Policy that uses object in question
                        	**type**\:  str
                        
                        .. attribute:: saf_name
                        
                        	Subsequent Address Family Identifier
                        	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                        
                        .. attribute:: source_protocol
                        
                        	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding, self).__init__()

                            self.yang_name = "binding"
                            self.yang_parent_name = "attached"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                            self.area_id = YLeaf(YType.str, "area-id")

                            self.attach_point = YLeaf(YType.str, "attach-point")

                            self.attached_policy = YLeaf(YType.str, "attached-policy")

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.group = YLeaf(YType.enumeration, "group")

                            self.group_name = YLeaf(YType.str, "group-name")

                            self.instance = YLeaf(YType.str, "instance")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                            self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                            self.propogate_from = YLeaf(YType.int32, "propogate-from")

                            self.propogate_to = YLeaf(YType.int32, "propogate-to")

                            self.proto_instance = YLeaf(YType.str, "proto-instance")

                            self.protocol = YLeaf(YType.str, "protocol")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                            self.saf_name = YLeaf(YType.enumeration, "saf-name")

                            self.source_protocol = YLeaf(YType.str, "source-protocol")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "binding"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                class PolicyUses(Entity):
                    """
                    Information about which policies and sets
                    this policy uses
                    
                    .. attribute:: all_used_policies
                    
                    	Policies used by this policy, or by policies that it uses
                    	**type**\:   :py:class:`AllUsedPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies>`
                    
                    .. attribute:: all_used_sets
                    
                    	Sets used by this policy, or by policies that it uses
                    	**type**\:   :py:class:`AllUsedSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets>`
                    
                    .. attribute:: directly_used_policies
                    
                    	Policies that this policy uses directly
                    	**type**\:   :py:class:`DirectlyUsedPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies>`
                    
                    .. attribute:: directly_used_sets
                    
                    	Sets that this policy uses directly
                    	**type**\:   :py:class:`DirectlyUsedSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses, self).__init__()

                        self.yang_name = "policy-uses"
                        self.yang_parent_name = "route-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"all-used-policies" : ("all_used_policies", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies), "all-used-sets" : ("all_used_sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets), "directly-used-policies" : ("directly_used_policies", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies), "directly-used-sets" : ("directly_used_sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets)}
                        self._child_list_classes = {}

                        self.all_used_policies = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies()
                        self.all_used_policies.parent = self
                        self._children_name_map["all_used_policies"] = "all-used-policies"
                        self._children_yang_names.add("all-used-policies")

                        self.all_used_sets = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets()
                        self.all_used_sets.parent = self
                        self._children_name_map["all_used_sets"] = "all-used-sets"
                        self._children_yang_names.add("all-used-sets")

                        self.directly_used_policies = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies()
                        self.directly_used_policies.parent = self
                        self._children_name_map["directly_used_policies"] = "directly-used-policies"
                        self._children_yang_names.add("directly-used-policies")

                        self.directly_used_sets = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets()
                        self.directly_used_sets.parent = self
                        self._children_name_map["directly_used_sets"] = "directly-used-sets"
                        self._children_yang_names.add("directly-used-sets")
                        self._segment_path = lambda: "policy-uses"


                    class AllUsedPolicies(Entity):
                        """
                        Policies used by this policy, or by policies
                        that it uses
                        
                        .. attribute:: object
                        
                        	Policy objects
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies, self).__init__()

                            self.yang_name = "all-used-policies"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.object = YLeafList(YType.str, "object")
                            self._segment_path = lambda: "all-used-policies"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies, ['object'], name, value)


                    class AllUsedSets(Entity):
                        """
                        Sets used by this policy, or by policies
                        that it uses
                        
                        .. attribute:: sets
                        
                        	List of sets in several domains
                        	**type**\: list of    :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets, self).__init__()

                            self.yang_name = "all-used-sets"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sets" : ("sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets)}

                            self.sets = YList(self)
                            self._segment_path = lambda: "all-used-sets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets, [], name, value)


                        class Sets(Entity):
                            """
                            List of sets in several domains
                            
                            .. attribute:: set_domain
                            
                            	Domain of sets
                            	**type**\:  str
                            
                            .. attribute:: set_name
                            
                            	Names of sets in this domain
                            	**type**\:  list of str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets, self).__init__()

                                self.yang_name = "sets"
                                self.yang_parent_name = "all-used-sets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.set_domain = YLeaf(YType.str, "set-domain")

                                self.set_name = YLeafList(YType.str, "set-name")
                                self._segment_path = lambda: "sets"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets, ['set_domain', 'set_name'], name, value)


                    class DirectlyUsedPolicies(Entity):
                        """
                        Policies that this policy uses directly
                        
                        .. attribute:: object
                        
                        	Policy objects
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies, self).__init__()

                            self.yang_name = "directly-used-policies"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.object = YLeafList(YType.str, "object")
                            self._segment_path = lambda: "directly-used-policies"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies, ['object'], name, value)


                    class DirectlyUsedSets(Entity):
                        """
                        Sets that this policy uses directly
                        
                        .. attribute:: sets
                        
                        	List of sets in several domains
                        	**type**\: list of    :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets, self).__init__()

                            self.yang_name = "directly-used-sets"
                            self.yang_parent_name = "policy-uses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sets" : ("sets", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets)}

                            self.sets = YList(self)
                            self._segment_path = lambda: "directly-used-sets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets, [], name, value)


                        class Sets(Entity):
                            """
                            List of sets in several domains
                            
                            .. attribute:: set_domain
                            
                            	Domain of sets
                            	**type**\:  str
                            
                            .. attribute:: set_name
                            
                            	Names of sets in this domain
                            	**type**\:  list of str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets, self).__init__()

                                self.yang_name = "sets"
                                self.yang_parent_name = "directly-used-sets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.set_domain = YLeaf(YType.str, "set-domain")

                                self.set_name = YLeafList(YType.str, "set-name")
                                self._segment_path = lambda: "sets"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets, ['set_domain', 'set_name'], name, value)


                class UsedBy(Entity):
                    """
                    Policies that use this object, directly or
                    indirectly
                    
                    .. attribute:: reference
                    
                    	Information about policies referring to this object
                    	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy, self).__init__()

                        self.yang_name = "used-by"
                        self.yang_parent_name = "route-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference)}

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
                        	**type**\:  str
                        
                        .. attribute:: status
                        
                        	Active, Inactive, or Unused
                        	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                        
                        .. attribute:: used_directly
                        
                        	Whether the policy uses this object directly or indirectly
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference, self).__init__()

                            self.yang_name = "reference"
                            self.yang_parent_name = "used-by"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.used_directly = YLeaf(YType.boolean, "used-directly")
                            self._segment_path = lambda: "reference"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


        class Unused(Entity):
            """
            All objects of a given type that are not
            referenced at all
            
            .. attribute:: object
            
            	Policy objects
            	**type**\:  list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Policies.Unused, self).__init__()

                self.yang_name = "unused"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.object = YLeafList(YType.str, "object")
                self._segment_path = lambda: "unused"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Policies.Unused, ['object'], name, value)


    class Sets(Entity):
        """
        Information about configured sets
        
        .. attribute:: as_path
        
        	Information about AS Path sets
        	**type**\:   :py:class:`AsPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath>`
        
        .. attribute:: community
        
        	Information about Community sets
        	**type**\:   :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community>`
        
        .. attribute:: esi
        
        	Information about Esi sets
        	**type**\:   :py:class:`Esi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi>`
        
        .. attribute:: etag
        
        	Information about Etag sets
        	**type**\:   :py:class:`Etag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag>`
        
        .. attribute:: extended_community_bandwidth
        
        	Information about Extended Community Bandwidth sets
        	**type**\:   :py:class:`ExtendedCommunityBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth>`
        
        .. attribute:: extended_community_cost
        
        	Information about Extended Community Cost sets
        	**type**\:   :py:class:`ExtendedCommunityCost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost>`
        
        .. attribute:: extended_community_opaque
        
        	Information about Extended Community Opaque sets
        	**type**\:   :py:class:`ExtendedCommunityOpaque <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque>`
        
        .. attribute:: extended_community_rt
        
        	Information about Extended Community RT sets
        	**type**\:   :py:class:`ExtendedCommunityRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt>`
        
        .. attribute:: extended_community_seg_nh
        
        	Information about Extended Community SegNH sets
        	**type**\:   :py:class:`ExtendedCommunitySegNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh>`
        
        .. attribute:: extended_community_soo
        
        	Information about Extended Community SOO sets
        	**type**\:   :py:class:`ExtendedCommunitySoo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo>`
        
        .. attribute:: large_community
        
        	Information about Large Community sets
        	**type**\:   :py:class:`LargeCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity>`
        
        .. attribute:: mac
        
        	Information about Mac sets
        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac>`
        
        .. attribute:: ospf_area
        
        	Information about OSPF Area sets
        	**type**\:   :py:class:`OspfArea <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea>`
        
        .. attribute:: prefix
        
        	Information about AS Path sets
        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix>`
        
        .. attribute:: rd
        
        	Information about RD sets
        	**type**\:   :py:class:`Rd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd>`
        
        .. attribute:: tag
        
        	Information about Tag sets
        	**type**\:   :py:class:`Tag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag>`
        
        

        """

        _prefix = 'policy-repository-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Sets, self).__init__()

            self.yang_name = "sets"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"as-path" : ("as_path", RoutingPolicy.Sets.AsPath), "community" : ("community", RoutingPolicy.Sets.Community), "esi" : ("esi", RoutingPolicy.Sets.Esi), "etag" : ("etag", RoutingPolicy.Sets.Etag), "extended-community-bandwidth" : ("extended_community_bandwidth", RoutingPolicy.Sets.ExtendedCommunityBandwidth), "extended-community-cost" : ("extended_community_cost", RoutingPolicy.Sets.ExtendedCommunityCost), "extended-community-opaque" : ("extended_community_opaque", RoutingPolicy.Sets.ExtendedCommunityOpaque), "extended-community-rt" : ("extended_community_rt", RoutingPolicy.Sets.ExtendedCommunityRt), "extended-community-seg-nh" : ("extended_community_seg_nh", RoutingPolicy.Sets.ExtendedCommunitySegNh), "extended-community-soo" : ("extended_community_soo", RoutingPolicy.Sets.ExtendedCommunitySoo), "large-community" : ("large_community", RoutingPolicy.Sets.LargeCommunity), "mac" : ("mac", RoutingPolicy.Sets.Mac), "ospf-area" : ("ospf_area", RoutingPolicy.Sets.OspfArea), "prefix" : ("prefix", RoutingPolicy.Sets.Prefix), "rd" : ("rd", RoutingPolicy.Sets.Rd), "tag" : ("tag", RoutingPolicy.Sets.Tag)}
            self._child_list_classes = {}

            self.as_path = RoutingPolicy.Sets.AsPath()
            self.as_path.parent = self
            self._children_name_map["as_path"] = "as-path"
            self._children_yang_names.add("as-path")

            self.community = RoutingPolicy.Sets.Community()
            self.community.parent = self
            self._children_name_map["community"] = "community"
            self._children_yang_names.add("community")

            self.esi = RoutingPolicy.Sets.Esi()
            self.esi.parent = self
            self._children_name_map["esi"] = "esi"
            self._children_yang_names.add("esi")

            self.etag = RoutingPolicy.Sets.Etag()
            self.etag.parent = self
            self._children_name_map["etag"] = "etag"
            self._children_yang_names.add("etag")

            self.extended_community_bandwidth = RoutingPolicy.Sets.ExtendedCommunityBandwidth()
            self.extended_community_bandwidth.parent = self
            self._children_name_map["extended_community_bandwidth"] = "extended-community-bandwidth"
            self._children_yang_names.add("extended-community-bandwidth")

            self.extended_community_cost = RoutingPolicy.Sets.ExtendedCommunityCost()
            self.extended_community_cost.parent = self
            self._children_name_map["extended_community_cost"] = "extended-community-cost"
            self._children_yang_names.add("extended-community-cost")

            self.extended_community_opaque = RoutingPolicy.Sets.ExtendedCommunityOpaque()
            self.extended_community_opaque.parent = self
            self._children_name_map["extended_community_opaque"] = "extended-community-opaque"
            self._children_yang_names.add("extended-community-opaque")

            self.extended_community_rt = RoutingPolicy.Sets.ExtendedCommunityRt()
            self.extended_community_rt.parent = self
            self._children_name_map["extended_community_rt"] = "extended-community-rt"
            self._children_yang_names.add("extended-community-rt")

            self.extended_community_seg_nh = RoutingPolicy.Sets.ExtendedCommunitySegNh()
            self.extended_community_seg_nh.parent = self
            self._children_name_map["extended_community_seg_nh"] = "extended-community-seg-nh"
            self._children_yang_names.add("extended-community-seg-nh")

            self.extended_community_soo = RoutingPolicy.Sets.ExtendedCommunitySoo()
            self.extended_community_soo.parent = self
            self._children_name_map["extended_community_soo"] = "extended-community-soo"
            self._children_yang_names.add("extended-community-soo")

            self.large_community = RoutingPolicy.Sets.LargeCommunity()
            self.large_community.parent = self
            self._children_name_map["large_community"] = "large-community"
            self._children_yang_names.add("large-community")

            self.mac = RoutingPolicy.Sets.Mac()
            self.mac.parent = self
            self._children_name_map["mac"] = "mac"
            self._children_yang_names.add("mac")

            self.ospf_area = RoutingPolicy.Sets.OspfArea()
            self.ospf_area.parent = self
            self._children_name_map["ospf_area"] = "ospf-area"
            self._children_yang_names.add("ospf-area")

            self.prefix = RoutingPolicy.Sets.Prefix()
            self.prefix.parent = self
            self._children_name_map["prefix"] = "prefix"
            self._children_yang_names.add("prefix")

            self.rd = RoutingPolicy.Sets.Rd()
            self.rd.parent = self
            self._children_name_map["rd"] = "rd"
            self._children_yang_names.add("rd")

            self.tag = RoutingPolicy.Sets.Tag()
            self.tag.parent = self
            self._children_name_map["tag"] = "tag"
            self._children_yang_names.add("tag")
            self._segment_path = lambda: "sets"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/%s" % self._segment_path()


        class AsPath(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AsPath, self).__init__()

                self.yang_name = "as-path"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.AsPath.Active), "inactive" : ("inactive", RoutingPolicy.Sets.AsPath.Inactive), "sets" : ("sets", RoutingPolicy.Sets.AsPath.Sets), "unused" : ("unused", RoutingPolicy.Sets.AsPath.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.AsPath.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.AsPath.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.AsPath.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.AsPath.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "as-path"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.AsPath.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.AsPath.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.AsPath.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.AsPath.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.AsPath.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.AsPath.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.AsPath.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.AsPath.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPath.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "as-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/as-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPath.Unused, ['object'], name, value)


        class Community(Entity):
            """
            Information about Community sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Community, self).__init__()

                self.yang_name = "community"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Community.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Community.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Community.Sets), "unused" : ("unused", RoutingPolicy.Sets.Community.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Community.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Community.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Community.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Community.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "community"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Community.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Community.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Community.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Community.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Community.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Community.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Community.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Community.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Community.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Community.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Community.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Community.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Community.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Community.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Community.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Community.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Community.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Community.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Community.Unused, ['object'], name, value)


        class Esi(Entity):
            """
            Information about Esi sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Esi, self).__init__()

                self.yang_name = "esi"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Esi.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Esi.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Esi.Sets), "unused" : ("unused", RoutingPolicy.Sets.Esi.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Esi.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Esi.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Esi.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Esi.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "esi"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Esi.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Esi.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Esi.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Esi.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Esi.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Esi.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Esi.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Esi.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Esi.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Esi.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Esi.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Esi.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Esi.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Esi.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Esi.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Esi.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Esi.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Esi.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "esi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/esi/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Esi.Unused, ['object'], name, value)


        class Etag(Entity):
            """
            Information about Etag sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Etag, self).__init__()

                self.yang_name = "etag"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Etag.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Etag.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Etag.Sets), "unused" : ("unused", RoutingPolicy.Sets.Etag.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Etag.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Etag.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Etag.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Etag.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "etag"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Etag.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Etag.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Etag.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Etag.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Etag.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Etag.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Etag.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Etag.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Etag.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Etag.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Etag.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Etag.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Etag.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Etag.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Etag.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Etag.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Etag.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Etag.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "etag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/etag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Etag.Unused, ['object'], name, value)


        class ExtendedCommunityBandwidth(Entity):
            """
            Information about Extended Community Bandwidth
            sets
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityBandwidth, self).__init__()

                self.yang_name = "extended-community-bandwidth"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"inactive" : ("inactive", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive), "sets" : ("sets", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets), "unused" : ("unused", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused)}
                self._child_list_classes = {}

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "extended-community-bandwidth"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused, ['object'], name, value)


        class ExtendedCommunityCost(Entity):
            """
            Information about Extended Community Cost sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityCost, self).__init__()

                self.yang_name = "extended-community-cost"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.ExtendedCommunityCost.Active), "inactive" : ("inactive", RoutingPolicy.Sets.ExtendedCommunityCost.Inactive), "sets" : ("sets", RoutingPolicy.Sets.ExtendedCommunityCost.Sets), "unused" : ("unused", RoutingPolicy.Sets.ExtendedCommunityCost.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.ExtendedCommunityCost.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityCost.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.ExtendedCommunityCost.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityCost.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "extended-community-cost"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCost.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-cost"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-cost/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCost.Unused, ['object'], name, value)


        class ExtendedCommunityOpaque(Entity):
            """
            Information about Extended Community Opaque
            sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityOpaque, self).__init__()

                self.yang_name = "extended-community-opaque"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.ExtendedCommunityOpaque.Active), "inactive" : ("inactive", RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive), "sets" : ("sets", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets), "unused" : ("unused", RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.ExtendedCommunityOpaque.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "extended-community-opaque"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-opaque"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-opaque/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused, ['object'], name, value)


        class ExtendedCommunityRt(Entity):
            """
            Information about Extended Community RT sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityRt, self).__init__()

                self.yang_name = "extended-community-rt"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.ExtendedCommunityRt.Active), "inactive" : ("inactive", RoutingPolicy.Sets.ExtendedCommunityRt.Inactive), "sets" : ("sets", RoutingPolicy.Sets.ExtendedCommunityRt.Sets), "unused" : ("unused", RoutingPolicy.Sets.ExtendedCommunityRt.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.ExtendedCommunityRt.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunityRt.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.ExtendedCommunityRt.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunityRt.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "extended-community-rt"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRt.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-rt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-rt/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRt.Unused, ['object'], name, value)


        class ExtendedCommunitySegNh(Entity):
            """
            Information about Extended Community SegNH sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySegNh, self).__init__()

                self.yang_name = "extended-community-seg-nh"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.ExtendedCommunitySegNh.Active), "inactive" : ("inactive", RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive), "sets" : ("sets", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets), "unused" : ("unused", RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.ExtendedCommunitySegNh.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "extended-community-seg-nh"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-seg-nh"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-seg-nh/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused, ['object'], name, value)


        class ExtendedCommunitySoo(Entity):
            """
            Information about Extended Community SOO sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySoo, self).__init__()

                self.yang_name = "extended-community-soo"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.ExtendedCommunitySoo.Active), "inactive" : ("inactive", RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive), "sets" : ("sets", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets), "unused" : ("unused", RoutingPolicy.Sets.ExtendedCommunitySoo.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.ExtendedCommunitySoo.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.ExtendedCommunitySoo.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "extended-community-soo"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySoo.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "extended-community-soo"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/extended-community-soo/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySoo.Unused, ['object'], name, value)


        class LargeCommunity(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.LargeCommunity, self).__init__()

                self.yang_name = "large-community"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.LargeCommunity.Active), "inactive" : ("inactive", RoutingPolicy.Sets.LargeCommunity.Inactive), "sets" : ("sets", RoutingPolicy.Sets.LargeCommunity.Sets), "unused" : ("unused", RoutingPolicy.Sets.LargeCommunity.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.LargeCommunity.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.LargeCommunity.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.LargeCommunity.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.LargeCommunity.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "large-community"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.LargeCommunity.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.LargeCommunity.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunity.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "large-community"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/large-community/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunity.Unused, ['object'], name, value)


        class Mac(Entity):
            """
            Information about Mac sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Mac, self).__init__()

                self.yang_name = "mac"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Mac.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Mac.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Mac.Sets), "unused" : ("unused", RoutingPolicy.Sets.Mac.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Mac.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Mac.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Mac.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Mac.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "mac"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Mac.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Mac.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Mac.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Mac.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Mac.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Mac.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Mac.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Mac.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Mac.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Mac.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Mac.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Mac.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Mac.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Mac.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Mac.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Mac.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Mac.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Mac.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "mac"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/mac/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Mac.Unused, ['object'], name, value)


        class OspfArea(Entity):
            """
            Information about OSPF Area sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.OspfArea, self).__init__()

                self.yang_name = "ospf-area"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.OspfArea.Active), "inactive" : ("inactive", RoutingPolicy.Sets.OspfArea.Inactive), "sets" : ("sets", RoutingPolicy.Sets.OspfArea.Sets), "unused" : ("unused", RoutingPolicy.Sets.OspfArea.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.OspfArea.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.OspfArea.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.OspfArea.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.OspfArea.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "ospf-area"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.OspfArea.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.OspfArea.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.OspfArea.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.OspfArea.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.OspfArea.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.OspfArea.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.OspfArea.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.OspfArea.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfArea.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "ospf-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/ospf-area/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfArea.Unused, ['object'], name, value)


        class Prefix(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Prefix, self).__init__()

                self.yang_name = "prefix"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Prefix.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Prefix.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Prefix.Sets), "unused" : ("unused", RoutingPolicy.Sets.Prefix.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Prefix.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Prefix.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Prefix.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Prefix.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "prefix"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Prefix.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Prefix.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Prefix.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Prefix.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Prefix.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Prefix.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Prefix.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Prefix.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Prefix.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/prefix/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Prefix.Unused, ['object'], name, value)


        class Rd(Entity):
            """
            Information about RD sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Rd, self).__init__()

                self.yang_name = "rd"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Rd.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Rd.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Rd.Sets), "unused" : ("unused", RoutingPolicy.Sets.Rd.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Rd.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Rd.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Rd.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Rd.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "rd"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Rd.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Rd.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Rd.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Rd.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Rd.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Rd.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Rd.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Rd.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Rd.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Rd.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Rd.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Rd.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Rd.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Rd.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Rd.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Rd.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Rd.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Rd.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/rd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Rd.Unused, ['object'], name, value)


        class Tag(Entity):
            """
            Information about Tag sets
            
            .. attribute:: active
            
            	All objects of a given type that are attached to a protocol
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Active>`
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.Tag, self).__init__()

                self.yang_name = "tag"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", RoutingPolicy.Sets.Tag.Active), "inactive" : ("inactive", RoutingPolicy.Sets.Tag.Inactive), "sets" : ("sets", RoutingPolicy.Sets.Tag.Sets), "unused" : ("unused", RoutingPolicy.Sets.Tag.Unused)}
                self._child_list_classes = {}

                self.active = RoutingPolicy.Sets.Tag.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.inactive = RoutingPolicy.Sets.Tag.Inactive()
                self.inactive.parent = self
                self._children_name_map["inactive"] = "inactive"
                self._children_yang_names.add("inactive")

                self.sets = RoutingPolicy.Sets.Tag.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
                self._children_yang_names.add("sets")

                self.unused = RoutingPolicy.Sets.Tag.Unused()
                self.unused.parent = self
                self._children_name_map["unused"] = "unused"
                self._children_yang_names.add("unused")
                self._segment_path = lambda: "tag"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/%s" % self._segment_path()


            class Active(Entity):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Active, ['object'], name, value)


            class Inactive(Entity):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Inactive, self).__init__()

                    self.yang_name = "inactive"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "inactive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Inactive, ['object'], name, value)


            class Sets(Entity):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Sets, self).__init__()

                    self.yang_name = "sets"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"set" : ("set", RoutingPolicy.Sets.Tag.Sets.Set)}

                    self.set = YList(self)
                    self._segment_path = lambda: "sets"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Sets, [], name, value)


                class Set(Entity):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RoutingPolicy.Sets.Tag.Sets.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"attached" : ("attached", RoutingPolicy.Sets.Tag.Sets.Set.Attached), "used-by" : ("used_by", RoutingPolicy.Sets.Tag.Sets.Set.UsedBy)}
                        self._child_list_classes = {}

                        self.set_name = YLeaf(YType.str, "set-name")

                        self.attached = RoutingPolicy.Sets.Tag.Sets.Set.Attached()
                        self.attached.parent = self
                        self._children_name_map["attached"] = "attached"
                        self._children_yang_names.add("attached")

                        self.used_by = RoutingPolicy.Sets.Tag.Sets.Set.UsedBy()
                        self.used_by.parent = self
                        self._children_name_map["used_by"] = "used-by"
                        self._children_yang_names.add("used-by")
                        self._segment_path = lambda: "set" + "[set-name='" + self.set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.Sets.Tag.Sets.Set, ['set_name'], name, value)


                    class Attached(Entity):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Tag.Sets.Set.Attached, self).__init__()

                            self.yang_name = "attached"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"binding" : ("binding", RoutingPolicy.Sets.Tag.Sets.Set.Attached.Binding)}

                            self.binding = YList(self)
                            self._segment_path = lambda: "attached"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Tag.Sets.Set.Attached, [], name, value)


                        class Binding(Entity):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address in IPv4 or IPv6 Format
                            	**type**\:  str
                            
                            .. attribute:: area_id
                            
                            	OSPF Area ID in Decimal Integer Format
                            	**type**\:  str
                            
                            .. attribute:: attach_point
                            
                            	Name of attach point where policy is attached
                            	**type**\:  str
                            
                            .. attribute:: attached_policy
                            
                            	The attached policy that (maybe indirectly) uses the object in question
                            	**type**\:  str
                            
                            .. attribute:: direction
                            
                            	Direction In or Out
                            	**type**\:   :py:class:`AttachPointDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirection>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.Group>`
                            
                            .. attribute:: group_name
                            
                            	Neighbor Group Name
                            	**type**\:  str
                            
                            .. attribute:: instance
                            
                            	Instance
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\:  str
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor IP Address
                            	**type**\:  str
                            
                            .. attribute:: neighbor_af_name
                            
                            	Neighbor IP Address Family
                            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamily>`
                            
                            .. attribute:: propogate_from
                            
                            	ISIS Propogate From Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: propogate_to
                            
                            	ISIS Propogate To Level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: proto_instance
                            
                            	Protocol instance
                            	**type**\:  str
                            
                            .. attribute:: protocol
                            
                            	Protocol to which policy attached
                            	**type**\:  str
                            
                            .. attribute:: route_policy_name
                            
                            	Policy that uses object in question
                            	**type**\:  str
                            
                            .. attribute:: saf_name
                            
                            	Subsequent Address Family Identifier
                            	**type**\:   :py:class:`SubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamily>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute, Source Protocol can be one of the following values{all, connected, local, static, bgp, rip, isis, ospf ,ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Tag.Sets.Set.Attached.Binding, self).__init__()

                                self.yang_name = "binding"
                                self.yang_parent_name = "attached"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.aggregate_network_address = YLeaf(YType.str, "aggregate-network-address")

                                self.area_id = YLeaf(YType.str, "area-id")

                                self.attach_point = YLeaf(YType.str, "attach-point")

                                self.attached_policy = YLeaf(YType.str, "attached-policy")

                                self.direction = YLeaf(YType.enumeration, "direction")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.instance = YLeaf(YType.str, "instance")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                                self.neighbor_af_name = YLeaf(YType.enumeration, "neighbor-af-name")

                                self.propogate_from = YLeaf(YType.int32, "propogate-from")

                                self.propogate_to = YLeaf(YType.int32, "propogate-to")

                                self.proto_instance = YLeaf(YType.str, "proto-instance")

                                self.protocol = YLeaf(YType.str, "protocol")

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.source_protocol = YLeaf(YType.str, "source-protocol")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "binding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Tag.Sets.Set.Attached.Binding, ['af_name', 'aggregate_network_address', 'area_id', 'attach_point', 'attached_policy', 'direction', 'group', 'group_name', 'instance', 'interface_name', 'neighbor_address', 'neighbor_af_name', 'propogate_from', 'propogate_to', 'proto_instance', 'protocol', 'route_policy_name', 'saf_name', 'source_protocol', 'vrf_name'], name, value)


                    class UsedBy(Entity):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(RoutingPolicy.Sets.Tag.Sets.Set.UsedBy, self).__init__()

                            self.yang_name = "used-by"
                            self.yang_parent_name = "set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"reference" : ("reference", RoutingPolicy.Sets.Tag.Sets.Set.UsedBy.Reference)}

                            self.reference = YList(self)
                            self._segment_path = lambda: "used-by"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.Sets.Tag.Sets.Set.UsedBy, [], name, value)


                        class Reference(Entity):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatus>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(RoutingPolicy.Sets.Tag.Sets.Set.UsedBy.Reference, self).__init__()

                                self.yang_name = "reference"
                                self.yang_parent_name = "used-by"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.used_directly = YLeaf(YType.boolean, "used-directly")
                                self._segment_path = lambda: "reference"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.Sets.Tag.Sets.Set.UsedBy.Reference, ['route_policy_name', 'status', 'used_directly'], name, value)


            class Unused(Entity):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.Tag.Unused, self).__init__()

                    self.yang_name = "unused"
                    self.yang_parent_name = "tag"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.object = YLeafList(YType.str, "object")
                    self._segment_path = lambda: "unused"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-oper:routing-policy/sets/tag/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.Tag.Unused, ['object'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

