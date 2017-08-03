""" Cisco_IOS_XR_ip_daps_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-daps package operational data.

This module contains definitions
for the following management objects\:
  address\-pool\-service\: Pool operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DapsClient(Enum):
    """
    DapsClient

    DAPS client types

    .. data:: none = 0

    	Client type is None

    .. data:: ppp = 1

    	Client type is PPP

    .. data:: dhcp = 2

    	Client type is DHCP

    .. data:: dhcpv6 = 4

    	Client type is DHCPv6

    .. data:: ipv6nd = 5

    	Client type is IPv6ND

    """

    none = Enum.YLeaf(0, "none")

    ppp = Enum.YLeaf(1, "ppp")

    dhcp = Enum.YLeaf(2, "dhcp")

    dhcpv6 = Enum.YLeaf(4, "dhcpv6")

    ipv6nd = Enum.YLeaf(5, "ipv6nd")


class IpAddr(Enum):
    """
    IpAddr

    Address type

    .. data:: ipv4 = 2

    	IPv4 address

    .. data:: ipv6 = 10

    	IPv6 address

    """

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(10, "ipv6")



class AddressPoolService(Entity):
    """
    Pool operational data
    
    .. attribute:: nodes
    
    	Pool operational data for a particular location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes>`
    
    

    """

    _prefix = 'ip-daps-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AddressPoolService, self).__init__()
        self._top_entity = None

        self.yang_name = "address-pool-service"
        self.yang_parent_name = "Cisco-IOS-XR-ip-daps-oper"

        self.nodes = AddressPoolService.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Pool operational data for a particular location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node>`
        
        

        """

        _prefix = 'ip-daps-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AddressPoolService.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "address-pool-service"

            self.node = YList(self)

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
                        super(AddressPoolService.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AddressPoolService.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: pools
            
            	List of IPv4/IPv6 pool data
            	**type**\:   :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools>`
            
            .. attribute:: total_utilization
            
            	Show total utilization for pool
            	**type**\:   :py:class:`TotalUtilization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.TotalUtilization>`
            
            .. attribute:: vrfs
            
            	Pool VRF data
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs>`
            
            

            """

            _prefix = 'ip-daps-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AddressPoolService.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.pools = AddressPoolService.Nodes.Node.Pools()
                self.pools.parent = self
                self._children_name_map["pools"] = "pools"
                self._children_yang_names.add("pools")

                self.total_utilization = AddressPoolService.Nodes.Node.TotalUtilization()
                self.total_utilization.parent = self
                self._children_name_map["total_utilization"] = "total-utilization"
                self._children_yang_names.add("total-utilization")

                self.vrfs = AddressPoolService.Nodes.Node.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AddressPoolService.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AddressPoolService.Nodes.Node, self).__setattr__(name, value)


            class Pools(Entity):
                """
                List of IPv4/IPv6 pool data
                
                .. attribute:: pool
                
                	Pool data by pool name
                	**type**\: list of    :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool>`
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Nodes.Node.Pools, self).__init__()

                    self.yang_name = "pools"
                    self.yang_parent_name = "node"

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
                                super(AddressPoolService.Nodes.Node.Pools, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AddressPoolService.Nodes.Node.Pools, self).__setattr__(name, value)


                class Pool(Entity):
                    """
                    Pool data by pool name
                    
                    .. attribute:: pool_name  <key>
                    
                    	The pool name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: address_ranges
                    
                    	Summary info for pool
                    	**type**\:   :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges>`
                    
                    .. attribute:: allocated_addresses
                    
                    	Detailed info for the Pool
                    	**type**\:   :py:class:`AllocatedAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses>`
                    
                    .. attribute:: configuration
                    
                    	Configuration info for pool
                    	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.Configuration>`
                    
                    

                    """

                    _prefix = 'ip-daps-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AddressPoolService.Nodes.Node.Pools.Pool, self).__init__()

                        self.yang_name = "pool"
                        self.yang_parent_name = "pools"

                        self.pool_name = YLeaf(YType.str, "pool-name")

                        self.address_ranges = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"
                        self._children_yang_names.add("address-ranges")

                        self.allocated_addresses = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses()
                        self.allocated_addresses.parent = self
                        self._children_name_map["allocated_addresses"] = "allocated-addresses"
                        self._children_yang_names.add("allocated-addresses")

                        self.configuration = AddressPoolService.Nodes.Node.Pools.Pool.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                        self._children_yang_names.add("configuration")

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
                                    super(AddressPoolService.Nodes.Node.Pools.Pool, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AddressPoolService.Nodes.Node.Pools.Pool, self).__setattr__(name, value)


                    class AddressRanges(Entity):
                        """
                        Summary info for pool
                        
                        .. attribute:: address_range
                        
                        	Start Address of the Range
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges, self).__init__()

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
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges, self).__setattr__(name, value)


                        class AddressRange(Entity):
                            """
                            Start Address of the Range
                            
                            .. attribute:: start_address  <key>
                            
                            	IP Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: allocated_addresses
                            
                            	Number of addresses allocated
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: default_router
                            
                            	Default router
                            	**type**\:   :py:class:`DefaultRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter>`
                            
                            .. attribute:: end_address
                            
                            	Range end
                            	**type**\:   :py:class:`EndAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress>`
                            
                            .. attribute:: excluded_addresses
                            
                            	Number of addresses excluded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free_addresses
                            
                            	Number of addresses free
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_blocked_status
                            
                            	Is network blocked
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_blocked_status_trp
                            
                            	Is network blocked trap send
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pool_name
                            
                            	Pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: pool_scope
                            
                            	Pool scope
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: start_address_xr
                            
                            	Range start
                            	**type**\:   :py:class:`StartAddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr>`
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"

                                self.start_address = YLeaf(YType.str, "start-address")

                                self.allocated_addresses = YLeaf(YType.uint32, "allocated-addresses")

                                self.excluded_addresses = YLeaf(YType.uint32, "excluded-addresses")

                                self.free_addresses = YLeaf(YType.uint32, "free-addresses")

                                self.network_blocked_status = YLeaf(YType.uint32, "network-blocked-status")

                                self.network_blocked_status_trp = YLeaf(YType.uint32, "network-blocked-status-trp")

                                self.pool_name = YLeaf(YType.str, "pool-name")

                                self.pool_scope = YLeaf(YType.str, "pool-scope")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                                self.default_router = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter()
                                self.default_router.parent = self
                                self._children_name_map["default_router"] = "default-router"
                                self._children_yang_names.add("default-router")

                                self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress()
                                self.end_address.parent = self
                                self._children_name_map["end_address"] = "end-address"
                                self._children_yang_names.add("end-address")

                                self.start_address_xr = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr()
                                self.start_address_xr.parent = self
                                self._children_name_map["start_address_xr"] = "start-address-xr"
                                self._children_yang_names.add("start-address-xr")

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
                                                "allocated_addresses",
                                                "excluded_addresses",
                                                "free_addresses",
                                                "network_blocked_status",
                                                "network_blocked_status_trp",
                                                "pool_name",
                                                "pool_scope",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange, self).__setattr__(name, value)


                            class StartAddressXr(Entity):
                                """
                                Range start
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr, self).__init__()

                                    self.yang_name = "start-address-xr"
                                    self.yang_parent_name = "address-range"

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "start-address-xr"

                                        self.address_family = YLeaf(YType.enumeration, "address-family")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_family",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address_family.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_family.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_family.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-family" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-family"):
                                            self.address_family = value
                                            self.address_family.value_namespace = name_space
                                            self.address_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.address is not None and self.address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "start-address-xr" + path_buffer

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

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class EndAddress(Entity):
                                """
                                Range end
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress, self).__init__()

                                    self.yang_name = "end-address"
                                    self.yang_parent_name = "address-range"

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "end-address"

                                        self.address_family = YLeaf(YType.enumeration, "address-family")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_family",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address_family.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_family.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_family.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-family" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-family"):
                                            self.address_family = value
                                            self.address_family.value_namespace = name_space
                                            self.address_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.address is not None and self.address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "end-address" + path_buffer

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

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class DefaultRouter(Entity):
                                """
                                Default router
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter, self).__init__()

                                    self.yang_name = "default-router"
                                    self.yang_parent_name = "address-range"

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "default-router"

                                        self.address_family = YLeaf(YType.enumeration, "address-family")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_family",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address_family.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_family.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_family.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-family" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-family"):
                                            self.address_family = value
                                            self.address_family.value_namespace = name_space
                                            self.address_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.address is not None and self.address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "default-router" + path_buffer

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

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.start_address.is_set or
                                    self.allocated_addresses.is_set or
                                    self.excluded_addresses.is_set or
                                    self.free_addresses.is_set or
                                    self.network_blocked_status.is_set or
                                    self.network_blocked_status_trp.is_set or
                                    self.pool_name.is_set or
                                    self.pool_scope.is_set or
                                    self.vrf_name.is_set or
                                    (self.default_router is not None and self.default_router.has_data()) or
                                    (self.end_address is not None and self.end_address.has_data()) or
                                    (self.start_address_xr is not None and self.start_address_xr.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.start_address.yfilter != YFilter.not_set or
                                    self.allocated_addresses.yfilter != YFilter.not_set or
                                    self.excluded_addresses.yfilter != YFilter.not_set or
                                    self.free_addresses.yfilter != YFilter.not_set or
                                    self.network_blocked_status.yfilter != YFilter.not_set or
                                    self.network_blocked_status_trp.yfilter != YFilter.not_set or
                                    self.pool_name.yfilter != YFilter.not_set or
                                    self.pool_scope.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set or
                                    (self.default_router is not None and self.default_router.has_operation()) or
                                    (self.end_address is not None and self.end_address.has_operation()) or
                                    (self.start_address_xr is not None and self.start_address_xr.has_operation()))

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
                                if (self.allocated_addresses.is_set or self.allocated_addresses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allocated_addresses.get_name_leafdata())
                                if (self.excluded_addresses.is_set or self.excluded_addresses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded_addresses.get_name_leafdata())
                                if (self.free_addresses.is_set or self.free_addresses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free_addresses.get_name_leafdata())
                                if (self.network_blocked_status.is_set or self.network_blocked_status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_blocked_status.get_name_leafdata())
                                if (self.network_blocked_status_trp.is_set or self.network_blocked_status_trp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_blocked_status_trp.get_name_leafdata())
                                if (self.pool_name.is_set or self.pool_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pool_name.get_name_leafdata())
                                if (self.pool_scope.is_set or self.pool_scope.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pool_scope.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "default-router"):
                                    if (self.default_router is None):
                                        self.default_router = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter()
                                        self.default_router.parent = self
                                        self._children_name_map["default_router"] = "default-router"
                                    return self.default_router

                                if (child_yang_name == "end-address"):
                                    if (self.end_address is None):
                                        self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress()
                                        self.end_address.parent = self
                                        self._children_name_map["end_address"] = "end-address"
                                    return self.end_address

                                if (child_yang_name == "start-address-xr"):
                                    if (self.start_address_xr is None):
                                        self.start_address_xr = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr()
                                        self.start_address_xr.parent = self
                                        self._children_name_map["start_address_xr"] = "start-address-xr"
                                    return self.start_address_xr

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "default-router" or name == "end-address" or name == "start-address-xr" or name == "start-address" or name == "allocated-addresses" or name == "excluded-addresses" or name == "free-addresses" or name == "network-blocked-status" or name == "network-blocked-status-trp" or name == "pool-name" or name == "pool-scope" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "start-address"):
                                    self.start_address = value
                                    self.start_address.value_namespace = name_space
                                    self.start_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "allocated-addresses"):
                                    self.allocated_addresses = value
                                    self.allocated_addresses.value_namespace = name_space
                                    self.allocated_addresses.value_namespace_prefix = name_space_prefix
                                if(value_path == "excluded-addresses"):
                                    self.excluded_addresses = value
                                    self.excluded_addresses.value_namespace = name_space
                                    self.excluded_addresses.value_namespace_prefix = name_space_prefix
                                if(value_path == "free-addresses"):
                                    self.free_addresses = value
                                    self.free_addresses.value_namespace = name_space
                                    self.free_addresses.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-blocked-status"):
                                    self.network_blocked_status = value
                                    self.network_blocked_status.value_namespace = name_space
                                    self.network_blocked_status.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-blocked-status-trp"):
                                    self.network_blocked_status_trp = value
                                    self.network_blocked_status_trp.value_namespace = name_space
                                    self.network_blocked_status_trp.value_namespace_prefix = name_space_prefix
                                if(value_path == "pool-name"):
                                    self.pool_name = value
                                    self.pool_name.value_namespace = name_space
                                    self.pool_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "pool-scope"):
                                    self.pool_scope = value
                                    self.pool_scope.value_namespace = name_space
                                    self.pool_scope.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

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
                                c = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange()
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


                    class AllocatedAddresses(Entity):
                        """
                        Detailed info for the Pool
                        
                        .. attribute:: address_range
                        
                        	Address ranges
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange>`
                        
                        .. attribute:: in_use_address
                        
                        	In\-use addresses
                        	**type**\: list of    :py:class:`InUseAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress>`
                        
                        .. attribute:: pool_allocations
                        
                        	Pool allocations
                        	**type**\:   :py:class:`PoolAllocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses, self).__init__()

                            self.yang_name = "allocated-addresses"
                            self.yang_parent_name = "pool"

                            self.pool_allocations = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations()
                            self.pool_allocations.parent = self
                            self._children_name_map["pool_allocations"] = "pool-allocations"
                            self._children_yang_names.add("pool-allocations")

                            self.address_range = YList(self)
                            self.in_use_address = YList(self)

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
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses, self).__setattr__(name, value)


                        class PoolAllocations(Entity):
                            """
                            Pool allocations
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: high_threshold
                            
                            	High threshold data
                            	**type**\:   :py:class:`HighThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold>`
                            
                            .. attribute:: low_threshold
                            
                            	Low threshold data
                            	**type**\:   :py:class:`LowThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold>`
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: utilization
                            
                            	Current utilization in percentage
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations, self).__init__()

                                self.yang_name = "pool-allocations"
                                self.yang_parent_name = "allocated-addresses"

                                self.excluded = YLeaf(YType.uint32, "excluded")

                                self.free = YLeaf(YType.uint32, "free")

                                self.total = YLeaf(YType.uint32, "total")

                                self.used = YLeaf(YType.uint32, "used")

                                self.utilization = YLeaf(YType.uint32, "utilization")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                                self.high_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold()
                                self.high_threshold.parent = self
                                self._children_name_map["high_threshold"] = "high-threshold"
                                self._children_yang_names.add("high-threshold")

                                self.low_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold()
                                self.low_threshold.parent = self
                                self._children_name_map["low_threshold"] = "low-threshold"
                                self._children_yang_names.add("low-threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("excluded",
                                                "free",
                                                "total",
                                                "used",
                                                "utilization",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations, self).__setattr__(name, value)


                            class HighThreshold(Entity):
                                """
                                High threshold data
                                
                                .. attribute:: threshold
                                
                                	Threshold in percentage
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: time_last_crossed
                                
                                	Last time at which threshold crossed in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\:  str
                                
                                .. attribute:: triggers
                                
                                	Number of Triggers
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold, self).__init__()

                                    self.yang_name = "high-threshold"
                                    self.yang_parent_name = "pool-allocations"

                                    self.threshold = YLeaf(YType.uint32, "threshold")

                                    self.time_last_crossed = YLeaf(YType.str, "time-last-crossed")

                                    self.triggers = YLeaf(YType.uint32, "triggers")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("threshold",
                                                    "time_last_crossed",
                                                    "triggers") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.threshold.is_set or
                                        self.time_last_crossed.is_set or
                                        self.triggers.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.threshold.yfilter != YFilter.not_set or
                                        self.time_last_crossed.yfilter != YFilter.not_set or
                                        self.triggers.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "high-threshold" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.threshold.get_name_leafdata())
                                    if (self.time_last_crossed.is_set or self.time_last_crossed.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_last_crossed.get_name_leafdata())
                                    if (self.triggers.is_set or self.triggers.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.triggers.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "threshold" or name == "time-last-crossed" or name == "triggers"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "threshold"):
                                        self.threshold = value
                                        self.threshold.value_namespace = name_space
                                        self.threshold.value_namespace_prefix = name_space_prefix
                                    if(value_path == "time-last-crossed"):
                                        self.time_last_crossed = value
                                        self.time_last_crossed.value_namespace = name_space
                                        self.time_last_crossed.value_namespace_prefix = name_space_prefix
                                    if(value_path == "triggers"):
                                        self.triggers = value
                                        self.triggers.value_namespace = name_space
                                        self.triggers.value_namespace_prefix = name_space_prefix


                            class LowThreshold(Entity):
                                """
                                Low threshold data
                                
                                .. attribute:: threshold
                                
                                	Threshold in percentage
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: time_last_crossed
                                
                                	Last time at which threshold crossed in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\:  str
                                
                                .. attribute:: triggers
                                
                                	Number of Triggers
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold, self).__init__()

                                    self.yang_name = "low-threshold"
                                    self.yang_parent_name = "pool-allocations"

                                    self.threshold = YLeaf(YType.uint32, "threshold")

                                    self.time_last_crossed = YLeaf(YType.str, "time-last-crossed")

                                    self.triggers = YLeaf(YType.uint32, "triggers")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("threshold",
                                                    "time_last_crossed",
                                                    "triggers") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.threshold.is_set or
                                        self.time_last_crossed.is_set or
                                        self.triggers.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.threshold.yfilter != YFilter.not_set or
                                        self.time_last_crossed.yfilter != YFilter.not_set or
                                        self.triggers.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "low-threshold" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.threshold.get_name_leafdata())
                                    if (self.time_last_crossed.is_set or self.time_last_crossed.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_last_crossed.get_name_leafdata())
                                    if (self.triggers.is_set or self.triggers.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.triggers.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "threshold" or name == "time-last-crossed" or name == "triggers"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "threshold"):
                                        self.threshold = value
                                        self.threshold.value_namespace = name_space
                                        self.threshold.value_namespace_prefix = name_space_prefix
                                    if(value_path == "time-last-crossed"):
                                        self.time_last_crossed = value
                                        self.time_last_crossed.value_namespace = name_space
                                        self.time_last_crossed.value_namespace_prefix = name_space_prefix
                                    if(value_path == "triggers"):
                                        self.triggers = value
                                        self.triggers.value_namespace = name_space
                                        self.triggers.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.excluded.is_set or
                                    self.free.is_set or
                                    self.total.is_set or
                                    self.used.is_set or
                                    self.utilization.is_set or
                                    self.vrf_name.is_set or
                                    (self.high_threshold is not None and self.high_threshold.has_data()) or
                                    (self.low_threshold is not None and self.low_threshold.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.excluded.yfilter != YFilter.not_set or
                                    self.free.yfilter != YFilter.not_set or
                                    self.total.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set or
                                    self.utilization.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set or
                                    (self.high_threshold is not None and self.high_threshold.has_operation()) or
                                    (self.low_threshold is not None and self.low_threshold.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pool-allocations" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.excluded.is_set or self.excluded.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded.get_name_leafdata())
                                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free.get_name_leafdata())
                                if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())
                                if (self.utilization.is_set or self.utilization.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.utilization.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "high-threshold"):
                                    if (self.high_threshold is None):
                                        self.high_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold()
                                        self.high_threshold.parent = self
                                        self._children_name_map["high_threshold"] = "high-threshold"
                                    return self.high_threshold

                                if (child_yang_name == "low-threshold"):
                                    if (self.low_threshold is None):
                                        self.low_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold()
                                        self.low_threshold.parent = self
                                        self._children_name_map["low_threshold"] = "low-threshold"
                                    return self.low_threshold

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "high-threshold" or name == "low-threshold" or name == "excluded" or name == "free" or name == "total" or name == "used" or name == "utilization" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "excluded"):
                                    self.excluded = value
                                    self.excluded.value_namespace = name_space
                                    self.excluded.value_namespace_prefix = name_space_prefix
                                if(value_path == "free"):
                                    self.free = value
                                    self.free.value_namespace = name_space
                                    self.free.value_namespace_prefix = name_space_prefix
                                if(value_path == "total"):
                                    self.total = value
                                    self.total.value_namespace = name_space
                                    self.total.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix
                                if(value_path == "utilization"):
                                    self.utilization = value
                                    self.utilization.value_namespace = name_space
                                    self.utilization.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class AddressRange(Entity):
                            """
                            Address ranges
                            
                            .. attribute:: end_address
                            
                            	Range end
                            	**type**\:   :py:class:`EndAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress>`
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_address
                            
                            	Range start
                            	**type**\:   :py:class:`StartAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress>`
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "allocated-addresses"

                                self.excluded = YLeaf(YType.uint32, "excluded")

                                self.free = YLeaf(YType.uint32, "free")

                                self.used = YLeaf(YType.uint32, "used")

                                self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress()
                                self.end_address.parent = self
                                self._children_name_map["end_address"] = "end-address"
                                self._children_yang_names.add("end-address")

                                self.start_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress()
                                self.start_address.parent = self
                                self._children_name_map["start_address"] = "start-address"
                                self._children_yang_names.add("start-address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("excluded",
                                                "free",
                                                "used") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange, self).__setattr__(name, value)


                            class StartAddress(Entity):
                                """
                                Range start
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress, self).__init__()

                                    self.yang_name = "start-address"
                                    self.yang_parent_name = "address-range"

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "start-address"

                                        self.address_family = YLeaf(YType.enumeration, "address-family")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_family",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address_family.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_family.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_family.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-family" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-family"):
                                            self.address_family = value
                                            self.address_family.value_namespace = name_space
                                            self.address_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.address is not None and self.address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "start-address" + path_buffer

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

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class EndAddress(Entity):
                                """
                                Range end
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress, self).__init__()

                                    self.yang_name = "end-address"
                                    self.yang_parent_name = "address-range"

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "end-address"

                                        self.address_family = YLeaf(YType.enumeration, "address-family")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_family",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address_family.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_family.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_family.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-family" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-family"):
                                            self.address_family = value
                                            self.address_family.value_namespace = name_space
                                            self.address_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.address is not None and self.address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "end-address" + path_buffer

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

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.excluded.is_set or
                                    self.free.is_set or
                                    self.used.is_set or
                                    (self.end_address is not None and self.end_address.has_data()) or
                                    (self.start_address is not None and self.start_address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.excluded.yfilter != YFilter.not_set or
                                    self.free.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set or
                                    (self.end_address is not None and self.end_address.has_operation()) or
                                    (self.start_address is not None and self.start_address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-range" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.excluded.is_set or self.excluded.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded.get_name_leafdata())
                                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "end-address"):
                                    if (self.end_address is None):
                                        self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress()
                                        self.end_address.parent = self
                                        self._children_name_map["end_address"] = "end-address"
                                    return self.end_address

                                if (child_yang_name == "start-address"):
                                    if (self.start_address is None):
                                        self.start_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress()
                                        self.start_address.parent = self
                                        self._children_name_map["start_address"] = "start-address"
                                    return self.start_address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "end-address" or name == "start-address" or name == "excluded" or name == "free" or name == "used"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "excluded"):
                                    self.excluded = value
                                    self.excluded.value_namespace = name_space
                                    self.excluded.value_namespace_prefix = name_space_prefix
                                if(value_path == "free"):
                                    self.free = value
                                    self.free.value_namespace = name_space
                                    self.free.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix


                        class InUseAddress(Entity):
                            """
                            In\-use addresses
                            
                            .. attribute:: address
                            
                            	Client address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address>`
                            
                            .. attribute:: client_type
                            
                            	Client type
                            	**type**\:   :py:class:`DapsClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.DapsClient>`
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress, self).__init__()

                                self.yang_name = "in-use-address"
                                self.yang_parent_name = "allocated-addresses"

                                self.client_type = YLeaf(YType.enumeration, "client-type")

                                self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("client_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress, self).__setattr__(name, value)


                            class Address(Entity):
                                """
                                Client address
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "in-use-address"

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "address"

                                        self.address_family = YLeaf(YType.enumeration, "address-family")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_family",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address_family.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_family.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_family.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-family" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-family"):
                                            self.address_family = value
                                            self.address_family.value_namespace = name_space
                                            self.address_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.address is not None and self.address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address" + path_buffer

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

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.client_type.is_set or
                                    (self.address is not None and self.address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.client_type.yfilter != YFilter.not_set or
                                    (self.address is not None and self.address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "in-use-address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.client_type.is_set or self.client_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.client_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "address"):
                                    if (self.address is None):
                                        self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address()
                                        self.address.parent = self
                                        self._children_name_map["address"] = "address"
                                    return self.address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "client-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "client-type"):
                                    self.client_type = value
                                    self.client_type.value_namespace = name_space
                                    self.client_type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address_range:
                                if (c.has_data()):
                                    return True
                            for c in self.in_use_address:
                                if (c.has_data()):
                                    return True
                            return (self.pool_allocations is not None and self.pool_allocations.has_data())

                        def has_operation(self):
                            for c in self.address_range:
                                if (c.has_operation()):
                                    return True
                            for c in self.in_use_address:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.pool_allocations is not None and self.pool_allocations.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "allocated-addresses" + path_buffer

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
                                c = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address_range.append(c)
                                return c

                            if (child_yang_name == "in-use-address"):
                                for c in self.in_use_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.in_use_address.append(c)
                                return c

                            if (child_yang_name == "pool-allocations"):
                                if (self.pool_allocations is None):
                                    self.pool_allocations = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations()
                                    self.pool_allocations.parent = self
                                    self._children_name_map["pool_allocations"] = "pool-allocations"
                                return self.pool_allocations

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-range" or name == "in-use-address" or name == "pool-allocations"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Configuration(Entity):
                        """
                        Configuration info for pool
                        
                        .. attribute:: current_utilization
                        
                        	Current utilization
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: high_utilization_mark
                        
                        	High utilization mark
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: low_utilization_mark
                        
                        	Low utilization mark
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: pool_id
                        
                        	Pool ID for MIBS
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pool_name
                        
                        	Pool name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: pool_prefix_length
                        
                        	Prefix length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pool_scope
                        
                        	Pool Scope
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: utilization_high_count
                        
                        	Number of times High utilization threshold was crossed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: utilization_low_count
                        
                        	Number of times Low utilization threshold was crossed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Pools.Pool.Configuration, self).__init__()

                            self.yang_name = "configuration"
                            self.yang_parent_name = "pool"

                            self.current_utilization = YLeaf(YType.uint8, "current-utilization")

                            self.high_utilization_mark = YLeaf(YType.uint8, "high-utilization-mark")

                            self.low_utilization_mark = YLeaf(YType.uint8, "low-utilization-mark")

                            self.pool_id = YLeaf(YType.uint32, "pool-id")

                            self.pool_name = YLeaf(YType.str, "pool-name")

                            self.pool_prefix_length = YLeaf(YType.uint32, "pool-prefix-length")

                            self.pool_scope = YLeaf(YType.str, "pool-scope")

                            self.utilization_high_count = YLeaf(YType.uint32, "utilization-high-count")

                            self.utilization_low_count = YLeaf(YType.uint32, "utilization-low-count")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("current_utilization",
                                            "high_utilization_mark",
                                            "low_utilization_mark",
                                            "pool_id",
                                            "pool_name",
                                            "pool_prefix_length",
                                            "pool_scope",
                                            "utilization_high_count",
                                            "utilization_low_count",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.Configuration, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.Configuration, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.current_utilization.is_set or
                                self.high_utilization_mark.is_set or
                                self.low_utilization_mark.is_set or
                                self.pool_id.is_set or
                                self.pool_name.is_set or
                                self.pool_prefix_length.is_set or
                                self.pool_scope.is_set or
                                self.utilization_high_count.is_set or
                                self.utilization_low_count.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.current_utilization.yfilter != YFilter.not_set or
                                self.high_utilization_mark.yfilter != YFilter.not_set or
                                self.low_utilization_mark.yfilter != YFilter.not_set or
                                self.pool_id.yfilter != YFilter.not_set or
                                self.pool_name.yfilter != YFilter.not_set or
                                self.pool_prefix_length.yfilter != YFilter.not_set or
                                self.pool_scope.yfilter != YFilter.not_set or
                                self.utilization_high_count.yfilter != YFilter.not_set or
                                self.utilization_low_count.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "configuration" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.current_utilization.is_set or self.current_utilization.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.current_utilization.get_name_leafdata())
                            if (self.high_utilization_mark.is_set or self.high_utilization_mark.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.high_utilization_mark.get_name_leafdata())
                            if (self.low_utilization_mark.is_set or self.low_utilization_mark.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.low_utilization_mark.get_name_leafdata())
                            if (self.pool_id.is_set or self.pool_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool_id.get_name_leafdata())
                            if (self.pool_name.is_set or self.pool_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool_name.get_name_leafdata())
                            if (self.pool_prefix_length.is_set or self.pool_prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool_prefix_length.get_name_leafdata())
                            if (self.pool_scope.is_set or self.pool_scope.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool_scope.get_name_leafdata())
                            if (self.utilization_high_count.is_set or self.utilization_high_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.utilization_high_count.get_name_leafdata())
                            if (self.utilization_low_count.is_set or self.utilization_low_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.utilization_low_count.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "current-utilization" or name == "high-utilization-mark" or name == "low-utilization-mark" or name == "pool-id" or name == "pool-name" or name == "pool-prefix-length" or name == "pool-scope" or name == "utilization-high-count" or name == "utilization-low-count" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "current-utilization"):
                                self.current_utilization = value
                                self.current_utilization.value_namespace = name_space
                                self.current_utilization.value_namespace_prefix = name_space_prefix
                            if(value_path == "high-utilization-mark"):
                                self.high_utilization_mark = value
                                self.high_utilization_mark.value_namespace = name_space
                                self.high_utilization_mark.value_namespace_prefix = name_space_prefix
                            if(value_path == "low-utilization-mark"):
                                self.low_utilization_mark = value
                                self.low_utilization_mark.value_namespace = name_space
                                self.low_utilization_mark.value_namespace_prefix = name_space_prefix
                            if(value_path == "pool-id"):
                                self.pool_id = value
                                self.pool_id.value_namespace = name_space
                                self.pool_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "pool-name"):
                                self.pool_name = value
                                self.pool_name.value_namespace = name_space
                                self.pool_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "pool-prefix-length"):
                                self.pool_prefix_length = value
                                self.pool_prefix_length.value_namespace = name_space
                                self.pool_prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "pool-scope"):
                                self.pool_scope = value
                                self.pool_scope.value_namespace = name_space
                                self.pool_scope.value_namespace_prefix = name_space_prefix
                            if(value_path == "utilization-high-count"):
                                self.utilization_high_count = value
                                self.utilization_high_count.value_namespace = name_space
                                self.utilization_high_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "utilization-low-count"):
                                self.utilization_low_count = value
                                self.utilization_low_count.value_namespace = name_space
                                self.utilization_low_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.pool_name.is_set or
                            (self.address_ranges is not None and self.address_ranges.has_data()) or
                            (self.allocated_addresses is not None and self.allocated_addresses.has_data()) or
                            (self.configuration is not None and self.configuration.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pool_name.yfilter != YFilter.not_set or
                            (self.address_ranges is not None and self.address_ranges.has_operation()) or
                            (self.allocated_addresses is not None and self.allocated_addresses.has_operation()) or
                            (self.configuration is not None and self.configuration.has_operation()))

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
                                self.address_ranges = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges()
                                self.address_ranges.parent = self
                                self._children_name_map["address_ranges"] = "address-ranges"
                            return self.address_ranges

                        if (child_yang_name == "allocated-addresses"):
                            if (self.allocated_addresses is None):
                                self.allocated_addresses = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses()
                                self.allocated_addresses.parent = self
                                self._children_name_map["allocated_addresses"] = "allocated-addresses"
                            return self.allocated_addresses

                        if (child_yang_name == "configuration"):
                            if (self.configuration is None):
                                self.configuration = AddressPoolService.Nodes.Node.Pools.Pool.Configuration()
                                self.configuration.parent = self
                                self._children_name_map["configuration"] = "configuration"
                            return self.configuration

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address-ranges" or name == "allocated-addresses" or name == "configuration" or name == "pool-name"):
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
                        c = AddressPoolService.Nodes.Node.Pools.Pool()
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


            class TotalUtilization(Entity):
                """
                Show total utilization for pool
                
                .. attribute:: current_total_utilization
                
                	Current utilization
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: total_utilization_high_mark
                
                	High utilization mark
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: total_utilization_low_mark
                
                	Low utilization mark
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Nodes.Node.TotalUtilization, self).__init__()

                    self.yang_name = "total-utilization"
                    self.yang_parent_name = "node"

                    self.current_total_utilization = YLeaf(YType.uint8, "current-total-utilization")

                    self.total_utilization_high_mark = YLeaf(YType.uint8, "total-utilization-high-mark")

                    self.total_utilization_low_mark = YLeaf(YType.uint8, "total-utilization-low-mark")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("current_total_utilization",
                                    "total_utilization_high_mark",
                                    "total_utilization_low_mark") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AddressPoolService.Nodes.Node.TotalUtilization, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AddressPoolService.Nodes.Node.TotalUtilization, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.current_total_utilization.is_set or
                        self.total_utilization_high_mark.is_set or
                        self.total_utilization_low_mark.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.current_total_utilization.yfilter != YFilter.not_set or
                        self.total_utilization_high_mark.yfilter != YFilter.not_set or
                        self.total_utilization_low_mark.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "total-utilization" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.current_total_utilization.is_set or self.current_total_utilization.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_total_utilization.get_name_leafdata())
                    if (self.total_utilization_high_mark.is_set or self.total_utilization_high_mark.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_utilization_high_mark.get_name_leafdata())
                    if (self.total_utilization_low_mark.is_set or self.total_utilization_low_mark.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_utilization_low_mark.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "current-total-utilization" or name == "total-utilization-high-mark" or name == "total-utilization-low-mark"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "current-total-utilization"):
                        self.current_total_utilization = value
                        self.current_total_utilization.value_namespace = name_space
                        self.current_total_utilization.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-utilization-high-mark"):
                        self.total_utilization_high_mark = value
                        self.total_utilization_high_mark.value_namespace = name_space
                        self.total_utilization_high_mark.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-utilization-low-mark"):
                        self.total_utilization_low_mark = value
                        self.total_utilization_low_mark.value_namespace = name_space
                        self.total_utilization_low_mark.value_namespace_prefix = name_space_prefix


            class Vrfs(Entity):
                """
                Pool VRF data
                
                .. attribute:: vrf
                
                	VRF level Pool information
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Nodes.Node.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "node"

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
                                super(AddressPoolService.Nodes.Node.Vrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AddressPoolService.Nodes.Node.Vrfs, self).__setattr__(name, value)


                class Vrf(Entity):
                    """
                    VRF level Pool information
                    
                    .. attribute:: vrf_name  <key>
                    
                    	The VRF name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ipv4
                    
                    	IPv4 pool VRF data
                    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	IPv6 Pool VRF data
                    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6>`
                    
                    

                    """

                    _prefix = 'ip-daps-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.ipv4 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                        self._children_yang_names.add("ipv4")

                        self.ipv6 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6()
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
                                    super(AddressPoolService.Nodes.Node.Vrfs.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf, self).__setattr__(name, value)


                    class Ipv4(Entity):
                        """
                        IPv4 pool VRF data
                        
                        .. attribute:: allocation_summary
                        
                        	Allocation summary
                        	**type**\:   :py:class:`AllocationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary>`
                        
                        .. attribute:: pools
                        
                        	Pools data
                        	**type**\: list of    :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "vrf"

                            self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary()
                            self.allocation_summary.parent = self
                            self._children_name_map["allocation_summary"] = "allocation-summary"
                            self._children_yang_names.add("allocation-summary")

                            self.pools = YList(self)

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
                                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4, self).__setattr__(name, value)


                        class AllocationSummary(Entity):
                            """
                            Allocation summary
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: high_utilization_threshold
                            
                            	High utilization threshold in percentage
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: low_utilization_threshold
                            
                            	Low utilization threshold in percentage
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: utilization
                            
                            	Current utilization in percentage
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary, self).__init__()

                                self.yang_name = "allocation-summary"
                                self.yang_parent_name = "ipv4"

                                self.excluded = YLeaf(YType.uint32, "excluded")

                                self.free = YLeaf(YType.uint32, "free")

                                self.high_utilization_threshold = YLeaf(YType.uint8, "high-utilization-threshold")

                                self.low_utilization_threshold = YLeaf(YType.uint8, "low-utilization-threshold")

                                self.total = YLeaf(YType.uint32, "total")

                                self.used = YLeaf(YType.uint32, "used")

                                self.utilization = YLeaf(YType.uint8, "utilization")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("excluded",
                                                "free",
                                                "high_utilization_threshold",
                                                "low_utilization_threshold",
                                                "total",
                                                "used",
                                                "utilization") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.excluded.is_set or
                                    self.free.is_set or
                                    self.high_utilization_threshold.is_set or
                                    self.low_utilization_threshold.is_set or
                                    self.total.is_set or
                                    self.used.is_set or
                                    self.utilization.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.excluded.yfilter != YFilter.not_set or
                                    self.free.yfilter != YFilter.not_set or
                                    self.high_utilization_threshold.yfilter != YFilter.not_set or
                                    self.low_utilization_threshold.yfilter != YFilter.not_set or
                                    self.total.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set or
                                    self.utilization.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "allocation-summary" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.excluded.is_set or self.excluded.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded.get_name_leafdata())
                                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free.get_name_leafdata())
                                if (self.high_utilization_threshold.is_set or self.high_utilization_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.high_utilization_threshold.get_name_leafdata())
                                if (self.low_utilization_threshold.is_set or self.low_utilization_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.low_utilization_threshold.get_name_leafdata())
                                if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())
                                if (self.utilization.is_set or self.utilization.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.utilization.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "excluded" or name == "free" or name == "high-utilization-threshold" or name == "low-utilization-threshold" or name == "total" or name == "used" or name == "utilization"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "excluded"):
                                    self.excluded = value
                                    self.excluded.value_namespace = name_space
                                    self.excluded.value_namespace_prefix = name_space_prefix
                                if(value_path == "free"):
                                    self.free = value
                                    self.free.value_namespace = name_space
                                    self.free.value_namespace_prefix = name_space_prefix
                                if(value_path == "high-utilization-threshold"):
                                    self.high_utilization_threshold = value
                                    self.high_utilization_threshold.value_namespace = name_space
                                    self.high_utilization_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "low-utilization-threshold"):
                                    self.low_utilization_threshold = value
                                    self.low_utilization_threshold.value_namespace = name_space
                                    self.low_utilization_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "total"):
                                    self.total = value
                                    self.total.value_namespace = name_space
                                    self.total.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix
                                if(value_path == "utilization"):
                                    self.utilization = value
                                    self.utilization.value_namespace = name_space
                                    self.utilization.value_namespace_prefix = name_space_prefix


                        class Pools(Entity):
                            """
                            Pools data
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pool_name
                            
                            	Pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools, self).__init__()

                                self.yang_name = "pools"
                                self.yang_parent_name = "ipv4"

                                self.excluded = YLeaf(YType.uint32, "excluded")

                                self.free = YLeaf(YType.uint32, "free")

                                self.pool_name = YLeaf(YType.str, "pool-name")

                                self.total = YLeaf(YType.uint32, "total")

                                self.used = YLeaf(YType.uint32, "used")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("excluded",
                                                "free",
                                                "pool_name",
                                                "total",
                                                "used",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.excluded.is_set or
                                    self.free.is_set or
                                    self.pool_name.is_set or
                                    self.total.is_set or
                                    self.used.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.excluded.yfilter != YFilter.not_set or
                                    self.free.yfilter != YFilter.not_set or
                                    self.pool_name.yfilter != YFilter.not_set or
                                    self.total.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

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
                                if (self.excluded.is_set or self.excluded.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded.get_name_leafdata())
                                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free.get_name_leafdata())
                                if (self.pool_name.is_set or self.pool_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pool_name.get_name_leafdata())
                                if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "excluded" or name == "free" or name == "pool-name" or name == "total" or name == "used" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "excluded"):
                                    self.excluded = value
                                    self.excluded.value_namespace = name_space
                                    self.excluded.value_namespace_prefix = name_space_prefix
                                if(value_path == "free"):
                                    self.free = value
                                    self.free.value_namespace = name_space
                                    self.free.value_namespace_prefix = name_space_prefix
                                if(value_path == "pool-name"):
                                    self.pool_name = value
                                    self.pool_name.value_namespace = name_space
                                    self.pool_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "total"):
                                    self.total = value
                                    self.total.value_namespace = name_space
                                    self.total.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.pools:
                                if (c.has_data()):
                                    return True
                            return (self.allocation_summary is not None and self.allocation_summary.has_data())

                        def has_operation(self):
                            for c in self.pools:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.allocation_summary is not None and self.allocation_summary.has_operation()))

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

                            if (child_yang_name == "allocation-summary"):
                                if (self.allocation_summary is None):
                                    self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary()
                                    self.allocation_summary.parent = self
                                    self._children_name_map["allocation_summary"] = "allocation-summary"
                                return self.allocation_summary

                            if (child_yang_name == "pools"):
                                for c in self.pools:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.pools.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allocation-summary" or name == "pools"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Ipv6(Entity):
                        """
                        IPv6 Pool VRF data
                        
                        .. attribute:: allocation_summary
                        
                        	Allocation summary
                        	**type**\:   :py:class:`AllocationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary>`
                        
                        .. attribute:: pools
                        
                        	Pools data
                        	**type**\: list of    :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "vrf"

                            self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary()
                            self.allocation_summary.parent = self
                            self._children_name_map["allocation_summary"] = "allocation-summary"
                            self._children_yang_names.add("allocation-summary")

                            self.pools = YList(self)

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
                                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6, self).__setattr__(name, value)


                        class AllocationSummary(Entity):
                            """
                            Allocation summary
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: high_utilization_threshold
                            
                            	High utilization threshold in percentage
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: low_utilization_threshold
                            
                            	Low utilization threshold in percentage
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: utilization
                            
                            	Current utilization in percentage
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary, self).__init__()

                                self.yang_name = "allocation-summary"
                                self.yang_parent_name = "ipv6"

                                self.excluded = YLeaf(YType.uint32, "excluded")

                                self.free = YLeaf(YType.uint32, "free")

                                self.high_utilization_threshold = YLeaf(YType.uint8, "high-utilization-threshold")

                                self.low_utilization_threshold = YLeaf(YType.uint8, "low-utilization-threshold")

                                self.total = YLeaf(YType.uint32, "total")

                                self.used = YLeaf(YType.uint32, "used")

                                self.utilization = YLeaf(YType.uint8, "utilization")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("excluded",
                                                "free",
                                                "high_utilization_threshold",
                                                "low_utilization_threshold",
                                                "total",
                                                "used",
                                                "utilization") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.excluded.is_set or
                                    self.free.is_set or
                                    self.high_utilization_threshold.is_set or
                                    self.low_utilization_threshold.is_set or
                                    self.total.is_set or
                                    self.used.is_set or
                                    self.utilization.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.excluded.yfilter != YFilter.not_set or
                                    self.free.yfilter != YFilter.not_set or
                                    self.high_utilization_threshold.yfilter != YFilter.not_set or
                                    self.low_utilization_threshold.yfilter != YFilter.not_set or
                                    self.total.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set or
                                    self.utilization.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "allocation-summary" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.excluded.is_set or self.excluded.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded.get_name_leafdata())
                                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free.get_name_leafdata())
                                if (self.high_utilization_threshold.is_set or self.high_utilization_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.high_utilization_threshold.get_name_leafdata())
                                if (self.low_utilization_threshold.is_set or self.low_utilization_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.low_utilization_threshold.get_name_leafdata())
                                if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())
                                if (self.utilization.is_set or self.utilization.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.utilization.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "excluded" or name == "free" or name == "high-utilization-threshold" or name == "low-utilization-threshold" or name == "total" or name == "used" or name == "utilization"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "excluded"):
                                    self.excluded = value
                                    self.excluded.value_namespace = name_space
                                    self.excluded.value_namespace_prefix = name_space_prefix
                                if(value_path == "free"):
                                    self.free = value
                                    self.free.value_namespace = name_space
                                    self.free.value_namespace_prefix = name_space_prefix
                                if(value_path == "high-utilization-threshold"):
                                    self.high_utilization_threshold = value
                                    self.high_utilization_threshold.value_namespace = name_space
                                    self.high_utilization_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "low-utilization-threshold"):
                                    self.low_utilization_threshold = value
                                    self.low_utilization_threshold.value_namespace = name_space
                                    self.low_utilization_threshold.value_namespace_prefix = name_space_prefix
                                if(value_path == "total"):
                                    self.total = value
                                    self.total.value_namespace = name_space
                                    self.total.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix
                                if(value_path == "utilization"):
                                    self.utilization = value
                                    self.utilization.value_namespace = name_space
                                    self.utilization.value_namespace_prefix = name_space_prefix


                        class Pools(Entity):
                            """
                            Pools data
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pool_name
                            
                            	Pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools, self).__init__()

                                self.yang_name = "pools"
                                self.yang_parent_name = "ipv6"

                                self.excluded = YLeaf(YType.uint32, "excluded")

                                self.free = YLeaf(YType.uint32, "free")

                                self.pool_name = YLeaf(YType.str, "pool-name")

                                self.total = YLeaf(YType.uint32, "total")

                                self.used = YLeaf(YType.uint32, "used")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("excluded",
                                                "free",
                                                "pool_name",
                                                "total",
                                                "used",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.excluded.is_set or
                                    self.free.is_set or
                                    self.pool_name.is_set or
                                    self.total.is_set or
                                    self.used.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.excluded.yfilter != YFilter.not_set or
                                    self.free.yfilter != YFilter.not_set or
                                    self.pool_name.yfilter != YFilter.not_set or
                                    self.total.yfilter != YFilter.not_set or
                                    self.used.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

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
                                if (self.excluded.is_set or self.excluded.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.excluded.get_name_leafdata())
                                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.free.get_name_leafdata())
                                if (self.pool_name.is_set or self.pool_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pool_name.get_name_leafdata())
                                if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total.get_name_leafdata())
                                if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.used.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "excluded" or name == "free" or name == "pool-name" or name == "total" or name == "used" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "excluded"):
                                    self.excluded = value
                                    self.excluded.value_namespace = name_space
                                    self.excluded.value_namespace_prefix = name_space_prefix
                                if(value_path == "free"):
                                    self.free = value
                                    self.free.value_namespace = name_space
                                    self.free.value_namespace_prefix = name_space_prefix
                                if(value_path == "pool-name"):
                                    self.pool_name = value
                                    self.pool_name.value_namespace = name_space
                                    self.pool_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "total"):
                                    self.total = value
                                    self.total.value_namespace = name_space
                                    self.total.value_namespace_prefix = name_space_prefix
                                if(value_path == "used"):
                                    self.used = value
                                    self.used.value_namespace = name_space
                                    self.used.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.pools:
                                if (c.has_data()):
                                    return True
                            return (self.allocation_summary is not None and self.allocation_summary.has_data())

                        def has_operation(self):
                            for c in self.pools:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.allocation_summary is not None and self.allocation_summary.has_operation()))

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

                            if (child_yang_name == "allocation-summary"):
                                if (self.allocation_summary is None):
                                    self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary()
                                    self.allocation_summary.parent = self
                                    self._children_name_map["allocation_summary"] = "allocation-summary"
                                return self.allocation_summary

                            if (child_yang_name == "pools"):
                                for c in self.pools:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.pools.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allocation-summary" or name == "pools"):
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
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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
                                self.ipv4 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4()
                                self.ipv4.parent = self
                                self._children_name_map["ipv4"] = "ipv4"
                            return self.ipv4

                        if (child_yang_name == "ipv6"):
                            if (self.ipv6 is None):
                                self.ipv6 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6()
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

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AddressPoolService.Nodes.Node.Vrfs.Vrf()
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
                return (
                    self.node_name.is_set or
                    (self.pools is not None and self.pools.has_data()) or
                    (self.total_utilization is not None and self.total_utilization.has_data()) or
                    (self.vrfs is not None and self.vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.pools is not None and self.pools.has_operation()) or
                    (self.total_utilization is not None and self.total_utilization.has_operation()) or
                    (self.vrfs is not None and self.vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-daps-oper:address-pool-service/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "pools"):
                    if (self.pools is None):
                        self.pools = AddressPoolService.Nodes.Node.Pools()
                        self.pools.parent = self
                        self._children_name_map["pools"] = "pools"
                    return self.pools

                if (child_yang_name == "total-utilization"):
                    if (self.total_utilization is None):
                        self.total_utilization = AddressPoolService.Nodes.Node.TotalUtilization()
                        self.total_utilization.parent = self
                        self._children_name_map["total_utilization"] = "total-utilization"
                    return self.total_utilization

                if (child_yang_name == "vrfs"):
                    if (self.vrfs is None):
                        self.vrfs = AddressPoolService.Nodes.Node.Vrfs()
                        self.vrfs.parent = self
                        self._children_name_map["vrfs"] = "vrfs"
                    return self.vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pools" or name == "total-utilization" or name == "vrfs" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-daps-oper:address-pool-service/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AddressPoolService.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-daps-oper:address-pool-service" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = AddressPoolService.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AddressPoolService()
        return self._top_entity

