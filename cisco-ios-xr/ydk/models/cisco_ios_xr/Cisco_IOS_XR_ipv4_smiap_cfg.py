""" Cisco_IOS_XR_ipv4_smiap_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-smiap package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-virtual\: IPv4 virtual address for management interfaces

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ipv4Virtual(Entity):
    """
    IPv4 virtual address for management interfaces
    
    .. attribute:: use_as_source_address
    
    	Enable use as default source address on sourced packets
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: vrfs
    
    	VRFs for the virtual IPv4 addresses
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs>`
    
    

    """

    _prefix = 'ipv4-smiap-cfg'
    _revision = '2016-07-04'

    def __init__(self):
        super(Ipv4Virtual, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-virtual"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-smiap-cfg"

        self.use_as_source_address = YLeaf(YType.empty, "use-as-source-address")

        self.vrfs = Ipv4Virtual.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("use_as_source_address") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ipv4Virtual, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ipv4Virtual, self).__setattr__(name, value)


    class Vrfs(Entity):
        """
        VRFs for the virtual IPv4 addresses
        
        .. attribute:: vrf
        
        	A VRF for a virtual IPv4 address.  Specify 'default' for VRF default
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-smiap-cfg'
        _revision = '2016-07-04'

        def __init__(self):
            super(Ipv4Virtual.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ipv4-virtual"

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
                        super(Ipv4Virtual.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Virtual.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            A VRF for a virtual IPv4 address.  Specify
            'default' for VRF default
            
            .. attribute:: vrf_name  <key>
            
            	Name of VRF
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	IPv4 sddress and mask
            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs.Vrf.Address>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-smiap-cfg'
            _revision = '2016-07-04'

            def __init__(self):
                super(Ipv4Virtual.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.address = None
                self._children_name_map["address"] = "address"
                self._children_yang_names.add("address")

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
                            super(Ipv4Virtual.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Virtual.Vrfs.Vrf, self).__setattr__(name, value)


            class Address(Entity):
                """
                IPv4 sddress and mask
                
                .. attribute:: address
                
                	IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                .. attribute:: netmask
                
                	IPv4 address mask
                	**type**\:  int
                
                	**range:** 0..32
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-smiap-cfg'
                _revision = '2016-07-04'

                def __init__(self):
                    super(Ipv4Virtual.Vrfs.Vrf.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "vrf"
                    self.is_presence_container = True

                    self.address = YLeaf(YType.str, "address")

                    self.netmask = YLeaf(YType.uint8, "netmask")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "netmask") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Virtual.Vrfs.Vrf.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Virtual.Vrfs.Vrf.Address, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.netmask.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.netmask.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "address" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.netmask.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "netmask"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "netmask"):
                        self.netmask = value
                        self.netmask.value_namespace = name_space
                        self.netmask.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.address is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.address is not None and self.address.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual/vrfs/%s" % self.get_segment_path()
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

                if (child_yang_name == "address"):
                    if (self.address is None):
                        self.address = Ipv4Virtual.Vrfs.Vrf.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                    return self.address

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "vrf-name"):
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
                path_buffer = "Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual/%s" % self.get_segment_path()
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
                c = Ipv4Virtual.Vrfs.Vrf()
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
        return (
            self.use_as_source_address.is_set or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.use_as_source_address.yfilter != YFilter.not_set or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.use_as_source_address.is_set or self.use_as_source_address.yfilter != YFilter.not_set):
            leaf_name_data.append(self.use_as_source_address.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Ipv4Virtual.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vrfs" or name == "use-as-source-address"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "use-as-source-address"):
            self.use_as_source_address = value
            self.use_as_source_address.value_namespace = name_space
            self.use_as_source_address.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ipv4Virtual()
        return self._top_entity

