""" Cisco_IOS_XR_ip_domain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package operational data.

This module contains definitions
for the following management objects\:
  ip\-domain\: Domain server and host data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ServerDomainLkup(Enum):
    """
    ServerDomainLkup

    Domain look up

    .. data:: static_mapping = 0

    	Static mapping

    .. data:: domain_service = 1

    	Domain service

    """

    static_mapping = Enum.YLeaf(0, "static-mapping")

    domain_service = Enum.YLeaf(1, "domain-service")



class HostAddressBase(Identity):
    """
    Base identity for Host\-address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(HostAddressBase, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper:Host-address-base")


class IpDomain(Entity):
    """
    Domain server and host data
    
    .. attribute:: vrfs
    
    	List of VRFs
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs>`
    
    

    """

    _prefix = 'ip-domain-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(IpDomain, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-domain"
        self.yang_parent_name = "Cisco-IOS-XR-ip-domain-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"vrfs" : ("vrfs", IpDomain.Vrfs)}
        self._child_list_classes = {}

        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-domain-oper:ip-domain"


    class Vrfs(Entity):
        """
        List of VRFs
        
        .. attribute:: vrf
        
        	VRF instance
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-domain-oper'
        _revision = '2017-05-01'

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
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-domain-oper:ip-domain/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IpDomain.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF instance
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: hosts
            
            	List of domain hosts
            	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts>`
            
            .. attribute:: server
            
            	Domain server data
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Server>`
            
            

            """

            _prefix = 'ip-domain-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(IpDomain.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"hosts" : ("hosts", IpDomain.Vrfs.Vrf.Hosts), "server" : ("server", IpDomain.Vrfs.Vrf.Server)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.hosts = IpDomain.Vrfs.Vrf.Hosts()
                self.hosts.parent = self
                self._children_name_map["hosts"] = "hosts"
                self._children_yang_names.add("hosts")

                self.server = IpDomain.Vrfs.Vrf.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-domain-oper:ip-domain/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IpDomain.Vrfs.Vrf, ['vrf_name'], name, value)


            class Hosts(Entity):
                """
                List of domain hosts
                
                .. attribute:: host
                
                	IP domain\-name, lookup style, nameservers for specific host
                	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host>`
                
                

                """

                _prefix = 'ip-domain-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Hosts, self).__init__()

                    self.yang_name = "hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"host" : ("host", IpDomain.Vrfs.Vrf.Hosts.Host)}

                    self.host = YList(self)
                    self._segment_path = lambda: "hosts"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Hosts, [], name, value)


                class Host(Entity):
                    """
                    IP domain\-name, lookup style, nameservers for
                    specific host
                    
                    .. attribute:: host_name  <key>
                    
                    	Hostname
                    	**type**\:  str
                    
                    .. attribute:: af_name
                    
                    	Address type
                    	**type**\:   :py:class:`HostAddressBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.HostAddressBase>`
                    
                    .. attribute:: age
                    
                    	Age in hours
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: hour
                    
                    .. attribute:: host_address
                    
                    	Host address list
                    	**type**\: list of    :py:class:`HostAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress>`
                    
                    .. attribute:: host_alias_list
                    
                    	Host alias
                    	**type**\:   :py:class:`HostAliasList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList>`
                    
                    

                    """

                    _prefix = 'ip-domain-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Hosts.Host, self).__init__()

                        self.yang_name = "host"
                        self.yang_parent_name = "hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"host-alias-list" : ("host_alias_list", IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList)}
                        self._child_list_classes = {"host-address" : ("host_address", IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress)}

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.af_name = YLeaf(YType.identityref, "af-name")

                        self.age = YLeaf(YType.uint16, "age")

                        self.host_alias_list = IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList()
                        self.host_alias_list.parent = self
                        self._children_name_map["host_alias_list"] = "host-alias-list"
                        self._children_yang_names.add("host-alias-list")

                        self.host_address = YList(self)
                        self._segment_path = lambda: "host" + "[host-name='" + self.host_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Hosts.Host, ['host_name', 'af_name', 'age'], name, value)


                    class HostAddress(Entity):
                        """
                        Host address list
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`HostAddressBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.HostAddressBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-domain-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress, self).__init__()

                            self.yang_name = "host-address"
                            self.yang_parent_name = "host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "host-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                    class HostAliasList(Entity):
                        """
                        Host alias
                        
                        .. attribute:: host_alias
                        
                        	Host alias list
                        	**type**\:  list of str
                        
                        	**length:** 0..256
                        
                        

                        """

                        _prefix = 'ip-domain-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList, self).__init__()

                            self.yang_name = "host-alias-list"
                            self.yang_parent_name = "host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.host_alias = YLeafList(YType.str, "host-alias")
                            self._segment_path = lambda: "host-alias-list"

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList, ['host_alias'], name, value)


            class Server(Entity):
                """
                Domain server data
                
                .. attribute:: domain
                
                	Domain list
                	**type**\:  list of str
                
                	**length:** 0..256
                
                .. attribute:: domain_lookup
                
                	Domain lookup
                	**type**\:   :py:class:`ServerDomainLkup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.ServerDomainLkup>`
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: server_address
                
                	Server address list
                	**type**\: list of    :py:class:`ServerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Server.ServerAddress>`
                
                

                """

                _prefix = 'ip-domain-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"server-address" : ("server_address", IpDomain.Vrfs.Vrf.Server.ServerAddress)}

                    self.domain = YLeafList(YType.str, "domain")

                    self.domain_lookup = YLeaf(YType.enumeration, "domain-lookup")

                    self.domain_name = YLeaf(YType.str, "domain-name")

                    self.server_address = YList(self)
                    self._segment_path = lambda: "server"

                def __setattr__(self, name, value):
                    self._perform_setattr(IpDomain.Vrfs.Vrf.Server, ['domain', 'domain_lookup', 'domain_name'], name, value)


                class ServerAddress(Entity):
                    """
                    Server address list
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`HostAddressBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.HostAddressBase>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Server.ServerAddress, self).__init__()

                        self.yang_name = "server-address"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.identityref, "af-name")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                        self._segment_path = lambda: "server-address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpDomain.Vrfs.Vrf.Server.ServerAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)

    def clone_ptr(self):
        self._top_entity = IpDomain()
        return self._top_entity

class Ipv4(Identity):
    """
    IPv4 family address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv4, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper:ipv4")


class Ipv6(Identity):
    """
    IPv6 family address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv6, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper:ipv6")


