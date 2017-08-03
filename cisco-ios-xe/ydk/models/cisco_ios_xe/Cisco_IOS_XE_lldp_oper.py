""" Cisco_IOS_XE_lldp_oper 

This module contains a collection of YANG definitions
for monitoring of LLDP state information.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LldpEntries(Entity):
    """
    Data nodes for lldp entries
    
    .. attribute:: lldp_entry
    
    	The list of LLDP entries
    	**type**\: list of    :py:class:`LldpEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper.LldpEntries.LldpEntry>`
    
    

    """

    _prefix = 'lldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LldpEntries, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp-entries"
        self.yang_parent_name = "Cisco-IOS-XE-lldp-oper"

        self.lldp_entry = YList(self)

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
                    super(LldpEntries, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(LldpEntries, self).__setattr__(name, value)


    class LldpEntry(Entity):
        """
        The list of LLDP entries
        
        .. attribute:: device_id  <key>
        
        	Device ID of the link
        	**type**\:  str
        
        .. attribute:: local_interface  <key>
        
        	Name of the local interface on the current device
        	**type**\:  str
        
        .. attribute:: connecting_interface  <key>
        
        	Name of the connected interface to 'local\-interface'
        	**type**\:  str
        
        .. attribute:: capabilities
        
        	LLD device capabilities
        	**type**\:   :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper.LldpEntries.LldpEntry.Capabilities>`
        
        .. attribute:: ttl
        
        	TTL denoting hold\-time of this link entry
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'lldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(LldpEntries.LldpEntry, self).__init__()

            self.yang_name = "lldp-entry"
            self.yang_parent_name = "lldp-entries"

            self.device_id = YLeaf(YType.str, "device-id")

            self.local_interface = YLeaf(YType.str, "local-interface")

            self.connecting_interface = YLeaf(YType.str, "connecting-interface")

            self.ttl = YLeaf(YType.uint32, "ttl")

            self.capabilities = LldpEntries.LldpEntry.Capabilities()
            self.capabilities.parent = self
            self._children_name_map["capabilities"] = "capabilities"
            self._children_yang_names.add("capabilities")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("device_id",
                            "local_interface",
                            "connecting_interface",
                            "ttl") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(LldpEntries.LldpEntry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LldpEntries.LldpEntry, self).__setattr__(name, value)


        class Capabilities(Entity):
            """
            LLD device capabilities
            
            .. attribute:: access_point
            
            	Access point
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: bridge
            
            	Bridge
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: docsis
            
            	Docsis
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: other
            
            	Other
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: repeater
            
            	Repeater
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: router
            
            	Router
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: station
            
            	Station
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: telephone
            
            	Phone
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'lldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(LldpEntries.LldpEntry.Capabilities, self).__init__()

                self.yang_name = "capabilities"
                self.yang_parent_name = "lldp-entry"

                self.access_point = YLeaf(YType.empty, "access-point")

                self.bridge = YLeaf(YType.empty, "bridge")

                self.docsis = YLeaf(YType.empty, "docsis")

                self.other = YLeaf(YType.empty, "other")

                self.repeater = YLeaf(YType.empty, "repeater")

                self.router = YLeaf(YType.empty, "router")

                self.station = YLeaf(YType.empty, "station")

                self.telephone = YLeaf(YType.empty, "telephone")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("access_point",
                                "bridge",
                                "docsis",
                                "other",
                                "repeater",
                                "router",
                                "station",
                                "telephone") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LldpEntries.LldpEntry.Capabilities, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LldpEntries.LldpEntry.Capabilities, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.access_point.is_set or
                    self.bridge.is_set or
                    self.docsis.is_set or
                    self.other.is_set or
                    self.repeater.is_set or
                    self.router.is_set or
                    self.station.is_set or
                    self.telephone.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.access_point.yfilter != YFilter.not_set or
                    self.bridge.yfilter != YFilter.not_set or
                    self.docsis.yfilter != YFilter.not_set or
                    self.other.yfilter != YFilter.not_set or
                    self.repeater.yfilter != YFilter.not_set or
                    self.router.yfilter != YFilter.not_set or
                    self.station.yfilter != YFilter.not_set or
                    self.telephone.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "capabilities" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.access_point.is_set or self.access_point.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access_point.get_name_leafdata())
                if (self.bridge.is_set or self.bridge.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bridge.get_name_leafdata())
                if (self.docsis.is_set or self.docsis.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.docsis.get_name_leafdata())
                if (self.other.is_set or self.other.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.other.get_name_leafdata())
                if (self.repeater.is_set or self.repeater.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.repeater.get_name_leafdata())
                if (self.router.is_set or self.router.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.router.get_name_leafdata())
                if (self.station.is_set or self.station.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.station.get_name_leafdata())
                if (self.telephone.is_set or self.telephone.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.telephone.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-point" or name == "bridge" or name == "docsis" or name == "other" or name == "repeater" or name == "router" or name == "station" or name == "telephone"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "access-point"):
                    self.access_point = value
                    self.access_point.value_namespace = name_space
                    self.access_point.value_namespace_prefix = name_space_prefix
                if(value_path == "bridge"):
                    self.bridge = value
                    self.bridge.value_namespace = name_space
                    self.bridge.value_namespace_prefix = name_space_prefix
                if(value_path == "docsis"):
                    self.docsis = value
                    self.docsis.value_namespace = name_space
                    self.docsis.value_namespace_prefix = name_space_prefix
                if(value_path == "other"):
                    self.other = value
                    self.other.value_namespace = name_space
                    self.other.value_namespace_prefix = name_space_prefix
                if(value_path == "repeater"):
                    self.repeater = value
                    self.repeater.value_namespace = name_space
                    self.repeater.value_namespace_prefix = name_space_prefix
                if(value_path == "router"):
                    self.router = value
                    self.router.value_namespace = name_space
                    self.router.value_namespace_prefix = name_space_prefix
                if(value_path == "station"):
                    self.station = value
                    self.station.value_namespace = name_space
                    self.station.value_namespace_prefix = name_space_prefix
                if(value_path == "telephone"):
                    self.telephone = value
                    self.telephone.value_namespace = name_space
                    self.telephone.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.device_id.is_set or
                self.local_interface.is_set or
                self.connecting_interface.is_set or
                self.ttl.is_set or
                (self.capabilities is not None and self.capabilities.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.device_id.yfilter != YFilter.not_set or
                self.local_interface.yfilter != YFilter.not_set or
                self.connecting_interface.yfilter != YFilter.not_set or
                self.ttl.yfilter != YFilter.not_set or
                (self.capabilities is not None and self.capabilities.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lldp-entry" + "[device-id='" + self.device_id.get() + "']" + "[local-interface='" + self.local_interface.get() + "']" + "[connecting-interface='" + self.connecting_interface.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-lldp-oper:lldp-entries/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.device_id.get_name_leafdata())
            if (self.local_interface.is_set or self.local_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.local_interface.get_name_leafdata())
            if (self.connecting_interface.is_set or self.connecting_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.connecting_interface.get_name_leafdata())
            if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ttl.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "capabilities"):
                if (self.capabilities is None):
                    self.capabilities = LldpEntries.LldpEntry.Capabilities()
                    self.capabilities.parent = self
                    self._children_name_map["capabilities"] = "capabilities"
                return self.capabilities

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "capabilities" or name == "device-id" or name == "local-interface" or name == "connecting-interface" or name == "ttl"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "device-id"):
                self.device_id = value
                self.device_id.value_namespace = name_space
                self.device_id.value_namespace_prefix = name_space_prefix
            if(value_path == "local-interface"):
                self.local_interface = value
                self.local_interface.value_namespace = name_space
                self.local_interface.value_namespace_prefix = name_space_prefix
            if(value_path == "connecting-interface"):
                self.connecting_interface = value
                self.connecting_interface.value_namespace = name_space
                self.connecting_interface.value_namespace_prefix = name_space_prefix
            if(value_path == "ttl"):
                self.ttl = value
                self.ttl.value_namespace = name_space
                self.ttl.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.lldp_entry:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.lldp_entry:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-lldp-oper:lldp-entries" + path_buffer

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

        if (child_yang_name == "lldp-entry"):
            for c in self.lldp_entry:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = LldpEntries.LldpEntry()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.lldp_entry.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "lldp-entry"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = LldpEntries()
        return self._top_entity

