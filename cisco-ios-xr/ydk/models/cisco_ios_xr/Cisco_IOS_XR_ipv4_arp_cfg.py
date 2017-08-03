""" Cisco_IOS_XR_ipv4_arp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-arp package configuration.

This module contains definitions
for the following management objects\:
  arp\: ARP configuraiton
  arpgmp\: arpgmp
  arp\-redundancy\: arp redundancy

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ArpEncap(Enum):
    """
    ArpEncap

    Arp encap

    .. data:: arpa = 1

    	Encapsulation type ARPA

    .. data:: srp = 4

    	Encapsulation type SRP

    .. data:: srpa = 5

    	Encapsulation type SRPA

    .. data:: srpb = 6

    	Encapsulation type SRPB

    """

    arpa = Enum.YLeaf(1, "arpa")

    srp = Enum.YLeaf(4, "srp")

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")


class ArpEntry(Enum):
    """
    ArpEntry

    Arp entry

    .. data:: static = 0

    	Static ARP entry type

    .. data:: alias = 1

    	Alias ARP entry type

    """

    static = Enum.YLeaf(0, "static")

    alias = Enum.YLeaf(1, "alias")



class Arp(Entity):
    """
    ARP configuraiton
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for arp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    .. attribute:: max_entries
    
    	Configure maximum number of safe ARP entries per line card
    	**type**\:  int
    
    	**range:** 1..256000
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for arp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Arp, self).__init__()
        self._top_entity = None

        self.yang_name = "arp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"

        self.inner_cos = YLeaf(YType.uint32, "inner-cos")

        self.max_entries = YLeaf(YType.uint32, "max-entries")

        self.outer_cos = YLeaf(YType.uint32, "outer-cos")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("inner_cos",
                        "max_entries",
                        "outer_cos") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Arp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Arp, self).__setattr__(name, value)

    def has_data(self):
        return (
            self.inner_cos.is_set or
            self.max_entries.is_set or
            self.outer_cos.is_set)

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.inner_cos.yfilter != YFilter.not_set or
            self.max_entries.yfilter != YFilter.not_set or
            self.outer_cos.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
            leaf_name_data.append(self.inner_cos.get_name_leafdata())
        if (self.max_entries.is_set or self.max_entries.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max_entries.get_name_leafdata())
        if (self.outer_cos.is_set or self.outer_cos.yfilter != YFilter.not_set):
            leaf_name_data.append(self.outer_cos.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "inner-cos" or name == "max-entries" or name == "outer-cos"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "inner-cos"):
            self.inner_cos = value
            self.inner_cos.value_namespace = name_space
            self.inner_cos.value_namespace_prefix = name_space_prefix
        if(value_path == "max-entries"):
            self.max_entries = value
            self.max_entries.value_namespace = name_space
            self.max_entries.value_namespace_prefix = name_space_prefix
        if(value_path == "outer-cos"):
            self.outer_cos = value
            self.outer_cos.value_namespace = name_space
            self.outer_cos.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Arp()
        return self._top_entity

class Arpgmp(Entity):
    """
    arpgmp
    
    .. attribute:: vrf
    
    	Per VRF configuration, for the default VRF use 'default'
    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf>`
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Arpgmp, self).__init__()
        self._top_entity = None

        self.yang_name = "arpgmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"

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
                    super(Arpgmp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Arpgmp, self).__setattr__(name, value)


    class Vrf(Entity):
        """
        Per VRF configuration, for the default VRF use
        'default'
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: entries
        
        	ARP static and alias entry configuration
        	**type**\:   :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries>`
        
        

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Arpgmp.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "arpgmp"

            self.vrf_name = YLeaf(YType.str, "vrf-name")

            self.entries = Arpgmp.Vrf.Entries()
            self.entries.parent = self
            self._children_name_map["entries"] = "entries"
            self._children_yang_names.add("entries")

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
                        super(Arpgmp.Vrf, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Arpgmp.Vrf, self).__setattr__(name, value)


        class Entries(Entity):
            """
            ARP static and alias entry configuration
            
            .. attribute:: entry
            
            	ARP static and alias entry configuration item
            	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries.Entry>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Arpgmp.Vrf.Entries, self).__init__()

                self.yang_name = "entries"
                self.yang_parent_name = "vrf"

                self.entry = YList(self)

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
                            super(Arpgmp.Vrf.Entries, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Arpgmp.Vrf.Entries, self).__setattr__(name, value)


            class Entry(Entity):
                """
                ARP static and alias entry configuration item
                
                .. attribute:: address  <key>
                
                	IP Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: encapsulation
                
                	Encapsulation type
                	**type**\:   :py:class:`ArpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpEncap>`
                
                .. attribute:: entry_type
                
                	Entry type
                	**type**\:   :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpEntry>`
                
                .. attribute:: interface
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Arpgmp.Vrf.Entries.Entry, self).__init__()

                    self.yang_name = "entry"
                    self.yang_parent_name = "entries"

                    self.address = YLeaf(YType.str, "address")

                    self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                    self.entry_type = YLeaf(YType.enumeration, "entry-type")

                    self.interface = YLeaf(YType.str, "interface")

                    self.mac_address = YLeaf(YType.str, "mac-address")

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
                                    "encapsulation",
                                    "entry_type",
                                    "interface",
                                    "mac_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arpgmp.Vrf.Entries.Entry, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arpgmp.Vrf.Entries.Entry, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.encapsulation.is_set or
                        self.entry_type.is_set or
                        self.interface.is_set or
                        self.mac_address.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.encapsulation.yfilter != YFilter.not_set or
                        self.entry_type.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.mac_address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "entry" + "[address='" + self.address.get() + "']" + path_buffer

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
                    if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encapsulation.get_name_leafdata())
                    if (self.entry_type.is_set or self.entry_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.entry_type.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "encapsulation" or name == "entry-type" or name == "interface" or name == "mac-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "encapsulation"):
                        self.encapsulation = value
                        self.encapsulation.value_namespace = name_space
                        self.encapsulation.value_namespace_prefix = name_space_prefix
                    if(value_path == "entry-type"):
                        self.entry_type = value
                        self.entry_type.value_namespace = name_space
                        self.entry_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-address"):
                        self.mac_address = value
                        self.mac_address.value_namespace = name_space
                        self.mac_address.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.entry:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.entry:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entries" + path_buffer

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

                if (child_yang_name == "entry"):
                    for c in self.entry:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Arpgmp.Vrf.Entries.Entry()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.entry.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entry"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.vrf_name.is_set or
                (self.entries is not None and self.entries.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vrf_name.yfilter != YFilter.not_set or
                (self.entries is not None and self.entries.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arpgmp/%s" % self.get_segment_path()
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

            if (child_yang_name == "entries"):
                if (self.entries is None):
                    self.entries = Arpgmp.Vrf.Entries()
                    self.entries.parent = self
                    self._children_name_map["entries"] = "entries"
                return self.entries

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entries" or name == "vrf-name"):
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
        path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arpgmp" + path_buffer

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

        if (child_yang_name == "vrf"):
            for c in self.vrf:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Arpgmp.Vrf()
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

    def clone_ptr(self):
        self._top_entity = Arpgmp()
        return self._top_entity

class ArpRedundancy(Entity):
    """
    arp redundancy
    
    .. attribute:: redundancy
    
    	Configure parameter for ARP Geo redundancy
    	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ArpRedundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "arp-redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"

        self.redundancy = None
        self._children_name_map["redundancy"] = "redundancy"
        self._children_yang_names.add("redundancy")


    class Redundancy(Entity):
        """
        Configure parameter for ARP Geo redundancy
        
        .. attribute:: enable
        
        	Enable Configure parameter for ARP Geo redundancy. Deletion of this object also causes deletion of all associated objects under ArpRedundancy
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: groups
        
        	Table of Group
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ArpRedundancy.Redundancy, self).__init__()

            self.yang_name = "redundancy"
            self.yang_parent_name = "arp-redundancy"
            self.is_presence_container = True

            self.enable = YLeaf(YType.empty, "enable")

            self.groups = ArpRedundancy.Redundancy.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ArpRedundancy.Redundancy, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ArpRedundancy.Redundancy, self).__setattr__(name, value)


        class Groups(Entity):
            """
            Table of Group
            
            .. attribute:: group
            
            	None
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ArpRedundancy.Redundancy.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "redundancy"

                self.group = YList(self)

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
                            super(ArpRedundancy.Redundancy.Groups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ArpRedundancy.Redundancy.Groups, self).__setattr__(name, value)


            class Group(Entity):
                """
                None
                
                .. attribute:: group_id  <key>
                
                	Group ID
                	**type**\:  int
                
                	**range:** 1..32
                
                .. attribute:: interface_list
                
                	List of Interfaces for this Group
                	**type**\:   :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList>`
                
                	**presence node**\: True
                
                .. attribute:: peers
                
                	Table of Peer
                	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers>`
                
                .. attribute:: source_interface
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ArpRedundancy.Redundancy.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"

                    self.group_id = YLeaf(YType.uint32, "group-id")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.interface_list = None
                    self._children_name_map["interface_list"] = "interface-list"
                    self._children_yang_names.add("interface-list")

                    self.peers = ArpRedundancy.Redundancy.Groups.Group.Peers()
                    self.peers.parent = self
                    self._children_name_map["peers"] = "peers"
                    self._children_yang_names.add("peers")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_id",
                                    "source_interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ArpRedundancy.Redundancy.Groups.Group, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ArpRedundancy.Redundancy.Groups.Group, self).__setattr__(name, value)


                class Peers(Entity):
                    """
                    Table of Peer
                    
                    .. attribute:: peer
                    
                    	None
                    	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers.Peer>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ArpRedundancy.Redundancy.Groups.Group.Peers, self).__init__()

                        self.yang_name = "peers"
                        self.yang_parent_name = "group"

                        self.peer = YList(self)

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
                                    super(ArpRedundancy.Redundancy.Groups.Group.Peers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ArpRedundancy.Redundancy.Groups.Group.Peers, self).__setattr__(name, value)


                    class Peer(Entity):
                        """
                        None
                        
                        .. attribute:: prefix_string  <key>
                        
                        	Neighbor IPv4 address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, self).__init__()

                            self.yang_name = "peer"
                            self.yang_parent_name = "peers"

                            self.prefix_string = YLeaf(YType.str, "prefix-string")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("prefix_string") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, self).__setattr__(name, value)

                        def has_data(self):
                            return self.prefix_string.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.prefix_string.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer" + "[prefix-string='" + self.prefix_string.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.prefix_string.is_set or self.prefix_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_string.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prefix-string"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "prefix-string"):
                                self.prefix_string = value
                                self.prefix_string.value_namespace = name_space
                                self.prefix_string.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.peer:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.peer:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peers" + path_buffer

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

                        if (child_yang_name == "peer"):
                            for c in self.peer:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ArpRedundancy.Redundancy.Groups.Group.Peers.Peer()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.peer.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class InterfaceList(Entity):
                    """
                    List of Interfaces for this Group
                    
                    .. attribute:: enable
                    
                    	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interfaces
                    
                    	Table of Interface
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList, self).__init__()

                        self.yang_name = "interface-list"
                        self.yang_parent_name = "group"
                        self.is_presence_container = True

                        self.enable = YLeaf(YType.empty, "enable")

                        self.interfaces = ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList, self).__setattr__(name, value)


                    class Interfaces(Entity):
                        """
                        Table of Interface
                        
                        .. attribute:: interface
                        
                        	Interface for this Group
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "interface-list"

                            self.interface = YList(self)

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
                                        super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            Interface for this Group
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: interface_id
                            
                            	Interface Id for the interface
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-arp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.interface_id = YLeaf(YType.uint32, "interface-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface_name",
                                                "interface_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.interface_name.is_set or
                                    self.interface_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.interface_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.interface_id.is_set or self.interface_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-name" or name == "interface-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-id"):
                                    self.interface_id = value
                                    self.interface_id.value_namespace = name_space
                                    self.interface_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.interface:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.interface:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interfaces" + path_buffer

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

                            if (child_yang_name == "interface"):
                                for c in self.interface:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.interface.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.enable.is_set or
                            (self.interfaces is not None and self.interfaces.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.interfaces is not None and self.interfaces.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-list" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interfaces"):
                            if (self.interfaces is None):
                                self.interfaces = ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"
                            return self.interfaces

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interfaces" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.group_id.is_set or
                        self.source_interface.is_set or
                        (self.peers is not None and self.peers.has_data()) or
                        (self.interface_list is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_id.yfilter != YFilter.not_set or
                        self.source_interface.yfilter != YFilter.not_set or
                        (self.interface_list is not None and self.interface_list.has_operation()) or
                        (self.peers is not None and self.peers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/redundancy/groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_id.get_name_leafdata())
                    if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-list"):
                        if (self.interface_list is None):
                            self.interface_list = ArpRedundancy.Redundancy.Groups.Group.InterfaceList()
                            self.interface_list.parent = self
                            self._children_name_map["interface_list"] = "interface-list"
                        return self.interface_list

                    if (child_yang_name == "peers"):
                        if (self.peers is None):
                            self.peers = ArpRedundancy.Redundancy.Groups.Group.Peers()
                            self.peers.parent = self
                            self._children_name_map["peers"] = "peers"
                        return self.peers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-list" or name == "peers" or name == "group-id" or name == "source-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-id"):
                        self.group_id = value
                        self.group_id.value_namespace = name_space
                        self.group_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface"):
                        self.source_interface = value
                        self.source_interface.value_namespace = name_space
                        self.source_interface.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/redundancy/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group"):
                    for c in self.group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ArpRedundancy.Redundancy.Groups.Group()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.enable.is_set or
                (self.groups is not None and self.groups.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.groups is not None and self.groups.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "redundancy" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "groups"):
                if (self.groups is None):
                    self.groups = ArpRedundancy.Redundancy.Groups()
                    self.groups.parent = self
                    self._children_name_map["groups"] = "groups"
                return self.groups

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "groups" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.redundancy is not None)

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.redundancy is not None and self.redundancy.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy" + path_buffer

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

        if (child_yang_name == "redundancy"):
            if (self.redundancy is None):
                self.redundancy = ArpRedundancy.Redundancy()
                self.redundancy.parent = self
                self._children_name_map["redundancy"] = "redundancy"
            return self.redundancy

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "redundancy"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ArpRedundancy()
        return self._top_entity

