""" Cisco_IOS_XR_policy_repository_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package configuration.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class RoutingPolicy(object):
    """
    Routing policy configuration
    
    .. attribute:: route_policies
    
    	All configured policies
    	**type**\: :py:class:`RoutePolicies <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies>`
    
    .. attribute:: sets
    
    	All configured sets
    	**type**\: :py:class:`Sets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets>`
    
    .. attribute:: limits
    
    	Limits for Routing Policy
    	**type**\: :py:class:`Limits <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Limits>`
    
    .. attribute:: editor
    
    	'emacs' or 'vim' or 'nano'
    	**type**\: str
    
    

    """

    _prefix = 'policy-repository-cfg'
    _revision = '2015-08-27'

    def __init__(self):
        self.route_policies = RoutingPolicy.RoutePolicies()
        self.route_policies.parent = self
        self.sets = RoutingPolicy.Sets()
        self.sets.parent = self
        self.limits = RoutingPolicy.Limits()
        self.limits.parent = self
        self.editor = None


    class RoutePolicies(object):
        """
        All configured policies
        
        .. attribute:: route_policy
        
        	Information about an individual policy
        	**type**\: list of :py:class:`RoutePolicy <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies.RoutePolicy>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2015-08-27'

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
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: rpl_route_policy
            
            	policy statements
            	**type**\: str
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.route_policy_name = None
                self.rpl_route_policy = None

            @property
            def _common_path(self):
                if self.route_policy_name is None:
                    raise YPYDataValidationError('Key property route_policy_name is None')

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:route-policies/Cisco-IOS-XR-policy-repository-cfg:route-policy[Cisco-IOS-XR-policy-repository-cfg:route-policy-name = ' + str(self.route_policy_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.route_policy_name is not None:
                    return True

                if self.rpl_route_policy is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.RoutePolicies.RoutePolicy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:route-policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.route_policy is not None:
                for child_ref in self.route_policy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
            return meta._meta_table['RoutingPolicy.RoutePolicies']['meta_info']


    class Sets(object):
        """
        All configured sets
        
        .. attribute:: prefix_sets
        
        	Information about Prefix sets
        	**type**\: :py:class:`PrefixSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets>`
        
        .. attribute:: append_extended_community_opaque_sets
        
        	Information about Opaque sets
        	**type**\: :py:class:`AppendExtendedCommunityOpaqueSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets>`
        
        .. attribute:: append_extended_community_seg_nh_sets
        
        	Information about SegNH sets
        	**type**\: :py:class:`AppendExtendedCommunitySegNhSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets>`
        
        .. attribute:: remove_extended_community_opaque_sets
        
        	Information about Opaque sets
        	**type**\: :py:class:`RemoveExtendedCommunityOpaqueSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets>`
        
        .. attribute:: extended_community_opaque_sets
        
        	Information about Opaque sets
        	**type**\: :py:class:`ExtendedCommunityOpaqueSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets>`
        
        .. attribute:: remove_extended_community_seg_nh_sets
        
        	Information about SegNH sets
        	**type**\: :py:class:`RemoveExtendedCommunitySegNhSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets>`
        
        .. attribute:: remove_ospf_area_sets
        
        	Information about OSPF Area sets
        	**type**\: :py:class:`RemoveOspfAreaSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveOspfAreaSets>`
        
        .. attribute:: ospf_area_sets
        
        	Information about OSPF Area sets
        	**type**\: :py:class:`OspfAreaSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets>`
        
        .. attribute:: extended_community_cost_sets
        
        	Information about Cost sets
        	**type**\: :py:class:`ExtendedCommunityCostSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets>`
        
        .. attribute:: extended_community_soo_sets
        
        	Information about SOO sets
        	**type**\: :py:class:`ExtendedCommunitySooSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets>`
        
        .. attribute:: prepend_extended_community_opaque_sets
        
        	Information about Opaque sets
        	**type**\: :py:class:`PrependExtendedCommunityOpaqueSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets>`
        
        .. attribute:: extended_community_seg_nh_sets
        
        	Information about SegNH sets
        	**type**\: :py:class:`ExtendedCommunitySegNhSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets>`
        
        .. attribute:: rd_sets
        
        	Information about RD sets
        	**type**\: :py:class:`RdSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets>`
        
        .. attribute:: policy_global_set_table
        
        	Information about PolicyGlobal sets
        	**type**\: :py:class:`PolicyGlobalSetTable <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PolicyGlobalSetTable>`
        
        .. attribute:: prepend_extended_community_seg_nh_sets
        
        	Information about SegNH sets
        	**type**\: :py:class:`PrependExtendedCommunitySegNhSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets>`
        
        .. attribute:: extended_community_bandwidth_sets
        
        	Information about Bandwidth sets
        	**type**\: :py:class:`ExtendedCommunityBandwidthSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets>`
        
        .. attribute:: community_sets
        
        	Information about Community sets
        	**type**\: :py:class:`CommunitySets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets>`
        
        .. attribute:: prepend_ospf_area_sets
        
        	Information about OSPF Area sets
        	**type**\: :py:class:`PrependOspfAreaSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependOspfAreaSets>`
        
        .. attribute:: append_ospf_area_sets
        
        	Information about OSPF Area sets
        	**type**\: :py:class:`AppendOspfAreaSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendOspfAreaSets>`
        
        .. attribute:: as_path_sets
        
        	Information about AS Path sets
        	**type**\: :py:class:`AsPathSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets>`
        
        .. attribute:: tag_sets
        
        	Information about Tag sets
        	**type**\: :py:class:`TagSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets>`
        
        .. attribute:: extended_community_rt_sets
        
        	Information about RT sets
        	**type**\: :py:class:`ExtendedCommunityRtSets <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2015-08-27'

        def __init__(self):
            self.parent = None
            self.prefix_sets = RoutingPolicy.Sets.PrefixSets()
            self.prefix_sets.parent = self
            self.append_extended_community_opaque_sets = RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets()
            self.append_extended_community_opaque_sets.parent = self
            self.append_extended_community_seg_nh_sets = RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets()
            self.append_extended_community_seg_nh_sets.parent = self
            self.remove_extended_community_opaque_sets = RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets()
            self.remove_extended_community_opaque_sets.parent = self
            self.extended_community_opaque_sets = RoutingPolicy.Sets.ExtendedCommunityOpaqueSets()
            self.extended_community_opaque_sets.parent = self
            self.remove_extended_community_seg_nh_sets = RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets()
            self.remove_extended_community_seg_nh_sets.parent = self
            self.remove_ospf_area_sets = RoutingPolicy.Sets.RemoveOspfAreaSets()
            self.remove_ospf_area_sets.parent = self
            self.ospf_area_sets = RoutingPolicy.Sets.OspfAreaSets()
            self.ospf_area_sets.parent = self
            self.extended_community_cost_sets = RoutingPolicy.Sets.ExtendedCommunityCostSets()
            self.extended_community_cost_sets.parent = self
            self.extended_community_soo_sets = RoutingPolicy.Sets.ExtendedCommunitySooSets()
            self.extended_community_soo_sets.parent = self
            self.prepend_extended_community_opaque_sets = RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets()
            self.prepend_extended_community_opaque_sets.parent = self
            self.extended_community_seg_nh_sets = RoutingPolicy.Sets.ExtendedCommunitySegNhSets()
            self.extended_community_seg_nh_sets.parent = self
            self.rd_sets = RoutingPolicy.Sets.RdSets()
            self.rd_sets.parent = self
            self.policy_global_set_table = RoutingPolicy.Sets.PolicyGlobalSetTable()
            self.policy_global_set_table.parent = self
            self.prepend_extended_community_seg_nh_sets = RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets()
            self.prepend_extended_community_seg_nh_sets.parent = self
            self.extended_community_bandwidth_sets = RoutingPolicy.Sets.ExtendedCommunityBandwidthSets()
            self.extended_community_bandwidth_sets.parent = self
            self.community_sets = RoutingPolicy.Sets.CommunitySets()
            self.community_sets.parent = self
            self.prepend_ospf_area_sets = RoutingPolicy.Sets.PrependOspfAreaSets()
            self.prepend_ospf_area_sets.parent = self
            self.append_ospf_area_sets = RoutingPolicy.Sets.AppendOspfAreaSets()
            self.append_ospf_area_sets.parent = self
            self.as_path_sets = RoutingPolicy.Sets.AsPathSets()
            self.as_path_sets.parent = self
            self.tag_sets = RoutingPolicy.Sets.TagSets()
            self.tag_sets.parent = self
            self.extended_community_rt_sets = RoutingPolicy.Sets.ExtendedCommunityRtSets()
            self.extended_community_rt_sets.parent = self


        class PrefixSets(object):
            """
            Information about Prefix sets
            
            .. attribute:: prefix_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`PrefixSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prefix_set = YList()
                self.prefix_set.parent = self
                self.prefix_set.name = 'prefix_set'


            class PrefixSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_prefix_set
                
                	prefix statements
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_prefix_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prefix-sets/Cisco-IOS-XR-policy-repository-cfg:prefix-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_prefix_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrefixSets.PrefixSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prefix-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.prefix_set is not None:
                    for child_ref in self.prefix_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrefixSets']['meta_info']


        class AppendExtendedCommunityOpaqueSets(object):
            """
            Information about Opaque sets
            
            .. attribute:: append_extended_community_opaque_set
            
            	Append the entries to the existing set
            	**type**\: list of :py:class:`AppendExtendedCommunityOpaqueSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets.AppendExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.append_extended_community_opaque_set = YList()
                self.append_extended_community_opaque_set.parent = self
                self.append_extended_community_opaque_set.name = 'append_extended_community_opaque_set'


            class AppendExtendedCommunityOpaqueSet(object):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_opaque_set
                
                	Extended Community Opaque Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_opaque_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-extended-community-opaque-sets/Cisco-IOS-XR-policy-repository-cfg:append-extended-community-opaque-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_opaque_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets.AppendExtendedCommunityOpaqueSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-extended-community-opaque-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.append_extended_community_opaque_set is not None:
                    for child_ref in self.append_extended_community_opaque_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets']['meta_info']


        class AppendExtendedCommunitySegNhSets(object):
            """
            Information about SegNH sets
            
            .. attribute:: append_extended_community_seg_nh_set
            
            	Append the entries to the existing set
            	**type**\: list of :py:class:`AppendExtendedCommunitySegNhSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets.AppendExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.append_extended_community_seg_nh_set = YList()
                self.append_extended_community_seg_nh_set.parent = self
                self.append_extended_community_seg_nh_set.name = 'append_extended_community_seg_nh_set'


            class AppendExtendedCommunitySegNhSet(object):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_seg_nh_set
                
                	Extended Community SegNH Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_seg_nh_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-extended-community-seg-nh-sets/Cisco-IOS-XR-policy-repository-cfg:append-extended-community-seg-nh-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_seg_nh_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets.AppendExtendedCommunitySegNhSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-extended-community-seg-nh-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.append_extended_community_seg_nh_set is not None:
                    for child_ref in self.append_extended_community_seg_nh_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets']['meta_info']


        class RemoveExtendedCommunityOpaqueSets(object):
            """
            Information about Opaque sets
            
            .. attribute:: remove_extended_community_opaque_set
            
            	Remove the entries from the existing set
            	**type**\: list of :py:class:`RemoveExtendedCommunityOpaqueSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets.RemoveExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.remove_extended_community_opaque_set = YList()
                self.remove_extended_community_opaque_set.parent = self
                self.remove_extended_community_opaque_set.name = 'remove_extended_community_opaque_set'


            class RemoveExtendedCommunityOpaqueSet(object):
                """
                Remove the entries from the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_opaque_set
                
                	Extended Community Opaque Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_opaque_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-extended-community-opaque-sets/Cisco-IOS-XR-policy-repository-cfg:remove-extended-community-opaque-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_opaque_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets.RemoveExtendedCommunityOpaqueSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-extended-community-opaque-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.remove_extended_community_opaque_set is not None:
                    for child_ref in self.remove_extended_community_opaque_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets']['meta_info']


        class ExtendedCommunityOpaqueSets(object):
            """
            Information about Opaque sets
            
            .. attribute:: extended_community_opaque_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`ExtendedCommunityOpaqueSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.extended_community_opaque_set = YList()
                self.extended_community_opaque_set.parent = self
                self.extended_community_opaque_set.name = 'extended_community_opaque_set'


            class ExtendedCommunityOpaqueSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_opaque_set
                
                	Extended Community Opaque Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_opaque_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-opaque-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-opaque-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_opaque_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-opaque-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.extended_community_opaque_set is not None:
                    for child_ref in self.extended_community_opaque_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets']['meta_info']


        class RemoveExtendedCommunitySegNhSets(object):
            """
            Information about SegNH sets
            
            .. attribute:: remove_extended_community_seg_nh_set
            
            	Remove the entries from the existing set
            	**type**\: list of :py:class:`RemoveExtendedCommunitySegNhSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets.RemoveExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.remove_extended_community_seg_nh_set = YList()
                self.remove_extended_community_seg_nh_set.parent = self
                self.remove_extended_community_seg_nh_set.name = 'remove_extended_community_seg_nh_set'


            class RemoveExtendedCommunitySegNhSet(object):
                """
                Remove the entries from the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_seg_nh_set
                
                	Extended Community SegNH Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_seg_nh_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-extended-community-seg-nh-sets/Cisco-IOS-XR-policy-repository-cfg:remove-extended-community-seg-nh-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_seg_nh_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets.RemoveExtendedCommunitySegNhSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-extended-community-seg-nh-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.remove_extended_community_seg_nh_set is not None:
                    for child_ref in self.remove_extended_community_seg_nh_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets']['meta_info']


        class RemoveOspfAreaSets(object):
            """
            Information about OSPF Area sets
            
            .. attribute:: remove_ospf_area_set
            
            	Remove the entries from the existing set
            	**type**\: list of :py:class:`RemoveOspfAreaSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveOspfAreaSets.RemoveOspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.remove_ospf_area_set = YList()
                self.remove_ospf_area_set.parent = self
                self.remove_ospf_area_set.name = 'remove_ospf_area_set'


            class RemoveOspfAreaSet(object):
                """
                Remove the entries from the existing set.
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplospf_area_set
                
                	OSPF Area Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rplospf_area_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-ospf-area-sets/Cisco-IOS-XR-policy-repository-cfg:remove-ospf-area-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rplospf_area_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RemoveOspfAreaSets.RemoveOspfAreaSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-ospf-area-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.remove_ospf_area_set is not None:
                    for child_ref in self.remove_ospf_area_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RemoveOspfAreaSets']['meta_info']


        class OspfAreaSets(object):
            """
            Information about OSPF Area sets
            
            .. attribute:: ospf_area_set
            
            	Information about an individual OSPF area set. Usage\: OSPF area set allows to define named set of area numbers        which can be referenced in the route\-policy. Area sets      may be used during redistribution of the ospf protocol.  Example\: ospf\-area\-set EXAMPLE      1,                                             192.168.1.255                                  end\-set                                        Syntax\: OSPF area number can be entered as 32 bit number or in          the ip address format. See example.                     Semantic\: Area numbers listed in the set will be searched for             a match. In the example these are areas 1 and                  192.168.1.255.                                
            	**type**\: list of :py:class:`OspfAreaSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.ospf_area_set = YList()
                self.ospf_area_set.parent = self
                self.ospf_area_set.name = 'ospf_area_set'


            class OspfAreaSet(object):
                """
                Information about an individual OSPF area set.
                Usage\: OSPF area set allows to define named
                set of area numbers        which can be
                referenced in the route\-policy. Area sets     
                may be used during redistribution of the ospf
                protocol.  Example\: ospf\-area\-set EXAMPLE     
                1,                                            
                192.168.1.255                                 
                end\-set                                       
                Syntax\: OSPF area number can be entered as 32
                bit number or in          the ip address
                format. See example.                    
                Semantic\: Area numbers listed in the set will
                be searched for             a match. In the
                example these are areas 1 and                 
                192.168.1.255.                                
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplospf_area_set
                
                	OSPF Area Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rplospf_area_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:ospf-area-sets/Cisco-IOS-XR-policy-repository-cfg:ospf-area-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rplospf_area_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:ospf-area-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ospf_area_set is not None:
                    for child_ref in self.ospf_area_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.OspfAreaSets']['meta_info']


        class ExtendedCommunityCostSets(object):
            """
            Information about Cost sets
            
            .. attribute:: extended_community_cost_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`ExtendedCommunityCostSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.extended_community_cost_set = YList()
                self.extended_community_cost_set.parent = self
                self.extended_community_cost_set.name = 'extended_community_cost_set'


            class ExtendedCommunityCostSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_cost_set
                
                	Extended Community Cost Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_cost_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-cost-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-cost-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_cost_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-cost-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.extended_community_cost_set is not None:
                    for child_ref in self.extended_community_cost_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets']['meta_info']


        class ExtendedCommunitySooSets(object):
            """
            Information about SOO sets
            
            .. attribute:: extended_community_soo_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`ExtendedCommunitySooSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.extended_community_soo_set = YList()
                self.extended_community_soo_set.parent = self
                self.extended_community_soo_set.name = 'extended_community_soo_set'


            class ExtendedCommunitySooSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_soo_set
                
                	Extended Community SOO Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_soo_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-soo-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-soo-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_soo_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-soo-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.extended_community_soo_set is not None:
                    for child_ref in self.extended_community_soo_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets']['meta_info']


        class PrependExtendedCommunityOpaqueSets(object):
            """
            Information about Opaque sets
            
            .. attribute:: prepend_extended_community_opaque_set
            
            	Prepend the entries to the existing set
            	**type**\: list of :py:class:`PrependExtendedCommunityOpaqueSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets.PrependExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prepend_extended_community_opaque_set = YList()
                self.prepend_extended_community_opaque_set.parent = self
                self.prepend_extended_community_opaque_set.name = 'prepend_extended_community_opaque_set'


            class PrependExtendedCommunityOpaqueSet(object):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_opaque_set
                
                	Extended Community Opaque Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_opaque_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-extended-community-opaque-sets/Cisco-IOS-XR-policy-repository-cfg:prepend-extended-community-opaque-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_opaque_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets.PrependExtendedCommunityOpaqueSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-extended-community-opaque-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.prepend_extended_community_opaque_set is not None:
                    for child_ref in self.prepend_extended_community_opaque_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets']['meta_info']


        class ExtendedCommunitySegNhSets(object):
            """
            Information about SegNH sets
            
            .. attribute:: extended_community_seg_nh_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`ExtendedCommunitySegNhSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.extended_community_seg_nh_set = YList()
                self.extended_community_seg_nh_set.parent = self
                self.extended_community_seg_nh_set.name = 'extended_community_seg_nh_set'


            class ExtendedCommunitySegNhSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_seg_nh_set
                
                	Extended Community SegNH Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_seg_nh_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-seg-nh-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-seg-nh-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_seg_nh_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-seg-nh-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.extended_community_seg_nh_set is not None:
                    for child_ref in self.extended_community_seg_nh_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets']['meta_info']


        class RdSets(object):
            """
            Information about RD sets
            
            .. attribute:: rd_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`RdSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets.RdSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.rd_set = YList()
                self.rd_set.parent = self
                self.rd_set.name = 'rd_set'


            class RdSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplrd_set
                
                	RD Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rplrd_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:rd-sets/Cisco-IOS-XR-policy-repository-cfg:rd-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rplrd_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RdSets.RdSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:rd-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.rd_set is not None:
                    for child_ref in self.rd_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RdSets']['meta_info']


        class PolicyGlobalSetTable(object):
            """
            Information about PolicyGlobal sets
            
            .. attribute:: policy_global_set
            
            	Information about an individual set
            	**type**\: str
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.policy_global_set = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:policy-global-set-table'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.policy_global_set is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PolicyGlobalSetTable']['meta_info']


        class PrependExtendedCommunitySegNhSets(object):
            """
            Information about SegNH sets
            
            .. attribute:: prepend_extended_community_seg_nh_set
            
            	Prepend the entries to the existing set
            	**type**\: list of :py:class:`PrependExtendedCommunitySegNhSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets.PrependExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prepend_extended_community_seg_nh_set = YList()
                self.prepend_extended_community_seg_nh_set.parent = self
                self.prepend_extended_community_seg_nh_set.name = 'prepend_extended_community_seg_nh_set'


            class PrependExtendedCommunitySegNhSet(object):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_seg_nh_set
                
                	Extended Community SegNH Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_seg_nh_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-extended-community-seg-nh-sets/Cisco-IOS-XR-policy-repository-cfg:prepend-extended-community-seg-nh-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_seg_nh_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets.PrependExtendedCommunitySegNhSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-extended-community-seg-nh-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.prepend_extended_community_seg_nh_set is not None:
                    for child_ref in self.prepend_extended_community_seg_nh_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets']['meta_info']


        class ExtendedCommunityBandwidthSets(object):
            """
            Information about Bandwidth sets
            
            .. attribute:: extended_community_bandwidth_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`ExtendedCommunityBandwidthSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.extended_community_bandwidth_set = YList()
                self.extended_community_bandwidth_set.parent = self
                self.extended_community_bandwidth_set.name = 'extended_community_bandwidth_set'


            class ExtendedCommunityBandwidthSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_bandwidth_set
                
                	Extended Community Bandwidth Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_bandwidth_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-bandwidth-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-bandwidth-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_bandwidth_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-bandwidth-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.extended_community_bandwidth_set is not None:
                    for child_ref in self.extended_community_bandwidth_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets']['meta_info']


        class CommunitySets(object):
            """
            Information about Community sets
            
            .. attribute:: community_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`CommunitySet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets.CommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.community_set = YList()
                self.community_set.parent = self
                self.community_set.name = 'community_set'


            class CommunitySet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_community_set
                
                	Community Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_community_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:community-sets/Cisco-IOS-XR-policy-repository-cfg:community-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_community_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.CommunitySets.CommunitySet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:community-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.community_set is not None:
                    for child_ref in self.community_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.CommunitySets']['meta_info']


        class PrependOspfAreaSets(object):
            """
            Information about OSPF Area sets
            
            .. attribute:: prepend_ospf_area_set
            
            	Prepend the entries to the existing set
            	**type**\: list of :py:class:`PrependOspfAreaSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependOspfAreaSets.PrependOspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prepend_ospf_area_set = YList()
                self.prepend_ospf_area_set.parent = self
                self.prepend_ospf_area_set.name = 'prepend_ospf_area_set'


            class PrependOspfAreaSet(object):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplospf_area_set
                
                	OSPF Area Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rplospf_area_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-ospf-area-sets/Cisco-IOS-XR-policy-repository-cfg:prepend-ospf-area-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rplospf_area_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrependOspfAreaSets.PrependOspfAreaSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-ospf-area-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.prepend_ospf_area_set is not None:
                    for child_ref in self.prepend_ospf_area_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrependOspfAreaSets']['meta_info']


        class AppendOspfAreaSets(object):
            """
            Information about OSPF Area sets
            
            .. attribute:: append_ospf_area_set
            
            	Append the entries to the existing set
            	**type**\: list of :py:class:`AppendOspfAreaSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendOspfAreaSets.AppendOspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.append_ospf_area_set = YList()
                self.append_ospf_area_set.parent = self
                self.append_ospf_area_set.name = 'append_ospf_area_set'


            class AppendOspfAreaSet(object):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplospf_area_set
                
                	OSPF Area Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rplospf_area_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-ospf-area-sets/Cisco-IOS-XR-policy-repository-cfg:append-ospf-area-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rplospf_area_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AppendOspfAreaSets.AppendOspfAreaSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-ospf-area-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.append_ospf_area_set is not None:
                    for child_ref in self.append_ospf_area_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AppendOspfAreaSets']['meta_info']


        class AsPathSets(object):
            """
            Information about AS Path sets
            
            .. attribute:: as_path_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`AsPathSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets.AsPathSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.as_path_set = YList()
                self.as_path_set.parent = self
                self.as_path_set.name = 'as_path_set'


            class AsPathSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplas_path_set
                
                	ASPath Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rplas_path_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:as-path-sets/Cisco-IOS-XR-policy-repository-cfg:as-path-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rplas_path_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AsPathSets.AsPathSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:as-path-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.as_path_set is not None:
                    for child_ref in self.as_path_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AsPathSets']['meta_info']


        class TagSets(object):
            """
            Information about Tag sets
            
            .. attribute:: tag_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`TagSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets.TagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.tag_set = YList()
                self.tag_set.parent = self
                self.tag_set.name = 'tag_set'


            class TagSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_tag_set
                
                	Tag Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_tag_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:tag-sets/Cisco-IOS-XR-policy-repository-cfg:tag-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_tag_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.TagSets.TagSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:tag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.tag_set is not None:
                    for child_ref in self.tag_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.TagSets']['meta_info']


        class ExtendedCommunityRtSets(object):
            """
            Information about RT sets
            
            .. attribute:: extended_community_rt_set
            
            	Information about an individual set
            	**type**\: list of :py:class:`ExtendedCommunityRtSet <ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.extended_community_rt_set = YList()
                self.extended_community_rt_set.parent = self
                self.extended_community_rt_set.name = 'extended_community_rt_set'


            class ExtendedCommunityRtSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_rt_set
                
                	Extended Community RT Set
                	**type**\: str
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.rpl_extended_community_rt_set = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYDataValidationError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-rt-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-rt-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_rt_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-rt-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.extended_community_rt_set is not None:
                    for child_ref in self.extended_community_rt_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.prefix_sets is not None and self.prefix_sets._has_data():
                return True

            if self.append_extended_community_opaque_sets is not None and self.append_extended_community_opaque_sets._has_data():
                return True

            if self.append_extended_community_seg_nh_sets is not None and self.append_extended_community_seg_nh_sets._has_data():
                return True

            if self.remove_extended_community_opaque_sets is not None and self.remove_extended_community_opaque_sets._has_data():
                return True

            if self.extended_community_opaque_sets is not None and self.extended_community_opaque_sets._has_data():
                return True

            if self.remove_extended_community_seg_nh_sets is not None and self.remove_extended_community_seg_nh_sets._has_data():
                return True

            if self.remove_ospf_area_sets is not None and self.remove_ospf_area_sets._has_data():
                return True

            if self.ospf_area_sets is not None and self.ospf_area_sets._has_data():
                return True

            if self.extended_community_cost_sets is not None and self.extended_community_cost_sets._has_data():
                return True

            if self.extended_community_soo_sets is not None and self.extended_community_soo_sets._has_data():
                return True

            if self.prepend_extended_community_opaque_sets is not None and self.prepend_extended_community_opaque_sets._has_data():
                return True

            if self.extended_community_seg_nh_sets is not None and self.extended_community_seg_nh_sets._has_data():
                return True

            if self.rd_sets is not None and self.rd_sets._has_data():
                return True

            if self.policy_global_set_table is not None and self.policy_global_set_table._has_data():
                return True

            if self.prepend_extended_community_seg_nh_sets is not None and self.prepend_extended_community_seg_nh_sets._has_data():
                return True

            if self.extended_community_bandwidth_sets is not None and self.extended_community_bandwidth_sets._has_data():
                return True

            if self.community_sets is not None and self.community_sets._has_data():
                return True

            if self.prepend_ospf_area_sets is not None and self.prepend_ospf_area_sets._has_data():
                return True

            if self.append_ospf_area_sets is not None and self.append_ospf_area_sets._has_data():
                return True

            if self.as_path_sets is not None and self.as_path_sets._has_data():
                return True

            if self.tag_sets is not None and self.tag_sets._has_data():
                return True

            if self.extended_community_rt_sets is not None and self.extended_community_rt_sets._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
            return meta._meta_table['RoutingPolicy.Sets']['meta_info']


    class Limits(object):
        """
        Limits for Routing Policy
        
        .. attribute:: maximum_lines_of_policy
        
        	Maximum number of lines of policy configuration that may be configured in total
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: maximum_number_of_policies
        
        	Maximum number of policies that may be configured
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2015-08-27'

        def __init__(self):
            self.parent = None
            self.maximum_lines_of_policy = None
            self.maximum_number_of_policies = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:limits'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.maximum_lines_of_policy is not None:
                return True

            if self.maximum_number_of_policies is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
            return meta._meta_table['RoutingPolicy.Limits']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.route_policies is not None and self.route_policies._has_data():
            return True

        if self.sets is not None and self.sets._has_data():
            return True

        if self.limits is not None and self.limits._has_data():
            return True

        if self.editor is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.policy._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
        return meta._meta_table['RoutingPolicy']['meta_info']


