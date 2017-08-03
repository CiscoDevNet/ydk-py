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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Sbfd(Entity):
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
        super(Sbfd, self).__init__()
        self._top_entity = None

        self.yang_name = "sbfd"
        self.yang_parent_name = "Cisco-IOS-XR-ip-sbfd-cfg"

        self.local_discriminator = Sbfd.LocalDiscriminator()
        self.local_discriminator.parent = self
        self._children_name_map["local_discriminator"] = "local-discriminator"
        self._children_yang_names.add("local-discriminator")

        self.remote_target = Sbfd.RemoteTarget()
        self.remote_target.parent = self
        self._children_name_map["remote_target"] = "remote-target"
        self._children_yang_names.add("remote-target")


    class RemoteTarget(Entity):
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
            super(Sbfd.RemoteTarget, self).__init__()

            self.yang_name = "remote-target"
            self.yang_parent_name = "sbfd"

            self.ipv4_addresses = Sbfd.RemoteTarget.Ipv4Addresses()
            self.ipv4_addresses.parent = self
            self._children_name_map["ipv4_addresses"] = "ipv4-addresses"
            self._children_yang_names.add("ipv4-addresses")

            self.ipv6_addresses = Sbfd.RemoteTarget.Ipv6Addresses()
            self.ipv6_addresses.parent = self
            self._children_name_map["ipv6_addresses"] = "ipv6-addresses"
            self._children_yang_names.add("ipv6-addresses")


        class Ipv4Addresses(Entity):
            """
            ipv4 address as target
            
            .. attribute:: ipv4_address
            
            	IP Address Value for RemoteDiscriminatorTable
            	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.RemoteTarget.Ipv4Addresses, self).__init__()

                self.yang_name = "ipv4-addresses"
                self.yang_parent_name = "remote-target"

                self.ipv4_address = YList(self)

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
                            super(Sbfd.RemoteTarget.Ipv4Addresses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.RemoteTarget.Ipv4Addresses, self).__setattr__(name, value)


            class Ipv4Address(Entity):
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
                    super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address, self).__init__()

                    self.yang_name = "ipv4-address"
                    self.yang_parent_name = "ipv4-addresses"

                    self.address = YLeaf(YType.str, "address")

                    self.remote_discriminator = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address, self).__setattr__(name, value)


                class RemoteDiscriminator(Entity):
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
                        super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator, self).__init__()

                        self.yang_name = "remote-discriminator"
                        self.yang_parent_name = "ipv4-address"

                        self.remote_discriminator = YLeaf(YType.uint32, "remote-discriminator")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("remote_discriminator") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator, self).__setattr__(name, value)

                    def has_data(self):
                        return self.remote_discriminator.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.remote_discriminator.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-discriminator" + "[remote-discriminator='" + self.remote_discriminator.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.remote_discriminator.is_set or self.remote_discriminator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_discriminator.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "remote-discriminator"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "remote-discriminator"):
                            self.remote_discriminator = value
                            self.remote_discriminator.value_namespace = name_space
                            self.remote_discriminator.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.remote_discriminator:
                        if (c.has_data()):
                            return True
                    return self.address.is_set

                def has_operation(self):
                    for c in self.remote_discriminator:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-address" + "[address='" + self.address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/ipv4-addresses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "remote-discriminator"):
                        for c in self.remote_discriminator:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.remote_discriminator.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-discriminator" or name == "address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv4_address:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ipv4_address:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4-addresses" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-address"):
                    for c in self.ipv4_address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv4_address.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv6Addresses(Entity):
            """
            ipv6 address as target
            
            .. attribute:: ipv6_address
            
            	IP Address Value for RemoteDiscriminatorTable
            	**type**\: list of    :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.RemoteTarget.Ipv6Addresses, self).__init__()

                self.yang_name = "ipv6-addresses"
                self.yang_parent_name = "remote-target"

                self.ipv6_address = YList(self)

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
                            super(Sbfd.RemoteTarget.Ipv6Addresses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.RemoteTarget.Ipv6Addresses, self).__setattr__(name, value)


            class Ipv6Address(Entity):
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
                    super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address, self).__init__()

                    self.yang_name = "ipv6-address"
                    self.yang_parent_name = "ipv6-addresses"

                    self.address = YLeaf(YType.str, "address")

                    self.remote_discriminator = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address, self).__setattr__(name, value)


                class RemoteDiscriminator(Entity):
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
                        super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator, self).__init__()

                        self.yang_name = "remote-discriminator"
                        self.yang_parent_name = "ipv6-address"

                        self.remote_discriminator = YLeaf(YType.uint32, "remote-discriminator")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("remote_discriminator") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator, self).__setattr__(name, value)

                    def has_data(self):
                        return self.remote_discriminator.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.remote_discriminator.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-discriminator" + "[remote-discriminator='" + self.remote_discriminator.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.remote_discriminator.is_set or self.remote_discriminator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_discriminator.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "remote-discriminator"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "remote-discriminator"):
                            self.remote_discriminator = value
                            self.remote_discriminator.value_namespace = name_space
                            self.remote_discriminator.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.remote_discriminator:
                        if (c.has_data()):
                            return True
                    return self.address.is_set

                def has_operation(self):
                    for c in self.remote_discriminator:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6-address" + "[address='" + self.address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/ipv6-addresses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "remote-discriminator"):
                        for c in self.remote_discriminator:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.remote_discriminator.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-discriminator" or name == "address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv6_address:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ipv6_address:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6-addresses" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv6-address"):
                    for c in self.ipv6_address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv6_address.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv6-address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.ipv4_addresses is not None and self.ipv4_addresses.has_data()) or
                (self.ipv6_addresses is not None and self.ipv6_addresses.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ipv4_addresses is not None and self.ipv4_addresses.has_operation()) or
                (self.ipv6_addresses is not None and self.ipv6_addresses.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "remote-target" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv4-addresses"):
                if (self.ipv4_addresses is None):
                    self.ipv4_addresses = Sbfd.RemoteTarget.Ipv4Addresses()
                    self.ipv4_addresses.parent = self
                    self._children_name_map["ipv4_addresses"] = "ipv4-addresses"
                return self.ipv4_addresses

            if (child_yang_name == "ipv6-addresses"):
                if (self.ipv6_addresses is None):
                    self.ipv6_addresses = Sbfd.RemoteTarget.Ipv6Addresses()
                    self.ipv6_addresses.parent = self
                    self._children_name_map["ipv6_addresses"] = "ipv6-addresses"
                return self.ipv6_addresses

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv4-addresses" or name == "ipv6-addresses"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LocalDiscriminator(Entity):
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
            super(Sbfd.LocalDiscriminator, self).__init__()

            self.yang_name = "local-discriminator"
            self.yang_parent_name = "sbfd"

            self.dynamic_discriminators = Sbfd.LocalDiscriminator.DynamicDiscriminators()
            self.dynamic_discriminators.parent = self
            self._children_name_map["dynamic_discriminators"] = "dynamic-discriminators"
            self._children_yang_names.add("dynamic-discriminators")

            self.intf_discriminators = Sbfd.LocalDiscriminator.IntfDiscriminators()
            self.intf_discriminators.parent = self
            self._children_name_map["intf_discriminators"] = "intf-discriminators"
            self._children_yang_names.add("intf-discriminators")

            self.ipv4_discriminators = Sbfd.LocalDiscriminator.Ipv4Discriminators()
            self.ipv4_discriminators.parent = self
            self._children_name_map["ipv4_discriminators"] = "ipv4-discriminators"
            self._children_yang_names.add("ipv4-discriminators")

            self.val32_discriminators = Sbfd.LocalDiscriminator.Val32Discriminators()
            self.val32_discriminators.parent = self
            self._children_name_map["val32_discriminators"] = "val32-discriminators"
            self._children_yang_names.add("val32-discriminators")


        class IntfDiscriminators(Entity):
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
                super(Sbfd.LocalDiscriminator.IntfDiscriminators, self).__init__()

                self.yang_name = "intf-discriminators"
                self.yang_parent_name = "local-discriminator"

                self.intf_discriminator = YList(self)

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
                            super(Sbfd.LocalDiscriminator.IntfDiscriminators, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.LocalDiscriminator.IntfDiscriminators, self).__setattr__(name, value)


            class IntfDiscriminator(Entity):
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
                    super(Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator, self).__init__()

                    self.yang_name = "intf-discriminator"
                    self.yang_parent_name = "intf-discriminators"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator, self).__setattr__(name, value)

                def has_data(self):
                    return self.interface_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "intf-discriminator" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/intf-discriminators/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.intf_discriminator:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.intf_discriminator:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "intf-discriminators" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "intf-discriminator"):
                    for c in self.intf_discriminator:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.intf_discriminator.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "intf-discriminator"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class DynamicDiscriminators(Entity):
            """
            Configure local discriminator dynamically
            
            .. attribute:: dynamic_discriminator
            
            	Local discriminator value
            	**type**\: list of    :py:class:`DynamicDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.LocalDiscriminator.DynamicDiscriminators, self).__init__()

                self.yang_name = "dynamic-discriminators"
                self.yang_parent_name = "local-discriminator"

                self.dynamic_discriminator = YList(self)

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
                            super(Sbfd.LocalDiscriminator.DynamicDiscriminators, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.LocalDiscriminator.DynamicDiscriminators, self).__setattr__(name, value)


            class DynamicDiscriminator(Entity):
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
                    super(Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator, self).__init__()

                    self.yang_name = "dynamic-discriminator"
                    self.yang_parent_name = "dynamic-discriminators"

                    self.discriminator = YLeaf(YType.uint32, "discriminator")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminator") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator, self).__setattr__(name, value)

                def has_data(self):
                    return self.discriminator.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminator.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dynamic-discriminator" + "[discriminator='" + self.discriminator.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/dynamic-discriminators/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminator.is_set or self.discriminator.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminator.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discriminator"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminator"):
                        self.discriminator = value
                        self.discriminator.value_namespace = name_space
                        self.discriminator.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.dynamic_discriminator:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.dynamic_discriminator:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dynamic-discriminators" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "dynamic-discriminator"):
                    for c in self.dynamic_discriminator:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.dynamic_discriminator.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dynamic-discriminator"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv4Discriminators(Entity):
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
                super(Sbfd.LocalDiscriminator.Ipv4Discriminators, self).__init__()

                self.yang_name = "ipv4-discriminators"
                self.yang_parent_name = "local-discriminator"

                self.ipv4_discriminator = YList(self)

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
                            super(Sbfd.LocalDiscriminator.Ipv4Discriminators, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.LocalDiscriminator.Ipv4Discriminators, self).__setattr__(name, value)


            class Ipv4Discriminator(Entity):
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
                    super(Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator, self).__init__()

                    self.yang_name = "ipv4-discriminator"
                    self.yang_parent_name = "ipv4-discriminators"

                    self.address = YLeaf(YType.str, "address")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator, self).__setattr__(name, value)

                def has_data(self):
                    return self.address.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-discriminator" + "[address='" + self.address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/ipv4-discriminators/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv4_discriminator:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ipv4_discriminator:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4-discriminators" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-discriminator"):
                    for c in self.ipv4_discriminator:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv4_discriminator.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-discriminator"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Val32Discriminators(Entity):
            """
            Configure local discriminator as an integer
            
            .. attribute:: val32_discriminator
            
            	Local discriminator value
            	**type**\: list of    :py:class:`Val32Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.LocalDiscriminator.Val32Discriminators, self).__init__()

                self.yang_name = "val32-discriminators"
                self.yang_parent_name = "local-discriminator"

                self.val32_discriminator = YList(self)

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
                            super(Sbfd.LocalDiscriminator.Val32Discriminators, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.LocalDiscriminator.Val32Discriminators, self).__setattr__(name, value)


            class Val32Discriminator(Entity):
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
                    super(Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator, self).__init__()

                    self.yang_name = "val32-discriminator"
                    self.yang_parent_name = "val32-discriminators"

                    self.discriminator = YLeaf(YType.uint32, "discriminator")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminator") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator, self).__setattr__(name, value)

                def has_data(self):
                    return self.discriminator.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminator.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "val32-discriminator" + "[discriminator='" + self.discriminator.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/val32-discriminators/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminator.is_set or self.discriminator.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminator.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discriminator"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminator"):
                        self.discriminator = value
                        self.discriminator.value_namespace = name_space
                        self.discriminator.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.val32_discriminator:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.val32_discriminator:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "val32-discriminators" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "val32-discriminator"):
                    for c in self.val32_discriminator:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.val32_discriminator.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "val32-discriminator"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.dynamic_discriminators is not None and self.dynamic_discriminators.has_data()) or
                (self.intf_discriminators is not None and self.intf_discriminators.has_data()) or
                (self.ipv4_discriminators is not None and self.ipv4_discriminators.has_data()) or
                (self.val32_discriminators is not None and self.val32_discriminators.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.dynamic_discriminators is not None and self.dynamic_discriminators.has_operation()) or
                (self.intf_discriminators is not None and self.intf_discriminators.has_operation()) or
                (self.ipv4_discriminators is not None and self.ipv4_discriminators.has_operation()) or
                (self.val32_discriminators is not None and self.val32_discriminators.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "local-discriminator" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dynamic-discriminators"):
                if (self.dynamic_discriminators is None):
                    self.dynamic_discriminators = Sbfd.LocalDiscriminator.DynamicDiscriminators()
                    self.dynamic_discriminators.parent = self
                    self._children_name_map["dynamic_discriminators"] = "dynamic-discriminators"
                return self.dynamic_discriminators

            if (child_yang_name == "intf-discriminators"):
                if (self.intf_discriminators is None):
                    self.intf_discriminators = Sbfd.LocalDiscriminator.IntfDiscriminators()
                    self.intf_discriminators.parent = self
                    self._children_name_map["intf_discriminators"] = "intf-discriminators"
                return self.intf_discriminators

            if (child_yang_name == "ipv4-discriminators"):
                if (self.ipv4_discriminators is None):
                    self.ipv4_discriminators = Sbfd.LocalDiscriminator.Ipv4Discriminators()
                    self.ipv4_discriminators.parent = self
                    self._children_name_map["ipv4_discriminators"] = "ipv4-discriminators"
                return self.ipv4_discriminators

            if (child_yang_name == "val32-discriminators"):
                if (self.val32_discriminators is None):
                    self.val32_discriminators = Sbfd.LocalDiscriminator.Val32Discriminators()
                    self.val32_discriminators.parent = self
                    self._children_name_map["val32_discriminators"] = "val32-discriminators"
                return self.val32_discriminators

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dynamic-discriminators" or name == "intf-discriminators" or name == "ipv4-discriminators" or name == "val32-discriminators"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.local_discriminator is not None and self.local_discriminator.has_data()) or
            (self.remote_target is not None and self.remote_target.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.local_discriminator is not None and self.local_discriminator.has_operation()) or
            (self.remote_target is not None and self.remote_target.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-sbfd-cfg:sbfd" + path_buffer

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

        if (child_yang_name == "local-discriminator"):
            if (self.local_discriminator is None):
                self.local_discriminator = Sbfd.LocalDiscriminator()
                self.local_discriminator.parent = self
                self._children_name_map["local_discriminator"] = "local-discriminator"
            return self.local_discriminator

        if (child_yang_name == "remote-target"):
            if (self.remote_target is None):
                self.remote_target = Sbfd.RemoteTarget()
                self.remote_target.parent = self
                self._children_name_map["remote_target"] = "remote-target"
            return self.remote_target

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "local-discriminator" or name == "remote-target"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Sbfd()
        return self._top_entity

