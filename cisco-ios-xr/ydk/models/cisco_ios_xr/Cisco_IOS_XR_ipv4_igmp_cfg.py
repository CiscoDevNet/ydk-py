""" Cisco_IOS_XR_ipv4_igmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-igmp package configuration.

This module contains definitions
for the following management objects\:
  igmp\: IGMPconfiguration
  amt\: amt
  mld\: mld

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IgmpFilter(Enum):
    """
    IgmpFilter

    Igmp filter

    .. data:: include = 0

    	Include

    .. data:: exclude = 1

    	Exclude

    .. data:: star_g = 2

    	StarG

    """

    include = Enum.YLeaf(0, "include")

    exclude = Enum.YLeaf(1, "exclude")

    star_g = Enum.YLeaf(2, "star-g")



class Igmp(Entity):
    """
    IGMPconfiguration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Igmp, self).__init__()
        self._top_entity = None

        self.yang_name = "igmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_presence_container = True

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Igmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class Vrfs(Entity):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Igmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "igmp"

            self.vrf = YList(self)

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
                        super(Igmp.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Igmp.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            Configuration for a particular vrf
            
            .. attribute:: vrf_name  <key>
            
            	Name for this vrf
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: inheritable_defaults
            
            	Inheritable Defaults
            	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults>`
            
            .. attribute:: interfaces
            
            	Interface\-level configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: maximum
            
            	Configure IGMP State Limits
            	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Maximum>`
            
            .. attribute:: robustness
            
            	Configure IGMP Robustness variable
            	**type**\:  int
            
            	**range:** 2..10
            
            	**default value**\: 2
            
            .. attribute:: ssm_access_groups
            
            	IGMP Source specific mode
            	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups>`
            
            .. attribute:: ssmdns_query_group
            
            	Enable SSM mapping using DNS Query
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: traffic
            
            	Configure IGMP Traffic variables
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Traffic>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.robustness = YLeaf(YType.uint32, "robustness")

                self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

                self.inheritable_defaults = Igmp.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                self._children_yang_names.add("inheritable-defaults")

                self.interfaces = Igmp.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.maximum = Igmp.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"
                self._children_yang_names.add("maximum")

                self.ssm_access_groups = Igmp.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                self._children_yang_names.add("ssm-access-groups")

                self.traffic = Igmp.Vrfs.Vrf.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "robustness",
                                "ssmdns_query_group") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.Vrfs.Vrf, self).__setattr__(name, value)


            class Traffic(Entity):
                """
                Configure IGMP Traffic variables
                
                .. attribute:: profile
                
                	Configure the route\-policy profile
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "vrf"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.Vrfs.Vrf.Traffic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.Vrfs.Vrf.Traffic, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class InheritableDefaults(Entity):
                """
                Inheritable Defaults
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "vrf"

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_group",
                                    "query_interval",
                                    "query_max_response_time",
                                    "query_timeout",
                                    "router_enable",
                                    "version") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.Vrfs.Vrf.InheritableDefaults, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.Vrfs.Vrf.InheritableDefaults, self).__setattr__(name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "maximum_groups",
                                        "warning_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.maximum_groups.is_set or
                            self.warning_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.maximum_groups.yfilter != YFilter.not_set or
                            self.warning_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                        if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-groups"):
                            self.maximum_groups = value
                            self.maximum_groups.value_namespace = name_space
                            self.maximum_groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "warning-threshold"):
                            self.warning_threshold = value
                            self.warning_threshold.value_namespace = name_space
                            self.warning_threshold.value_namespace_prefix = name_space_prefix


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.enable.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "explicit-tracking" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.access_group.is_set or
                        self.query_interval.is_set or
                        self.query_max_response_time.is_set or
                        self.query_timeout.is_set or
                        self.router_enable.is_set or
                        self.version.is_set or
                        (self.explicit_tracking is not None) or
                        (self.maximum_groups_per_interface_oor is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_group.yfilter != YFilter.not_set or
                        self.query_interval.yfilter != YFilter.not_set or
                        self.query_max_response_time.yfilter != YFilter.not_set or
                        self.query_timeout.yfilter != YFilter.not_set or
                        self.router_enable.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                        (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "inheritable-defaults" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_group.get_name_leafdata())
                    if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_interval.get_name_leafdata())
                    if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                    if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_timeout.get_name_leafdata())
                    if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_enable.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "explicit-tracking"):
                        if (self.explicit_tracking is None):
                            self.explicit_tracking = Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking()
                            self.explicit_tracking.parent = self
                            self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        return self.explicit_tracking

                    if (child_yang_name == "maximum-groups-per-interface-oor"):
                        if (self.maximum_groups_per_interface_oor is None):
                            self.maximum_groups_per_interface_oor = Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor()
                            self.maximum_groups_per_interface_oor.parent = self
                            self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        return self.maximum_groups_per_interface_oor

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "explicit-tracking" or name == "maximum-groups-per-interface-oor" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-group"):
                        self.access_group = value
                        self.access_group.value_namespace = name_space
                        self.access_group.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-interval"):
                        self.query_interval = value
                        self.query_interval.value_namespace = name_space
                        self.query_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-max-response-time"):
                        self.query_max_response_time = value
                        self.query_max_response_time.value_namespace = name_space
                        self.query_max_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-timeout"):
                        self.query_timeout = value
                        self.query_timeout.value_namespace = name_space
                        self.query_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-enable"):
                        self.router_enable = value
                        self.router_enable.value_namespace = name_space
                        self.router_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix


            class SsmAccessGroups(Entity):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.SsmAccessGroups, self).__init__()

                    self.yang_name = "ssm-access-groups"
                    self.yang_parent_name = "vrf"

                    self.ssm_access_group = YList(self)

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
                                super(Igmp.Vrfs.Vrf.SsmAccessGroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.Vrfs.Vrf.SsmAccessGroups, self).__setattr__(name, value)


                class SsmAccessGroup(Entity):
                    """
                    SSM static Access Group
                    
                    .. attribute:: source_address  <key>
                    
                    	IP source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list specifying access group
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__init__()

                        self.yang_name = "ssm-access-group"
                        self.yang_parent_name = "ssm-access-groups"

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("source_address",
                                        "access_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.source_address.is_set or
                            self.access_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.source_address.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ssm-access-group" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_address.get_name_leafdata())
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "source-address" or name == "access-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "source-address"):
                            self.source_address = value
                            self.source_address.value_namespace = name_space
                            self.source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ssm_access_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ssm_access_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssm-access-groups" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ssm-access-group"):
                        for c in self.ssm_access_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ssm_access_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ssm-access-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Maximum(Entity):
                """
                Configure IGMP State Limits
                
                .. attribute:: maximum_groups
                
                	Configure maximum number of groups accepted by this router
                	**type**\:  int
                
                	**range:** 1..75000
                
                	**default value**\: 50000
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "vrf"

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("maximum_groups") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.Vrfs.Vrf.Maximum, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.Vrfs.Vrf.Maximum, self).__setattr__(name, value)

                def has_data(self):
                    return self.maximum_groups.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.maximum_groups.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "maximum" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_groups.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "maximum-groups"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "maximum-groups"):
                        self.maximum_groups = value
                        self.maximum_groups.value_namespace = name_space
                        self.maximum_groups.value_namespace_prefix = name_space_prefix


            class Interfaces(Entity):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"

                    self.interface = YList(self)

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
                                super(Igmp.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: join_groups
                    
                    	IGMP join multicast group
                    	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: maximum_groups_per_interface_oor
                    
                    	Configure maximum number of groups accepted per interface by this router
                    	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: query_timeout
                    
                    	IGMP previous querier timeout
                    	**type**\:  int
                    
                    	**range:** 60..300
                    
                    	**units**\: second
                    
                    .. attribute:: router_enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: static_group_group_addresses
                    
                    	IGMP static multicast group
                    	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses>`
                    
                    .. attribute:: version
                    
                    	Version number
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                        self.router_enable = YLeaf(YType.boolean, "router-enable")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")

                        self.join_groups = None
                        self._children_name_map["join_groups"] = "join-groups"
                        self._children_yang_names.add("join-groups")

                        self.maximum_groups_per_interface_oor = None
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        self._children_yang_names.add("maximum-groups-per-interface-oor")

                        self.static_group_group_addresses = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                        self._children_yang_names.add("static-group-group-addresses")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "access_group",
                                        "query_interval",
                                        "query_max_response_time",
                                        "query_timeout",
                                        "router_enable",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Igmp.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)


                    class JoinGroups(Entity):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__init__()

                            self.yang_name = "join-groups"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.join_group = YList(self)
                            self.join_group_source_address = YList(self)

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
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)


                        class JoinGroup(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                                self.yang_name = "join-group"
                                self.yang_parent_name = "join-groups"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.mode = YLeaf(YType.enumeration, "mode")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "join-group" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mode.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mode"):
                                    self.mode = value
                                    self.mode.value_namespace = name_space
                                    self.mode.value_namespace_prefix = name_space_prefix


                        class JoinGroupSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	Optional IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                                self.yang_name = "join-group-source-address"
                                self.yang_parent_name = "join-groups"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.mode = YLeaf(YType.enumeration, "mode")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "source_address",
                                                "mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.source_address.is_set or
                                    self.mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mode.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "source-address" or name == "mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mode"):
                                    self.mode = value
                                    self.mode.value_namespace = name_space
                                    self.mode.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.join_group:
                                if (c.has_data()):
                                    return True
                            for c in self.join_group_source_address:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.join_group:
                                if (c.has_operation()):
                                    return True
                            for c in self.join_group_source_address:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "join-groups" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "join-group"):
                                for c in self.join_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.join_group.append(c)
                                return c

                            if (child_yang_name == "join-group-source-address"):
                                for c in self.join_group_source_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.join_group_source_address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "join-group" or name == "join-group-source-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class StaticGroupGroupAddresses(Entity):
                        """
                        IGMP static multicast group
                        
                        .. attribute:: static_group_group_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                        
                        .. attribute:: static_group_group_address_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                        
                        .. attribute:: static_group_group_address_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                            self.yang_name = "static-group-group-addresses"
                            self.yang_parent_name = "interface"

                            self.static_group_group_address = YList(self)
                            self.static_group_group_address_group_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask_source_address = YList(self)
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                            self.static_group_group_address_source_address = YList(self)
                            self.static_group_group_address_source_address_source_address_mask = YList(self)

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
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)


                        class StaticGroupGroupAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                                self.yang_name = "static-group-group-address"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-source-address"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "source_address",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.source_address.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "source_address",
                                                "source_address_mask",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.source_address.is_set or
                                    self.source_address_mask.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.source_address_mask.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address-mask"):
                                    self.source_address_mask = value
                                    self.source_address_mask.value_namespace = name_space
                                    self.source_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressGroupAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_address_mask",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_address_mask.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_address_mask.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-address-mask"):
                                    self.group_address_mask = value
                                    self.group_address_mask.value_namespace = name_space
                                    self.group_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_address_mask",
                                                "source_address",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_address_mask.is_set or
                                    self.source_address.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_address_mask.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-address-mask"):
                                    self.group_address_mask = value
                                    self.group_address_mask.value_namespace = name_space
                                    self.group_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_address_mask",
                                                "source_address",
                                                "source_address_mask",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_address_mask.is_set or
                                    self.source_address.is_set or
                                    self.source_address_mask.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_address_mask.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.source_address_mask.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-address-mask"):
                                    self.group_address_mask = value
                                    self.group_address_mask.value_namespace = name_space
                                    self.group_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address-mask"):
                                    self.source_address_mask = value
                                    self.source_address_mask.value_namespace = name_space
                                    self.source_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.static_group_group_address:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_source_address:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_source_address_source_address_mask:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.static_group_group_address:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_source_address:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_source_address_source_address_mask:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-addresses" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "static-group-group-address"):
                                for c in self.static_group_group_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-group-address-mask"):
                                for c in self.static_group_group_address_group_address_mask:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_group_address_mask.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-group-address-mask-source-address"):
                                for c in self.static_group_group_address_group_address_mask_source_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_group_address_mask_source_address.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-group-address-mask-source-address-source-address-mask"):
                                for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_group_address_mask_source_address_source_address_mask.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-source-address"):
                                for c in self.static_group_group_address_source_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_source_address.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-source-address-source-address-mask"):
                                for c in self.static_group_group_address_source_address_source_address_mask:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_source_address_source_address_mask.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "static-group-group-address" or name == "static-group-group-address-group-address-mask" or name == "static-group-group-address-group-address-mask-source-address" or name == "static-group-group-address-group-address-mask-source-address-source-address-mask" or name == "static-group-group-address-source-address" or name == "static-group-group-address-source-address-source-address-mask"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class MaximumGroupsPerInterfaceOor(Entity):
                        """
                        Configure maximum number of groups accepted per
                        interface by this router
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: maximum_groups
                        
                        	Maximum number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	 WarningThreshold for number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**default value**\: 25000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                            self.yang_name = "maximum-groups-per-interface-oor"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                            self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_list_name",
                                            "maximum_groups",
                                            "warning_threshold") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_list_name.is_set or
                                self.maximum_groups.is_set or
                                self.warning_threshold.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set or
                                self.maximum_groups.yfilter != YFilter.not_set or
                                self.warning_threshold.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())
                            if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                            if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "maximum-groups"):
                                self.maximum_groups = value
                                self.maximum_groups.value_namespace = name_space
                                self.maximum_groups.value_namespace_prefix = name_space_prefix
                            if(value_path == "warning-threshold"):
                                self.warning_threshold = value
                                self.warning_threshold.value_namespace = name_space
                                self.warning_threshold.value_namespace_prefix = name_space_prefix


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enabled or disabled, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_list_name",
                                            "enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_list_name.is_set or
                                self.enable.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "explicit-tracking" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-list-name" or name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.access_group.is_set or
                            self.query_interval.is_set or
                            self.query_max_response_time.is_set or
                            self.query_timeout.is_set or
                            self.router_enable.is_set or
                            self.version.is_set or
                            (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_data()) or
                            (self.explicit_tracking is not None) or
                            (self.join_groups is not None) or
                            (self.maximum_groups_per_interface_oor is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.access_group.yfilter != YFilter.not_set or
                            self.query_interval.yfilter != YFilter.not_set or
                            self.query_max_response_time.yfilter != YFilter.not_set or
                            self.query_timeout.yfilter != YFilter.not_set or
                            self.router_enable.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                            (self.join_groups is not None and self.join_groups.has_operation()) or
                            (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()) or
                            (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_group.get_name_leafdata())
                        if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_interval.get_name_leafdata())
                        if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                        if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_timeout.get_name_leafdata())
                        if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router_enable.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "explicit-tracking"):
                            if (self.explicit_tracking is None):
                                self.explicit_tracking = Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking()
                                self.explicit_tracking.parent = self
                                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                            return self.explicit_tracking

                        if (child_yang_name == "join-groups"):
                            if (self.join_groups is None):
                                self.join_groups = Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups()
                                self.join_groups.parent = self
                                self._children_name_map["join_groups"] = "join-groups"
                            return self.join_groups

                        if (child_yang_name == "maximum-groups-per-interface-oor"):
                            if (self.maximum_groups_per_interface_oor is None):
                                self.maximum_groups_per_interface_oor = Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor()
                                self.maximum_groups_per_interface_oor.parent = self
                                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                            return self.maximum_groups_per_interface_oor

                        if (child_yang_name == "static-group-group-addresses"):
                            if (self.static_group_group_addresses is None):
                                self.static_group_group_addresses = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                                self.static_group_group_addresses.parent = self
                                self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                            return self.static_group_group_addresses

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "explicit-tracking" or name == "join-groups" or name == "maximum-groups-per-interface-oor" or name == "static-group-group-addresses" or name == "interface-name" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-group"):
                            self.access_group = value
                            self.access_group.value_namespace = name_space
                            self.access_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-interval"):
                            self.query_interval = value
                            self.query_interval.value_namespace = name_space
                            self.query_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-max-response-time"):
                            self.query_max_response_time = value
                            self.query_max_response_time.value_namespace = name_space
                            self.query_max_response_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-timeout"):
                            self.query_timeout = value
                            self.query_timeout.value_namespace = name_space
                            self.query_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "router-enable"):
                            self.router_enable = value
                            self.router_enable.value_namespace = name_space
                            self.router_enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Igmp.Vrfs.Vrf.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.robustness.is_set or
                    self.ssmdns_query_group.is_set or
                    (self.inheritable_defaults is not None and self.inheritable_defaults.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.maximum is not None and self.maximum.has_data()) or
                    (self.ssm_access_groups is not None and self.ssm_access_groups.has_data()) or
                    (self.traffic is not None and self.traffic.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.robustness.yfilter != YFilter.not_set or
                    self.ssmdns_query_group.yfilter != YFilter.not_set or
                    (self.inheritable_defaults is not None and self.inheritable_defaults.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.maximum is not None and self.maximum.has_operation()) or
                    (self.ssm_access_groups is not None and self.ssm_access_groups.has_operation()) or
                    (self.traffic is not None and self.traffic.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.robustness.is_set or self.robustness.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.robustness.get_name_leafdata())
                if (self.ssmdns_query_group.is_set or self.ssmdns_query_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ssmdns_query_group.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "inheritable-defaults"):
                    if (self.inheritable_defaults is None):
                        self.inheritable_defaults = Igmp.Vrfs.Vrf.InheritableDefaults()
                        self.inheritable_defaults.parent = self
                        self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                    return self.inheritable_defaults

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Igmp.Vrfs.Vrf.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "maximum"):
                    if (self.maximum is None):
                        self.maximum = Igmp.Vrfs.Vrf.Maximum()
                        self.maximum.parent = self
                        self._children_name_map["maximum"] = "maximum"
                    return self.maximum

                if (child_yang_name == "ssm-access-groups"):
                    if (self.ssm_access_groups is None):
                        self.ssm_access_groups = Igmp.Vrfs.Vrf.SsmAccessGroups()
                        self.ssm_access_groups.parent = self
                        self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                    return self.ssm_access_groups

                if (child_yang_name == "traffic"):
                    if (self.traffic is None):
                        self.traffic = Igmp.Vrfs.Vrf.Traffic()
                        self.traffic.parent = self
                        self._children_name_map["traffic"] = "traffic"
                    return self.traffic

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "inheritable-defaults" or name == "interfaces" or name == "maximum" or name == "ssm-access-groups" or name == "traffic" or name == "vrf-name" or name == "robustness" or name == "ssmdns-query-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "robustness"):
                    self.robustness = value
                    self.robustness.value_namespace = name_space
                    self.robustness.value_namespace_prefix = name_space_prefix
                if(value_path == "ssmdns-query-group"):
                    self.ssmdns_query_group = value
                    self.ssmdns_query_group.value_namespace = name_space
                    self.ssmdns_query_group.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Igmp.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: accounting
        
        	Configure IGMP accounting for logging join/leave records
        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Accounting>`
        
        .. attribute:: inheritable_defaults
        
        	Inheritable Defaults
        	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults>`
        
        .. attribute:: interfaces
        
        	Interface\-level configuration
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces>`
        
        .. attribute:: maximum
        
        	Configure IGMP State Limits
        	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Maximum>`
        
        .. attribute:: nsf
        
        	Configure NSF specific options
        	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Nsf>`
        
        .. attribute:: robustness
        
        	Configure IGMP Robustness variable
        	**type**\:  int
        
        	**range:** 2..10
        
        	**default value**\: 2
        
        .. attribute:: ssm_access_groups
        
        	IGMP Source specific mode
        	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups>`
        
        .. attribute:: ssmdns_query_group
        
        	Enable SSM mapping using DNS Query
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: traffic
        
        	Configure IGMP Traffic variables
        	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Traffic>`
        
        .. attribute:: unicast_qos_adjust
        
        	Configure IGMP QoS shapers for subscriber interfaces
        	**type**\:   :py:class:`UnicastQosAdjust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.UnicastQosAdjust>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Igmp.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "igmp"
            self.is_presence_container = True

            self.robustness = YLeaf(YType.uint32, "robustness")

            self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

            self.accounting = Igmp.DefaultContext.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"
            self._children_yang_names.add("accounting")

            self.inheritable_defaults = Igmp.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
            self._children_yang_names.add("inheritable-defaults")

            self.interfaces = Igmp.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.maximum = Igmp.DefaultContext.Maximum()
            self.maximum.parent = self
            self._children_name_map["maximum"] = "maximum"
            self._children_yang_names.add("maximum")

            self.nsf = Igmp.DefaultContext.Nsf()
            self.nsf.parent = self
            self._children_name_map["nsf"] = "nsf"
            self._children_yang_names.add("nsf")

            self.ssm_access_groups = Igmp.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
            self._children_yang_names.add("ssm-access-groups")

            self.traffic = Igmp.DefaultContext.Traffic()
            self.traffic.parent = self
            self._children_name_map["traffic"] = "traffic"
            self._children_yang_names.add("traffic")

            self.unicast_qos_adjust = Igmp.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self
            self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"
            self._children_yang_names.add("unicast-qos-adjust")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("robustness",
                            "ssmdns_query_group") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Igmp.DefaultContext, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Igmp.DefaultContext, self).__setattr__(name, value)


        class Nsf(Entity):
            """
            Configure NSF specific options
            
            .. attribute:: lifetime
            
            	Maximum time for IGMP NSF mode in seconds
            	**type**\:  int
            
            	**range:** 10..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Nsf, self).__init__()

                self.yang_name = "nsf"
                self.yang_parent_name = "default-context"

                self.lifetime = YLeaf(YType.uint32, "lifetime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lifetime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.DefaultContext.Nsf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.Nsf, self).__setattr__(name, value)

            def has_data(self):
                return self.lifetime.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lifetime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nsf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lifetime.is_set or self.lifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lifetime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lifetime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lifetime"):
                    self.lifetime = value
                    self.lifetime.value_namespace = name_space
                    self.lifetime.value_namespace_prefix = name_space_prefix


        class UnicastQosAdjust(Entity):
            """
            Configure IGMP QoS shapers for subscriber
            interfaces
            
            .. attribute:: adjustment_delay
            
            	Configure the QoS delay before programming (in seconds)
            	**type**\:  int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 1
            
            .. attribute:: download_interval
            
            	Configure the QoS download interval (in milliseconds)
            	**type**\:  int
            
            	**range:** 10..500
            
            	**units**\: millisecond
            
            	**default value**\: 100
            
            .. attribute:: hold_off
            
            	Configure the QoS hold off time (in seconds)
            	**type**\:  int
            
            	**range:** 5..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.UnicastQosAdjust, self).__init__()

                self.yang_name = "unicast-qos-adjust"
                self.yang_parent_name = "default-context"

                self.adjustment_delay = YLeaf(YType.uint32, "adjustment-delay")

                self.download_interval = YLeaf(YType.uint32, "download-interval")

                self.hold_off = YLeaf(YType.uint32, "hold-off")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("adjustment_delay",
                                "download_interval",
                                "hold_off") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.DefaultContext.UnicastQosAdjust, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.UnicastQosAdjust, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.adjustment_delay.is_set or
                    self.download_interval.is_set or
                    self.hold_off.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.adjustment_delay.yfilter != YFilter.not_set or
                    self.download_interval.yfilter != YFilter.not_set or
                    self.hold_off.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "unicast-qos-adjust" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.adjustment_delay.is_set or self.adjustment_delay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.adjustment_delay.get_name_leafdata())
                if (self.download_interval.is_set or self.download_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.download_interval.get_name_leafdata())
                if (self.hold_off.is_set or self.hold_off.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_off.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "adjustment-delay" or name == "download-interval" or name == "hold-off"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "adjustment-delay"):
                    self.adjustment_delay = value
                    self.adjustment_delay.value_namespace = name_space
                    self.adjustment_delay.value_namespace_prefix = name_space_prefix
                if(value_path == "download-interval"):
                    self.download_interval = value
                    self.download_interval.value_namespace = name_space
                    self.download_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-off"):
                    self.hold_off = value
                    self.hold_off.value_namespace = name_space
                    self.hold_off.value_namespace_prefix = name_space_prefix


        class Accounting(Entity):
            """
            Configure IGMP accounting for logging
            join/leave records
            
            .. attribute:: max_history
            
            	Configure IGMP accounting Maximum History setting
            	**type**\:  int
            
            	**range:** 0..365
            
            	**units**\: day
            
            	**default value**\: 0
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "default-context"

                self.max_history = YLeaf(YType.uint32, "max-history")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("max_history") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.DefaultContext.Accounting, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.Accounting, self).__setattr__(name, value)

            def has_data(self):
                return self.max_history.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.max_history.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "accounting" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.max_history.is_set or self.max_history.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_history.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "max-history"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "max-history"):
                    self.max_history = value
                    self.max_history.value_namespace = name_space
                    self.max_history.value_namespace_prefix = name_space_prefix


        class Traffic(Entity):
            """
            Configure IGMP Traffic variables
            
            .. attribute:: profile
            
            	Configure the route\-policy profile
            	**type**\:  str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Traffic, self).__init__()

                self.yang_name = "traffic"
                self.yang_parent_name = "default-context"

                self.profile = YLeaf(YType.str, "profile")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("profile") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.DefaultContext.Traffic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.Traffic, self).__setattr__(name, value)

            def has_data(self):
                return self.profile.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.profile.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "traffic" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.profile.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "profile"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "profile"):
                    self.profile = value
                    self.profile.value_namespace = name_space
                    self.profile.value_namespace_prefix = name_space_prefix


        class InheritableDefaults(Entity):
            """
            Inheritable Defaults
            
            .. attribute:: access_group
            
            	Access list specifying access group range
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: explicit_tracking
            
            	IGMPv3 explicit host tracking
            	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults.ExplicitTracking>`
            
            	**presence node**\: True
            
            .. attribute:: maximum_groups_per_interface_oor
            
            	Configure maximum number of groups accepted per interface by this router
            	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
            
            	**presence node**\: True
            
            .. attribute:: query_interval
            
            	Query interval in seconds
            	**type**\:  int
            
            	**range:** 1..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: query_max_response_time
            
            	Query response value in seconds
            	**type**\:  int
            
            	**range:** 1..12
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: query_timeout
            
            	IGMP previous querier timeout
            	**type**\:  int
            
            	**range:** 60..300
            
            	**units**\: second
            
            .. attribute:: router_enable
            
            	Enabled or disabled, when value is TRUE or FALSE respectively
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: version
            
            	Version number
            	**type**\:  int
            
            	**range:** 1..3
            
            	**default value**\: 3
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.InheritableDefaults, self).__init__()

                self.yang_name = "inheritable-defaults"
                self.yang_parent_name = "default-context"

                self.access_group = YLeaf(YType.str, "access-group")

                self.query_interval = YLeaf(YType.uint32, "query-interval")

                self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                self.router_enable = YLeaf(YType.boolean, "router-enable")

                self.version = YLeaf(YType.uint32, "version")

                self.explicit_tracking = None
                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                self._children_yang_names.add("explicit-tracking")

                self.maximum_groups_per_interface_oor = None
                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                self._children_yang_names.add("maximum-groups-per-interface-oor")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("access_group",
                                "query_interval",
                                "query_max_response_time",
                                "query_timeout",
                                "router_enable",
                                "version") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.DefaultContext.InheritableDefaults, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.InheritableDefaults, self).__setattr__(name, value)


            class MaximumGroupsPerInterfaceOor(Entity):
                """
                Configure maximum number of groups accepted per
                interface by this router
                
                .. attribute:: access_list_name
                
                	Access\-list to account for
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: maximum_groups
                
                	Maximum number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**mandatory**\: True
                
                .. attribute:: warning_threshold
                
                	 WarningThreshold for number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**default value**\: 25000
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                    self.yang_name = "maximum-groups-per-interface-oor"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                    self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_list_name",
                                    "maximum_groups",
                                    "warning_threshold") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.maximum_groups.is_set or
                        self.warning_threshold.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.maximum_groups.yfilter != YFilter.not_set or
                        self.warning_threshold.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/inheritable-defaults/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                    if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-groups"):
                        self.maximum_groups = value
                        self.maximum_groups.value_namespace = name_space
                        self.maximum_groups.value_namespace_prefix = name_space_prefix
                    if(value_path == "warning-threshold"):
                        self.warning_threshold = value
                        self.warning_threshold.value_namespace = name_space
                        self.warning_threshold.value_namespace_prefix = name_space_prefix


            class ExplicitTracking(Entity):
                """
                IGMPv3 explicit host tracking
                
                .. attribute:: access_list_name
                
                	Access list specifying tracking group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, self).__init__()

                    self.yang_name = "explicit-tracking"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.enable = YLeaf(YType.boolean, "enable")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_list_name",
                                    "enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.enable.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "explicit-tracking" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/inheritable-defaults/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.access_group.is_set or
                    self.query_interval.is_set or
                    self.query_max_response_time.is_set or
                    self.query_timeout.is_set or
                    self.router_enable.is_set or
                    self.version.is_set or
                    (self.explicit_tracking is not None) or
                    (self.maximum_groups_per_interface_oor is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.access_group.yfilter != YFilter.not_set or
                    self.query_interval.yfilter != YFilter.not_set or
                    self.query_max_response_time.yfilter != YFilter.not_set or
                    self.query_timeout.yfilter != YFilter.not_set or
                    self.router_enable.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set or
                    (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                    (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "inheritable-defaults" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access_group.get_name_leafdata())
                if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_interval.get_name_leafdata())
                if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_timeout.get_name_leafdata())
                if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.router_enable.get_name_leafdata())
                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "explicit-tracking"):
                    if (self.explicit_tracking is None):
                        self.explicit_tracking = Igmp.DefaultContext.InheritableDefaults.ExplicitTracking()
                        self.explicit_tracking.parent = self
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    return self.explicit_tracking

                if (child_yang_name == "maximum-groups-per-interface-oor"):
                    if (self.maximum_groups_per_interface_oor is None):
                        self.maximum_groups_per_interface_oor = Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor()
                        self.maximum_groups_per_interface_oor.parent = self
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    return self.maximum_groups_per_interface_oor

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "explicit-tracking" or name == "maximum-groups-per-interface-oor" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "access-group"):
                    self.access_group = value
                    self.access_group.value_namespace = name_space
                    self.access_group.value_namespace_prefix = name_space_prefix
                if(value_path == "query-interval"):
                    self.query_interval = value
                    self.query_interval.value_namespace = name_space
                    self.query_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "query-max-response-time"):
                    self.query_max_response_time = value
                    self.query_max_response_time.value_namespace = name_space
                    self.query_max_response_time.value_namespace_prefix = name_space_prefix
                if(value_path == "query-timeout"):
                    self.query_timeout = value
                    self.query_timeout.value_namespace = name_space
                    self.query_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "router-enable"):
                    self.router_enable = value
                    self.router_enable.value_namespace = name_space
                    self.router_enable.value_namespace_prefix = name_space_prefix
                if(value_path == "version"):
                    self.version = value
                    self.version.value_namespace = name_space
                    self.version.value_namespace_prefix = name_space_prefix


        class SsmAccessGroups(Entity):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.SsmAccessGroups, self).__init__()

                self.yang_name = "ssm-access-groups"
                self.yang_parent_name = "default-context"

                self.ssm_access_group = YList(self)

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
                            super(Igmp.DefaultContext.SsmAccessGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.SsmAccessGroups, self).__setattr__(name, value)


            class SsmAccessGroup(Entity):
                """
                SSM static Access Group
                
                .. attribute:: source_address  <key>
                
                	IP source address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: access_list_name
                
                	Access list specifying access group
                	**type**\:  str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__init__()

                    self.yang_name = "ssm-access-group"
                    self.yang_parent_name = "ssm-access-groups"

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_address",
                                    "access_list_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.source_address.is_set or
                        self.access_list_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_address.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssm-access-group" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/ssm-access-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_address.get_name_leafdata())
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-address" or name == "access-list-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-address"):
                        self.source_address = value
                        self.source_address.value_namespace = name_space
                        self.source_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ssm_access_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ssm_access_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ssm-access-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssm-access-group"):
                    for c in self.ssm_access_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ssm_access_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssm-access-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Maximum(Entity):
            """
            Configure IGMP State Limits
            
            .. attribute:: maximum_groups
            
            	Configure maximum number of groups accepted by this router
            	**type**\:  int
            
            	**range:** 1..75000
            
            	**default value**\: 50000
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Maximum, self).__init__()

                self.yang_name = "maximum"
                self.yang_parent_name = "default-context"

                self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("maximum_groups") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Igmp.DefaultContext.Maximum, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.Maximum, self).__setattr__(name, value)

            def has_data(self):
                return self.maximum_groups.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.maximum_groups.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "maximum" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_groups.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "maximum-groups"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "maximum-groups"):
                    self.maximum_groups = value
                    self.maximum_groups.value_namespace = name_space
                    self.maximum_groups.value_namespace_prefix = name_space_prefix


        class Interfaces(Entity):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-context"

                self.interface = YList(self)

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
                            super(Igmp.DefaultContext.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Igmp.DefaultContext.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                The name of the interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: join_groups
                
                	IGMP join multicast group
                	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: static_group_group_addresses
                
                	IGMP static multicast group
                	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses>`
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.join_groups = None
                    self._children_name_map["join_groups"] = "join-groups"
                    self._children_yang_names.add("join-groups")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")

                    self.static_group_group_addresses = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                    self._children_yang_names.add("static-group-group-addresses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "access_group",
                                    "query_interval",
                                    "query_max_response_time",
                                    "query_timeout",
                                    "router_enable",
                                    "version") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Igmp.DefaultContext.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Igmp.DefaultContext.Interfaces.Interface, self).__setattr__(name, value)


                class JoinGroups(Entity):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, self).__init__()

                        self.yang_name = "join-groups"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.join_group = YList(self)
                        self.join_group_source_address = YList(self)

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
                                    super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)


                    class JoinGroup(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                            self.yang_name = "join-group"
                            self.yang_parent_name = "join-groups"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.mode = YLeaf(YType.enumeration, "mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "join-group" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mode"):
                                self.mode = value
                                self.mode.value_namespace = name_space
                                self.mode.value_namespace_prefix = name_space_prefix


                    class JoinGroupSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	Optional IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                            self.yang_name = "join-group-source-address"
                            self.yang_parent_name = "join-groups"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.mode = YLeaf(YType.enumeration, "mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "source_address",
                                            "mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.source_address.is_set or
                                self.mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "source-address" or name == "mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mode"):
                                self.mode = value
                                self.mode.value_namespace = name_space
                                self.mode.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.join_group:
                            if (c.has_data()):
                                return True
                        for c in self.join_group_source_address:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.join_group:
                            if (c.has_operation()):
                                return True
                        for c in self.join_group_source_address:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "join-groups" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "join-group"):
                            for c in self.join_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.join_group.append(c)
                            return c

                        if (child_yang_name == "join-group-source-address"):
                            for c in self.join_group_source_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.join_group_source_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "join-group" or name == "join-group-source-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class StaticGroupGroupAddresses(Entity):
                    """
                    IGMP static multicast group
                    
                    .. attribute:: static_group_group_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                    
                    .. attribute:: static_group_group_address_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                    
                    .. attribute:: static_group_group_address_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                        self.yang_name = "static-group-group-addresses"
                        self.yang_parent_name = "interface"

                        self.static_group_group_address = YList(self)
                        self.static_group_group_address_group_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask_source_address = YList(self)
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                        self.static_group_group_address_source_address = YList(self)
                        self.static_group_group_address_source_address_source_address_mask = YList(self)

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
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)


                    class StaticGroupGroupAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                            self.yang_name = "static-group-group-address"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-source-address"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "source_address",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.source_address.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "source_address",
                                            "source_address_mask",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.source_address.is_set or
                                self.source_address_mask.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_address_mask.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address-mask"):
                                self.source_address_mask = value
                                self.source_address_mask.value_namespace = name_space
                                self.source_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressGroupAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_address_mask",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_address_mask.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_address_mask.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-address-mask"):
                                self.group_address_mask = value
                                self.group_address_mask.value_namespace = name_space
                                self.group_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_address_mask",
                                            "source_address",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_address_mask.is_set or
                                self.source_address.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_address_mask.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-address-mask"):
                                self.group_address_mask = value
                                self.group_address_mask.value_namespace = name_space
                                self.group_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_address_mask",
                                            "source_address",
                                            "source_address_mask",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_address_mask.is_set or
                                self.source_address.is_set or
                                self.source_address_mask.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_address_mask.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_address_mask.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-address-mask"):
                                self.group_address_mask = value
                                self.group_address_mask.value_namespace = name_space
                                self.group_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address-mask"):
                                self.source_address_mask = value
                                self.source_address_mask.value_namespace = name_space
                                self.source_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.static_group_group_address:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_group_address_mask:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_source_address:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_source_address_source_address_mask:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.static_group_group_address:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_group_address_mask:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_source_address:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_source_address_source_address_mask:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-group-group-addresses" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "static-group-group-address"):
                            for c in self.static_group_group_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-group-address-mask"):
                            for c in self.static_group_group_address_group_address_mask:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_group_address_mask.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-group-address-mask-source-address"):
                            for c in self.static_group_group_address_group_address_mask_source_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_group_address_mask_source_address.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-group-address-mask-source-address-source-address-mask"):
                            for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-source-address"):
                            for c in self.static_group_group_address_source_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_source_address.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-source-address-source-address-mask"):
                            for c in self.static_group_group_address_source_address_source_address_mask:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_source_address_source_address_mask.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "static-group-group-address" or name == "static-group-group-address-group-address-mask" or name == "static-group-group-address-group-address-mask-source-address" or name == "static-group-group-address-group-address-mask-source-address-source-address-mask" or name == "static-group-group-address-source-address" or name == "static-group-group-address-source-address-source-address-mask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "maximum_groups",
                                        "warning_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.maximum_groups.is_set or
                            self.warning_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.maximum_groups.yfilter != YFilter.not_set or
                            self.warning_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                        if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-groups"):
                            self.maximum_groups = value
                            self.maximum_groups.value_namespace = name_space
                            self.maximum_groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "warning-threshold"):
                            self.warning_threshold = value
                            self.warning_threshold.value_namespace = name_space
                            self.warning_threshold.value_namespace_prefix = name_space_prefix


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.enable.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "explicit-tracking" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.access_group.is_set or
                        self.query_interval.is_set or
                        self.query_max_response_time.is_set or
                        self.query_timeout.is_set or
                        self.router_enable.is_set or
                        self.version.is_set or
                        (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_data()) or
                        (self.explicit_tracking is not None) or
                        (self.join_groups is not None) or
                        (self.maximum_groups_per_interface_oor is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.access_group.yfilter != YFilter.not_set or
                        self.query_interval.yfilter != YFilter.not_set or
                        self.query_max_response_time.yfilter != YFilter.not_set or
                        self.query_timeout.yfilter != YFilter.not_set or
                        self.router_enable.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                        (self.join_groups is not None and self.join_groups.has_operation()) or
                        (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()) or
                        (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_group.get_name_leafdata())
                    if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_interval.get_name_leafdata())
                    if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                    if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_timeout.get_name_leafdata())
                    if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_enable.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "explicit-tracking"):
                        if (self.explicit_tracking is None):
                            self.explicit_tracking = Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking()
                            self.explicit_tracking.parent = self
                            self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        return self.explicit_tracking

                    if (child_yang_name == "join-groups"):
                        if (self.join_groups is None):
                            self.join_groups = Igmp.DefaultContext.Interfaces.Interface.JoinGroups()
                            self.join_groups.parent = self
                            self._children_name_map["join_groups"] = "join-groups"
                        return self.join_groups

                    if (child_yang_name == "maximum-groups-per-interface-oor"):
                        if (self.maximum_groups_per_interface_oor is None):
                            self.maximum_groups_per_interface_oor = Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor()
                            self.maximum_groups_per_interface_oor.parent = self
                            self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        return self.maximum_groups_per_interface_oor

                    if (child_yang_name == "static-group-group-addresses"):
                        if (self.static_group_group_addresses is None):
                            self.static_group_group_addresses = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                            self.static_group_group_addresses.parent = self
                            self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                        return self.static_group_group_addresses

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "explicit-tracking" or name == "join-groups" or name == "maximum-groups-per-interface-oor" or name == "static-group-group-addresses" or name == "interface-name" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-group"):
                        self.access_group = value
                        self.access_group.value_namespace = name_space
                        self.access_group.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-interval"):
                        self.query_interval = value
                        self.query_interval.value_namespace = name_space
                        self.query_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-max-response-time"):
                        self.query_max_response_time = value
                        self.query_max_response_time.value_namespace = name_space
                        self.query_max_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-timeout"):
                        self.query_timeout = value
                        self.query_timeout.value_namespace = name_space
                        self.query_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-enable"):
                        self.router_enable = value
                        self.router_enable.value_namespace = name_space
                        self.router_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Igmp.DefaultContext.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.robustness.is_set or
                self.ssmdns_query_group.is_set or
                (self.accounting is not None and self.accounting.has_data()) or
                (self.inheritable_defaults is not None and self.inheritable_defaults.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.maximum is not None and self.maximum.has_data()) or
                (self.nsf is not None and self.nsf.has_data()) or
                (self.ssm_access_groups is not None and self.ssm_access_groups.has_data()) or
                (self.traffic is not None and self.traffic.has_data()) or
                (self.unicast_qos_adjust is not None and self.unicast_qos_adjust.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.robustness.yfilter != YFilter.not_set or
                self.ssmdns_query_group.yfilter != YFilter.not_set or
                (self.accounting is not None and self.accounting.has_operation()) or
                (self.inheritable_defaults is not None and self.inheritable_defaults.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.maximum is not None and self.maximum.has_operation()) or
                (self.nsf is not None and self.nsf.has_operation()) or
                (self.ssm_access_groups is not None and self.ssm_access_groups.has_operation()) or
                (self.traffic is not None and self.traffic.has_operation()) or
                (self.unicast_qos_adjust is not None and self.unicast_qos_adjust.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-context" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.robustness.is_set or self.robustness.yfilter != YFilter.not_set):
                leaf_name_data.append(self.robustness.get_name_leafdata())
            if (self.ssmdns_query_group.is_set or self.ssmdns_query_group.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ssmdns_query_group.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "accounting"):
                if (self.accounting is None):
                    self.accounting = Igmp.DefaultContext.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                return self.accounting

            if (child_yang_name == "inheritable-defaults"):
                if (self.inheritable_defaults is None):
                    self.inheritable_defaults = Igmp.DefaultContext.InheritableDefaults()
                    self.inheritable_defaults.parent = self
                    self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                return self.inheritable_defaults

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Igmp.DefaultContext.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "maximum"):
                if (self.maximum is None):
                    self.maximum = Igmp.DefaultContext.Maximum()
                    self.maximum.parent = self
                    self._children_name_map["maximum"] = "maximum"
                return self.maximum

            if (child_yang_name == "nsf"):
                if (self.nsf is None):
                    self.nsf = Igmp.DefaultContext.Nsf()
                    self.nsf.parent = self
                    self._children_name_map["nsf"] = "nsf"
                return self.nsf

            if (child_yang_name == "ssm-access-groups"):
                if (self.ssm_access_groups is None):
                    self.ssm_access_groups = Igmp.DefaultContext.SsmAccessGroups()
                    self.ssm_access_groups.parent = self
                    self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                return self.ssm_access_groups

            if (child_yang_name == "traffic"):
                if (self.traffic is None):
                    self.traffic = Igmp.DefaultContext.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                return self.traffic

            if (child_yang_name == "unicast-qos-adjust"):
                if (self.unicast_qos_adjust is None):
                    self.unicast_qos_adjust = Igmp.DefaultContext.UnicastQosAdjust()
                    self.unicast_qos_adjust.parent = self
                    self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"
                return self.unicast_qos_adjust

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "accounting" or name == "inheritable-defaults" or name == "interfaces" or name == "maximum" or name == "nsf" or name == "ssm-access-groups" or name == "traffic" or name == "unicast-qos-adjust" or name == "robustness" or name == "ssmdns-query-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "robustness"):
                self.robustness = value
                self.robustness.value_namespace = name_space
                self.robustness.value_namespace_prefix = name_space_prefix
            if(value_path == "ssmdns-query-group"):
                self.ssmdns_query_group = value
                self.ssmdns_query_group.value_namespace = name_space
                self.ssmdns_query_group.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.vrfs is not None and self.vrfs.has_data()) or
            (self.default_context is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.default_context is not None and self.default_context.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:igmp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "default-context"):
            if (self.default_context is None):
                self.default_context = Igmp.DefaultContext()
                self.default_context.parent = self
                self._children_name_map["default_context"] = "default-context"
            return self.default_context

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Igmp.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-context" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Igmp()
        return self._top_entity

class Amt(Entity):
    """
    amt
    
    .. attribute:: amtmtu
    
    	Configure AMT Relay MTU
    	**type**\:  int
    
    	**range:** 100..65535
    
    .. attribute:: amtqqic
    
    	Configure AMT QQIC value
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: amttos
    
    	Configure AMT Relay TOS
    	**type**\:  int
    
    	**range:** 1..255
    
    .. attribute:: amtttl
    
    	Configure AMT Relay TTL
    	**type**\:  int
    
    	**range:** 1..255
    
    .. attribute:: gateway_filter
    
    	Access list for Gateway Filter
    	**type**\:  str
    
    	**length:** 1..64
    
    .. attribute:: maximum_gateway
    
    	Configure AMT maximum number of Gateways
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v4_route_gateway
    
    	Configure Maximum number of IPv4 route\-gateways (Tunnels)
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v4_routes
    
    	Configure Maximum number of IPv4 Routes
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v6_route_gateway
    
    	Configure Maximum number of IPv6 route\-gateways (Tunnels)
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v6_routes
    
    	Configure Maximum number of IPv6 Routes
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: relay_adv_add
    
    	Configure AMT Relay IPv4 Advertisement Address
    	**type**\:   :py:class:`RelayAdvAdd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Amt.RelayAdvAdd>`
    
    	**presence node**\: True
    
    .. attribute:: relay_anycast_prefix
    
    	Configure AMT Relay IPv4 Anycast\-Prefix
    	**type**\:   :py:class:`RelayAnycastPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Amt.RelayAnycastPrefix>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Amt, self).__init__()
        self._top_entity = None

        self.yang_name = "amt"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"

        self.amtmtu = YLeaf(YType.uint32, "amtmtu")

        self.amtqqic = YLeaf(YType.uint32, "amtqqic")

        self.amttos = YLeaf(YType.uint32, "amttos")

        self.amtttl = YLeaf(YType.uint32, "amtttl")

        self.gateway_filter = YLeaf(YType.str, "gateway-filter")

        self.maximum_gateway = YLeaf(YType.uint32, "maximum-gateway")

        self.maximum_v4_route_gateway = YLeaf(YType.uint32, "maximum-v4-route-gateway")

        self.maximum_v4_routes = YLeaf(YType.uint32, "maximum-v4-routes")

        self.maximum_v6_route_gateway = YLeaf(YType.uint32, "maximum-v6-route-gateway")

        self.maximum_v6_routes = YLeaf(YType.uint32, "maximum-v6-routes")

        self.relay_adv_add = None
        self._children_name_map["relay_adv_add"] = "relay-adv-add"
        self._children_yang_names.add("relay-adv-add")

        self.relay_anycast_prefix = None
        self._children_name_map["relay_anycast_prefix"] = "relay-anycast-prefix"
        self._children_yang_names.add("relay-anycast-prefix")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("amtmtu",
                        "amtqqic",
                        "amttos",
                        "amtttl",
                        "gateway_filter",
                        "maximum_gateway",
                        "maximum_v4_route_gateway",
                        "maximum_v4_routes",
                        "maximum_v6_route_gateway",
                        "maximum_v6_routes") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Amt, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Amt, self).__setattr__(name, value)


    class RelayAdvAdd(Entity):
        """
        Configure AMT Relay IPv4 Advertisement Address
        
        .. attribute:: address
        
        	AMT Relay IPv4 Advertisement Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: interface
        
        	Relay Advertisement Interface
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Amt.RelayAdvAdd, self).__init__()

            self.yang_name = "relay-adv-add"
            self.yang_parent_name = "amt"
            self.is_presence_container = True

            self.address = YLeaf(YType.str, "address")

            self.interface = YLeaf(YType.str, "interface")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address",
                            "interface") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Amt.RelayAdvAdd, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Amt.RelayAdvAdd, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.address.is_set or
                self.interface.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address.yfilter != YFilter.not_set or
                self.interface.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "relay-adv-add" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:amt/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address.get_name_leafdata())
            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address" or name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address"):
                self.address = value
                self.address.value_namespace = name_space
                self.address.value_namespace_prefix = name_space_prefix
            if(value_path == "interface"):
                self.interface = value
                self.interface.value_namespace = name_space
                self.interface.value_namespace_prefix = name_space_prefix


    class RelayAnycastPrefix(Entity):
        """
        Configure AMT Relay IPv4 Anycast\-Prefix
        
        .. attribute:: address
        
        	Anycast\-Prefix Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: prefix_length
        
        	Mask Length for Anycast Prefix
        	**type**\:  int
        
        	**range:** 1..32
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Amt.RelayAnycastPrefix, self).__init__()

            self.yang_name = "relay-anycast-prefix"
            self.yang_parent_name = "amt"
            self.is_presence_container = True

            self.address = YLeaf(YType.str, "address")

            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address",
                            "prefix_length") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Amt.RelayAnycastPrefix, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Amt.RelayAnycastPrefix, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.address.is_set or
                self.prefix_length.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address.yfilter != YFilter.not_set or
                self.prefix_length.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "relay-anycast-prefix" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:amt/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address.get_name_leafdata())
            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prefix_length.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address" or name == "prefix-length"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address"):
                self.address = value
                self.address.value_namespace = name_space
                self.address.value_namespace_prefix = name_space_prefix
            if(value_path == "prefix-length"):
                self.prefix_length = value
                self.prefix_length.value_namespace = name_space
                self.prefix_length.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.amtmtu.is_set or
            self.amtqqic.is_set or
            self.amttos.is_set or
            self.amtttl.is_set or
            self.gateway_filter.is_set or
            self.maximum_gateway.is_set or
            self.maximum_v4_route_gateway.is_set or
            self.maximum_v4_routes.is_set or
            self.maximum_v6_route_gateway.is_set or
            self.maximum_v6_routes.is_set or
            (self.relay_adv_add is not None) or
            (self.relay_anycast_prefix is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.amtmtu.yfilter != YFilter.not_set or
            self.amtqqic.yfilter != YFilter.not_set or
            self.amttos.yfilter != YFilter.not_set or
            self.amtttl.yfilter != YFilter.not_set or
            self.gateway_filter.yfilter != YFilter.not_set or
            self.maximum_gateway.yfilter != YFilter.not_set or
            self.maximum_v4_route_gateway.yfilter != YFilter.not_set or
            self.maximum_v4_routes.yfilter != YFilter.not_set or
            self.maximum_v6_route_gateway.yfilter != YFilter.not_set or
            self.maximum_v6_routes.yfilter != YFilter.not_set or
            (self.relay_adv_add is not None and self.relay_adv_add.has_operation()) or
            (self.relay_anycast_prefix is not None and self.relay_anycast_prefix.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:amt" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.amtmtu.is_set or self.amtmtu.yfilter != YFilter.not_set):
            leaf_name_data.append(self.amtmtu.get_name_leafdata())
        if (self.amtqqic.is_set or self.amtqqic.yfilter != YFilter.not_set):
            leaf_name_data.append(self.amtqqic.get_name_leafdata())
        if (self.amttos.is_set or self.amttos.yfilter != YFilter.not_set):
            leaf_name_data.append(self.amttos.get_name_leafdata())
        if (self.amtttl.is_set or self.amtttl.yfilter != YFilter.not_set):
            leaf_name_data.append(self.amtttl.get_name_leafdata())
        if (self.gateway_filter.is_set or self.gateway_filter.yfilter != YFilter.not_set):
            leaf_name_data.append(self.gateway_filter.get_name_leafdata())
        if (self.maximum_gateway.is_set or self.maximum_gateway.yfilter != YFilter.not_set):
            leaf_name_data.append(self.maximum_gateway.get_name_leafdata())
        if (self.maximum_v4_route_gateway.is_set or self.maximum_v4_route_gateway.yfilter != YFilter.not_set):
            leaf_name_data.append(self.maximum_v4_route_gateway.get_name_leafdata())
        if (self.maximum_v4_routes.is_set or self.maximum_v4_routes.yfilter != YFilter.not_set):
            leaf_name_data.append(self.maximum_v4_routes.get_name_leafdata())
        if (self.maximum_v6_route_gateway.is_set or self.maximum_v6_route_gateway.yfilter != YFilter.not_set):
            leaf_name_data.append(self.maximum_v6_route_gateway.get_name_leafdata())
        if (self.maximum_v6_routes.is_set or self.maximum_v6_routes.yfilter != YFilter.not_set):
            leaf_name_data.append(self.maximum_v6_routes.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "relay-adv-add"):
            if (self.relay_adv_add is None):
                self.relay_adv_add = Amt.RelayAdvAdd()
                self.relay_adv_add.parent = self
                self._children_name_map["relay_adv_add"] = "relay-adv-add"
            return self.relay_adv_add

        if (child_yang_name == "relay-anycast-prefix"):
            if (self.relay_anycast_prefix is None):
                self.relay_anycast_prefix = Amt.RelayAnycastPrefix()
                self.relay_anycast_prefix.parent = self
                self._children_name_map["relay_anycast_prefix"] = "relay-anycast-prefix"
            return self.relay_anycast_prefix

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "relay-adv-add" or name == "relay-anycast-prefix" or name == "amtmtu" or name == "amtqqic" or name == "amttos" or name == "amtttl" or name == "gateway-filter" or name == "maximum-gateway" or name == "maximum-v4-route-gateway" or name == "maximum-v4-routes" or name == "maximum-v6-route-gateway" or name == "maximum-v6-routes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "amtmtu"):
            self.amtmtu = value
            self.amtmtu.value_namespace = name_space
            self.amtmtu.value_namespace_prefix = name_space_prefix
        if(value_path == "amtqqic"):
            self.amtqqic = value
            self.amtqqic.value_namespace = name_space
            self.amtqqic.value_namespace_prefix = name_space_prefix
        if(value_path == "amttos"):
            self.amttos = value
            self.amttos.value_namespace = name_space
            self.amttos.value_namespace_prefix = name_space_prefix
        if(value_path == "amtttl"):
            self.amtttl = value
            self.amtttl.value_namespace = name_space
            self.amtttl.value_namespace_prefix = name_space_prefix
        if(value_path == "gateway-filter"):
            self.gateway_filter = value
            self.gateway_filter.value_namespace = name_space
            self.gateway_filter.value_namespace_prefix = name_space_prefix
        if(value_path == "maximum-gateway"):
            self.maximum_gateway = value
            self.maximum_gateway.value_namespace = name_space
            self.maximum_gateway.value_namespace_prefix = name_space_prefix
        if(value_path == "maximum-v4-route-gateway"):
            self.maximum_v4_route_gateway = value
            self.maximum_v4_route_gateway.value_namespace = name_space
            self.maximum_v4_route_gateway.value_namespace_prefix = name_space_prefix
        if(value_path == "maximum-v4-routes"):
            self.maximum_v4_routes = value
            self.maximum_v4_routes.value_namespace = name_space
            self.maximum_v4_routes.value_namespace_prefix = name_space_prefix
        if(value_path == "maximum-v6-route-gateway"):
            self.maximum_v6_route_gateway = value
            self.maximum_v6_route_gateway.value_namespace = name_space
            self.maximum_v6_route_gateway.value_namespace_prefix = name_space_prefix
        if(value_path == "maximum-v6-routes"):
            self.maximum_v6_routes = value
            self.maximum_v6_routes.value_namespace = name_space
            self.maximum_v6_routes.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Amt()
        return self._top_entity

class Mld(Entity):
    """
    mld
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Mld, self).__init__()
        self._top_entity = None

        self.yang_name = "mld"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_presence_container = True

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Mld.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class Vrfs(Entity):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Mld.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mld"

            self.vrf = YList(self)

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
                        super(Mld.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Mld.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            Configuration for a particular vrf
            
            .. attribute:: vrf_name  <key>
            
            	Name for this vrf
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: inheritable_defaults
            
            	Inheritable Defaults
            	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults>`
            
            .. attribute:: interfaces
            
            	Interface\-level configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: maximum
            
            	Configure IGMP State Limits
            	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Maximum>`
            
            .. attribute:: robustness
            
            	Configure IGMP Robustness variable
            	**type**\:  int
            
            	**range:** 2..10
            
            	**default value**\: 2
            
            .. attribute:: ssm_access_groups
            
            	IGMP Source specific mode
            	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups>`
            
            .. attribute:: ssmdns_query_group
            
            	Enable SSM mapping using DNS Query
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: traffic
            
            	Configure IGMP Traffic variables
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Traffic>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.robustness = YLeaf(YType.uint32, "robustness")

                self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

                self.inheritable_defaults = Mld.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                self._children_yang_names.add("inheritable-defaults")

                self.interfaces = Mld.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.maximum = Mld.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"
                self._children_yang_names.add("maximum")

                self.ssm_access_groups = Mld.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                self._children_yang_names.add("ssm-access-groups")

                self.traffic = Mld.Vrfs.Vrf.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "robustness",
                                "ssmdns_query_group") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.Vrfs.Vrf, self).__setattr__(name, value)


            class Traffic(Entity):
                """
                Configure IGMP Traffic variables
                
                .. attribute:: profile
                
                	Configure the route\-policy profile
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "vrf"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.Vrfs.Vrf.Traffic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.Vrfs.Vrf.Traffic, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class InheritableDefaults(Entity):
                """
                Inheritable Defaults
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "vrf"

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_group",
                                    "query_interval",
                                    "query_max_response_time",
                                    "query_timeout",
                                    "router_enable",
                                    "version") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.Vrfs.Vrf.InheritableDefaults, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.Vrfs.Vrf.InheritableDefaults, self).__setattr__(name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "maximum_groups",
                                        "warning_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.maximum_groups.is_set or
                            self.warning_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.maximum_groups.yfilter != YFilter.not_set or
                            self.warning_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                        if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-groups"):
                            self.maximum_groups = value
                            self.maximum_groups.value_namespace = name_space
                            self.maximum_groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "warning-threshold"):
                            self.warning_threshold = value
                            self.warning_threshold.value_namespace = name_space
                            self.warning_threshold.value_namespace_prefix = name_space_prefix


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.enable.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "explicit-tracking" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.access_group.is_set or
                        self.query_interval.is_set or
                        self.query_max_response_time.is_set or
                        self.query_timeout.is_set or
                        self.router_enable.is_set or
                        self.version.is_set or
                        (self.explicit_tracking is not None) or
                        (self.maximum_groups_per_interface_oor is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_group.yfilter != YFilter.not_set or
                        self.query_interval.yfilter != YFilter.not_set or
                        self.query_max_response_time.yfilter != YFilter.not_set or
                        self.query_timeout.yfilter != YFilter.not_set or
                        self.router_enable.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                        (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "inheritable-defaults" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_group.get_name_leafdata())
                    if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_interval.get_name_leafdata())
                    if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                    if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_timeout.get_name_leafdata())
                    if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_enable.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "explicit-tracking"):
                        if (self.explicit_tracking is None):
                            self.explicit_tracking = Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking()
                            self.explicit_tracking.parent = self
                            self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        return self.explicit_tracking

                    if (child_yang_name == "maximum-groups-per-interface-oor"):
                        if (self.maximum_groups_per_interface_oor is None):
                            self.maximum_groups_per_interface_oor = Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor()
                            self.maximum_groups_per_interface_oor.parent = self
                            self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        return self.maximum_groups_per_interface_oor

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "explicit-tracking" or name == "maximum-groups-per-interface-oor" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-group"):
                        self.access_group = value
                        self.access_group.value_namespace = name_space
                        self.access_group.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-interval"):
                        self.query_interval = value
                        self.query_interval.value_namespace = name_space
                        self.query_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-max-response-time"):
                        self.query_max_response_time = value
                        self.query_max_response_time.value_namespace = name_space
                        self.query_max_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-timeout"):
                        self.query_timeout = value
                        self.query_timeout.value_namespace = name_space
                        self.query_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-enable"):
                        self.router_enable = value
                        self.router_enable.value_namespace = name_space
                        self.router_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix


            class SsmAccessGroups(Entity):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.SsmAccessGroups, self).__init__()

                    self.yang_name = "ssm-access-groups"
                    self.yang_parent_name = "vrf"

                    self.ssm_access_group = YList(self)

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
                                super(Mld.Vrfs.Vrf.SsmAccessGroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.Vrfs.Vrf.SsmAccessGroups, self).__setattr__(name, value)


                class SsmAccessGroup(Entity):
                    """
                    SSM static Access Group
                    
                    .. attribute:: source_address  <key>
                    
                    	IP source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list specifying access group
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__init__()

                        self.yang_name = "ssm-access-group"
                        self.yang_parent_name = "ssm-access-groups"

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("source_address",
                                        "access_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.source_address.is_set or
                            self.access_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.source_address.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ssm-access-group" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_address.get_name_leafdata())
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "source-address" or name == "access-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "source-address"):
                            self.source_address = value
                            self.source_address.value_namespace = name_space
                            self.source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ssm_access_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ssm_access_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssm-access-groups" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ssm-access-group"):
                        for c in self.ssm_access_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ssm_access_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ssm-access-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Maximum(Entity):
                """
                Configure IGMP State Limits
                
                .. attribute:: maximum_groups
                
                	Configure maximum number of groups accepted by this router
                	**type**\:  int
                
                	**range:** 1..75000
                
                	**default value**\: 50000
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "vrf"

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("maximum_groups") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.Vrfs.Vrf.Maximum, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.Vrfs.Vrf.Maximum, self).__setattr__(name, value)

                def has_data(self):
                    return self.maximum_groups.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.maximum_groups.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "maximum" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_groups.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "maximum-groups"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "maximum-groups"):
                        self.maximum_groups = value
                        self.maximum_groups.value_namespace = name_space
                        self.maximum_groups.value_namespace_prefix = name_space_prefix


            class Interfaces(Entity):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"

                    self.interface = YList(self)

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
                                super(Mld.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: join_groups
                    
                    	IGMP join multicast group
                    	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: maximum_groups_per_interface_oor
                    
                    	Configure maximum number of groups accepted per interface by this router
                    	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: query_timeout
                    
                    	IGMP previous querier timeout
                    	**type**\:  int
                    
                    	**range:** 60..300
                    
                    	**units**\: second
                    
                    .. attribute:: router_enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: static_group_group_addresses
                    
                    	IGMP static multicast group
                    	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses>`
                    
                    .. attribute:: version
                    
                    	Version number
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                        self.router_enable = YLeaf(YType.boolean, "router-enable")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")

                        self.join_groups = None
                        self._children_name_map["join_groups"] = "join-groups"
                        self._children_yang_names.add("join-groups")

                        self.maximum_groups_per_interface_oor = None
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        self._children_yang_names.add("maximum-groups-per-interface-oor")

                        self.static_group_group_addresses = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                        self._children_yang_names.add("static-group-group-addresses")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "access_group",
                                        "query_interval",
                                        "query_max_response_time",
                                        "query_timeout",
                                        "router_enable",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mld.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)


                    class JoinGroups(Entity):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__init__()

                            self.yang_name = "join-groups"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.join_group = YList(self)
                            self.join_group_source_address = YList(self)

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
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)


                        class JoinGroup(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                                self.yang_name = "join-group"
                                self.yang_parent_name = "join-groups"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.mode = YLeaf(YType.enumeration, "mode")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "join-group" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mode.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mode"):
                                    self.mode = value
                                    self.mode.value_namespace = name_space
                                    self.mode.value_namespace_prefix = name_space_prefix


                        class JoinGroupSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	Optional IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                                self.yang_name = "join-group-source-address"
                                self.yang_parent_name = "join-groups"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.mode = YLeaf(YType.enumeration, "mode")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "source_address",
                                                "mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.source_address.is_set or
                                    self.mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mode.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "source-address" or name == "mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mode"):
                                    self.mode = value
                                    self.mode.value_namespace = name_space
                                    self.mode.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.join_group:
                                if (c.has_data()):
                                    return True
                            for c in self.join_group_source_address:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.join_group:
                                if (c.has_operation()):
                                    return True
                            for c in self.join_group_source_address:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "join-groups" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "join-group"):
                                for c in self.join_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.join_group.append(c)
                                return c

                            if (child_yang_name == "join-group-source-address"):
                                for c in self.join_group_source_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.join_group_source_address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "join-group" or name == "join-group-source-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class StaticGroupGroupAddresses(Entity):
                        """
                        IGMP static multicast group
                        
                        .. attribute:: static_group_group_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                        
                        .. attribute:: static_group_group_address_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                        
                        .. attribute:: static_group_group_address_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                            self.yang_name = "static-group-group-addresses"
                            self.yang_parent_name = "interface"

                            self.static_group_group_address = YList(self)
                            self.static_group_group_address_group_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask_source_address = YList(self)
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                            self.static_group_group_address_source_address = YList(self)
                            self.static_group_group_address_source_address_source_address_mask = YList(self)

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
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)


                        class StaticGroupGroupAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                                self.yang_name = "static-group-group-address"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-source-address"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "source_address",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.source_address.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "source_address",
                                                "source_address_mask",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.source_address.is_set or
                                    self.source_address_mask.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.source_address_mask.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address-mask"):
                                    self.source_address_mask = value
                                    self.source_address_mask.value_namespace = name_space
                                    self.source_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressGroupAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_address_mask",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_address_mask.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_address_mask.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-address-mask"):
                                    self.group_address_mask = value
                                    self.group_address_mask.value_namespace = name_space
                                    self.group_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_address_mask",
                                                "source_address",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_address_mask.is_set or
                                    self.source_address.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_address_mask.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-address-mask"):
                                    self.group_address_mask = value
                                    self.group_address_mask.value_namespace = name_space
                                    self.group_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address",
                                                "group_address_mask",
                                                "source_address",
                                                "source_address_mask",
                                                "group_count",
                                                "source_count",
                                                "suppress_report") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.group_address.is_set or
                                    self.group_address_mask.is_set or
                                    self.source_address.is_set or
                                    self.source_address_mask.is_set or
                                    self.group_count.is_set or
                                    self.source_count.is_set or
                                    self.suppress_report.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set or
                                    self.group_address_mask.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.source_address_mask.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.source_count.yfilter != YFilter.not_set or
                                    self.suppress_report.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())
                                if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_count.get_name_leafdata())
                                if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_report.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-address-mask"):
                                    self.group_address_mask = value
                                    self.group_address_mask.value_namespace = name_space
                                    self.group_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address-mask"):
                                    self.source_address_mask = value
                                    self.source_address_mask.value_namespace = name_space
                                    self.source_address_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-count"):
                                    self.source_count = value
                                    self.source_count.value_namespace = name_space
                                    self.source_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-report"):
                                    self.suppress_report = value
                                    self.suppress_report.value_namespace = name_space
                                    self.suppress_report.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.static_group_group_address:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_source_address:
                                if (c.has_data()):
                                    return True
                            for c in self.static_group_group_address_source_address_source_address_mask:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.static_group_group_address:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_source_address:
                                if (c.has_operation()):
                                    return True
                            for c in self.static_group_group_address_source_address_source_address_mask:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-addresses" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "static-group-group-address"):
                                for c in self.static_group_group_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-group-address-mask"):
                                for c in self.static_group_group_address_group_address_mask:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_group_address_mask.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-group-address-mask-source-address"):
                                for c in self.static_group_group_address_group_address_mask_source_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_group_address_mask_source_address.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-group-address-mask-source-address-source-address-mask"):
                                for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_group_address_mask_source_address_source_address_mask.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-source-address"):
                                for c in self.static_group_group_address_source_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_source_address.append(c)
                                return c

                            if (child_yang_name == "static-group-group-address-source-address-source-address-mask"):
                                for c in self.static_group_group_address_source_address_source_address_mask:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.static_group_group_address_source_address_source_address_mask.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "static-group-group-address" or name == "static-group-group-address-group-address-mask" or name == "static-group-group-address-group-address-mask-source-address" or name == "static-group-group-address-group-address-mask-source-address-source-address-mask" or name == "static-group-group-address-source-address" or name == "static-group-group-address-source-address-source-address-mask"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class MaximumGroupsPerInterfaceOor(Entity):
                        """
                        Configure maximum number of groups accepted per
                        interface by this router
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: maximum_groups
                        
                        	Maximum number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	 WarningThreshold for number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**default value**\: 25000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                            self.yang_name = "maximum-groups-per-interface-oor"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                            self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_list_name",
                                            "maximum_groups",
                                            "warning_threshold") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_list_name.is_set or
                                self.maximum_groups.is_set or
                                self.warning_threshold.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set or
                                self.maximum_groups.yfilter != YFilter.not_set or
                                self.warning_threshold.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())
                            if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                            if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "maximum-groups"):
                                self.maximum_groups = value
                                self.maximum_groups.value_namespace = name_space
                                self.maximum_groups.value_namespace_prefix = name_space_prefix
                            if(value_path == "warning-threshold"):
                                self.warning_threshold = value
                                self.warning_threshold.value_namespace = name_space
                                self.warning_threshold.value_namespace_prefix = name_space_prefix


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enabled or disabled, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "interface"
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_list_name",
                                            "enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_list_name.is_set or
                                self.enable.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_list_name.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "explicit-tracking" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_list_name.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-list-name" or name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-list-name"):
                                self.access_list_name = value
                                self.access_list_name.value_namespace = name_space
                                self.access_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.access_group.is_set or
                            self.query_interval.is_set or
                            self.query_max_response_time.is_set or
                            self.query_timeout.is_set or
                            self.router_enable.is_set or
                            self.version.is_set or
                            (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_data()) or
                            (self.explicit_tracking is not None) or
                            (self.join_groups is not None) or
                            (self.maximum_groups_per_interface_oor is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.access_group.yfilter != YFilter.not_set or
                            self.query_interval.yfilter != YFilter.not_set or
                            self.query_max_response_time.yfilter != YFilter.not_set or
                            self.query_timeout.yfilter != YFilter.not_set or
                            self.router_enable.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                            (self.join_groups is not None and self.join_groups.has_operation()) or
                            (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()) or
                            (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_group.get_name_leafdata())
                        if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_interval.get_name_leafdata())
                        if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                        if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.query_timeout.get_name_leafdata())
                        if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router_enable.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "explicit-tracking"):
                            if (self.explicit_tracking is None):
                                self.explicit_tracking = Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking()
                                self.explicit_tracking.parent = self
                                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                            return self.explicit_tracking

                        if (child_yang_name == "join-groups"):
                            if (self.join_groups is None):
                                self.join_groups = Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups()
                                self.join_groups.parent = self
                                self._children_name_map["join_groups"] = "join-groups"
                            return self.join_groups

                        if (child_yang_name == "maximum-groups-per-interface-oor"):
                            if (self.maximum_groups_per_interface_oor is None):
                                self.maximum_groups_per_interface_oor = Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor()
                                self.maximum_groups_per_interface_oor.parent = self
                                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                            return self.maximum_groups_per_interface_oor

                        if (child_yang_name == "static-group-group-addresses"):
                            if (self.static_group_group_addresses is None):
                                self.static_group_group_addresses = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                                self.static_group_group_addresses.parent = self
                                self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                            return self.static_group_group_addresses

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "explicit-tracking" or name == "join-groups" or name == "maximum-groups-per-interface-oor" or name == "static-group-group-addresses" or name == "interface-name" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-group"):
                            self.access_group = value
                            self.access_group.value_namespace = name_space
                            self.access_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-interval"):
                            self.query_interval = value
                            self.query_interval.value_namespace = name_space
                            self.query_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-max-response-time"):
                            self.query_max_response_time = value
                            self.query_max_response_time.value_namespace = name_space
                            self.query_max_response_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "query-timeout"):
                            self.query_timeout = value
                            self.query_timeout.value_namespace = name_space
                            self.query_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "router-enable"):
                            self.router_enable = value
                            self.router_enable.value_namespace = name_space
                            self.router_enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mld.Vrfs.Vrf.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.robustness.is_set or
                    self.ssmdns_query_group.is_set or
                    (self.inheritable_defaults is not None and self.inheritable_defaults.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.maximum is not None and self.maximum.has_data()) or
                    (self.ssm_access_groups is not None and self.ssm_access_groups.has_data()) or
                    (self.traffic is not None and self.traffic.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.robustness.yfilter != YFilter.not_set or
                    self.ssmdns_query_group.yfilter != YFilter.not_set or
                    (self.inheritable_defaults is not None and self.inheritable_defaults.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.maximum is not None and self.maximum.has_operation()) or
                    (self.ssm_access_groups is not None and self.ssm_access_groups.has_operation()) or
                    (self.traffic is not None and self.traffic.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.robustness.is_set or self.robustness.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.robustness.get_name_leafdata())
                if (self.ssmdns_query_group.is_set or self.ssmdns_query_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ssmdns_query_group.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "inheritable-defaults"):
                    if (self.inheritable_defaults is None):
                        self.inheritable_defaults = Mld.Vrfs.Vrf.InheritableDefaults()
                        self.inheritable_defaults.parent = self
                        self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                    return self.inheritable_defaults

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Mld.Vrfs.Vrf.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "maximum"):
                    if (self.maximum is None):
                        self.maximum = Mld.Vrfs.Vrf.Maximum()
                        self.maximum.parent = self
                        self._children_name_map["maximum"] = "maximum"
                    return self.maximum

                if (child_yang_name == "ssm-access-groups"):
                    if (self.ssm_access_groups is None):
                        self.ssm_access_groups = Mld.Vrfs.Vrf.SsmAccessGroups()
                        self.ssm_access_groups.parent = self
                        self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                    return self.ssm_access_groups

                if (child_yang_name == "traffic"):
                    if (self.traffic is None):
                        self.traffic = Mld.Vrfs.Vrf.Traffic()
                        self.traffic.parent = self
                        self._children_name_map["traffic"] = "traffic"
                    return self.traffic

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "inheritable-defaults" or name == "interfaces" or name == "maximum" or name == "ssm-access-groups" or name == "traffic" or name == "vrf-name" or name == "robustness" or name == "ssmdns-query-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "robustness"):
                    self.robustness = value
                    self.robustness.value_namespace = name_space
                    self.robustness.value_namespace_prefix = name_space_prefix
                if(value_path == "ssmdns-query-group"):
                    self.ssmdns_query_group = value
                    self.ssmdns_query_group.value_namespace = name_space
                    self.ssmdns_query_group.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Mld.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: accounting
        
        	Configure IGMP accounting for logging join/leave records
        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Accounting>`
        
        .. attribute:: inheritable_defaults
        
        	Inheritable Defaults
        	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults>`
        
        .. attribute:: interfaces
        
        	Interface\-level configuration
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces>`
        
        .. attribute:: maximum
        
        	Configure IGMP State Limits
        	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Maximum>`
        
        .. attribute:: nsf
        
        	Configure NSF specific options
        	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Nsf>`
        
        .. attribute:: robustness
        
        	Configure IGMP Robustness variable
        	**type**\:  int
        
        	**range:** 2..10
        
        	**default value**\: 2
        
        .. attribute:: ssm_access_groups
        
        	IGMP Source specific mode
        	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups>`
        
        .. attribute:: ssmdns_query_group
        
        	Enable SSM mapping using DNS Query
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: traffic
        
        	Configure IGMP Traffic variables
        	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Traffic>`
        
        .. attribute:: unicast_qos_adjust
        
        	Configure IGMP QoS shapers for subscriber interfaces
        	**type**\:   :py:class:`UnicastQosAdjust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.UnicastQosAdjust>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Mld.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "mld"
            self.is_presence_container = True

            self.robustness = YLeaf(YType.uint32, "robustness")

            self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

            self.accounting = Mld.DefaultContext.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"
            self._children_yang_names.add("accounting")

            self.inheritable_defaults = Mld.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
            self._children_yang_names.add("inheritable-defaults")

            self.interfaces = Mld.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.maximum = Mld.DefaultContext.Maximum()
            self.maximum.parent = self
            self._children_name_map["maximum"] = "maximum"
            self._children_yang_names.add("maximum")

            self.nsf = Mld.DefaultContext.Nsf()
            self.nsf.parent = self
            self._children_name_map["nsf"] = "nsf"
            self._children_yang_names.add("nsf")

            self.ssm_access_groups = Mld.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
            self._children_yang_names.add("ssm-access-groups")

            self.traffic = Mld.DefaultContext.Traffic()
            self.traffic.parent = self
            self._children_name_map["traffic"] = "traffic"
            self._children_yang_names.add("traffic")

            self.unicast_qos_adjust = Mld.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self
            self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"
            self._children_yang_names.add("unicast-qos-adjust")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("robustness",
                            "ssmdns_query_group") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Mld.DefaultContext, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Mld.DefaultContext, self).__setattr__(name, value)


        class Nsf(Entity):
            """
            Configure NSF specific options
            
            .. attribute:: lifetime
            
            	Maximum time for IGMP NSF mode in seconds
            	**type**\:  int
            
            	**range:** 10..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Nsf, self).__init__()

                self.yang_name = "nsf"
                self.yang_parent_name = "default-context"

                self.lifetime = YLeaf(YType.uint32, "lifetime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lifetime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.DefaultContext.Nsf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.Nsf, self).__setattr__(name, value)

            def has_data(self):
                return self.lifetime.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lifetime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nsf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lifetime.is_set or self.lifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lifetime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lifetime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lifetime"):
                    self.lifetime = value
                    self.lifetime.value_namespace = name_space
                    self.lifetime.value_namespace_prefix = name_space_prefix


        class UnicastQosAdjust(Entity):
            """
            Configure IGMP QoS shapers for subscriber
            interfaces
            
            .. attribute:: adjustment_delay
            
            	Configure the QoS delay before programming (in seconds)
            	**type**\:  int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 1
            
            .. attribute:: download_interval
            
            	Configure the QoS download interval (in milliseconds)
            	**type**\:  int
            
            	**range:** 10..500
            
            	**units**\: millisecond
            
            	**default value**\: 100
            
            .. attribute:: hold_off
            
            	Configure the QoS hold off time (in seconds)
            	**type**\:  int
            
            	**range:** 5..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.UnicastQosAdjust, self).__init__()

                self.yang_name = "unicast-qos-adjust"
                self.yang_parent_name = "default-context"

                self.adjustment_delay = YLeaf(YType.uint32, "adjustment-delay")

                self.download_interval = YLeaf(YType.uint32, "download-interval")

                self.hold_off = YLeaf(YType.uint32, "hold-off")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("adjustment_delay",
                                "download_interval",
                                "hold_off") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.DefaultContext.UnicastQosAdjust, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.UnicastQosAdjust, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.adjustment_delay.is_set or
                    self.download_interval.is_set or
                    self.hold_off.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.adjustment_delay.yfilter != YFilter.not_set or
                    self.download_interval.yfilter != YFilter.not_set or
                    self.hold_off.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "unicast-qos-adjust" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.adjustment_delay.is_set or self.adjustment_delay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.adjustment_delay.get_name_leafdata())
                if (self.download_interval.is_set or self.download_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.download_interval.get_name_leafdata())
                if (self.hold_off.is_set or self.hold_off.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_off.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "adjustment-delay" or name == "download-interval" or name == "hold-off"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "adjustment-delay"):
                    self.adjustment_delay = value
                    self.adjustment_delay.value_namespace = name_space
                    self.adjustment_delay.value_namespace_prefix = name_space_prefix
                if(value_path == "download-interval"):
                    self.download_interval = value
                    self.download_interval.value_namespace = name_space
                    self.download_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-off"):
                    self.hold_off = value
                    self.hold_off.value_namespace = name_space
                    self.hold_off.value_namespace_prefix = name_space_prefix


        class Accounting(Entity):
            """
            Configure IGMP accounting for logging
            join/leave records
            
            .. attribute:: max_history
            
            	Configure IGMP accounting Maximum History setting
            	**type**\:  int
            
            	**range:** 0..365
            
            	**units**\: day
            
            	**default value**\: 0
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "default-context"

                self.max_history = YLeaf(YType.uint32, "max-history")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("max_history") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.DefaultContext.Accounting, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.Accounting, self).__setattr__(name, value)

            def has_data(self):
                return self.max_history.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.max_history.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "accounting" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.max_history.is_set or self.max_history.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_history.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "max-history"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "max-history"):
                    self.max_history = value
                    self.max_history.value_namespace = name_space
                    self.max_history.value_namespace_prefix = name_space_prefix


        class Traffic(Entity):
            """
            Configure IGMP Traffic variables
            
            .. attribute:: profile
            
            	Configure the route\-policy profile
            	**type**\:  str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Traffic, self).__init__()

                self.yang_name = "traffic"
                self.yang_parent_name = "default-context"

                self.profile = YLeaf(YType.str, "profile")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("profile") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.DefaultContext.Traffic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.Traffic, self).__setattr__(name, value)

            def has_data(self):
                return self.profile.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.profile.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "traffic" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.profile.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "profile"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "profile"):
                    self.profile = value
                    self.profile.value_namespace = name_space
                    self.profile.value_namespace_prefix = name_space_prefix


        class InheritableDefaults(Entity):
            """
            Inheritable Defaults
            
            .. attribute:: access_group
            
            	Access list specifying access group range
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: explicit_tracking
            
            	IGMPv3 explicit host tracking
            	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults.ExplicitTracking>`
            
            	**presence node**\: True
            
            .. attribute:: maximum_groups_per_interface_oor
            
            	Configure maximum number of groups accepted per interface by this router
            	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
            
            	**presence node**\: True
            
            .. attribute:: query_interval
            
            	Query interval in seconds
            	**type**\:  int
            
            	**range:** 1..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: query_max_response_time
            
            	Query response value in seconds
            	**type**\:  int
            
            	**range:** 1..12
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: query_timeout
            
            	IGMP previous querier timeout
            	**type**\:  int
            
            	**range:** 60..300
            
            	**units**\: second
            
            .. attribute:: router_enable
            
            	Enabled or disabled, when value is TRUE or FALSE respectively
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: version
            
            	Version number
            	**type**\:  int
            
            	**range:** 1..3
            
            	**default value**\: 3
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.InheritableDefaults, self).__init__()

                self.yang_name = "inheritable-defaults"
                self.yang_parent_name = "default-context"

                self.access_group = YLeaf(YType.str, "access-group")

                self.query_interval = YLeaf(YType.uint32, "query-interval")

                self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                self.router_enable = YLeaf(YType.boolean, "router-enable")

                self.version = YLeaf(YType.uint32, "version")

                self.explicit_tracking = None
                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                self._children_yang_names.add("explicit-tracking")

                self.maximum_groups_per_interface_oor = None
                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                self._children_yang_names.add("maximum-groups-per-interface-oor")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("access_group",
                                "query_interval",
                                "query_max_response_time",
                                "query_timeout",
                                "router_enable",
                                "version") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.DefaultContext.InheritableDefaults, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.InheritableDefaults, self).__setattr__(name, value)


            class MaximumGroupsPerInterfaceOor(Entity):
                """
                Configure maximum number of groups accepted per
                interface by this router
                
                .. attribute:: access_list_name
                
                	Access\-list to account for
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: maximum_groups
                
                	Maximum number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**mandatory**\: True
                
                .. attribute:: warning_threshold
                
                	 WarningThreshold for number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**default value**\: 25000
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                    self.yang_name = "maximum-groups-per-interface-oor"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                    self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_list_name",
                                    "maximum_groups",
                                    "warning_threshold") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.maximum_groups.is_set or
                        self.warning_threshold.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.maximum_groups.yfilter != YFilter.not_set or
                        self.warning_threshold.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/inheritable-defaults/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                    if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-groups"):
                        self.maximum_groups = value
                        self.maximum_groups.value_namespace = name_space
                        self.maximum_groups.value_namespace_prefix = name_space_prefix
                    if(value_path == "warning-threshold"):
                        self.warning_threshold = value
                        self.warning_threshold.value_namespace = name_space
                        self.warning_threshold.value_namespace_prefix = name_space_prefix


            class ExplicitTracking(Entity):
                """
                IGMPv3 explicit host tracking
                
                .. attribute:: access_list_name
                
                	Access list specifying tracking group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, self).__init__()

                    self.yang_name = "explicit-tracking"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.enable = YLeaf(YType.boolean, "enable")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_list_name",
                                    "enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.enable.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "explicit-tracking" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/inheritable-defaults/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.access_group.is_set or
                    self.query_interval.is_set or
                    self.query_max_response_time.is_set or
                    self.query_timeout.is_set or
                    self.router_enable.is_set or
                    self.version.is_set or
                    (self.explicit_tracking is not None) or
                    (self.maximum_groups_per_interface_oor is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.access_group.yfilter != YFilter.not_set or
                    self.query_interval.yfilter != YFilter.not_set or
                    self.query_max_response_time.yfilter != YFilter.not_set or
                    self.query_timeout.yfilter != YFilter.not_set or
                    self.router_enable.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set or
                    (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                    (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "inheritable-defaults" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access_group.get_name_leafdata())
                if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_interval.get_name_leafdata())
                if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_timeout.get_name_leafdata())
                if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.router_enable.get_name_leafdata())
                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "explicit-tracking"):
                    if (self.explicit_tracking is None):
                        self.explicit_tracking = Mld.DefaultContext.InheritableDefaults.ExplicitTracking()
                        self.explicit_tracking.parent = self
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    return self.explicit_tracking

                if (child_yang_name == "maximum-groups-per-interface-oor"):
                    if (self.maximum_groups_per_interface_oor is None):
                        self.maximum_groups_per_interface_oor = Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor()
                        self.maximum_groups_per_interface_oor.parent = self
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    return self.maximum_groups_per_interface_oor

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "explicit-tracking" or name == "maximum-groups-per-interface-oor" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "access-group"):
                    self.access_group = value
                    self.access_group.value_namespace = name_space
                    self.access_group.value_namespace_prefix = name_space_prefix
                if(value_path == "query-interval"):
                    self.query_interval = value
                    self.query_interval.value_namespace = name_space
                    self.query_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "query-max-response-time"):
                    self.query_max_response_time = value
                    self.query_max_response_time.value_namespace = name_space
                    self.query_max_response_time.value_namespace_prefix = name_space_prefix
                if(value_path == "query-timeout"):
                    self.query_timeout = value
                    self.query_timeout.value_namespace = name_space
                    self.query_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "router-enable"):
                    self.router_enable = value
                    self.router_enable.value_namespace = name_space
                    self.router_enable.value_namespace_prefix = name_space_prefix
                if(value_path == "version"):
                    self.version = value
                    self.version.value_namespace = name_space
                    self.version.value_namespace_prefix = name_space_prefix


        class SsmAccessGroups(Entity):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.SsmAccessGroups, self).__init__()

                self.yang_name = "ssm-access-groups"
                self.yang_parent_name = "default-context"

                self.ssm_access_group = YList(self)

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
                            super(Mld.DefaultContext.SsmAccessGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.SsmAccessGroups, self).__setattr__(name, value)


            class SsmAccessGroup(Entity):
                """
                SSM static Access Group
                
                .. attribute:: source_address  <key>
                
                	IP source address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: access_list_name
                
                	Access list specifying access group
                	**type**\:  str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__init__()

                    self.yang_name = "ssm-access-group"
                    self.yang_parent_name = "ssm-access-groups"

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_address",
                                    "access_list_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.source_address.is_set or
                        self.access_list_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_address.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssm-access-group" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/ssm-access-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_address.get_name_leafdata())
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-address" or name == "access-list-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-address"):
                        self.source_address = value
                        self.source_address.value_namespace = name_space
                        self.source_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ssm_access_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ssm_access_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ssm-access-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssm-access-group"):
                    for c in self.ssm_access_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ssm_access_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssm-access-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Maximum(Entity):
            """
            Configure IGMP State Limits
            
            .. attribute:: maximum_groups
            
            	Configure maximum number of groups accepted by this router
            	**type**\:  int
            
            	**range:** 1..75000
            
            	**default value**\: 50000
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Maximum, self).__init__()

                self.yang_name = "maximum"
                self.yang_parent_name = "default-context"

                self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("maximum_groups") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mld.DefaultContext.Maximum, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.Maximum, self).__setattr__(name, value)

            def has_data(self):
                return self.maximum_groups.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.maximum_groups.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "maximum" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_groups.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "maximum-groups"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "maximum-groups"):
                    self.maximum_groups = value
                    self.maximum_groups.value_namespace = name_space
                    self.maximum_groups.value_namespace_prefix = name_space_prefix


        class Interfaces(Entity):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-context"

                self.interface = YList(self)

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
                            super(Mld.DefaultContext.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mld.DefaultContext.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                The name of the interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: join_groups
                
                	IGMP join multicast group
                	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: static_group_group_addresses
                
                	IGMP static multicast group
                	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses>`
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.join_groups = None
                    self._children_name_map["join_groups"] = "join-groups"
                    self._children_yang_names.add("join-groups")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")

                    self.static_group_group_addresses = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                    self._children_yang_names.add("static-group-group-addresses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "access_group",
                                    "query_interval",
                                    "query_max_response_time",
                                    "query_timeout",
                                    "router_enable",
                                    "version") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mld.DefaultContext.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mld.DefaultContext.Interfaces.Interface, self).__setattr__(name, value)


                class JoinGroups(Entity):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.JoinGroups, self).__init__()

                        self.yang_name = "join-groups"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.join_group = YList(self)
                        self.join_group_source_address = YList(self)

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
                                    super(Mld.DefaultContext.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.DefaultContext.Interfaces.Interface.JoinGroups, self).__setattr__(name, value)


                    class JoinGroup(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                            self.yang_name = "join-group"
                            self.yang_parent_name = "join-groups"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.mode = YLeaf(YType.enumeration, "mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "join-group" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mode"):
                                self.mode = value
                                self.mode.value_namespace = name_space
                                self.mode.value_namespace_prefix = name_space_prefix


                    class JoinGroupSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	Optional IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                            self.yang_name = "join-group-source-address"
                            self.yang_parent_name = "join-groups"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.mode = YLeaf(YType.enumeration, "mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "source_address",
                                            "mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.source_address.is_set or
                                self.mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "source-address" or name == "mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mode"):
                                self.mode = value
                                self.mode.value_namespace = name_space
                                self.mode.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.join_group:
                            if (c.has_data()):
                                return True
                        for c in self.join_group_source_address:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.join_group:
                            if (c.has_operation()):
                                return True
                        for c in self.join_group_source_address:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "join-groups" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "join-group"):
                            for c in self.join_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.join_group.append(c)
                            return c

                        if (child_yang_name == "join-group-source-address"):
                            for c in self.join_group_source_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.join_group_source_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "join-group" or name == "join-group-source-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class StaticGroupGroupAddresses(Entity):
                    """
                    IGMP static multicast group
                    
                    .. attribute:: static_group_group_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                    
                    .. attribute:: static_group_group_address_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                    
                    .. attribute:: static_group_group_address_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                        self.yang_name = "static-group-group-addresses"
                        self.yang_parent_name = "interface"

                        self.static_group_group_address = YList(self)
                        self.static_group_group_address_group_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask_source_address = YList(self)
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                        self.static_group_group_address_source_address = YList(self)
                        self.static_group_group_address_source_address_source_address_mask = YList(self)

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
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__setattr__(name, value)


                    class StaticGroupGroupAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                            self.yang_name = "static-group-group-address"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address" + "[group-address='" + self.group_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-source-address"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "source_address",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.source_address.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "source_address",
                                            "source_address_mask",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.source_address.is_set or
                                self.source_address_mask.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_address_mask.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address-mask"):
                                self.source_address_mask = value
                                self.source_address_mask.value_namespace = name_space
                                self.source_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressGroupAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_address_mask",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_address_mask.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_address_mask.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-address-mask"):
                                self.group_address_mask = value
                                self.group_address_mask.value_namespace = name_space
                                self.group_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_address_mask",
                                            "source_address",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_address_mask.is_set or
                                self.source_address.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_address_mask.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-address-mask"):
                                self.group_address_mask = value
                                self.group_address_mask.value_namespace = name_space
                                self.group_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_address",
                                            "group_address_mask",
                                            "source_address",
                                            "source_address_mask",
                                            "group_count",
                                            "source_count",
                                            "suppress_report") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_address.is_set or
                                self.group_address_mask.is_set or
                                self.source_address.is_set or
                                self.source_address_mask.is_set or
                                self.group_count.is_set or
                                self.source_count.is_set or
                                self.suppress_report.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_address.yfilter != YFilter.not_set or
                                self.group_address_mask.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_address_mask.yfilter != YFilter.not_set or
                                self.group_count.yfilter != YFilter.not_set or
                                self.source_count.yfilter != YFilter.not_set or
                                self.suppress_report.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address.get_name_leafdata())
                            if (self.group_address_mask.is_set or self.group_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_address_mask.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_count.get_name_leafdata())
                            if (self.source_count.is_set or self.source_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_count.get_name_leafdata())
                            if (self.suppress_report.is_set or self.suppress_report.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppress_report.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-address" or name == "group-address-mask" or name == "source-address" or name == "source-address-mask" or name == "group-count" or name == "source-count" or name == "suppress-report"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-address"):
                                self.group_address = value
                                self.group_address.value_namespace = name_space
                                self.group_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-address-mask"):
                                self.group_address_mask = value
                                self.group_address_mask.value_namespace = name_space
                                self.group_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address-mask"):
                                self.source_address_mask = value
                                self.source_address_mask.value_namespace = name_space
                                self.source_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-count"):
                                self.group_count = value
                                self.group_count.value_namespace = name_space
                                self.group_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-count"):
                                self.source_count = value
                                self.source_count.value_namespace = name_space
                                self.source_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppress-report"):
                                self.suppress_report = value
                                self.suppress_report.value_namespace = name_space
                                self.suppress_report.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.static_group_group_address:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_group_address_mask:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_source_address:
                            if (c.has_data()):
                                return True
                        for c in self.static_group_group_address_source_address_source_address_mask:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.static_group_group_address:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_group_address_mask:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_source_address:
                            if (c.has_operation()):
                                return True
                        for c in self.static_group_group_address_source_address_source_address_mask:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-group-group-addresses" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "static-group-group-address"):
                            for c in self.static_group_group_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-group-address-mask"):
                            for c in self.static_group_group_address_group_address_mask:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_group_address_mask.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-group-address-mask-source-address"):
                            for c in self.static_group_group_address_group_address_mask_source_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_group_address_mask_source_address.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-group-address-mask-source-address-source-address-mask"):
                            for c in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-source-address"):
                            for c in self.static_group_group_address_source_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_source_address.append(c)
                            return c

                        if (child_yang_name == "static-group-group-address-source-address-source-address-mask"):
                            for c in self.static_group_group_address_source_address_source_address_mask:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_group_group_address_source_address_source_address_mask.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "static-group-group-address" or name == "static-group-group-address-group-address-mask" or name == "static-group-group-address-group-address-mask-source-address" or name == "static-group-group-address-group-address-mask-source-address-source-address-mask" or name == "static-group-group-address-source-address" or name == "static-group-group-address-source-address-source-address-mask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "maximum_groups",
                                        "warning_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.maximum_groups.is_set or
                            self.warning_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.maximum_groups.yfilter != YFilter.not_set or
                            self.warning_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "maximum-groups-per-interface-oor" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.maximum_groups.is_set or self.maximum_groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_groups.get_name_leafdata())
                        if (self.warning_threshold.is_set or self.warning_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.warning_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "maximum-groups" or name == "warning-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-groups"):
                            self.maximum_groups = value
                            self.maximum_groups.value_namespace = name_space
                            self.maximum_groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "warning-threshold"):
                            self.warning_threshold = value
                            self.warning_threshold.value_namespace = name_space
                            self.warning_threshold.value_namespace_prefix = name_space_prefix


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "interface"
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.enable.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "explicit-tracking" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.access_group.is_set or
                        self.query_interval.is_set or
                        self.query_max_response_time.is_set or
                        self.query_timeout.is_set or
                        self.router_enable.is_set or
                        self.version.is_set or
                        (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_data()) or
                        (self.explicit_tracking is not None) or
                        (self.join_groups is not None) or
                        (self.maximum_groups_per_interface_oor is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.access_group.yfilter != YFilter.not_set or
                        self.query_interval.yfilter != YFilter.not_set or
                        self.query_max_response_time.yfilter != YFilter.not_set or
                        self.query_timeout.yfilter != YFilter.not_set or
                        self.router_enable.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        (self.explicit_tracking is not None and self.explicit_tracking.has_operation()) or
                        (self.join_groups is not None and self.join_groups.has_operation()) or
                        (self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor.has_operation()) or
                        (self.static_group_group_addresses is not None and self.static_group_group_addresses.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.access_group.is_set or self.access_group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_group.get_name_leafdata())
                    if (self.query_interval.is_set or self.query_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_interval.get_name_leafdata())
                    if (self.query_max_response_time.is_set or self.query_max_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_max_response_time.get_name_leafdata())
                    if (self.query_timeout.is_set or self.query_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_timeout.get_name_leafdata())
                    if (self.router_enable.is_set or self.router_enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_enable.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "explicit-tracking"):
                        if (self.explicit_tracking is None):
                            self.explicit_tracking = Mld.DefaultContext.Interfaces.Interface.ExplicitTracking()
                            self.explicit_tracking.parent = self
                            self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        return self.explicit_tracking

                    if (child_yang_name == "join-groups"):
                        if (self.join_groups is None):
                            self.join_groups = Mld.DefaultContext.Interfaces.Interface.JoinGroups()
                            self.join_groups.parent = self
                            self._children_name_map["join_groups"] = "join-groups"
                        return self.join_groups

                    if (child_yang_name == "maximum-groups-per-interface-oor"):
                        if (self.maximum_groups_per_interface_oor is None):
                            self.maximum_groups_per_interface_oor = Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor()
                            self.maximum_groups_per_interface_oor.parent = self
                            self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        return self.maximum_groups_per_interface_oor

                    if (child_yang_name == "static-group-group-addresses"):
                        if (self.static_group_group_addresses is None):
                            self.static_group_group_addresses = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                            self.static_group_group_addresses.parent = self
                            self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                        return self.static_group_group_addresses

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "explicit-tracking" or name == "join-groups" or name == "maximum-groups-per-interface-oor" or name == "static-group-group-addresses" or name == "interface-name" or name == "access-group" or name == "query-interval" or name == "query-max-response-time" or name == "query-timeout" or name == "router-enable" or name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-group"):
                        self.access_group = value
                        self.access_group.value_namespace = name_space
                        self.access_group.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-interval"):
                        self.query_interval = value
                        self.query_interval.value_namespace = name_space
                        self.query_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-max-response-time"):
                        self.query_max_response_time = value
                        self.query_max_response_time.value_namespace = name_space
                        self.query_max_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-timeout"):
                        self.query_timeout = value
                        self.query_timeout.value_namespace = name_space
                        self.query_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-enable"):
                        self.router_enable = value
                        self.router_enable.value_namespace = name_space
                        self.router_enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Mld.DefaultContext.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.robustness.is_set or
                self.ssmdns_query_group.is_set or
                (self.accounting is not None and self.accounting.has_data()) or
                (self.inheritable_defaults is not None and self.inheritable_defaults.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.maximum is not None and self.maximum.has_data()) or
                (self.nsf is not None and self.nsf.has_data()) or
                (self.ssm_access_groups is not None and self.ssm_access_groups.has_data()) or
                (self.traffic is not None and self.traffic.has_data()) or
                (self.unicast_qos_adjust is not None and self.unicast_qos_adjust.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.robustness.yfilter != YFilter.not_set or
                self.ssmdns_query_group.yfilter != YFilter.not_set or
                (self.accounting is not None and self.accounting.has_operation()) or
                (self.inheritable_defaults is not None and self.inheritable_defaults.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.maximum is not None and self.maximum.has_operation()) or
                (self.nsf is not None and self.nsf.has_operation()) or
                (self.ssm_access_groups is not None and self.ssm_access_groups.has_operation()) or
                (self.traffic is not None and self.traffic.has_operation()) or
                (self.unicast_qos_adjust is not None and self.unicast_qos_adjust.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-context" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.robustness.is_set or self.robustness.yfilter != YFilter.not_set):
                leaf_name_data.append(self.robustness.get_name_leafdata())
            if (self.ssmdns_query_group.is_set or self.ssmdns_query_group.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ssmdns_query_group.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "accounting"):
                if (self.accounting is None):
                    self.accounting = Mld.DefaultContext.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                return self.accounting

            if (child_yang_name == "inheritable-defaults"):
                if (self.inheritable_defaults is None):
                    self.inheritable_defaults = Mld.DefaultContext.InheritableDefaults()
                    self.inheritable_defaults.parent = self
                    self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                return self.inheritable_defaults

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Mld.DefaultContext.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "maximum"):
                if (self.maximum is None):
                    self.maximum = Mld.DefaultContext.Maximum()
                    self.maximum.parent = self
                    self._children_name_map["maximum"] = "maximum"
                return self.maximum

            if (child_yang_name == "nsf"):
                if (self.nsf is None):
                    self.nsf = Mld.DefaultContext.Nsf()
                    self.nsf.parent = self
                    self._children_name_map["nsf"] = "nsf"
                return self.nsf

            if (child_yang_name == "ssm-access-groups"):
                if (self.ssm_access_groups is None):
                    self.ssm_access_groups = Mld.DefaultContext.SsmAccessGroups()
                    self.ssm_access_groups.parent = self
                    self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                return self.ssm_access_groups

            if (child_yang_name == "traffic"):
                if (self.traffic is None):
                    self.traffic = Mld.DefaultContext.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                return self.traffic

            if (child_yang_name == "unicast-qos-adjust"):
                if (self.unicast_qos_adjust is None):
                    self.unicast_qos_adjust = Mld.DefaultContext.UnicastQosAdjust()
                    self.unicast_qos_adjust.parent = self
                    self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"
                return self.unicast_qos_adjust

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "accounting" or name == "inheritable-defaults" or name == "interfaces" or name == "maximum" or name == "nsf" or name == "ssm-access-groups" or name == "traffic" or name == "unicast-qos-adjust" or name == "robustness" or name == "ssmdns-query-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "robustness"):
                self.robustness = value
                self.robustness.value_namespace = name_space
                self.robustness.value_namespace_prefix = name_space_prefix
            if(value_path == "ssmdns-query-group"):
                self.ssmdns_query_group = value
                self.ssmdns_query_group.value_namespace = name_space
                self.ssmdns_query_group.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.vrfs is not None and self.vrfs.has_data()) or
            (self.default_context is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.default_context is not None and self.default_context.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-igmp-cfg:mld" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "default-context"):
            if (self.default_context is None):
                self.default_context = Mld.DefaultContext()
                self.default_context.parent = self
                self._children_name_map["default_context"] = "default-context"
            return self.default_context

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Mld.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-context" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Mld()
        return self._top_entity

