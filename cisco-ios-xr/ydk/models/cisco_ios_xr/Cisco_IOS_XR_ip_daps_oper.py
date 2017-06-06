""" Cisco_IOS_XR_ip_daps_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-daps package operational data.

This module contains definitions
for the following management objects\:
  address\-pool\-service\: Pool operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DapsClientEnum(Enum):
    """
    DapsClientEnum

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

    none = 0

    ppp = 1

    dhcp = 2

    dhcpv6 = 4

    ipv6nd = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
        return meta._meta_table['DapsClientEnum']


class IpAddrEnum(Enum):
    """
    IpAddrEnum

    Address type

    .. data:: ipv4 = 2

    	IPv4 address

    .. data:: ipv6 = 10

    	IPv6 address

    """

    ipv4 = 2

    ipv6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
        return meta._meta_table['IpAddrEnum']



class AddressPoolService(object):
    """
    Pool operational data
    
    .. attribute:: nodes
    
    	Pool operational data for a particular location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes>`
    
    

    """

    _prefix = 'ip-daps-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = AddressPoolService.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Pool operational data for a particular location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node>`
        
        

        """

        _prefix = 'ip-daps-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.pools = AddressPoolService.Nodes.Node.Pools()
                self.pools.parent = self
                self.total_utilization = AddressPoolService.Nodes.Node.TotalUtilization()
                self.total_utilization.parent = self
                self.vrfs = AddressPoolService.Nodes.Node.Vrfs()
                self.vrfs.parent = self


            class Pools(object):
                """
                List of IPv4/IPv6 pool data
                
                .. attribute:: pool
                
                	Pool data by pool name
                	**type**\: list of    :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool>`
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.pool = YList()
                    self.pool.parent = self
                    self.pool.name = 'pool'


                class Pool(object):
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
                        self.parent = None
                        self.pool_name = None
                        self.address_ranges = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges()
                        self.address_ranges.parent = self
                        self.allocated_addresses = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses()
                        self.allocated_addresses.parent = self
                        self.configuration = AddressPoolService.Nodes.Node.Pools.Pool.Configuration()
                        self.configuration.parent = self


                    class AddressRanges(object):
                        """
                        Summary info for pool
                        
                        .. attribute:: address_range
                        
                        	Start Address of the Range
                        	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange>`
                        
                        

                        """

                        _prefix = 'ip-daps-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_range = YList()
                            self.address_range.parent = self
                            self.address_range.name = 'address_range'


                        class AddressRange(object):
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
                                self.parent = None
                                self.start_address = None
                                self.allocated_addresses = None
                                self.default_router = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter()
                                self.default_router.parent = self
                                self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress()
                                self.end_address.parent = self
                                self.excluded_addresses = None
                                self.free_addresses = None
                                self.network_blocked_status = None
                                self.network_blocked_status_trp = None
                                self.pool_name = None
                                self.pool_scope = None
                                self.start_address_xr = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr()
                                self.start_address_xr.parent = self
                                self.vrf_name = None


                            class StartAddressXr(object):
                                """
                                Range start
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address()
                                    self.address.parent = self


                                class Address(object):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_family is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:start-address-xr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr']['meta_info']


                            class EndAddress(object):
                                """
                                Range end
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address()
                                    self.address.parent = self


                                class Address(object):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_family is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:end-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress']['meta_info']


                            class DefaultRouter(object):
                                """
                                Default router
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address()
                                    self.address.parent = self


                                class Address(object):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_family is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:default-router'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.start_address is None:
                                    raise YPYModelError('Key property start_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address-range[Cisco-IOS-XR-ip-daps-oper:start-address = ' + str(self.start_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.start_address is not None:
                                    return True

                                if self.allocated_addresses is not None:
                                    return True

                                if self.default_router is not None and self.default_router._has_data():
                                    return True

                                if self.end_address is not None and self.end_address._has_data():
                                    return True

                                if self.excluded_addresses is not None:
                                    return True

                                if self.free_addresses is not None:
                                    return True

                                if self.network_blocked_status is not None:
                                    return True

                                if self.network_blocked_status_trp is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.pool_scope is not None:
                                    return True

                                if self.start_address_xr is not None and self.start_address_xr._has_data():
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address-ranges'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_range is not None:
                                for child_ref in self.address_range:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                            return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges']['meta_info']


                    class AllocatedAddresses(object):
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
                            self.parent = None
                            self.address_range = YList()
                            self.address_range.parent = self
                            self.address_range.name = 'address_range'
                            self.in_use_address = YList()
                            self.in_use_address.parent = self
                            self.in_use_address.name = 'in_use_address'
                            self.pool_allocations = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations()
                            self.pool_allocations.parent = self


                        class PoolAllocations(object):
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
                                self.parent = None
                                self.excluded = None
                                self.free = None
                                self.high_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold()
                                self.high_threshold.parent = self
                                self.low_threshold = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold()
                                self.low_threshold.parent = self
                                self.total = None
                                self.used = None
                                self.utilization = None
                                self.vrf_name = None


                            class HighThreshold(object):
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
                                    self.parent = None
                                    self.threshold = None
                                    self.time_last_crossed = None
                                    self.triggers = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:high-threshold'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.threshold is not None:
                                        return True

                                    if self.time_last_crossed is not None:
                                        return True

                                    if self.triggers is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold']['meta_info']


                            class LowThreshold(object):
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
                                    self.parent = None
                                    self.threshold = None
                                    self.time_last_crossed = None
                                    self.triggers = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:low-threshold'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.threshold is not None:
                                        return True

                                    if self.time_last_crossed is not None:
                                        return True

                                    if self.triggers is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:pool-allocations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.excluded is not None:
                                    return True

                                if self.free is not None:
                                    return True

                                if self.high_threshold is not None and self.high_threshold._has_data():
                                    return True

                                if self.low_threshold is not None and self.low_threshold._has_data():
                                    return True

                                if self.total is not None:
                                    return True

                                if self.used is not None:
                                    return True

                                if self.utilization is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations']['meta_info']


                        class AddressRange(object):
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
                                self.parent = None
                                self.end_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress()
                                self.end_address.parent = self
                                self.excluded = None
                                self.free = None
                                self.start_address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress()
                                self.start_address.parent = self
                                self.used = None


                            class StartAddress(object):
                                """
                                Range start
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address()
                                    self.address.parent = self


                                class Address(object):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_family is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:start-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress']['meta_info']


                            class EndAddress(object):
                                """
                                Range end
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address()
                                    self.address.parent = self


                                class Address(object):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_family is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:end-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address-range'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.end_address is not None and self.end_address._has_data():
                                    return True

                                if self.excluded is not None:
                                    return True

                                if self.free is not None:
                                    return True

                                if self.start_address is not None and self.start_address._has_data():
                                    return True

                                if self.used is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange']['meta_info']


                        class InUseAddress(object):
                            """
                            In\-use addresses
                            
                            .. attribute:: address
                            
                            	Client address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address>`
                            
                            .. attribute:: client_type
                            
                            	Client type
                            	**type**\:   :py:class:`DapsClientEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.DapsClientEnum>`
                            
                            

                            """

                            _prefix = 'ip-daps-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address()
                                self.address.parent = self
                                self.client_type = None


                            class Address(object):
                                """
                                Client address
                                
                                .. attribute:: address
                                
                                	Address
                                	**type**\:   :py:class:`Address_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_>`
                                
                                

                                """

                                _prefix = 'ip-daps-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_()
                                    self.address.parent = self


                                class Address_(object):
                                    """
                                    Address
                                    
                                    .. attribute:: address_family
                                    
                                    	AddressFamily
                                    	**type**\:   :py:class:`IpAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.IpAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.address_family = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address_family is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:in-use-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None and self.address._has_data():
                                    return True

                                if self.client_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:allocated-addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_range is not None:
                                for child_ref in self.address_range:
                                    if child_ref._has_data():
                                        return True

                            if self.in_use_address is not None:
                                for child_ref in self.in_use_address:
                                    if child_ref._has_data():
                                        return True

                            if self.pool_allocations is not None and self.pool_allocations._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                            return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses']['meta_info']


                    class Configuration(object):
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
                            self.parent = None
                            self.current_utilization = None
                            self.high_utilization_mark = None
                            self.low_utilization_mark = None
                            self.pool_id = None
                            self.pool_name = None
                            self.pool_prefix_length = None
                            self.pool_scope = None
                            self.utilization_high_count = None
                            self.utilization_low_count = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:configuration'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.current_utilization is not None:
                                return True

                            if self.high_utilization_mark is not None:
                                return True

                            if self.low_utilization_mark is not None:
                                return True

                            if self.pool_id is not None:
                                return True

                            if self.pool_name is not None:
                                return True

                            if self.pool_prefix_length is not None:
                                return True

                            if self.pool_scope is not None:
                                return True

                            if self.utilization_high_count is not None:
                                return True

                            if self.utilization_low_count is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                            return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool.Configuration']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.pool_name is None:
                            raise YPYModelError('Key property pool_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:pool[Cisco-IOS-XR-ip-daps-oper:pool-name = ' + str(self.pool_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pool_name is not None:
                            return True

                        if self.address_ranges is not None and self.address_ranges._has_data():
                            return True

                        if self.allocated_addresses is not None and self.allocated_addresses._has_data():
                            return True

                        if self.configuration is not None and self.configuration._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                        return meta._meta_table['AddressPoolService.Nodes.Node.Pools.Pool']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:pools'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pool is not None:
                        for child_ref in self.pool:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                    return meta._meta_table['AddressPoolService.Nodes.Node.Pools']['meta_info']


            class TotalUtilization(object):
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
                    self.parent = None
                    self.current_total_utilization = None
                    self.total_utilization_high_mark = None
                    self.total_utilization_low_mark = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:total-utilization'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.current_total_utilization is not None:
                        return True

                    if self.total_utilization_high_mark is not None:
                        return True

                    if self.total_utilization_low_mark is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                    return meta._meta_table['AddressPoolService.Nodes.Node.TotalUtilization']['meta_info']


            class Vrfs(object):
                """
                Pool VRF data
                
                .. attribute:: vrf
                
                	VRF level Pool information
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper.AddressPoolService.Nodes.Node.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ip-daps-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
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
                        self.parent = None
                        self.vrf_name = None
                        self.ipv4 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self.ipv6 = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self


                    class Ipv4(object):
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
                            self.parent = None
                            self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary()
                            self.allocation_summary.parent = self
                            self.pools = YList()
                            self.pools.parent = self
                            self.pools.name = 'pools'


                        class AllocationSummary(object):
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
                                self.parent = None
                                self.excluded = None
                                self.free = None
                                self.high_utilization_threshold = None
                                self.low_utilization_threshold = None
                                self.total = None
                                self.used = None
                                self.utilization = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:allocation-summary'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.excluded is not None:
                                    return True

                                if self.free is not None:
                                    return True

                                if self.high_utilization_threshold is not None:
                                    return True

                                if self.low_utilization_threshold is not None:
                                    return True

                                if self.total is not None:
                                    return True

                                if self.used is not None:
                                    return True

                                if self.utilization is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary']['meta_info']


                        class Pools(object):
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
                                self.parent = None
                                self.excluded = None
                                self.free = None
                                self.pool_name = None
                                self.total = None
                                self.used = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:pools'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.excluded is not None:
                                    return True

                                if self.free is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.total is not None:
                                    return True

                                if self.used is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:ipv4'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.allocation_summary is not None and self.allocation_summary._has_data():
                                return True

                            if self.pools is not None:
                                for child_ref in self.pools:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                            return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4']['meta_info']


                    class Ipv6(object):
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
                            self.parent = None
                            self.allocation_summary = AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary()
                            self.allocation_summary.parent = self
                            self.pools = YList()
                            self.pools.parent = self
                            self.pools.name = 'pools'


                        class AllocationSummary(object):
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
                                self.parent = None
                                self.excluded = None
                                self.free = None
                                self.high_utilization_threshold = None
                                self.low_utilization_threshold = None
                                self.total = None
                                self.used = None
                                self.utilization = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:allocation-summary'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.excluded is not None:
                                    return True

                                if self.free is not None:
                                    return True

                                if self.high_utilization_threshold is not None:
                                    return True

                                if self.low_utilization_threshold is not None:
                                    return True

                                if self.total is not None:
                                    return True

                                if self.used is not None:
                                    return True

                                if self.utilization is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary']['meta_info']


                        class Pools(object):
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
                                self.parent = None
                                self.excluded = None
                                self.free = None
                                self.pool_name = None
                                self.total = None
                                self.used = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:pools'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.excluded is not None:
                                    return True

                                if self.free is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.total is not None:
                                    return True

                                if self.used is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                                return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:ipv6'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.allocation_summary is not None and self.allocation_summary._has_data():
                                return True

                            if self.pools is not None:
                                for child_ref in self.pools:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                            return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:vrf[Cisco-IOS-XR-ip-daps-oper:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.ipv4 is not None and self.ipv4._has_data():
                            return True

                        if self.ipv6 is not None and self.ipv6._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                        return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-oper:vrfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                    return meta._meta_table['AddressPoolService.Nodes.Node.Vrfs']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-daps-oper:address-pool-service/Cisco-IOS-XR-ip-daps-oper:nodes/Cisco-IOS-XR-ip-daps-oper:node[Cisco-IOS-XR-ip-daps-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.pools is not None and self.pools._has_data():
                    return True

                if self.total_utilization is not None and self.total_utilization._has_data():
                    return True

                if self.vrfs is not None and self.vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
                return meta._meta_table['AddressPoolService.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-daps-oper:address-pool-service/Cisco-IOS-XR-ip-daps-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
            return meta._meta_table['AddressPoolService.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-daps-oper:address-pool-service'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_oper as meta
        return meta._meta_table['AddressPoolService']['meta_info']


