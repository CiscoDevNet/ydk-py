""" Cisco_IOS_XR_ip_daps_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-daps package configuration.

This module contains definitions
for the following management objects\:
  address\-pool\-service\: Address Pool configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AddressPoolService(Entity):
    """
    Address Pool configuration data
    
    .. attribute:: vrfs
    
    	Enter VRF specific config mode
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs>`
    
    

    """

    _prefix = 'ip-daps-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(AddressPoolService, self).__init__()
        self._top_entity = None

        self.yang_name = "address-pool-service"
        self.yang_parent_name = "Cisco-IOS-XR-ip-daps-cfg"

        self.vrfs = AddressPoolService.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class Vrfs(Entity):
        """
        Enter VRF specific config mode
        
        .. attribute:: vrf
        
        	Specify VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-daps-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(AddressPoolService.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "address-pool-service"

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
                        super(AddressPoolService.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AddressPoolService.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            Specify VRF Name
            
            .. attribute:: vrf_name  <key>
            
            	none
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4
            
            	Enter IPv4 specific configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4>`
            
            .. attribute:: ipv6
            
            	Enter IPv6 specific mode
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6>`
            
            

            """

            _prefix = 'ip-daps-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(AddressPoolService.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.ipv4 = AddressPoolService.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = AddressPoolService.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AddressPoolService.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AddressPoolService.Vrfs.Vrf, self).__setattr__(name, value)


            class Ipv6(Entity):
                """
                Enter IPv6 specific mode
                
                .. attribute:: pools
                
                	IPv6 Pool Name
                	**type**\:   :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools>`
                
                

                """

                _prefix = 'ip-daps-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Vrfs.Vrf.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "vrf"

                    self.pools = AddressPoolService.Vrfs.Vrf.Ipv6.Pools()
                    self.pools.parent = self
                    self._children_name_map["pools"] = "pools"
                    self._children_yang_names.add("pools")


                class Pools(Entity):
                    """
                    IPv6 Pool Name
                    
                    .. attribute:: pool
                    
                    	Enter the IPv6 Pool name
                    	**type**\: list of    :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool>`
                    
                    

                    """

                    _prefix = 'ip-daps-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools, self).__init__()

                        self.yang_name = "pools"
                        self.yang_parent_name = "ipv6"

                        self.pool = YList(self)

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
                                    super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools, self).__setattr__(name, value)


                    class Pool(Entity):
                        """
                        Enter the IPv6 Pool name
                        
                        .. attribute:: ipv6_pool_name  <key>
                        
                        	Enter the IPv6 Pool name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address_ranges
                        
                        	Specify address range for allocation
                        	**type**\:   :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges>`
                        
                        .. attribute:: excludes
                        
                        	Exclude IPv6 addresses / prefixes
                        	**type**\:   :py:class:`Excludes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes>`
                        
                        .. attribute:: networks
                        
                        	Specify network for allocation
                        	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks>`
                        
                        .. attribute:: prefix_length
                        
                        	Enter the prefix\-length for the Pool
                        	**type**\:  int
                        
                        	**range:** 1..128
                        
                        .. attribute:: prefix_ranges
                        
                        	Specify prefix range for allocation
                        	**type**\:   :py:class:`PrefixRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges>`
                        
                        .. attribute:: utilization_mark
                        
                        	Specify utilization mark
                        	**type**\:   :py:class:`UtilizationMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark>`
                        
                        

                        """

                        _prefix = 'ip-daps-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool, self).__init__()

                            self.yang_name = "pool"
                            self.yang_parent_name = "pools"

                            self.ipv6_pool_name = YLeaf(YType.str, "ipv6-pool-name")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.address_ranges = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges()
                            self.address_ranges.parent = self
                            self._children_name_map["address_ranges"] = "address-ranges"
                            self._children_yang_names.add("address-ranges")

                            self.excludes = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes()
                            self.excludes.parent = self
                            self._children_name_map["excludes"] = "excludes"
                            self._children_yang_names.add("excludes")

                            self.networks = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks()
                            self.networks.parent = self
                            self._children_name_map["networks"] = "networks"
                            self._children_yang_names.add("networks")

                            self.prefix_ranges = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges()
                            self.prefix_ranges.parent = self
                            self._children_name_map["prefix_ranges"] = "prefix-ranges"
                            self._children_yang_names.add("prefix-ranges")

                            self.utilization_mark = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark()
                            self.utilization_mark.parent = self
                            self._children_name_map["utilization_mark"] = "utilization-mark"
                            self._children_yang_names.add("utilization-mark")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_pool_name",
                                            "prefix_length") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool, self).__setattr__(name, value)


                        class AddressRanges(Entity):
                            """
                            Specify address range for allocation
                            
                            .. attribute:: address_range
                            
                            	None
                            	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges, self).__init__()

                                self.yang_name = "address-ranges"
                                self.yang_parent_name = "pool"

                                self.address_range = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges, self).__setattr__(name, value)


                            class AddressRange(Entity):
                                """
                                None
                                
                                .. attribute:: start_address  <key>
                                
                                	Start address of the range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: blocked
                                
                                	Blocked flag
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: end_address
                                
                                	End Address of the range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange, self).__init__()

                                    self.yang_name = "address-range"
                                    self.yang_parent_name = "address-ranges"

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.end_address = YLeaf(YType.str, "end-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("start_address",
                                                    "blocked",
                                                    "end_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.start_address.is_set or
                                        self.blocked.is_set or
                                        self.end_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.start_address.yfilter != YFilter.not_set or
                                        self.blocked.yfilter != YFilter.not_set or
                                        self.end_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address-range" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_address.get_name_leafdata())
                                    if (self.blocked.is_set or self.blocked.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.blocked.get_name_leafdata())
                                    if (self.end_address.is_set or self.end_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.end_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "start-address" or name == "blocked" or name == "end-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "start-address"):
                                        self.start_address = value
                                        self.start_address.value_namespace = name_space
                                        self.start_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "blocked"):
                                        self.blocked = value
                                        self.blocked.value_namespace = name_space
                                        self.blocked.value_namespace_prefix = name_space_prefix
                                    if(value_path == "end-address"):
                                        self.end_address = value
                                        self.end_address.value_namespace = name_space
                                        self.end_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.address_range:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.address_range:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-ranges" + path_buffer

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

                                if (child_yang_name == "address-range"):
                                    for c in self.address_range:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.address_range.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address-range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Excludes(Entity):
                            """
                            Exclude IPv6 addresses / prefixes
                            
                            .. attribute:: exclude
                            
                            	None
                            	**type**\: list of    :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes, self).__init__()

                                self.yang_name = "excludes"
                                self.yang_parent_name = "pool"

                                self.exclude = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes, self).__setattr__(name, value)


                            class Exclude(Entity):
                                """
                                None
                                
                                .. attribute:: start_address  <key>
                                
                                	First Address in IPv6 exclude range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: end_address
                                
                                	Last address in exclude Range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude, self).__init__()

                                    self.yang_name = "exclude"
                                    self.yang_parent_name = "excludes"

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.end_address = YLeaf(YType.str, "end-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("start_address",
                                                    "end_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.start_address.is_set or
                                        self.end_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.start_address.yfilter != YFilter.not_set or
                                        self.end_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "exclude" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_address.get_name_leafdata())
                                    if (self.end_address.is_set or self.end_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.end_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "start-address" or name == "end-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "start-address"):
                                        self.start_address = value
                                        self.start_address.value_namespace = name_space
                                        self.start_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "end-address"):
                                        self.end_address = value
                                        self.end_address.value_namespace = name_space
                                        self.end_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.exclude:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.exclude:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "excludes" + path_buffer

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

                                if (child_yang_name == "exclude"):
                                    for c in self.exclude:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.exclude.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "exclude"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class UtilizationMark(Entity):
                            """
                            Specify utilization mark
                            
                            .. attribute:: high_mark
                            
                            	Specify numerical value as percentage
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            	**units**\: percentage
                            
                            .. attribute:: low_mark
                            
                            	Specify numerical value as percentage
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark, self).__init__()

                                self.yang_name = "utilization-mark"
                                self.yang_parent_name = "pool"

                                self.high_mark = YLeaf(YType.uint32, "high-mark")

                                self.low_mark = YLeaf(YType.uint32, "low-mark")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("high_mark",
                                                "low_mark") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.high_mark.is_set or
                                    self.low_mark.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.high_mark.yfilter != YFilter.not_set or
                                    self.low_mark.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "utilization-mark" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.high_mark.is_set or self.high_mark.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.high_mark.get_name_leafdata())
                                if (self.low_mark.is_set or self.low_mark.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.low_mark.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "high-mark" or name == "low-mark"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "high-mark"):
                                    self.high_mark = value
                                    self.high_mark.value_namespace = name_space
                                    self.high_mark.value_namespace_prefix = name_space_prefix
                                if(value_path == "low-mark"):
                                    self.low_mark = value
                                    self.low_mark.value_namespace = name_space
                                    self.low_mark.value_namespace_prefix = name_space_prefix


                        class PrefixRanges(Entity):
                            """
                            Specify prefix range for allocation
                            
                            .. attribute:: prefix_range
                            
                            	None
                            	**type**\: list of    :py:class:`PrefixRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges, self).__init__()

                                self.yang_name = "prefix-ranges"
                                self.yang_parent_name = "pool"

                                self.prefix_range = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges, self).__setattr__(name, value)


                            class PrefixRange(Entity):
                                """
                                None
                                
                                .. attribute:: start_prefix  <key>
                                
                                	First prefix of range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: blocked
                                
                                	Blocked flag
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: end_prefix
                                
                                	Last prefix of range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange, self).__init__()

                                    self.yang_name = "prefix-range"
                                    self.yang_parent_name = "prefix-ranges"

                                    self.start_prefix = YLeaf(YType.str, "start-prefix")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.end_prefix = YLeaf(YType.str, "end-prefix")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("start_prefix",
                                                    "blocked",
                                                    "end_prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.start_prefix.is_set or
                                        self.blocked.is_set or
                                        self.end_prefix.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.start_prefix.yfilter != YFilter.not_set or
                                        self.blocked.yfilter != YFilter.not_set or
                                        self.end_prefix.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "prefix-range" + "[start-prefix='" + self.start_prefix.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.start_prefix.is_set or self.start_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_prefix.get_name_leafdata())
                                    if (self.blocked.is_set or self.blocked.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.blocked.get_name_leafdata())
                                    if (self.end_prefix.is_set or self.end_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.end_prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "start-prefix" or name == "blocked" or name == "end-prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "start-prefix"):
                                        self.start_prefix = value
                                        self.start_prefix.value_namespace = name_space
                                        self.start_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "blocked"):
                                        self.blocked = value
                                        self.blocked.value_namespace = name_space
                                        self.blocked.value_namespace_prefix = name_space_prefix
                                    if(value_path == "end-prefix"):
                                        self.end_prefix = value
                                        self.end_prefix.value_namespace = name_space
                                        self.end_prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.prefix_range:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.prefix_range:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefix-ranges" + path_buffer

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

                                if (child_yang_name == "prefix-range"):
                                    for c in self.prefix_range:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.prefix_range.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "prefix-range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Networks(Entity):
                            """
                            Specify network for allocation
                            
                            .. attribute:: network
                            
                            	None
                            	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks, self).__init__()

                                self.yang_name = "networks"
                                self.yang_parent_name = "pool"

                                self.network = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks, self).__setattr__(name, value)


                            class Network(Entity):
                                """
                                None
                                
                                .. attribute:: prefix  <key>
                                
                                	None
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: blocked
                                
                                	Blocked flag
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length for the IPv6 Prefix
                                	**type**\:  int
                                
                                	**range:** 1..128
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "networks"

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.blocked = YLeaf(YType.int32, "blocked")

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
                                        if name in ("prefix",
                                                    "blocked",
                                                    "prefix_length") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.prefix.is_set or
                                        self.blocked.is_set or
                                        self.prefix_length.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.prefix.yfilter != YFilter.not_set or
                                        self.blocked.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "network" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix.get_name_leafdata())
                                    if (self.blocked.is_set or self.blocked.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.blocked.get_name_leafdata())
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
                                    if(name == "prefix" or name == "blocked" or name == "prefix-length"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "prefix"):
                                        self.prefix = value
                                        self.prefix.value_namespace = name_space
                                        self.prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "blocked"):
                                        self.blocked = value
                                        self.blocked.value_namespace = name_space
                                        self.blocked.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.network:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.network:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "networks" + path_buffer

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

                                if (child_yang_name == "network"):
                                    for c in self.network:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.network.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "network"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.ipv6_pool_name.is_set or
                                self.prefix_length.is_set or
                                (self.address_ranges is not None and self.address_ranges.has_data()) or
                                (self.excludes is not None and self.excludes.has_data()) or
                                (self.networks is not None and self.networks.has_data()) or
                                (self.prefix_ranges is not None and self.prefix_ranges.has_data()) or
                                (self.utilization_mark is not None and self.utilization_mark.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_pool_name.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                (self.address_ranges is not None and self.address_ranges.has_operation()) or
                                (self.excludes is not None and self.excludes.has_operation()) or
                                (self.networks is not None and self.networks.has_operation()) or
                                (self.prefix_ranges is not None and self.prefix_ranges.has_operation()) or
                                (self.utilization_mark is not None and self.utilization_mark.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pool" + "[ipv6-pool-name='" + self.ipv6_pool_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_pool_name.is_set or self.ipv6_pool_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_pool_name.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "address-ranges"):
                                if (self.address_ranges is None):
                                    self.address_ranges = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges()
                                    self.address_ranges.parent = self
                                    self._children_name_map["address_ranges"] = "address-ranges"
                                return self.address_ranges

                            if (child_yang_name == "excludes"):
                                if (self.excludes is None):
                                    self.excludes = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes()
                                    self.excludes.parent = self
                                    self._children_name_map["excludes"] = "excludes"
                                return self.excludes

                            if (child_yang_name == "networks"):
                                if (self.networks is None):
                                    self.networks = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks()
                                    self.networks.parent = self
                                    self._children_name_map["networks"] = "networks"
                                return self.networks

                            if (child_yang_name == "prefix-ranges"):
                                if (self.prefix_ranges is None):
                                    self.prefix_ranges = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges()
                                    self.prefix_ranges.parent = self
                                    self._children_name_map["prefix_ranges"] = "prefix-ranges"
                                return self.prefix_ranges

                            if (child_yang_name == "utilization-mark"):
                                if (self.utilization_mark is None):
                                    self.utilization_mark = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark()
                                    self.utilization_mark.parent = self
                                    self._children_name_map["utilization_mark"] = "utilization-mark"
                                return self.utilization_mark

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-ranges" or name == "excludes" or name == "networks" or name == "prefix-ranges" or name == "utilization-mark" or name == "ipv6-pool-name" or name == "prefix-length"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-pool-name"):
                                self.ipv6_pool_name = value
                                self.ipv6_pool_name.value_namespace = name_space
                                self.ipv6_pool_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.pool:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.pool:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pools" + path_buffer

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

                        if (child_yang_name == "pool"):
                            for c in self.pool:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.pool.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pool"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.pools is not None and self.pools.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.pools is not None and self.pools.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6" + path_buffer

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

                    if (child_yang_name == "pools"):
                        if (self.pools is None):
                            self.pools = AddressPoolService.Vrfs.Vrf.Ipv6.Pools()
                            self.pools.parent = self
                            self._children_name_map["pools"] = "pools"
                        return self.pools

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pools"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv4(Entity):
                """
                Enter IPv4 specific configuration
                
                .. attribute:: pools
                
                	IPv4 Pool Table
                	**type**\:   :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools>`
                
                

                """

                _prefix = 'ip-daps-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Vrfs.Vrf.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "vrf"

                    self.pools = AddressPoolService.Vrfs.Vrf.Ipv4.Pools()
                    self.pools.parent = self
                    self._children_name_map["pools"] = "pools"
                    self._children_yang_names.add("pools")


                class Pools(Entity):
                    """
                    IPv4 Pool Table
                    
                    .. attribute:: pool
                    
                    	IPv4 Pool name
                    	**type**\: list of    :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool>`
                    
                    

                    """

                    _prefix = 'ip-daps-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools, self).__init__()

                        self.yang_name = "pools"
                        self.yang_parent_name = "ipv4"

                        self.pool = YList(self)

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
                                    super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools, self).__setattr__(name, value)


                    class Pool(Entity):
                        """
                        IPv4 Pool name
                        
                        .. attribute:: pool_name  <key>
                        
                        	Enter the IPv4 Pool name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address_ranges
                        
                        	address range for allocation
                        	**type**\:   :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges>`
                        
                        .. attribute:: excludes
                        
                        	Exclude addresses
                        	**type**\:   :py:class:`Excludes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes>`
                        
                        .. attribute:: networks
                        
                        	Specify network for allocation
                        	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks>`
                        
                        .. attribute:: utilization_mark
                        
                        	Specify utilization mark
                        	**type**\:   :py:class:`UtilizationMark <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark>`
                        
                        

                        """

                        _prefix = 'ip-daps-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool, self).__init__()

                            self.yang_name = "pool"
                            self.yang_parent_name = "pools"

                            self.pool_name = YLeaf(YType.str, "pool-name")

                            self.address_ranges = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges()
                            self.address_ranges.parent = self
                            self._children_name_map["address_ranges"] = "address-ranges"
                            self._children_yang_names.add("address-ranges")

                            self.excludes = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes()
                            self.excludes.parent = self
                            self._children_name_map["excludes"] = "excludes"
                            self._children_yang_names.add("excludes")

                            self.networks = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks()
                            self.networks.parent = self
                            self._children_name_map["networks"] = "networks"
                            self._children_yang_names.add("networks")

                            self.utilization_mark = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark()
                            self.utilization_mark.parent = self
                            self._children_name_map["utilization_mark"] = "utilization-mark"
                            self._children_yang_names.add("utilization-mark")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pool_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool, self).__setattr__(name, value)


                        class AddressRanges(Entity):
                            """
                            address range for allocation
                            
                            .. attribute:: address_range
                            
                            	Specify first address in range
                            	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges, self).__init__()

                                self.yang_name = "address-ranges"
                                self.yang_parent_name = "pool"

                                self.address_range = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges, self).__setattr__(name, value)


                            class AddressRange(Entity):
                                """
                                Specify first address in range
                                
                                .. attribute:: start_address  <key>
                                
                                	Specify first address of the range
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: blocked
                                
                                	Blocked flag
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: end_address
                                
                                	Last address of the range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange, self).__init__()

                                    self.yang_name = "address-range"
                                    self.yang_parent_name = "address-ranges"

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.end_address = YLeaf(YType.str, "end-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("start_address",
                                                    "blocked",
                                                    "end_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.start_address.is_set or
                                        self.blocked.is_set or
                                        self.end_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.start_address.yfilter != YFilter.not_set or
                                        self.blocked.yfilter != YFilter.not_set or
                                        self.end_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address-range" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_address.get_name_leafdata())
                                    if (self.blocked.is_set or self.blocked.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.blocked.get_name_leafdata())
                                    if (self.end_address.is_set or self.end_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.end_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "start-address" or name == "blocked" or name == "end-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "start-address"):
                                        self.start_address = value
                                        self.start_address.value_namespace = name_space
                                        self.start_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "blocked"):
                                        self.blocked = value
                                        self.blocked.value_namespace = name_space
                                        self.blocked.value_namespace_prefix = name_space_prefix
                                    if(value_path == "end-address"):
                                        self.end_address = value
                                        self.end_address.value_namespace = name_space
                                        self.end_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.address_range:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.address_range:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-ranges" + path_buffer

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

                                if (child_yang_name == "address-range"):
                                    for c in self.address_range:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.address_range.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address-range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Excludes(Entity):
                            """
                            Exclude addresses
                            
                            .. attribute:: exclude
                            
                            	First address in range
                            	**type**\: list of    :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes, self).__init__()

                                self.yang_name = "excludes"
                                self.yang_parent_name = "pool"

                                self.exclude = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes, self).__setattr__(name, value)


                            class Exclude(Entity):
                                """
                                First address in range
                                
                                .. attribute:: start_address  <key>
                                
                                	First address in exclude range
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: end_address
                                
                                	Last address in excluded range
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude, self).__init__()

                                    self.yang_name = "exclude"
                                    self.yang_parent_name = "excludes"

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.end_address = YLeaf(YType.str, "end-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("start_address",
                                                    "end_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.start_address.is_set or
                                        self.end_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.start_address.yfilter != YFilter.not_set or
                                        self.end_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "exclude" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_address.get_name_leafdata())
                                    if (self.end_address.is_set or self.end_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.end_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "start-address" or name == "end-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "start-address"):
                                        self.start_address = value
                                        self.start_address.value_namespace = name_space
                                        self.start_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "end-address"):
                                        self.end_address = value
                                        self.end_address.value_namespace = name_space
                                        self.end_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.exclude:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.exclude:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "excludes" + path_buffer

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

                                if (child_yang_name == "exclude"):
                                    for c in self.exclude:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.exclude.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "exclude"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class UtilizationMark(Entity):
                            """
                            Specify utilization mark
                            
                            .. attribute:: high
                            
                            	Specify numerical value as percentage
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            	**units**\: percentage
                            
                            .. attribute:: low
                            
                            	Specify numerical value as percentage
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark, self).__init__()

                                self.yang_name = "utilization-mark"
                                self.yang_parent_name = "pool"

                                self.high = YLeaf(YType.uint32, "high")

                                self.low = YLeaf(YType.uint32, "low")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("high",
                                                "low") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.high.is_set or
                                    self.low.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.high.yfilter != YFilter.not_set or
                                    self.low.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "utilization-mark" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.high.is_set or self.high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.high.get_name_leafdata())
                                if (self.low.is_set or self.low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.low.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "high" or name == "low"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "high"):
                                    self.high = value
                                    self.high.value_namespace = name_space
                                    self.high.value_namespace_prefix = name_space_prefix
                                if(value_path == "low"):
                                    self.low = value
                                    self.low.value_namespace = name_space
                                    self.low.value_namespace_prefix = name_space_prefix


                        class Networks(Entity):
                            """
                            Specify network for allocation
                            
                            .. attribute:: network
                            
                            	Network Prefix
                            	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks, self).__init__()

                                self.yang_name = "networks"
                                self.yang_parent_name = "pool"

                                self.network = YList(self)

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
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks, self).__setattr__(name, value)


                            class Network(Entity):
                                """
                                Network Prefix
                                
                                .. attribute:: ipv4_prefix  <key>
                                
                                	None
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: blocked
                                
                                	Blocked flag
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: default_router
                                
                                	Default Gateway for IPv4 subnet
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: prefix_length
                                
                                	Subnet Length for IPv4 subnet
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'ip-daps-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "networks"

                                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.default_router = YLeaf(YType.str, "default-router")

                                    self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ipv4_prefix",
                                                    "blocked",
                                                    "default_router",
                                                    "prefix_length") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.ipv4_prefix.is_set or
                                        self.blocked.is_set or
                                        self.default_router.is_set or
                                        self.prefix_length.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ipv4_prefix.yfilter != YFilter.not_set or
                                        self.blocked.yfilter != YFilter.not_set or
                                        self.default_router.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "network" + "[ipv4-prefix='" + self.ipv4_prefix.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                    if (self.blocked.is_set or self.blocked.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.blocked.get_name_leafdata())
                                    if (self.default_router.is_set or self.default_router.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.default_router.get_name_leafdata())
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
                                    if(name == "ipv4-prefix" or name == "blocked" or name == "default-router" or name == "prefix-length"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ipv4-prefix"):
                                        self.ipv4_prefix = value
                                        self.ipv4_prefix.value_namespace = name_space
                                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "blocked"):
                                        self.blocked = value
                                        self.blocked.value_namespace = name_space
                                        self.blocked.value_namespace_prefix = name_space_prefix
                                    if(value_path == "default-router"):
                                        self.default_router = value
                                        self.default_router.value_namespace = name_space
                                        self.default_router.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.network:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.network:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "networks" + path_buffer

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

                                if (child_yang_name == "network"):
                                    for c in self.network:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.network.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "network"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.pool_name.is_set or
                                (self.address_ranges is not None and self.address_ranges.has_data()) or
                                (self.excludes is not None and self.excludes.has_data()) or
                                (self.networks is not None and self.networks.has_data()) or
                                (self.utilization_mark is not None and self.utilization_mark.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pool_name.yfilter != YFilter.not_set or
                                (self.address_ranges is not None and self.address_ranges.has_operation()) or
                                (self.excludes is not None and self.excludes.has_operation()) or
                                (self.networks is not None and self.networks.has_operation()) or
                                (self.utilization_mark is not None and self.utilization_mark.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pool" + "[pool-name='" + self.pool_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pool_name.is_set or self.pool_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "address-ranges"):
                                if (self.address_ranges is None):
                                    self.address_ranges = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges()
                                    self.address_ranges.parent = self
                                    self._children_name_map["address_ranges"] = "address-ranges"
                                return self.address_ranges

                            if (child_yang_name == "excludes"):
                                if (self.excludes is None):
                                    self.excludes = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes()
                                    self.excludes.parent = self
                                    self._children_name_map["excludes"] = "excludes"
                                return self.excludes

                            if (child_yang_name == "networks"):
                                if (self.networks is None):
                                    self.networks = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks()
                                    self.networks.parent = self
                                    self._children_name_map["networks"] = "networks"
                                return self.networks

                            if (child_yang_name == "utilization-mark"):
                                if (self.utilization_mark is None):
                                    self.utilization_mark = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark()
                                    self.utilization_mark.parent = self
                                    self._children_name_map["utilization_mark"] = "utilization-mark"
                                return self.utilization_mark

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-ranges" or name == "excludes" or name == "networks" or name == "utilization-mark" or name == "pool-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pool-name"):
                                self.pool_name = value
                                self.pool_name.value_namespace = name_space
                                self.pool_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.pool:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.pool:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pools" + path_buffer

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

                        if (child_yang_name == "pool"):
                            for c in self.pool:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.pool.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pool"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.pools is not None and self.pools.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.pools is not None and self.pools.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + path_buffer

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

                    if (child_yang_name == "pools"):
                        if (self.pools is None):
                            self.pools = AddressPoolService.Vrfs.Vrf.Ipv4.Pools()
                            self.pools.parent = self
                            self._children_name_map["pools"] = "pools"
                        return self.pools

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pools"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.ipv6 is not None and self.ipv6.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-daps-cfg:address-pool-service/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = AddressPoolService.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = AddressPoolService.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4" or name == "ipv6" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ip-daps-cfg:address-pool-service/%s" % self.get_segment_path()
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
                c = AddressPoolService.Vrfs.Vrf()
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

    def has_data(self):
        return (self.vrfs is not None and self.vrfs.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-daps-cfg:address-pool-service" + path_buffer

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

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = AddressPoolService.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AddressPoolService()
        return self._top_entity

