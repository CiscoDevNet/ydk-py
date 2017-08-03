""" Cisco_IOS_XR_kim_tpa_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR kim\-tpa package configuration.

This module contains definitions
for the following management objects\:
  tpa\: tpa configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Tpa(Entity):
    """
    tpa configuration commands
    
    .. attribute:: statistics
    
    	Statistics
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.Statistics>`
    
    .. attribute:: vrf_names
    
    	VRF container
    	**type**\:   :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames>`
    
    

    """

    _prefix = 'kim-tpa-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Tpa, self).__init__()
        self._top_entity = None

        self.yang_name = "tpa"
        self.yang_parent_name = "Cisco-IOS-XR-kim-tpa-cfg"

        self.statistics = Tpa.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")

        self.vrf_names = Tpa.VrfNames()
        self.vrf_names.parent = self
        self._children_name_map["vrf_names"] = "vrf-names"
        self._children_yang_names.add("vrf-names")


    class VrfNames(Entity):
        """
        VRF container
        
        .. attribute:: vrf_name
        
        	VRF name
        	**type**\: list of    :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName>`
        
        

        """

        _prefix = 'kim-tpa-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Tpa.VrfNames, self).__init__()

            self.yang_name = "vrf-names"
            self.yang_parent_name = "tpa"

            self.vrf_name = YList(self)

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
                        super(Tpa.VrfNames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tpa.VrfNames, self).__setattr__(name, value)


        class VrfName(Entity):
            """
            VRF name
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:   :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily>`
            
            .. attribute:: east_west_names
            
            	EastWest container
            	**type**\:   :py:class:`EastWestNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.EastWestNames>`
            
            

            """

            _prefix = 'kim-tpa-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Tpa.VrfNames.VrfName, self).__init__()

                self.yang_name = "vrf-name"
                self.yang_parent_name = "vrf-names"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.address_family = Tpa.VrfNames.VrfName.AddressFamily()
                self.address_family.parent = self
                self._children_name_map["address_family"] = "address-family"
                self._children_yang_names.add("address-family")

                self.east_west_names = Tpa.VrfNames.VrfName.EastWestNames()
                self.east_west_names.parent = self
                self._children_name_map["east_west_names"] = "east-west-names"
                self._children_yang_names.add("east-west-names")

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
                            super(Tpa.VrfNames.VrfName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Tpa.VrfNames.VrfName, self).__setattr__(name, value)


            class EastWestNames(Entity):
                """
                EastWest container
                
                .. attribute:: east_west_name
                
                	East West interface
                	**type**\: list of    :py:class:`EastWestName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.EastWestNames.EastWestName>`
                
                

                """

                _prefix = 'kim-tpa-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Tpa.VrfNames.VrfName.EastWestNames, self).__init__()

                    self.yang_name = "east-west-names"
                    self.yang_parent_name = "vrf-name"

                    self.east_west_name = YList(self)

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
                                super(Tpa.VrfNames.VrfName.EastWestNames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tpa.VrfNames.VrfName.EastWestNames, self).__setattr__(name, value)


                class EastWestName(Entity):
                    """
                    East West interface
                    
                    .. attribute:: east_west_name  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    .. attribute:: vrf
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'kim-tpa-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Tpa.VrfNames.VrfName.EastWestNames.EastWestName, self).__init__()

                        self.yang_name = "east-west-name"
                        self.yang_parent_name = "east-west-names"

                        self.east_west_name = YLeaf(YType.str, "east-west-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("east_west_name",
                                        "interface",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tpa.VrfNames.VrfName.EastWestNames.EastWestName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tpa.VrfNames.VrfName.EastWestNames.EastWestName, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.east_west_name.is_set or
                            self.interface.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.east_west_name.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "east-west-name" + "[east-west-name='" + self.east_west_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.east_west_name.is_set or self.east_west_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.east_west_name.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "east-west-name" or name == "interface" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "east-west-name"):
                            self.east_west_name = value
                            self.east_west_name.value_namespace = name_space
                            self.east_west_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.east_west_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.east_west_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "east-west-names" + path_buffer

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

                    if (child_yang_name == "east-west-name"):
                        for c in self.east_west_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Tpa.VrfNames.VrfName.EastWestNames.EastWestName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.east_west_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "east-west-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AddressFamily(Entity):
                """
                Address family
                
                .. attribute:: ipv4
                
                	IPv4 configuration
                	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv4>`
                
                .. attribute:: ipv6
                
                	IPv6 configuration
                	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv6>`
                
                

                """

                _prefix = 'kim-tpa-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Tpa.VrfNames.VrfName.AddressFamily, self).__init__()

                    self.yang_name = "address-family"
                    self.yang_parent_name = "vrf-name"

                    self.ipv4 = Tpa.VrfNames.VrfName.AddressFamily.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                    self._children_yang_names.add("ipv4")

                    self.ipv6 = Tpa.VrfNames.VrfName.AddressFamily.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                    self._children_yang_names.add("ipv6")


                class Ipv6(Entity):
                    """
                    IPv6 configuration
                    
                    .. attribute:: default_route
                    
                    	Default interface used for routing
                    	**type**\:  str
                    
                    .. attribute:: update_source
                    
                    	Interface name for source address
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'kim-tpa-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6, self).__init__()

                        self.yang_name = "ipv6"
                        self.yang_parent_name = "address-family"

                        self.default_route = YLeaf(YType.str, "default-route")

                        self.update_source = YLeaf(YType.str, "update-source")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default_route",
                                        "update_source") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.default_route.is_set or
                            self.update_source.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default_route.yfilter != YFilter.not_set or
                            self.update_source.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default_route.is_set or self.default_route.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_route.get_name_leafdata())
                        if (self.update_source.is_set or self.update_source.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.update_source.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "default-route" or name == "update-source"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default-route"):
                            self.default_route = value
                            self.default_route.value_namespace = name_space
                            self.default_route.value_namespace_prefix = name_space_prefix
                        if(value_path == "update-source"):
                            self.update_source = value
                            self.update_source.value_namespace = name_space
                            self.update_source.value_namespace_prefix = name_space_prefix


                class Ipv4(Entity):
                    """
                    IPv4 configuration
                    
                    .. attribute:: default_route
                    
                    	Default interface used for routing
                    	**type**\:  str
                    
                    .. attribute:: update_source
                    
                    	Interface name for source address
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'kim-tpa-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4, self).__init__()

                        self.yang_name = "ipv4"
                        self.yang_parent_name = "address-family"

                        self.default_route = YLeaf(YType.str, "default-route")

                        self.update_source = YLeaf(YType.str, "update-source")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default_route",
                                        "update_source") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.default_route.is_set or
                            self.update_source.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default_route.yfilter != YFilter.not_set or
                            self.update_source.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default_route.is_set or self.default_route.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default_route.get_name_leafdata())
                        if (self.update_source.is_set or self.update_source.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.update_source.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "default-route" or name == "update-source"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default-route"):
                            self.default_route = value
                            self.default_route.value_namespace = name_space
                            self.default_route.value_namespace_prefix = name_space_prefix
                        if(value_path == "update-source"):
                            self.update_source = value
                            self.update_source.value_namespace = name_space
                            self.update_source.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.ipv4 is not None and self.ipv4.has_data()) or
                        (self.ipv6 is not None and self.ipv6.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipv4 is not None and self.ipv4.has_operation()) or
                        (self.ipv6 is not None and self.ipv6.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "address-family" + path_buffer

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

                    if (child_yang_name == "ipv4"):
                        if (self.ipv4 is None):
                            self.ipv4 = Tpa.VrfNames.VrfName.AddressFamily.Ipv4()
                            self.ipv4.parent = self
                            self._children_name_map["ipv4"] = "ipv4"
                        return self.ipv4

                    if (child_yang_name == "ipv6"):
                        if (self.ipv6 is None):
                            self.ipv6 = Tpa.VrfNames.VrfName.AddressFamily.Ipv6()
                            self.ipv6.parent = self
                            self._children_name_map["ipv6"] = "ipv6"
                        return self.ipv6

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4" or name == "ipv6"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.address_family is not None and self.address_family.has_data()) or
                    (self.east_west_names is not None and self.east_west_names.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.address_family is not None and self.address_family.has_operation()) or
                    (self.east_west_names is not None and self.east_west_names.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf-name" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-kim-tpa-cfg:tpa/vrf-names/%s" % self.get_segment_path()
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

                if (child_yang_name == "address-family"):
                    if (self.address_family is None):
                        self.address_family = Tpa.VrfNames.VrfName.AddressFamily()
                        self.address_family.parent = self
                        self._children_name_map["address_family"] = "address-family"
                    return self.address_family

                if (child_yang_name == "east-west-names"):
                    if (self.east_west_names is None):
                        self.east_west_names = Tpa.VrfNames.VrfName.EastWestNames()
                        self.east_west_names.parent = self
                        self._children_name_map["east_west_names"] = "east-west-names"
                    return self.east_west_names

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address-family" or name == "east-west-names" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf-names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-kim-tpa-cfg:tpa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf-name"):
                for c in self.vrf_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Tpa.VrfNames.VrfName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Statistics(Entity):
        """
        Statistics
        
        .. attribute:: statistics_update_frequency
        
        	Statistics update frequency into Linux
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: second
        
        

        """

        _prefix = 'kim-tpa-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Tpa.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "tpa"

            self.statistics_update_frequency = YLeaf(YType.int32, "statistics-update-frequency")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("statistics_update_frequency") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Tpa.Statistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tpa.Statistics, self).__setattr__(name, value)

        def has_data(self):
            return self.statistics_update_frequency.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.statistics_update_frequency.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-kim-tpa-cfg:tpa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.statistics_update_frequency.is_set or self.statistics_update_frequency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.statistics_update_frequency.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "statistics-update-frequency"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "statistics-update-frequency"):
                self.statistics_update_frequency = value
                self.statistics_update_frequency.value_namespace = name_space
                self.statistics_update_frequency.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.statistics is not None and self.statistics.has_data()) or
            (self.vrf_names is not None and self.vrf_names.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.statistics is not None and self.statistics.has_operation()) or
            (self.vrf_names is not None and self.vrf_names.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-kim-tpa-cfg:tpa" + path_buffer

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

        if (child_yang_name == "statistics"):
            if (self.statistics is None):
                self.statistics = Tpa.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
            return self.statistics

        if (child_yang_name == "vrf-names"):
            if (self.vrf_names is None):
                self.vrf_names = Tpa.VrfNames()
                self.vrf_names.parent = self
                self._children_name_map["vrf_names"] = "vrf-names"
            return self.vrf_names

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "statistics" or name == "vrf-names"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Tpa()
        return self._top_entity

