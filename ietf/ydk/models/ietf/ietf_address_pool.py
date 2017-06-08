""" ietf_address_pool 

This module contains a collection of YANG definitions for
   configuring IP address pools.

   Copyright (c) 2015 IETF Trust and the persons identified as
   authors of the code.  All rights reserved.

   Redistribution and use in source and binary forms, with or
   without modification, is permitted pursuant to, and subject
   to the license terms contained in, the Simplified BSD License
   set forth in Section 4.c of the IETF Trust's Legal Provisions
   Relating to IETF Documents
   (http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC 7277; see
   the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AddressPoolTypeEnum(Enum):
    """
    AddressPoolTypeEnum

    Address pool type.

    .. data:: usergateway = 0

    	The address pool has a usergateway.

    .. data:: import_route = 1

    	The address pool need to import a route

    	to external network.

    """

    usergateway = 0

    import_route = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_address_pool as meta
        return meta._meta_table['AddressPoolTypeEnum']


class InstanceTypeEnum(Enum):
    """
    InstanceTypeEnum

    Instance type.

    .. data:: pppoe = 0

    	The address pool is used for pppoe access.

    .. data:: dhcp = 1

    	The address pool is used for dhcp access.

    .. data:: vpn = 2

    	The address pool is used for vpn access.

    .. data:: ds_lite = 3

    	The address pool is used for ds-lite access.

    .. data:: lw4over6 = 4

    	The address pool is used for lw4over6 access.

    .. data:: map = 5

    	The address pool is used for map access.

    .. data:: cgn = 6

    	The address pool is used for cgn access.

    .. data:: xlat = 7

    	The address pool is used for xlat access.

    .. data:: other = 8

    	The address pool is used for others.

    """

    pppoe = 0

    dhcp = 1

    vpn = 2

    ds_lite = 3

    lw4over6 = 4

    map = 5

    cgn = 6

    xlat = 7

    other = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_address_pool as meta
        return meta._meta_table['InstanceTypeEnum']



class AddressPools(object):
    """
    This is a top level container for Address Pools.
    It can have one or more Address Pools. The pools may
    not be contiguous.
    
    .. attribute:: address_pool
    
    	An Address Pool is an ordered list of Address Pool Entries (APE). Each Access Pool Entry has a list of address ranges and its associated lifetime
    	**type**\: list of    :py:class:`AddressPool <ydk.models.ietf.ietf_address_pool.AddressPools.AddressPool>`
    
    

    """

    _prefix = 'address-pool'
    _revision = '2015-10-14'

    def __init__(self):
        self.address_pool = YList()
        self.address_pool.parent = self
        self.address_pool.name = 'address_pool'


    class AddressPool(object):
        """
        An Address Pool is an ordered list of
        Address Pool Entries (APE). Each Access Pool Entry has a
        list of address ranges and its associated lifetime.
        
        .. attribute:: address_pool_name  <key>
        
        	The name of address pool
        	**type**\:  str
        
        .. attribute:: address_pool_entries
        
        	The address\-pool\-entries container contains a list of address\-ranges and associated attributes
        	**type**\:   :py:class:`AddressPoolEntries <ydk.models.ietf.ietf_address_pool.AddressPools.AddressPool.AddressPoolEntries>`
        
        .. attribute:: address_pool_id
        
        	The Address Pool id
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 0
        
        .. attribute:: address_pool_service
        
        	The services that can use these pool
        	**type**\: list of    :py:class:`AddressPoolService <ydk.models.ietf.ietf_address_pool.AddressPools.AddressPool.AddressPoolService>`
        
        .. attribute:: device_id
        
        	The identifier of device that using address pool
        	**type**\:  str
        
        .. attribute:: domain_name
        
        	The domain name
        	**type**\:  str
        
        

        """

        _prefix = 'address-pool'
        _revision = '2015-10-14'

        def __init__(self):
            self.parent = None
            self.address_pool_name = None
            self.address_pool_entries = AddressPools.AddressPool.AddressPoolEntries()
            self.address_pool_entries.parent = self
            self.address_pool_id = None
            self.address_pool_service = YList()
            self.address_pool_service.parent = self
            self.address_pool_service.name = 'address_pool_service'
            self.device_id = None
            self.domain_name = None


        class AddressPoolService(object):
            """
            The services that can use these pool.
            
            .. attribute:: service_name  <key>
            
            	A service name\: e.g., any, voip, iptv, internet, etc
            	**type**\:  str
            
            

            """

            _prefix = 'address-pool'
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.service_name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.service_name is None:
                    raise YPYModelError('Key property service_name is None')

                return self.parent._common_path +'/ietf-address-pool:address-pool-service[ietf-address-pool:service-name = ' + str(self.service_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.service_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_address_pool as meta
                return meta._meta_table['AddressPools.AddressPool.AddressPoolService']['meta_info']


        class AddressPoolEntries(object):
            """
            The address\-pool\-entries container contains
            a list of address\-ranges and associated attributes.
            
            .. attribute:: ipv4_address_range
            
            	IPv4 Address range
            	**type**\: list of    :py:class:`Ipv4AddressRange <ydk.models.ietf.ietf_address_pool.AddressPools.AddressPool.AddressPoolEntries.Ipv4AddressRange>`
            
            .. attribute:: ipv6_prefix
            
            	IPv6 prefix
            	**type**\: list of    :py:class:`Ipv6Prefix <ydk.models.ietf.ietf_address_pool.AddressPools.AddressPool.AddressPoolEntries.Ipv6Prefix>`
            
            .. attribute:: warning_threshold_v4
            
            	The threshold of the ipv4 address pool
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: warning_threshold_v6
            
            	The threshold of the ipv6 address pool
            	**type**\:  int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'address-pool'
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.ipv4_address_range = YList()
                self.ipv4_address_range.parent = self
                self.ipv4_address_range.name = 'ipv4_address_range'
                self.ipv6_prefix = YList()
                self.ipv6_prefix.parent = self
                self.ipv6_prefix.name = 'ipv6_prefix'
                self.warning_threshold_v4 = None
                self.warning_threshold_v6 = None


            class Ipv4AddressRange(object):
                """
                IPv4 Address range.
                
                .. attribute:: ipv4_address_range_name  <key>
                
                	The name of IPv4 address range
                	**type**\:  str
                
                .. attribute:: gwnetmask
                
                	The netmask for usergateway
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                .. attribute:: instance
                
                	The instance of the address pool
                	**type**\:   :py:class:`InstanceTypeEnum <ydk.models.ietf.ietf_address_pool.InstanceTypeEnum>`
                
                .. attribute:: ip_lower_address
                
                	The lower IPv4 address of the address range
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ip_upper_address
                
                	The upper IPv4 address of the address range
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: lifetime
                
                	The lifetime for the address pool. '0' means withdrawal
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: type
                
                	The type of the address pool
                	**type**\:   :py:class:`AddressPoolTypeEnum <ydk.models.ietf.ietf_address_pool.AddressPoolTypeEnum>`
                
                .. attribute:: usergateway
                
                	It only exists when address pool are used for user addressing
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'address-pool'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.ipv4_address_range_name = None
                    self.gwnetmask = None
                    self.instance = None
                    self.ip_lower_address = None
                    self.ip_upper_address = None
                    self.lifetime = None
                    self.type = None
                    self.usergateway = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ipv4_address_range_name is None:
                        raise YPYModelError('Key property ipv4_address_range_name is None')

                    return self.parent._common_path +'/ietf-address-pool:ipv4-address-range[ietf-address-pool:ipv4-address-range-name = ' + str(self.ipv4_address_range_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ipv4_address_range_name is not None:
                        return True

                    if self.gwnetmask is not None:
                        return True

                    if self.instance is not None:
                        return True

                    if self.ip_lower_address is not None:
                        return True

                    if self.ip_upper_address is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.usergateway is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_address_pool as meta
                    return meta._meta_table['AddressPools.AddressPool.AddressPoolEntries.Ipv4AddressRange']['meta_info']


            class Ipv6Prefix(object):
                """
                IPv6 prefix.
                
                .. attribute:: ipv6_prefix_name  <key>
                
                	The name of IPv6 prefix
                	**type**\:  str
                
                .. attribute:: instance
                
                	The instance of the address pool
                	**type**\:   :py:class:`InstanceTypeEnum <ydk.models.ietf.ietf_address_pool.InstanceTypeEnum>`
                
                .. attribute:: ipv6_prefix
                
                	The IPv6 prefix
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: lifetime
                
                	The lifetime for the address pool. '0' means withdrawal
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: type
                
                	The type of the address pool
                	**type**\:   :py:class:`AddressPoolTypeEnum <ydk.models.ietf.ietf_address_pool.AddressPoolTypeEnum>`
                
                .. attribute:: usergateway
                
                	It only exists when address pool are used for user addressing
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'address-pool'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.ipv6_prefix_name = None
                    self.instance = None
                    self.ipv6_prefix = None
                    self.lifetime = None
                    self.type = None
                    self.usergateway = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ipv6_prefix_name is None:
                        raise YPYModelError('Key property ipv6_prefix_name is None')

                    return self.parent._common_path +'/ietf-address-pool:ipv6-prefix[ietf-address-pool:ipv6-prefix-name = ' + str(self.ipv6_prefix_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ipv6_prefix_name is not None:
                        return True

                    if self.instance is not None:
                        return True

                    if self.ipv6_prefix is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.usergateway is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_address_pool as meta
                    return meta._meta_table['AddressPools.AddressPool.AddressPoolEntries.Ipv6Prefix']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-address-pool:address-pool-entries'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ipv4_address_range is not None:
                    for child_ref in self.ipv4_address_range:
                        if child_ref._has_data():
                            return True

                if self.ipv6_prefix is not None:
                    for child_ref in self.ipv6_prefix:
                        if child_ref._has_data():
                            return True

                if self.warning_threshold_v4 is not None:
                    return True

                if self.warning_threshold_v6 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_address_pool as meta
                return meta._meta_table['AddressPools.AddressPool.AddressPoolEntries']['meta_info']

        @property
        def _common_path(self):
            if self.address_pool_name is None:
                raise YPYModelError('Key property address_pool_name is None')

            return '/ietf-address-pool:address-pools/ietf-address-pool:address-pool[ietf-address-pool:address-pool-name = ' + str(self.address_pool_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.address_pool_name is not None:
                return True

            if self.address_pool_entries is not None and self.address_pool_entries._has_data():
                return True

            if self.address_pool_id is not None:
                return True

            if self.address_pool_service is not None:
                for child_ref in self.address_pool_service:
                    if child_ref._has_data():
                        return True

            if self.device_id is not None:
                return True

            if self.domain_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_address_pool as meta
            return meta._meta_table['AddressPools.AddressPool']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-address-pool:address-pools'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.address_pool is not None:
            for child_ref in self.address_pool:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_address_pool as meta
        return meta._meta_table['AddressPools']['meta_info']


class AddressPoolStatus(object):
    """
    This is a top level container for Address Pool Status,
    which contains the status of address pool usage.
    
    .. attribute:: address_pool
    
    	An Address Pool is an ordered list of Address Pool Entries (APE). Each Access Pool Entry has a list of address ranges and its associated lifetime. 
    	**type**\: list of    :py:class:`AddressPool <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool>`
    
    

    """

    _prefix = 'address-pool'
    _revision = '2015-10-14'

    def __init__(self):
        self.address_pool = YList()
        self.address_pool.parent = self
        self.address_pool.name = 'address_pool'


    class AddressPool(object):
        """
        An Address Pool is an ordered list of
        Address Pool Entries (APE). Each Access Pool Entry has a
        list of address ranges and its associated lifetime. 
        
        .. attribute:: address_pool_name  <key>
        
        	The name of address pool
        	**type**\:  str
        
        .. attribute:: address_pool_entries
        
        	The address\-pool\-entries container contains a list of address\-ranges and associated attributes
        	**type**\:   :py:class:`AddressPoolEntries <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool.AddressPoolEntries>`
        
        .. attribute:: address_pool_service
        
        	The services that can use these pool
        	**type**\: list of    :py:class:`AddressPoolService <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool.AddressPoolService>`
        
        .. attribute:: status
        
        	The status of address pool
        	**type**\:   :py:class:`StatusEnum <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool.StatusEnum>`
        
        

        """

        _prefix = 'address-pool'
        _revision = '2015-10-14'

        def __init__(self):
            self.parent = None
            self.address_pool_name = None
            self.address_pool_entries = AddressPoolStatus.AddressPool.AddressPoolEntries()
            self.address_pool_entries.parent = self
            self.address_pool_service = YList()
            self.address_pool_service.parent = self
            self.address_pool_service.name = 'address_pool_service'
            self.status = None

        class StatusEnum(Enum):
            """
            StatusEnum

            The status of address pool

            .. data:: active = 0

            	The address pool is in active status.

            .. data:: idle = 1

            	The address pool is in idle status.

            """

            active = 0

            idle = 1


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_address_pool as meta
                return meta._meta_table['AddressPoolStatus.AddressPool.StatusEnum']



        class AddressPoolService(object):
            """
            The services that can use these pool.
            
            .. attribute:: service_name  <key>
            
            	A service name\: e.g., any, voip, iptv, internet, etc
            	**type**\:  str
            
            

            """

            _prefix = 'address-pool'
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.service_name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.service_name is None:
                    raise YPYModelError('Key property service_name is None')

                return self.parent._common_path +'/ietf-address-pool:address-pool-service[ietf-address-pool:service-name = ' + str(self.service_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.service_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_address_pool as meta
                return meta._meta_table['AddressPoolStatus.AddressPool.AddressPoolService']['meta_info']


        class AddressPoolEntries(object):
            """
            The address\-pool\-entries container contains
            a list of address\-ranges and associated attributes.
            
            .. attribute:: ipv4_address_range
            
            	IPv4 Address range
            	**type**\: list of    :py:class:`Ipv4AddressRange <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv4AddressRange>`
            
            .. attribute:: ipv6_prefix
            
            	IPv6 prefix
            	**type**\: list of    :py:class:`Ipv6Prefix <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv6Prefix>`
            
            .. attribute:: port_range
            
            	port range
            	**type**\: list of    :py:class:`PortRange <ydk.models.ietf.ietf_address_pool.AddressPoolStatus.AddressPool.AddressPoolEntries.PortRange>`
            
            

            """

            _prefix = 'address-pool'
            _revision = '2015-10-14'

            def __init__(self):
                self.parent = None
                self.ipv4_address_range = YList()
                self.ipv4_address_range.parent = self
                self.ipv4_address_range.name = 'ipv4_address_range'
                self.ipv6_prefix = YList()
                self.ipv6_prefix.parent = self
                self.ipv6_prefix.name = 'ipv6_prefix'
                self.port_range = YList()
                self.port_range.parent = self
                self.port_range.name = 'port_range'


            class Ipv4AddressRange(object):
                """
                IPv4 Address range.
                
                .. attribute:: ipv4_address_range_name  <key>
                
                	The name of IPv4 address range
                	**type**\:  str
                
                .. attribute:: average_address_usage_ratio
                
                	The average usage rate of the address range
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: peak_address_usage_ratio
                
                	The peak usage rate of the address range
                	**type**\:  int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'address-pool'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.ipv4_address_range_name = None
                    self.average_address_usage_ratio = None
                    self.peak_address_usage_ratio = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ipv4_address_range_name is None:
                        raise YPYModelError('Key property ipv4_address_range_name is None')

                    return self.parent._common_path +'/ietf-address-pool:ipv4-address-range[ietf-address-pool:ipv4-address-range-name = ' + str(self.ipv4_address_range_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ipv4_address_range_name is not None:
                        return True

                    if self.average_address_usage_ratio is not None:
                        return True

                    if self.peak_address_usage_ratio is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_address_pool as meta
                    return meta._meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv4AddressRange']['meta_info']


            class Ipv6Prefix(object):
                """
                IPv6 prefix.
                
                .. attribute:: ipv6_prefix_name  <key>
                
                	The name of IPv6 prefix
                	**type**\:  str
                
                .. attribute:: average_prefix_usage_ratio
                
                	The average usage rate of the prefix
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: peak_prefix_usage_ratio
                
                	The peak usage rate of the prefix
                	**type**\:  int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'address-pool'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.ipv6_prefix_name = None
                    self.average_prefix_usage_ratio = None
                    self.peak_prefix_usage_ratio = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ipv6_prefix_name is None:
                        raise YPYModelError('Key property ipv6_prefix_name is None')

                    return self.parent._common_path +'/ietf-address-pool:ipv6-prefix[ietf-address-pool:ipv6-prefix-name = ' + str(self.ipv6_prefix_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ipv6_prefix_name is not None:
                        return True

                    if self.average_prefix_usage_ratio is not None:
                        return True

                    if self.peak_prefix_usage_ratio is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_address_pool as meta
                    return meta._meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv6Prefix']['meta_info']


            class PortRange(object):
                """
                port range.
                
                .. attribute:: port_range_name  <key>
                
                	The name of port range
                	**type**\:  str
                
                .. attribute:: average_address_usage_ratio
                
                	The average usage rate of the port range
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: peak_address_usage_ratio
                
                	The peak usage rate of the port range
                	**type**\:  int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'address-pool'
                _revision = '2015-10-14'

                def __init__(self):
                    self.parent = None
                    self.port_range_name = None
                    self.average_address_usage_ratio = None
                    self.peak_address_usage_ratio = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.port_range_name is None:
                        raise YPYModelError('Key property port_range_name is None')

                    return self.parent._common_path +'/ietf-address-pool:port-range[ietf-address-pool:port-range-name = ' + str(self.port_range_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.port_range_name is not None:
                        return True

                    if self.average_address_usage_ratio is not None:
                        return True

                    if self.peak_address_usage_ratio is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_address_pool as meta
                    return meta._meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries.PortRange']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-address-pool:address-pool-entries'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ipv4_address_range is not None:
                    for child_ref in self.ipv4_address_range:
                        if child_ref._has_data():
                            return True

                if self.ipv6_prefix is not None:
                    for child_ref in self.ipv6_prefix:
                        if child_ref._has_data():
                            return True

                if self.port_range is not None:
                    for child_ref in self.port_range:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_address_pool as meta
                return meta._meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries']['meta_info']

        @property
        def _common_path(self):
            if self.address_pool_name is None:
                raise YPYModelError('Key property address_pool_name is None')

            return '/ietf-address-pool:address-pool-status/ietf-address-pool:address-pool[ietf-address-pool:address-pool-name = ' + str(self.address_pool_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.address_pool_name is not None:
                return True

            if self.address_pool_entries is not None and self.address_pool_entries._has_data():
                return True

            if self.address_pool_service is not None:
                for child_ref in self.address_pool_service:
                    if child_ref._has_data():
                        return True

            if self.status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_address_pool as meta
            return meta._meta_table['AddressPoolStatus.AddressPool']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-address-pool:address-pool-status'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.address_pool is not None:
            for child_ref in self.address_pool:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_address_pool as meta
        return meta._meta_table['AddressPoolStatus']['meta_info']


