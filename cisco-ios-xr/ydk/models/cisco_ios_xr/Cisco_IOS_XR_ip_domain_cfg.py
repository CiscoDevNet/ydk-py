""" Cisco_IOS_XR_ip_domain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package configuration.

This module contains definitions
for the following management objects\:
  ip\-domain\: IP domain configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class IpDomain(Entity):
    """
    IP domain configuration
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs>`
    
    

    """

    _prefix = 'ip-domain-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(IpDomain, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-domain"
        self.yang_parent_name = "Cisco-IOS-XR-ip-domain-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", IpDomain.Vrfs))])
        self._leafs = OrderedDict()

        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-domain-cfg:ip-domain"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IpDomain, [], name, value)


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF specific data
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-domain-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(IpDomain.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ip-domain"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", IpDomain.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-domain-cfg:ip-domain/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpDomain.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF specific data
            
            .. attribute:: vrf_name  (key)
            
            	Name of the VRF instance
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv6_hosts
            
            	IPv6 host
            	**type**\:  :py:class:`Ipv6Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv6Hosts>`
            
            .. attribute:: servers
            
            	Name server addresses
            	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Servers>`
            
            .. attribute:: lists
            
            	Domain names to complete unqualified host names
            	**type**\:  :py:class:`Lists <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Lists>`
            
            .. attribute:: ipv4_hosts
            
            	IPv4 host
            	**type**\:  :py:class:`Ipv4Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv4Hosts>`
            
            .. attribute:: lookup
            
            	Disable Domain Name System hostname translation
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: multicast_domain
            
            	Default multicast domain name
            	**type**\: str
            
            .. attribute:: source_interface
            
            	Specify interface for source address in connections
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: name
            
            	Default domain name
            	**type**\: str
            
            

            """

            _prefix = 'ip-domain-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(IpDomain.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("ipv6-hosts", ("ipv6_hosts", IpDomain.Vrfs.Vrf.Ipv6Hosts)), ("servers", ("servers", IpDomain.Vrfs.Vrf.Servers)), ("lists", ("lists", IpDomain.Vrfs.Vrf.Lists)), ("ipv4-hosts", ("ipv4_hosts", IpDomain.Vrfs.Vrf.Ipv4Hosts))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('lookup', (YLeaf(YType.empty, 'lookup'), ['Empty'])),
                    ('multicast_domain', (YLeaf(YType.str, 'multicast-domain'), ['str'])),
                    ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.vrf_name = None
                self.lookup = None
                self.multicast_domain = None
                self.source_interface = None
                self.name = None

                self.ipv6_hosts = IpDomain.Vrfs.Vrf.Ipv6Hosts()
                self.ipv6_hosts.parent = self
                self._children_name_map["ipv6_hosts"] = "ipv6-hosts"

                self.servers = IpDomain.Vrfs.Vrf.Servers()
                self.servers.parent = self
                self._children_name_map["servers"] = "servers"

                self.lists = IpDomain.Vrfs.Vrf.Lists()
                self.lists.parent = self
                self._children_name_map["lists"] = "lists"

                self.ipv4_hosts = IpDomain.Vrfs.Vrf.Ipv4Hosts()
                self.ipv4_hosts.parent = self
                self._children_name_map["ipv4_hosts"] = "ipv4-hosts"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-domain-cfg:ip-domain/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpDomain.Vrfs.Vrf, ['vrf_name', 'lookup', 'multicast_domain', 'source_interface', 'name'], name, value)


            class Ipv6Hosts(Entity):
                """
                IPv6 host
                
                .. attribute:: ipv6_host
                
                	Host name and up to 4 host IPv6 addresses
                	**type**\: list of  		 :py:class:`Ipv6Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Ipv6Hosts, self).__init__()

                    self.yang_name = "ipv6-hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv6-host", ("ipv6_host", IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host))])
                    self._leafs = OrderedDict()

                    self.ipv6_host = YList(self)
                    self._segment_path = lambda: "ipv6-hosts"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv6Hosts, [], name, value)


                class Ipv6Host(Entity):
                    """
                    Host name and up to 4 host IPv6 addresses
                    
                    .. attribute:: host_name  (key)
                    
                    	A hostname
                    	**type**\: str
                    
                    .. attribute:: address
                    
                    	Host IPv6 addresses
                    	**type**\: list of str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host, self).__init__()

                        self.yang_name = "ipv6-host"
                        self.yang_parent_name = "ipv6-hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['host_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                            ('address', (YLeafList(YType.str, 'address'), ['str'])),
                        ])
                        self.host_name = None
                        self.address = []
                        self._segment_path = lambda: "ipv6-host" + "[host-name='" + str(self.host_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host, ['host_name', 'address'], name, value)


            class Servers(Entity):
                """
                Name server addresses
                
                .. attribute:: server
                
                	Name server address
                	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Servers.Server>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Servers, self).__init__()

                    self.yang_name = "servers"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("server", ("server", IpDomain.Vrfs.Vrf.Servers.Server))])
                    self._leafs = OrderedDict()

                    self.server = YList(self)
                    self._segment_path = lambda: "servers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Servers, [], name, value)


                class Server(Entity):
                    """
                    Name server address
                    
                    .. attribute:: order  (key)
                    
                    	This is used to sort the servers in the order of precedence
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_address  (key)
                    
                    	A name server address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Servers.Server, self).__init__()

                        self.yang_name = "server"
                        self.yang_parent_name = "servers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['order','server_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('order', (YLeaf(YType.uint32, 'order'), ['int'])),
                            ('server_address', (YLeaf(YType.str, 'server-address'), ['str','str'])),
                        ])
                        self.order = None
                        self.server_address = None
                        self._segment_path = lambda: "server" + "[order='" + str(self.order) + "']" + "[server-address='" + str(self.server_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Servers.Server, ['order', 'server_address'], name, value)


            class Lists(Entity):
                """
                Domain names to complete unqualified host
                names
                
                .. attribute:: list
                
                	Domain name to complete unqualified host names
                	**type**\: list of  		 :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Lists.List>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Lists, self).__init__()

                    self.yang_name = "lists"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("list", ("list", IpDomain.Vrfs.Vrf.Lists.List))])
                    self._leafs = OrderedDict()

                    self.list = YList(self)
                    self._segment_path = lambda: "lists"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Lists, [], name, value)


                class List(Entity):
                    """
                    Domain name to complete unqualified host
                    names
                    
                    .. attribute:: order  (key)
                    
                    	This is used to sort the names in the order of precedence
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: list_name  (key)
                    
                    	A domain name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Lists.List, self).__init__()

                        self.yang_name = "list"
                        self.yang_parent_name = "lists"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['order','list_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('order', (YLeaf(YType.uint32, 'order'), ['int'])),
                            ('list_name', (YLeaf(YType.str, 'list-name'), ['str'])),
                        ])
                        self.order = None
                        self.list_name = None
                        self._segment_path = lambda: "list" + "[order='" + str(self.order) + "']" + "[list-name='" + str(self.list_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Lists.List, ['order', 'list_name'], name, value)


            class Ipv4Hosts(Entity):
                """
                IPv4 host
                
                .. attribute:: ipv4_host
                
                	Host name and up to 8 host IPv4 addresses
                	**type**\: list of  		 :py:class:`Ipv4Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Ipv4Hosts, self).__init__()

                    self.yang_name = "ipv4-hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv4-host", ("ipv4_host", IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host))])
                    self._leafs = OrderedDict()

                    self.ipv4_host = YList(self)
                    self._segment_path = lambda: "ipv4-hosts"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv4Hosts, [], name, value)


                class Ipv4Host(Entity):
                    """
                    Host name and up to 8 host IPv4 addresses
                    
                    .. attribute:: host_name  (key)
                    
                    	A hostname
                    	**type**\: str
                    
                    .. attribute:: address
                    
                    	Host IPv4 addresses
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host, self).__init__()

                        self.yang_name = "ipv4-host"
                        self.yang_parent_name = "ipv4-hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['host_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                            ('address', (YLeafList(YType.str, 'address'), ['str'])),
                        ])
                        self.host_name = None
                        self.address = []
                        self._segment_path = lambda: "ipv4-host" + "[host-name='" + str(self.host_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host, ['host_name', 'address'], name, value)

    def clone_ptr(self):
        self._top_entity = IpDomain()
        return self._top_entity

