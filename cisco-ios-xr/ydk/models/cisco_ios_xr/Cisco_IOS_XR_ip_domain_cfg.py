""" Cisco_IOS_XR_ip_domain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package configuration.

This module contains definitions
for the following management objects\:
  ip\-domain\: IP domain configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IpDomain(object):
    """
    IP domain configuration
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs>`
    
    

    """

    _prefix = 'ip-domain-cfg'
    _revision = '2015-05-13'

    def __init__(self):
        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF specific data
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-domain-cfg'
        _revision = '2015-05-13'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF specific data
            
            .. attribute:: vrf_name  <key>
            
            	Name of the VRF instance
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4_hosts
            
            	IPv4 host
            	**type**\:   :py:class:`Ipv4Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv4Hosts>`
            
            .. attribute:: ipv6_hosts
            
            	IPv6 host
            	**type**\:   :py:class:`Ipv6Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv6Hosts>`
            
            .. attribute:: lists
            
            	Domain names to complete unqualified host names
            	**type**\:   :py:class:`Lists <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Lists>`
            
            .. attribute:: lookup
            
            	Disable Domain Name System hostname translation
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: multicast_domain
            
            	Default multicast domain name
            	**type**\:  str
            
            .. attribute:: name
            
            	Default domain name
            	**type**\:  str
            
            .. attribute:: servers
            
            	Name server addresses
            	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Servers>`
            
            .. attribute:: source_interface
            
            	Specify interface for source address in connections
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'ip-domain-cfg'
            _revision = '2015-05-13'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.ipv4_hosts = IpDomain.Vrfs.Vrf.Ipv4Hosts()
                self.ipv4_hosts.parent = self
                self.ipv6_hosts = IpDomain.Vrfs.Vrf.Ipv6Hosts()
                self.ipv6_hosts.parent = self
                self.lists = IpDomain.Vrfs.Vrf.Lists()
                self.lists.parent = self
                self.lookup = None
                self.multicast_domain = None
                self.name = None
                self.servers = IpDomain.Vrfs.Vrf.Servers()
                self.servers.parent = self
                self.source_interface = None


            class Ipv6Hosts(object):
                """
                IPv6 host
                
                .. attribute:: ipv6_host
                
                	Host name and up to 4 host IPv6 addresses
                	**type**\: list of    :py:class:`Ipv6Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    self.parent = None
                    self.ipv6_host = YList()
                    self.ipv6_host.parent = self
                    self.ipv6_host.name = 'ipv6_host'


                class Ipv6Host(object):
                    """
                    Host name and up to 4 host IPv6 addresses
                    
                    .. attribute:: host_name  <key>
                    
                    	A hostname
                    	**type**\:  str
                    
                    .. attribute:: address
                    
                    	Host IPv6 addresses
                    	**type**\:  list of str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2015-05-13'

                    def __init__(self):
                        self.parent = None
                        self.host_name = None
                        self.address = YLeafList()
                        self.address.parent = self
                        self.address.name = 'address'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.host_name is None:
                            raise YPYModelError('Key property host_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:ipv6-host[Cisco-IOS-XR-ip-domain-cfg:host-name = ' + str(self.host_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.host_name is not None:
                            return True

                        if self.address is not None:
                            for child in self.address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                        return meta._meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:ipv6-hosts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipv6_host is not None:
                        for child_ref in self.ipv6_host:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                    return meta._meta_table['IpDomain.Vrfs.Vrf.Ipv6Hosts']['meta_info']


            class Servers(object):
                """
                Name server addresses
                
                .. attribute:: server
                
                	Name server address
                	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Servers.Server>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    self.parent = None
                    self.server = YList()
                    self.server.parent = self
                    self.server.name = 'server'


                class Server(object):
                    """
                    Name server address
                    
                    .. attribute:: order  <key>
                    
                    	This is used to sort the servers in the order of precedence
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: server_address  <key>
                    
                    	A name server address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2015-05-13'

                    def __init__(self):
                        self.parent = None
                        self.order = None
                        self.server_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.order is None:
                            raise YPYModelError('Key property order is None')
                        if self.server_address is None:
                            raise YPYModelError('Key property server_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:server[Cisco-IOS-XR-ip-domain-cfg:order = ' + str(self.order) + '][Cisco-IOS-XR-ip-domain-cfg:server-address = ' + str(self.server_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.order is not None:
                            return True

                        if self.server_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                        return meta._meta_table['IpDomain.Vrfs.Vrf.Servers.Server']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:servers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.server is not None:
                        for child_ref in self.server:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                    return meta._meta_table['IpDomain.Vrfs.Vrf.Servers']['meta_info']


            class Lists(object):
                """
                Domain names to complete unqualified host
                names
                
                .. attribute:: list
                
                	Domain name to complete unqualified host names
                	**type**\: list of    :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Lists.List>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    self.parent = None
                    self.list = YList()
                    self.list.parent = self
                    self.list.name = 'list'


                class List(object):
                    """
                    Domain name to complete unqualified host
                    names
                    
                    .. attribute:: order  <key>
                    
                    	This is used to sort the names in the order of precedence
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: list_name  <key>
                    
                    	A domain name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2015-05-13'

                    def __init__(self):
                        self.parent = None
                        self.order = None
                        self.list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.order is None:
                            raise YPYModelError('Key property order is None')
                        if self.list_name is None:
                            raise YPYModelError('Key property list_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:list[Cisco-IOS-XR-ip-domain-cfg:order = ' + str(self.order) + '][Cisco-IOS-XR-ip-domain-cfg:list-name = ' + str(self.list_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.order is not None:
                            return True

                        if self.list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                        return meta._meta_table['IpDomain.Vrfs.Vrf.Lists.List']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:lists'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.list is not None:
                        for child_ref in self.list:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                    return meta._meta_table['IpDomain.Vrfs.Vrf.Lists']['meta_info']


            class Ipv4Hosts(object):
                """
                IPv4 host
                
                .. attribute:: ipv4_host
                
                	Host name and up to 8 host IPv4 addresses
                	**type**\: list of    :py:class:`Ipv4Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    self.parent = None
                    self.ipv4_host = YList()
                    self.ipv4_host.parent = self
                    self.ipv4_host.name = 'ipv4_host'


                class Ipv4Host(object):
                    """
                    Host name and up to 8 host IPv4 addresses
                    
                    .. attribute:: host_name  <key>
                    
                    	A hostname
                    	**type**\:  str
                    
                    .. attribute:: address
                    
                    	Host IPv4 addresses
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2015-05-13'

                    def __init__(self):
                        self.parent = None
                        self.host_name = None
                        self.address = YLeafList()
                        self.address.parent = self
                        self.address.name = 'address'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.host_name is None:
                            raise YPYModelError('Key property host_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:ipv4-host[Cisco-IOS-XR-ip-domain-cfg:host-name = ' + str(self.host_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.host_name is not None:
                            return True

                        if self.address is not None:
                            for child in self.address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                        return meta._meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-cfg:ipv4-hosts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipv4_host is not None:
                        for child_ref in self.ipv4_host:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                    return meta._meta_table['IpDomain.Vrfs.Vrf.Ipv4Hosts']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-domain-cfg:ip-domain/Cisco-IOS-XR-ip-domain-cfg:vrfs/Cisco-IOS-XR-ip-domain-cfg:vrf[Cisco-IOS-XR-ip-domain-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.ipv4_hosts is not None and self.ipv4_hosts._has_data():
                    return True

                if self.ipv6_hosts is not None and self.ipv6_hosts._has_data():
                    return True

                if self.lists is not None and self.lists._has_data():
                    return True

                if self.lookup is not None:
                    return True

                if self.multicast_domain is not None:
                    return True

                if self.name is not None:
                    return True

                if self.servers is not None and self.servers._has_data():
                    return True

                if self.source_interface is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
                return meta._meta_table['IpDomain.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-domain-cfg:ip-domain/Cisco-IOS-XR-ip-domain-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
            return meta._meta_table['IpDomain.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-domain-cfg:ip-domain'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_domain_cfg as meta
        return meta._meta_table['IpDomain']['meta_info']


