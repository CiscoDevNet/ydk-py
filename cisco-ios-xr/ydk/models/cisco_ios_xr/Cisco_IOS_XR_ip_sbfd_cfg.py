""" Cisco_IOS_XR_ip_sbfd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-sbfd package configuration.

This module contains definitions
for the following management objects\:
  sbfd\: SBFD Configuration ,Seamless\-BFD is method for detecting
    faultsbetween two different nodes in a network

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Sbfd(object):
    """
    SBFD Configuration ,Seamless\-BFD is method for
    detecting faultsbetween two different nodes in a
    network
    
    .. attribute:: local_discriminator
    
    	Configure local discriminator
    	**type**\:   :py:class:`LocalDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator>`
    
    .. attribute:: remote_target
    
    	configure remote target
    	**type**\:   :py:class:`RemoteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget>`
    
    

    """

    _prefix = 'ip-sbfd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.local_discriminator = Sbfd.LocalDiscriminator()
        self.local_discriminator.parent = self
        self.remote_target = Sbfd.RemoteTarget()
        self.remote_target.parent = self


    class RemoteTarget(object):
        """
        configure remote target
        
        .. attribute:: ipv4_addresses
        
        	ipv4 address as target
        	**type**\:   :py:class:`Ipv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses>`
        
        .. attribute:: ipv6_addresses
        
        	ipv6 address as target
        	**type**\:   :py:class:`Ipv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses>`
        
        

        """

        _prefix = 'ip-sbfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ipv4_addresses = Sbfd.RemoteTarget.Ipv4Addresses()
            self.ipv4_addresses.parent = self
            self.ipv6_addresses = Sbfd.RemoteTarget.Ipv6Addresses()
            self.ipv6_addresses.parent = self


        class Ipv4Addresses(object):
            """
            ipv4 address as target
            
            .. attribute:: ipv4_address
            
            	IP Address Value for RemoteDiscriminatorTable
            	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipv4_address = YList()
                self.ipv4_address.parent = self
                self.ipv4_address.name = 'ipv4_address'


            class Ipv4Address(object):
                """
                IP Address Value for RemoteDiscriminatorTable
                
                .. attribute:: address  <key>
                
                	 IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_discriminator
                
                	Remote Discriminator value
                	**type**\: list of    :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.remote_discriminator = YList()
                    self.remote_discriminator.parent = self
                    self.remote_discriminator.name = 'remote_discriminator'


                class RemoteDiscriminator(object):
                    """
                    Remote Discriminator value
                    
                    .. attribute:: remote_discriminator  <key>
                    
                    	Remote Discriminator Value
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'ip-sbfd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.remote_discriminator = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.remote_discriminator is None:
                            raise YPYModelError('Key property remote_discriminator is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-sbfd-cfg:remote-discriminator[Cisco-IOS-XR-ip-sbfd-cfg:remote-discriminator = ' + str(self.remote_discriminator) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.remote_discriminator is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                        return meta._meta_table['Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator']['meta_info']

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')

                    return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:remote-target/Cisco-IOS-XR-ip-sbfd-cfg:ipv4-addresses/Cisco-IOS-XR-ip-sbfd-cfg:ipv4-address[Cisco-IOS-XR-ip-sbfd-cfg:address = ' + str(self.address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.remote_discriminator is not None:
                        for child_ref in self.remote_discriminator:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                    return meta._meta_table['Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:remote-target/Cisco-IOS-XR-ip-sbfd-cfg:ipv4-addresses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv4_address is not None:
                    for child_ref in self.ipv4_address:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                return meta._meta_table['Sbfd.RemoteTarget.Ipv4Addresses']['meta_info']


        class Ipv6Addresses(object):
            """
            ipv6 address as target
            
            .. attribute:: ipv6_address
            
            	IP Address Value for RemoteDiscriminatorTable
            	**type**\: list of    :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipv6_address = YList()
                self.ipv6_address.parent = self
                self.ipv6_address.name = 'ipv6_address'


            class Ipv6Address(object):
                """
                IP Address Value for RemoteDiscriminatorTable
                
                .. attribute:: address  <key>
                
                	 IPv6 adddress
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_discriminator
                
                	Remote Discriminator value
                	**type**\: list of    :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.remote_discriminator = YList()
                    self.remote_discriminator.parent = self
                    self.remote_discriminator.name = 'remote_discriminator'


                class RemoteDiscriminator(object):
                    """
                    Remote Discriminator value
                    
                    .. attribute:: remote_discriminator  <key>
                    
                    	Remote Discriminator Value
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'ip-sbfd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.remote_discriminator = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.remote_discriminator is None:
                            raise YPYModelError('Key property remote_discriminator is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-sbfd-cfg:remote-discriminator[Cisco-IOS-XR-ip-sbfd-cfg:remote-discriminator = ' + str(self.remote_discriminator) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.remote_discriminator is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                        return meta._meta_table['Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator']['meta_info']

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')

                    return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:remote-target/Cisco-IOS-XR-ip-sbfd-cfg:ipv6-addresses/Cisco-IOS-XR-ip-sbfd-cfg:ipv6-address[Cisco-IOS-XR-ip-sbfd-cfg:address = ' + str(self.address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.remote_discriminator is not None:
                        for child_ref in self.remote_discriminator:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                    return meta._meta_table['Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:remote-target/Cisco-IOS-XR-ip-sbfd-cfg:ipv6-addresses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv6_address is not None:
                    for child_ref in self.ipv6_address:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                return meta._meta_table['Sbfd.RemoteTarget.Ipv6Addresses']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:remote-target'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.ipv4_addresses is not None and self.ipv4_addresses._has_data():
                return True

            if self.ipv6_addresses is not None and self.ipv6_addresses._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
            return meta._meta_table['Sbfd.RemoteTarget']['meta_info']


    class LocalDiscriminator(object):
        """
        Configure local discriminator
        
        .. attribute:: dynamic_discriminators
        
        	Configure local discriminator dynamically
        	**type**\:   :py:class:`DynamicDiscriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.DynamicDiscriminators>`
        
        .. attribute:: intf_discriminators
        
        	Configure local discriminator from interface address
        	**type**\:   :py:class:`IntfDiscriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.IntfDiscriminators>`
        
        .. attribute:: ipv4_discriminators
        
        	Configure local discriminator as an ipv4 address
        	**type**\:   :py:class:`Ipv4Discriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Ipv4Discriminators>`
        
        .. attribute:: val32_discriminators
        
        	Configure local discriminator as an integer
        	**type**\:   :py:class:`Val32Discriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Val32Discriminators>`
        
        

        """

        _prefix = 'ip-sbfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.dynamic_discriminators = Sbfd.LocalDiscriminator.DynamicDiscriminators()
            self.dynamic_discriminators.parent = self
            self.intf_discriminators = Sbfd.LocalDiscriminator.IntfDiscriminators()
            self.intf_discriminators.parent = self
            self.ipv4_discriminators = Sbfd.LocalDiscriminator.Ipv4Discriminators()
            self.ipv4_discriminators.parent = self
            self.val32_discriminators = Sbfd.LocalDiscriminator.Val32Discriminators()
            self.val32_discriminators.parent = self


        class IntfDiscriminators(object):
            """
            Configure local discriminator from interface
            address
            
            .. attribute:: intf_discriminator
            
            	interface address as discriminator
            	**type**\: list of    :py:class:`IntfDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.intf_discriminator = YList()
                self.intf_discriminator.parent = self
                self.intf_discriminator.name = 'intf_discriminator'


            class IntfDiscriminator(object):
                """
                interface address as discriminator
                
                .. attribute:: interface_name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:intf-discriminators/Cisco-IOS-XR-ip-sbfd-cfg:intf-discriminator[Cisco-IOS-XR-ip-sbfd-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                    return meta._meta_table['Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:intf-discriminators'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.intf_discriminator is not None:
                    for child_ref in self.intf_discriminator:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                return meta._meta_table['Sbfd.LocalDiscriminator.IntfDiscriminators']['meta_info']


        class DynamicDiscriminators(object):
            """
            Configure local discriminator dynamically
            
            .. attribute:: dynamic_discriminator
            
            	Local discriminator value
            	**type**\: list of    :py:class:`DynamicDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dynamic_discriminator = YList()
                self.dynamic_discriminator.parent = self
                self.dynamic_discriminator.name = 'dynamic_discriminator'


            class DynamicDiscriminator(object):
                """
                Local discriminator value
                
                .. attribute:: discriminator  <key>
                
                	Dynamic discriminator value
                	**type**\:  int
                
                	**range:** 0..1
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.discriminator = None

                @property
                def _common_path(self):
                    if self.discriminator is None:
                        raise YPYModelError('Key property discriminator is None')

                    return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:dynamic-discriminators/Cisco-IOS-XR-ip-sbfd-cfg:dynamic-discriminator[Cisco-IOS-XR-ip-sbfd-cfg:discriminator = ' + str(self.discriminator) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.discriminator is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                    return meta._meta_table['Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:dynamic-discriminators'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dynamic_discriminator is not None:
                    for child_ref in self.dynamic_discriminator:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                return meta._meta_table['Sbfd.LocalDiscriminator.DynamicDiscriminators']['meta_info']


        class Ipv4Discriminators(object):
            """
            Configure local discriminator as an ipv4
            address
            
            .. attribute:: ipv4_discriminator
            
            	ipv4 address as discriminator
            	**type**\: list of    :py:class:`Ipv4Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipv4_discriminator = YList()
                self.ipv4_discriminator.parent = self
                self.ipv4_discriminator.name = 'ipv4_discriminator'


            class Ipv4Discriminator(object):
                """
                ipv4 address as discriminator
                
                .. attribute:: address  <key>
                
                	 IPv4 address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')

                    return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:ipv4-discriminators/Cisco-IOS-XR-ip-sbfd-cfg:ipv4-discriminator[Cisco-IOS-XR-ip-sbfd-cfg:address = ' + str(self.address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                    return meta._meta_table['Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:ipv4-discriminators'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv4_discriminator is not None:
                    for child_ref in self.ipv4_discriminator:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                return meta._meta_table['Sbfd.LocalDiscriminator.Ipv4Discriminators']['meta_info']


        class Val32Discriminators(object):
            """
            Configure local discriminator as an integer
            
            .. attribute:: val32_discriminator
            
            	Local discriminator value
            	**type**\: list of    :py:class:`Val32Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.val32_discriminator = YList()
                self.val32_discriminator.parent = self
                self.val32_discriminator.name = 'val32_discriminator'


            class Val32Discriminator(object):
                """
                Local discriminator value
                
                .. attribute:: discriminator  <key>
                
                	Local discriminator value
                	**type**\:  int
                
                	**range:** 1..4294967295
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.discriminator = None

                @property
                def _common_path(self):
                    if self.discriminator is None:
                        raise YPYModelError('Key property discriminator is None')

                    return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:val32-discriminators/Cisco-IOS-XR-ip-sbfd-cfg:val32-discriminator[Cisco-IOS-XR-ip-sbfd-cfg:discriminator = ' + str(self.discriminator) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.discriminator is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                    return meta._meta_table['Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator/Cisco-IOS-XR-ip-sbfd-cfg:val32-discriminators'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.val32_discriminator is not None:
                    for child_ref in self.val32_discriminator:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
                return meta._meta_table['Sbfd.LocalDiscriminator.Val32Discriminators']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd/Cisco-IOS-XR-ip-sbfd-cfg:local-discriminator'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.dynamic_discriminators is not None and self.dynamic_discriminators._has_data():
                return True

            if self.intf_discriminators is not None and self.intf_discriminators._has_data():
                return True

            if self.ipv4_discriminators is not None and self.ipv4_discriminators._has_data():
                return True

            if self.val32_discriminators is not None and self.val32_discriminators._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
            return meta._meta_table['Sbfd.LocalDiscriminator']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-sbfd-cfg:sbfd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.local_discriminator is not None and self.local_discriminator._has_data():
            return True

        if self.remote_target is not None and self.remote_target._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_cfg as meta
        return meta._meta_table['Sbfd']['meta_info']


