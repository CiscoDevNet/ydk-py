""" Cisco_IOS_XR_ip_daps_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-daps package configuration.

This module contains definitions
for the following management objects\:
  address\-pool\-service\: Address Pool configuration data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"vrfs" : ("vrfs", AddressPoolService.Vrfs)}
        self._child_list_classes = {}

        self.vrfs = AddressPoolService.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-daps-cfg:address-pool-service"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", AddressPoolService.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-daps-cfg:address-pool-service/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AddressPoolService.Vrfs, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv4" : ("ipv4", AddressPoolService.Vrfs.Vrf.Ipv4), "ipv6" : ("ipv6", AddressPoolService.Vrfs.Vrf.Ipv6)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.ipv4 = AddressPoolService.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = AddressPoolService.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-daps-cfg:address-pool-service/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AddressPoolService.Vrfs.Vrf, ['vrf_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"pools" : ("pools", AddressPoolService.Vrfs.Vrf.Ipv4.Pools)}
                    self._child_list_classes = {}

                    self.pools = AddressPoolService.Vrfs.Vrf.Ipv4.Pools()
                    self.pools.parent = self
                    self._children_name_map["pools"] = "pools"
                    self._children_yang_names.add("pools")
                    self._segment_path = lambda: "ipv4"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"pool" : ("pool", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool)}

                        self.pool = YList(self)
                        self._segment_path = lambda: "pools"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools, [], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-ranges" : ("address_ranges", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges), "excludes" : ("excludes", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes), "networks" : ("networks", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks), "utilization-mark" : ("utilization_mark", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "pool" + "[pool-name='" + self.pool_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool, ['pool_name'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"address-range" : ("address_range", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange)}

                                self.address_range = YList(self)
                                self._segment_path = lambda: "address-ranges"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.end_address = YLeaf(YType.str, "end-address")
                                    self._segment_path = lambda: "address-range" + "[start-address='" + self.start_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange, ['start_address', 'blocked', 'end_address'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"exclude" : ("exclude", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude)}

                                self.exclude = YList(self)
                                self._segment_path = lambda: "excludes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.end_address = YLeaf(YType.str, "end-address")
                                    self._segment_path = lambda: "exclude" + "[start-address='" + self.start_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude, ['start_address', 'end_address'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"network" : ("network", AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network)}

                                self.network = YList(self)
                                self._segment_path = lambda: "networks"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.default_router = YLeaf(YType.str, "default-router")

                                    self.prefix_length = YLeaf(YType.int32, "prefix-length")
                                    self._segment_path = lambda: "network" + "[ipv4-prefix='" + self.ipv4_prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network, ['ipv4_prefix', 'blocked', 'default_router', 'prefix_length'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.high = YLeaf(YType.uint32, "high")

                                self.low = YLeaf(YType.uint32, "low")
                                self._segment_path = lambda: "utilization-mark"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark, ['high', 'low'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"pools" : ("pools", AddressPoolService.Vrfs.Vrf.Ipv6.Pools)}
                    self._child_list_classes = {}

                    self.pools = AddressPoolService.Vrfs.Vrf.Ipv6.Pools()
                    self.pools.parent = self
                    self._children_name_map["pools"] = "pools"
                    self._children_yang_names.add("pools")
                    self._segment_path = lambda: "ipv6"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"pool" : ("pool", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool)}

                        self.pool = YList(self)
                        self._segment_path = lambda: "pools"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools, [], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-ranges" : ("address_ranges", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges), "excludes" : ("excludes", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes), "networks" : ("networks", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks), "prefix-ranges" : ("prefix_ranges", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges), "utilization-mark" : ("utilization_mark", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "pool" + "[ipv6-pool-name='" + self.ipv6_pool_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool, ['ipv6_pool_name', 'prefix_length'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"address-range" : ("address_range", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange)}

                                self.address_range = YList(self)
                                self._segment_path = lambda: "address-ranges"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.end_address = YLeaf(YType.str, "end-address")
                                    self._segment_path = lambda: "address-range" + "[start-address='" + self.start_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange, ['start_address', 'blocked', 'end_address'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"exclude" : ("exclude", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude)}

                                self.exclude = YList(self)
                                self._segment_path = lambda: "excludes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.start_address = YLeaf(YType.str, "start-address")

                                    self.end_address = YLeaf(YType.str, "end-address")
                                    self._segment_path = lambda: "exclude" + "[start-address='" + self.start_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude, ['start_address', 'end_address'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"network" : ("network", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network)}

                                self.network = YList(self)
                                self._segment_path = lambda: "networks"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")
                                    self._segment_path = lambda: "network" + "[prefix='" + self.prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network, ['prefix', 'blocked', 'prefix_length'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"prefix-range" : ("prefix_range", AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange)}

                                self.prefix_range = YList(self)
                                self._segment_path = lambda: "prefix-ranges"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges, [], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.start_prefix = YLeaf(YType.str, "start-prefix")

                                    self.blocked = YLeaf(YType.int32, "blocked")

                                    self.end_prefix = YLeaf(YType.str, "end-prefix")
                                    self._segment_path = lambda: "prefix-range" + "[start-prefix='" + self.start_prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange, ['start_prefix', 'blocked', 'end_prefix'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.high_mark = YLeaf(YType.uint32, "high-mark")

                                self.low_mark = YLeaf(YType.uint32, "low-mark")
                                self._segment_path = lambda: "utilization-mark"

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark, ['high_mark', 'low_mark'], name, value)

    def clone_ptr(self):
        self._top_entity = AddressPoolService()
        return self._top_entity

