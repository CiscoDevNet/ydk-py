""" Cisco_IOS_XR_policy_repository_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package configuration.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class RoutingPolicy(object):
    """
    Routing policy configuration
    
    .. attribute:: editor
    
    	'emacs' or 'vim' or 'nano'
    	**type**\:  str
    
    .. attribute:: limits
    
    	Limits for Routing Policy
    	**type**\:   :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Limits>`
    
    .. attribute:: route_policies
    
    	All configured policies
    	**type**\:   :py:class:`RoutePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies>`
    
    .. attribute:: sets
    
    	All configured sets
    	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets>`
    
    

    """

    _prefix = 'policy-repository-cfg'
    _revision = '2015-08-27'

    def __init__(self):
        self.editor = None
        self.limits = RoutingPolicy.Limits()
        self.limits.parent = self
        self.route_policies = RoutingPolicy.RoutePolicies()
        self.route_policies.parent = self
        self.sets = RoutingPolicy.Sets()
        self.sets.parent = self


    class RoutePolicies(object):
        """
        All configured policies
        
        .. attribute:: route_policy
        
        	Information about an individual policy
        	**type**\: list of    :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies.RoutePolicy>`
        
        

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
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: rpl_route_policy
            
            	policy statements
            	**type**\:  str
            
            	**mandatory**\: True
            
            

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
                    raise YPYModelError('Key property route_policy_name is None')

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:route-policies/Cisco-IOS-XR-policy-repository-cfg:route-policy[Cisco-IOS-XR-policy-repository-cfg:route-policy-name = ' + str(self.route_policy_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.route_policy_name is not None:
                    return True

                if self.rpl_route_policy is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.RoutePolicies.RoutePolicy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:route-policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.route_policy is not None:
                for child_ref in self.route_policy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
            return meta._meta_table['RoutingPolicy.RoutePolicies']['meta_info']


    class Sets(object):
        """
        All configured sets
        
        .. attribute:: append_esi_sets
        
        	Information about Esi sets
        	**type**\:   :py:class:`AppendEsiSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEsiSets>`
        
        .. attribute:: append_etag_sets
        
        	Information about Etag sets
        	**type**\:   :py:class:`AppendEtagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEtagSets>`
        
        .. attribute:: append_mac_sets
        
        	Information about Mac sets
        	**type**\:   :py:class:`AppendMacSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendMacSets>`
        
        .. attribute:: as_path_sets
        
        	Information about AS Path sets
        	**type**\:   :py:class:`AsPathSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets>`
        
        .. attribute:: community_sets
        
        	Information about Community sets
        	**type**\:   :py:class:`CommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets>`
        
        .. attribute:: esi_sets
        
        	Information about Esi sets
        	**type**\:   :py:class:`EsiSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EsiSets>`
        
        .. attribute:: etag_sets
        
        	Information about Etag sets
        	**type**\:   :py:class:`EtagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EtagSets>`
        
        .. attribute:: extended_community_bandwidth_sets
        
        	Information about Bandwidth sets
        	**type**\:   :py:class:`ExtendedCommunityBandwidthSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets>`
        
        .. attribute:: extended_community_cost_sets
        
        	Information about Cost sets
        	**type**\:   :py:class:`ExtendedCommunityCostSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets>`
        
        .. attribute:: extended_community_opaque_sets
        
        	Information about Opaque sets
        	**type**\:   :py:class:`ExtendedCommunityOpaqueSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets>`
        
        .. attribute:: extended_community_rt_sets
        
        	Information about RT sets
        	**type**\:   :py:class:`ExtendedCommunityRtSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets>`
        
        .. attribute:: extended_community_seg_nh_sets
        
        	Information about SegNH sets
        	**type**\:   :py:class:`ExtendedCommunitySegNhSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets>`
        
        .. attribute:: extended_community_soo_sets
        
        	Information about SOO sets
        	**type**\:   :py:class:`ExtendedCommunitySooSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets>`
        
        .. attribute:: mac_sets
        
        	Information about Mac sets
        	**type**\:   :py:class:`MacSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.MacSets>`
        
        .. attribute:: ospf_area_sets
        
        	Information about OSPF Area sets
        	**type**\:   :py:class:`OspfAreaSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets>`
        
        .. attribute:: policy_global_set_table
        
        	Information about PolicyGlobal sets
        	**type**\:   :py:class:`PolicyGlobalSetTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PolicyGlobalSetTable>`
        
        .. attribute:: prefix_sets
        
        	Information about Prefix sets
        	**type**\:   :py:class:`PrefixSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets>`
        
        .. attribute:: prepend_esi_sets
        
        	Information about Esi sets
        	**type**\:   :py:class:`PrependEsiSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEsiSets>`
        
        .. attribute:: prepend_etag_sets
        
        	Information about Etag sets
        	**type**\:   :py:class:`PrependEtagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEtagSets>`
        
        .. attribute:: prepend_mac_sets
        
        	Information about Mac sets
        	**type**\:   :py:class:`PrependMacSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependMacSets>`
        
        .. attribute:: rd_sets
        
        	Information about RD sets
        	**type**\:   :py:class:`RdSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets>`
        
        .. attribute:: remove_esi_sets
        
        	Information about Esi sets
        	**type**\:   :py:class:`RemoveEsiSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEsiSets>`
        
        .. attribute:: remove_etag_sets
        
        	Information about Etag sets
        	**type**\:   :py:class:`RemoveEtagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEtagSets>`
        
        .. attribute:: remove_mac_sets
        
        	Information about Mac sets
        	**type**\:   :py:class:`RemoveMacSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveMacSets>`
        
        .. attribute:: tag_sets
        
        	Information about Tag sets
        	**type**\:   :py:class:`TagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2015-08-27'

        def __init__(self):
            self.parent = None
            self.append_esi_sets = RoutingPolicy.Sets.AppendEsiSets()
            self.append_esi_sets.parent = self
            self.append_etag_sets = RoutingPolicy.Sets.AppendEtagSets()
            self.append_etag_sets.parent = self
            self.append_mac_sets = RoutingPolicy.Sets.AppendMacSets()
            self.append_mac_sets.parent = self
            self.as_path_sets = RoutingPolicy.Sets.AsPathSets()
            self.as_path_sets.parent = self
            self.community_sets = RoutingPolicy.Sets.CommunitySets()
            self.community_sets.parent = self
            self.esi_sets = RoutingPolicy.Sets.EsiSets()
            self.esi_sets.parent = self
            self.etag_sets = RoutingPolicy.Sets.EtagSets()
            self.etag_sets.parent = self
            self.extended_community_bandwidth_sets = RoutingPolicy.Sets.ExtendedCommunityBandwidthSets()
            self.extended_community_bandwidth_sets.parent = self
            self.extended_community_cost_sets = RoutingPolicy.Sets.ExtendedCommunityCostSets()
            self.extended_community_cost_sets.parent = self
            self.extended_community_opaque_sets = RoutingPolicy.Sets.ExtendedCommunityOpaqueSets()
            self.extended_community_opaque_sets.parent = self
            self.extended_community_rt_sets = RoutingPolicy.Sets.ExtendedCommunityRtSets()
            self.extended_community_rt_sets.parent = self
            self.extended_community_seg_nh_sets = RoutingPolicy.Sets.ExtendedCommunitySegNhSets()
            self.extended_community_seg_nh_sets.parent = self
            self.extended_community_soo_sets = RoutingPolicy.Sets.ExtendedCommunitySooSets()
            self.extended_community_soo_sets.parent = self
            self.mac_sets = RoutingPolicy.Sets.MacSets()
            self.mac_sets.parent = self
            self.ospf_area_sets = RoutingPolicy.Sets.OspfAreaSets()
            self.ospf_area_sets.parent = self
            self.policy_global_set_table = RoutingPolicy.Sets.PolicyGlobalSetTable()
            self.policy_global_set_table.parent = self
            self.prefix_sets = RoutingPolicy.Sets.PrefixSets()
            self.prefix_sets.parent = self
            self.prepend_esi_sets = RoutingPolicy.Sets.PrependEsiSets()
            self.prepend_esi_sets.parent = self
            self.prepend_etag_sets = RoutingPolicy.Sets.PrependEtagSets()
            self.prepend_etag_sets.parent = self
            self.prepend_mac_sets = RoutingPolicy.Sets.PrependMacSets()
            self.prepend_mac_sets.parent = self
            self.rd_sets = RoutingPolicy.Sets.RdSets()
            self.rd_sets.parent = self
            self.remove_esi_sets = RoutingPolicy.Sets.RemoveEsiSets()
            self.remove_esi_sets.parent = self
            self.remove_etag_sets = RoutingPolicy.Sets.RemoveEtagSets()
            self.remove_etag_sets.parent = self
            self.remove_mac_sets = RoutingPolicy.Sets.RemoveMacSets()
            self.remove_mac_sets.parent = self
            self.tag_sets = RoutingPolicy.Sets.TagSets()
            self.tag_sets.parent = self


        class PrependEtagSets(object):
            """
            Information about Etag sets
            
            .. attribute:: prepend_etag_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prepend_etag_set = YList()
                self.prepend_etag_set.parent = self
                self.prepend_etag_set.name = 'prepend_etag_set'


            class PrependEtagSet(object):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: etag_set_as_text
                
                	Etag Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.etag_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-etag-sets/Cisco-IOS-XR-policy-repository-cfg:prepend-etag-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.etag_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-etag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prepend_etag_set is not None:
                    for child_ref in self.prepend_etag_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrependEtagSets']['meta_info']


        class PrefixSets(object):
            """
            Information about Prefix sets
            
            .. attribute:: prefix_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`PrefixSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets.PrefixSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_prefix_set
                
                	prefix statements
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prefix-sets/Cisco-IOS-XR-policy-repository-cfg:prefix-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_prefix_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrefixSets.PrefixSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prefix-sets'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrefixSets']['meta_info']


        class AppendEtagSets(object):
            """
            Information about Etag sets
            
            .. attribute:: append_etag_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.append_etag_set = YList()
                self.append_etag_set.parent = self
                self.append_etag_set.name = 'append_etag_set'


            class AppendEtagSet(object):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: etag_set_as_text
                
                	Etag Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.etag_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-etag-sets/Cisco-IOS-XR-policy-repository-cfg:append-etag-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.etag_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-etag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.append_etag_set is not None:
                    for child_ref in self.append_etag_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AppendEtagSets']['meta_info']


        class RemoveEtagSets(object):
            """
            Information about Etag sets
            
            .. attribute:: remove_etag_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.remove_etag_set = YList()
                self.remove_etag_set.parent = self
                self.remove_etag_set.name = 'remove_etag_set'


            class RemoveEtagSet(object):
                """
                Remove the entries from the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: etag_set_as_text
                
                	Etag Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.etag_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-etag-sets/Cisco-IOS-XR-policy-repository-cfg:remove-etag-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.etag_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-etag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.remove_etag_set is not None:
                    for child_ref in self.remove_etag_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RemoveEtagSets']['meta_info']


        class MacSets(object):
            """
            Information about Mac sets
            
            .. attribute:: mac_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`MacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.MacSets.MacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.mac_set = YList()
                self.mac_set.parent = self
                self.mac_set.name = 'mac_set'


            class MacSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mac_set_as_text
                
                	Mac Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.mac_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:mac-sets/Cisco-IOS-XR-policy-repository-cfg:mac-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.mac_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.MacSets.MacSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:mac-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.mac_set is not None:
                    for child_ref in self.mac_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.MacSets']['meta_info']


        class ExtendedCommunityOpaqueSets(object):
            """
            Information about Opaque sets
            
            .. attribute:: extended_community_opaque_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityOpaqueSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_opaque_set
                
                	Extended Community Opaque Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-opaque-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-opaque-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_opaque_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-opaque-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended_community_opaque_set is not None:
                    for child_ref in self.extended_community_opaque_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets']['meta_info']


        class PrependMacSets(object):
            """
            Information about Mac sets
            
            .. attribute:: prepend_mac_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependMacSets.PrependMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prepend_mac_set = YList()
                self.prepend_mac_set.parent = self
                self.prepend_mac_set.name = 'prepend_mac_set'


            class PrependMacSet(object):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mac_set_as_text
                
                	Mac Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.mac_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-mac-sets/Cisco-IOS-XR-policy-repository-cfg:prepend-mac-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.mac_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrependMacSets.PrependMacSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-mac-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prepend_mac_set is not None:
                    for child_ref in self.prepend_mac_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrependMacSets']['meta_info']


        class OspfAreaSets(object):
            """
            Information about OSPF Area sets
            
            .. attribute:: ospf_area_set
            
            	Information about an individual OSPF area set. Usage\: OSPF area set allows to define named set of area numbers        which can be referenced in the route\-policy. Area sets      may be used during redistribution of the ospf protocol.  Example\: ospf\-area\-set EXAMPLE      1,                                             192.168.1.255                                  end\-set                                        Syntax\: OSPF area number can be entered as 32 bit number or in          the ip address format. See example.                     Semantic\: Area numbers listed in the set will be searched for             a match. In the example these are areas 1 and                  192.168.1.255.                                
            	**type**\: list of    :py:class:`OspfAreaSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplospf_area_set
                
                	OSPF Area Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:ospf-area-sets/Cisco-IOS-XR-policy-repository-cfg:ospf-area-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rplospf_area_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:ospf-area-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ospf_area_set is not None:
                    for child_ref in self.ospf_area_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.OspfAreaSets']['meta_info']


        class AppendMacSets(object):
            """
            Information about Mac sets
            
            .. attribute:: append_mac_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendMacSets.AppendMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.append_mac_set = YList()
                self.append_mac_set.parent = self
                self.append_mac_set.name = 'append_mac_set'


            class AppendMacSet(object):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mac_set_as_text
                
                	Mac Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.mac_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-mac-sets/Cisco-IOS-XR-policy-repository-cfg:append-mac-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.mac_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AppendMacSets.AppendMacSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-mac-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.append_mac_set is not None:
                    for child_ref in self.append_mac_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AppendMacSets']['meta_info']


        class ExtendedCommunityCostSets(object):
            """
            Information about Cost sets
            
            .. attribute:: extended_community_cost_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityCostSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_cost_set
                
                	Extended Community Cost Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-cost-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-cost-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_cost_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-cost-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended_community_cost_set is not None:
                    for child_ref in self.extended_community_cost_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets']['meta_info']


        class RemoveMacSets(object):
            """
            Information about Mac sets
            
            .. attribute:: remove_mac_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.remove_mac_set = YList()
                self.remove_mac_set.parent = self
                self.remove_mac_set.name = 'remove_mac_set'


            class RemoveMacSet(object):
                """
                Remove the entries from the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mac_set_as_text
                
                	Mac Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.mac_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-mac-sets/Cisco-IOS-XR-policy-repository-cfg:remove-mac-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.mac_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-mac-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.remove_mac_set is not None:
                    for child_ref in self.remove_mac_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RemoveMacSets']['meta_info']


        class ExtendedCommunitySooSets(object):
            """
            Information about SOO sets
            
            .. attribute:: extended_community_soo_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunitySooSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_soo_set
                
                	Extended Community SOO Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-soo-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-soo-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_soo_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-soo-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended_community_soo_set is not None:
                    for child_ref in self.extended_community_soo_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets']['meta_info']


        class EsiSets(object):
            """
            Information about Esi sets
            
            .. attribute:: esi_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`EsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EsiSets.EsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.esi_set = YList()
                self.esi_set.parent = self
                self.esi_set.name = 'esi_set'


            class EsiSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: esi_set_as_text
                
                	Esi Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.esi_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:esi-sets/Cisco-IOS-XR-policy-repository-cfg:esi-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.esi_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.EsiSets.EsiSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:esi-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.esi_set is not None:
                    for child_ref in self.esi_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.EsiSets']['meta_info']


        class PrependEsiSets(object):
            """
            Information about Esi sets
            
            .. attribute:: prepend_esi_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.prepend_esi_set = YList()
                self.prepend_esi_set.parent = self
                self.prepend_esi_set.name = 'prepend_esi_set'


            class PrependEsiSet(object):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: esi_set_as_text
                
                	Esi Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.esi_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-esi-sets/Cisco-IOS-XR-policy-repository-cfg:prepend-esi-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.esi_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:prepend-esi-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prepend_esi_set is not None:
                    for child_ref in self.prepend_esi_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PrependEsiSets']['meta_info']


        class AppendEsiSets(object):
            """
            Information about Esi sets
            
            .. attribute:: append_esi_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.append_esi_set = YList()
                self.append_esi_set.parent = self
                self.append_esi_set.name = 'append_esi_set'


            class AppendEsiSet(object):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: esi_set_as_text
                
                	Esi Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.esi_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-esi-sets/Cisco-IOS-XR-policy-repository-cfg:append-esi-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.esi_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:append-esi-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.append_esi_set is not None:
                    for child_ref in self.append_esi_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AppendEsiSets']['meta_info']


        class RemoveEsiSets(object):
            """
            Information about Esi sets
            
            .. attribute:: remove_esi_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.remove_esi_set = YList()
                self.remove_esi_set.parent = self
                self.remove_esi_set.name = 'remove_esi_set'


            class RemoveEsiSet(object):
                """
                Remove the entries from the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: esi_set_as_text
                
                	Esi Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.esi_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-esi-sets/Cisco-IOS-XR-policy-repository-cfg:remove-esi-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.esi_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:remove-esi-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.remove_esi_set is not None:
                    for child_ref in self.remove_esi_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RemoveEsiSets']['meta_info']


        class ExtendedCommunitySegNhSets(object):
            """
            Information about SegNH sets
            
            .. attribute:: extended_community_seg_nh_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunitySegNhSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_seg_nh_set
                
                	Extended Community SegNH Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-seg-nh-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-seg-nh-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_seg_nh_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-seg-nh-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended_community_seg_nh_set is not None:
                    for child_ref in self.extended_community_seg_nh_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets']['meta_info']


        class RdSets(object):
            """
            Information about RD sets
            
            .. attribute:: rd_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`RdSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets.RdSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplrd_set
                
                	RD Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:rd-sets/Cisco-IOS-XR-policy-repository-cfg:rd-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rplrd_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.RdSets.RdSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:rd-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rd_set is not None:
                    for child_ref in self.rd_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.RdSets']['meta_info']


        class PolicyGlobalSetTable(object):
            """
            Information about PolicyGlobal sets
            
            .. attribute:: policy_global_set
            
            	Information about an individual set
            	**type**\:  str
            
            

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
                if self.policy_global_set is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.PolicyGlobalSetTable']['meta_info']


        class ExtendedCommunityBandwidthSets(object):
            """
            Information about Bandwidth sets
            
            .. attribute:: extended_community_bandwidth_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityBandwidthSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_bandwidth_set
                
                	Extended Community Bandwidth Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-bandwidth-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-bandwidth-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_bandwidth_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-bandwidth-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended_community_bandwidth_set is not None:
                    for child_ref in self.extended_community_bandwidth_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets']['meta_info']


        class CommunitySets(object):
            """
            Information about Community sets
            
            .. attribute:: community_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`CommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets.CommunitySet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_community_set
                
                	Community Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:community-sets/Cisco-IOS-XR-policy-repository-cfg:community-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_community_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.CommunitySets.CommunitySet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:community-sets'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.CommunitySets']['meta_info']


        class AsPathSets(object):
            """
            Information about AS Path sets
            
            .. attribute:: as_path_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`AsPathSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets.AsPathSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplas_path_set
                
                	ASPath Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:as-path-sets/Cisco-IOS-XR-policy-repository-cfg:as-path-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rplas_path_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.AsPathSets.AsPathSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:as-path-sets'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.AsPathSets']['meta_info']


        class TagSets(object):
            """
            Information about Tag sets
            
            .. attribute:: tag_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`TagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets.TagSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_tag_set
                
                	Tag Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:tag-sets/Cisco-IOS-XR-policy-repository-cfg:tag-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_tag_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.TagSets.TagSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:tag-sets'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.TagSets']['meta_info']


        class EtagSets(object):
            """
            Information about Etag sets
            
            .. attribute:: etag_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`EtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EtagSets.EtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.etag_set = YList()
                self.etag_set.parent = self
                self.etag_set.name = 'etag_set'


            class EtagSet(object):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: etag_set_as_text
                
                	Etag Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.set_name = None
                    self.etag_set_as_text = None

                @property
                def _common_path(self):
                    if self.set_name is None:
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:etag-sets/Cisco-IOS-XR-policy-repository-cfg:etag-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.etag_set_as_text is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.EtagSets.EtagSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:etag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.etag_set is not None:
                    for child_ref in self.etag_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.EtagSets']['meta_info']


        class ExtendedCommunityRtSets(object):
            """
            Information about RT sets
            
            .. attribute:: extended_community_rt_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityRtSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet>`
            
            

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_rt_set
                
                	Extended Community RT Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

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
                        raise YPYModelError('Key property set_name is None')

                    return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-rt-sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-rt-set[Cisco-IOS-XR-policy-repository-cfg:set-name = ' + str(self.set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.set_name is not None:
                        return True

                    if self.rpl_extended_community_rt_set is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                    return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets/Cisco-IOS-XR-policy-repository-cfg:extended-community-rt-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended_community_rt_set is not None:
                    for child_ref in self.extended_community_rt_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
                return meta._meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy/Cisco-IOS-XR-policy-repository-cfg:sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.append_esi_sets is not None and self.append_esi_sets._has_data():
                return True

            if self.append_etag_sets is not None and self.append_etag_sets._has_data():
                return True

            if self.append_mac_sets is not None and self.append_mac_sets._has_data():
                return True

            if self.as_path_sets is not None and self.as_path_sets._has_data():
                return True

            if self.community_sets is not None and self.community_sets._has_data():
                return True

            if self.esi_sets is not None and self.esi_sets._has_data():
                return True

            if self.etag_sets is not None and self.etag_sets._has_data():
                return True

            if self.extended_community_bandwidth_sets is not None and self.extended_community_bandwidth_sets._has_data():
                return True

            if self.extended_community_cost_sets is not None and self.extended_community_cost_sets._has_data():
                return True

            if self.extended_community_opaque_sets is not None and self.extended_community_opaque_sets._has_data():
                return True

            if self.extended_community_rt_sets is not None and self.extended_community_rt_sets._has_data():
                return True

            if self.extended_community_seg_nh_sets is not None and self.extended_community_seg_nh_sets._has_data():
                return True

            if self.extended_community_soo_sets is not None and self.extended_community_soo_sets._has_data():
                return True

            if self.mac_sets is not None and self.mac_sets._has_data():
                return True

            if self.ospf_area_sets is not None and self.ospf_area_sets._has_data():
                return True

            if self.policy_global_set_table is not None and self.policy_global_set_table._has_data():
                return True

            if self.prefix_sets is not None and self.prefix_sets._has_data():
                return True

            if self.prepend_esi_sets is not None and self.prepend_esi_sets._has_data():
                return True

            if self.prepend_etag_sets is not None and self.prepend_etag_sets._has_data():
                return True

            if self.prepend_mac_sets is not None and self.prepend_mac_sets._has_data():
                return True

            if self.rd_sets is not None and self.rd_sets._has_data():
                return True

            if self.remove_esi_sets is not None and self.remove_esi_sets._has_data():
                return True

            if self.remove_etag_sets is not None and self.remove_etag_sets._has_data():
                return True

            if self.remove_mac_sets is not None and self.remove_mac_sets._has_data():
                return True

            if self.tag_sets is not None and self.tag_sets._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
            return meta._meta_table['RoutingPolicy.Sets']['meta_info']


    class Limits(object):
        """
        Limits for Routing Policy
        
        .. attribute:: maximum_lines_of_policy
        
        	Maximum number of lines of policy configuration that may be configured in total
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**default value**\: 131072
        
        .. attribute:: maximum_number_of_policies
        
        	Maximum number of policies that may be configured
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**default value**\: 5000
        
        

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
            if self.maximum_lines_of_policy is not None:
                return True

            if self.maximum_number_of_policies is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
            return meta._meta_table['RoutingPolicy.Limits']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-policy-repository-cfg:routing-policy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.editor is not None:
            return True

        if self.limits is not None and self.limits._has_data():
            return True

        if self.route_policies is not None and self.route_policies._has_data():
            return True

        if self.sets is not None and self.sets._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_policy_repository_cfg as meta
        return meta._meta_table['RoutingPolicy']['meta_info']


