""" Cisco_IOS_XR_ip_iarm_v4_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iarm\-v4 package operational data.

This module contains definitions
for the following management objects\:
  ipv4arm\: IPv4 Address Repository Manager (IPv4 ARM)
    operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ipv4Arm(object):
    """
    IPv4 Address Repository Manager (IPv4 ARM)
    operational data
    
    .. attribute:: addresses
    
    	IPv4 ARM address database information
    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses>`
    
    .. attribute:: multicast_host_interface
    
    	Default multicast host interface
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: router_id
    
    	IPv4 ARM Router ID information
    	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.RouterId>`
    
    .. attribute:: summary
    
    	IPv4 ARM summary information
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Summary>`
    
    .. attribute:: vrf_summaries
    
    	IPv4 ARM VRFs summary information
    	**type**\:   :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.VrfSummaries>`
    
    

    """

    _prefix = 'ip-iarm-v4-oper'
    _revision = '2016-12-19'

    def __init__(self):
        self.addresses = Ipv4Arm.Addresses()
        self.addresses.parent = self
        self.multicast_host_interface = None
        self.router_id = Ipv4Arm.RouterId()
        self.router_id.parent = self
        self.summary = Ipv4Arm.Summary()
        self.summary.parent = self
        self.vrf_summaries = Ipv4Arm.VrfSummaries()
        self.vrf_summaries.parent = self


    class Addresses(object):
        """
        IPv4 ARM address database information
        
        .. attribute:: vrfs
        
        	IPv4 ARM address database information per VRF
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs>`
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.vrfs = Ipv4Arm.Addresses.Vrfs()
            self.vrfs.parent = self


        class Vrfs(object):
            """
            IPv4 ARM address database information per VRF
            
            .. attribute:: vrf
            
            	IPv4 ARM address database information in a VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf>`
            
            

            """

            _prefix = 'ip-iarm-v4-oper'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.vrf = YList()
                self.vrf.parent = self
                self.vrf.name = 'vrf'


            class Vrf(object):
                """
                IPv4 ARM address database information in a VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                .. attribute:: interfaces
                
                	IPv4 ARM address database information by interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces>`
                
                .. attribute:: networks
                
                	IPv4 ARM address database information by network
                	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks>`
                
                

                """

                _prefix = 'ip-iarm-v4-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.interfaces = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces()
                    self.interfaces.parent = self
                    self.networks = Ipv4Arm.Addresses.Vrfs.Vrf.Networks()
                    self.networks.parent = self


                class Networks(object):
                    """
                    IPv4 ARM address database information by
                    network
                    
                    .. attribute:: network
                    
                    	An IPv4 Address in IPv4 ARM
                    	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v4-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.network = YList()
                        self.network.parent = self
                        self.network.name = 'network'


                    class Network(object):
                        """
                        An IPv4 Address in IPv4 ARM
                        
                        .. attribute:: address
                        
                        	Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_xr
                        
                        	Address info
                        	**type**\:   :py:class:`AddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr>`
                        
                        .. attribute:: handle
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  str
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-iarm-v4-oper'
                        _revision = '2016-12-19'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.address_xr = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr()
                            self.address_xr.parent = self
                            self.handle = None
                            self.interface_name = None
                            self.prefix_length = None
                            self.referenced_interface = None
                            self.vrf_name = None


                        class AddressXr(object):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address>`
                            
                            .. attribute:: is_prefix_sid
                            
                            	Is prefix\_sid valid \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_primary
                            
                            	Is address primary \- valid only for IPv4 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_tentative
                            
                            	Is address valid/tentative \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: producer
                            
                            	Producer Name
                            	**type**\:  str
                            
                            .. attribute:: route_tag
                            
                            	Route Tag of the address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-iarm-v4-oper'
                            _revision = '2016-12-19'

                            def __init__(self):
                                self.parent = None
                                self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address()
                                self.address.parent = self
                                self.is_prefix_sid = None
                                self.is_primary = None
                                self.is_tentative = None
                                self.prefix_length = None
                                self.producer = None
                                self.route_tag = None


                            class Address(object):
                                """
                                Address
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: ipv4_address
                                
                                	IPV4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPV6 Address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-iarm-v4-oper'
                                _revision = '2016-12-19'

                                def __init__(self):
                                    self.parent = None
                                    self.afi = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.afi is not None:
                                        return True

                                    if self.ipv4_address is not None:
                                        return True

                                    if self.ipv6_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                                    return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:address-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None and self.address._has_data():
                                    return True

                                if self.is_prefix_sid is not None:
                                    return True

                                if self.is_primary is not None:
                                    return True

                                if self.is_tentative is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.producer is not None:
                                    return True

                                if self.route_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                                return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:network'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.address_xr is not None and self.address_xr._has_data():
                                return True

                            if self.handle is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.referenced_interface is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                            return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Networks.Network']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:networks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.network is not None:
                            for child_ref in self.network:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                        return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Networks']['meta_info']


                class Interfaces(object):
                    """
                    IPv4 ARM address database information by
                    interface
                    
                    .. attribute:: interface
                    
                    	An IPv4 address in IPv4 ARM
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ip-iarm-v4-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        An IPv4 address in IPv4 ARM
                        
                        .. attribute:: interface  <key>
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: address
                        
                        	Address info
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address>`
                        
                        .. attribute:: referenced_interface
                        
                        	Referenced Interface \- only valid for an unnumbered interface
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-iarm-v4-oper'
                        _revision = '2016-12-19'

                        def __init__(self):
                            self.parent = None
                            self.interface = None
                            self.address = YList()
                            self.address.parent = self
                            self.address.name = 'address'
                            self.referenced_interface = None
                            self.vrf_name = None


                        class Address(object):
                            """
                            Address info
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:   :py:class:`Address_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_>`
                            
                            .. attribute:: is_prefix_sid
                            
                            	Is prefix\_sid valid \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_primary
                            
                            	Is address primary \- valid only for IPv4 addresses
                            	**type**\:  bool
                            
                            .. attribute:: is_tentative
                            
                            	Is address valid/tentative \- valid only for IPV6 addresses
                            	**type**\:  bool
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: producer
                            
                            	Producer Name
                            	**type**\:  str
                            
                            .. attribute:: route_tag
                            
                            	Route Tag of the address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-iarm-v4-oper'
                            _revision = '2016-12-19'

                            def __init__(self):
                                self.parent = None
                                self.address = Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_()
                                self.address.parent = self
                                self.is_prefix_sid = None
                                self.is_primary = None
                                self.is_tentative = None
                                self.prefix_length = None
                                self.producer = None
                                self.route_tag = None


                            class Address_(object):
                                """
                                Address
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: ipv4_address
                                
                                	IPV4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPV6 Address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-iarm-v4-oper'
                                _revision = '2016-12-19'

                                def __init__(self):
                                    self.parent = None
                                    self.afi = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.afi is not None:
                                        return True

                                    if self.ipv4_address is not None:
                                        return True

                                    if self.ipv6_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                                    return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None and self.address._has_data():
                                    return True

                                if self.is_prefix_sid is not None:
                                    return True

                                if self.is_primary is not None:
                                    return True

                                if self.is_tentative is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.producer is not None:
                                    return True

                                if self.route_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                                return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface is None:
                                raise YPYModelError('Key property interface is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:interface[Cisco-IOS-XR-ip-iarm-v4-oper:interface = ' + str(self.interface) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                return True

                            if self.address is not None:
                                for child_ref in self.address:
                                    if child_ref._has_data():
                                        return True

                            if self.referenced_interface is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                            return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-v4-oper:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                        return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:addresses/Cisco-IOS-XR-ip-iarm-v4-oper:vrfs/Cisco-IOS-XR-ip-iarm-v4-oper:vrf[Cisco-IOS-XR-ip-iarm-v4-oper:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    if self.networks is not None and self.networks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                    return meta._meta_table['Ipv4Arm.Addresses.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:addresses/Cisco-IOS-XR-ip-iarm-v4-oper:vrfs'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                return meta._meta_table['Ipv4Arm.Addresses.Vrfs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:addresses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vrfs is not None and self.vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
            return meta._meta_table['Ipv4Arm.Addresses']['meta_info']


    class Summary(object):
        """
        IPv4 ARM summary information
        
        .. attribute:: address_conflict_count
        
        	Number of address conflicts
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: db_master_version
        
        	IP\-ARM DB master version
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: producer_count
        
        	Number of producers
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: unnumbered_conflict_count
        
        	Number of unnumbered interface conflicts
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: vrf_count
        
        	Number of known VRFs
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.address_conflict_count = None
            self.db_master_version = None
            self.producer_count = None
            self.unnumbered_conflict_count = None
            self.vrf_count = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.address_conflict_count is not None:
                return True

            if self.db_master_version is not None:
                return True

            if self.producer_count is not None:
                return True

            if self.unnumbered_conflict_count is not None:
                return True

            if self.vrf_count is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
            return meta._meta_table['Ipv4Arm.Summary']['meta_info']


    class VrfSummaries(object):
        """
        IPv4 ARM VRFs summary information
        
        .. attribute:: vrf_summary
        
        	IPv4 ARM VRF summary information
        	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v4_oper.Ipv4Arm.VrfSummaries.VrfSummary>`
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.vrf_summary = YList()
            self.vrf_summary.parent = self
            self.vrf_summary.name = 'vrf_summary'


        class VrfSummary(object):
            """
            IPv4 ARM VRF summary information
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            .. attribute:: vrf_id
            
            	VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'ip-iarm-v4-oper'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.vrf_id = None
                self.vrf_name_xr = None

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:vrf-summaries/Cisco-IOS-XR-ip-iarm-v4-oper:vrf-summary[Cisco-IOS-XR-ip-iarm-v4-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.vrf_id is not None:
                    return True

                if self.vrf_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
                return meta._meta_table['Ipv4Arm.VrfSummaries.VrfSummary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:vrf-summaries'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vrf_summary is not None:
                for child_ref in self.vrf_summary:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
            return meta._meta_table['Ipv4Arm.VrfSummaries']['meta_info']


    class RouterId(object):
        """
        IPv4 ARM Router ID information
        
        .. attribute:: interface_name
        
        	Interface name
        	**type**\:  str
        
        .. attribute:: router_id
        
        	Router ID
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vrf_id
        
        	VRF ID
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\:  str
        
        

        """

        _prefix = 'ip-iarm-v4-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.interface_name = None
            self.router_id = None
            self.vrf_id = None
            self.vrf_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm/Cisco-IOS-XR-ip-iarm-v4-oper:router-id'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_name is not None:
                return True

            if self.router_id is not None:
                return True

            if self.vrf_id is not None:
                return True

            if self.vrf_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
            return meta._meta_table['Ipv4Arm.RouterId']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-iarm-v4-oper:ipv4arm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.addresses is not None and self.addresses._has_data():
            return True

        if self.multicast_host_interface is not None:
            return True

        if self.router_id is not None and self.router_id._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        if self.vrf_summaries is not None and self.vrf_summaries._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iarm_v4_oper as meta
        return meta._meta_table['Ipv4Arm']['meta_info']


