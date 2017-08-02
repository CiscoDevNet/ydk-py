""" Cisco_IOS_XR_ip_icmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-icmp package configuration.

This module contains definitions
for the following management objects\:
  icmp\: IP ICMP configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SourcePolicy(Enum):
    """
    SourcePolicy

    Source policy

    .. data:: vrf = 1

    	Set Source Selection Policy to vrf

    .. data:: rfc = 2

    	Set Source Selection Policy to rfc

    """

    vrf = Enum.YLeaf(1, "vrf")

    rfc = Enum.YLeaf(2, "rfc")



class Icmp(Entity):
    """
    IP ICMP configuration data
    
    .. attribute:: ip_protocol
    
    	IP Protocol Type
    	**type**\: list of    :py:class:`IpProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol>`
    
    

    """

    _prefix = 'ip-icmp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Icmp, self).__init__()
        self._top_entity = None

        self.yang_name = "icmp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-icmp-cfg"

        self.ip_protocol = YList(self)

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
                    super(Icmp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Icmp, self).__setattr__(name, value)


    class IpProtocol(Entity):
        """
        IP Protocol Type
        
        .. attribute:: protocol_type  <key>
        
        	IP Protocol Type; ipv4 or ipv6
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: rate_limit
        
        	Set ratelimit of ICMP packets
        	**type**\:   :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol.RateLimit>`
        
        .. attribute:: source
        
        	IP ICMP Source Address Selection Policy
        	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol.Source>`
        
        

        """

        _prefix = 'ip-icmp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Icmp.IpProtocol, self).__init__()

            self.yang_name = "ip-protocol"
            self.yang_parent_name = "icmp"

            self.protocol_type = YLeaf(YType.str, "protocol-type")

            self.rate_limit = Icmp.IpProtocol.RateLimit()
            self.rate_limit.parent = self
            self._children_name_map["rate_limit"] = "rate-limit"
            self._children_yang_names.add("rate-limit")

            self.source = Icmp.IpProtocol.Source()
            self.source.parent = self
            self._children_name_map["source"] = "source"
            self._children_yang_names.add("source")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("protocol_type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Icmp.IpProtocol, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Icmp.IpProtocol, self).__setattr__(name, value)


        class RateLimit(Entity):
            """
            Set ratelimit of ICMP packets
            
            .. attribute:: unreachable
            
            	Set unreachable ICMP packets ratelimit
            	**type**\:   :py:class:`Unreachable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.Icmp.IpProtocol.RateLimit.Unreachable>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Icmp.IpProtocol.RateLimit, self).__init__()

                self.yang_name = "rate-limit"
                self.yang_parent_name = "ip-protocol"

                self.unreachable = Icmp.IpProtocol.RateLimit.Unreachable()
                self.unreachable.parent = self
                self._children_name_map["unreachable"] = "unreachable"
                self._children_yang_names.add("unreachable")


            class Unreachable(Entity):
                """
                Set unreachable ICMP packets ratelimit
                
                .. attribute:: fragmentation
                
                	Rate Limit of Unreachable DF paclets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rate
                
                	Rate Limit of Unreachable ICMP paclets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-icmp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Icmp.IpProtocol.RateLimit.Unreachable, self).__init__()

                    self.yang_name = "unreachable"
                    self.yang_parent_name = "rate-limit"

                    self.fragmentation = YLeaf(YType.uint32, "fragmentation")

                    self.rate = YLeaf(YType.uint32, "rate")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("fragmentation",
                                    "rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Icmp.IpProtocol.RateLimit.Unreachable, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Icmp.IpProtocol.RateLimit.Unreachable, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.fragmentation.is_set or
                        self.rate.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.fragmentation.yfilter != YFilter.not_set or
                        self.rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "unreachable" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.fragmentation.is_set or self.fragmentation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fragmentation.get_name_leafdata())
                    if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fragmentation" or name == "rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "fragmentation"):
                        self.fragmentation = value
                        self.fragmentation.value_namespace = name_space
                        self.fragmentation.value_namespace_prefix = name_space_prefix
                    if(value_path == "rate"):
                        self.rate = value
                        self.rate.value_namespace = name_space
                        self.rate.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.unreachable is not None and self.unreachable.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.unreachable is not None and self.unreachable.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rate-limit" + path_buffer

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

                if (child_yang_name == "unreachable"):
                    if (self.unreachable is None):
                        self.unreachable = Icmp.IpProtocol.RateLimit.Unreachable()
                        self.unreachable.parent = self
                        self._children_name_map["unreachable"] = "unreachable"
                    return self.unreachable

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "unreachable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Source(Entity):
            """
            IP ICMP Source Address Selection Policy
            
            .. attribute:: source_address_policy
            
            	Configure Source Address Policy
            	**type**\:   :py:class:`SourcePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg.SourcePolicy>`
            
            

            """

            _prefix = 'ip-icmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Icmp.IpProtocol.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "ip-protocol"

                self.source_address_policy = YLeaf(YType.enumeration, "source-address-policy")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("source_address_policy") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Icmp.IpProtocol.Source, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Icmp.IpProtocol.Source, self).__setattr__(name, value)

            def has_data(self):
                return self.source_address_policy.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.source_address_policy.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.source_address_policy.is_set or self.source_address_policy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_address_policy.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "source-address-policy"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "source-address-policy"):
                    self.source_address_policy = value
                    self.source_address_policy.value_namespace = name_space
                    self.source_address_policy.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.protocol_type.is_set or
                (self.rate_limit is not None and self.rate_limit.has_data()) or
                (self.source is not None and self.source.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.protocol_type.yfilter != YFilter.not_set or
                (self.rate_limit is not None and self.rate_limit.has_operation()) or
                (self.source is not None and self.source.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ip-protocol" + "[protocol-type='" + self.protocol_type.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-icmp-cfg:icmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.protocol_type.is_set or self.protocol_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.protocol_type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rate-limit"):
                if (self.rate_limit is None):
                    self.rate_limit = Icmp.IpProtocol.RateLimit()
                    self.rate_limit.parent = self
                    self._children_name_map["rate_limit"] = "rate-limit"
                return self.rate_limit

            if (child_yang_name == "source"):
                if (self.source is None):
                    self.source = Icmp.IpProtocol.Source()
                    self.source.parent = self
                    self._children_name_map["source"] = "source"
                return self.source

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rate-limit" or name == "source" or name == "protocol-type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "protocol-type"):
                self.protocol_type = value
                self.protocol_type.value_namespace = name_space
                self.protocol_type.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.ip_protocol:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.ip_protocol:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-icmp-cfg:icmp" + path_buffer

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

        if (child_yang_name == "ip-protocol"):
            for c in self.ip_protocol:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Icmp.IpProtocol()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.ip_protocol.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ip-protocol"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Icmp()
        return self._top_entity

