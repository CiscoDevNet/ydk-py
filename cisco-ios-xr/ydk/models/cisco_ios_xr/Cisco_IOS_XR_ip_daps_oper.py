""" Cisco_IOS_XR_ip_daps_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-daps package operational data.

This module contains definitions
for the following management objects\:
  address\-pool\-service\: Pool operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DapsClient(Enum):
    """
    DapsClient (Enum Class)

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


class DapsSergRole(Enum):
    """
    DapsSergRole (Enum Class)

    DAPS SERG role

    .. data:: none = 0

    	Role None

    .. data:: master = 1

    	Role Master

    .. data:: slave = 2

    	Role Slave

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class IpAddr(Enum):
    """
    IpAddr (Enum Class)

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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes>`
    
    

    """

    _prefix = 'ip-daps-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AddressPoolService, self).__init__()
        self._top_entity = None

        self.yang_name = "address-pool-service"
        self.yang_parent_name = "Cisco-IOS-XR-ip-daps-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", AddressPoolService.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = AddressPoolService.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-daps-oper:address-pool-service"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AddressPoolService, [], name, value)


    class Nodes(Entity):
        """
        Pool operational data for a particular location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node>`
        
        

        """

        _prefix = 'ip-daps-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AddressPoolService.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "address-pool-service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", AddressPoolService.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-daps-oper:address-pool-service/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AddressPoolService.Nodes, [], name, value)


        class Node(Entity):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: pools
            
            	List of IPv4/IPv6 pool data
            	**type**\:  :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools>`
            
            .. attribute:: total_utilization
            
            	Show total utilization for pool
            	**type**\:  :py:class:`TotalUtilization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.TotalUtilization>`
            
            .. attribute:: vrfs
            
            	Pool VRF data
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs>`
            
            

            """

            _prefix = 'ip-daps-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AddressPoolService.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("pools", ("pools", AddressPoolService.Nodes.Node.Pools)), ("total-utilization", ("total_utilization", AddressPoolService.Nodes.Node.TotalUtilization)), ("vrfs", ("vrfs", AddressPoolService.Nodes.Node.Vrfs))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.pools = AddressPoolService.Nodes.Node.Pools()
                self.pools.parent = self
                self._children_name_map["pools"] = "pools"

                self.total_utilization = AddressPoolService.Nodes.Node.TotalUtilization()
                self.total_utilization.parent = self
                self._children_name_map["total_utilization"] = "total-utilization"

                self.vrfs = AddressPoolService.Nodes.Node.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-daps-oper:address-pool-service/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AddressPoolService.Nodes.Node, ['node_name'], name, value)


            class Pools(Entity):
                """
                List of IPv4/IPv6 pool data
                
                .. attribute:: pool
                
                	Pool data by pool name
                	**type**\: list of  		 :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool>`
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Nodes.Node.Pools, self).__init__()

                    self.yang_name = "pools"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pool", ("pool", AddressPoolService.Nodes.Node.Pools.Pool))])
                    self._leafs = OrderedDict()

                    self.pool = YList(self)
                    self._segment_path = lambda: "pools"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools, [], name, value)


                class Pool(Entity):
                    """
                    Pool data by pool name
                    
                    .. attribute:: pool_name  (key)
                    
                    	The pool name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: address_ranges
                    
                    	Summary info for pool
                    	**type**\:  :py:class:`AddressRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges>`
                    
                    .. attribute:: allocated_addresses
                    
                    	Detailed info for the Pool
                    	**type**\:  :py:class:`AllocatedAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses>`
                    
                    .. attribute:: configuration
                    
                    	Configuration info for pool
                    	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.Configuration>`
                    
                    

                    """

                    _prefix = 'ip-daps-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AddressPoolService.Nodes.Node.Pools.Pool, self).__init__()

                        self.yang_name = "pool"
                        self.yang_parent_name = "pools"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pool_name']
                        self._child_classes = OrderedDict([("address-ranges", ("address_ranges", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges)), ("allocated-addresses", ("allocated_addresses", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses)), ("configuration", ("configuration", AddressPoolService.Nodes.Node.Pools.Pool.Configuration))])
                        self._leafs = OrderedDict([
                            ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                        ])
                        self.pool_name = None

                        self.address_ranges = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges()
                        self.address_ranges.parent = self
                        self._children_name_map["address_ranges"] = "address-ranges"

                        self.allocated_addresses = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses()
                        self.allocated_addresses.parent = self
                        self._children_name_map["allocated_addresses"] = "allocated-addresses"

                        self.configuration = AddressPoolService.Nodes.Node.Pools.Pool.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                        self._segment_path = lambda: "pool" + "[pool-name='" + str(self.pool_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool, ['pool_name'], name, value)


                    class AddressRanges(Entity):
                        """
                        Summary info for pool
                        
                        .. attribute:: address_range
                        
                        	Start Address of the Range
                        	**type**\: list of  		 :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges, self).__init__()

                            self.yang_name = "address-ranges"
                            self.yang_parent_name = "pool"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address-range", ("address_range", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange))])
                            self._leafs = OrderedDict()

                            self.address_range = YList(self)
                            self._segment_path = lambda: "address-ranges"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges, [], name, value)


                        class AddressRange(Entity):
                            """
                            Start Address of the Range
                            
                            .. attribute:: start_address  (key)
                            
                            	IP Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: start_address_xr
                            
                            	Range start
                            	**type**\:  :py:class:`StartAddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr>`
                            
                            .. attribute:: end_address
                            
                            	Range end
                            	**type**\:  :py:class:`EndAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress>`
                            
                            .. attribute:: default_router
                            
                            	Default router
                            	**type**\:  :py:class:`DefaultRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter>`
                            
                            .. attribute:: pool_name
                            
                            	Pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: pool_scope
                            
                            	Pool scope
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: allocated_addresses
                            
                            	Number of addresses allocated
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free_addresses
                            
                            	Number of addresses free
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded_addresses
                            
                            	Number of addresses excluded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_blocked_status
                            
                            	Is network blocked
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_blocked_status_trp
                            
                            	Is network blocked trap send
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "address-ranges"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['start_address']
                                self._child_classes = OrderedDict([("start-address-xr", ("start_address_xr", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr)), ("end-address", ("end_address", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress)), ("default-router", ("default_router", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter))])
                                self._leafs = OrderedDict([
                                    ('start_address', (YLeaf(YType.str, 'start-address'), ['str','str'])),
                                    ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('pool_scope', (YLeaf(YType.str, 'pool-scope'), ['str'])),
                                    ('allocated_addresses', (YLeaf(YType.uint32, 'allocated-addresses'), ['int'])),
                                    ('free_addresses', (YLeaf(YType.uint32, 'free-addresses'), ['int'])),
                                    ('excluded_addresses', (YLeaf(YType.uint32, 'excluded-addresses'), ['int'])),
                                    ('network_blocked_status', (YLeaf(YType.uint32, 'network-blocked-status'), ['int'])),
                                    ('network_blocked_status_trp', (YLeaf(YType.uint32, 'network-blocked-status-trp'), ['int'])),
                                ])
                                self.start_address = None
                                self.pool_name = None
                                self.vrf_name = None
                                self.pool_scope = None
                                self.allocated_addresses = None
                                self.free_addresses = None
                                self.excluded_addresses = None
                                self.network_blocked_status = None
                                self.network_blocked_status_trp = None

                                self.start_address_xr = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr()
                                self.start_address_xr.parent = self
                                self._children_name_map["start_address_xr"] = "start-address-xr"

                                self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress()
                                self.end_address.parent = self
                                self._children_name_map["end_address"] = "end-address"

                                self.default_router = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter()
                                self.default_router.parent = self
                                self._children_name_map["default_router"] = "default-router"
                                self._segment_path = lambda: "address-range" + "[start-address='" + str(self.start_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange, ['start_address', 'pool_name', 'vrf_name', 'pool_scope', 'allocated_addresses', 'free_addresses', 'excluded_addresses', 'network_blocked_status', 'network_blocked_status_trp'], name, value)


                            class StartAddressXr(Entity):
                                """
                                Range start
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr, self).__init__()

                                    self.yang_name = "start-address-xr"
                                    self.yang_parent_name = "address-range"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address))])
                                    self._leafs = OrderedDict()

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "start-address-xr"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr, [], name, value)


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:  :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "start-address-xr"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddr', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address, ['address_family', 'ipv4_address', 'ipv6_address'], name, value)


                            class EndAddress(Entity):
                                """
                                Range end
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress, self).__init__()

                                    self.yang_name = "end-address"
                                    self.yang_parent_name = "address-range"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address))])
                                    self._leafs = OrderedDict()

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "end-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress, [], name, value)


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:  :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "end-address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddr', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address, ['address_family', 'ipv4_address', 'ipv6_address'], name, value)


                            class DefaultRouter(Entity):
                                """
                                Default router
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter, self).__init__()

                                    self.yang_name = "default-router"
                                    self.yang_parent_name = "address-range"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address))])
                                    self._leafs = OrderedDict()

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "default-router"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter, [], name, value)


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:  :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "default-router"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddr', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address, ['address_family', 'ipv4_address', 'ipv6_address'], name, value)


                    class AllocatedAddresses(Entity):
                        """
                        Detailed info for the Pool
                        
                        .. attribute:: pool_allocations
                        
                        	Pool allocations
                        	**type**\:  :py:class:`PoolAllocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations>`
                        
                        .. attribute:: address_range
                        
                        	Address ranges
                        	**type**\: list of  		 :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange>`
                        
                        .. attribute:: in_use_address
                        
                        	In\-use addresses
                        	**type**\: list of  		 :py:class:`InUseAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses, self).__init__()

                            self.yang_name = "allocated-addresses"
                            self.yang_parent_name = "pool"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("pool-allocations", ("pool_allocations", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations)), ("address-range", ("address_range", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange)), ("in-use-address", ("in_use_address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress))])
                            self._leafs = OrderedDict()

                            self.pool_allocations = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations()
                            self.pool_allocations.parent = self
                            self._children_name_map["pool_allocations"] = "pool-allocations"

                            self.address_range = YList(self)
                            self.in_use_address = YList(self)
                            self._segment_path = lambda: "allocated-addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses, [], name, value)


                        class PoolAllocations(Entity):
                            """
                            Pool allocations
                            
                            .. attribute:: high_threshold
                            
                            	High threshold data
                            	**type**\:  :py:class:`HighThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold>`
                            
                            .. attribute:: low_threshold
                            
                            	Low threshold data
                            	**type**\:  :py:class:`LowThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold>`
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: utilization
                            
                            	Current utilization in percentage
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations, self).__init__()

                                self.yang_name = "pool-allocations"
                                self.yang_parent_name = "allocated-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("high-threshold", ("high_threshold", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold)), ("low-threshold", ("low_threshold", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold))])
                                self._leafs = OrderedDict([
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                    ('excluded', (YLeaf(YType.uint32, 'excluded'), ['int'])),
                                    ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                    ('utilization', (YLeaf(YType.uint32, 'utilization'), ['int'])),
                                ])
                                self.vrf_name = None
                                self.used = None
                                self.excluded = None
                                self.free = None
                                self.total = None
                                self.utilization = None

                                self.high_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold()
                                self.high_threshold.parent = self
                                self._children_name_map["high_threshold"] = "high-threshold"

                                self.low_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold()
                                self.low_threshold.parent = self
                                self._children_name_map["low_threshold"] = "low-threshold"
                                self._segment_path = lambda: "pool-allocations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations, ['vrf_name', 'used', 'excluded', 'free', 'total', 'utilization'], name, value)


                            class HighThreshold(Entity):
                                """
                                High threshold data
                                
                                .. attribute:: threshold
                                
                                	Threshold in percentage
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: triggers
                                
                                	Number of Triggers
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_last_crossed
                                
                                	Last time at which threshold crossed in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold, self).__init__()

                                    self.yang_name = "high-threshold"
                                    self.yang_parent_name = "pool-allocations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                        ('triggers', (YLeaf(YType.uint32, 'triggers'), ['int'])),
                                        ('time_last_crossed', (YLeaf(YType.str, 'time-last-crossed'), ['str'])),
                                    ])
                                    self.threshold = None
                                    self.triggers = None
                                    self.time_last_crossed = None
                                    self._segment_path = lambda: "high-threshold"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold, ['threshold', 'triggers', 'time_last_crossed'], name, value)


                            class LowThreshold(Entity):
                                """
                                Low threshold data
                                
                                .. attribute:: threshold
                                
                                	Threshold in percentage
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: percentage
                                
                                .. attribute:: triggers
                                
                                	Number of Triggers
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_last_crossed
                                
                                	Last time at which threshold crossed in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold, self).__init__()

                                    self.yang_name = "low-threshold"
                                    self.yang_parent_name = "pool-allocations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                        ('triggers', (YLeaf(YType.uint32, 'triggers'), ['int'])),
                                        ('time_last_crossed', (YLeaf(YType.str, 'time-last-crossed'), ['str'])),
                                    ])
                                    self.threshold = None
                                    self.triggers = None
                                    self.time_last_crossed = None
                                    self._segment_path = lambda: "low-threshold"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold, ['threshold', 'triggers', 'time_last_crossed'], name, value)


                        class AddressRange(Entity):
                            """
                            Address ranges
                            
                            .. attribute:: start_address
                            
                            	Range start
                            	**type**\:  :py:class:`StartAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress>`
                            
                            .. attribute:: end_address
                            
                            	Range end
                            	**type**\:  :py:class:`EndAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress>`
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange, self).__init__()

                                self.yang_name = "address-range"
                                self.yang_parent_name = "allocated-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("start-address", ("start_address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress)), ("end-address", ("end_address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress))])
                                self._leafs = OrderedDict([
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                    ('excluded', (YLeaf(YType.uint32, 'excluded'), ['int'])),
                                    ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                ])
                                self.used = None
                                self.excluded = None
                                self.free = None

                                self.start_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress()
                                self.start_address.parent = self
                                self._children_name_map["start_address"] = "start-address"

                                self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress()
                                self.end_address.parent = self
                                self._children_name_map["end_address"] = "end-address"
                                self._segment_path = lambda: "address-range"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange, ['used', 'excluded', 'free'], name, value)


                            class StartAddress(Entity):
                                """
                                Range start
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress, self).__init__()

                                    self.yang_name = "start-address"
                                    self.yang_parent_name = "address-range"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address))])
                                    self._leafs = OrderedDict()

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "start-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress, [], name, value)


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:  :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "start-address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddr', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address, ['address_family', 'ipv4_address', 'ipv6_address'], name, value)


                            class EndAddress(Entity):
                                """
                                Range end
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress, self).__init__()

                                    self.yang_name = "end-address"
                                    self.yang_parent_name = "address-range"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address))])
                                    self._leafs = OrderedDict()

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "end-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress, [], name, value)


                                class Address(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:  :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "end-address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddr', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address, ['address_family', 'ipv4_address', 'ipv6_address'], name, value)


                        class InUseAddress(Entity):
                            """
                            In\-use addresses
                            
                            .. attribute:: address
                            
                            	Client address
                            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address>`
                            
                            .. attribute:: client_type
                            
                            	Client type
                            	**type**\:  :py:class:`DapsClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.DapsClient>`
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress, self).__init__()

                                self.yang_name = "in-use-address"
                                self.yang_parent_name = "allocated-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address))])
                                self._leafs = OrderedDict([
                                    ('client_type', (YLeaf(YType.enumeration, 'client-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'DapsClient', '')])),
                                ])
                                self.client_type = None

                                self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._segment_path = lambda: "in-use-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress, ['client_type'], name, value)


                            class Address(Entity):
                                """
                                Client address
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:  :py:class:`Address_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "in-use-address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_))])
                                    self._leafs = OrderedDict()

                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address, [], name, value)


                                class Address_(Entity):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:  :py:class:`IpAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddr>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-daps-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "address"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddr', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_, ['address_family', 'ipv4_address', 'ipv6_address'], name, value)


                    class Configuration(Entity):
                        """
                        Configuration info for pool
                        
                        .. attribute:: serg_info
                        
                        	SERG Info
                        	**type**\:  :py:class:`SergInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.Configuration.SergInfo>`
                        
                        .. attribute:: pool_name
                        
                        	Pool name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: pool_id
                        
                        	Pool ID for MIBS
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: pool_scope
                        
                        	Pool Scope
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: pool_prefix_length
                        
                        	Prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: high_utilization_mark
                        
                        	High utilization mark
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: low_utilization_mark
                        
                        	Low utilization mark
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: current_utilization
                        
                        	Current utilization
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: utilization_high_count
                        
                        	Number of times High utilization threshold was crossed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: utilization_low_count
                        
                        	Number of times Low utilization threshold was crossed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Pools.Pool.Configuration, self).__init__()

                            self.yang_name = "configuration"
                            self.yang_parent_name = "pool"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("serg-info", ("serg_info", AddressPoolService.Nodes.Node.Pools.Pool.Configuration.SergInfo))])
                            self._leafs = OrderedDict([
                                ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                                ('pool_id', (YLeaf(YType.uint32, 'pool-id'), ['int'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('pool_scope', (YLeaf(YType.str, 'pool-scope'), ['str'])),
                                ('pool_prefix_length', (YLeaf(YType.uint32, 'pool-prefix-length'), ['int'])),
                                ('high_utilization_mark', (YLeaf(YType.uint8, 'high-utilization-mark'), ['int'])),
                                ('low_utilization_mark', (YLeaf(YType.uint8, 'low-utilization-mark'), ['int'])),
                                ('current_utilization', (YLeaf(YType.uint8, 'current-utilization'), ['int'])),
                                ('utilization_high_count', (YLeaf(YType.uint32, 'utilization-high-count'), ['int'])),
                                ('utilization_low_count', (YLeaf(YType.uint32, 'utilization-low-count'), ['int'])),
                            ])
                            self.pool_name = None
                            self.pool_id = None
                            self.vrf_name = None
                            self.pool_scope = None
                            self.pool_prefix_length = None
                            self.high_utilization_mark = None
                            self.low_utilization_mark = None
                            self.current_utilization = None
                            self.utilization_high_count = None
                            self.utilization_low_count = None

                            self.serg_info = AddressPoolService.Nodes.Node.Pools.Pool.Configuration.SergInfo()
                            self.serg_info.parent = self
                            self._children_name_map["serg_info"] = "serg-info"
                            self._segment_path = lambda: "configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.Configuration, ['pool_name', 'pool_id', 'vrf_name', 'pool_scope', 'pool_prefix_length', 'high_utilization_mark', 'low_utilization_mark', 'current_utilization', 'utilization_high_count', 'utilization_low_count'], name, value)


                        class SergInfo(Entity):
                            """
                            SERG Info
                            
                            .. attribute:: preferred_role
                            
                            	SERG PreferredRole
                            	**type**\:  :py:class:`DapsSergRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.DapsSergRole>`
                            
                            .. attribute:: peer_down
                            
                            	Peer Down
                            	**type**\: bool
                            
                            .. attribute:: verify_pend
                            
                            	Verify Pending
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Pools.Pool.Configuration.SergInfo, self).__init__()

                                self.yang_name = "serg-info"
                                self.yang_parent_name = "configuration"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('preferred_role', (YLeaf(YType.enumeration, 'preferred-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'DapsSergRole', '')])),
                                    ('peer_down', (YLeaf(YType.boolean, 'peer-down'), ['bool'])),
                                    ('verify_pend', (YLeaf(YType.boolean, 'verify-pend'), ['bool'])),
                                ])
                                self.preferred_role = None
                                self.peer_down = None
                                self.verify_pend = None
                                self._segment_path = lambda: "serg-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Pools.Pool.Configuration.SergInfo, ['preferred_role', 'peer_down', 'verify_pend'], name, value)


            class TotalUtilization(Entity):
                """
                Show total utilization for pool
                
                .. attribute:: total_utilization_high_mark
                
                	High utilization mark
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: total_utilization_low_mark
                
                	Low utilization mark
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: current_total_utilization
                
                	Current utilization
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Nodes.Node.TotalUtilization, self).__init__()

                    self.yang_name = "total-utilization"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_utilization_high_mark', (YLeaf(YType.uint8, 'total-utilization-high-mark'), ['int'])),
                        ('total_utilization_low_mark', (YLeaf(YType.uint8, 'total-utilization-low-mark'), ['int'])),
                        ('current_total_utilization', (YLeaf(YType.uint8, 'current-total-utilization'), ['int'])),
                    ])
                    self.total_utilization_high_mark = None
                    self.total_utilization_low_mark = None
                    self.current_total_utilization = None
                    self._segment_path = lambda: "total-utilization"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AddressPoolService.Nodes.Node.TotalUtilization, ['total_utilization_high_mark', 'total_utilization_low_mark', 'current_total_utilization'], name, value)


            class Vrfs(Entity):
                """
                Pool VRF data
                
                .. attribute:: vrf
                
                	VRF level Pool information
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AddressPoolService.Nodes.Node.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", AddressPoolService.Nodes.Node.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs, [], name, value)


                class Vrf(Entity):
                    """
                    VRF level Pool information
                    
                    .. attribute:: vrf_name  (key)
                    
                    	The VRF name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ipv4
                    
                    	IPv4 pool VRF data
                    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	IPv6 Pool VRF data
                    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6>`
                    
                    

                    """

                    _prefix = 'ip-daps-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AddressPoolService.Nodes.Node.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([("ipv4", ("ipv4", AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4)), ("ipv6", ("ipv6", AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6))])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ])
                        self.vrf_name = None

                        self.ipv4 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"

                        self.ipv6 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf, ['vrf_name'], name, value)


                    class Ipv4(Entity):
                        """
                        IPv4 pool VRF data
                        
                        .. attribute:: allocation_summary
                        
                        	Allocation summary
                        	**type**\:  :py:class:`AllocationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary>`
                        
                        .. attribute:: pools
                        
                        	Pools data
                        	**type**\: list of  		 :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("allocation-summary", ("allocation_summary", AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary)), ("pools", ("pools", AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools))])
                            self._leafs = OrderedDict()

                            self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary()
                            self.allocation_summary.parent = self
                            self._children_name_map["allocation_summary"] = "allocation-summary"

                            self.pools = YList(self)
                            self._segment_path = lambda: "ipv4"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4, [], name, value)


                        class AllocationSummary(Entity):
                            """
                            Allocation summary
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: high_utilization_threshold
                            
                            	High utilization threshold in percentage
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: low_utilization_threshold
                            
                            	Low utilization threshold in percentage
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: utilization
                            
                            	Current utilization in percentage
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary, self).__init__()

                                self.yang_name = "allocation-summary"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                    ('excluded', (YLeaf(YType.uint32, 'excluded'), ['int'])),
                                    ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                    ('high_utilization_threshold', (YLeaf(YType.uint8, 'high-utilization-threshold'), ['int'])),
                                    ('low_utilization_threshold', (YLeaf(YType.uint8, 'low-utilization-threshold'), ['int'])),
                                    ('utilization', (YLeaf(YType.uint8, 'utilization'), ['int'])),
                                ])
                                self.used = None
                                self.excluded = None
                                self.free = None
                                self.total = None
                                self.high_utilization_threshold = None
                                self.low_utilization_threshold = None
                                self.utilization = None
                                self._segment_path = lambda: "allocation-summary"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary, ['used', 'excluded', 'free', 'total', 'high_utilization_threshold', 'low_utilization_threshold', 'utilization'], name, value)


                        class Pools(Entity):
                            """
                            Pools data
                            
                            .. attribute:: pool_name
                            
                            	Pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools, self).__init__()

                                self.yang_name = "pools"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                    ('excluded', (YLeaf(YType.uint32, 'excluded'), ['int'])),
                                    ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                ])
                                self.pool_name = None
                                self.vrf_name = None
                                self.used = None
                                self.excluded = None
                                self.free = None
                                self.total = None
                                self._segment_path = lambda: "pools"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools, ['pool_name', 'vrf_name', 'used', 'excluded', 'free', 'total'], name, value)


                    class Ipv6(Entity):
                        """
                        IPv6 Pool VRF data
                        
                        .. attribute:: allocation_summary
                        
                        	Allocation summary
                        	**type**\:  :py:class:`AllocationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary>`
                        
                        .. attribute:: pools
                        
                        	Pools data
                        	**type**\: list of  		 :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("allocation-summary", ("allocation_summary", AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary)), ("pools", ("pools", AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools))])
                            self._leafs = OrderedDict()

                            self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary()
                            self.allocation_summary.parent = self
                            self._children_name_map["allocation_summary"] = "allocation-summary"

                            self.pools = YList(self)
                            self._segment_path = lambda: "ipv6"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6, [], name, value)


                        class AllocationSummary(Entity):
                            """
                            Allocation summary
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: high_utilization_threshold
                            
                            	High utilization threshold in percentage
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: low_utilization_threshold
                            
                            	Low utilization threshold in percentage
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            .. attribute:: utilization
                            
                            	Current utilization in percentage
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary, self).__init__()

                                self.yang_name = "allocation-summary"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                    ('excluded', (YLeaf(YType.uint32, 'excluded'), ['int'])),
                                    ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                    ('high_utilization_threshold', (YLeaf(YType.uint8, 'high-utilization-threshold'), ['int'])),
                                    ('low_utilization_threshold', (YLeaf(YType.uint8, 'low-utilization-threshold'), ['int'])),
                                    ('utilization', (YLeaf(YType.uint8, 'utilization'), ['int'])),
                                ])
                                self.used = None
                                self.excluded = None
                                self.free = None
                                self.total = None
                                self.high_utilization_threshold = None
                                self.low_utilization_threshold = None
                                self.utilization = None
                                self._segment_path = lambda: "allocation-summary"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary, ['used', 'excluded', 'free', 'total', 'high_utilization_threshold', 'low_utilization_threshold', 'utilization'], name, value)


                        class Pools(Entity):
                            """
                            Pools data
                            
                            .. attribute:: pool_name
                            
                            	Pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: used
                            
                            	Used allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excluded
                            
                            	Excluded allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: free
                            
                            	Free allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: total
                            
                            	Total allocations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools, self).__init__()

                                self.yang_name = "pools"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                    ('excluded', (YLeaf(YType.uint32, 'excluded'), ['int'])),
                                    ('free', (YLeaf(YType.uint32, 'free'), ['int'])),
                                    ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                                ])
                                self.pool_name = None
                                self.vrf_name = None
                                self.used = None
                                self.excluded = None
                                self.free = None
                                self.total = None
                                self._segment_path = lambda: "pools"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools, ['pool_name', 'vrf_name', 'used', 'excluded', 'free', 'total'], name, value)

    def clone_ptr(self):
        self._top_entity = AddressPoolService()
        return self._top_entity

