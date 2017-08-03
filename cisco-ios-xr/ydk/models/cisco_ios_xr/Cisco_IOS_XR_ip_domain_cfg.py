""" Cisco_IOS_XR_ip_domain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package configuration.

This module contains definitions
for the following management objects\:
  ip\-domain\: IP domain configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


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

            self.vrf = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpDomain.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpDomain.Vrfs, self).__setattr__(name, value)


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
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'ip-domain-cfg'
            _revision = '2015-05-13'

            def __init__(self):
                super(IpDomain.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "lookup",
                                "multicast_domain",
                                "name",
                                "source_interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpDomain.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpDomain.Vrfs.Vrf, self).__setattr__(name, value)


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

                    self.ipv6_host = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpDomain.Vrfs.Vrf.Ipv6Hosts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpDomain.Vrfs.Vrf.Ipv6Hosts, self).__setattr__(name, value)


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

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.address = YLeafList(YType.str, "address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("host_name",
                                        "address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.host_name.is_set

                    def has_operation(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.host_name.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-host" + "[host-name='" + self.host_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host_name.get_name_leafdata())

                        leaf_name_data.extend(self.address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host-name" or name == "address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "host-name"):
                            self.host_name = value
                            self.host_name.value_namespace = name_space
                            self.host_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "address"):
                            self.address.append(value)

                def has_data(self):
                    for c in self.ipv6_host:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv6_host:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6-hosts" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipv6-host"):
                        for c in self.ipv6_host:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpDomain.Vrfs.Vrf.Ipv6Hosts.Ipv6Host()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_host.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv6-host"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.server = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpDomain.Vrfs.Vrf.Servers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpDomain.Vrfs.Vrf.Servers, self).__setattr__(name, value)


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

                        self.order = YLeaf(YType.int32, "order")

                        self.server_address = YLeaf(YType.str, "server-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("order",
                                        "server_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpDomain.Vrfs.Vrf.Servers.Server, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpDomain.Vrfs.Vrf.Servers.Server, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.order.is_set or
                            self.server_address.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.order.yfilter != YFilter.not_set or
                            self.server_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server" + "[order='" + self.order.get() + "']" + "[server-address='" + self.server_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.order.is_set or self.order.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.order.get_name_leafdata())
                        if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "order" or name == "server-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "order"):
                            self.order = value
                            self.order.value_namespace = name_space
                            self.order.value_namespace_prefix = name_space_prefix
                        if(value_path == "server-address"):
                            self.server_address = value
                            self.server_address.value_namespace = name_space
                            self.server_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.server:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.server:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "servers" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "server"):
                        for c in self.server:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpDomain.Vrfs.Vrf.Servers.Server()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.server.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "server"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.list = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpDomain.Vrfs.Vrf.Lists, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpDomain.Vrfs.Vrf.Lists, self).__setattr__(name, value)


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

                        self.order = YLeaf(YType.int32, "order")

                        self.list_name = YLeaf(YType.str, "list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("order",
                                        "list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpDomain.Vrfs.Vrf.Lists.List, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpDomain.Vrfs.Vrf.Lists.List, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.order.is_set or
                            self.list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.order.yfilter != YFilter.not_set or
                            self.list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "list" + "[order='" + self.order.get() + "']" + "[list-name='" + self.list_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.order.is_set or self.order.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.order.get_name_leafdata())
                        if (self.list_name.is_set or self.list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "order" or name == "list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "order"):
                            self.order = value
                            self.order.value_namespace = name_space
                            self.order.value_namespace_prefix = name_space_prefix
                        if(value_path == "list-name"):
                            self.list_name = value
                            self.list_name.value_namespace = name_space
                            self.list_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.list:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.list:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lists" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "list"):
                        for c in self.list:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpDomain.Vrfs.Vrf.Lists.List()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.list.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "list"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.ipv4_host = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpDomain.Vrfs.Vrf.Ipv4Hosts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpDomain.Vrfs.Vrf.Ipv4Hosts, self).__setattr__(name, value)


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

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.address = YLeafList(YType.str, "address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("host_name",
                                        "address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.host_name.is_set

                    def has_operation(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.host_name.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-host" + "[host-name='" + self.host_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.host_name.get_name_leafdata())

                        leaf_name_data.extend(self.address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host-name" or name == "address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "host-name"):
                            self.host_name = value
                            self.host_name.value_namespace = name_space
                            self.host_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "address"):
                            self.address.append(value)

                def has_data(self):
                    for c in self.ipv4_host:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv4_host:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-hosts" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipv4-host"):
                        for c in self.ipv4_host:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpDomain.Vrfs.Vrf.Ipv4Hosts.Ipv4Host()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv4_host.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-host"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.lookup.is_set or
                    self.multicast_domain.is_set or
                    self.name.is_set or
                    self.source_interface.is_set or
                    (self.ipv4_hosts is not None and self.ipv4_hosts.has_data()) or
                    (self.ipv6_hosts is not None and self.ipv6_hosts.has_data()) or
                    (self.lists is not None and self.lists.has_data()) or
                    (self.servers is not None and self.servers.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.lookup.yfilter != YFilter.not_set or
                    self.multicast_domain.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.source_interface.yfilter != YFilter.not_set or
                    (self.ipv4_hosts is not None and self.ipv4_hosts.has_operation()) or
                    (self.ipv6_hosts is not None and self.ipv6_hosts.has_operation()) or
                    (self.lists is not None and self.lists.has_operation()) or
                    (self.servers is not None and self.servers.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-domain-cfg:ip-domain/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.lookup.is_set or self.lookup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lookup.get_name_leafdata())
                if (self.multicast_domain.is_set or self.multicast_domain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multicast_domain.get_name_leafdata())
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-hosts"):
                    if (self.ipv4_hosts is None):
                        self.ipv4_hosts = IpDomain.Vrfs.Vrf.Ipv4Hosts()
                        self.ipv4_hosts.parent = self
                        self._children_name_map["ipv4_hosts"] = "ipv4-hosts"
                    return self.ipv4_hosts

                if (child_yang_name == "ipv6-hosts"):
                    if (self.ipv6_hosts is None):
                        self.ipv6_hosts = IpDomain.Vrfs.Vrf.Ipv6Hosts()
                        self.ipv6_hosts.parent = self
                        self._children_name_map["ipv6_hosts"] = "ipv6-hosts"
                    return self.ipv6_hosts

                if (child_yang_name == "lists"):
                    if (self.lists is None):
                        self.lists = IpDomain.Vrfs.Vrf.Lists()
                        self.lists.parent = self
                        self._children_name_map["lists"] = "lists"
                    return self.lists

                if (child_yang_name == "servers"):
                    if (self.servers is None):
                        self.servers = IpDomain.Vrfs.Vrf.Servers()
                        self.servers.parent = self
                        self._children_name_map["servers"] = "servers"
                    return self.servers

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-hosts" or name == "ipv6-hosts" or name == "lists" or name == "servers" or name == "vrf-name" or name == "lookup" or name == "multicast-domain" or name == "name" or name == "source-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "lookup"):
                    self.lookup = value
                    self.lookup.value_namespace = name_space
                    self.lookup.value_namespace_prefix = name_space_prefix
                if(value_path == "multicast-domain"):
                    self.multicast_domain = value
                    self.multicast_domain.value_namespace = name_space
                    self.multicast_domain.value_namespace_prefix = name_space_prefix
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface"):
                    self.source_interface = value
                    self.source_interface.value_namespace = name_space
                    self.source_interface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-domain-cfg:ip-domain/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpDomain.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.vrfs is not None and self.vrfs.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-domain-cfg:ip-domain" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = IpDomain.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpDomain()
        return self._top_entity

