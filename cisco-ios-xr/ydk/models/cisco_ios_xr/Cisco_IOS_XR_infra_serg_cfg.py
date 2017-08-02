""" Cisco_IOS_XR_infra_serg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package configuration.

This module contains definitions
for the following management objects\:
  session\-redundancy\: Session Redundancy configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SergAddrFamily(Enum):
    """
    SergAddrFamily

    Serg addr family

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(10, "ipv6")


class SessionRedundancyGroupRole(Enum):
    """
    SessionRedundancyGroupRole

    Session redundancy group role

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")



class SessionRedundancy(Entity):
    """
    Session Redundancy configuration
    
    .. attribute:: enable
    
    	Enable Session Redundancy configuration. Deletion of this object also causes deletion of all associated objects under SessionRedundancy
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Table of Group
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups>`
    
    .. attribute:: hold_timer
    
    	Set hold time (in Minutes)
    	**type**\:  int
    
    	**range:** 1..65535
    
    	**units**\: minute
    
    .. attribute:: preferred_role
    
    	Set preferred role
    	**type**\:   :py:class:`SessionRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancyGroupRole>`
    
    .. attribute:: redundancy_disable
    
    	Disable
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: revertive_timer
    
    	None
    	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.RevertiveTimer>`
    
    .. attribute:: source_interface
    
    	Source Interface for Redundancy Peer Communication
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    

    """

    _prefix = 'infra-serg-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionRedundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.hold_timer = YLeaf(YType.uint32, "hold-timer")

        self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

        self.redundancy_disable = YLeaf(YType.empty, "redundancy-disable")

        self.source_interface = YLeaf(YType.str, "source-interface")

        self.groups = SessionRedundancy.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.revertive_timer = SessionRedundancy.RevertiveTimer()
        self.revertive_timer.parent = self
        self._children_name_map["revertive_timer"] = "revertive-timer"
        self._children_yang_names.add("revertive-timer")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable",
                        "hold_timer",
                        "preferred_role",
                        "redundancy_disable",
                        "source_interface") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(SessionRedundancy, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SessionRedundancy, self).__setattr__(name, value)


    class Groups(Entity):
        """
        Table of Group
        
        .. attribute:: group
        
        	Redundancy Group configuration
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancy.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "session-redundancy"

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
                        super(SessionRedundancy.Groups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionRedundancy.Groups, self).__setattr__(name, value)


        class Group(Entity):
            """
            Redundancy Group configuration
            
            .. attribute:: group_id  <key>
            
            	Group ID
            	**type**\:  int
            
            	**range:** 1..500
            
            .. attribute:: access_tracking_object
            
            	Access Tracking Object for this Group
            	**type**\:  str
            
            .. attribute:: core_tracking_object
            
            	Core Tracking Object for this Group
            	**type**\:  str
            
            .. attribute:: description
            
            	Description for this Group
            	**type**\:  str
            
            .. attribute:: disable_tracking_object
            
            	Disable Tracking Object for this Group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable Redundancy Group configuration. Deletion of this object also causes deletion of all associated objects under Group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hold_timer
            
            	Set hold time (in Minutes)
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: minute
            
            .. attribute:: interface_list
            
            	List of Interfaces for this Group
            	**type**\:   :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList>`
            
            .. attribute:: peer
            
            	None
            	**type**\:   :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.Peer>`
            
            .. attribute:: preferred_role
            
            	Set preferred role
            	**type**\:   :py:class:`SessionRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancyGroupRole>`
            
            .. attribute:: redundancy_disable
            
            	Disable
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: revertive_timer
            
            	None
            	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.RevertiveTimer>`
            
            

            """

            _prefix = 'infra-serg-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancy.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"

                self.group_id = YLeaf(YType.uint32, "group-id")

                self.access_tracking_object = YLeaf(YType.str, "access-tracking-object")

                self.core_tracking_object = YLeaf(YType.str, "core-tracking-object")

                self.description = YLeaf(YType.str, "description")

                self.disable_tracking_object = YLeaf(YType.empty, "disable-tracking-object")

                self.enable = YLeaf(YType.empty, "enable")

                self.hold_timer = YLeaf(YType.uint32, "hold-timer")

                self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

                self.redundancy_disable = YLeaf(YType.empty, "redundancy-disable")

                self.interface_list = SessionRedundancy.Groups.Group.InterfaceList()
                self.interface_list.parent = self
                self._children_name_map["interface_list"] = "interface-list"
                self._children_yang_names.add("interface-list")

                self.peer = SessionRedundancy.Groups.Group.Peer()
                self.peer.parent = self
                self._children_name_map["peer"] = "peer"
                self._children_yang_names.add("peer")

                self.revertive_timer = SessionRedundancy.Groups.Group.RevertiveTimer()
                self.revertive_timer.parent = self
                self._children_name_map["revertive_timer"] = "revertive-timer"
                self._children_yang_names.add("revertive-timer")

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
                                "access_tracking_object",
                                "core_tracking_object",
                                "description",
                                "disable_tracking_object",
                                "enable",
                                "hold_timer",
                                "preferred_role",
                                "redundancy_disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SessionRedundancy.Groups.Group, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SessionRedundancy.Groups.Group, self).__setattr__(name, value)


            class Peer(Entity):
                """
                None
                
                .. attribute:: ipaddress
                
                	IPv4 or IPv6 Address of SERG Peer
                	**type**\:   :py:class:`Ipaddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.Peer.Ipaddress>`
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancy.Groups.Group.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "group"

                    self.ipaddress = SessionRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self
                    self._children_name_map["ipaddress"] = "ipaddress"
                    self._children_yang_names.add("ipaddress")


                class Ipaddress(Entity):
                    """
                    IPv4 or IPv6 Address of SERG Peer
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4/IPv6 address
                    	**type**\:   :py:class:`SergAddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SergAddrFamily>`
                    
                    .. attribute:: prefix_string
                    
                    	IPv4/IPv6 address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancy.Groups.Group.Peer.Ipaddress, self).__init__()

                        self.yang_name = "ipaddress"
                        self.yang_parent_name = "peer"

                        self.address_family = YLeaf(YType.enumeration, "address-family")

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
                            if name in ("address_family",
                                        "prefix_string") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancy.Groups.Group.Peer.Ipaddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancy.Groups.Group.Peer.Ipaddress, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address_family.is_set or
                            self.prefix_string.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address_family.yfilter != YFilter.not_set or
                            self.prefix_string.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipaddress" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address_family.get_name_leafdata())
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
                        if(name == "address-family" or name == "prefix-string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address-family"):
                            self.address_family = value
                            self.address_family.value_namespace = name_space
                            self.address_family.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-string"):
                            self.prefix_string = value
                            self.prefix_string.value_namespace = name_space
                            self.prefix_string.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.ipaddress is not None and self.ipaddress.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipaddress is not None and self.ipaddress.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peer" + path_buffer

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

                    if (child_yang_name == "ipaddress"):
                        if (self.ipaddress is None):
                            self.ipaddress = SessionRedundancy.Groups.Group.Peer.Ipaddress()
                            self.ipaddress.parent = self
                            self._children_name_map["ipaddress"] = "ipaddress"
                        return self.ipaddress

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipaddress"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class RevertiveTimer(Entity):
                """
                None
                
                .. attribute:: max_value
                
                	Value of MAX Revertive Timer
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: value
                
                	Value of revertive time in minutes
                	**type**\:  int
                
                	**range:** 1..65535
                
                	**units**\: minute
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancy.Groups.Group.RevertiveTimer, self).__init__()

                    self.yang_name = "revertive-timer"
                    self.yang_parent_name = "group"

                    self.max_value = YLeaf(YType.uint32, "max-value")

                    self.value = YLeaf(YType.uint32, "value")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("max_value",
                                    "value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SessionRedundancy.Groups.Group.RevertiveTimer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancy.Groups.Group.RevertiveTimer, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.max_value.is_set or
                        self.value.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.max_value.yfilter != YFilter.not_set or
                        self.value.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "revertive-timer" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.max_value.is_set or self.max_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_value.get_name_leafdata())
                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "max-value" or name == "value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "max-value"):
                        self.max_value = value
                        self.max_value.value_namespace = name_space
                        self.max_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "value"):
                        self.value = value
                        self.value.value_namespace = name_space
                        self.value.value_namespace_prefix = name_space_prefix


            class InterfaceList(Entity):
                """
                List of Interfaces for this Group
                
                .. attribute:: enable
                
                	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList 
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface_ranges
                
                	Table of InterfaceRange
                	**type**\:   :py:class:`InterfaceRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges>`
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.Interfaces>`
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancy.Groups.Group.InterfaceList, self).__init__()

                    self.yang_name = "interface-list"
                    self.yang_parent_name = "group"

                    self.enable = YLeaf(YType.empty, "enable")

                    self.interface_ranges = SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self._children_name_map["interface_ranges"] = "interface-ranges"
                    self._children_yang_names.add("interface-ranges")

                    self.interfaces = SessionRedundancy.Groups.Group.InterfaceList.Interfaces()
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
                                super(SessionRedundancy.Groups.Group.InterfaceList, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancy.Groups.Group.InterfaceList, self).__setattr__(name, value)


                class InterfaceRanges(Entity):
                    """
                    Table of InterfaceRange
                    
                    .. attribute:: interface_range
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`InterfaceRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange>`
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__init__()

                        self.yang_name = "interface-ranges"
                        self.yang_parent_name = "interface-list"

                        self.interface_range = YList(self)

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
                                    super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__setattr__(name, value)


                    class InterfaceRange(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: sub_interface_range_start  <key>
                        
                        	Sub Interface Start Range
                        	**type**\:  int
                        
                        	**range:** 0..2147483647
                        
                        .. attribute:: sub_interface_range_end  <key>
                        
                        	Sub Interface End Range
                        	**type**\:  int
                        
                        	**range:** 0..2147483647
                        
                        .. attribute:: interface_id_range_end
                        
                        	Interface ID End Range
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: interface_id_range_start
                        
                        	Interface ID Start Range
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        

                        """

                        _prefix = 'infra-serg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__init__()

                            self.yang_name = "interface-range"
                            self.yang_parent_name = "interface-ranges"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.sub_interface_range_start = YLeaf(YType.uint32, "sub-interface-range-start")

                            self.sub_interface_range_end = YLeaf(YType.uint32, "sub-interface-range-end")

                            self.interface_id_range_end = YLeaf(YType.uint32, "interface-id-range-end")

                            self.interface_id_range_start = YLeaf(YType.uint32, "interface-id-range-start")

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
                                            "sub_interface_range_start",
                                            "sub_interface_range_end",
                                            "interface_id_range_end",
                                            "interface_id_range_start") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.sub_interface_range_start.is_set or
                                self.sub_interface_range_end.is_set or
                                self.interface_id_range_end.is_set or
                                self.interface_id_range_start.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.sub_interface_range_start.yfilter != YFilter.not_set or
                                self.sub_interface_range_end.yfilter != YFilter.not_set or
                                self.interface_id_range_end.yfilter != YFilter.not_set or
                                self.interface_id_range_start.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-range" + "[interface-name='" + self.interface_name.get() + "']" + "[sub-interface-range-start='" + self.sub_interface_range_start.get() + "']" + "[sub-interface-range-end='" + self.sub_interface_range_end.get() + "']" + path_buffer

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
                            if (self.sub_interface_range_start.is_set or self.sub_interface_range_start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sub_interface_range_start.get_name_leafdata())
                            if (self.sub_interface_range_end.is_set or self.sub_interface_range_end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sub_interface_range_end.get_name_leafdata())
                            if (self.interface_id_range_end.is_set or self.interface_id_range_end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_id_range_end.get_name_leafdata())
                            if (self.interface_id_range_start.is_set or self.interface_id_range_start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_id_range_start.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "sub-interface-range-start" or name == "sub-interface-range-end" or name == "interface-id-range-end" or name == "interface-id-range-start"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "sub-interface-range-start"):
                                self.sub_interface_range_start = value
                                self.sub_interface_range_start.value_namespace = name_space
                                self.sub_interface_range_start.value_namespace_prefix = name_space_prefix
                            if(value_path == "sub-interface-range-end"):
                                self.sub_interface_range_end = value
                                self.sub_interface_range_end.value_namespace = name_space
                                self.sub_interface_range_end.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-id-range-end"):
                                self.interface_id_range_end = value
                                self.interface_id_range_end.value_namespace = name_space
                                self.interface_id_range_end.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-id-range-start"):
                                self.interface_id_range_start = value
                                self.interface_id_range_start.value_namespace = name_space
                                self.interface_id_range_start.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.interface_range:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.interface_range:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-ranges" + path_buffer

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

                        if (child_yang_name == "interface-range"):
                            for c in self.interface_range:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface_range.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-range"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

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
                                    super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces, self).__setattr__(name, value)


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

                        _prefix = 'infra-serg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__init__()

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
                                        super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__setattr__(name, value)

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
                            c = SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface()
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
                        (self.interface_ranges is not None and self.interface_ranges.has_data()) or
                        (self.interfaces is not None and self.interfaces.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.interface_ranges is not None and self.interface_ranges.has_operation()) or
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

                    if (child_yang_name == "interface-ranges"):
                        if (self.interface_ranges is None):
                            self.interface_ranges = SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                            self.interface_ranges.parent = self
                            self._children_name_map["interface_ranges"] = "interface-ranges"
                        return self.interface_ranges

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = SessionRedundancy.Groups.Group.InterfaceList.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"
                        return self.interfaces

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-ranges" or name == "interfaces" or name == "enable"):
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
                    self.access_tracking_object.is_set or
                    self.core_tracking_object.is_set or
                    self.description.is_set or
                    self.disable_tracking_object.is_set or
                    self.enable.is_set or
                    self.hold_timer.is_set or
                    self.preferred_role.is_set or
                    self.redundancy_disable.is_set or
                    (self.interface_list is not None and self.interface_list.has_data()) or
                    (self.peer is not None and self.peer.has_data()) or
                    (self.revertive_timer is not None and self.revertive_timer.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.group_id.yfilter != YFilter.not_set or
                    self.access_tracking_object.yfilter != YFilter.not_set or
                    self.core_tracking_object.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.disable_tracking_object.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.hold_timer.yfilter != YFilter.not_set or
                    self.preferred_role.yfilter != YFilter.not_set or
                    self.redundancy_disable.yfilter != YFilter.not_set or
                    (self.interface_list is not None and self.interface_list.has_operation()) or
                    (self.peer is not None and self.peer.has_operation()) or
                    (self.revertive_timer is not None and self.revertive_timer.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-serg-cfg:session-redundancy/groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group_id.get_name_leafdata())
                if (self.access_tracking_object.is_set or self.access_tracking_object.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access_tracking_object.get_name_leafdata())
                if (self.core_tracking_object.is_set or self.core_tracking_object.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.core_tracking_object.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.disable_tracking_object.is_set or self.disable_tracking_object.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable_tracking_object.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.hold_timer.is_set or self.hold_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_timer.get_name_leafdata())
                if (self.preferred_role.is_set or self.preferred_role.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.preferred_role.get_name_leafdata())
                if (self.redundancy_disable.is_set or self.redundancy_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.redundancy_disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-list"):
                    if (self.interface_list is None):
                        self.interface_list = SessionRedundancy.Groups.Group.InterfaceList()
                        self.interface_list.parent = self
                        self._children_name_map["interface_list"] = "interface-list"
                    return self.interface_list

                if (child_yang_name == "peer"):
                    if (self.peer is None):
                        self.peer = SessionRedundancy.Groups.Group.Peer()
                        self.peer.parent = self
                        self._children_name_map["peer"] = "peer"
                    return self.peer

                if (child_yang_name == "revertive-timer"):
                    if (self.revertive_timer is None):
                        self.revertive_timer = SessionRedundancy.Groups.Group.RevertiveTimer()
                        self.revertive_timer.parent = self
                        self._children_name_map["revertive_timer"] = "revertive-timer"
                    return self.revertive_timer

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-list" or name == "peer" or name == "revertive-timer" or name == "group-id" or name == "access-tracking-object" or name == "core-tracking-object" or name == "description" or name == "disable-tracking-object" or name == "enable" or name == "hold-timer" or name == "preferred-role" or name == "redundancy-disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "group-id"):
                    self.group_id = value
                    self.group_id.value_namespace = name_space
                    self.group_id.value_namespace_prefix = name_space_prefix
                if(value_path == "access-tracking-object"):
                    self.access_tracking_object = value
                    self.access_tracking_object.value_namespace = name_space
                    self.access_tracking_object.value_namespace_prefix = name_space_prefix
                if(value_path == "core-tracking-object"):
                    self.core_tracking_object = value
                    self.core_tracking_object.value_namespace = name_space
                    self.core_tracking_object.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "disable-tracking-object"):
                    self.disable_tracking_object = value
                    self.disable_tracking_object.value_namespace = name_space
                    self.disable_tracking_object.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-timer"):
                    self.hold_timer = value
                    self.hold_timer.value_namespace = name_space
                    self.hold_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "preferred-role"):
                    self.preferred_role = value
                    self.preferred_role.value_namespace = name_space
                    self.preferred_role.value_namespace_prefix = name_space_prefix
                if(value_path == "redundancy-disable"):
                    self.redundancy_disable = value
                    self.redundancy_disable.value_namespace = name_space
                    self.redundancy_disable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-infra-serg-cfg:session-redundancy/%s" % self.get_segment_path()
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
                c = SessionRedundancy.Groups.Group()
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


    class RevertiveTimer(Entity):
        """
        None
        
        .. attribute:: max_value
        
        	Value of MAX Revertive Timer
        	**type**\:  int
        
        	**range:** 1..65535
        
        .. attribute:: value
        
        	Value of revertive time in minutes
        	**type**\:  int
        
        	**range:** 1..65535
        
        	**units**\: minute
        
        

        """

        _prefix = 'infra-serg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancy.RevertiveTimer, self).__init__()

            self.yang_name = "revertive-timer"
            self.yang_parent_name = "session-redundancy"

            self.max_value = YLeaf(YType.uint32, "max-value")

            self.value = YLeaf(YType.uint32, "value")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("max_value",
                            "value") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SessionRedundancy.RevertiveTimer, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionRedundancy.RevertiveTimer, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.max_value.is_set or
                self.value.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.max_value.yfilter != YFilter.not_set or
                self.value.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "revertive-timer" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-serg-cfg:session-redundancy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.max_value.is_set or self.max_value.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_value.get_name_leafdata())
            if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                leaf_name_data.append(self.value.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "max-value" or name == "value"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "max-value"):
                self.max_value = value
                self.max_value.value_namespace = name_space
                self.max_value.value_namespace_prefix = name_space_prefix
            if(value_path == "value"):
                self.value = value
                self.value.value_namespace = name_space
                self.value.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.enable.is_set or
            self.hold_timer.is_set or
            self.preferred_role.is_set or
            self.redundancy_disable.is_set or
            self.source_interface.is_set or
            (self.groups is not None and self.groups.has_data()) or
            (self.revertive_timer is not None and self.revertive_timer.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.hold_timer.yfilter != YFilter.not_set or
            self.preferred_role.yfilter != YFilter.not_set or
            self.redundancy_disable.yfilter != YFilter.not_set or
            self.source_interface.yfilter != YFilter.not_set or
            (self.groups is not None and self.groups.has_operation()) or
            (self.revertive_timer is not None and self.revertive_timer.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-serg-cfg:session-redundancy" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.hold_timer.is_set or self.hold_timer.yfilter != YFilter.not_set):
            leaf_name_data.append(self.hold_timer.get_name_leafdata())
        if (self.preferred_role.is_set or self.preferred_role.yfilter != YFilter.not_set):
            leaf_name_data.append(self.preferred_role.get_name_leafdata())
        if (self.redundancy_disable.is_set or self.redundancy_disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.redundancy_disable.get_name_leafdata())
        if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
            leaf_name_data.append(self.source_interface.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "groups"):
            if (self.groups is None):
                self.groups = SessionRedundancy.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
            return self.groups

        if (child_yang_name == "revertive-timer"):
            if (self.revertive_timer is None):
                self.revertive_timer = SessionRedundancy.RevertiveTimer()
                self.revertive_timer.parent = self
                self._children_name_map["revertive_timer"] = "revertive-timer"
            return self.revertive_timer

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "groups" or name == "revertive-timer" or name == "enable" or name == "hold-timer" or name == "preferred-role" or name == "redundancy-disable" or name == "source-interface"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "hold-timer"):
            self.hold_timer = value
            self.hold_timer.value_namespace = name_space
            self.hold_timer.value_namespace_prefix = name_space_prefix
        if(value_path == "preferred-role"):
            self.preferred_role = value
            self.preferred_role.value_namespace = name_space
            self.preferred_role.value_namespace_prefix = name_space_prefix
        if(value_path == "redundancy-disable"):
            self.redundancy_disable = value
            self.redundancy_disable.value_namespace = name_space
            self.redundancy_disable.value_namespace_prefix = name_space_prefix
        if(value_path == "source-interface"):
            self.source_interface = value
            self.source_interface.value_namespace = name_space
            self.source_interface.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = SessionRedundancy()
        return self._top_entity

