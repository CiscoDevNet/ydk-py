""" Cisco_IOS_XR_policy_repository_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package configuration.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RoutingPolicy(Entity):
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
    
    .. attribute:: set_exit_as_abort
    
    	Set exit under RPL config to abort
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: sets
    
    	All configured sets
    	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets>`
    
    

    """

    _prefix = 'policy-repository-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-policy"
        self.yang_parent_name = "Cisco-IOS-XR-policy-repository-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"limits" : ("limits", RoutingPolicy.Limits), "route-policies" : ("route_policies", RoutingPolicy.RoutePolicies), "sets" : ("sets", RoutingPolicy.Sets)}
        self._child_list_classes = {}

        self.editor = YLeaf(YType.str, "editor")

        self.set_exit_as_abort = YLeaf(YType.empty, "set-exit-as-abort")

        self.limits = RoutingPolicy.Limits()
        self.limits.parent = self
        self._children_name_map["limits"] = "limits"
        self._children_yang_names.add("limits")

        self.route_policies = RoutingPolicy.RoutePolicies()
        self.route_policies.parent = self
        self._children_name_map["route_policies"] = "route-policies"
        self._children_yang_names.add("route-policies")

        self.sets = RoutingPolicy.Sets()
        self.sets.parent = self
        self._children_name_map["sets"] = "sets"
        self._children_yang_names.add("sets")
        self._segment_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy"

    def __setattr__(self, name, value):
        self._perform_setattr(RoutingPolicy, ['editor', 'set_exit_as_abort'], name, value)


    class Limits(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Limits, self).__init__()

            self.yang_name = "limits"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.maximum_lines_of_policy = YLeaf(YType.int32, "maximum-lines-of-policy")

            self.maximum_number_of_policies = YLeaf(YType.int32, "maximum-number-of-policies")
            self._segment_path = lambda: "limits"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.Limits, ['maximum_lines_of_policy', 'maximum_number_of_policies'], name, value)


    class RoutePolicies(Entity):
        """
        All configured policies
        
        .. attribute:: route_policy
        
        	Information about an individual policy
        	**type**\: list of    :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies.RoutePolicy>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.RoutePolicies, self).__init__()

            self.yang_name = "route-policies"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"route-policy" : ("route_policy", RoutingPolicy.RoutePolicies.RoutePolicy)}

            self.route_policy = YList(self)
            self._segment_path = lambda: "route-policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.RoutePolicies, [], name, value)


        class RoutePolicy(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.RoutePolicies.RoutePolicy, self).__init__()

                self.yang_name = "route-policy"
                self.yang_parent_name = "route-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                self.rpl_route_policy = YLeaf(YType.str, "rpl-route-policy")
                self._segment_path = lambda: "route-policy" + "[route-policy-name='" + self.route_policy_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/route-policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.RoutePolicies.RoutePolicy, ['route_policy_name', 'rpl_route_policy'], name, value)


    class Sets(Entity):
        """
        All configured sets
        
        .. attribute:: append_esi_sets
        
        	Information about Esi sets
        	**type**\:   :py:class:`AppendEsiSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEsiSets>`
        
        .. attribute:: append_etag_sets
        
        	Information about Etag sets
        	**type**\:   :py:class:`AppendEtagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEtagSets>`
        
        .. attribute:: append_large_community_sets
        
        	Information about Large Community sets
        	**type**\:   :py:class:`AppendLargeCommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendLargeCommunitySets>`
        
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
        
        .. attribute:: large_community_sets
        
        	Information about Large Community sets
        	**type**\:   :py:class:`LargeCommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.LargeCommunitySets>`
        
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
        
        .. attribute:: prepend_large_community_sets
        
        	Information about Large Community sets
        	**type**\:   :py:class:`PrependLargeCommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependLargeCommunitySets>`
        
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
        
        .. attribute:: remove_large_community_sets
        
        	Information about Large Community sets
        	**type**\:   :py:class:`RemoveLargeCommunitySets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveLargeCommunitySets>`
        
        .. attribute:: remove_mac_sets
        
        	Information about Mac sets
        	**type**\:   :py:class:`RemoveMacSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveMacSets>`
        
        .. attribute:: tag_sets
        
        	Information about Tag sets
        	**type**\:   :py:class:`TagSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingPolicy.Sets, self).__init__()

            self.yang_name = "sets"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"append-esi-sets" : ("append_esi_sets", RoutingPolicy.Sets.AppendEsiSets), "append-etag-sets" : ("append_etag_sets", RoutingPolicy.Sets.AppendEtagSets), "append-large-community-sets" : ("append_large_community_sets", RoutingPolicy.Sets.AppendLargeCommunitySets), "append-mac-sets" : ("append_mac_sets", RoutingPolicy.Sets.AppendMacSets), "as-path-sets" : ("as_path_sets", RoutingPolicy.Sets.AsPathSets), "community-sets" : ("community_sets", RoutingPolicy.Sets.CommunitySets), "esi-sets" : ("esi_sets", RoutingPolicy.Sets.EsiSets), "etag-sets" : ("etag_sets", RoutingPolicy.Sets.EtagSets), "extended-community-bandwidth-sets" : ("extended_community_bandwidth_sets", RoutingPolicy.Sets.ExtendedCommunityBandwidthSets), "extended-community-cost-sets" : ("extended_community_cost_sets", RoutingPolicy.Sets.ExtendedCommunityCostSets), "extended-community-opaque-sets" : ("extended_community_opaque_sets", RoutingPolicy.Sets.ExtendedCommunityOpaqueSets), "extended-community-rt-sets" : ("extended_community_rt_sets", RoutingPolicy.Sets.ExtendedCommunityRtSets), "extended-community-seg-nh-sets" : ("extended_community_seg_nh_sets", RoutingPolicy.Sets.ExtendedCommunitySegNhSets), "extended-community-soo-sets" : ("extended_community_soo_sets", RoutingPolicy.Sets.ExtendedCommunitySooSets), "large-community-sets" : ("large_community_sets", RoutingPolicy.Sets.LargeCommunitySets), "mac-sets" : ("mac_sets", RoutingPolicy.Sets.MacSets), "ospf-area-sets" : ("ospf_area_sets", RoutingPolicy.Sets.OspfAreaSets), "policy-global-set-table" : ("policy_global_set_table", RoutingPolicy.Sets.PolicyGlobalSetTable), "prefix-sets" : ("prefix_sets", RoutingPolicy.Sets.PrefixSets), "prepend-esi-sets" : ("prepend_esi_sets", RoutingPolicy.Sets.PrependEsiSets), "prepend-etag-sets" : ("prepend_etag_sets", RoutingPolicy.Sets.PrependEtagSets), "prepend-large-community-sets" : ("prepend_large_community_sets", RoutingPolicy.Sets.PrependLargeCommunitySets), "prepend-mac-sets" : ("prepend_mac_sets", RoutingPolicy.Sets.PrependMacSets), "rd-sets" : ("rd_sets", RoutingPolicy.Sets.RdSets), "remove-esi-sets" : ("remove_esi_sets", RoutingPolicy.Sets.RemoveEsiSets), "remove-etag-sets" : ("remove_etag_sets", RoutingPolicy.Sets.RemoveEtagSets), "remove-large-community-sets" : ("remove_large_community_sets", RoutingPolicy.Sets.RemoveLargeCommunitySets), "remove-mac-sets" : ("remove_mac_sets", RoutingPolicy.Sets.RemoveMacSets), "tag-sets" : ("tag_sets", RoutingPolicy.Sets.TagSets)}
            self._child_list_classes = {}

            self.append_esi_sets = RoutingPolicy.Sets.AppendEsiSets()
            self.append_esi_sets.parent = self
            self._children_name_map["append_esi_sets"] = "append-esi-sets"
            self._children_yang_names.add("append-esi-sets")

            self.append_etag_sets = RoutingPolicy.Sets.AppendEtagSets()
            self.append_etag_sets.parent = self
            self._children_name_map["append_etag_sets"] = "append-etag-sets"
            self._children_yang_names.add("append-etag-sets")

            self.append_large_community_sets = RoutingPolicy.Sets.AppendLargeCommunitySets()
            self.append_large_community_sets.parent = self
            self._children_name_map["append_large_community_sets"] = "append-large-community-sets"
            self._children_yang_names.add("append-large-community-sets")

            self.append_mac_sets = RoutingPolicy.Sets.AppendMacSets()
            self.append_mac_sets.parent = self
            self._children_name_map["append_mac_sets"] = "append-mac-sets"
            self._children_yang_names.add("append-mac-sets")

            self.as_path_sets = RoutingPolicy.Sets.AsPathSets()
            self.as_path_sets.parent = self
            self._children_name_map["as_path_sets"] = "as-path-sets"
            self._children_yang_names.add("as-path-sets")

            self.community_sets = RoutingPolicy.Sets.CommunitySets()
            self.community_sets.parent = self
            self._children_name_map["community_sets"] = "community-sets"
            self._children_yang_names.add("community-sets")

            self.esi_sets = RoutingPolicy.Sets.EsiSets()
            self.esi_sets.parent = self
            self._children_name_map["esi_sets"] = "esi-sets"
            self._children_yang_names.add("esi-sets")

            self.etag_sets = RoutingPolicy.Sets.EtagSets()
            self.etag_sets.parent = self
            self._children_name_map["etag_sets"] = "etag-sets"
            self._children_yang_names.add("etag-sets")

            self.extended_community_bandwidth_sets = RoutingPolicy.Sets.ExtendedCommunityBandwidthSets()
            self.extended_community_bandwidth_sets.parent = self
            self._children_name_map["extended_community_bandwidth_sets"] = "extended-community-bandwidth-sets"
            self._children_yang_names.add("extended-community-bandwidth-sets")

            self.extended_community_cost_sets = RoutingPolicy.Sets.ExtendedCommunityCostSets()
            self.extended_community_cost_sets.parent = self
            self._children_name_map["extended_community_cost_sets"] = "extended-community-cost-sets"
            self._children_yang_names.add("extended-community-cost-sets")

            self.extended_community_opaque_sets = RoutingPolicy.Sets.ExtendedCommunityOpaqueSets()
            self.extended_community_opaque_sets.parent = self
            self._children_name_map["extended_community_opaque_sets"] = "extended-community-opaque-sets"
            self._children_yang_names.add("extended-community-opaque-sets")

            self.extended_community_rt_sets = RoutingPolicy.Sets.ExtendedCommunityRtSets()
            self.extended_community_rt_sets.parent = self
            self._children_name_map["extended_community_rt_sets"] = "extended-community-rt-sets"
            self._children_yang_names.add("extended-community-rt-sets")

            self.extended_community_seg_nh_sets = RoutingPolicy.Sets.ExtendedCommunitySegNhSets()
            self.extended_community_seg_nh_sets.parent = self
            self._children_name_map["extended_community_seg_nh_sets"] = "extended-community-seg-nh-sets"
            self._children_yang_names.add("extended-community-seg-nh-sets")

            self.extended_community_soo_sets = RoutingPolicy.Sets.ExtendedCommunitySooSets()
            self.extended_community_soo_sets.parent = self
            self._children_name_map["extended_community_soo_sets"] = "extended-community-soo-sets"
            self._children_yang_names.add("extended-community-soo-sets")

            self.large_community_sets = RoutingPolicy.Sets.LargeCommunitySets()
            self.large_community_sets.parent = self
            self._children_name_map["large_community_sets"] = "large-community-sets"
            self._children_yang_names.add("large-community-sets")

            self.mac_sets = RoutingPolicy.Sets.MacSets()
            self.mac_sets.parent = self
            self._children_name_map["mac_sets"] = "mac-sets"
            self._children_yang_names.add("mac-sets")

            self.ospf_area_sets = RoutingPolicy.Sets.OspfAreaSets()
            self.ospf_area_sets.parent = self
            self._children_name_map["ospf_area_sets"] = "ospf-area-sets"
            self._children_yang_names.add("ospf-area-sets")

            self.policy_global_set_table = RoutingPolicy.Sets.PolicyGlobalSetTable()
            self.policy_global_set_table.parent = self
            self._children_name_map["policy_global_set_table"] = "policy-global-set-table"
            self._children_yang_names.add("policy-global-set-table")

            self.prefix_sets = RoutingPolicy.Sets.PrefixSets()
            self.prefix_sets.parent = self
            self._children_name_map["prefix_sets"] = "prefix-sets"
            self._children_yang_names.add("prefix-sets")

            self.prepend_esi_sets = RoutingPolicy.Sets.PrependEsiSets()
            self.prepend_esi_sets.parent = self
            self._children_name_map["prepend_esi_sets"] = "prepend-esi-sets"
            self._children_yang_names.add("prepend-esi-sets")

            self.prepend_etag_sets = RoutingPolicy.Sets.PrependEtagSets()
            self.prepend_etag_sets.parent = self
            self._children_name_map["prepend_etag_sets"] = "prepend-etag-sets"
            self._children_yang_names.add("prepend-etag-sets")

            self.prepend_large_community_sets = RoutingPolicy.Sets.PrependLargeCommunitySets()
            self.prepend_large_community_sets.parent = self
            self._children_name_map["prepend_large_community_sets"] = "prepend-large-community-sets"
            self._children_yang_names.add("prepend-large-community-sets")

            self.prepend_mac_sets = RoutingPolicy.Sets.PrependMacSets()
            self.prepend_mac_sets.parent = self
            self._children_name_map["prepend_mac_sets"] = "prepend-mac-sets"
            self._children_yang_names.add("prepend-mac-sets")

            self.rd_sets = RoutingPolicy.Sets.RdSets()
            self.rd_sets.parent = self
            self._children_name_map["rd_sets"] = "rd-sets"
            self._children_yang_names.add("rd-sets")

            self.remove_esi_sets = RoutingPolicy.Sets.RemoveEsiSets()
            self.remove_esi_sets.parent = self
            self._children_name_map["remove_esi_sets"] = "remove-esi-sets"
            self._children_yang_names.add("remove-esi-sets")

            self.remove_etag_sets = RoutingPolicy.Sets.RemoveEtagSets()
            self.remove_etag_sets.parent = self
            self._children_name_map["remove_etag_sets"] = "remove-etag-sets"
            self._children_yang_names.add("remove-etag-sets")

            self.remove_large_community_sets = RoutingPolicy.Sets.RemoveLargeCommunitySets()
            self.remove_large_community_sets.parent = self
            self._children_name_map["remove_large_community_sets"] = "remove-large-community-sets"
            self._children_yang_names.add("remove-large-community-sets")

            self.remove_mac_sets = RoutingPolicy.Sets.RemoveMacSets()
            self.remove_mac_sets.parent = self
            self._children_name_map["remove_mac_sets"] = "remove-mac-sets"
            self._children_yang_names.add("remove-mac-sets")

            self.tag_sets = RoutingPolicy.Sets.TagSets()
            self.tag_sets.parent = self
            self._children_name_map["tag_sets"] = "tag-sets"
            self._children_yang_names.add("tag-sets")
            self._segment_path = lambda: "sets"
            self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self._segment_path()


        class AppendEsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: append_esi_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendEsiSets, self).__init__()

                self.yang_name = "append-esi-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"append-esi-set" : ("append_esi_set", RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet)}

                self.append_esi_set = YList(self)
                self._segment_path = lambda: "append-esi-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.AppendEsiSets, [], name, value)


            class AppendEsiSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet, self).__init__()

                    self.yang_name = "append-esi-set"
                    self.yang_parent_name = "append-esi-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")
                    self._segment_path = lambda: "append-esi-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-esi-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet, ['set_name', 'esi_set_as_text'], name, value)


        class AppendEtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: append_etag_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendEtagSets, self).__init__()

                self.yang_name = "append-etag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"append-etag-set" : ("append_etag_set", RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet)}

                self.append_etag_set = YList(self)
                self._segment_path = lambda: "append-etag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.AppendEtagSets, [], name, value)


            class AppendEtagSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet, self).__init__()

                    self.yang_name = "append-etag-set"
                    self.yang_parent_name = "append-etag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")
                    self._segment_path = lambda: "append-etag-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-etag-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet, ['set_name', 'etag_set_as_text'], name, value)


        class AppendLargeCommunitySets(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: append_large_community_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendLargeCommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendLargeCommunitySets.AppendLargeCommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendLargeCommunitySets, self).__init__()

                self.yang_name = "append-large-community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"append-large-community-set" : ("append_large_community_set", RoutingPolicy.Sets.AppendLargeCommunitySets.AppendLargeCommunitySet)}

                self.append_large_community_set = YList(self)
                self._segment_path = lambda: "append-large-community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.AppendLargeCommunitySets, [], name, value)


            class AppendLargeCommunitySet(Entity):
                """
                Append the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: large_community_set_as_text
                
                	Large Community Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendLargeCommunitySets.AppendLargeCommunitySet, self).__init__()

                    self.yang_name = "append-large-community-set"
                    self.yang_parent_name = "append-large-community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.large_community_set_as_text = YLeaf(YType.str, "large-community-set-as-text")
                    self._segment_path = lambda: "append-large-community-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-large-community-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AppendLargeCommunitySets.AppendLargeCommunitySet, ['set_name', 'large_community_set_as_text'], name, value)


        class AppendMacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: append_mac_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendMacSets.AppendMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendMacSets, self).__init__()

                self.yang_name = "append-mac-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"append-mac-set" : ("append_mac_set", RoutingPolicy.Sets.AppendMacSets.AppendMacSet)}

                self.append_mac_set = YList(self)
                self._segment_path = lambda: "append-mac-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.AppendMacSets, [], name, value)


            class AppendMacSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendMacSets.AppendMacSet, self).__init__()

                    self.yang_name = "append-mac-set"
                    self.yang_parent_name = "append-mac-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")
                    self._segment_path = lambda: "append-mac-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-mac-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AppendMacSets.AppendMacSet, ['set_name', 'mac_set_as_text'], name, value)


        class AsPathSets(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: as_path_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`AsPathSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets.AsPathSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.AsPathSets, self).__init__()

                self.yang_name = "as-path-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"as-path-set" : ("as_path_set", RoutingPolicy.Sets.AsPathSets.AsPathSet)}

                self.as_path_set = YList(self)
                self._segment_path = lambda: "as-path-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.AsPathSets, [], name, value)


            class AsPathSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPathSets.AsPathSet, self).__init__()

                    self.yang_name = "as-path-set"
                    self.yang_parent_name = "as-path-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rplas_path_set = YLeaf(YType.str, "rplas-path-set")
                    self._segment_path = lambda: "as-path-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/as-path-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.AsPathSets.AsPathSet, ['set_name', 'rplas_path_set'], name, value)


        class CommunitySets(Entity):
            """
            Information about Community sets
            
            .. attribute:: community_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`CommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets.CommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.CommunitySets, self).__init__()

                self.yang_name = "community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"community-set" : ("community_set", RoutingPolicy.Sets.CommunitySets.CommunitySet)}

                self.community_set = YList(self)
                self._segment_path = lambda: "community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.CommunitySets, [], name, value)


            class CommunitySet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.CommunitySets.CommunitySet, self).__init__()

                    self.yang_name = "community-set"
                    self.yang_parent_name = "community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_community_set = YLeaf(YType.str, "rpl-community-set")
                    self._segment_path = lambda: "community-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/community-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.CommunitySets.CommunitySet, ['set_name', 'rpl_community_set'], name, value)


        class EsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: esi_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`EsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EsiSets.EsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.EsiSets, self).__init__()

                self.yang_name = "esi-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"esi-set" : ("esi_set", RoutingPolicy.Sets.EsiSets.EsiSet)}

                self.esi_set = YList(self)
                self._segment_path = lambda: "esi-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.EsiSets, [], name, value)


            class EsiSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.EsiSets.EsiSet, self).__init__()

                    self.yang_name = "esi-set"
                    self.yang_parent_name = "esi-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")
                    self._segment_path = lambda: "esi-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/esi-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.EsiSets.EsiSet, ['set_name', 'esi_set_as_text'], name, value)


        class EtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: etag_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`EtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EtagSets.EtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.EtagSets, self).__init__()

                self.yang_name = "etag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"etag-set" : ("etag_set", RoutingPolicy.Sets.EtagSets.EtagSet)}

                self.etag_set = YList(self)
                self._segment_path = lambda: "etag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.EtagSets, [], name, value)


            class EtagSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.EtagSets.EtagSet, self).__init__()

                    self.yang_name = "etag-set"
                    self.yang_parent_name = "etag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")
                    self._segment_path = lambda: "etag-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/etag-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.EtagSets.EtagSet, ['set_name', 'etag_set_as_text'], name, value)


        class ExtendedCommunityBandwidthSets(Entity):
            """
            Information about Bandwidth sets
            
            .. attribute:: extended_community_bandwidth_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityBandwidthSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, self).__init__()

                self.yang_name = "extended-community-bandwidth-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"extended-community-bandwidth-set" : ("extended_community_bandwidth_set", RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet)}

                self.extended_community_bandwidth_set = YList(self)
                self._segment_path = lambda: "extended-community-bandwidth-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, [], name, value)


            class ExtendedCommunityBandwidthSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, self).__init__()

                    self.yang_name = "extended-community-bandwidth-set"
                    self.yang_parent_name = "extended-community-bandwidth-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_bandwidth_set = YLeaf(YType.str, "rpl-extended-community-bandwidth-set")
                    self._segment_path = lambda: "extended-community-bandwidth-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-bandwidth-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, ['set_name', 'rpl_extended_community_bandwidth_set'], name, value)


        class ExtendedCommunityCostSets(Entity):
            """
            Information about Cost sets
            
            .. attribute:: extended_community_cost_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityCostSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityCostSets, self).__init__()

                self.yang_name = "extended-community-cost-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"extended-community-cost-set" : ("extended_community_cost_set", RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet)}

                self.extended_community_cost_set = YList(self)
                self._segment_path = lambda: "extended-community-cost-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCostSets, [], name, value)


            class ExtendedCommunityCostSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, self).__init__()

                    self.yang_name = "extended-community-cost-set"
                    self.yang_parent_name = "extended-community-cost-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_cost_set = YLeaf(YType.str, "rpl-extended-community-cost-set")
                    self._segment_path = lambda: "extended-community-cost-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-cost-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, ['set_name', 'rpl_extended_community_cost_set'], name, value)


        class ExtendedCommunityOpaqueSets(Entity):
            """
            Information about Opaque sets
            
            .. attribute:: extended_community_opaque_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityOpaqueSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, self).__init__()

                self.yang_name = "extended-community-opaque-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"extended-community-opaque-set" : ("extended_community_opaque_set", RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet)}

                self.extended_community_opaque_set = YList(self)
                self._segment_path = lambda: "extended-community-opaque-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, [], name, value)


            class ExtendedCommunityOpaqueSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, self).__init__()

                    self.yang_name = "extended-community-opaque-set"
                    self.yang_parent_name = "extended-community-opaque-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_opaque_set = YLeaf(YType.str, "rpl-extended-community-opaque-set")
                    self._segment_path = lambda: "extended-community-opaque-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-opaque-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, ['set_name', 'rpl_extended_community_opaque_set'], name, value)


        class ExtendedCommunityRtSets(Entity):
            """
            Information about RT sets
            
            .. attribute:: extended_community_rt_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityRtSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityRtSets, self).__init__()

                self.yang_name = "extended-community-rt-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"extended-community-rt-set" : ("extended_community_rt_set", RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet)}

                self.extended_community_rt_set = YList(self)
                self._segment_path = lambda: "extended-community-rt-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRtSets, [], name, value)


            class ExtendedCommunityRtSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, self).__init__()

                    self.yang_name = "extended-community-rt-set"
                    self.yang_parent_name = "extended-community-rt-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_rt_set = YLeaf(YType.str, "rpl-extended-community-rt-set")
                    self._segment_path = lambda: "extended-community-rt-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-rt-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, ['set_name', 'rpl_extended_community_rt_set'], name, value)


        class ExtendedCommunitySegNhSets(Entity):
            """
            Information about SegNH sets
            
            .. attribute:: extended_community_seg_nh_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunitySegNhSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, self).__init__()

                self.yang_name = "extended-community-seg-nh-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"extended-community-seg-nh-set" : ("extended_community_seg_nh_set", RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet)}

                self.extended_community_seg_nh_set = YList(self)
                self._segment_path = lambda: "extended-community-seg-nh-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, [], name, value)


            class ExtendedCommunitySegNhSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, self).__init__()

                    self.yang_name = "extended-community-seg-nh-set"
                    self.yang_parent_name = "extended-community-seg-nh-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_seg_nh_set = YLeaf(YType.str, "rpl-extended-community-seg-nh-set")
                    self._segment_path = lambda: "extended-community-seg-nh-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-seg-nh-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, ['set_name', 'rpl_extended_community_seg_nh_set'], name, value)


        class ExtendedCommunitySooSets(Entity):
            """
            Information about SOO sets
            
            .. attribute:: extended_community_soo_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunitySooSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySooSets, self).__init__()

                self.yang_name = "extended-community-soo-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"extended-community-soo-set" : ("extended_community_soo_set", RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet)}

                self.extended_community_soo_set = YList(self)
                self._segment_path = lambda: "extended-community-soo-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySooSets, [], name, value)


            class ExtendedCommunitySooSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, self).__init__()

                    self.yang_name = "extended-community-soo-set"
                    self.yang_parent_name = "extended-community-soo-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_soo_set = YLeaf(YType.str, "rpl-extended-community-soo-set")
                    self._segment_path = lambda: "extended-community-soo-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-soo-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, ['set_name', 'rpl_extended_community_soo_set'], name, value)


        class LargeCommunitySets(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: large_community_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`LargeCommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.LargeCommunitySets, self).__init__()

                self.yang_name = "large-community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"large-community-set" : ("large_community_set", RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet)}

                self.large_community_set = YList(self)
                self._segment_path = lambda: "large-community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.LargeCommunitySets, [], name, value)


            class LargeCommunitySet(Entity):
                """
                Information about an individual set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: large_community_set_as_text
                
                	Large Community Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet, self).__init__()

                    self.yang_name = "large-community-set"
                    self.yang_parent_name = "large-community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.large_community_set_as_text = YLeaf(YType.str, "large-community-set-as-text")
                    self._segment_path = lambda: "large-community-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/large-community-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.LargeCommunitySets.LargeCommunitySet, ['set_name', 'large_community_set_as_text'], name, value)


        class MacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: mac_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`MacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.MacSets.MacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.MacSets, self).__init__()

                self.yang_name = "mac-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"mac-set" : ("mac_set", RoutingPolicy.Sets.MacSets.MacSet)}

                self.mac_set = YList(self)
                self._segment_path = lambda: "mac-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.MacSets, [], name, value)


            class MacSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.MacSets.MacSet, self).__init__()

                    self.yang_name = "mac-set"
                    self.yang_parent_name = "mac-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")
                    self._segment_path = lambda: "mac-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/mac-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.MacSets.MacSet, ['set_name', 'mac_set_as_text'], name, value)


        class OspfAreaSets(Entity):
            """
            Information about OSPF Area sets
            
            .. attribute:: ospf_area_set
            
            	Information about an individual OSPF area set. Usage\: OSPF area set allows to define named set of area numbers        which can be referenced in the route\-policy. Area sets      may be used during redistribution of the ospf protocol.  Example\: ospf\-area\-set EXAMPLE      1,                                             192.168.1.255                                  end\-set                                        Syntax\: OSPF area number can be entered as 32 bit number or in          the ip address format. See example.                     Semantic\: Area numbers listed in the set will be searched for             a match. In the example these are areas 1 and                  192.168.1.255.                                
            	**type**\: list of    :py:class:`OspfAreaSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.OspfAreaSets, self).__init__()

                self.yang_name = "ospf-area-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ospf-area-set" : ("ospf_area_set", RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet)}

                self.ospf_area_set = YList(self)
                self._segment_path = lambda: "ospf-area-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, self).__init__()

                    self.yang_name = "ospf-area-set"
                    self.yang_parent_name = "ospf-area-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rplospf_area_set = YLeaf(YType.str, "rplospf-area-set")
                    self._segment_path = lambda: "ospf-area-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/ospf-area-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, ['set_name', 'rplospf_area_set'], name, value)


        class PolicyGlobalSetTable(Entity):
            """
            Information about PolicyGlobal sets
            
            .. attribute:: policy_global_set
            
            	Information about an individual set
            	**type**\:  str
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.PolicyGlobalSetTable, self).__init__()

                self.yang_name = "policy-global-set-table"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.policy_global_set = YLeaf(YType.str, "policy-global-set")
                self._segment_path = lambda: "policy-global-set-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PolicyGlobalSetTable, ['policy_global_set'], name, value)


        class PrefixSets(Entity):
            """
            Information about Prefix sets
            
            .. attribute:: prefix_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`PrefixSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.PrefixSets, self).__init__()

                self.yang_name = "prefix-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"prefix-set" : ("prefix_set", RoutingPolicy.Sets.PrefixSets.PrefixSet)}

                self.prefix_set = YList(self)
                self._segment_path = lambda: "prefix-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PrefixSets, [], name, value)


            class PrefixSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrefixSets.PrefixSet, self).__init__()

                    self.yang_name = "prefix-set"
                    self.yang_parent_name = "prefix-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_prefix_set = YLeaf(YType.str, "rpl-prefix-set")
                    self._segment_path = lambda: "prefix-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prefix-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.PrefixSets.PrefixSet, ['set_name', 'rpl_prefix_set'], name, value)


        class PrependEsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: prepend_esi_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependEsiSets, self).__init__()

                self.yang_name = "prepend-esi-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"prepend-esi-set" : ("prepend_esi_set", RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet)}

                self.prepend_esi_set = YList(self)
                self._segment_path = lambda: "prepend-esi-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PrependEsiSets, [], name, value)


            class PrependEsiSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet, self).__init__()

                    self.yang_name = "prepend-esi-set"
                    self.yang_parent_name = "prepend-esi-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")
                    self._segment_path = lambda: "prepend-esi-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-esi-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet, ['set_name', 'esi_set_as_text'], name, value)


        class PrependEtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: prepend_etag_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependEtagSets, self).__init__()

                self.yang_name = "prepend-etag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"prepend-etag-set" : ("prepend_etag_set", RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet)}

                self.prepend_etag_set = YList(self)
                self._segment_path = lambda: "prepend-etag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PrependEtagSets, [], name, value)


            class PrependEtagSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet, self).__init__()

                    self.yang_name = "prepend-etag-set"
                    self.yang_parent_name = "prepend-etag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")
                    self._segment_path = lambda: "prepend-etag-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-etag-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet, ['set_name', 'etag_set_as_text'], name, value)


        class PrependLargeCommunitySets(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: prepend_large_community_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependLargeCommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependLargeCommunitySets.PrependLargeCommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependLargeCommunitySets, self).__init__()

                self.yang_name = "prepend-large-community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"prepend-large-community-set" : ("prepend_large_community_set", RoutingPolicy.Sets.PrependLargeCommunitySets.PrependLargeCommunitySet)}

                self.prepend_large_community_set = YList(self)
                self._segment_path = lambda: "prepend-large-community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PrependLargeCommunitySets, [], name, value)


            class PrependLargeCommunitySet(Entity):
                """
                Prepend the entries to the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: large_community_set_as_text
                
                	Large Community Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependLargeCommunitySets.PrependLargeCommunitySet, self).__init__()

                    self.yang_name = "prepend-large-community-set"
                    self.yang_parent_name = "prepend-large-community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.large_community_set_as_text = YLeaf(YType.str, "large-community-set-as-text")
                    self._segment_path = lambda: "prepend-large-community-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-large-community-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.PrependLargeCommunitySets.PrependLargeCommunitySet, ['set_name', 'large_community_set_as_text'], name, value)


        class PrependMacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: prepend_mac_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependMacSets.PrependMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependMacSets, self).__init__()

                self.yang_name = "prepend-mac-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"prepend-mac-set" : ("prepend_mac_set", RoutingPolicy.Sets.PrependMacSets.PrependMacSet)}

                self.prepend_mac_set = YList(self)
                self._segment_path = lambda: "prepend-mac-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.PrependMacSets, [], name, value)


            class PrependMacSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependMacSets.PrependMacSet, self).__init__()

                    self.yang_name = "prepend-mac-set"
                    self.yang_parent_name = "prepend-mac-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")
                    self._segment_path = lambda: "prepend-mac-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-mac-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.PrependMacSets.PrependMacSet, ['set_name', 'mac_set_as_text'], name, value)


        class RdSets(Entity):
            """
            Information about RD sets
            
            .. attribute:: rd_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`RdSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets.RdSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.RdSets, self).__init__()

                self.yang_name = "rd-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"rd-set" : ("rd_set", RoutingPolicy.Sets.RdSets.RdSet)}

                self.rd_set = YList(self)
                self._segment_path = lambda: "rd-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.RdSets, [], name, value)


            class RdSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.RdSets.RdSet, self).__init__()

                    self.yang_name = "rd-set"
                    self.yang_parent_name = "rd-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rplrd_set = YLeaf(YType.str, "rplrd-set")
                    self._segment_path = lambda: "rd-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/rd-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.RdSets.RdSet, ['set_name', 'rplrd_set'], name, value)


        class RemoveEsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: remove_esi_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveEsiSets, self).__init__()

                self.yang_name = "remove-esi-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"remove-esi-set" : ("remove_esi_set", RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet)}

                self.remove_esi_set = YList(self)
                self._segment_path = lambda: "remove-esi-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.RemoveEsiSets, [], name, value)


            class RemoveEsiSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet, self).__init__()

                    self.yang_name = "remove-esi-set"
                    self.yang_parent_name = "remove-esi-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")
                    self._segment_path = lambda: "remove-esi-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-esi-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet, ['set_name', 'esi_set_as_text'], name, value)


        class RemoveEtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: remove_etag_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveEtagSets, self).__init__()

                self.yang_name = "remove-etag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"remove-etag-set" : ("remove_etag_set", RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet)}

                self.remove_etag_set = YList(self)
                self._segment_path = lambda: "remove-etag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.RemoveEtagSets, [], name, value)


            class RemoveEtagSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet, self).__init__()

                    self.yang_name = "remove-etag-set"
                    self.yang_parent_name = "remove-etag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")
                    self._segment_path = lambda: "remove-etag-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-etag-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet, ['set_name', 'etag_set_as_text'], name, value)


        class RemoveLargeCommunitySets(Entity):
            """
            Information about Large Community sets
            
            .. attribute:: remove_large_community_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveLargeCommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveLargeCommunitySets.RemoveLargeCommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveLargeCommunitySets, self).__init__()

                self.yang_name = "remove-large-community-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"remove-large-community-set" : ("remove_large_community_set", RoutingPolicy.Sets.RemoveLargeCommunitySets.RemoveLargeCommunitySet)}

                self.remove_large_community_set = YList(self)
                self._segment_path = lambda: "remove-large-community-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.RemoveLargeCommunitySets, [], name, value)


            class RemoveLargeCommunitySet(Entity):
                """
                Remove the entries from the existing set
                
                .. attribute:: set_name  <key>
                
                	Set name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: large_community_set_as_text
                
                	Large Community Set
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'policy-repository-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveLargeCommunitySets.RemoveLargeCommunitySet, self).__init__()

                    self.yang_name = "remove-large-community-set"
                    self.yang_parent_name = "remove-large-community-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.large_community_set_as_text = YLeaf(YType.str, "large-community-set-as-text")
                    self._segment_path = lambda: "remove-large-community-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-large-community-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.RemoveLargeCommunitySets.RemoveLargeCommunitySet, ['set_name', 'large_community_set_as_text'], name, value)


        class RemoveMacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: remove_mac_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveMacSets, self).__init__()

                self.yang_name = "remove-mac-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"remove-mac-set" : ("remove_mac_set", RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet)}

                self.remove_mac_set = YList(self)
                self._segment_path = lambda: "remove-mac-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.RemoveMacSets, [], name, value)


            class RemoveMacSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet, self).__init__()

                    self.yang_name = "remove-mac-set"
                    self.yang_parent_name = "remove-mac-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")
                    self._segment_path = lambda: "remove-mac-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-mac-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet, ['set_name', 'mac_set_as_text'], name, value)


        class TagSets(Entity):
            """
            Information about Tag sets
            
            .. attribute:: tag_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`TagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets.TagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(RoutingPolicy.Sets.TagSets, self).__init__()

                self.yang_name = "tag-sets"
                self.yang_parent_name = "sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"tag-set" : ("tag_set", RoutingPolicy.Sets.TagSets.TagSet)}

                self.tag_set = YList(self)
                self._segment_path = lambda: "tag-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.Sets.TagSets, [], name, value)


            class TagSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(RoutingPolicy.Sets.TagSets.TagSet, self).__init__()

                    self.yang_name = "tag-set"
                    self.yang_parent_name = "tag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_tag_set = YLeaf(YType.str, "rpl-tag-set")
                    self._segment_path = lambda: "tag-set" + "[set-name='" + self.set_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/tag-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.Sets.TagSets.TagSet, ['set_name', 'rpl_tag_set'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

