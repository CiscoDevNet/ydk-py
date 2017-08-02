""" Cisco_IOS_XR_fia_hw_profile_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-hw\-profile package configuration.

This module contains definitions
for the following management objects\:
  hw\-module\-profile\-config\: none

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HwModuleProfileConfig(Entity):
    """
    none
    
    .. attribute:: fib_scale
    
    	Configure Fib for Scale for noTcam LC
    	**type**\:   :py:class:`FibScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale>`
    
    .. attribute:: profile
    
    	Configure profile
    	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile>`
    
    .. attribute:: tcam
    
    	Configure Tcam
    	**type**\:   :py:class:`Tcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam>`
    
    

    """

    _prefix = 'fia-hw-profile-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        super(HwModuleProfileConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module-profile-config"
        self.yang_parent_name = "Cisco-IOS-XR-fia-hw-profile-cfg"

        self.fib_scale = HwModuleProfileConfig.FibScale()
        self.fib_scale.parent = self
        self._children_name_map["fib_scale"] = "fib-scale"
        self._children_yang_names.add("fib-scale")

        self.profile = HwModuleProfileConfig.Profile()
        self.profile.parent = self
        self._children_name_map["profile"] = "profile"
        self._children_yang_names.add("profile")

        self.tcam = HwModuleProfileConfig.Tcam()
        self.tcam.parent = self
        self._children_name_map["tcam"] = "tcam"
        self._children_yang_names.add("tcam")


    class Profile(Entity):
        """
        Configure profile.
        
        .. attribute:: tcam_table
        
        	Configure profile for TCAM LC cards
        	**type**\:   :py:class:`TcamTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Profile, self).__init__()

            self.yang_name = "profile"
            self.yang_parent_name = "hw-module-profile-config"

            self.tcam_table = HwModuleProfileConfig.Profile.TcamTable()
            self.tcam_table.parent = self
            self._children_name_map["tcam_table"] = "tcam-table"
            self._children_yang_names.add("tcam-table")


        class TcamTable(Entity):
            """
            Configure profile for TCAM LC cards
            
            .. attribute:: fib_table
            
            	FIB table for TCAM LC cards
            	**type**\:   :py:class:`FibTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.TcamTable, self).__init__()

                self.yang_name = "tcam-table"
                self.yang_parent_name = "profile"

                self.fib_table = HwModuleProfileConfig.Profile.TcamTable.FibTable()
                self.fib_table.parent = self
                self._children_name_map["fib_table"] = "fib-table"
                self._children_yang_names.add("fib-table")


            class FibTable(Entity):
                """
                FIB table for TCAM LC cards
                
                .. attribute:: ipv4_address
                
                	IPv4 table for TCAM LC cards
                	**type**\:   :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address>`
                
                .. attribute:: ipv6_address
                
                	IPv6 table for TCAM LC cards
                	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable, self).__init__()

                    self.yang_name = "fib-table"
                    self.yang_parent_name = "tcam-table"

                    self.ipv4_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address()
                    self.ipv4_address.parent = self
                    self._children_name_map["ipv4_address"] = "ipv4-address"
                    self._children_yang_names.add("ipv4-address")

                    self.ipv6_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address()
                    self.ipv6_address.parent = self
                    self._children_name_map["ipv6_address"] = "ipv6-address"
                    self._children_yang_names.add("ipv6-address")


                class Ipv4Address(Entity):
                    """
                    IPv4 table for TCAM LC cards
                    
                    .. attribute:: ipv4_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:   :py:class:`Ipv4Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address, self).__init__()

                        self.yang_name = "ipv4-address"
                        self.yang_parent_name = "fib-table"

                        self.ipv4_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                        self._children_yang_names.add("ipv4-unicast")


                    class Ipv4Unicast(Entity):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv4_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        .. attribute:: ipv4_unicast_prefix_lengths
                        
                        	IPv4 Unicast prefix 
                        	**type**\:   :py:class:`Ipv4UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, self).__init__()

                            self.yang_name = "ipv4-unicast"
                            self.yang_parent_name = "ipv4-address"

                            self.ipv4_unicast_percent = YLeaf(YType.uint32, "ipv4-unicast-percent")

                            self.ipv4_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths()
                            self.ipv4_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv4_unicast_prefix_lengths"] = "ipv4-unicast-prefix-lengths"
                            self._children_yang_names.add("ipv4-unicast-prefix-lengths")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv4_unicast_percent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, self).__setattr__(name, value)


                        class Ipv4UnicastPrefixLengths(Entity):
                            """
                            IPv4 Unicast prefix 
                            
                            .. attribute:: ipv4_unicast_prefix_length
                            
                            	IPv4 Unicast prefix length
                            	**type**\: list of    :py:class:`Ipv4UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, self).__init__()

                                self.yang_name = "ipv4-unicast-prefix-lengths"
                                self.yang_parent_name = "ipv4-unicast"

                                self.ipv4_unicast_prefix_length = YList(self)

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
                                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, self).__setattr__(name, value)


                            class Ipv4UnicastPrefixLength(Entity):
                                """
                                IPv4 Unicast prefix length
                                
                                .. attribute:: prefix_length  <key>
                                
                                	prefix length
                                	**type**\:  int
                                
                                	**range:** 0..32
                                
                                .. attribute:: ipv4_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\:  str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, self).__init__()

                                    self.yang_name = "ipv4-unicast-prefix-length"
                                    self.yang_parent_name = "ipv4-unicast-prefix-lengths"

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                    self.ipv4_unicast_prefix_percent = YLeaf(YType.str, "ipv4-unicast-prefix-percent")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("prefix_length",
                                                    "ipv4_unicast_prefix_percent") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.prefix_length.is_set or
                                        self.ipv4_unicast_prefix_percent.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set or
                                        self.ipv4_unicast_prefix_percent.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv4-unicast-prefix-length" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/ipv4-unicast-prefix-lengths/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                    if (self.ipv4_unicast_prefix_percent.is_set or self.ipv4_unicast_prefix_percent.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_unicast_prefix_percent.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "prefix-length" or name == "ipv4-unicast-prefix-percent"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv4-unicast-prefix-percent"):
                                        self.ipv4_unicast_prefix_percent = value
                                        self.ipv4_unicast_prefix_percent.value_namespace = name_space
                                        self.ipv4_unicast_prefix_percent.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.ipv4_unicast_prefix_length:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.ipv4_unicast_prefix_length:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-unicast-prefix-lengths" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "ipv4-unicast-prefix-length"):
                                    for c in self.ipv4_unicast_prefix_length:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.ipv4_unicast_prefix_length.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-unicast-prefix-length"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.ipv4_unicast_percent.is_set or
                                (self.ipv4_unicast_prefix_lengths is not None and self.ipv4_unicast_prefix_lengths.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv4_unicast_percent.yfilter != YFilter.not_set or
                                (self.ipv4_unicast_prefix_lengths is not None and self.ipv4_unicast_prefix_lengths.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4-unicast" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv4_unicast_percent.is_set or self.ipv4_unicast_percent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_unicast_percent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv4-unicast-prefix-lengths"):
                                if (self.ipv4_unicast_prefix_lengths is None):
                                    self.ipv4_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths()
                                    self.ipv4_unicast_prefix_lengths.parent = self
                                    self._children_name_map["ipv4_unicast_prefix_lengths"] = "ipv4-unicast-prefix-lengths"
                                return self.ipv4_unicast_prefix_lengths

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-unicast-prefix-lengths" or name == "ipv4-unicast-percent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv4-unicast-percent"):
                                self.ipv4_unicast_percent = value
                                self.ipv4_unicast_percent.value_namespace = name_space
                                self.ipv4_unicast_percent.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.ipv4_unicast is not None and self.ipv4_unicast.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.ipv4_unicast is not None and self.ipv4_unicast.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-address" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ipv4-unicast"):
                            if (self.ipv4_unicast is None):
                                self.ipv4_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast()
                                self.ipv4_unicast.parent = self
                                self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                            return self.ipv4_unicast

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4-unicast"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Ipv6Address(Entity):
                    """
                    IPv6 table for TCAM LC cards
                    
                    .. attribute:: ipv6_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:   :py:class:`Ipv6Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address, self).__init__()

                        self.yang_name = "ipv6-address"
                        self.yang_parent_name = "fib-table"

                        self.ipv6_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                        self._children_yang_names.add("ipv6-unicast")


                    class Ipv6Unicast(Entity):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv6_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        .. attribute:: ipv6_unicast_prefix_lengths
                        
                        	IPv6 Unicast prefix 
                        	**type**\:   :py:class:`Ipv6UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, self).__init__()

                            self.yang_name = "ipv6-unicast"
                            self.yang_parent_name = "ipv6-address"

                            self.ipv6_unicast_percent = YLeaf(YType.uint32, "ipv6-unicast-percent")

                            self.ipv6_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths()
                            self.ipv6_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv6_unicast_prefix_lengths"] = "ipv6-unicast-prefix-lengths"
                            self._children_yang_names.add("ipv6-unicast-prefix-lengths")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_unicast_percent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, self).__setattr__(name, value)


                        class Ipv6UnicastPrefixLengths(Entity):
                            """
                            IPv6 Unicast prefix 
                            
                            .. attribute:: ipv6_unicast_prefix_length
                            
                            	IPv6 Unicast prefix length
                            	**type**\: list of    :py:class:`Ipv6UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, self).__init__()

                                self.yang_name = "ipv6-unicast-prefix-lengths"
                                self.yang_parent_name = "ipv6-unicast"

                                self.ipv6_unicast_prefix_length = YList(self)

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
                                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, self).__setattr__(name, value)


                            class Ipv6UnicastPrefixLength(Entity):
                                """
                                IPv6 Unicast prefix length
                                
                                .. attribute:: prefix_length  <key>
                                
                                	prefix length
                                	**type**\:  int
                                
                                	**range:** 0..128
                                
                                .. attribute:: ipv6_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\:  str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, self).__init__()

                                    self.yang_name = "ipv6-unicast-prefix-length"
                                    self.yang_parent_name = "ipv6-unicast-prefix-lengths"

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                    self.ipv6_unicast_prefix_percent = YLeaf(YType.str, "ipv6-unicast-prefix-percent")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("prefix_length",
                                                    "ipv6_unicast_prefix_percent") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.prefix_length.is_set or
                                        self.ipv6_unicast_prefix_percent.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set or
                                        self.ipv6_unicast_prefix_percent.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv6-unicast-prefix-length" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/ipv6-unicast-prefix-lengths/%s" % self.get_segment_path()
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                    if (self.ipv6_unicast_prefix_percent.is_set or self.ipv6_unicast_prefix_percent.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_unicast_prefix_percent.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "prefix-length" or name == "ipv6-unicast-prefix-percent"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv6-unicast-prefix-percent"):
                                        self.ipv6_unicast_prefix_percent = value
                                        self.ipv6_unicast_prefix_percent.value_namespace = name_space
                                        self.ipv6_unicast_prefix_percent.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.ipv6_unicast_prefix_length:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.ipv6_unicast_prefix_length:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-unicast-prefix-lengths" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "ipv6-unicast-prefix-length"):
                                    for c in self.ipv6_unicast_prefix_length:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.ipv6_unicast_prefix_length.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv6-unicast-prefix-length"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.ipv6_unicast_percent.is_set or
                                (self.ipv6_unicast_prefix_lengths is not None and self.ipv6_unicast_prefix_lengths.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_unicast_percent.yfilter != YFilter.not_set or
                                (self.ipv6_unicast_prefix_lengths is not None and self.ipv6_unicast_prefix_lengths.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6-unicast" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_unicast_percent.is_set or self.ipv6_unicast_percent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_unicast_percent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv6-unicast-prefix-lengths"):
                                if (self.ipv6_unicast_prefix_lengths is None):
                                    self.ipv6_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths()
                                    self.ipv6_unicast_prefix_lengths.parent = self
                                    self._children_name_map["ipv6_unicast_prefix_lengths"] = "ipv6-unicast-prefix-lengths"
                                return self.ipv6_unicast_prefix_lengths

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-unicast-prefix-lengths" or name == "ipv6-unicast-percent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-unicast-percent"):
                                self.ipv6_unicast_percent = value
                                self.ipv6_unicast_percent.value_namespace = name_space
                                self.ipv6_unicast_percent.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.ipv6_unicast is not None and self.ipv6_unicast.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.ipv6_unicast is not None and self.ipv6_unicast.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-address" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ipv6-unicast"):
                            if (self.ipv6_unicast is None):
                                self.ipv6_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast()
                                self.ipv6_unicast.parent = self
                                self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                            return self.ipv6_unicast

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv6-unicast"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.ipv4_address is not None and self.ipv4_address.has_data()) or
                        (self.ipv6_address is not None and self.ipv6_address.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipv4_address is not None and self.ipv4_address.has_operation()) or
                        (self.ipv6_address is not None and self.ipv6_address.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "fib-table" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/%s" % self.get_segment_path()
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
                        if (self.ipv4_address is None):
                            self.ipv4_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address()
                            self.ipv4_address.parent = self
                            self._children_name_map["ipv4_address"] = "ipv4-address"
                        return self.ipv4_address

                    if (child_yang_name == "ipv6-address"):
                        if (self.ipv6_address is None):
                            self.ipv6_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address()
                            self.ipv6_address.parent = self
                            self._children_name_map["ipv6_address"] = "ipv6-address"
                        return self.ipv6_address

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-address" or name == "ipv6-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.fib_table is not None and self.fib_table.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.fib_table is not None and self.fib_table.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tcam-table" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "fib-table"):
                    if (self.fib_table is None):
                        self.fib_table = HwModuleProfileConfig.Profile.TcamTable.FibTable()
                        self.fib_table.parent = self
                        self._children_name_map["fib_table"] = "fib-table"
                    return self.fib_table

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "fib-table"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.tcam_table is not None and self.tcam_table.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.tcam_table is not None and self.tcam_table.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "profile" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tcam-table"):
                if (self.tcam_table is None):
                    self.tcam_table = HwModuleProfileConfig.Profile.TcamTable()
                    self.tcam_table.parent = self
                    self._children_name_map["tcam_table"] = "tcam-table"
                return self.tcam_table

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcam-table"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class FibScale(Entity):
        """
        Configure Fib for Scale for noTcam LC.
        
        .. attribute:: ipv4_unicast_scale_no_tcam
        
        	IPv4 table for NOTCAM LC Scale
        	**type**\:   :py:class:`Ipv4UnicastScaleNoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam>`
        
        .. attribute:: ipv6_unicast_scale_no_tcam
        
        	IPv6 table for NOTCAM LC Scale
        	**type**\:   :py:class:`Ipv6UnicastScaleNoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.FibScale, self).__init__()

            self.yang_name = "fib-scale"
            self.yang_parent_name = "hw-module-profile-config"

            self.ipv4_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam()
            self.ipv4_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv4_unicast_scale_no_tcam"] = "ipv4-unicast-scale-no-tcam"
            self._children_yang_names.add("ipv4-unicast-scale-no-tcam")

            self.ipv6_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam()
            self.ipv6_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv6_unicast_scale_no_tcam"] = "ipv6-unicast-scale-no-tcam"
            self._children_yang_names.add("ipv6-unicast-scale-no-tcam")


        class Ipv6UnicastScaleNoTcam(Entity):
            """
            IPv6 table for NOTCAM LC Scale.
            
            .. attribute:: scale_ipv6_no_tcam
            
            	Scale for IPv6 table for NoTCAM LC
            	**type**\:   :py:class:`ScaleIpv6NoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam, self).__init__()

                self.yang_name = "ipv6-unicast-scale-no-tcam"
                self.yang_parent_name = "fib-scale"

                self.scale_ipv6_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam()
                self.scale_ipv6_no_tcam.parent = self
                self._children_name_map["scale_ipv6_no_tcam"] = "scale-ipv6-no-tcam"
                self._children_yang_names.add("scale-ipv6-no-tcam")


            class ScaleIpv6NoTcam(Entity):
                """
                Scale for IPv6 table for NoTCAM LC.
                
                .. attribute:: internet_optimized_ipv6_no_tcam
                
                	Internet\-optimized Scale for IPv6 table for NoTCAM LC
                	**type**\:  str
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, self).__init__()

                    self.yang_name = "scale-ipv6-no-tcam"
                    self.yang_parent_name = "ipv6-unicast-scale-no-tcam"

                    self.internet_optimized_ipv6_no_tcam = YLeaf(YType.str, "internet-optimized-ipv6-no-tcam")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("internet_optimized_ipv6_no_tcam") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, self).__setattr__(name, value)

                def has_data(self):
                    return self.internet_optimized_ipv6_no_tcam.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.internet_optimized_ipv6_no_tcam.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "scale-ipv6-no-tcam" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv6-unicast-scale-no-tcam/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.internet_optimized_ipv6_no_tcam.is_set or self.internet_optimized_ipv6_no_tcam.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.internet_optimized_ipv6_no_tcam.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "internet-optimized-ipv6-no-tcam"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "internet-optimized-ipv6-no-tcam"):
                        self.internet_optimized_ipv6_no_tcam = value
                        self.internet_optimized_ipv6_no_tcam.value_namespace = name_space
                        self.internet_optimized_ipv6_no_tcam.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.scale_ipv6_no_tcam is not None and self.scale_ipv6_no_tcam.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.scale_ipv6_no_tcam is not None and self.scale_ipv6_no_tcam.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6-unicast-scale-no-tcam" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "scale-ipv6-no-tcam"):
                    if (self.scale_ipv6_no_tcam is None):
                        self.scale_ipv6_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam()
                        self.scale_ipv6_no_tcam.parent = self
                        self._children_name_map["scale_ipv6_no_tcam"] = "scale-ipv6-no-tcam"
                    return self.scale_ipv6_no_tcam

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "scale-ipv6-no-tcam"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv4UnicastScaleNoTcam(Entity):
            """
            IPv4 table for NOTCAM LC Scale.
            
            .. attribute:: scale_ipv4_no_tcam
            
            	Scale for IPv4 table for NoTCAM LC
            	**type**\:   :py:class:`ScaleIpv4NoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam, self).__init__()

                self.yang_name = "ipv4-unicast-scale-no-tcam"
                self.yang_parent_name = "fib-scale"

                self.scale_ipv4_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam()
                self.scale_ipv4_no_tcam.parent = self
                self._children_name_map["scale_ipv4_no_tcam"] = "scale-ipv4-no-tcam"
                self._children_yang_names.add("scale-ipv4-no-tcam")


            class ScaleIpv4NoTcam(Entity):
                """
                Scale for IPv4 table for NoTCAM LC.
                
                .. attribute:: host_optimized_ipv4_no_tcam
                
                	Host\-optimized Scale for IPv4 table for NoTCAM LC
                	**type**\:  str
                
                .. attribute:: internet_optimized_ipv4_no_tcam
                
                	Internet\-optimized Scale for IPv4 table for NoTCAM LC
                	**type**\:  str
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, self).__init__()

                    self.yang_name = "scale-ipv4-no-tcam"
                    self.yang_parent_name = "ipv4-unicast-scale-no-tcam"

                    self.host_optimized_ipv4_no_tcam = YLeaf(YType.str, "host-optimized-ipv4-no-tcam")

                    self.internet_optimized_ipv4_no_tcam = YLeaf(YType.str, "internet-optimized-ipv4-no-tcam")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("host_optimized_ipv4_no_tcam",
                                    "internet_optimized_ipv4_no_tcam") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.host_optimized_ipv4_no_tcam.is_set or
                        self.internet_optimized_ipv4_no_tcam.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.host_optimized_ipv4_no_tcam.yfilter != YFilter.not_set or
                        self.internet_optimized_ipv4_no_tcam.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "scale-ipv4-no-tcam" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv4-unicast-scale-no-tcam/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.host_optimized_ipv4_no_tcam.is_set or self.host_optimized_ipv4_no_tcam.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.host_optimized_ipv4_no_tcam.get_name_leafdata())
                    if (self.internet_optimized_ipv4_no_tcam.is_set or self.internet_optimized_ipv4_no_tcam.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.internet_optimized_ipv4_no_tcam.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "host-optimized-ipv4-no-tcam" or name == "internet-optimized-ipv4-no-tcam"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "host-optimized-ipv4-no-tcam"):
                        self.host_optimized_ipv4_no_tcam = value
                        self.host_optimized_ipv4_no_tcam.value_namespace = name_space
                        self.host_optimized_ipv4_no_tcam.value_namespace_prefix = name_space_prefix
                    if(value_path == "internet-optimized-ipv4-no-tcam"):
                        self.internet_optimized_ipv4_no_tcam = value
                        self.internet_optimized_ipv4_no_tcam.value_namespace = name_space
                        self.internet_optimized_ipv4_no_tcam.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.scale_ipv4_no_tcam is not None and self.scale_ipv4_no_tcam.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.scale_ipv4_no_tcam is not None and self.scale_ipv4_no_tcam.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4-unicast-scale-no-tcam" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "scale-ipv4-no-tcam"):
                    if (self.scale_ipv4_no_tcam is None):
                        self.scale_ipv4_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam()
                        self.scale_ipv4_no_tcam.parent = self
                        self._children_name_map["scale_ipv4_no_tcam"] = "scale-ipv4-no-tcam"
                    return self.scale_ipv4_no_tcam

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "scale-ipv4-no-tcam"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.ipv4_unicast_scale_no_tcam is not None and self.ipv4_unicast_scale_no_tcam.has_data()) or
                (self.ipv6_unicast_scale_no_tcam is not None and self.ipv6_unicast_scale_no_tcam.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ipv4_unicast_scale_no_tcam is not None and self.ipv4_unicast_scale_no_tcam.has_operation()) or
                (self.ipv6_unicast_scale_no_tcam is not None and self.ipv6_unicast_scale_no_tcam.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "fib-scale" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv4-unicast-scale-no-tcam"):
                if (self.ipv4_unicast_scale_no_tcam is None):
                    self.ipv4_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam()
                    self.ipv4_unicast_scale_no_tcam.parent = self
                    self._children_name_map["ipv4_unicast_scale_no_tcam"] = "ipv4-unicast-scale-no-tcam"
                return self.ipv4_unicast_scale_no_tcam

            if (child_yang_name == "ipv6-unicast-scale-no-tcam"):
                if (self.ipv6_unicast_scale_no_tcam is None):
                    self.ipv6_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam()
                    self.ipv6_unicast_scale_no_tcam.parent = self
                    self._children_name_map["ipv6_unicast_scale_no_tcam"] = "ipv6-unicast-scale-no-tcam"
                return self.ipv6_unicast_scale_no_tcam

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv4-unicast-scale-no-tcam" or name == "ipv6-unicast-scale-no-tcam"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tcam(Entity):
        """
        Configure Tcam.
        
        .. attribute:: fib_tcam_scale
        
        	Configure Fib iscale for Tcam
        	**type**\:   :py:class:`FibTcamScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam.FibTcamScale>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Tcam, self).__init__()

            self.yang_name = "tcam"
            self.yang_parent_name = "hw-module-profile-config"

            self.fib_tcam_scale = HwModuleProfileConfig.Tcam.FibTcamScale()
            self.fib_tcam_scale.parent = self
            self._children_name_map["fib_tcam_scale"] = "fib-tcam-scale"
            self._children_yang_names.add("fib-tcam-scale")


        class FibTcamScale(Entity):
            """
            Configure Fib iscale for Tcam.
            
            .. attribute:: ipv4_unicast_scale
            
            	IPv4 table for TCAM LC Scale
            	**type**\:   :py:class:`Ipv4UnicastScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Tcam.FibTcamScale, self).__init__()

                self.yang_name = "fib-tcam-scale"
                self.yang_parent_name = "tcam"

                self.ipv4_unicast_scale = HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale()
                self.ipv4_unicast_scale.parent = self
                self._children_name_map["ipv4_unicast_scale"] = "ipv4-unicast-scale"
                self._children_yang_names.add("ipv4-unicast-scale")


            class Ipv4UnicastScale(Entity):
                """
                IPv4 table for TCAM LC Scale.
                
                .. attribute:: ipv4_scale
                
                	Scale for IPv4 table for TCAM LC
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, self).__init__()

                    self.yang_name = "ipv4-unicast-scale"
                    self.yang_parent_name = "fib-tcam-scale"

                    self.ipv4_scale = YLeaf(YType.empty, "ipv4-scale")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ipv4_scale") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, self).__setattr__(name, value)

                def has_data(self):
                    return self.ipv4_scale.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ipv4_scale.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-unicast-scale" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/fib-tcam-scale/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ipv4_scale.is_set or self.ipv4_scale.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_scale.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-scale"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ipv4-scale"):
                        self.ipv4_scale = value
                        self.ipv4_scale.value_namespace = name_space
                        self.ipv4_scale.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.ipv4_unicast_scale is not None and self.ipv4_unicast_scale.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipv4_unicast_scale is not None and self.ipv4_unicast_scale.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "fib-tcam-scale" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-unicast-scale"):
                    if (self.ipv4_unicast_scale is None):
                        self.ipv4_unicast_scale = HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale()
                        self.ipv4_unicast_scale.parent = self
                        self._children_name_map["ipv4_unicast_scale"] = "ipv4-unicast-scale"
                    return self.ipv4_unicast_scale

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-unicast-scale"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.fib_tcam_scale is not None and self.fib_tcam_scale.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.fib_tcam_scale is not None and self.fib_tcam_scale.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tcam" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "fib-tcam-scale"):
                if (self.fib_tcam_scale is None):
                    self.fib_tcam_scale = HwModuleProfileConfig.Tcam.FibTcamScale()
                    self.fib_tcam_scale.parent = self
                    self._children_name_map["fib_tcam_scale"] = "fib-tcam-scale"
                return self.fib_tcam_scale

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "fib-tcam-scale"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.fib_scale is not None and self.fib_scale.has_data()) or
            (self.profile is not None and self.profile.has_data()) or
            (self.tcam is not None and self.tcam.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.fib_scale is not None and self.fib_scale.has_operation()) or
            (self.profile is not None and self.profile.has_operation()) or
            (self.tcam is not None and self.tcam.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config" + path_buffer

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

        if (child_yang_name == "fib-scale"):
            if (self.fib_scale is None):
                self.fib_scale = HwModuleProfileConfig.FibScale()
                self.fib_scale.parent = self
                self._children_name_map["fib_scale"] = "fib-scale"
            return self.fib_scale

        if (child_yang_name == "profile"):
            if (self.profile is None):
                self.profile = HwModuleProfileConfig.Profile()
                self.profile.parent = self
                self._children_name_map["profile"] = "profile"
            return self.profile

        if (child_yang_name == "tcam"):
            if (self.tcam is None):
                self.tcam = HwModuleProfileConfig.Tcam()
                self.tcam.parent = self
                self._children_name_map["tcam"] = "tcam"
            return self.tcam

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "fib-scale" or name == "profile" or name == "tcam"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = HwModuleProfileConfig()
        return self._top_entity

