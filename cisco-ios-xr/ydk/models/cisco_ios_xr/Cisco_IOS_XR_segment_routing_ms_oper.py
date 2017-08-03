""" Cisco_IOS_XR_segment_routing_ms_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-ms package operational data.

This module contains definitions
for the following management objects\:
  srms\: Segment Routing Mapping Server operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrmsMiAfEB(Enum):
    """
    SrmsMiAfEB

    Srms mi af e b

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    none = Enum.YLeaf(0, "none")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class SrmsMiFlagEB(Enum):
    """
    SrmsMiFlagEB

    Srms mi flag e b

    .. data:: false = 0

    	False

    .. data:: true = 1

    	True

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


class SrmsMiSrcEB(Enum):
    """
    SrmsMiSrcEB

    Srms mi src e b

    .. data:: none = 0

    	None

    .. data:: local = 1

    	Local

    .. data:: remote = 2

    	Remote

    """

    none = Enum.YLeaf(0, "none")

    local = Enum.YLeaf(1, "local")

    remote = Enum.YLeaf(2, "remote")



class Srms(Entity):
    """
    Segment Routing Mapping Server operational data
    
    .. attribute:: mapping
    
    	IP prefix to SID mappings
    	**type**\:   :py:class:`Mapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping>`
    
    .. attribute:: policy
    
    	Policy operational data
    	**type**\:   :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy>`
    
    

    """

    _prefix = 'segment-routing-ms-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Srms, self).__init__()
        self._top_entity = None

        self.yang_name = "srms"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-ms-oper"

        self.mapping = Srms.Mapping()
        self.mapping.parent = self
        self._children_name_map["mapping"] = "mapping"
        self._children_yang_names.add("mapping")

        self.policy = Srms.Policy()
        self.policy.parent = self
        self._children_name_map["policy"] = "policy"
        self._children_yang_names.add("policy")


    class Mapping(Entity):
        """
        IP prefix to SID mappings
        
        .. attribute:: mapping_ipv4
        
        	IPv4 prefix to SID mappings
        	**type**\:   :py:class:`MappingIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4>`
        
        .. attribute:: mapping_ipv6
        
        	IPv6 prefix to SID mappings
        	**type**\:   :py:class:`MappingIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6>`
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Srms.Mapping, self).__init__()

            self.yang_name = "mapping"
            self.yang_parent_name = "srms"

            self.mapping_ipv4 = Srms.Mapping.MappingIpv4()
            self.mapping_ipv4.parent = self
            self._children_name_map["mapping_ipv4"] = "mapping-ipv4"
            self._children_yang_names.add("mapping-ipv4")

            self.mapping_ipv6 = Srms.Mapping.MappingIpv6()
            self.mapping_ipv6.parent = self
            self._children_name_map["mapping_ipv6"] = "mapping-ipv6"
            self._children_yang_names.add("mapping-ipv6")


        class MappingIpv4(Entity):
            """
            IPv4 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of    :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Mapping.MappingIpv4, self).__init__()

                self.yang_name = "mapping-ipv4"
                self.yang_parent_name = "mapping"

                self.mapping_mi = YList(self)

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
                            super(Srms.Mapping.MappingIpv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srms.Mapping.MappingIpv4, self).__setattr__(name, value)


            class MappingMi(Entity):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: addr
                
                	addr
                	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv4.MappingMi.Addr>`
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                .. attribute:: ip
                
                	IP
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\:  str
                
                	**length:** 0..50
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: router
                
                	Router ID
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: src
                
                	src
                	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Mapping.MappingIpv4.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv4"

                    self.area = YLeaf(YType.str, "area")

                    self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                    self.ip = YLeaf(YType.str, "ip")

                    self.last_prefix = YLeaf(YType.str, "last-prefix")

                    self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                    self.prefix = YLeaf(YType.int32, "prefix")

                    self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                    self.router = YLeaf(YType.str, "router")

                    self.sid_count = YLeaf(YType.uint32, "sid-count")

                    self.sid_start = YLeaf(YType.uint32, "sid-start")

                    self.src = YLeaf(YType.enumeration, "src")

                    self.addr = Srms.Mapping.MappingIpv4.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._children_yang_names.add("addr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("area",
                                    "flag_attached",
                                    "ip",
                                    "last_prefix",
                                    "last_sid_index",
                                    "prefix",
                                    "prefix_xr",
                                    "router",
                                    "sid_count",
                                    "sid_start",
                                    "src") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Srms.Mapping.MappingIpv4.MappingMi, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srms.Mapping.MappingIpv4.MappingMi, self).__setattr__(name, value)


                class Addr(Entity):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Mapping.MappingIpv4.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"

                        self.af = YLeaf(YType.enumeration, "af")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af",
                                        "ipv4",
                                        "ipv6") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srms.Mapping.MappingIpv4.MappingMi.Addr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srms.Mapping.MappingIpv4.MappingMi.Addr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.af.is_set or
                            self.ipv4.is_set or
                            self.ipv6.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af.yfilter != YFilter.not_set or
                            self.ipv4.yfilter != YFilter.not_set or
                            self.ipv6.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "addr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv4/mapping-mi/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af.get_name_leafdata())
                        if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4.get_name_leafdata())
                        if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af" or name == "ipv4" or name == "ipv6"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af"):
                            self.af = value
                            self.af.value_namespace = name_space
                            self.af.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4"):
                            self.ipv4 = value
                            self.ipv4.value_namespace = name_space
                            self.ipv4.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6"):
                            self.ipv6 = value
                            self.ipv6.value_namespace = name_space
                            self.ipv6.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.area.is_set or
                        self.flag_attached.is_set or
                        self.ip.is_set or
                        self.last_prefix.is_set or
                        self.last_sid_index.is_set or
                        self.prefix.is_set or
                        self.prefix_xr.is_set or
                        self.router.is_set or
                        self.sid_count.is_set or
                        self.sid_start.is_set or
                        self.src.is_set or
                        (self.addr is not None and self.addr.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.area.yfilter != YFilter.not_set or
                        self.flag_attached.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.last_prefix.yfilter != YFilter.not_set or
                        self.last_sid_index.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.prefix_xr.yfilter != YFilter.not_set or
                        self.router.yfilter != YFilter.not_set or
                        self.sid_count.yfilter != YFilter.not_set or
                        self.sid_start.yfilter != YFilter.not_set or
                        self.src.yfilter != YFilter.not_set or
                        (self.addr is not None and self.addr.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mapping-mi" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv4/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.area.is_set or self.area.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.area.get_name_leafdata())
                    if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flag_attached.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.last_prefix.is_set or self.last_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_prefix.get_name_leafdata())
                    if (self.last_sid_index.is_set or self.last_sid_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_sid_index.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_xr.get_name_leafdata())
                    if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router.get_name_leafdata())
                    if (self.sid_count.is_set or self.sid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sid_count.get_name_leafdata())
                    if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sid_start.get_name_leafdata())
                    if (self.src.is_set or self.src.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.src.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "addr"):
                        if (self.addr is None):
                            self.addr = Srms.Mapping.MappingIpv4.MappingMi.Addr()
                            self.addr.parent = self
                            self._children_name_map["addr"] = "addr"
                        return self.addr

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "addr" or name == "area" or name == "flag-attached" or name == "ip" or name == "last-prefix" or name == "last-sid-index" or name == "prefix" or name == "prefix-xr" or name == "router" or name == "sid-count" or name == "sid-start" or name == "src"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "area"):
                        self.area = value
                        self.area.value_namespace = name_space
                        self.area.value_namespace_prefix = name_space_prefix
                    if(value_path == "flag-attached"):
                        self.flag_attached = value
                        self.flag_attached.value_namespace = name_space
                        self.flag_attached.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-prefix"):
                        self.last_prefix = value
                        self.last_prefix.value_namespace = name_space
                        self.last_prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-sid-index"):
                        self.last_sid_index = value
                        self.last_sid_index.value_namespace = name_space
                        self.last_sid_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-xr"):
                        self.prefix_xr = value
                        self.prefix_xr.value_namespace = name_space
                        self.prefix_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "router"):
                        self.router = value
                        self.router.value_namespace = name_space
                        self.router.value_namespace_prefix = name_space_prefix
                    if(value_path == "sid-count"):
                        self.sid_count = value
                        self.sid_count.value_namespace = name_space
                        self.sid_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "sid-start"):
                        self.sid_start = value
                        self.sid_start.value_namespace = name_space
                        self.sid_start.value_namespace_prefix = name_space_prefix
                    if(value_path == "src"):
                        self.src = value
                        self.src.value_namespace = name_space
                        self.src.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.mapping_mi:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.mapping_mi:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mapping-ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mapping-mi"):
                    for c in self.mapping_mi:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Srms.Mapping.MappingIpv4.MappingMi()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.mapping_mi.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mapping-mi"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class MappingIpv6(Entity):
            """
            IPv6 prefix to SID mappings
            
            .. attribute:: mapping_mi
            
            	IP prefix to SID mapping item. It's not possible to list all of the IP prefix to SID mappings, as the set of valid prefixes could be very large. Instead, SID map information must be retrieved individually for each prefix of interest
            	**type**\: list of    :py:class:`MappingMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Mapping.MappingIpv6, self).__init__()

                self.yang_name = "mapping-ipv6"
                self.yang_parent_name = "mapping"

                self.mapping_mi = YList(self)

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
                            super(Srms.Mapping.MappingIpv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srms.Mapping.MappingIpv6, self).__setattr__(name, value)


            class MappingMi(Entity):
                """
                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                
                .. attribute:: addr
                
                	addr
                	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Mapping.MappingIpv6.MappingMi.Addr>`
                
                .. attribute:: area
                
                	Area (OSPF) or Level (ISIS)
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: flag_attached
                
                	Attached flag
                	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                
                .. attribute:: ip
                
                	IP
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: last_prefix
                
                	Last IP Prefix
                	**type**\:  str
                
                	**length:** 0..50
                
                .. attribute:: last_sid_index
                
                	Last SID Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: prefix_xr
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: router
                
                	Router ID
                	**type**\:  str
                
                	**length:** 0..30
                
                .. attribute:: sid_count
                
                	SID range
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sid_start
                
                	Starting SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: src
                
                	src
                	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Mapping.MappingIpv6.MappingMi, self).__init__()

                    self.yang_name = "mapping-mi"
                    self.yang_parent_name = "mapping-ipv6"

                    self.area = YLeaf(YType.str, "area")

                    self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                    self.ip = YLeaf(YType.str, "ip")

                    self.last_prefix = YLeaf(YType.str, "last-prefix")

                    self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                    self.prefix = YLeaf(YType.int32, "prefix")

                    self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                    self.router = YLeaf(YType.str, "router")

                    self.sid_count = YLeaf(YType.uint32, "sid-count")

                    self.sid_start = YLeaf(YType.uint32, "sid-start")

                    self.src = YLeaf(YType.enumeration, "src")

                    self.addr = Srms.Mapping.MappingIpv6.MappingMi.Addr()
                    self.addr.parent = self
                    self._children_name_map["addr"] = "addr"
                    self._children_yang_names.add("addr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("area",
                                    "flag_attached",
                                    "ip",
                                    "last_prefix",
                                    "last_sid_index",
                                    "prefix",
                                    "prefix_xr",
                                    "router",
                                    "sid_count",
                                    "sid_start",
                                    "src") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Srms.Mapping.MappingIpv6.MappingMi, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srms.Mapping.MappingIpv6.MappingMi, self).__setattr__(name, value)


                class Addr(Entity):
                    """
                    addr
                    
                    .. attribute:: af
                    
                    	AF
                    	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Mapping.MappingIpv6.MappingMi.Addr, self).__init__()

                        self.yang_name = "addr"
                        self.yang_parent_name = "mapping-mi"

                        self.af = YLeaf(YType.enumeration, "af")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af",
                                        "ipv4",
                                        "ipv6") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srms.Mapping.MappingIpv6.MappingMi.Addr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srms.Mapping.MappingIpv6.MappingMi.Addr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.af.is_set or
                            self.ipv4.is_set or
                            self.ipv6.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af.yfilter != YFilter.not_set or
                            self.ipv4.yfilter != YFilter.not_set or
                            self.ipv6.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "addr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv6/mapping-mi/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af.get_name_leafdata())
                        if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4.get_name_leafdata())
                        if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af" or name == "ipv4" or name == "ipv6"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af"):
                            self.af = value
                            self.af.value_namespace = name_space
                            self.af.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4"):
                            self.ipv4 = value
                            self.ipv4.value_namespace = name_space
                            self.ipv4.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6"):
                            self.ipv6 = value
                            self.ipv6.value_namespace = name_space
                            self.ipv6.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.area.is_set or
                        self.flag_attached.is_set or
                        self.ip.is_set or
                        self.last_prefix.is_set or
                        self.last_sid_index.is_set or
                        self.prefix.is_set or
                        self.prefix_xr.is_set or
                        self.router.is_set or
                        self.sid_count.is_set or
                        self.sid_start.is_set or
                        self.src.is_set or
                        (self.addr is not None and self.addr.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.area.yfilter != YFilter.not_set or
                        self.flag_attached.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.last_prefix.yfilter != YFilter.not_set or
                        self.last_sid_index.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.prefix_xr.yfilter != YFilter.not_set or
                        self.router.yfilter != YFilter.not_set or
                        self.sid_count.yfilter != YFilter.not_set or
                        self.sid_start.yfilter != YFilter.not_set or
                        self.src.yfilter != YFilter.not_set or
                        (self.addr is not None and self.addr.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mapping-mi" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/mapping-ipv6/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.area.is_set or self.area.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.area.get_name_leafdata())
                    if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flag_attached.get_name_leafdata())
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.last_prefix.is_set or self.last_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_prefix.get_name_leafdata())
                    if (self.last_sid_index.is_set or self.last_sid_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_sid_index.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_xr.get_name_leafdata())
                    if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router.get_name_leafdata())
                    if (self.sid_count.is_set or self.sid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sid_count.get_name_leafdata())
                    if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sid_start.get_name_leafdata())
                    if (self.src.is_set or self.src.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.src.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "addr"):
                        if (self.addr is None):
                            self.addr = Srms.Mapping.MappingIpv6.MappingMi.Addr()
                            self.addr.parent = self
                            self._children_name_map["addr"] = "addr"
                        return self.addr

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "addr" or name == "area" or name == "flag-attached" or name == "ip" or name == "last-prefix" or name == "last-sid-index" or name == "prefix" or name == "prefix-xr" or name == "router" or name == "sid-count" or name == "sid-start" or name == "src"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "area"):
                        self.area = value
                        self.area.value_namespace = name_space
                        self.area.value_namespace_prefix = name_space_prefix
                    if(value_path == "flag-attached"):
                        self.flag_attached = value
                        self.flag_attached.value_namespace = name_space
                        self.flag_attached.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-prefix"):
                        self.last_prefix = value
                        self.last_prefix.value_namespace = name_space
                        self.last_prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-sid-index"):
                        self.last_sid_index = value
                        self.last_sid_index.value_namespace = name_space
                        self.last_sid_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-xr"):
                        self.prefix_xr = value
                        self.prefix_xr.value_namespace = name_space
                        self.prefix_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "router"):
                        self.router = value
                        self.router.value_namespace = name_space
                        self.router.value_namespace_prefix = name_space_prefix
                    if(value_path == "sid-count"):
                        self.sid_count = value
                        self.sid_count.value_namespace = name_space
                        self.sid_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "sid-start"):
                        self.sid_start = value
                        self.sid_start.value_namespace = name_space
                        self.sid_start.value_namespace_prefix = name_space_prefix
                    if(value_path == "src"):
                        self.src = value
                        self.src.value_namespace = name_space
                        self.src.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.mapping_mi:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.mapping_mi:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mapping-ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/mapping/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mapping-mi"):
                    for c in self.mapping_mi:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Srms.Mapping.MappingIpv6.MappingMi()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.mapping_mi.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mapping-mi"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.mapping_ipv4 is not None and self.mapping_ipv4.has_data()) or
                (self.mapping_ipv6 is not None and self.mapping_ipv6.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.mapping_ipv4 is not None and self.mapping_ipv4.has_operation()) or
                (self.mapping_ipv6 is not None and self.mapping_ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mapping" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mapping-ipv4"):
                if (self.mapping_ipv4 is None):
                    self.mapping_ipv4 = Srms.Mapping.MappingIpv4()
                    self.mapping_ipv4.parent = self
                    self._children_name_map["mapping_ipv4"] = "mapping-ipv4"
                return self.mapping_ipv4

            if (child_yang_name == "mapping-ipv6"):
                if (self.mapping_ipv6 is None):
                    self.mapping_ipv6 = Srms.Mapping.MappingIpv6()
                    self.mapping_ipv6.parent = self
                    self._children_name_map["mapping_ipv6"] = "mapping-ipv6"
                return self.mapping_ipv6

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mapping-ipv4" or name == "mapping-ipv6"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Policy(Entity):
        """
        Policy operational data
        
        .. attribute:: policy_ipv4
        
        	IPv4 policy operational data
        	**type**\:   :py:class:`PolicyIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4>`
        
        .. attribute:: policy_ipv6
        
        	IPv6 policy operational data
        	**type**\:   :py:class:`PolicyIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6>`
        
        

        """

        _prefix = 'segment-routing-ms-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Srms.Policy, self).__init__()

            self.yang_name = "policy"
            self.yang_parent_name = "srms"

            self.policy_ipv4 = Srms.Policy.PolicyIpv4()
            self.policy_ipv4.parent = self
            self._children_name_map["policy_ipv4"] = "policy-ipv4"
            self._children_yang_names.add("policy-ipv4")

            self.policy_ipv6 = Srms.Policy.PolicyIpv6()
            self.policy_ipv6.parent = self
            self._children_name_map["policy_ipv6"] = "policy-ipv6"
            self._children_yang_names.add("policy-ipv6")


        class PolicyIpv4(Entity):
            """
            IPv4 policy operational data
            
            .. attribute:: policy_ipv4_active
            
            	IPv4 active policy operational data
            	**type**\:   :py:class:`PolicyIpv4Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active>`
            
            .. attribute:: policy_ipv4_backup
            
            	IPv4 backup policy operational data
            	**type**\:   :py:class:`PolicyIpv4Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Policy.PolicyIpv4, self).__init__()

                self.yang_name = "policy-ipv4"
                self.yang_parent_name = "policy"

                self.policy_ipv4_active = Srms.Policy.PolicyIpv4.PolicyIpv4Active()
                self.policy_ipv4_active.parent = self
                self._children_name_map["policy_ipv4_active"] = "policy-ipv4-active"
                self._children_yang_names.add("policy-ipv4-active")

                self.policy_ipv4_backup = Srms.Policy.PolicyIpv4.PolicyIpv4Backup()
                self.policy_ipv4_backup.parent = self
                self._children_name_map["policy_ipv4_backup"] = "policy-ipv4-backup"
                self._children_yang_names.add("policy-ipv4-backup")


            class PolicyIpv4Backup(Entity):
                """
                IPv4 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, self).__init__()

                    self.yang_name = "policy-ipv4-backup"
                    self.yang_parent_name = "policy-ipv4"

                    self.policy_mi = YList(self)

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
                                super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup, self).__setattr__(name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-backup"

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mi_id",
                                        "area",
                                        "flag_attached",
                                        "last_prefix",
                                        "last_sid_index",
                                        "prefix_xr",
                                        "router",
                                        "sid_count",
                                        "sid_start",
                                        "src") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi, self).__setattr__(name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af",
                                            "ipv4",
                                            "ipv6") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af.is_set or
                                self.ipv4.is_set or
                                self.ipv6.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af.yfilter != YFilter.not_set or
                                self.ipv4.yfilter != YFilter.not_set or
                                self.ipv6.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af.get_name_leafdata())
                            if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4.get_name_leafdata())
                            if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af" or name == "ipv4" or name == "ipv6"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af"):
                                self.af = value
                                self.af.value_namespace = name_space
                                self.af.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4"):
                                self.ipv4 = value
                                self.ipv4.value_namespace = name_space
                                self.ipv4.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6"):
                                self.ipv6 = value
                                self.ipv6.value_namespace = name_space
                                self.ipv6.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mi_id.is_set or
                            self.area.is_set or
                            self.flag_attached.is_set or
                            self.last_prefix.is_set or
                            self.last_sid_index.is_set or
                            self.prefix_xr.is_set or
                            self.router.is_set or
                            self.sid_count.is_set or
                            self.sid_start.is_set or
                            self.src.is_set or
                            (self.addr is not None and self.addr.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mi_id.yfilter != YFilter.not_set or
                            self.area.yfilter != YFilter.not_set or
                            self.flag_attached.yfilter != YFilter.not_set or
                            self.last_prefix.yfilter != YFilter.not_set or
                            self.last_sid_index.yfilter != YFilter.not_set or
                            self.prefix_xr.yfilter != YFilter.not_set or
                            self.router.yfilter != YFilter.not_set or
                            self.sid_count.yfilter != YFilter.not_set or
                            self.sid_start.yfilter != YFilter.not_set or
                            self.src.yfilter != YFilter.not_set or
                            (self.addr is not None and self.addr.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "policy-mi" + "[mi-id='" + self.mi_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/policy-ipv4-backup/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mi_id.is_set or self.mi_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mi_id.get_name_leafdata())
                        if (self.area.is_set or self.area.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.area.get_name_leafdata())
                        if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flag_attached.get_name_leafdata())
                        if (self.last_prefix.is_set or self.last_prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_prefix.get_name_leafdata())
                        if (self.last_sid_index.is_set or self.last_sid_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_sid_index.get_name_leafdata())
                        if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_xr.get_name_leafdata())
                        if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router.get_name_leafdata())
                        if (self.sid_count.is_set or self.sid_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_count.get_name_leafdata())
                        if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_start.get_name_leafdata())
                        if (self.src.is_set or self.src.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.src.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "addr"):
                            if (self.addr is None):
                                self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr()
                                self.addr.parent = self
                                self._children_name_map["addr"] = "addr"
                            return self.addr

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "addr" or name == "mi-id" or name == "area" or name == "flag-attached" or name == "last-prefix" or name == "last-sid-index" or name == "prefix-xr" or name == "router" or name == "sid-count" or name == "sid-start" or name == "src"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mi-id"):
                            self.mi_id = value
                            self.mi_id.value_namespace = name_space
                            self.mi_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "area"):
                            self.area = value
                            self.area.value_namespace = name_space
                            self.area.value_namespace_prefix = name_space_prefix
                        if(value_path == "flag-attached"):
                            self.flag_attached = value
                            self.flag_attached.value_namespace = name_space
                            self.flag_attached.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-prefix"):
                            self.last_prefix = value
                            self.last_prefix.value_namespace = name_space
                            self.last_prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-sid-index"):
                            self.last_sid_index = value
                            self.last_sid_index.value_namespace = name_space
                            self.last_sid_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-xr"):
                            self.prefix_xr = value
                            self.prefix_xr.value_namespace = name_space
                            self.prefix_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "router"):
                            self.router = value
                            self.router.value_namespace = name_space
                            self.router.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-count"):
                            self.sid_count = value
                            self.sid_count.value_namespace = name_space
                            self.sid_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-start"):
                            self.sid_start = value
                            self.sid_start.value_namespace = name_space
                            self.sid_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "src"):
                            self.src = value
                            self.src.value_namespace = name_space
                            self.src.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.policy_mi:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.policy_mi:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-ipv4-backup" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "policy-mi"):
                        for c in self.policy_mi:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.policy_mi.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "policy-mi"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PolicyIpv4Active(Entity):
                """
                IPv4 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Active, self).__init__()

                    self.yang_name = "policy-ipv4-active"
                    self.yang_parent_name = "policy-ipv4"

                    self.policy_mi = YList(self)

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
                                super(Srms.Policy.PolicyIpv4.PolicyIpv4Active, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Active, self).__setattr__(name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv4-active"

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mi_id",
                                        "area",
                                        "flag_attached",
                                        "last_prefix",
                                        "last_sid_index",
                                        "prefix_xr",
                                        "router",
                                        "sid_count",
                                        "sid_start",
                                        "src") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi, self).__setattr__(name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af",
                                            "ipv4",
                                            "ipv6") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af.is_set or
                                self.ipv4.is_set or
                                self.ipv6.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af.yfilter != YFilter.not_set or
                                self.ipv4.yfilter != YFilter.not_set or
                                self.ipv6.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af.get_name_leafdata())
                            if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4.get_name_leafdata())
                            if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af" or name == "ipv4" or name == "ipv6"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af"):
                                self.af = value
                                self.af.value_namespace = name_space
                                self.af.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4"):
                                self.ipv4 = value
                                self.ipv4.value_namespace = name_space
                                self.ipv4.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6"):
                                self.ipv6 = value
                                self.ipv6.value_namespace = name_space
                                self.ipv6.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mi_id.is_set or
                            self.area.is_set or
                            self.flag_attached.is_set or
                            self.last_prefix.is_set or
                            self.last_sid_index.is_set or
                            self.prefix_xr.is_set or
                            self.router.is_set or
                            self.sid_count.is_set or
                            self.sid_start.is_set or
                            self.src.is_set or
                            (self.addr is not None and self.addr.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mi_id.yfilter != YFilter.not_set or
                            self.area.yfilter != YFilter.not_set or
                            self.flag_attached.yfilter != YFilter.not_set or
                            self.last_prefix.yfilter != YFilter.not_set or
                            self.last_sid_index.yfilter != YFilter.not_set or
                            self.prefix_xr.yfilter != YFilter.not_set or
                            self.router.yfilter != YFilter.not_set or
                            self.sid_count.yfilter != YFilter.not_set or
                            self.sid_start.yfilter != YFilter.not_set or
                            self.src.yfilter != YFilter.not_set or
                            (self.addr is not None and self.addr.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "policy-mi" + "[mi-id='" + self.mi_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/policy-ipv4-active/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mi_id.is_set or self.mi_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mi_id.get_name_leafdata())
                        if (self.area.is_set or self.area.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.area.get_name_leafdata())
                        if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flag_attached.get_name_leafdata())
                        if (self.last_prefix.is_set or self.last_prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_prefix.get_name_leafdata())
                        if (self.last_sid_index.is_set or self.last_sid_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_sid_index.get_name_leafdata())
                        if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_xr.get_name_leafdata())
                        if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router.get_name_leafdata())
                        if (self.sid_count.is_set or self.sid_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_count.get_name_leafdata())
                        if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_start.get_name_leafdata())
                        if (self.src.is_set or self.src.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.src.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "addr"):
                            if (self.addr is None):
                                self.addr = Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr()
                                self.addr.parent = self
                                self._children_name_map["addr"] = "addr"
                            return self.addr

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "addr" or name == "mi-id" or name == "area" or name == "flag-attached" or name == "last-prefix" or name == "last-sid-index" or name == "prefix-xr" or name == "router" or name == "sid-count" or name == "sid-start" or name == "src"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mi-id"):
                            self.mi_id = value
                            self.mi_id.value_namespace = name_space
                            self.mi_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "area"):
                            self.area = value
                            self.area.value_namespace = name_space
                            self.area.value_namespace_prefix = name_space_prefix
                        if(value_path == "flag-attached"):
                            self.flag_attached = value
                            self.flag_attached.value_namespace = name_space
                            self.flag_attached.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-prefix"):
                            self.last_prefix = value
                            self.last_prefix.value_namespace = name_space
                            self.last_prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-sid-index"):
                            self.last_sid_index = value
                            self.last_sid_index.value_namespace = name_space
                            self.last_sid_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-xr"):
                            self.prefix_xr = value
                            self.prefix_xr.value_namespace = name_space
                            self.prefix_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "router"):
                            self.router = value
                            self.router.value_namespace = name_space
                            self.router.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-count"):
                            self.sid_count = value
                            self.sid_count.value_namespace = name_space
                            self.sid_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-start"):
                            self.sid_start = value
                            self.sid_start.value_namespace = name_space
                            self.sid_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "src"):
                            self.src = value
                            self.src.value_namespace = name_space
                            self.src.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.policy_mi:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.policy_mi:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-ipv4-active" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv4/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "policy-mi"):
                        for c in self.policy_mi:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.policy_mi.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "policy-mi"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.policy_ipv4_active is not None and self.policy_ipv4_active.has_data()) or
                    (self.policy_ipv4_backup is not None and self.policy_ipv4_backup.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.policy_ipv4_active is not None and self.policy_ipv4_active.has_operation()) or
                    (self.policy_ipv4_backup is not None and self.policy_ipv4_backup.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy-ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "policy-ipv4-active"):
                    if (self.policy_ipv4_active is None):
                        self.policy_ipv4_active = Srms.Policy.PolicyIpv4.PolicyIpv4Active()
                        self.policy_ipv4_active.parent = self
                        self._children_name_map["policy_ipv4_active"] = "policy-ipv4-active"
                    return self.policy_ipv4_active

                if (child_yang_name == "policy-ipv4-backup"):
                    if (self.policy_ipv4_backup is None):
                        self.policy_ipv4_backup = Srms.Policy.PolicyIpv4.PolicyIpv4Backup()
                        self.policy_ipv4_backup.parent = self
                        self._children_name_map["policy_ipv4_backup"] = "policy-ipv4-backup"
                    return self.policy_ipv4_backup

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "policy-ipv4-active" or name == "policy-ipv4-backup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PolicyIpv6(Entity):
            """
            IPv6 policy operational data
            
            .. attribute:: policy_ipv6_active
            
            	IPv6 active policy operational data
            	**type**\:   :py:class:`PolicyIpv6Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active>`
            
            .. attribute:: policy_ipv6_backup
            
            	IPv6 backup policy operational data
            	**type**\:   :py:class:`PolicyIpv6Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup>`
            
            

            """

            _prefix = 'segment-routing-ms-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Srms.Policy.PolicyIpv6, self).__init__()

                self.yang_name = "policy-ipv6"
                self.yang_parent_name = "policy"

                self.policy_ipv6_active = Srms.Policy.PolicyIpv6.PolicyIpv6Active()
                self.policy_ipv6_active.parent = self
                self._children_name_map["policy_ipv6_active"] = "policy-ipv6-active"
                self._children_yang_names.add("policy-ipv6-active")

                self.policy_ipv6_backup = Srms.Policy.PolicyIpv6.PolicyIpv6Backup()
                self.policy_ipv6_backup.parent = self
                self._children_name_map["policy_ipv6_backup"] = "policy-ipv6-backup"
                self._children_yang_names.add("policy-ipv6-backup")


            class PolicyIpv6Backup(Entity):
                """
                IPv6 backup policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, self).__init__()

                    self.yang_name = "policy-ipv6-backup"
                    self.yang_parent_name = "policy-ipv6"

                    self.policy_mi = YList(self)

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
                                super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup, self).__setattr__(name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-backup"

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mi_id",
                                        "area",
                                        "flag_attached",
                                        "last_prefix",
                                        "last_sid_index",
                                        "prefix_xr",
                                        "router",
                                        "sid_count",
                                        "sid_start",
                                        "src") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi, self).__setattr__(name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af",
                                            "ipv4",
                                            "ipv6") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af.is_set or
                                self.ipv4.is_set or
                                self.ipv6.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af.yfilter != YFilter.not_set or
                                self.ipv4.yfilter != YFilter.not_set or
                                self.ipv6.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af.get_name_leafdata())
                            if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4.get_name_leafdata())
                            if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af" or name == "ipv4" or name == "ipv6"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af"):
                                self.af = value
                                self.af.value_namespace = name_space
                                self.af.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4"):
                                self.ipv4 = value
                                self.ipv4.value_namespace = name_space
                                self.ipv4.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6"):
                                self.ipv6 = value
                                self.ipv6.value_namespace = name_space
                                self.ipv6.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mi_id.is_set or
                            self.area.is_set or
                            self.flag_attached.is_set or
                            self.last_prefix.is_set or
                            self.last_sid_index.is_set or
                            self.prefix_xr.is_set or
                            self.router.is_set or
                            self.sid_count.is_set or
                            self.sid_start.is_set or
                            self.src.is_set or
                            (self.addr is not None and self.addr.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mi_id.yfilter != YFilter.not_set or
                            self.area.yfilter != YFilter.not_set or
                            self.flag_attached.yfilter != YFilter.not_set or
                            self.last_prefix.yfilter != YFilter.not_set or
                            self.last_sid_index.yfilter != YFilter.not_set or
                            self.prefix_xr.yfilter != YFilter.not_set or
                            self.router.yfilter != YFilter.not_set or
                            self.sid_count.yfilter != YFilter.not_set or
                            self.sid_start.yfilter != YFilter.not_set or
                            self.src.yfilter != YFilter.not_set or
                            (self.addr is not None and self.addr.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "policy-mi" + "[mi-id='" + self.mi_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/policy-ipv6-backup/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mi_id.is_set or self.mi_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mi_id.get_name_leafdata())
                        if (self.area.is_set or self.area.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.area.get_name_leafdata())
                        if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flag_attached.get_name_leafdata())
                        if (self.last_prefix.is_set or self.last_prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_prefix.get_name_leafdata())
                        if (self.last_sid_index.is_set or self.last_sid_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_sid_index.get_name_leafdata())
                        if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_xr.get_name_leafdata())
                        if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router.get_name_leafdata())
                        if (self.sid_count.is_set or self.sid_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_count.get_name_leafdata())
                        if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_start.get_name_leafdata())
                        if (self.src.is_set or self.src.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.src.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "addr"):
                            if (self.addr is None):
                                self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr()
                                self.addr.parent = self
                                self._children_name_map["addr"] = "addr"
                            return self.addr

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "addr" or name == "mi-id" or name == "area" or name == "flag-attached" or name == "last-prefix" or name == "last-sid-index" or name == "prefix-xr" or name == "router" or name == "sid-count" or name == "sid-start" or name == "src"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mi-id"):
                            self.mi_id = value
                            self.mi_id.value_namespace = name_space
                            self.mi_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "area"):
                            self.area = value
                            self.area.value_namespace = name_space
                            self.area.value_namespace_prefix = name_space_prefix
                        if(value_path == "flag-attached"):
                            self.flag_attached = value
                            self.flag_attached.value_namespace = name_space
                            self.flag_attached.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-prefix"):
                            self.last_prefix = value
                            self.last_prefix.value_namespace = name_space
                            self.last_prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-sid-index"):
                            self.last_sid_index = value
                            self.last_sid_index.value_namespace = name_space
                            self.last_sid_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-xr"):
                            self.prefix_xr = value
                            self.prefix_xr.value_namespace = name_space
                            self.prefix_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "router"):
                            self.router = value
                            self.router.value_namespace = name_space
                            self.router.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-count"):
                            self.sid_count = value
                            self.sid_count.value_namespace = name_space
                            self.sid_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-start"):
                            self.sid_start = value
                            self.sid_start.value_namespace = name_space
                            self.sid_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "src"):
                            self.src = value
                            self.src.value_namespace = name_space
                            self.src.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.policy_mi:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.policy_mi:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-ipv6-backup" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "policy-mi"):
                        for c in self.policy_mi:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.policy_mi.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "policy-mi"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PolicyIpv6Active(Entity):
                """
                IPv6 active policy operational data
                
                .. attribute:: policy_mi
                
                	Mapping Item
                	**type**\: list of    :py:class:`PolicyMi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi>`
                
                

                """

                _prefix = 'segment-routing-ms-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Active, self).__init__()

                    self.yang_name = "policy-ipv6-active"
                    self.yang_parent_name = "policy-ipv6"

                    self.policy_mi = YList(self)

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
                                super(Srms.Policy.PolicyIpv6.PolicyIpv6Active, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Active, self).__setattr__(name, value)


                class PolicyMi(Entity):
                    """
                    Mapping Item
                    
                    .. attribute:: mi_id  <key>
                    
                    	Mapping Item ID (0, 1, 2, ...)
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: addr
                    
                    	addr
                    	**type**\:   :py:class:`Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr>`
                    
                    .. attribute:: area
                    
                    	Area (OSPF) or Level (ISIS)
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: flag_attached
                    
                    	Attached flag
                    	**type**\:   :py:class:`SrmsMiFlagEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiFlagEB>`
                    
                    .. attribute:: last_prefix
                    
                    	Last IP Prefix
                    	**type**\:  str
                    
                    	**length:** 0..50
                    
                    .. attribute:: last_sid_index
                    
                    	Last SID Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_xr
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: router
                    
                    	Router ID
                    	**type**\:  str
                    
                    	**length:** 0..30
                    
                    .. attribute:: sid_count
                    
                    	SID range
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sid_start
                    
                    	Starting SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: src
                    
                    	src
                    	**type**\:   :py:class:`SrmsMiSrcEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiSrcEB>`
                    
                    

                    """

                    _prefix = 'segment-routing-ms-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, self).__init__()

                        self.yang_name = "policy-mi"
                        self.yang_parent_name = "policy-ipv6-active"

                        self.mi_id = YLeaf(YType.str, "mi-id")

                        self.area = YLeaf(YType.str, "area")

                        self.flag_attached = YLeaf(YType.enumeration, "flag-attached")

                        self.last_prefix = YLeaf(YType.str, "last-prefix")

                        self.last_sid_index = YLeaf(YType.uint32, "last-sid-index")

                        self.prefix_xr = YLeaf(YType.uint8, "prefix-xr")

                        self.router = YLeaf(YType.str, "router")

                        self.sid_count = YLeaf(YType.uint32, "sid-count")

                        self.sid_start = YLeaf(YType.uint32, "sid-start")

                        self.src = YLeaf(YType.enumeration, "src")

                        self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr()
                        self.addr.parent = self
                        self._children_name_map["addr"] = "addr"
                        self._children_yang_names.add("addr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mi_id",
                                        "area",
                                        "flag_attached",
                                        "last_prefix",
                                        "last_sid_index",
                                        "prefix_xr",
                                        "router",
                                        "sid_count",
                                        "sid_start",
                                        "src") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi, self).__setattr__(name, value)


                    class Addr(Entity):
                        """
                        addr
                        
                        .. attribute:: af
                        
                        	AF
                        	**type**\:   :py:class:`SrmsMiAfEB <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper.SrmsMiAfEB>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'segment-routing-ms-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, self).__init__()

                            self.yang_name = "addr"
                            self.yang_parent_name = "policy-mi"

                            self.af = YLeaf(YType.enumeration, "af")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af",
                                            "ipv4",
                                            "ipv6") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af.is_set or
                                self.ipv4.is_set or
                                self.ipv6.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af.yfilter != YFilter.not_set or
                                self.ipv4.yfilter != YFilter.not_set or
                                self.ipv6.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af.get_name_leafdata())
                            if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4.get_name_leafdata())
                            if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af" or name == "ipv4" or name == "ipv6"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af"):
                                self.af = value
                                self.af.value_namespace = name_space
                                self.af.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4"):
                                self.ipv4 = value
                                self.ipv4.value_namespace = name_space
                                self.ipv4.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6"):
                                self.ipv6 = value
                                self.ipv6.value_namespace = name_space
                                self.ipv6.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mi_id.is_set or
                            self.area.is_set or
                            self.flag_attached.is_set or
                            self.last_prefix.is_set or
                            self.last_sid_index.is_set or
                            self.prefix_xr.is_set or
                            self.router.is_set or
                            self.sid_count.is_set or
                            self.sid_start.is_set or
                            self.src.is_set or
                            (self.addr is not None and self.addr.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mi_id.yfilter != YFilter.not_set or
                            self.area.yfilter != YFilter.not_set or
                            self.flag_attached.yfilter != YFilter.not_set or
                            self.last_prefix.yfilter != YFilter.not_set or
                            self.last_sid_index.yfilter != YFilter.not_set or
                            self.prefix_xr.yfilter != YFilter.not_set or
                            self.router.yfilter != YFilter.not_set or
                            self.sid_count.yfilter != YFilter.not_set or
                            self.sid_start.yfilter != YFilter.not_set or
                            self.src.yfilter != YFilter.not_set or
                            (self.addr is not None and self.addr.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "policy-mi" + "[mi-id='" + self.mi_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/policy-ipv6-active/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mi_id.is_set or self.mi_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mi_id.get_name_leafdata())
                        if (self.area.is_set or self.area.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.area.get_name_leafdata())
                        if (self.flag_attached.is_set or self.flag_attached.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flag_attached.get_name_leafdata())
                        if (self.last_prefix.is_set or self.last_prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_prefix.get_name_leafdata())
                        if (self.last_sid_index.is_set or self.last_sid_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_sid_index.get_name_leafdata())
                        if (self.prefix_xr.is_set or self.prefix_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_xr.get_name_leafdata())
                        if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.router.get_name_leafdata())
                        if (self.sid_count.is_set or self.sid_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_count.get_name_leafdata())
                        if (self.sid_start.is_set or self.sid_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sid_start.get_name_leafdata())
                        if (self.src.is_set or self.src.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.src.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "addr"):
                            if (self.addr is None):
                                self.addr = Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr()
                                self.addr.parent = self
                                self._children_name_map["addr"] = "addr"
                            return self.addr

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "addr" or name == "mi-id" or name == "area" or name == "flag-attached" or name == "last-prefix" or name == "last-sid-index" or name == "prefix-xr" or name == "router" or name == "sid-count" or name == "sid-start" or name == "src"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mi-id"):
                            self.mi_id = value
                            self.mi_id.value_namespace = name_space
                            self.mi_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "area"):
                            self.area = value
                            self.area.value_namespace = name_space
                            self.area.value_namespace_prefix = name_space_prefix
                        if(value_path == "flag-attached"):
                            self.flag_attached = value
                            self.flag_attached.value_namespace = name_space
                            self.flag_attached.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-prefix"):
                            self.last_prefix = value
                            self.last_prefix.value_namespace = name_space
                            self.last_prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-sid-index"):
                            self.last_sid_index = value
                            self.last_sid_index.value_namespace = name_space
                            self.last_sid_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-xr"):
                            self.prefix_xr = value
                            self.prefix_xr.value_namespace = name_space
                            self.prefix_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "router"):
                            self.router = value
                            self.router.value_namespace = name_space
                            self.router.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-count"):
                            self.sid_count = value
                            self.sid_count.value_namespace = name_space
                            self.sid_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "sid-start"):
                            self.sid_start = value
                            self.sid_start.value_namespace = name_space
                            self.sid_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "src"):
                            self.src = value
                            self.src.value_namespace = name_space
                            self.src.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.policy_mi:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.policy_mi:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-ipv6-active" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/policy-ipv6/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "policy-mi"):
                        for c in self.policy_mi:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.policy_mi.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "policy-mi"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.policy_ipv6_active is not None and self.policy_ipv6_active.has_data()) or
                    (self.policy_ipv6_backup is not None and self.policy_ipv6_backup.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.policy_ipv6_active is not None and self.policy_ipv6_active.has_operation()) or
                    (self.policy_ipv6_backup is not None and self.policy_ipv6_backup.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy-ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/policy/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "policy-ipv6-active"):
                    if (self.policy_ipv6_active is None):
                        self.policy_ipv6_active = Srms.Policy.PolicyIpv6.PolicyIpv6Active()
                        self.policy_ipv6_active.parent = self
                        self._children_name_map["policy_ipv6_active"] = "policy-ipv6-active"
                    return self.policy_ipv6_active

                if (child_yang_name == "policy-ipv6-backup"):
                    if (self.policy_ipv6_backup is None):
                        self.policy_ipv6_backup = Srms.Policy.PolicyIpv6.PolicyIpv6Backup()
                        self.policy_ipv6_backup.parent = self
                        self._children_name_map["policy_ipv6_backup"] = "policy-ipv6-backup"
                    return self.policy_ipv6_backup

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "policy-ipv6-active" or name == "policy-ipv6-backup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.policy_ipv4 is not None and self.policy_ipv4.has_data()) or
                (self.policy_ipv6 is not None and self.policy_ipv6.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.policy_ipv4 is not None and self.policy_ipv4.has_operation()) or
                (self.policy_ipv6 is not None and self.policy_ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "policy" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "policy-ipv4"):
                if (self.policy_ipv4 is None):
                    self.policy_ipv4 = Srms.Policy.PolicyIpv4()
                    self.policy_ipv4.parent = self
                    self._children_name_map["policy_ipv4"] = "policy-ipv4"
                return self.policy_ipv4

            if (child_yang_name == "policy-ipv6"):
                if (self.policy_ipv6 is None):
                    self.policy_ipv6 = Srms.Policy.PolicyIpv6()
                    self.policy_ipv6.parent = self
                    self._children_name_map["policy_ipv6"] = "policy-ipv6"
                return self.policy_ipv6

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "policy-ipv4" or name == "policy-ipv6"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mapping is not None and self.mapping.has_data()) or
            (self.policy is not None and self.policy.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mapping is not None and self.mapping.has_operation()) or
            (self.policy is not None and self.policy.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-segment-routing-ms-oper:srms" + path_buffer

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

        if (child_yang_name == "mapping"):
            if (self.mapping is None):
                self.mapping = Srms.Mapping()
                self.mapping.parent = self
                self._children_name_map["mapping"] = "mapping"
            return self.mapping

        if (child_yang_name == "policy"):
            if (self.policy is None):
                self.policy = Srms.Policy()
                self.policy.parent = self
                self._children_name_map["policy"] = "policy"
            return self.policy

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mapping" or name == "policy"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Srms()
        return self._top_entity

