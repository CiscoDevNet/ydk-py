""" Cisco_IOS_XR_policy_repository_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package configuration.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class RoutingPolicy(Entity):
    """
    Routing policy configuration
    
    .. attribute:: route_policies
    
    	All configured policies
    	**type**\:  :py:class:`RoutePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies>`
    
    .. attribute:: sets
    
    	All configured sets
    	**type**\:  :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets>`
    
    .. attribute:: limits
    
    	Limits for Routing Policy
    	**type**\:  :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Limits>`
    
    .. attribute:: set_exit_as_abort
    
    	Set exit under RPL config to abort
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: editor
    
    	'emacs' or 'vim' or 'nano'
    	**type**\: str
    
    

    """

    _prefix = 'policy-repository-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(RoutingPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-policy"
        self.yang_parent_name = "Cisco-IOS-XR-policy-repository-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("route-policies", ("route_policies", RoutingPolicy.RoutePolicies)), ("sets", ("sets", RoutingPolicy.Sets)), ("limits", ("limits", RoutingPolicy.Limits))])
        self._leafs = OrderedDict([
            ('set_exit_as_abort', (YLeaf(YType.empty, 'set-exit-as-abort'), ['Empty'])),
            ('editor', (YLeaf(YType.str, 'editor'), ['str'])),
        ])
        self.set_exit_as_abort = None
        self.editor = None

        self.route_policies = RoutingPolicy.RoutePolicies()
        self.route_policies.parent = self
        self._children_name_map["route_policies"] = "route-policies"

        self.sets = RoutingPolicy.Sets()
        self.sets.parent = self
        self._children_name_map["sets"] = "sets"

        self.limits = RoutingPolicy.Limits()
        self.limits.parent = self
        self._children_name_map["limits"] = "limits"
        self._segment_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RoutingPolicy, ['set_exit_as_abort', 'editor'], name, value)


    class RoutePolicies(Entity):
        """
        All configured policies
        
        .. attribute:: route_policy
        
        	Information about an individual policy
        	**type**\: list of  		 :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies.RoutePolicy>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(RoutingPolicy.RoutePolicies, self).__init__()

            self.yang_name = "route-policies"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("route-policy", ("route_policy", RoutingPolicy.RoutePolicies.RoutePolicy))])
            self._leafs = OrderedDict()

            self.route_policy = YList(self)
            self._segment_path = lambda: "route-policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.RoutePolicies, [], name, value)


        class RoutePolicy(Entity):
            """
            Information about an individual policy
            
            .. attribute:: route_policy_name  (key)
            
            	Route policy name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: rpl_route_policy
            
            	policy statements
            	**type**\: str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.RoutePolicies.RoutePolicy, self).__init__()

                self.yang_name = "route-policy"
                self.yang_parent_name = "route-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['route_policy_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                    ('rpl_route_policy', (YLeaf(YType.str, 'rpl-route-policy'), ['str'])),
                ])
                self.route_policy_name = None
                self.rpl_route_policy = None
                self._segment_path = lambda: "route-policy" + "[route-policy-name='" + str(self.route_policy_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/route-policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.RoutePolicies.RoutePolicy, ['route_policy_name', 'rpl_route_policy'], name, value)


    class Sets(Entity):
        """
        All configured sets
        
        .. attribute:: prefix_sets
        
        	Information about Prefix sets
        	**type**\:  :py:class:`PrefixSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets>`
        
        .. attribute:: large_community_sets
        
        	Information about Large Community sets
        	**type**\:  :py:class:`LargeCommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.LargeCommunitySets>`
        
        .. attribute:: mac_sets
        
        	Information about Mac sets
        	**type**\:  :py:class:`MacSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.MacSets>`
        
        .. attribute:: extended_community_opaque_sets
        
        	Information about Opaque sets
        	**type**\:  :py:class:`ExtendedCommunityOpaqueSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets>`
        
        .. attribute:: ospf_area_sets
        
        	Information about OSPF Area sets
        	**type**\:  :py:class:`OspfAreaSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets>`
        
        .. attribute:: extended_community_cost_sets
        
        	Information about Cost sets
        	**type**\:  :py:class:`ExtendedCommunityCostSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets>`
        
        .. attribute:: extended_community_soo_sets
        
        	Information about SOO sets
        	**type**\:  :py:class:`ExtendedCommunitySooSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets>`
        
        .. attribute:: esi_sets
        
        	Information about Esi sets
        	**type**\:  :py:class:`EsiSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EsiSets>`
        
        .. attribute:: extended_community_seg_nh_sets
        
        	Information about SegNH sets
        	**type**\:  :py:class:`ExtendedCommunitySegNhSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets>`
        
        .. attribute:: rd_sets
        
        	Information about RD sets
        	**type**\:  :py:class:`RdSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets>`
        
        .. attribute:: policy_global_set_table
        
        	Information about PolicyGlobal sets
        	**type**\:  :py:class:`PolicyGlobalSetTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PolicyGlobalSetTable>`
        
        .. attribute:: extended_community_bandwidth_sets
        
        	Information about Bandwidth sets
        	**type**\:  :py:class:`ExtendedCommunityBandwidthSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets>`
        
        .. attribute:: community_sets
        
        	Information about Community sets
        	**type**\:  :py:class:`CommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets>`
        
        .. attribute:: as_path_sets
        
        	Information about AS Path sets
        	**type**\:  :py:class:`AsPathSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets>`
        
        .. attribute:: tag_sets
        
        	Information about Tag sets
        	**type**\:  :py:class:`TagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets>`
        
        .. attribute:: etag_sets
        
        	Information about Etag sets
        	**type**\:  :py:class:`EtagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EtagSets>`
        
        .. attribute:: extended_community_rt_sets
        
        	Information about RT sets
        	**type**\:  :py:class:`ExtendedCommunityRtSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(RoutingPolicy.Sets, self).__init__()

            self.yang_name = "sets"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefix-sets", ("prefix_sets", RoutingPolicy.Sets.PrefixSets)), ("large-community-sets", ("large_community_sets", RoutingPolicy.Sets.LargeCommunitySets)), ("mac-sets", ("mac_sets", RoutingPolicy.Sets.MacSets)), ("extended-community-opaque-sets", ("extended_community_opaque_sets", RoutingPolicy.Sets.ExtendedCommunityOpaqueSets)), ("ospf-area-sets", ("ospf_area_sets", RoutingPolicy.Sets.OspfAreaSets)), ("extended-community-cost-sets", ("extended_community_cost_sets", RoutingPolicy.Sets.ExtendedCommunityCostSets)), ("extended-community-soo-sets", ("extended_community_soo_sets", RoutingPolicy.Sets.ExtendedCommunitySooSets)), ("esi-sets", ("esi_sets", RoutingPolicy.Sets.EsiSets)), ("extended-community-seg-nh-sets", ("extended_community_seg_nh_sets", RoutingPolicy.Sets.ExtendedCommunitySegNhSets)), ("rd-sets", ("rd_sets", RoutingPolicy.Sets.RdSets)), ("policy-global-set-table", ("policy_global_set_table", RoutingPolicy.Sets.PolicyGlobalSetTable)), ("extended-community-bandwidth-sets", ("extended_community_bandwidth_sets", RoutingPolicy.Sets.ExtendedCommunityBandwidthSets)), ("community-sets", ("community_sets", RoutingPolicy.Sets.CommunitySets)), ("as-path-sets", ("as_path_sets", RoutingPolicy.Sets.AsPathSets)), ("tag-sets", ("tag_sets", RoutingPolicy.Sets.TagSets)), ("etag-sets", ("etag_sets", RoutingPolicy.Sets.EtagSets)), ("extended-community-rt-sets", ("extended_community_rt_sets", RoutingPolicy.Sets.ExtendedCommunityRtSets))])
            self._leafs = OrderedDict()

            self.prefix_sets = RoutingPolicy.Sets.PrefixSets()
            self.prefix_sets.parent = self
            self._children_name_map["prefix_sets"] = "prefix-sets"

            self.large_community_sets = RoutingPolicy.Sets.LargeCommunitySets()
            self.large_community_sets.parent = self
            self._children_name_map["large_community_sets"] = "large-community-sets"

            self.mac_sets = RoutingPolicy.Sets.MacSets()
            self.mac_sets.parent = self
            self._children_name_map["mac_sets"] = "mac-sets"

            self.extended_community_opaque_sets = RoutingPolicy.Sets.ExtendedCommunityOpaqueSets()
            self.extended_community_opaque_sets.parent = self
            self._children_name_map["extended_community_opaque_sets"] = "extended-community-opaque-sets"

            self.ospf_area_sets = RoutingPolicy.Sets.OspfAreaSets()
            self.ospf_area_sets.parent = self
            self._children_name_map["ospf_area_sets"] = "ospf-area-sets"

            self.extended_community_cost_sets = RoutingPolicy.Sets.ExtendedCommunityCostSets()
            self.extended_community_cost_sets.parent = self
            self._children_name_map["extended_community_cost_sets"] = "extended-community-cost-sets"

            self.extended_community_soo_sets = RoutingPolicy.Sets.ExtendedCommunitySooSets()
            self.extended_community_soo_sets.parent = self
            self._children_name_map["extended_community_soo_sets"] = "extended-community-soo-sets"

            self.esi_sets = RoutingPolicy.Sets.EsiSets()
            self.esi_sets.parent = self
            self._children_name_map["esi_sets"] = "esi-sets"

            self.extended_community_seg_nh_sets = RoutingPolicy.Sets.ExtendedCommunitySegNhSets()
            self.extended_community_seg_nh_sets.parent = self
            self._children_name_map["extended_community_seg_nh_sets"] = "extended-community-seg-nh-sets"

            self.rd_sets = RoutingPolicy.Sets.RdSets()
            self.rd_sets.parent = self
            self._children_name_map["rd_sets"] = "rd-sets"

            self.policy_global_set_table = RoutingPolicy.Sets.PolicyGlobalSetTable()
            self.policy_global_set_table.parent = self
            self._children_name_map["policy_global_set_table"] = "policy-global-set-table"

            self.extended_community_bandwidth_sets = RoutingPolicy.Sets.ExtendedCommunityBandwidthSets()
            self.extended_community_bandwidth_sets.parent = self
            self._children_name_map["extended_community_bandwidth_sets"] = "extended-community-bandwidth-sets"

            self.community_sets = RoutingPolicy.Sets.CommunitySets()
            self.community_sets.parent = self
            self._children_name_map["community_sets"] = "community-sets"

            self.as_path_sets = RoutingPolicy.Sets.AsPathSets()
            self.as_path_sets.parent = self
            self._children_name_map["as_path_sets"] = "as-path-sets"

            self.tag_sets = RoutingPolicy.Sets.TagSets()
            self.tag_sets.parent = self
            self._children_name_map["tag_sets"] = "tag-sets"

            self.etag_sets = RoutingPolicy.Sets.EtagSets()
            self.etag_sets.parent = self
            self._children_name_map["etag_sets"] = "etag-sets"

            self.extended_community_rt_sets = RoutingPolicy.Sets.ExtendedCommunityRtSets()
            self.extended_community_rt_sets.parent = self
            self._children_name_map["extended_community_rt_sets"] = "extended-community-rt-sets"
            self._segment_path = lambda: "sets"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.Sets, [], name, value)


        class PrefixSets(Entity):
            """
            Information about Prefix sets
            
            .. attribute:: prefix_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`PrefixSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.PrefixSets, self).__init__()

                self.yang_name = "prefix-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("prefix-set", ("prefix_set", RoutingPolicy.Sets.PrefixSets.PrefixSet))])
                self._leafs = OrderedDict()

                self.prefix_set = YList(self)
                self._segment_path = lambda: "prefix-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PrefixSets, [], name, value)


            class PrefixSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_prefix_set
                
                	prefix statements
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrefixSets.PrefixSet, self).__init__()

                    self.yang_name = "prefix-set"
                    self.yang_parent_name = "prefix-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_prefix_set', (YLeaf(YType.str, 'rpl-prefix-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_prefix_set = None
                    self._segment_path = lambda: "prefix-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prefix-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.PrefixSets.PrefixSet, ['set_name', 'rpl_prefix_set'], name, value)


        class LargeCommunitySets(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: large_community_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`LargeCommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.LargeCommunitySets, self).__init__()

                self.yang_name = "large-community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("large-community-set", ("large_community_set", RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet))])
                self._leafs = OrderedDict()

                self.large_community_set = YList(self)
                self._segment_path = lambda: "large-community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.LargeCommunitySets, [], name, value)


            class LargeCommunitySet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: large_community_set_as_text
                
                	Large Community Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet, self).__init__()

                    self.yang_name = "large-community-set"
                    self.yang_parent_name = "large-community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('large_community_set_as_text', (YLeaf(YType.str, 'large-community-set-as-text'), ['str'])),
                    ])
                    self.set_name = None
                    self.large_community_set_as_text = None
                    self._segment_path = lambda: "large-community-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/large-community-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet, ['set_name', 'large_community_set_as_text'], name, value)


        class MacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: mac_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`MacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.MacSets.MacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.MacSets, self).__init__()

                self.yang_name = "mac-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mac-set", ("mac_set", RoutingPolicy.Sets.MacSets.MacSet))])
                self._leafs = OrderedDict()

                self.mac_set = YList(self)
                self._segment_path = lambda: "mac-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.MacSets, [], name, value)


            class MacSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mac_set_as_text
                
                	Mac Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.MacSets.MacSet, self).__init__()

                    self.yang_name = "mac-set"
                    self.yang_parent_name = "mac-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('mac_set_as_text', (YLeaf(YType.str, 'mac-set-as-text'), ['str'])),
                    ])
                    self.set_name = None
                    self.mac_set_as_text = None
                    self._segment_path = lambda: "mac-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/mac-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.MacSets.MacSet, ['set_name', 'mac_set_as_text'], name, value)


        class ExtendedCommunityOpaqueSets(Entity):
            """
            Information about Opaque sets
            
            .. attribute:: extended_community_opaque_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`ExtendedCommunityOpaqueSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, self).__init__()

                self.yang_name = "extended-community-opaque-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("extended-community-opaque-set", ("extended_community_opaque_set", RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet))])
                self._leafs = OrderedDict()

                self.extended_community_opaque_set = YList(self)
                self._segment_path = lambda: "extended-community-opaque-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, [], name, value)


            class ExtendedCommunityOpaqueSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_opaque_set
                
                	Extended Community Opaque Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, self).__init__()

                    self.yang_name = "extended-community-opaque-set"
                    self.yang_parent_name = "extended-community-opaque-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_extended_community_opaque_set', (YLeaf(YType.str, 'rpl-extended-community-opaque-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_extended_community_opaque_set = None
                    self._segment_path = lambda: "extended-community-opaque-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-opaque-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, ['set_name', 'rpl_extended_community_opaque_set'], name, value)


        class OspfAreaSets(Entity):
            """
            Information about OSPF Area sets
            
            .. attribute:: ospf_area_set
            
            	Information about an individual OSPF area set. Usage\: OSPF area set allows to define named set of area numbers        which can be referenced in the route\-policy. Area sets      may be used during redistribution of the ospf protocol.  Example\: ospf\-area\-set EXAMPLE      1,                                             192.168.1.255                                  end\-set                                        Syntax\: OSPF area number can be entered as 32 bit number or in          the ip address format. See example.                     Semantic\: Area numbers listed in the set will be searched for             a match. In the example these are areas 1 and                  192.168.1.255.                                
            	**type**\: list of  		 :py:class:`OspfAreaSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.OspfAreaSets, self).__init__()

                self.yang_name = "ospf-area-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ospf-area-set", ("ospf_area_set", RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet))])
                self._leafs = OrderedDict()

                self.ospf_area_set = YList(self)
                self._segment_path = lambda: "ospf-area-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.OspfAreaSets, [], name, value)


            class OspfAreaSet(Entity):
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
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplospf_area_set
                
                	OSPF Area Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, self).__init__()

                    self.yang_name = "ospf-area-set"
                    self.yang_parent_name = "ospf-area-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rplospf_area_set', (YLeaf(YType.str, 'rplospf-area-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rplospf_area_set = None
                    self._segment_path = lambda: "ospf-area-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/ospf-area-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, ['set_name', 'rplospf_area_set'], name, value)


        class ExtendedCommunityCostSets(Entity):
            """
            Information about Cost sets
            
            .. attribute:: extended_community_cost_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`ExtendedCommunityCostSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityCostSets, self).__init__()

                self.yang_name = "extended-community-cost-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("extended-community-cost-set", ("extended_community_cost_set", RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet))])
                self._leafs = OrderedDict()

                self.extended_community_cost_set = YList(self)
                self._segment_path = lambda: "extended-community-cost-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCostSets, [], name, value)


            class ExtendedCommunityCostSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_cost_set
                
                	Extended Community Cost Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, self).__init__()

                    self.yang_name = "extended-community-cost-set"
                    self.yang_parent_name = "extended-community-cost-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_extended_community_cost_set', (YLeaf(YType.str, 'rpl-extended-community-cost-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_extended_community_cost_set = None
                    self._segment_path = lambda: "extended-community-cost-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-cost-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, ['set_name', 'rpl_extended_community_cost_set'], name, value)


        class ExtendedCommunitySooSets(Entity):
            """
            Information about SOO sets
            
            .. attribute:: extended_community_soo_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`ExtendedCommunitySooSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySooSets, self).__init__()

                self.yang_name = "extended-community-soo-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("extended-community-soo-set", ("extended_community_soo_set", RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet))])
                self._leafs = OrderedDict()

                self.extended_community_soo_set = YList(self)
                self._segment_path = lambda: "extended-community-soo-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySooSets, [], name, value)


            class ExtendedCommunitySooSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_soo_set
                
                	Extended Community SOO Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, self).__init__()

                    self.yang_name = "extended-community-soo-set"
                    self.yang_parent_name = "extended-community-soo-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_extended_community_soo_set', (YLeaf(YType.str, 'rpl-extended-community-soo-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_extended_community_soo_set = None
                    self._segment_path = lambda: "extended-community-soo-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-soo-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, ['set_name', 'rpl_extended_community_soo_set'], name, value)


        class EsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: esi_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`EsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EsiSets.EsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.EsiSets, self).__init__()

                self.yang_name = "esi-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("esi-set", ("esi_set", RoutingPolicy.Sets.EsiSets.EsiSet))])
                self._leafs = OrderedDict()

                self.esi_set = YList(self)
                self._segment_path = lambda: "esi-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.EsiSets, [], name, value)


            class EsiSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: esi_set_as_text
                
                	Esi Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.EsiSets.EsiSet, self).__init__()

                    self.yang_name = "esi-set"
                    self.yang_parent_name = "esi-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('esi_set_as_text', (YLeaf(YType.str, 'esi-set-as-text'), ['str'])),
                    ])
                    self.set_name = None
                    self.esi_set_as_text = None
                    self._segment_path = lambda: "esi-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/esi-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.EsiSets.EsiSet, ['set_name', 'esi_set_as_text'], name, value)


        class ExtendedCommunitySegNhSets(Entity):
            """
            Information about SegNH sets
            
            .. attribute:: extended_community_seg_nh_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`ExtendedCommunitySegNhSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, self).__init__()

                self.yang_name = "extended-community-seg-nh-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("extended-community-seg-nh-set", ("extended_community_seg_nh_set", RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet))])
                self._leafs = OrderedDict()

                self.extended_community_seg_nh_set = YList(self)
                self._segment_path = lambda: "extended-community-seg-nh-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, [], name, value)


            class ExtendedCommunitySegNhSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_seg_nh_set
                
                	Extended Community SegNH Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, self).__init__()

                    self.yang_name = "extended-community-seg-nh-set"
                    self.yang_parent_name = "extended-community-seg-nh-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_extended_community_seg_nh_set', (YLeaf(YType.str, 'rpl-extended-community-seg-nh-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_extended_community_seg_nh_set = None
                    self._segment_path = lambda: "extended-community-seg-nh-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-seg-nh-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, ['set_name', 'rpl_extended_community_seg_nh_set'], name, value)


        class RdSets(Entity):
            """
            Information about RD sets
            
            .. attribute:: rd_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`RdSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets.RdSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.RdSets, self).__init__()

                self.yang_name = "rd-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rd-set", ("rd_set", RoutingPolicy.Sets.RdSets.RdSet))])
                self._leafs = OrderedDict()

                self.rd_set = YList(self)
                self._segment_path = lambda: "rd-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.RdSets, [], name, value)


            class RdSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplrd_set
                
                	RD Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.RdSets.RdSet, self).__init__()

                    self.yang_name = "rd-set"
                    self.yang_parent_name = "rd-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rplrd_set', (YLeaf(YType.str, 'rplrd-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rplrd_set = None
                    self._segment_path = lambda: "rd-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/rd-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.RdSets.RdSet, ['set_name', 'rplrd_set'], name, value)


        class PolicyGlobalSetTable(Entity):
            """
            Information about PolicyGlobal sets
            
            .. attribute:: policy_global_set
            
            	Information about an individual set
            	**type**\: str
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.PolicyGlobalSetTable, self).__init__()

                self.yang_name = "policy-global-set-table"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('policy_global_set', (YLeaf(YType.str, 'policy-global-set'), ['str'])),
                ])
                self.policy_global_set = None
                self._segment_path = lambda: "policy-global-set-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PolicyGlobalSetTable, ['policy_global_set'], name, value)


        class ExtendedCommunityBandwidthSets(Entity):
            """
            Information about Bandwidth sets
            
            .. attribute:: extended_community_bandwidth_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`ExtendedCommunityBandwidthSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, self).__init__()

                self.yang_name = "extended-community-bandwidth-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("extended-community-bandwidth-set", ("extended_community_bandwidth_set", RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet))])
                self._leafs = OrderedDict()

                self.extended_community_bandwidth_set = YList(self)
                self._segment_path = lambda: "extended-community-bandwidth-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, [], name, value)


            class ExtendedCommunityBandwidthSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_bandwidth_set
                
                	Extended Community Bandwidth Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, self).__init__()

                    self.yang_name = "extended-community-bandwidth-set"
                    self.yang_parent_name = "extended-community-bandwidth-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_extended_community_bandwidth_set', (YLeaf(YType.str, 'rpl-extended-community-bandwidth-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_extended_community_bandwidth_set = None
                    self._segment_path = lambda: "extended-community-bandwidth-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-bandwidth-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, ['set_name', 'rpl_extended_community_bandwidth_set'], name, value)


        class CommunitySets(Entity):
            """
            Information about Community sets
            
            .. attribute:: community_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`CommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets.CommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.CommunitySets, self).__init__()

                self.yang_name = "community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("community-set", ("community_set", RoutingPolicy.Sets.CommunitySets.CommunitySet))])
                self._leafs = OrderedDict()

                self.community_set = YList(self)
                self._segment_path = lambda: "community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.CommunitySets, [], name, value)


            class CommunitySet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_community_set
                
                	Community Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.CommunitySets.CommunitySet, self).__init__()

                    self.yang_name = "community-set"
                    self.yang_parent_name = "community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_community_set', (YLeaf(YType.str, 'rpl-community-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_community_set = None
                    self._segment_path = lambda: "community-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/community-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.CommunitySets.CommunitySet, ['set_name', 'rpl_community_set'], name, value)


        class AsPathSets(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: as_path_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`AsPathSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets.AsPathSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.AsPathSets, self).__init__()

                self.yang_name = "as-path-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("as-path-set", ("as_path_set", RoutingPolicy.Sets.AsPathSets.AsPathSet))])
                self._leafs = OrderedDict()

                self.as_path_set = YList(self)
                self._segment_path = lambda: "as-path-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.AsPathSets, [], name, value)


            class AsPathSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rplas_path_set
                
                	ASPath Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPathSets.AsPathSet, self).__init__()

                    self.yang_name = "as-path-set"
                    self.yang_parent_name = "as-path-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rplas_path_set', (YLeaf(YType.str, 'rplas-path-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rplas_path_set = None
                    self._segment_path = lambda: "as-path-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/as-path-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPathSets.AsPathSet, ['set_name', 'rplas_path_set'], name, value)


        class TagSets(Entity):
            """
            Information about Tag sets
            
            .. attribute:: tag_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`TagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets.TagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.TagSets, self).__init__()

                self.yang_name = "tag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("tag-set", ("tag_set", RoutingPolicy.Sets.TagSets.TagSet))])
                self._leafs = OrderedDict()

                self.tag_set = YList(self)
                self._segment_path = lambda: "tag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.TagSets, [], name, value)


            class TagSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_tag_set
                
                	Tag Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.TagSets.TagSet, self).__init__()

                    self.yang_name = "tag-set"
                    self.yang_parent_name = "tag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_tag_set', (YLeaf(YType.str, 'rpl-tag-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_tag_set = None
                    self._segment_path = lambda: "tag-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/tag-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.TagSets.TagSet, ['set_name', 'rpl_tag_set'], name, value)


        class EtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: etag_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`EtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EtagSets.EtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.EtagSets, self).__init__()

                self.yang_name = "etag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("etag-set", ("etag_set", RoutingPolicy.Sets.EtagSets.EtagSet))])
                self._leafs = OrderedDict()

                self.etag_set = YList(self)
                self._segment_path = lambda: "etag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.EtagSets, [], name, value)


            class EtagSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: etag_set_as_text
                
                	Etag Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.EtagSets.EtagSet, self).__init__()

                    self.yang_name = "etag-set"
                    self.yang_parent_name = "etag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('etag_set_as_text', (YLeaf(YType.str, 'etag-set-as-text'), ['str'])),
                    ])
                    self.set_name = None
                    self.etag_set_as_text = None
                    self._segment_path = lambda: "etag-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/etag-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.EtagSets.EtagSet, ['set_name', 'etag_set_as_text'], name, value)


        class ExtendedCommunityRtSets(Entity):
            """
            Information about RT sets
            
            .. attribute:: extended_community_rt_set
            
            	Information about an individual set
            	**type**\: list of  		 :py:class:`ExtendedCommunityRtSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityRtSets, self).__init__()

                self.yang_name = "extended-community-rt-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("extended-community-rt-set", ("extended_community_rt_set", RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet))])
                self._leafs = OrderedDict()

                self.extended_community_rt_set = YList(self)
                self._segment_path = lambda: "extended-community-rt-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRtSets, [], name, value)


            class ExtendedCommunityRtSet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  (key)
                
                	Set name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rpl_extended_community_rt_set
                
                	Extended Community RT Set
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, self).__init__()

                    self.yang_name = "extended-community-rt-set"
                    self.yang_parent_name = "extended-community-rt-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['set_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('set_name', (YLeaf(YType.str, 'set-name'), ['str'])),
                        ('rpl_extended_community_rt_set', (YLeaf(YType.str, 'rpl-extended-community-rt-set'), ['str'])),
                    ])
                    self.set_name = None
                    self.rpl_extended_community_rt_set = None
                    self._segment_path = lambda: "extended-community-rt-set" + "[set-name='" + str(self.set_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-rt-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, ['set_name', 'rpl_extended_community_rt_set'], name, value)


    class Limits(Entity):
        """
        Limits for Routing Policy
        
        .. attribute:: maximum_lines_of_policy
        
        	Maximum number of lines of policy configuration that may be configured in total
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**default value**\: 131072
        
        .. attribute:: maximum_number_of_policies
        
        	Maximum number of policies that may be configured
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**default value**\: 5000
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(RoutingPolicy.Limits, self).__init__()

            self.yang_name = "limits"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('maximum_lines_of_policy', (YLeaf(YType.uint32, 'maximum-lines-of-policy'), ['int'])),
                ('maximum_number_of_policies', (YLeaf(YType.uint32, 'maximum-number-of-policies'), ['int'])),
            ])
            self.maximum_lines_of_policy = None
            self.maximum_number_of_policies = None
            self._segment_path = lambda: "limits"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.Limits, ['maximum_lines_of_policy', 'maximum_number_of_policies'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

