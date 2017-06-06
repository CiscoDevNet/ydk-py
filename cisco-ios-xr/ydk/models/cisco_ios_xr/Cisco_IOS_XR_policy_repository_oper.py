""" Cisco_IOS_XR_policy_repository_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package operational data.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AddressFamilyEnum(Enum):
    """
    AddressFamilyEnum

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

    ipv4 = 0

    ipv6 = 1

    l2vpn = 2

    ls = 3

    af_none = 4

    af_unknown = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
        return meta._meta_table['AddressFamilyEnum']


class AttachPointDirectionEnum(Enum):
    """
    AttachPointDirectionEnum

    Attach Point Direction

    .. data:: in_ = 0

    	Attach Point Direction IN

    .. data:: out = 1

    	Attach Point Direction OUT

    """

    in_ = 0

    out = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
        return meta._meta_table['AttachPointDirectionEnum']


class GroupEnum(Enum):
    """
    GroupEnum

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

    address_family_group = 0

    session_group = 1

    neighbor_group = 2

    neighbor = 3

    error_group = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
        return meta._meta_table['GroupEnum']


class ObjectStatusEnum(Enum):
    """
    ObjectStatusEnum

    Whether an RPL object is used/referenced

    .. data:: active = 0

    	The object is in use

    .. data:: inactive = 1

    	The object is referenced by another object, but

    	not used

    .. data:: unused = 2

    	The object is not used or referenced

    """

    active = 0

    inactive = 1

    unused = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
        return meta._meta_table['ObjectStatusEnum']


class SubAddressFamilyEnum(Enum):
    """
    SubAddressFamilyEnum

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

    unicast = 0

    multicast = 1

    label = 2

    tunnel = 3

    vpn = 4

    mdt = 5

    vpls = 6

    rt_constraint = 7

    mvpn = 8

    flow = 9

    vpn_mcast = 10

    saf_none = 11

    saf_unknown = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
        return meta._meta_table['SubAddressFamilyEnum']



class RoutingPolicy(object):
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
    _revision = '2015-11-09'

    def __init__(self):
        self.limits = RoutingPolicy.Limits()
        self.limits.parent = self
        self.policies = RoutingPolicy.Policies()
        self.policies.parent = self
        self.sets = RoutingPolicy.Sets()
        self.sets.parent = self


    class Limits(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.compiled_policies_length = None
            self.current_lines_of_policy_limit = None
            self.current_lines_of_policy_used = None
            self.current_number_of_policies_limit = None
            self.current_number_of_policies_used = None
            self.maximum_lines_of_policy = None
            self.maximum_number_of_policies = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:limits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.compiled_policies_length is not None:
                return True

            if self.current_lines_of_policy_limit is not None:
                return True

            if self.current_lines_of_policy_used is not None:
                return True

            if self.current_number_of_policies_limit is not None:
                return True

            if self.current_number_of_policies_used is not None:
                return True

            if self.maximum_lines_of_policy is not None:
                return True

            if self.maximum_number_of_policies is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
            return meta._meta_table['RoutingPolicy.Limits']['meta_info']


    class Policies(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.active = RoutingPolicy.Policies.Active()
            self.active.parent = self
            self.inactive = RoutingPolicy.Policies.Inactive()
            self.inactive.parent = self
            self.route_policies = RoutingPolicy.Policies.RoutePolicies()
            self.route_policies.parent = self
            self.unused = RoutingPolicy.Policies.Unused()
            self.unused.parent = self


        class RoutePolicies(object):
            """
            Information about individual policies
            
            .. attribute:: route_policy
            
            	Information about an individual policy
            	**type**\: list of    :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.route_policy = YList()
                self.route_policy.parent = self
                self.route_policy.name = 'route_policy'


            class RoutePolicy(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.route_policy_name = None
                    self.attached = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached()
                    self.attached.parent = self
                    self.policy_uses = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses()
                    self.policy_uses.parent = self
                    self.used_by = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy()
                    self.used_by.parent = self


                class PolicyUses(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all_used_policies = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies()
                        self.all_used_policies.parent = self
                        self.all_used_sets = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets()
                        self.all_used_sets.parent = self
                        self.directly_used_policies = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies()
                        self.directly_used_policies.parent = self
                        self.directly_used_sets = RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets()
                        self.directly_used_sets.parent = self


                    class DirectlyUsedPolicies(object):
                        """
                        Policies that this policy uses directly
                        
                        .. attribute:: object
                        
                        	Policy objects
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.object = YLeafList()
                            self.object.parent = self
                            self.object.name = 'object'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:directly-used-policies'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.object is not None:
                                for child in self.object:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies']['meta_info']


                    class AllUsedSets(object):
                        """
                        Sets used by this policy, or by policies
                        that it uses
                        
                        .. attribute:: sets
                        
                        	List of sets in several domains
                        	**type**\: list of    :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sets = YList()
                            self.sets.parent = self
                            self.sets.name = 'sets'


                        class Sets(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.set_domain = None
                                self.set_name = YLeafList()
                                self.set_name.parent = self
                                self.set_name.name = 'set_name'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:sets'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.set_domain is not None:
                                    return True

                                if self.set_name is not None:
                                    for child in self.set_name:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:all-used-sets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sets is not None:
                                for child_ref in self.sets:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info']


                    class DirectlyUsedSets(object):
                        """
                        Sets that this policy uses directly
                        
                        .. attribute:: sets
                        
                        	List of sets in several domains
                        	**type**\: list of    :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sets = YList()
                            self.sets.parent = self
                            self.sets.name = 'sets'


                        class Sets(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.set_domain = None
                                self.set_name = YLeafList()
                                self.set_name.parent = self
                                self.set_name.name = 'set_name'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:sets'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.set_domain is not None:
                                    return True

                                if self.set_name is not None:
                                    for child in self.set_name:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:directly-used-sets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sets is not None:
                                for child_ref in self.sets:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info']


                    class AllUsedPolicies(object):
                        """
                        Policies used by this policy, or by policies
                        that it uses
                        
                        .. attribute:: object
                        
                        	Policy objects
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.object = YLeafList()
                            self.object.parent = self
                            self.object.name = 'object'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:all-used-policies'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.object is not None:
                                for child in self.object:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:policy-uses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.all_used_policies is not None and self.all_used_policies._has_data():
                            return True

                        if self.all_used_sets is not None and self.all_used_sets._has_data():
                            return True

                        if self.directly_used_policies is not None and self.directly_used_policies._has_data():
                            return True

                        if self.directly_used_sets is not None and self.directly_used_sets._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']


                class UsedBy(object):
                    """
                    Policies that use this object, directly or
                    indirectly
                    
                    .. attribute:: reference
                    
                    	Information about policies referring to this object
                    	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.reference = YList()
                        self.reference.parent = self
                        self.reference.name = 'reference'


                    class Reference(object):
                        """
                        Information about policies referring to this
                        object
                        
                        .. attribute:: route_policy_name
                        
                        	Name of policy
                        	**type**\:  str
                        
                        .. attribute:: status
                        
                        	Active, Inactive, or Unused
                        	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                        
                        .. attribute:: used_directly
                        
                        	Whether the policy uses this object directly or indirectly
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.route_policy_name = None
                            self.status = None
                            self.used_directly = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.route_policy_name is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.used_directly is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.reference is not None:
                            for child_ref in self.reference:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info']


                class Attached(object):
                    """
                    Information about where this policy or set is
                    attached
                    
                    .. attribute:: binding
                    
                    	bindings list
                    	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.binding = YList()
                        self.binding.parent = self
                        self.binding.name = 'binding'


                    class Binding(object):
                        """
                        bindings list
                        
                        .. attribute:: af_name
                        
                        	Address Family Identifier
                        	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                        
                        .. attribute:: aggregate_network_address
                        
                        	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                        	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                        
                        .. attribute:: group
                        
                        	Neighbor Group 
                        	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                        
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
                        	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                        
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
                        	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                        
                        .. attribute:: source_protocol
                        
                        	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.aggregate_network_address = None
                            self.area_id = None
                            self.attach_point = None
                            self.attached_policy = None
                            self.direction = None
                            self.group = None
                            self.group_name = None
                            self.instance = None
                            self.interface_name = None
                            self.neighbor_address = None
                            self.neighbor_af_name = None
                            self.propogate_from = None
                            self.propogate_to = None
                            self.proto_instance = None
                            self.protocol = None
                            self.route_policy_name = None
                            self.saf_name = None
                            self.source_protocol = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.aggregate_network_address is not None:
                                return True

                            if self.area_id is not None:
                                return True

                            if self.attach_point is not None:
                                return True

                            if self.attached_policy is not None:
                                return True

                            if self.direction is not None:
                                return True

                            if self.group is not None:
                                return True

                            if self.group_name is not None:
                                return True

                            if self.instance is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.neighbor_address is not None:
                                return True

                            if self.neighbor_af_name is not None:
                                return True

                            if self.propogate_from is not None:
                                return True

                            if self.propogate_to is not None:
                                return True

                            if self.proto_instance is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            if self.route_policy_name is not None:
                                return True

                            if self.saf_name is not None:
                                return True

                            if self.source_protocol is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.binding is not None:
                            for child_ref in self.binding:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info']

                @property
                def _common_path(self):
                    if self.route_policy_name is None:
                        raise YPYModelError('Key property route_policy_name is None')

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:policies/Cisco-IOS-XR-policy-repository-oper:route-policies/Cisco-IOS-XR-policy-repository-oper:route-policy[Cisco-IOS-XR-policy-repository-oper:route-policy-name = ' + str(self.route_policy_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.route_policy_name is not None:
                        return True

                    if self.attached is not None and self.attached._has_data():
                        return True

                    if self.policy_uses is not None and self.policy_uses._has_data():
                        return True

                    if self.used_by is not None and self.used_by._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:policies/Cisco-IOS-XR-policy-repository-oper:route-policies'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.route_policy is not None:
                    for child_ref in self.route_policy:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Policies.RoutePolicies']['meta_info']


        class Unused(object):
            """
            All objects of a given type that are not
            referenced at all
            
            .. attribute:: object
            
            	Policy objects
            	**type**\:  list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.object = YLeafList()
                self.object.parent = self
                self.object.name = 'object'

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:policies/Cisco-IOS-XR-policy-repository-oper:unused'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.object is not None:
                    for child in self.object:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Policies.Unused']['meta_info']


        class Inactive(object):
            """
            All objects of a given type that are not
            attached to a protocol
            
            .. attribute:: object
            
            	Policy objects
            	**type**\:  list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.object = YLeafList()
                self.object.parent = self
                self.object.name = 'object'

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:policies/Cisco-IOS-XR-policy-repository-oper:inactive'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.object is not None:
                    for child in self.object:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Policies.Inactive']['meta_info']


        class Active(object):
            """
            All objects of a given type that are attached to
            a protocol
            
            .. attribute:: object
            
            	Policy objects
            	**type**\:  list of str
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.object = YLeafList()
                self.object.parent = self
                self.object.name = 'object'

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:policies/Cisco-IOS-XR-policy-repository-oper:active'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.object is not None:
                    for child in self.object:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Policies.Active']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.active is not None and self.active._has_data():
                return True

            if self.inactive is not None and self.inactive._has_data():
                return True

            if self.route_policies is not None and self.route_policies._has_data():
                return True

            if self.unused is not None and self.unused._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
            return meta._meta_table['RoutingPolicy.Policies']['meta_info']


    class Sets(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.as_path = RoutingPolicy.Sets.AsPath()
            self.as_path.parent = self
            self.community = RoutingPolicy.Sets.Community()
            self.community.parent = self
            self.esi = RoutingPolicy.Sets.Esi()
            self.esi.parent = self
            self.etag = RoutingPolicy.Sets.Etag()
            self.etag.parent = self
            self.extended_community_bandwidth = RoutingPolicy.Sets.ExtendedCommunityBandwidth()
            self.extended_community_bandwidth.parent = self
            self.extended_community_cost = RoutingPolicy.Sets.ExtendedCommunityCost()
            self.extended_community_cost.parent = self
            self.extended_community_opaque = RoutingPolicy.Sets.ExtendedCommunityOpaque()
            self.extended_community_opaque.parent = self
            self.extended_community_rt = RoutingPolicy.Sets.ExtendedCommunityRt()
            self.extended_community_rt.parent = self
            self.extended_community_seg_nh = RoutingPolicy.Sets.ExtendedCommunitySegNh()
            self.extended_community_seg_nh.parent = self
            self.extended_community_soo = RoutingPolicy.Sets.ExtendedCommunitySoo()
            self.extended_community_soo.parent = self
            self.mac = RoutingPolicy.Sets.Mac()
            self.mac.parent = self
            self.ospf_area = RoutingPolicy.Sets.OspfArea()
            self.ospf_area.parent = self
            self.prefix = RoutingPolicy.Sets.Prefix()
            self.prefix.parent = self
            self.rd = RoutingPolicy.Sets.Rd()
            self.rd.parent = self
            self.tag = RoutingPolicy.Sets.Tag()
            self.tag.parent = self


        class Etag(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Etag.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Etag.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Etag.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Etag.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Etag.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:etag/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:etag/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Etag.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:etag/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Etag.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:etag/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Etag.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:etag/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Etag.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:etag'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Etag']['meta_info']


        class OspfArea(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.OspfArea.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.OspfArea.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.OspfArea.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.OspfArea.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:ospf-area/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:ospf-area/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.OspfArea.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:ospf-area/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.OspfArea.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:ospf-area/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.OspfArea.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:ospf-area/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.OspfArea.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:ospf-area'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']


        class ExtendedCommunityOpaque(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.ExtendedCommunityOpaque.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-opaque/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-opaque/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-opaque/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-opaque/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-opaque/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-opaque'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']


        class ExtendedCommunitySegNh(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.ExtendedCommunitySegNh.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-seg-nh/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-seg-nh/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-seg-nh/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-seg-nh/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-seg-nh/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-seg-nh'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']


        class ExtendedCommunitySoo(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.ExtendedCommunitySoo.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.ExtendedCommunitySoo.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-soo/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-soo/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-soo/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-soo/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-soo/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-soo'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']


        class Tag(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Tag.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Tag.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Tag.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Tag.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Tag.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:tag/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:tag/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Tag.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:tag/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Tag.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:tag/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Tag.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:tag/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Tag.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:tag'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Tag']['meta_info']


        class Prefix(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Prefix.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Prefix.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Prefix.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Prefix.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Prefix.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:prefix/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:prefix/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Prefix.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:prefix/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Prefix.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:prefix/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Prefix.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:prefix/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Prefix.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:prefix'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Prefix']['meta_info']


        class Community(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Community.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Community.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Community.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Community.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Community.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Community.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:community/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:community/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Community.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:community/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Community.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:community/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Community.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:community/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Community.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:community'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Community']['meta_info']


        class AsPath(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.AsPath.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.AsPath.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.AsPath.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.AsPath.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.AsPath.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:as-path/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:as-path/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.AsPath.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:as-path/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.AsPath.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:as-path/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.AsPath.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:as-path/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.AsPath.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:as-path'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.AsPath']['meta_info']


        class Esi(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Esi.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Esi.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Esi.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Esi.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Esi.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:esi/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:esi/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Esi.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:esi/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Esi.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:esi/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Esi.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:esi/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Esi.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:esi'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Esi']['meta_info']


        class ExtendedCommunityBandwidth(object):
            """
            Information about Extended Community Bandwidth
            sets
            
            .. attribute:: inactive
            
            	All objects of a given type that are not attached to a protocol
            	**type**\:   :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive>`
            
            .. attribute:: sets
            
            	Information about individual sets
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.inactive = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-bandwidth/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-bandwidth/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-bandwidth/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-bandwidth/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-bandwidth'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']


        class ExtendedCommunityRt(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.ExtendedCommunityRt.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.ExtendedCommunityRt.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.ExtendedCommunityRt.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.ExtendedCommunityRt.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-rt/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-rt/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-rt/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-rt/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-rt/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-rt'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']


        class Rd(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Rd.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Rd.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Rd.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Rd.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Rd.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:rd/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:rd/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Rd.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:rd/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Rd.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:rd/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Rd.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:rd/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Rd.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:rd'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Rd']['meta_info']


        class Mac(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.Mac.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.Mac.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.Mac.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.Mac.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.Mac.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:mac/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:mac/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Mac.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:mac/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Mac.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:mac/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Mac.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:mac/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.Mac.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:mac'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.Mac']['meta_info']


        class ExtendedCommunityCost(object):
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
            	**type**\:   :py:class:`Sets_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_>`
            
            .. attribute:: unused
            
            	All objects of a given type that are not referenced at all
            	**type**\:   :py:class:`Unused <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Unused>`
            
            

            """

            _prefix = 'policy-repository-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active = RoutingPolicy.Sets.ExtendedCommunityCost.Active()
                self.active.parent = self
                self.inactive = RoutingPolicy.Sets.ExtendedCommunityCost.Inactive()
                self.inactive.parent = self
                self.sets = RoutingPolicy.Sets.ExtendedCommunityCost.Sets_()
                self.sets.parent = self
                self.unused = RoutingPolicy.Sets.ExtendedCommunityCost.Unused()
                self.unused.parent = self


            class Sets_(object):
                """
                Information about individual sets
                
                .. attribute:: set
                
                	Information about an individual set
                	**type**\: list of    :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set>`
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.set = YList()
                    self.set.parent = self
                    self.set.name = 'set'


                class Set(object):
                    """
                    Information about an individual set
                    
                    .. attribute:: set_name  <key>
                    
                    	Set name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attached
                    
                    	Information about where this policy or set is attached
                    	**type**\:   :py:class:`Attached <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached>`
                    
                    .. attribute:: used_by
                    
                    	Policies that use this object, directly or indirectly
                    	**type**\:   :py:class:`UsedBy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy>`
                    
                    

                    """

                    _prefix = 'policy-repository-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.set_name = None
                        self.attached = RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached()
                        self.attached.parent = self
                        self.used_by = RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy()
                        self.used_by.parent = self


                    class UsedBy(object):
                        """
                        Policies that use this object, directly or
                        indirectly
                        
                        .. attribute:: reference
                        
                        	Information about policies referring to this object
                        	**type**\: list of    :py:class:`Reference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.reference = YList()
                            self.reference.parent = self
                            self.reference.name = 'reference'


                        class Reference(object):
                            """
                            Information about policies referring to this
                            object
                            
                            .. attribute:: route_policy_name
                            
                            	Name of policy
                            	**type**\:  str
                            
                            .. attribute:: status
                            
                            	Active, Inactive, or Unused
                            	**type**\:   :py:class:`ObjectStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.ObjectStatusEnum>`
                            
                            .. attribute:: used_directly
                            
                            	Whether the policy uses this object directly or indirectly
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.route_policy_name = None
                                self.status = None
                                self.used_directly = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:reference'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.route_policy_name is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.used_directly is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:used-by'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.reference is not None:
                                for child_ref in self.reference:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info']


                    class Attached(object):
                        """
                        Information about where this policy or set is
                        attached
                        
                        .. attribute:: binding
                        
                        	bindings list
                        	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding>`
                        
                        

                        """

                        _prefix = 'policy-repository-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.binding = YList()
                            self.binding.parent = self
                            self.binding.name = 'binding'


                        class Binding(object):
                            """
                            bindings list
                            
                            .. attribute:: af_name
                            
                            	Address Family Identifier
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
                            .. attribute:: aggregate_network_address
                            
                            	Aggregate IP address or Network IP Address       in IPv4 or IPv6 Format
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
                            	**type**\:   :py:class:`AttachPointDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AttachPointDirectionEnum>`
                            
                            .. attribute:: group
                            
                            	Neighbor Group 
                            	**type**\:   :py:class:`GroupEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.GroupEnum>`
                            
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
                            	**type**\:   :py:class:`AddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.AddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`SubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper.SubAddressFamilyEnum>`
                            
                            .. attribute:: source_protocol
                            
                            	Source Protocol to redistribute,                 Source Protocol can be one of the following values                               {all, connected, local, static, bgp, rip, isis, ospf,  ospfv3, eigrp, unknown }
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'policy-repository-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.aggregate_network_address = None
                                self.area_id = None
                                self.attach_point = None
                                self.attached_policy = None
                                self.direction = None
                                self.group = None
                                self.group_name = None
                                self.instance = None
                                self.interface_name = None
                                self.neighbor_address = None
                                self.neighbor_af_name = None
                                self.propogate_from = None
                                self.propogate_to = None
                                self.proto_instance = None
                                self.protocol = None
                                self.route_policy_name = None
                                self.saf_name = None
                                self.source_protocol = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:binding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.aggregate_network_address is not None:
                                    return True

                                if self.area_id is not None:
                                    return True

                                if self.attach_point is not None:
                                    return True

                                if self.attached_policy is not None:
                                    return True

                                if self.direction is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.group_name is not None:
                                    return True

                                if self.instance is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.neighbor_af_name is not None:
                                    return True

                                if self.propogate_from is not None:
                                    return True

                                if self.propogate_to is not None:
                                    return True

                                if self.proto_instance is not None:
                                    return True

                                if self.protocol is not None:
                                    return True

                                if self.route_policy_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.source_protocol is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-policy-repository-oper:attached'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.binding is not None:
                                for child_ref in self.binding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                            return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info']

                    @property
                    def _common_path(self):
                        if self.set_name is None:
                            raise YPYModelError('Key property set_name is None')

                        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-cost/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:set[Cisco-IOS-XR-policy-repository-oper:set-name = ' + str(self.set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.set_name is not None:
                            return True

                        if self.attached is not None and self.attached._has_data():
                            return True

                        if self.used_by is not None and self.used_by._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                        return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-cost/Cisco-IOS-XR-policy-repository-oper:sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.set is not None:
                        for child_ref in self.set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_']['meta_info']


            class Unused(object):
                """
                All objects of a given type that are not
                referenced at all
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-cost/Cisco-IOS-XR-policy-repository-oper:unused'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Unused']['meta_info']


            class Inactive(object):
                """
                All objects of a given type that are not
                attached to a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-cost/Cisco-IOS-XR-policy-repository-oper:inactive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Inactive']['meta_info']


            class Active(object):
                """
                All objects of a given type that are attached to
                a protocol
                
                .. attribute:: object
                
                	Policy objects
                	**type**\:  list of str
                
                

                """

                _prefix = 'policy-repository-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.object = YLeafList()
                    self.object.parent = self
                    self.object.name = 'object'

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-cost/Cisco-IOS-XR-policy-repository-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.object is not None:
                        for child in self.object:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Active']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets/Cisco-IOS-XR-policy-repository-oper:extended-community-cost'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.inactive is not None and self.inactive._has_data():
                    return True

                if self.sets is not None and self.sets._has_data():
                    return True

                if self.unused is not None and self.unused._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-oper:routing-policy/Cisco-IOS-XR-policy-repository-oper:sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.as_path is not None and self.as_path._has_data():
                return True

            if self.community is not None and self.community._has_data():
                return True

            if self.esi is not None and self.esi._has_data():
                return True

            if self.etag is not None and self.etag._has_data():
                return True

            if self.extended_community_bandwidth is not None and self.extended_community_bandwidth._has_data():
                return True

            if self.extended_community_cost is not None and self.extended_community_cost._has_data():
                return True

            if self.extended_community_opaque is not None and self.extended_community_opaque._has_data():
                return True

            if self.extended_community_rt is not None and self.extended_community_rt._has_data():
                return True

            if self.extended_community_seg_nh is not None and self.extended_community_seg_nh._has_data():
                return True

            if self.extended_community_soo is not None and self.extended_community_soo._has_data():
                return True

            if self.mac is not None and self.mac._has_data():
                return True

            if self.ospf_area is not None and self.ospf_area._has_data():
                return True

            if self.prefix is not None and self.prefix._has_data():
                return True

            if self.rd is not None and self.rd._has_data():
                return True

            if self.tag is not None and self.tag._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
            return meta._meta_table['RoutingPolicy.Sets']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-policy-repository-oper:routing-policy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.limits is not None and self.limits._has_data():
            return True

        if self.policies is not None and self.policies._has_data():
            return True

        if self.sets is not None and self.sets._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_oper as meta
        return meta._meta_table['RoutingPolicy']['meta_info']


