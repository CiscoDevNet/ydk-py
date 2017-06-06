""" Cisco_IOS_XR_ip_daps_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-daps package configuration.

This module contains definitions
for the following management objects\:
  address\-pool\-service\: Address Pool configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AddressPoolService(object):
    """
    Address Pool configuration data
    
    .. attribute:: vrfs
    
    	Enter VRF specific config mode
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs>`
    
    

    """

    _prefix = 'ip-daps-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.vrfs = AddressPoolService.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        Enter VRF specific config mode
        
        .. attribute:: vrf
        
        	Specify VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-daps-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
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
                self.parent = None
                self.vrf_name = None
                self.ipv4 = AddressPoolService.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = AddressPoolService.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self


            class Ipv6(object):
                """
                Enter IPv6 specific mode
                
                .. attribute:: pools
                
                	IPv6 Pool Name
                	**type**\:   :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools>`
                
                

                """

                _prefix = 'ip-daps-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.pools = AddressPoolService.Vrfs.Vrf.Ipv6.Pools()
                    self.pools.parent = self


                class Pools(object):
                    """
                    IPv6 Pool Name
                    
                    .. attribute:: pool
                    
                    	Enter the IPv6 Pool name
                    	**type**\: list of    :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool>`
                    
                    

                    """

                    _prefix = 'ip-daps-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pool = YList()
                        self.pool.parent = self
                        self.pool.name = 'pool'


                    class Pool(object):
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
                            self.parent = None
                            self.ipv6_pool_name = None
                            self.address_ranges = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges()
                            self.address_ranges.parent = self
                            self.excludes = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes()
                            self.excludes.parent = self
                            self.networks = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks()
                            self.networks.parent = self
                            self.prefix_length = None
                            self.prefix_ranges = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges()
                            self.prefix_ranges.parent = self
                            self.utilization_mark = AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark()
                            self.utilization_mark.parent = self


                        class AddressRanges(object):
                            """
                            Specify address range for allocation
                            
                            .. attribute:: address_range
                            
                            	None
                            	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address_range = YList()
                                self.address_range.parent = self
                                self.address_range.name = 'address_range'


                            class AddressRange(object):
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
                                    self.parent = None
                                    self.start_address = None
                                    self.blocked = None
                                    self.end_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.start_address is None:
                                        raise YPYModelError('Key property start_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:address-range[Cisco-IOS-XR-ip-daps-cfg:start-address = ' + str(self.start_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.start_address is not None:
                                        return True

                                    if self.blocked is not None:
                                        return True

                                    if self.end_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:address-ranges'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address_range is not None:
                                    for child_ref in self.address_range:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges']['meta_info']


                        class Excludes(object):
                            """
                            Exclude IPv6 addresses / prefixes
                            
                            .. attribute:: exclude
                            
                            	None
                            	**type**\: list of    :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.exclude = YList()
                                self.exclude.parent = self
                                self.exclude.name = 'exclude'


                            class Exclude(object):
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
                                    self.parent = None
                                    self.start_address = None
                                    self.end_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.start_address is None:
                                        raise YPYModelError('Key property start_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:exclude[Cisco-IOS-XR-ip-daps-cfg:start-address = ' + str(self.start_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.start_address is not None:
                                        return True

                                    if self.end_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:excludes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.exclude is not None:
                                    for child_ref in self.exclude:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes']['meta_info']


                        class UtilizationMark(object):
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
                                self.parent = None
                                self.high_mark = None
                                self.low_mark = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:utilization-mark'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.high_mark is not None:
                                    return True

                                if self.low_mark is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark']['meta_info']


                        class PrefixRanges(object):
                            """
                            Specify prefix range for allocation
                            
                            .. attribute:: prefix_range
                            
                            	None
                            	**type**\: list of    :py:class:`PrefixRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.prefix_range = YList()
                                self.prefix_range.parent = self
                                self.prefix_range.name = 'prefix_range'


                            class PrefixRange(object):
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
                                    self.parent = None
                                    self.start_prefix = None
                                    self.blocked = None
                                    self.end_prefix = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.start_prefix is None:
                                        raise YPYModelError('Key property start_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:prefix-range[Cisco-IOS-XR-ip-daps-cfg:start-prefix = ' + str(self.start_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.start_prefix is not None:
                                        return True

                                    if self.blocked is not None:
                                        return True

                                    if self.end_prefix is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:prefix-ranges'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.prefix_range is not None:
                                    for child_ref in self.prefix_range:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges']['meta_info']


                        class Networks(object):
                            """
                            Specify network for allocation
                            
                            .. attribute:: network
                            
                            	None
                            	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.network = YList()
                                self.network.parent = self
                                self.network.name = 'network'


                            class Network(object):
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
                                    self.parent = None
                                    self.prefix = None
                                    self.blocked = None
                                    self.prefix_length = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.prefix is None:
                                        raise YPYModelError('Key property prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:network[Cisco-IOS-XR-ip-daps-cfg:prefix = ' + str(self.prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix is not None:
                                        return True

                                    if self.blocked is not None:
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:networks'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.network is not None:
                                    for child_ref in self.network:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ipv6_pool_name is None:
                                raise YPYModelError('Key property ipv6_pool_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:pool[Cisco-IOS-XR-ip-daps-cfg:ipv6-pool-name = ' + str(self.ipv6_pool_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ipv6_pool_name is not None:
                                return True

                            if self.address_ranges is not None and self.address_ranges._has_data():
                                return True

                            if self.excludes is not None and self.excludes._has_data():
                                return True

                            if self.networks is not None and self.networks._has_data():
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.prefix_ranges is not None and self.prefix_ranges._has_data():
                                return True

                            if self.utilization_mark is not None and self.utilization_mark._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                            return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:pools'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.pool is not None:
                            for child_ref in self.pool:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                        return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.pools is not None and self.pools._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv6']['meta_info']


            class Ipv4(object):
                """
                Enter IPv4 specific configuration
                
                .. attribute:: pools
                
                	IPv4 Pool Table
                	**type**\:   :py:class:`Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools>`
                
                

                """

                _prefix = 'ip-daps-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.pools = AddressPoolService.Vrfs.Vrf.Ipv4.Pools()
                    self.pools.parent = self


                class Pools(object):
                    """
                    IPv4 Pool Table
                    
                    .. attribute:: pool
                    
                    	IPv4 Pool name
                    	**type**\: list of    :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool>`
                    
                    

                    """

                    _prefix = 'ip-daps-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pool = YList()
                        self.pool.parent = self
                        self.pool.name = 'pool'


                    class Pool(object):
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
                            self.parent = None
                            self.pool_name = None
                            self.address_ranges = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges()
                            self.address_ranges.parent = self
                            self.excludes = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes()
                            self.excludes.parent = self
                            self.networks = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks()
                            self.networks.parent = self
                            self.utilization_mark = AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark()
                            self.utilization_mark.parent = self


                        class AddressRanges(object):
                            """
                            address range for allocation
                            
                            .. attribute:: address_range
                            
                            	Specify first address in range
                            	**type**\: list of    :py:class:`AddressRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address_range = YList()
                                self.address_range.parent = self
                                self.address_range.name = 'address_range'


                            class AddressRange(object):
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
                                    self.parent = None
                                    self.start_address = None
                                    self.blocked = None
                                    self.end_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.start_address is None:
                                        raise YPYModelError('Key property start_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:address-range[Cisco-IOS-XR-ip-daps-cfg:start-address = ' + str(self.start_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.start_address is not None:
                                        return True

                                    if self.blocked is not None:
                                        return True

                                    if self.end_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:address-ranges'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address_range is not None:
                                    for child_ref in self.address_range:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges']['meta_info']


                        class Excludes(object):
                            """
                            Exclude addresses
                            
                            .. attribute:: exclude
                            
                            	First address in range
                            	**type**\: list of    :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.exclude = YList()
                                self.exclude.parent = self
                                self.exclude.name = 'exclude'


                            class Exclude(object):
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
                                    self.parent = None
                                    self.start_address = None
                                    self.end_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.start_address is None:
                                        raise YPYModelError('Key property start_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:exclude[Cisco-IOS-XR-ip-daps-cfg:start-address = ' + str(self.start_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.start_address is not None:
                                        return True

                                    if self.end_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:excludes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.exclude is not None:
                                    for child_ref in self.exclude:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes']['meta_info']


                        class UtilizationMark(object):
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
                                self.parent = None
                                self.high = None
                                self.low = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:utilization-mark'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.high is not None:
                                    return True

                                if self.low is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark']['meta_info']


                        class Networks(object):
                            """
                            Specify network for allocation
                            
                            .. attribute:: network
                            
                            	Network Prefix
                            	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg.AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network>`
                            
                            

                            """

                            _prefix = 'ip-daps-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.network = YList()
                                self.network.parent = self
                                self.network.name = 'network'


                            class Network(object):
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
                                    self.parent = None
                                    self.ipv4_prefix = None
                                    self.blocked = None
                                    self.default_router = None
                                    self.prefix_length = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.ipv4_prefix is None:
                                        raise YPYModelError('Key property ipv4_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:network[Cisco-IOS-XR-ip-daps-cfg:ipv4-prefix = ' + str(self.ipv4_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.ipv4_prefix is not None:
                                        return True

                                    if self.blocked is not None:
                                        return True

                                    if self.default_router is not None:
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:networks'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.network is not None:
                                    for child_ref in self.network:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                                return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.pool_name is None:
                                raise YPYModelError('Key property pool_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:pool[Cisco-IOS-XR-ip-daps-cfg:pool-name = ' + str(self.pool_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.pool_name is not None:
                                return True

                            if self.address_ranges is not None and self.address_ranges._has_data():
                                return True

                            if self.excludes is not None and self.excludes._has_data():
                                return True

                            if self.networks is not None and self.networks._has_data():
                                return True

                            if self.utilization_mark is not None and self.utilization_mark._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                            return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:pools'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.pool is not None:
                            for child_ref in self.pool:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                        return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-daps-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.pools is not None and self.pools._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                    return meta._meta_table['AddressPoolService.Vrfs.Vrf.Ipv4']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-daps-cfg:address-pool-service/Cisco-IOS-XR-ip-daps-cfg:vrfs/Cisco-IOS-XR-ip-daps-cfg:vrf[Cisco-IOS-XR-ip-daps-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
                return meta._meta_table['AddressPoolService.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-daps-cfg:address-pool-service/Cisco-IOS-XR-ip-daps-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
            return meta._meta_table['AddressPoolService.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-daps-cfg:address-pool-service'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_daps_cfg as meta
        return meta._meta_table['AddressPoolService']['meta_info']


