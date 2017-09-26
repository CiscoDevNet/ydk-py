""" Cisco_IOS_XR_ip_domain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package configuration.

This module contains definitions
for the following management objects\:
  ip\-domain\: IP domain configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpDomain(Entity):
    """
    IP domain configuration
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs>`
    
    

    """

    _prefix = 'ip-domain-cfg'
    _revision = '2015-05-13'

    def __init__(self):
        super(IpDomain, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-domain"
        self.yang_parent_name = "Cisco-IOS-XR-ip-domain-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"vrfs" : ("vrfs", IpDomain.Vrfs)}
        self._child_list_classes = {}

        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-domain-cfg:ip-domain"


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF specific data
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-domain-cfg'
        _revision = '2015-05-13'

        def __init__(self):
            super(IpDomain.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ip-domain"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", IpDomain.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-domain-cfg:ip-domain/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IpDomain.Vrfs, [], name, value)


        class Vrf(Entity):
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
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            

            """

            _prefix = 'ip-domain-cfg'
            _revision = '2015-05-13'

            def __init__(self):
                super(IpDomain.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv4-hosts" : ("ipv4_hosts", IpDomain.Vrfs.Vrf.Ipv4Hosts), "ipv6-hosts" : ("ipv6_hosts", IpDomain.Vrfs.Vrf.Ipv6Hosts), "lists" : ("lists", IpDomain.Vrfs.Vrf.Lists), "servers" : ("servers", IpDomain.Vrfs.Vrf.Servers)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.lookup = YLeaf(YType.empty, "lookup")

                self.multicast_domain = YLeaf(YType.str, "multicast-domain")

                self.name = YLeaf(YType.str, "name")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.ipv4_hosts = IpDomain.Vrfs.Vrf.Ipv4Hosts()
                self.ipv4_hosts.parent = self
                self._children_name_map["ipv4_hosts"] = "ipv4-hosts"
                self._children_yang_names.add("ipv4-hosts")

                self.ipv6_hosts = IpDomain.Vrfs.Vrf.Ipv6Hosts()
                self.ipv6_hosts.parent = self
                self._children_name_map["ipv6_hosts"] = "ipv6-hosts"
                self._children_yang_names.add("ipv6-hosts")

                self.lists = IpDomain.Vrfs.Vrf.Lists()
                self.lists.parent = self
                self._children_name_map["lists"] = "lists"
                self._children_yang_names.add("lists")

                self.servers = IpDomain.Vrfs.Vrf.Servers()
                self.servers.parent = self
                self._children_name_map["servers"] = "servers"
                self._children_yang_names.add("servers")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-domain-cfg:ip-domain/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IpDomain.Vrfs.Vrf, ['vrf_name', 'lookup', 'multicast_domain', 'name', 'source_interface'], name, value)


            class Ipv4Hosts(Entity):
                """
                IPv4 host
                
                .. attribute:: ipv4_host
                
                	Host name and up to 8 host IPv4 addresses
                	**type**\: list of    :py:class:`Ipv4Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Ipv4Hosts, self).__init__()

                    self.yang_name = "ipv4-hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ipv4-host" : ("ipv4_host", IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host)}

                    self.ipv4_host = YList(self)
                    self._segment_path = lambda: "ipv4-hosts"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv4Hosts, [], name, value)


                class Ipv4Host(Entity):
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
                        super(IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host, self).__init__()

                        self.yang_name = "ipv4-host"
                        self.yang_parent_name = "ipv4-hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.address = YLeafList(YType.str, "address")
                        self._segment_path = lambda: "ipv4-host" + "[host-name='" + self.host_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host, ['host_name', 'address'], name, value)


            class Ipv6Hosts(Entity):
                """
                IPv6 host
                
                .. attribute:: ipv6_host
                
                	Host name and up to 4 host IPv6 addresses
                	**type**\: list of    :py:class:`Ipv6Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Ipv6Hosts, self).__init__()

                    self.yang_name = "ipv6-hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ipv6-host" : ("ipv6_host", IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host)}

                    self.ipv6_host = YList(self)
                    self._segment_path = lambda: "ipv6-hosts"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv6Hosts, [], name, value)


                class Ipv6Host(Entity):
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
                        super(IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host, self).__init__()

                        self.yang_name = "ipv6-host"
                        self.yang_parent_name = "ipv6-hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.address = YLeafList(YType.str, "address")
                        self._segment_path = lambda: "ipv6-host" + "[host-name='" + self.host_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host, ['host_name', 'address'], name, value)


            class Lists(Entity):
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
                    super(IpDomain.Vrfs.Vrf.Lists, self).__init__()

                    self.yang_name = "lists"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"list" : ("list", IpDomain.Vrfs.Vrf.Lists.List)}

                    self.list = YList(self)
                    self._segment_path = lambda: "lists"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Lists, [], name, value)


                class List(Entity):
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
                        super(IpDomain.Vrfs.Vrf.Lists.List, self).__init__()

                        self.yang_name = "list"
                        self.yang_parent_name = "lists"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.order = YLeaf(YType.int32, "order")

                        self.list_name = YLeaf(YType.str, "list-name")
                        self._segment_path = lambda: "list" + "[order='" + self.order.get() + "']" + "[list-name='" + self.list_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Lists.List, ['order', 'list_name'], name, value)


            class Servers(Entity):
                """
                Name server addresses
                
                .. attribute:: server
                
                	Name server address
                	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_cfg.IpDomain.Vrfs.Vrf.Servers.Server>`
                
                

                """

                _prefix = 'ip-domain-cfg'
                _revision = '2015-05-13'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Servers, self).__init__()

                    self.yang_name = "servers"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"server" : ("server", IpDomain.Vrfs.Vrf.Servers.Server)}

                    self.server = YList(self)
                    self._segment_path = lambda: "servers"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Servers, [], name, value)


                class Server(Entity):
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
                        super(IpDomain.Vrfs.Vrf.Servers.Server, self).__init__()

                        self.yang_name = "server"
                        self.yang_parent_name = "servers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.order = YLeaf(YType.int32, "order")

                        self.server_address = YLeaf(YType.str, "server-address")
                        self._segment_path = lambda: "server" + "[order='" + self.order.get() + "']" + "[server-address='" + self.server_address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Servers.Server, ['order', 'server_address'], name, value)

    def clone_ptr(self):
        self._top_entity = IpDomain()
        return self._top_entity

