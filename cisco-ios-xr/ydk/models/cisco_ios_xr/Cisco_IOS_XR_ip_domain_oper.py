""" Cisco_IOS_XR_ip_domain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package operational data.

This module contains definitions
for the following management objects\:
  ip\-domain\: Domain server and host data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2015-09-29'

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
    _revision = '2015-09-29'

    def __init__(self):
        super(IpDomain, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-domain"
        self.yang_parent_name = "Cisco-IOS-XR-ip-domain-oper"

        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class Vrfs(Entity):
        """
        List of VRFs
        
        .. attribute:: vrf
        
        	VRF instance
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-domain-oper'
        _revision = '2015-09-29'

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
            _revision = '2015-09-29'

            def __init__(self):
                super(IpDomain.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.hosts = IpDomain.Vrfs.Vrf.Hosts()
                self.hosts.parent = self
                self._children_name_map["hosts"] = "hosts"
                self._children_yang_names.add("hosts")

                self.server = IpDomain.Vrfs.Vrf.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
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
                _revision = '2015-09-29'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "vrf"

                    self.domain = YLeafList(YType.str, "domain")

                    self.domain_lookup = YLeaf(YType.enumeration, "domain-lookup")

                    self.domain_name = YLeaf(YType.str, "domain-name")

                    self.server_address = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("domain",
                                    "domain_lookup",
                                    "domain_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpDomain.Vrfs.Vrf.Server, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpDomain.Vrfs.Vrf.Server, self).__setattr__(name, value)


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
                    _revision = '2015-09-29'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Server.ServerAddress, self).__init__()

                        self.yang_name = "server-address"
                        self.yang_parent_name = "server"

                        self.af_name = YLeaf(YType.identityref, "af-name")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af_name",
                                        "ipv4_address",
                                        "ipv6_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpDomain.Vrfs.Vrf.Server.ServerAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpDomain.Vrfs.Vrf.Server.ServerAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.af_name.is_set or
                            self.ipv4_address.is_set or
                            self.ipv6_address.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.ipv4_address.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server-address" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-address"):
                            self.ipv4_address = value
                            self.ipv4_address.value_namespace = name_space
                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-address"):
                            self.ipv6_address = value
                            self.ipv6_address.value_namespace = name_space
                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.server_address:
                        if (c.has_data()):
                            return True
                    for leaf in self.domain.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.domain_lookup.is_set or
                        self.domain_name.is_set)

                def has_operation(self):
                    for c in self.server_address:
                        if (c.has_operation()):
                            return True
                    for leaf in self.domain.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.domain.yfilter != YFilter.not_set or
                        self.domain_lookup.yfilter != YFilter.not_set or
                        self.domain_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.domain_lookup.is_set or self.domain_lookup.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.domain_lookup.get_name_leafdata())
                    if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.domain_name.get_name_leafdata())

                    leaf_name_data.extend(self.domain.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "server-address"):
                        for c in self.server_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpDomain.Vrfs.Vrf.Server.ServerAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.server_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "server-address" or name == "domain" or name == "domain-lookup" or name == "domain-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "domain"):
                        self.domain.append(value)
                    if(value_path == "domain-lookup"):
                        self.domain_lookup = value
                        self.domain_lookup.value_namespace = name_space
                        self.domain_lookup.value_namespace_prefix = name_space_prefix
                    if(value_path == "domain-name"):
                        self.domain_name = value
                        self.domain_name.value_namespace = name_space
                        self.domain_name.value_namespace_prefix = name_space_prefix


            class Hosts(Entity):
                """
                List of domain hosts
                
                .. attribute:: host
                
                	IP domain\-name, lookup style, nameservers for specific host
                	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host>`
                
                

                """

                _prefix = 'ip-domain-oper'
                _revision = '2015-09-29'

                def __init__(self):
                    super(IpDomain.Vrfs.Vrf.Hosts, self).__init__()

                    self.yang_name = "hosts"
                    self.yang_parent_name = "vrf"

                    self.host = YList(self)

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
                                super(IpDomain.Vrfs.Vrf.Hosts, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpDomain.Vrfs.Vrf.Hosts, self).__setattr__(name, value)


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
                    _revision = '2015-09-29'

                    def __init__(self):
                        super(IpDomain.Vrfs.Vrf.Hosts.Host, self).__init__()

                        self.yang_name = "host"
                        self.yang_parent_name = "hosts"

                        self.host_name = YLeaf(YType.str, "host-name")

                        self.af_name = YLeaf(YType.identityref, "af-name")

                        self.age = YLeaf(YType.uint16, "age")

                        self.host_alias_list = IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList()
                        self.host_alias_list.parent = self
                        self._children_name_map["host_alias_list"] = "host-alias-list"
                        self._children_yang_names.add("host-alias-list")

                        self.host_address = YList(self)

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
                                        "af_name",
                                        "age") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpDomain.Vrfs.Vrf.Hosts.Host, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpDomain.Vrfs.Vrf.Hosts.Host, self).__setattr__(name, value)


                    class HostAliasList(Entity):
                        """
                        Host alias
                        
                        .. attribute:: host_alias
                        
                        	Host alias list
                        	**type**\:  list of str
                        
                        	**length:** 0..256
                        
                        

                        """

                        _prefix = 'ip-domain-oper'
                        _revision = '2015-09-29'

                        def __init__(self):
                            super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList, self).__init__()

                            self.yang_name = "host-alias-list"
                            self.yang_parent_name = "host"

                            self.host_alias = YLeafList(YType.str, "host-alias")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("host_alias") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.host_alias.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return False

                        def has_operation(self):
                            for leaf in self.host_alias.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.host_alias.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "host-alias-list" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            leaf_name_data.extend(self.host_alias.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "host-alias"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "host-alias"):
                                self.host_alias.append(value)


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
                        _revision = '2015-09-29'

                        def __init__(self):
                            super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress, self).__init__()

                            self.yang_name = "host-address"
                            self.yang_parent_name = "host"

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "host-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.host_address:
                            if (c.has_data()):
                                return True
                        return (
                            self.host_name.is_set or
                            self.af_name.is_set or
                            self.age.is_set or
                            (self.host_alias_list is not None and self.host_alias_list.has_data()))

                    def has_operation(self):
                        for c in self.host_address:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.host_name.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.age.yfilter != YFilter.not_set or
                            (self.host_alias_list is not None and self.host_alias_list.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "host" + "[host-name='" + self.host_name.get() + "']" + path_buffer

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
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.age.is_set or self.age.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.age.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "host-address"):
                            for c in self.host_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.host_address.append(c)
                            return c

                        if (child_yang_name == "host-alias-list"):
                            if (self.host_alias_list is None):
                                self.host_alias_list = IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList()
                                self.host_alias_list.parent = self
                                self._children_name_map["host_alias_list"] = "host-alias-list"
                            return self.host_alias_list

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host-address" or name == "host-alias-list" or name == "host-name" or name == "af-name" or name == "age"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "host-name"):
                            self.host_name = value
                            self.host_name.value_namespace = name_space
                            self.host_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "age"):
                            self.age = value
                            self.age.value_namespace = name_space
                            self.age.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.host:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.host:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "hosts" + path_buffer

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

                    if (child_yang_name == "host"):
                        for c in self.host:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = IpDomain.Vrfs.Vrf.Hosts.Host()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.host.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "host"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.hosts is not None and self.hosts.has_data()) or
                    (self.server is not None and self.server.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.hosts is not None and self.hosts.has_operation()) or
                    (self.server is not None and self.server.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-domain-oper:ip-domain/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "hosts"):
                    if (self.hosts is None):
                        self.hosts = IpDomain.Vrfs.Vrf.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                    return self.hosts

                if (child_yang_name == "server"):
                    if (self.server is None):
                        self.server = IpDomain.Vrfs.Vrf.Server()
                        self.server.parent = self
                        self._children_name_map["server"] = "server"
                    return self.server

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "hosts" or name == "server" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ip-domain-oper:ip-domain/%s" % self.get_segment_path()
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
        path_buffer = "Cisco-IOS-XR-ip-domain-oper:ip-domain" + path_buffer

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

class Ipv4(Identity):
    """
    IPv4 family address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2015-09-29'

    def __init__(self):
        super(Ipv4, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper:ipv4")


class Ipv6(Identity):
    """
    IPv6 family address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2015-09-29'

    def __init__(self):
        super(Ipv6, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper", "Cisco-IOS-XR-ip-domain-oper:ipv6")


