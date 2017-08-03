""" Cisco_IOS_XR_policy_repository_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR policy\-repository package configuration.

This module contains definitions
for the following management objects\:
  routing\-policy\: Routing policy configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    
    .. attribute:: sets
    
    	All configured sets
    	**type**\:   :py:class:`Sets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets>`
    
    

    """

    _prefix = 'policy-repository-cfg'
    _revision = '2015-08-27'

    def __init__(self):
        super(RoutingPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-policy"
        self.yang_parent_name = "Cisco-IOS-XR-policy-repository-cfg"

        self.editor = YLeaf(YType.str, "editor")

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

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("editor") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(RoutingPolicy, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(RoutingPolicy, self).__setattr__(name, value)


    class RoutePolicies(Entity):
        """
        All configured policies
        
        .. attribute:: route_policy
        
        	Information about an individual policy
        	**type**\: list of    :py:class:`RoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.RoutePolicies.RoutePolicy>`
        
        

        """

        _prefix = 'policy-repository-cfg'
        _revision = '2015-08-27'

        def __init__(self):
            super(RoutingPolicy.RoutePolicies, self).__init__()

            self.yang_name = "route-policies"
            self.yang_parent_name = "routing-policy"

            self.route_policy = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingPolicy.RoutePolicies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingPolicy.RoutePolicies, self).__setattr__(name, value)


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
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.RoutePolicies.RoutePolicy, self).__init__()

                self.yang_name = "route-policy"
                self.yang_parent_name = "route-policies"

                self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                self.rpl_route_policy = YLeaf(YType.str, "rpl-route-policy")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("route_policy_name",
                                "rpl_route_policy") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.RoutePolicies.RoutePolicy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.RoutePolicies.RoutePolicy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.route_policy_name.is_set or
                    self.rpl_route_policy.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.route_policy_name.yfilter != YFilter.not_set or
                    self.rpl_route_policy.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "route-policy" + "[route-policy-name='" + self.route_policy_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/route-policies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_policy_name.get_name_leafdata())
                if (self.rpl_route_policy.is_set or self.rpl_route_policy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rpl_route_policy.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "route-policy-name" or name == "rpl-route-policy"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "route-policy-name"):
                    self.route_policy_name = value
                    self.route_policy_name.value_namespace = name_space
                    self.route_policy_name.value_namespace_prefix = name_space_prefix
                if(value_path == "rpl-route-policy"):
                    self.rpl_route_policy = value
                    self.rpl_route_policy.value_namespace = name_space
                    self.rpl_route_policy.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.route_policy:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.route_policy:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "route-policies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "route-policy"):
                for c in self.route_policy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RoutingPolicy.RoutePolicies.RoutePolicy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.route_policy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "route-policy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sets(Entity):
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
            super(RoutingPolicy.Sets, self).__init__()

            self.yang_name = "sets"
            self.yang_parent_name = "routing-policy"

            self.append_esi_sets = RoutingPolicy.Sets.AppendEsiSets()
            self.append_esi_sets.parent = self
            self._children_name_map["append_esi_sets"] = "append-esi-sets"
            self._children_yang_names.add("append-esi-sets")

            self.append_etag_sets = RoutingPolicy.Sets.AppendEtagSets()
            self.append_etag_sets.parent = self
            self._children_name_map["append_etag_sets"] = "append-etag-sets"
            self._children_yang_names.add("append-etag-sets")

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

            self.remove_mac_sets = RoutingPolicy.Sets.RemoveMacSets()
            self.remove_mac_sets.parent = self
            self._children_name_map["remove_mac_sets"] = "remove-mac-sets"
            self._children_yang_names.add("remove-mac-sets")

            self.tag_sets = RoutingPolicy.Sets.TagSets()
            self.tag_sets.parent = self
            self._children_name_map["tag_sets"] = "tag-sets"
            self._children_yang_names.add("tag-sets")


        class PrependEtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: prepend_etag_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependEtagSets, self).__init__()

                self.yang_name = "prepend-etag-sets"
                self.yang_parent_name = "sets"

                self.prepend_etag_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.PrependEtagSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.PrependEtagSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet, self).__init__()

                    self.yang_name = "prepend-etag-set"
                    self.yang_parent_name = "prepend-etag-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "etag_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.etag_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.etag_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prepend-etag-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-etag-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.etag_set_as_text.is_set or self.etag_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.etag_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "etag-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "etag-set-as-text"):
                        self.etag_set_as_text = value
                        self.etag_set_as_text.value_namespace = name_space
                        self.etag_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.prepend_etag_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.prepend_etag_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prepend-etag-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prepend-etag-set"):
                    for c in self.prepend_etag_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.PrependEtagSets.PrependEtagSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.prepend_etag_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prepend-etag-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PrefixSets(Entity):
            """
            Information about Prefix sets
            
            .. attribute:: prefix_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`PrefixSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.PrefixSets, self).__init__()

                self.yang_name = "prefix-sets"
                self.yang_parent_name = "sets"

                self.prefix_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.PrefixSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.PrefixSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrefixSets.PrefixSet, self).__init__()

                    self.yang_name = "prefix-set"
                    self.yang_parent_name = "prefix-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_prefix_set = YLeaf(YType.str, "rpl-prefix-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_prefix_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.PrefixSets.PrefixSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.PrefixSets.PrefixSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_prefix_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_prefix_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefix-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prefix-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_prefix_set.is_set or self.rpl_prefix_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_prefix_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-prefix-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-prefix-set"):
                        self.rpl_prefix_set = value
                        self.rpl_prefix_set.value_namespace = name_space
                        self.rpl_prefix_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.prefix_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.prefix_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prefix-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prefix-set"):
                    for c in self.prefix_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.PrefixSets.PrefixSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.prefix_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prefix-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class AppendEtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: append_etag_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendEtagSets, self).__init__()

                self.yang_name = "append-etag-sets"
                self.yang_parent_name = "sets"

                self.append_etag_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.AppendEtagSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.AppendEtagSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet, self).__init__()

                    self.yang_name = "append-etag-set"
                    self.yang_parent_name = "append-etag-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "etag_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.etag_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.etag_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "append-etag-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-etag-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.etag_set_as_text.is_set or self.etag_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.etag_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "etag-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "etag-set-as-text"):
                        self.etag_set_as_text = value
                        self.etag_set_as_text.value_namespace = name_space
                        self.etag_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.append_etag_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.append_etag_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "append-etag-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "append-etag-set"):
                    for c in self.append_etag_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.AppendEtagSets.AppendEtagSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.append_etag_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "append-etag-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RemoveEtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: remove_etag_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveEtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveEtagSets, self).__init__()

                self.yang_name = "remove-etag-sets"
                self.yang_parent_name = "sets"

                self.remove_etag_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.RemoveEtagSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.RemoveEtagSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet, self).__init__()

                    self.yang_name = "remove-etag-set"
                    self.yang_parent_name = "remove-etag-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "etag_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.etag_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.etag_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "remove-etag-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-etag-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.etag_set_as_text.is_set or self.etag_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.etag_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "etag-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "etag-set-as-text"):
                        self.etag_set_as_text = value
                        self.etag_set_as_text.value_namespace = name_space
                        self.etag_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.remove_etag_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.remove_etag_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "remove-etag-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "remove-etag-set"):
                    for c in self.remove_etag_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.RemoveEtagSets.RemoveEtagSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.remove_etag_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "remove-etag-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class MacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: mac_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`MacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.MacSets.MacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.MacSets, self).__init__()

                self.yang_name = "mac-sets"
                self.yang_parent_name = "sets"

                self.mac_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.MacSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.MacSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.MacSets.MacSet, self).__init__()

                    self.yang_name = "mac-set"
                    self.yang_parent_name = "mac-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "mac_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.MacSets.MacSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.MacSets.MacSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.mac_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.mac_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mac-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/mac-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.mac_set_as_text.is_set or self.mac_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "mac-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-set-as-text"):
                        self.mac_set_as_text = value
                        self.mac_set_as_text.value_namespace = name_space
                        self.mac_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.mac_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.mac_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mac-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mac-set"):
                    for c in self.mac_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.MacSets.MacSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.mac_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mac-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ExtendedCommunityOpaqueSets(Entity):
            """
            Information about Opaque sets
            
            .. attribute:: extended_community_opaque_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityOpaqueSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, self).__init__()

                self.yang_name = "extended-community-opaque-sets"
                self.yang_parent_name = "sets"

                self.extended_community_opaque_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, self).__init__()

                    self.yang_name = "extended-community-opaque-set"
                    self.yang_parent_name = "extended-community-opaque-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_opaque_set = YLeaf(YType.str, "rpl-extended-community-opaque-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_extended_community_opaque_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_extended_community_opaque_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_extended_community_opaque_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "extended-community-opaque-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-opaque-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_extended_community_opaque_set.is_set or self.rpl_extended_community_opaque_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_extended_community_opaque_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-extended-community-opaque-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-extended-community-opaque-set"):
                        self.rpl_extended_community_opaque_set = value
                        self.rpl_extended_community_opaque_set.value_namespace = name_space
                        self.rpl_extended_community_opaque_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.extended_community_opaque_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.extended_community_opaque_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extended-community-opaque-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "extended-community-opaque-set"):
                    for c in self.extended_community_opaque_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.extended_community_opaque_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended-community-opaque-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PrependMacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: prepend_mac_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependMacSets.PrependMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependMacSets, self).__init__()

                self.yang_name = "prepend-mac-sets"
                self.yang_parent_name = "sets"

                self.prepend_mac_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.PrependMacSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.PrependMacSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependMacSets.PrependMacSet, self).__init__()

                    self.yang_name = "prepend-mac-set"
                    self.yang_parent_name = "prepend-mac-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "mac_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.PrependMacSets.PrependMacSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.PrependMacSets.PrependMacSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.mac_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.mac_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prepend-mac-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-mac-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.mac_set_as_text.is_set or self.mac_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "mac-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-set-as-text"):
                        self.mac_set_as_text = value
                        self.mac_set_as_text.value_namespace = name_space
                        self.mac_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.prepend_mac_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.prepend_mac_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prepend-mac-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prepend-mac-set"):
                    for c in self.prepend_mac_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.PrependMacSets.PrependMacSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.prepend_mac_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prepend-mac-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class OspfAreaSets(Entity):
            """
            Information about OSPF Area sets
            
            .. attribute:: ospf_area_set
            
            	Information about an individual OSPF area set. Usage\: OSPF area set allows to define named set of area numbers        which can be referenced in the route\-policy. Area sets      may be used during redistribution of the ospf protocol.  Example\: ospf\-area\-set EXAMPLE      1,                                             192.168.1.255                                  end\-set                                        Syntax\: OSPF area number can be entered as 32 bit number or in          the ip address format. See example.                     Semantic\: Area numbers listed in the set will be searched for             a match. In the example these are areas 1 and                  192.168.1.255.                                
            	**type**\: list of    :py:class:`OspfAreaSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.OspfAreaSets, self).__init__()

                self.yang_name = "ospf-area-sets"
                self.yang_parent_name = "sets"

                self.ospf_area_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.OspfAreaSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.OspfAreaSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, self).__init__()

                    self.yang_name = "ospf-area-set"
                    self.yang_parent_name = "ospf-area-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rplospf_area_set = YLeaf(YType.str, "rplospf-area-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rplospf_area_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rplospf_area_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rplospf_area_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ospf-area-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/ospf-area-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rplospf_area_set.is_set or self.rplospf_area_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rplospf_area_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rplospf-area-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rplospf-area-set"):
                        self.rplospf_area_set = value
                        self.rplospf_area_set.value_namespace = name_space
                        self.rplospf_area_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ospf_area_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ospf_area_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospf-area-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ospf-area-set"):
                    for c in self.ospf_area_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ospf_area_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospf-area-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class AppendMacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: append_mac_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendMacSets.AppendMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendMacSets, self).__init__()

                self.yang_name = "append-mac-sets"
                self.yang_parent_name = "sets"

                self.append_mac_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.AppendMacSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.AppendMacSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendMacSets.AppendMacSet, self).__init__()

                    self.yang_name = "append-mac-set"
                    self.yang_parent_name = "append-mac-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "mac_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.AppendMacSets.AppendMacSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.AppendMacSets.AppendMacSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.mac_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.mac_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "append-mac-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-mac-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.mac_set_as_text.is_set or self.mac_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "mac-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-set-as-text"):
                        self.mac_set_as_text = value
                        self.mac_set_as_text.value_namespace = name_space
                        self.mac_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.append_mac_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.append_mac_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "append-mac-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "append-mac-set"):
                    for c in self.append_mac_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.AppendMacSets.AppendMacSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.append_mac_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "append-mac-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ExtendedCommunityCostSets(Entity):
            """
            Information about Cost sets
            
            .. attribute:: extended_community_cost_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityCostSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityCostSets, self).__init__()

                self.yang_name = "extended-community-cost-sets"
                self.yang_parent_name = "sets"

                self.extended_community_cost_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.ExtendedCommunityCostSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.ExtendedCommunityCostSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, self).__init__()

                    self.yang_name = "extended-community-cost-set"
                    self.yang_parent_name = "extended-community-cost-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_cost_set = YLeaf(YType.str, "rpl-extended-community-cost-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_extended_community_cost_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_extended_community_cost_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_extended_community_cost_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "extended-community-cost-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-cost-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_extended_community_cost_set.is_set or self.rpl_extended_community_cost_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_extended_community_cost_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-extended-community-cost-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-extended-community-cost-set"):
                        self.rpl_extended_community_cost_set = value
                        self.rpl_extended_community_cost_set.value_namespace = name_space
                        self.rpl_extended_community_cost_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.extended_community_cost_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.extended_community_cost_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extended-community-cost-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "extended-community-cost-set"):
                    for c in self.extended_community_cost_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.extended_community_cost_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended-community-cost-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RemoveMacSets(Entity):
            """
            Information about Mac sets
            
            .. attribute:: remove_mac_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveMacSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveMacSets, self).__init__()

                self.yang_name = "remove-mac-sets"
                self.yang_parent_name = "sets"

                self.remove_mac_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.RemoveMacSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.RemoveMacSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet, self).__init__()

                    self.yang_name = "remove-mac-set"
                    self.yang_parent_name = "remove-mac-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.mac_set_as_text = YLeaf(YType.str, "mac-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "mac_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.mac_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.mac_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "remove-mac-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-mac-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.mac_set_as_text.is_set or self.mac_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "mac-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-set-as-text"):
                        self.mac_set_as_text = value
                        self.mac_set_as_text.value_namespace = name_space
                        self.mac_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.remove_mac_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.remove_mac_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "remove-mac-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "remove-mac-set"):
                    for c in self.remove_mac_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.RemoveMacSets.RemoveMacSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.remove_mac_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "remove-mac-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ExtendedCommunitySooSets(Entity):
            """
            Information about SOO sets
            
            .. attribute:: extended_community_soo_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunitySooSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySooSets, self).__init__()

                self.yang_name = "extended-community-soo-sets"
                self.yang_parent_name = "sets"

                self.extended_community_soo_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.ExtendedCommunitySooSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.ExtendedCommunitySooSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, self).__init__()

                    self.yang_name = "extended-community-soo-set"
                    self.yang_parent_name = "extended-community-soo-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_soo_set = YLeaf(YType.str, "rpl-extended-community-soo-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_extended_community_soo_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_extended_community_soo_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_extended_community_soo_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "extended-community-soo-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-soo-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_extended_community_soo_set.is_set or self.rpl_extended_community_soo_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_extended_community_soo_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-extended-community-soo-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-extended-community-soo-set"):
                        self.rpl_extended_community_soo_set = value
                        self.rpl_extended_community_soo_set.value_namespace = name_space
                        self.rpl_extended_community_soo_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.extended_community_soo_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.extended_community_soo_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extended-community-soo-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "extended-community-soo-set"):
                    for c in self.extended_community_soo_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.extended_community_soo_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended-community-soo-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class EsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: esi_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`EsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EsiSets.EsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.EsiSets, self).__init__()

                self.yang_name = "esi-sets"
                self.yang_parent_name = "sets"

                self.esi_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.EsiSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.EsiSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.EsiSets.EsiSet, self).__init__()

                    self.yang_name = "esi-set"
                    self.yang_parent_name = "esi-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "esi_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.EsiSets.EsiSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.EsiSets.EsiSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.esi_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.esi_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "esi-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/esi-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.esi_set_as_text.is_set or self.esi_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.esi_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "esi-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "esi-set-as-text"):
                        self.esi_set_as_text = value
                        self.esi_set_as_text.value_namespace = name_space
                        self.esi_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.esi_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.esi_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "esi-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "esi-set"):
                    for c in self.esi_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.EsiSets.EsiSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.esi_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "esi-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PrependEsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: prepend_esi_set
            
            	Prepend the entries to the existing set
            	**type**\: list of    :py:class:`PrependEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.PrependEsiSets, self).__init__()

                self.yang_name = "prepend-esi-sets"
                self.yang_parent_name = "sets"

                self.prepend_esi_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.PrependEsiSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.PrependEsiSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet, self).__init__()

                    self.yang_name = "prepend-esi-set"
                    self.yang_parent_name = "prepend-esi-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "esi_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.esi_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.esi_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prepend-esi-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/prepend-esi-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.esi_set_as_text.is_set or self.esi_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.esi_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "esi-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "esi-set-as-text"):
                        self.esi_set_as_text = value
                        self.esi_set_as_text.value_namespace = name_space
                        self.esi_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.prepend_esi_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.prepend_esi_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prepend-esi-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prepend-esi-set"):
                    for c in self.prepend_esi_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.PrependEsiSets.PrependEsiSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.prepend_esi_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prepend-esi-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class AppendEsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: append_esi_set
            
            	Append the entries to the existing set
            	**type**\: list of    :py:class:`AppendEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.AppendEsiSets, self).__init__()

                self.yang_name = "append-esi-sets"
                self.yang_parent_name = "sets"

                self.append_esi_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.AppendEsiSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.AppendEsiSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet, self).__init__()

                    self.yang_name = "append-esi-set"
                    self.yang_parent_name = "append-esi-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "esi_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.esi_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.esi_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "append-esi-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/append-esi-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.esi_set_as_text.is_set or self.esi_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.esi_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "esi-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "esi-set-as-text"):
                        self.esi_set_as_text = value
                        self.esi_set_as_text.value_namespace = name_space
                        self.esi_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.append_esi_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.append_esi_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "append-esi-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "append-esi-set"):
                    for c in self.append_esi_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.AppendEsiSets.AppendEsiSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.append_esi_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "append-esi-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RemoveEsiSets(Entity):
            """
            Information about Esi sets
            
            .. attribute:: remove_esi_set
            
            	Remove the entries from the existing set
            	**type**\: list of    :py:class:`RemoveEsiSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.RemoveEsiSets, self).__init__()

                self.yang_name = "remove-esi-sets"
                self.yang_parent_name = "sets"

                self.remove_esi_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.RemoveEsiSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.RemoveEsiSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet, self).__init__()

                    self.yang_name = "remove-esi-set"
                    self.yang_parent_name = "remove-esi-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.esi_set_as_text = YLeaf(YType.str, "esi-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "esi_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.esi_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.esi_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "remove-esi-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/remove-esi-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.esi_set_as_text.is_set or self.esi_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.esi_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "esi-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "esi-set-as-text"):
                        self.esi_set_as_text = value
                        self.esi_set_as_text.value_namespace = name_space
                        self.esi_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.remove_esi_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.remove_esi_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "remove-esi-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "remove-esi-set"):
                    for c in self.remove_esi_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.RemoveEsiSets.RemoveEsiSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.remove_esi_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "remove-esi-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ExtendedCommunitySegNhSets(Entity):
            """
            Information about SegNH sets
            
            .. attribute:: extended_community_seg_nh_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunitySegNhSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, self).__init__()

                self.yang_name = "extended-community-seg-nh-sets"
                self.yang_parent_name = "sets"

                self.extended_community_seg_nh_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, self).__init__()

                    self.yang_name = "extended-community-seg-nh-set"
                    self.yang_parent_name = "extended-community-seg-nh-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_seg_nh_set = YLeaf(YType.str, "rpl-extended-community-seg-nh-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_extended_community_seg_nh_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_extended_community_seg_nh_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_extended_community_seg_nh_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "extended-community-seg-nh-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-seg-nh-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_extended_community_seg_nh_set.is_set or self.rpl_extended_community_seg_nh_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_extended_community_seg_nh_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-extended-community-seg-nh-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-extended-community-seg-nh-set"):
                        self.rpl_extended_community_seg_nh_set = value
                        self.rpl_extended_community_seg_nh_set.value_namespace = name_space
                        self.rpl_extended_community_seg_nh_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.extended_community_seg_nh_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.extended_community_seg_nh_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extended-community-seg-nh-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "extended-community-seg-nh-set"):
                    for c in self.extended_community_seg_nh_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.extended_community_seg_nh_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended-community-seg-nh-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RdSets(Entity):
            """
            Information about RD sets
            
            .. attribute:: rd_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`RdSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.RdSets.RdSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.RdSets, self).__init__()

                self.yang_name = "rd-sets"
                self.yang_parent_name = "sets"

                self.rd_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.RdSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.RdSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.RdSets.RdSet, self).__init__()

                    self.yang_name = "rd-set"
                    self.yang_parent_name = "rd-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rplrd_set = YLeaf(YType.str, "rplrd-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rplrd_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.RdSets.RdSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.RdSets.RdSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rplrd_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rplrd_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rd-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/rd-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rplrd_set.is_set or self.rplrd_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rplrd_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rplrd-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rplrd-set"):
                        self.rplrd_set = value
                        self.rplrd_set.value_namespace = name_space
                        self.rplrd_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rd_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.rd_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rd-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rd-set"):
                    for c in self.rd_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.RdSets.RdSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rd_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rd-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PolicyGlobalSetTable(Entity):
            """
            Information about PolicyGlobal sets
            
            .. attribute:: policy_global_set
            
            	Information about an individual set
            	**type**\:  str
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.PolicyGlobalSetTable, self).__init__()

                self.yang_name = "policy-global-set-table"
                self.yang_parent_name = "sets"

                self.policy_global_set = YLeaf(YType.str, "policy-global-set")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("policy_global_set") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.PolicyGlobalSetTable, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.PolicyGlobalSetTable, self).__setattr__(name, value)

            def has_data(self):
                return self.policy_global_set.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.policy_global_set.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy-global-set-table" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.policy_global_set.is_set or self.policy_global_set.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_global_set.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "policy-global-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "policy-global-set"):
                    self.policy_global_set = value
                    self.policy_global_set.value_namespace = name_space
                    self.policy_global_set.value_namespace_prefix = name_space_prefix


        class ExtendedCommunityBandwidthSets(Entity):
            """
            Information about Bandwidth sets
            
            .. attribute:: extended_community_bandwidth_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityBandwidthSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, self).__init__()

                self.yang_name = "extended-community-bandwidth-sets"
                self.yang_parent_name = "sets"

                self.extended_community_bandwidth_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, self).__init__()

                    self.yang_name = "extended-community-bandwidth-set"
                    self.yang_parent_name = "extended-community-bandwidth-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_bandwidth_set = YLeaf(YType.str, "rpl-extended-community-bandwidth-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_extended_community_bandwidth_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_extended_community_bandwidth_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_extended_community_bandwidth_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "extended-community-bandwidth-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-bandwidth-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_extended_community_bandwidth_set.is_set or self.rpl_extended_community_bandwidth_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_extended_community_bandwidth_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-extended-community-bandwidth-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-extended-community-bandwidth-set"):
                        self.rpl_extended_community_bandwidth_set = value
                        self.rpl_extended_community_bandwidth_set.value_namespace = name_space
                        self.rpl_extended_community_bandwidth_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.extended_community_bandwidth_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.extended_community_bandwidth_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extended-community-bandwidth-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "extended-community-bandwidth-set"):
                    for c in self.extended_community_bandwidth_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.extended_community_bandwidth_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended-community-bandwidth-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class CommunitySets(Entity):
            """
            Information about Community sets
            
            .. attribute:: community_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`CommunitySet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.CommunitySets.CommunitySet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.CommunitySets, self).__init__()

                self.yang_name = "community-sets"
                self.yang_parent_name = "sets"

                self.community_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.CommunitySets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.CommunitySets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.CommunitySets.CommunitySet, self).__init__()

                    self.yang_name = "community-set"
                    self.yang_parent_name = "community-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_community_set = YLeaf(YType.str, "rpl-community-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_community_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.CommunitySets.CommunitySet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.CommunitySets.CommunitySet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_community_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_community_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "community-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/community-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_community_set.is_set or self.rpl_community_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_community_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-community-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-community-set"):
                        self.rpl_community_set = value
                        self.rpl_community_set.value_namespace = name_space
                        self.rpl_community_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.community_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.community_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "community-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "community-set"):
                    for c in self.community_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.CommunitySets.CommunitySet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.community_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "community-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class AsPathSets(Entity):
            """
            Information about AS Path sets
            
            .. attribute:: as_path_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`AsPathSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.AsPathSets.AsPathSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.AsPathSets, self).__init__()

                self.yang_name = "as-path-sets"
                self.yang_parent_name = "sets"

                self.as_path_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.AsPathSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.AsPathSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.AsPathSets.AsPathSet, self).__init__()

                    self.yang_name = "as-path-set"
                    self.yang_parent_name = "as-path-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rplas_path_set = YLeaf(YType.str, "rplas-path-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rplas_path_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.AsPathSets.AsPathSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.AsPathSets.AsPathSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rplas_path_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rplas_path_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "as-path-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/as-path-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rplas_path_set.is_set or self.rplas_path_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rplas_path_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rplas-path-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rplas-path-set"):
                        self.rplas_path_set = value
                        self.rplas_path_set.value_namespace = name_space
                        self.rplas_path_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.as_path_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.as_path_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "as-path-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "as-path-set"):
                    for c in self.as_path_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.AsPathSets.AsPathSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.as_path_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "as-path-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TagSets(Entity):
            """
            Information about Tag sets
            
            .. attribute:: tag_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`TagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.TagSets.TagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.TagSets, self).__init__()

                self.yang_name = "tag-sets"
                self.yang_parent_name = "sets"

                self.tag_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.TagSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.TagSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.TagSets.TagSet, self).__init__()

                    self.yang_name = "tag-set"
                    self.yang_parent_name = "tag-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_tag_set = YLeaf(YType.str, "rpl-tag-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_tag_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.TagSets.TagSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.TagSets.TagSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_tag_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_tag_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tag-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/tag-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_tag_set.is_set or self.rpl_tag_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_tag_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-tag-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-tag-set"):
                        self.rpl_tag_set = value
                        self.rpl_tag_set.value_namespace = name_space
                        self.rpl_tag_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.tag_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.tag_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tag-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "tag-set"):
                    for c in self.tag_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.TagSets.TagSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tag_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tag-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class EtagSets(Entity):
            """
            Information about Etag sets
            
            .. attribute:: etag_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`EtagSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.EtagSets.EtagSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.EtagSets, self).__init__()

                self.yang_name = "etag-sets"
                self.yang_parent_name = "sets"

                self.etag_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.EtagSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.EtagSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.EtagSets.EtagSet, self).__init__()

                    self.yang_name = "etag-set"
                    self.yang_parent_name = "etag-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.etag_set_as_text = YLeaf(YType.str, "etag-set-as-text")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "etag_set_as_text") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.EtagSets.EtagSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.EtagSets.EtagSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.etag_set_as_text.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.etag_set_as_text.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "etag-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/etag-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.etag_set_as_text.is_set or self.etag_set_as_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.etag_set_as_text.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "etag-set-as-text"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "etag-set-as-text"):
                        self.etag_set_as_text = value
                        self.etag_set_as_text.value_namespace = name_space
                        self.etag_set_as_text.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.etag_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.etag_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etag-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "etag-set"):
                    for c in self.etag_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.EtagSets.EtagSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.etag_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "etag-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ExtendedCommunityRtSets(Entity):
            """
            Information about RT sets
            
            .. attribute:: extended_community_rt_set
            
            	Information about an individual set
            	**type**\: list of    :py:class:`ExtendedCommunityRtSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_cfg.RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet>`
            
            

            """

            _prefix = 'policy-repository-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                super(RoutingPolicy.Sets.ExtendedCommunityRtSets, self).__init__()

                self.yang_name = "extended-community-rt-sets"
                self.yang_parent_name = "sets"

                self.extended_community_rt_set = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.Sets.ExtendedCommunityRtSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.Sets.ExtendedCommunityRtSets, self).__setattr__(name, value)


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
                _revision = '2015-08-27'

                def __init__(self):
                    super(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, self).__init__()

                    self.yang_name = "extended-community-rt-set"
                    self.yang_parent_name = "extended-community-rt-sets"

                    self.set_name = YLeaf(YType.str, "set-name")

                    self.rpl_extended_community_rt_set = YLeaf(YType.str, "rpl-extended-community-rt-set")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("set_name",
                                    "rpl_extended_community_rt_set") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.set_name.is_set or
                        self.rpl_extended_community_rt_set.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.set_name.yfilter != YFilter.not_set or
                        self.rpl_extended_community_rt_set.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "extended-community-rt-set" + "[set-name='" + self.set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/extended-community-rt-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.set_name.is_set or self.set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_name.get_name_leafdata())
                    if (self.rpl_extended_community_rt_set.is_set or self.rpl_extended_community_rt_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rpl_extended_community_rt_set.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "set-name" or name == "rpl-extended-community-rt-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "set-name"):
                        self.set_name = value
                        self.set_name.value_namespace = name_space
                        self.set_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "rpl-extended-community-rt-set"):
                        self.rpl_extended_community_rt_set = value
                        self.rpl_extended_community_rt_set.value_namespace = name_space
                        self.rpl_extended_community_rt_set.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.extended_community_rt_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.extended_community_rt_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "extended-community-rt-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "extended-community-rt-set"):
                    for c in self.extended_community_rt_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.extended_community_rt_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "extended-community-rt-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.append_esi_sets is not None and self.append_esi_sets.has_data()) or
                (self.append_etag_sets is not None and self.append_etag_sets.has_data()) or
                (self.append_mac_sets is not None and self.append_mac_sets.has_data()) or
                (self.as_path_sets is not None and self.as_path_sets.has_data()) or
                (self.community_sets is not None and self.community_sets.has_data()) or
                (self.esi_sets is not None and self.esi_sets.has_data()) or
                (self.etag_sets is not None and self.etag_sets.has_data()) or
                (self.extended_community_bandwidth_sets is not None and self.extended_community_bandwidth_sets.has_data()) or
                (self.extended_community_cost_sets is not None and self.extended_community_cost_sets.has_data()) or
                (self.extended_community_opaque_sets is not None and self.extended_community_opaque_sets.has_data()) or
                (self.extended_community_rt_sets is not None and self.extended_community_rt_sets.has_data()) or
                (self.extended_community_seg_nh_sets is not None and self.extended_community_seg_nh_sets.has_data()) or
                (self.extended_community_soo_sets is not None and self.extended_community_soo_sets.has_data()) or
                (self.mac_sets is not None and self.mac_sets.has_data()) or
                (self.ospf_area_sets is not None and self.ospf_area_sets.has_data()) or
                (self.policy_global_set_table is not None and self.policy_global_set_table.has_data()) or
                (self.prefix_sets is not None and self.prefix_sets.has_data()) or
                (self.prepend_esi_sets is not None and self.prepend_esi_sets.has_data()) or
                (self.prepend_etag_sets is not None and self.prepend_etag_sets.has_data()) or
                (self.prepend_mac_sets is not None and self.prepend_mac_sets.has_data()) or
                (self.rd_sets is not None and self.rd_sets.has_data()) or
                (self.remove_esi_sets is not None and self.remove_esi_sets.has_data()) or
                (self.remove_etag_sets is not None and self.remove_etag_sets.has_data()) or
                (self.remove_mac_sets is not None and self.remove_mac_sets.has_data()) or
                (self.tag_sets is not None and self.tag_sets.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.append_esi_sets is not None and self.append_esi_sets.has_operation()) or
                (self.append_etag_sets is not None and self.append_etag_sets.has_operation()) or
                (self.append_mac_sets is not None and self.append_mac_sets.has_operation()) or
                (self.as_path_sets is not None and self.as_path_sets.has_operation()) or
                (self.community_sets is not None and self.community_sets.has_operation()) or
                (self.esi_sets is not None and self.esi_sets.has_operation()) or
                (self.etag_sets is not None and self.etag_sets.has_operation()) or
                (self.extended_community_bandwidth_sets is not None and self.extended_community_bandwidth_sets.has_operation()) or
                (self.extended_community_cost_sets is not None and self.extended_community_cost_sets.has_operation()) or
                (self.extended_community_opaque_sets is not None and self.extended_community_opaque_sets.has_operation()) or
                (self.extended_community_rt_sets is not None and self.extended_community_rt_sets.has_operation()) or
                (self.extended_community_seg_nh_sets is not None and self.extended_community_seg_nh_sets.has_operation()) or
                (self.extended_community_soo_sets is not None and self.extended_community_soo_sets.has_operation()) or
                (self.mac_sets is not None and self.mac_sets.has_operation()) or
                (self.ospf_area_sets is not None and self.ospf_area_sets.has_operation()) or
                (self.policy_global_set_table is not None and self.policy_global_set_table.has_operation()) or
                (self.prefix_sets is not None and self.prefix_sets.has_operation()) or
                (self.prepend_esi_sets is not None and self.prepend_esi_sets.has_operation()) or
                (self.prepend_etag_sets is not None and self.prepend_etag_sets.has_operation()) or
                (self.prepend_mac_sets is not None and self.prepend_mac_sets.has_operation()) or
                (self.rd_sets is not None and self.rd_sets.has_operation()) or
                (self.remove_esi_sets is not None and self.remove_esi_sets.has_operation()) or
                (self.remove_etag_sets is not None and self.remove_etag_sets.has_operation()) or
                (self.remove_mac_sets is not None and self.remove_mac_sets.has_operation()) or
                (self.tag_sets is not None and self.tag_sets.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sets" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "append-esi-sets"):
                if (self.append_esi_sets is None):
                    self.append_esi_sets = RoutingPolicy.Sets.AppendEsiSets()
                    self.append_esi_sets.parent = self
                    self._children_name_map["append_esi_sets"] = "append-esi-sets"
                return self.append_esi_sets

            if (child_yang_name == "append-etag-sets"):
                if (self.append_etag_sets is None):
                    self.append_etag_sets = RoutingPolicy.Sets.AppendEtagSets()
                    self.append_etag_sets.parent = self
                    self._children_name_map["append_etag_sets"] = "append-etag-sets"
                return self.append_etag_sets

            if (child_yang_name == "append-mac-sets"):
                if (self.append_mac_sets is None):
                    self.append_mac_sets = RoutingPolicy.Sets.AppendMacSets()
                    self.append_mac_sets.parent = self
                    self._children_name_map["append_mac_sets"] = "append-mac-sets"
                return self.append_mac_sets

            if (child_yang_name == "as-path-sets"):
                if (self.as_path_sets is None):
                    self.as_path_sets = RoutingPolicy.Sets.AsPathSets()
                    self.as_path_sets.parent = self
                    self._children_name_map["as_path_sets"] = "as-path-sets"
                return self.as_path_sets

            if (child_yang_name == "community-sets"):
                if (self.community_sets is None):
                    self.community_sets = RoutingPolicy.Sets.CommunitySets()
                    self.community_sets.parent = self
                    self._children_name_map["community_sets"] = "community-sets"
                return self.community_sets

            if (child_yang_name == "esi-sets"):
                if (self.esi_sets is None):
                    self.esi_sets = RoutingPolicy.Sets.EsiSets()
                    self.esi_sets.parent = self
                    self._children_name_map["esi_sets"] = "esi-sets"
                return self.esi_sets

            if (child_yang_name == "etag-sets"):
                if (self.etag_sets is None):
                    self.etag_sets = RoutingPolicy.Sets.EtagSets()
                    self.etag_sets.parent = self
                    self._children_name_map["etag_sets"] = "etag-sets"
                return self.etag_sets

            if (child_yang_name == "extended-community-bandwidth-sets"):
                if (self.extended_community_bandwidth_sets is None):
                    self.extended_community_bandwidth_sets = RoutingPolicy.Sets.ExtendedCommunityBandwidthSets()
                    self.extended_community_bandwidth_sets.parent = self
                    self._children_name_map["extended_community_bandwidth_sets"] = "extended-community-bandwidth-sets"
                return self.extended_community_bandwidth_sets

            if (child_yang_name == "extended-community-cost-sets"):
                if (self.extended_community_cost_sets is None):
                    self.extended_community_cost_sets = RoutingPolicy.Sets.ExtendedCommunityCostSets()
                    self.extended_community_cost_sets.parent = self
                    self._children_name_map["extended_community_cost_sets"] = "extended-community-cost-sets"
                return self.extended_community_cost_sets

            if (child_yang_name == "extended-community-opaque-sets"):
                if (self.extended_community_opaque_sets is None):
                    self.extended_community_opaque_sets = RoutingPolicy.Sets.ExtendedCommunityOpaqueSets()
                    self.extended_community_opaque_sets.parent = self
                    self._children_name_map["extended_community_opaque_sets"] = "extended-community-opaque-sets"
                return self.extended_community_opaque_sets

            if (child_yang_name == "extended-community-rt-sets"):
                if (self.extended_community_rt_sets is None):
                    self.extended_community_rt_sets = RoutingPolicy.Sets.ExtendedCommunityRtSets()
                    self.extended_community_rt_sets.parent = self
                    self._children_name_map["extended_community_rt_sets"] = "extended-community-rt-sets"
                return self.extended_community_rt_sets

            if (child_yang_name == "extended-community-seg-nh-sets"):
                if (self.extended_community_seg_nh_sets is None):
                    self.extended_community_seg_nh_sets = RoutingPolicy.Sets.ExtendedCommunitySegNhSets()
                    self.extended_community_seg_nh_sets.parent = self
                    self._children_name_map["extended_community_seg_nh_sets"] = "extended-community-seg-nh-sets"
                return self.extended_community_seg_nh_sets

            if (child_yang_name == "extended-community-soo-sets"):
                if (self.extended_community_soo_sets is None):
                    self.extended_community_soo_sets = RoutingPolicy.Sets.ExtendedCommunitySooSets()
                    self.extended_community_soo_sets.parent = self
                    self._children_name_map["extended_community_soo_sets"] = "extended-community-soo-sets"
                return self.extended_community_soo_sets

            if (child_yang_name == "mac-sets"):
                if (self.mac_sets is None):
                    self.mac_sets = RoutingPolicy.Sets.MacSets()
                    self.mac_sets.parent = self
                    self._children_name_map["mac_sets"] = "mac-sets"
                return self.mac_sets

            if (child_yang_name == "ospf-area-sets"):
                if (self.ospf_area_sets is None):
                    self.ospf_area_sets = RoutingPolicy.Sets.OspfAreaSets()
                    self.ospf_area_sets.parent = self
                    self._children_name_map["ospf_area_sets"] = "ospf-area-sets"
                return self.ospf_area_sets

            if (child_yang_name == "policy-global-set-table"):
                if (self.policy_global_set_table is None):
                    self.policy_global_set_table = RoutingPolicy.Sets.PolicyGlobalSetTable()
                    self.policy_global_set_table.parent = self
                    self._children_name_map["policy_global_set_table"] = "policy-global-set-table"
                return self.policy_global_set_table

            if (child_yang_name == "prefix-sets"):
                if (self.prefix_sets is None):
                    self.prefix_sets = RoutingPolicy.Sets.PrefixSets()
                    self.prefix_sets.parent = self
                    self._children_name_map["prefix_sets"] = "prefix-sets"
                return self.prefix_sets

            if (child_yang_name == "prepend-esi-sets"):
                if (self.prepend_esi_sets is None):
                    self.prepend_esi_sets = RoutingPolicy.Sets.PrependEsiSets()
                    self.prepend_esi_sets.parent = self
                    self._children_name_map["prepend_esi_sets"] = "prepend-esi-sets"
                return self.prepend_esi_sets

            if (child_yang_name == "prepend-etag-sets"):
                if (self.prepend_etag_sets is None):
                    self.prepend_etag_sets = RoutingPolicy.Sets.PrependEtagSets()
                    self.prepend_etag_sets.parent = self
                    self._children_name_map["prepend_etag_sets"] = "prepend-etag-sets"
                return self.prepend_etag_sets

            if (child_yang_name == "prepend-mac-sets"):
                if (self.prepend_mac_sets is None):
                    self.prepend_mac_sets = RoutingPolicy.Sets.PrependMacSets()
                    self.prepend_mac_sets.parent = self
                    self._children_name_map["prepend_mac_sets"] = "prepend-mac-sets"
                return self.prepend_mac_sets

            if (child_yang_name == "rd-sets"):
                if (self.rd_sets is None):
                    self.rd_sets = RoutingPolicy.Sets.RdSets()
                    self.rd_sets.parent = self
                    self._children_name_map["rd_sets"] = "rd-sets"
                return self.rd_sets

            if (child_yang_name == "remove-esi-sets"):
                if (self.remove_esi_sets is None):
                    self.remove_esi_sets = RoutingPolicy.Sets.RemoveEsiSets()
                    self.remove_esi_sets.parent = self
                    self._children_name_map["remove_esi_sets"] = "remove-esi-sets"
                return self.remove_esi_sets

            if (child_yang_name == "remove-etag-sets"):
                if (self.remove_etag_sets is None):
                    self.remove_etag_sets = RoutingPolicy.Sets.RemoveEtagSets()
                    self.remove_etag_sets.parent = self
                    self._children_name_map["remove_etag_sets"] = "remove-etag-sets"
                return self.remove_etag_sets

            if (child_yang_name == "remove-mac-sets"):
                if (self.remove_mac_sets is None):
                    self.remove_mac_sets = RoutingPolicy.Sets.RemoveMacSets()
                    self.remove_mac_sets.parent = self
                    self._children_name_map["remove_mac_sets"] = "remove-mac-sets"
                return self.remove_mac_sets

            if (child_yang_name == "tag-sets"):
                if (self.tag_sets is None):
                    self.tag_sets = RoutingPolicy.Sets.TagSets()
                    self.tag_sets.parent = self
                    self._children_name_map["tag_sets"] = "tag-sets"
                return self.tag_sets

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "append-esi-sets" or name == "append-etag-sets" or name == "append-mac-sets" or name == "as-path-sets" or name == "community-sets" or name == "esi-sets" or name == "etag-sets" or name == "extended-community-bandwidth-sets" or name == "extended-community-cost-sets" or name == "extended-community-opaque-sets" or name == "extended-community-rt-sets" or name == "extended-community-seg-nh-sets" or name == "extended-community-soo-sets" or name == "mac-sets" or name == "ospf-area-sets" or name == "policy-global-set-table" or name == "prefix-sets" or name == "prepend-esi-sets" or name == "prepend-etag-sets" or name == "prepend-mac-sets" or name == "rd-sets" or name == "remove-esi-sets" or name == "remove-etag-sets" or name == "remove-mac-sets" or name == "tag-sets"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        _revision = '2015-08-27'

        def __init__(self):
            super(RoutingPolicy.Limits, self).__init__()

            self.yang_name = "limits"
            self.yang_parent_name = "routing-policy"

            self.maximum_lines_of_policy = YLeaf(YType.int32, "maximum-lines-of-policy")

            self.maximum_number_of_policies = YLeaf(YType.int32, "maximum-number-of-policies")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("maximum_lines_of_policy",
                            "maximum_number_of_policies") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingPolicy.Limits, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingPolicy.Limits, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.maximum_lines_of_policy.is_set or
                self.maximum_number_of_policies.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.maximum_lines_of_policy.yfilter != YFilter.not_set or
                self.maximum_number_of_policies.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "limits" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.maximum_lines_of_policy.is_set or self.maximum_lines_of_policy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maximum_lines_of_policy.get_name_leafdata())
            if (self.maximum_number_of_policies.is_set or self.maximum_number_of_policies.yfilter != YFilter.not_set):
                leaf_name_data.append(self.maximum_number_of_policies.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "maximum-lines-of-policy" or name == "maximum-number-of-policies"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "maximum-lines-of-policy"):
                self.maximum_lines_of_policy = value
                self.maximum_lines_of_policy.value_namespace = name_space
                self.maximum_lines_of_policy.value_namespace_prefix = name_space_prefix
            if(value_path == "maximum-number-of-policies"):
                self.maximum_number_of_policies = value
                self.maximum_number_of_policies.value_namespace = name_space
                self.maximum_number_of_policies.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.editor.is_set or
            (self.limits is not None and self.limits.has_data()) or
            (self.route_policies is not None and self.route_policies.has_data()) or
            (self.sets is not None and self.sets.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.editor.yfilter != YFilter.not_set or
            (self.limits is not None and self.limits.has_operation()) or
            (self.route_policies is not None and self.route_policies.has_operation()) or
            (self.sets is not None and self.sets.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-policy-repository-cfg:routing-policy" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.editor.is_set or self.editor.yfilter != YFilter.not_set):
            leaf_name_data.append(self.editor.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "limits"):
            if (self.limits is None):
                self.limits = RoutingPolicy.Limits()
                self.limits.parent = self
                self._children_name_map["limits"] = "limits"
            return self.limits

        if (child_yang_name == "route-policies"):
            if (self.route_policies is None):
                self.route_policies = RoutingPolicy.RoutePolicies()
                self.route_policies.parent = self
                self._children_name_map["route_policies"] = "route-policies"
            return self.route_policies

        if (child_yang_name == "sets"):
            if (self.sets is None):
                self.sets = RoutingPolicy.Sets()
                self.sets.parent = self
                self._children_name_map["sets"] = "sets"
            return self.sets

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "limits" or name == "route-policies" or name == "sets" or name == "editor"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "editor"):
            self.editor = value
            self.editor.value_namespace = name_space
            self.editor.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

