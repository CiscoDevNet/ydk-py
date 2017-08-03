""" Cisco_IOS_XR_subscriber_srg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\: Subscriber Redundancy configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrgAddrFamily(Enum):
    """
    SrgAddrFamily

    Srg addr family

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(10, "ipv6")


class SubscriberRedundancyGroupRole(Enum):
    """
    SubscriberRedundancyGroupRole

    Subscriber redundancy group role

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class SubscriberRedundancyGroupSlaveMode(Enum):
    """
    SubscriberRedundancyGroupSlaveMode

    Subscriber redundancy group slave mode

    .. data:: warm = 1

    	Warm Mode

    .. data:: hot = 2

    	Hot Mode

    """

    warm = Enum.YLeaf(1, "warm")

    hot = Enum.YLeaf(2, "hot")



class SubscriberRedundancy(Entity):
    """
    Subscriber Redundancy configuration
    
    .. attribute:: enable
    
    	Enable Subscriber Redundancy configuration. Deletion of this object also causes deletion of all associated objects under SubscriberRedundancy
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Table of Group
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups>`
    
    .. attribute:: hold_timer
    
    	Set hold time (in Minutes)
    	**type**\:  int
    
    	**range:** 1..65535
    
    	**units**\: minute
    
    .. attribute:: preferred_role
    
    	Set preferred role
    	**type**\:   :py:class:`SubscriberRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupRole>`
    
    .. attribute:: redundancy_disable
    
    	Disable
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: revertive_timer
    
    	None
    	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.RevertiveTimer>`
    
    .. attribute:: slave_mode
    
    	Set slave
    	**type**\:   :py:class:`SubscriberRedundancyGroupSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupSlaveMode>`
    
    .. attribute:: source_interface
    
    	Source Interface for Redundancy Peer Communication
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: virtual_mac_prefix
    
    	Virtual MAC Prefix for Subscriber Redundancy
    	**type**\:  str
    
    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
    
    

    """

    _prefix = 'subscriber-srg-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberRedundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-srg-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.hold_timer = YLeaf(YType.uint32, "hold-timer")

        self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

        self.redundancy_disable = YLeaf(YType.empty, "redundancy-disable")

        self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

        self.source_interface = YLeaf(YType.str, "source-interface")

        self.virtual_mac_prefix = YLeaf(YType.str, "virtual-mac-prefix")

        self.groups = SubscriberRedundancy.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.revertive_timer = SubscriberRedundancy.RevertiveTimer()
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
                        "slave_mode",
                        "source_interface",
                        "virtual_mac_prefix") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(SubscriberRedundancy, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SubscriberRedundancy, self).__setattr__(name, value)


    class Groups(Entity):
        """
        Table of Group
        
        .. attribute:: group
        
        	Redundancy Group configuration
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group>`
        
        

        """

        _prefix = 'subscriber-srg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancy.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "subscriber-redundancy"

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
                        super(SubscriberRedundancy.Groups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberRedundancy.Groups, self).__setattr__(name, value)


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
            
            .. attribute:: enable_fast_switchover
            
            	Enable fast switchover for this Group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hold_timer
            
            	Set hold time (in Minutes)
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: minute
            
            .. attribute:: interface_list
            
            	List of Interfaces for this Group
            	**type**\:   :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList>`
            
            .. attribute:: l2tp_source_ip_address
            
            	Enter an IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer
            
            	None
            	**type**\:   :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.Peer>`
            
            .. attribute:: preferred_role
            
            	Set preferred role
            	**type**\:   :py:class:`SubscriberRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupRole>`
            
            .. attribute:: redundancy_disable
            
            	Disable
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: revertive_timer
            
            	None
            	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.RevertiveTimer>`
            
            .. attribute:: slave_mode
            
            	Set Slave Mode
            	**type**\:   :py:class:`SubscriberRedundancyGroupSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupSlaveMode>`
            
            .. attribute:: state_control_route
            
            	None
            	**type**\:   :py:class:`StateControlRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute>`
            
            .. attribute:: virtual_mac
            
            	Virtual MAC Address for this Group
            	**type**\:   :py:class:`VirtualMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.VirtualMac>`
            
            

            """

            _prefix = 'subscriber-srg-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancy.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"

                self.group_id = YLeaf(YType.uint32, "group-id")

                self.access_tracking_object = YLeaf(YType.str, "access-tracking-object")

                self.core_tracking_object = YLeaf(YType.str, "core-tracking-object")

                self.description = YLeaf(YType.str, "description")

                self.disable_tracking_object = YLeaf(YType.empty, "disable-tracking-object")

                self.enable = YLeaf(YType.empty, "enable")

                self.enable_fast_switchover = YLeaf(YType.empty, "enable-fast-switchover")

                self.hold_timer = YLeaf(YType.uint32, "hold-timer")

                self.l2tp_source_ip_address = YLeaf(YType.str, "l2tp-source-ip-address")

                self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

                self.redundancy_disable = YLeaf(YType.empty, "redundancy-disable")

                self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

                self.interface_list = SubscriberRedundancy.Groups.Group.InterfaceList()
                self.interface_list.parent = self
                self._children_name_map["interface_list"] = "interface-list"
                self._children_yang_names.add("interface-list")

                self.peer = SubscriberRedundancy.Groups.Group.Peer()
                self.peer.parent = self
                self._children_name_map["peer"] = "peer"
                self._children_yang_names.add("peer")

                self.revertive_timer = SubscriberRedundancy.Groups.Group.RevertiveTimer()
                self.revertive_timer.parent = self
                self._children_name_map["revertive_timer"] = "revertive-timer"
                self._children_yang_names.add("revertive-timer")

                self.state_control_route = SubscriberRedundancy.Groups.Group.StateControlRoute()
                self.state_control_route.parent = self
                self._children_name_map["state_control_route"] = "state-control-route"
                self._children_yang_names.add("state-control-route")

                self.virtual_mac = SubscriberRedundancy.Groups.Group.VirtualMac()
                self.virtual_mac.parent = self
                self._children_name_map["virtual_mac"] = "virtual-mac"
                self._children_yang_names.add("virtual-mac")

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
                                "enable_fast_switchover",
                                "hold_timer",
                                "l2tp_source_ip_address",
                                "preferred_role",
                                "redundancy_disable",
                                "slave_mode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SubscriberRedundancy.Groups.Group, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberRedundancy.Groups.Group, self).__setattr__(name, value)


            class InterfaceList(Entity):
                """
                List of Interfaces for this Group
                
                .. attribute:: enable
                
                	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList 
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface_ranges
                
                	Table of InterfaceRange
                	**type**\:   :py:class:`InterfaceRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges>`
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.InterfaceList, self).__init__()

                    self.yang_name = "interface-list"
                    self.yang_parent_name = "group"

                    self.enable = YLeaf(YType.empty, "enable")

                    self.interface_ranges = SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self._children_name_map["interface_ranges"] = "interface-ranges"
                    self._children_yang_names.add("interface-ranges")

                    self.interfaces = SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces()
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
                                super(SubscriberRedundancy.Groups.Group.InterfaceList, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancy.Groups.Group.InterfaceList, self).__setattr__(name, value)


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

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
                                    super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces, self).__setattr__(name, value)


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

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__init__()

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
                                        super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__setattr__(name, value)

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
                            c = SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface()
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


                class InterfaceRanges(Entity):
                    """
                    Table of InterfaceRange
                    
                    .. attribute:: interface_range
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`InterfaceRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__init__()

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
                                    super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__setattr__(name, value)


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

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__init__()

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
                                        super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__setattr__(name, value)

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
                            c = SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange()
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
                            self.interface_ranges = SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                            self.interface_ranges.parent = self
                            self._children_name_map["interface_ranges"] = "interface-ranges"
                        return self.interface_ranges

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces()
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


            class Peer(Entity):
                """
                None
                
                .. attribute:: ipaddress
                
                	IPv4 or IPv6 Address of SRG Peer
                	**type**\:   :py:class:`Ipaddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.Peer.Ipaddress>`
                
                .. attribute:: route_add_disable
                
                	Set Route add disable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "group"

                    self.route_add_disable = YLeaf(YType.empty, "route-add-disable")

                    self.ipaddress = SubscriberRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self
                    self._children_name_map["ipaddress"] = "ipaddress"
                    self._children_yang_names.add("ipaddress")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("route_add_disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SubscriberRedundancy.Groups.Group.Peer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancy.Groups.Group.Peer, self).__setattr__(name, value)


                class Ipaddress(Entity):
                    """
                    IPv4 or IPv6 Address of SRG Peer
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4/IPv6 address
                    	**type**\:   :py:class:`SrgAddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SrgAddrFamily>`
                    
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

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.Peer.Ipaddress, self).__init__()

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
                                    super(SubscriberRedundancy.Groups.Group.Peer.Ipaddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancy.Groups.Group.Peer.Ipaddress, self).__setattr__(name, value)

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
                    return (
                        self.route_add_disable.is_set or
                        (self.ipaddress is not None and self.ipaddress.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.route_add_disable.yfilter != YFilter.not_set or
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
                    if (self.route_add_disable.is_set or self.route_add_disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_add_disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipaddress"):
                        if (self.ipaddress is None):
                            self.ipaddress = SubscriberRedundancy.Groups.Group.Peer.Ipaddress()
                            self.ipaddress.parent = self
                            self._children_name_map["ipaddress"] = "ipaddress"
                        return self.ipaddress

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipaddress" or name == "route-add-disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "route-add-disable"):
                        self.route_add_disable = value
                        self.route_add_disable.value_namespace = name_space
                        self.route_add_disable.value_namespace_prefix = name_space_prefix


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

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.RevertiveTimer, self).__init__()

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
                                super(SubscriberRedundancy.Groups.Group.RevertiveTimer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancy.Groups.Group.RevertiveTimer, self).__setattr__(name, value)

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


            class VirtualMac(Entity):
                """
                Virtual MAC Address for this Group
                
                .. attribute:: address
                
                	Virtual MAC Address for this Group
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: disable
                
                	Disable Virtual MAC Address for this Group
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.VirtualMac, self).__init__()

                    self.yang_name = "virtual-mac"
                    self.yang_parent_name = "group"

                    self.address = YLeaf(YType.str, "address")

                    self.disable = YLeaf(YType.empty, "disable")

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
                                    "disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SubscriberRedundancy.Groups.Group.VirtualMac, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancy.Groups.Group.VirtualMac, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.disable.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.disable.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "virtual-mac" + path_buffer

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
                    if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "disable"):
                        self.disable = value
                        self.disable.value_namespace = name_space
                        self.disable.value_namespace_prefix = name_space_prefix


            class StateControlRoute(Entity):
                """
                None
                
                .. attribute:: ipv4_routes
                
                	Table of IPv4Route
                	**type**\:   :py:class:`Ipv4Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes>`
                
                .. attribute:: ipv6_route
                
                	None
                	**type**\:   :py:class:`Ipv6Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.StateControlRoute, self).__init__()

                    self.yang_name = "state-control-route"
                    self.yang_parent_name = "group"

                    self.ipv4_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes()
                    self.ipv4_routes.parent = self
                    self._children_name_map["ipv4_routes"] = "ipv4-routes"
                    self._children_yang_names.add("ipv4-routes")

                    self.ipv6_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route()
                    self.ipv6_route.parent = self
                    self._children_name_map["ipv6_route"] = "ipv6-route"
                    self._children_yang_names.add("ipv6-route")


                class Ipv4Routes(Entity):
                    """
                    Table of IPv4Route
                    
                    .. attribute:: ipv4_route
                    
                    	None
                    	**type**\: list of    :py:class:`Ipv4Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes, self).__init__()

                        self.yang_name = "ipv4-routes"
                        self.yang_parent_name = "state-control-route"

                        self.ipv4_route = YList(self)

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
                                    super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes, self).__setattr__(name, value)


                    class Ipv4Route(Entity):
                        """
                        None
                        
                        .. attribute:: prefix_string  <key>
                        
                        	IPv4 address with prefix\-length
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: prefix_length  <key>
                        
                        	Prefix of the IP Address
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ipv4_route_data
                        
                        	Data container
                        	**type**\:   :py:class:`Ipv4RouteData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData>`
                        
                        .. attribute:: vrfname
                        
                        	keys\: vrfname
                        	**type**\: list of    :py:class:`Vrfname <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname>`
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route, self).__init__()

                            self.yang_name = "ipv4-route"
                            self.yang_parent_name = "ipv4-routes"

                            self.prefix_string = YLeaf(YType.str, "prefix-string")

                            self.prefix_length = YLeaf(YType.int32, "prefix-length")

                            self.ipv4_route_data = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData()
                            self.ipv4_route_data.parent = self
                            self._children_name_map["ipv4_route_data"] = "ipv4-route-data"
                            self._children_yang_names.add("ipv4-route-data")

                            self.vrfname = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("prefix_string",
                                            "prefix_length") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route, self).__setattr__(name, value)


                        class Ipv4RouteData(Entity):
                            """
                            Data container.
                            
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData, self).__init__()

                                self.yang_name = "ipv4-route-data"
                                self.yang_parent_name = "ipv4-route"

                                self.tagvalue = YLeaf(YType.int32, "tagvalue")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("tagvalue") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData, self).__setattr__(name, value)

                            def has_data(self):
                                return self.tagvalue.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.tagvalue.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-route-data" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.tagvalue.is_set or self.tagvalue.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tagvalue.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tagvalue"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "tagvalue"):
                                    self.tagvalue = value
                                    self.tagvalue.value_namespace = name_space
                                    self.tagvalue.value_namespace_prefix = name_space_prefix


                        class Vrfname(Entity):
                            """
                            keys\: vrfname
                            
                            .. attribute:: vrfname  <key>
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname, self).__init__()

                                self.yang_name = "vrfname"
                                self.yang_parent_name = "ipv4-route"

                                self.vrfname = YLeaf(YType.str, "vrfname")

                                self.tagvalue = YLeaf(YType.int32, "tagvalue")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("vrfname",
                                                "tagvalue") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.vrfname.is_set or
                                    self.tagvalue.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.vrfname.yfilter != YFilter.not_set or
                                    self.tagvalue.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "vrfname" + "[vrfname='" + self.vrfname.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.vrfname.is_set or self.vrfname.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrfname.get_name_leafdata())
                                if (self.tagvalue.is_set or self.tagvalue.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tagvalue.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "vrfname" or name == "tagvalue"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "vrfname"):
                                    self.vrfname = value
                                    self.vrfname.value_namespace = name_space
                                    self.vrfname.value_namespace_prefix = name_space_prefix
                                if(value_path == "tagvalue"):
                                    self.tagvalue = value
                                    self.tagvalue.value_namespace = name_space
                                    self.tagvalue.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.vrfname:
                                if (c.has_data()):
                                    return True
                            return (
                                self.prefix_string.is_set or
                                self.prefix_length.is_set or
                                (self.ipv4_route_data is not None and self.ipv4_route_data.has_data()))

                        def has_operation(self):
                            for c in self.vrfname:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.prefix_string.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                (self.ipv4_route_data is not None and self.ipv4_route_data.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4-route" + "[prefix-string='" + self.prefix_string.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

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
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv4-route-data"):
                                if (self.ipv4_route_data is None):
                                    self.ipv4_route_data = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData()
                                    self.ipv4_route_data.parent = self
                                    self._children_name_map["ipv4_route_data"] = "ipv4-route-data"
                                return self.ipv4_route_data

                            if (child_yang_name == "vrfname"):
                                for c in self.vrfname:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.vrfname.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-route-data" or name == "vrfname" or name == "prefix-string" or name == "prefix-length"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "prefix-string"):
                                self.prefix_string = value
                                self.prefix_string.value_namespace = name_space
                                self.prefix_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ipv4_route:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ipv4_route:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-routes" + path_buffer

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

                        if (child_yang_name == "ipv4-route"):
                            for c in self.ipv4_route:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ipv4_route.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4-route"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Ipv6Route(Entity):
                    """
                    None
                    
                    .. attribute:: ipv6na_routes
                    
                    	Table of IPv6NARoute
                    	**type**\:   :py:class:`Ipv6NaRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes>`
                    
                    .. attribute:: ipv6pd_routes
                    
                    	Table of IPv6PDRoute
                    	**type**\:   :py:class:`Ipv6PdRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route, self).__init__()

                        self.yang_name = "ipv6-route"
                        self.yang_parent_name = "state-control-route"

                        self.ipv6na_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes()
                        self.ipv6na_routes.parent = self
                        self._children_name_map["ipv6na_routes"] = "ipv6na-routes"
                        self._children_yang_names.add("ipv6na-routes")

                        self.ipv6pd_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes()
                        self.ipv6pd_routes.parent = self
                        self._children_name_map["ipv6pd_routes"] = "ipv6pd-routes"
                        self._children_yang_names.add("ipv6pd-routes")


                    class Ipv6NaRoutes(Entity):
                        """
                        Table of IPv6NARoute
                        
                        .. attribute:: ipv6na_route
                        
                        	None
                        	**type**\: list of    :py:class:`Ipv6NaRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute>`
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes, self).__init__()

                            self.yang_name = "ipv6na-routes"
                            self.yang_parent_name = "ipv6-route"

                            self.ipv6na_route = YList(self)

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
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes, self).__setattr__(name, value)


                        class Ipv6NaRoute(Entity):
                            """
                            None
                            
                            .. attribute:: vrfname  <key>
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: prefix_length  <key>
                            
                            	Prefix of the IP Address
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: prefix_string  <key>
                            
                            	IPv6 address with prefix\-length
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute, self).__init__()

                                self.yang_name = "ipv6na-route"
                                self.yang_parent_name = "ipv6na-routes"

                                self.vrfname = YLeaf(YType.str, "vrfname")

                                self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                self.prefix_string = YLeaf(YType.str, "prefix-string")

                                self.tagvalue = YLeaf(YType.int32, "tagvalue")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("vrfname",
                                                "prefix_length",
                                                "prefix_string",
                                                "tagvalue") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.vrfname.is_set or
                                    self.prefix_length.is_set or
                                    self.prefix_string.is_set or
                                    self.tagvalue.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.vrfname.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.prefix_string.yfilter != YFilter.not_set or
                                    self.tagvalue.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6na-route" + "[vrfname='" + self.vrfname.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + "[prefix-string='" + self.prefix_string.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.vrfname.is_set or self.vrfname.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrfname.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.prefix_string.is_set or self.prefix_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_string.get_name_leafdata())
                                if (self.tagvalue.is_set or self.tagvalue.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tagvalue.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "vrfname" or name == "prefix-length" or name == "prefix-string" or name == "tagvalue"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "vrfname"):
                                    self.vrfname = value
                                    self.vrfname.value_namespace = name_space
                                    self.vrfname.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-string"):
                                    self.prefix_string = value
                                    self.prefix_string.value_namespace = name_space
                                    self.prefix_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "tagvalue"):
                                    self.tagvalue = value
                                    self.tagvalue.value_namespace = name_space
                                    self.tagvalue.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.ipv6na_route:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.ipv6na_route:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6na-routes" + path_buffer

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

                            if (child_yang_name == "ipv6na-route"):
                                for c in self.ipv6na_route:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.ipv6na_route.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6na-route"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Ipv6PdRoutes(Entity):
                        """
                        Table of IPv6PDRoute
                        
                        .. attribute:: ipv6pd_route
                        
                        	None
                        	**type**\: list of    :py:class:`Ipv6PdRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute>`
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes, self).__init__()

                            self.yang_name = "ipv6pd-routes"
                            self.yang_parent_name = "ipv6-route"

                            self.ipv6pd_route = YList(self)

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
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes, self).__setattr__(name, value)


                        class Ipv6PdRoute(Entity):
                            """
                            None
                            
                            .. attribute:: vrfname  <key>
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: prefix_length  <key>
                            
                            	Prefix of the IP Address
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: prefix_string  <key>
                            
                            	IPv6 address with prefix\-length
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute, self).__init__()

                                self.yang_name = "ipv6pd-route"
                                self.yang_parent_name = "ipv6pd-routes"

                                self.vrfname = YLeaf(YType.str, "vrfname")

                                self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                self.prefix_string = YLeaf(YType.str, "prefix-string")

                                self.tagvalue = YLeaf(YType.int32, "tagvalue")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("vrfname",
                                                "prefix_length",
                                                "prefix_string",
                                                "tagvalue") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.vrfname.is_set or
                                    self.prefix_length.is_set or
                                    self.prefix_string.is_set or
                                    self.tagvalue.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.vrfname.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.prefix_string.yfilter != YFilter.not_set or
                                    self.tagvalue.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6pd-route" + "[vrfname='" + self.vrfname.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + "[prefix-string='" + self.prefix_string.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.vrfname.is_set or self.vrfname.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrfname.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.prefix_string.is_set or self.prefix_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_string.get_name_leafdata())
                                if (self.tagvalue.is_set or self.tagvalue.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tagvalue.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "vrfname" or name == "prefix-length" or name == "prefix-string" or name == "tagvalue"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "vrfname"):
                                    self.vrfname = value
                                    self.vrfname.value_namespace = name_space
                                    self.vrfname.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-string"):
                                    self.prefix_string = value
                                    self.prefix_string.value_namespace = name_space
                                    self.prefix_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "tagvalue"):
                                    self.tagvalue = value
                                    self.tagvalue.value_namespace = name_space
                                    self.tagvalue.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.ipv6pd_route:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.ipv6pd_route:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6pd-routes" + path_buffer

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

                            if (child_yang_name == "ipv6pd-route"):
                                for c in self.ipv6pd_route:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.ipv6pd_route.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6pd-route"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.ipv6na_routes is not None and self.ipv6na_routes.has_data()) or
                            (self.ipv6pd_routes is not None and self.ipv6pd_routes.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.ipv6na_routes is not None and self.ipv6na_routes.has_operation()) or
                            (self.ipv6pd_routes is not None and self.ipv6pd_routes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-route" + path_buffer

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

                        if (child_yang_name == "ipv6na-routes"):
                            if (self.ipv6na_routes is None):
                                self.ipv6na_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes()
                                self.ipv6na_routes.parent = self
                                self._children_name_map["ipv6na_routes"] = "ipv6na-routes"
                            return self.ipv6na_routes

                        if (child_yang_name == "ipv6pd-routes"):
                            if (self.ipv6pd_routes is None):
                                self.ipv6pd_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes()
                                self.ipv6pd_routes.parent = self
                                self._children_name_map["ipv6pd_routes"] = "ipv6pd-routes"
                            return self.ipv6pd_routes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv6na-routes" or name == "ipv6pd-routes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.ipv4_routes is not None and self.ipv4_routes.has_data()) or
                        (self.ipv6_route is not None and self.ipv6_route.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipv4_routes is not None and self.ipv4_routes.has_operation()) or
                        (self.ipv6_route is not None and self.ipv6_route.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state-control-route" + path_buffer

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

                    if (child_yang_name == "ipv4-routes"):
                        if (self.ipv4_routes is None):
                            self.ipv4_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes()
                            self.ipv4_routes.parent = self
                            self._children_name_map["ipv4_routes"] = "ipv4-routes"
                        return self.ipv4_routes

                    if (child_yang_name == "ipv6-route"):
                        if (self.ipv6_route is None):
                            self.ipv6_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route()
                            self.ipv6_route.parent = self
                            self._children_name_map["ipv6_route"] = "ipv6-route"
                        return self.ipv6_route

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-routes" or name == "ipv6-route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.group_id.is_set or
                    self.access_tracking_object.is_set or
                    self.core_tracking_object.is_set or
                    self.description.is_set or
                    self.disable_tracking_object.is_set or
                    self.enable.is_set or
                    self.enable_fast_switchover.is_set or
                    self.hold_timer.is_set or
                    self.l2tp_source_ip_address.is_set or
                    self.preferred_role.is_set or
                    self.redundancy_disable.is_set or
                    self.slave_mode.is_set or
                    (self.interface_list is not None and self.interface_list.has_data()) or
                    (self.peer is not None and self.peer.has_data()) or
                    (self.revertive_timer is not None and self.revertive_timer.has_data()) or
                    (self.state_control_route is not None and self.state_control_route.has_data()) or
                    (self.virtual_mac is not None and self.virtual_mac.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.group_id.yfilter != YFilter.not_set or
                    self.access_tracking_object.yfilter != YFilter.not_set or
                    self.core_tracking_object.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.disable_tracking_object.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.enable_fast_switchover.yfilter != YFilter.not_set or
                    self.hold_timer.yfilter != YFilter.not_set or
                    self.l2tp_source_ip_address.yfilter != YFilter.not_set or
                    self.preferred_role.yfilter != YFilter.not_set or
                    self.redundancy_disable.yfilter != YFilter.not_set or
                    self.slave_mode.yfilter != YFilter.not_set or
                    (self.interface_list is not None and self.interface_list.has_operation()) or
                    (self.peer is not None and self.peer.has_operation()) or
                    (self.revertive_timer is not None and self.revertive_timer.has_operation()) or
                    (self.state_control_route is not None and self.state_control_route.has_operation()) or
                    (self.virtual_mac is not None and self.virtual_mac.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/groups/%s" % self.get_segment_path()
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
                if (self.enable_fast_switchover.is_set or self.enable_fast_switchover.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable_fast_switchover.get_name_leafdata())
                if (self.hold_timer.is_set or self.hold_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_timer.get_name_leafdata())
                if (self.l2tp_source_ip_address.is_set or self.l2tp_source_ip_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.l2tp_source_ip_address.get_name_leafdata())
                if (self.preferred_role.is_set or self.preferred_role.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.preferred_role.get_name_leafdata())
                if (self.redundancy_disable.is_set or self.redundancy_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.redundancy_disable.get_name_leafdata())
                if (self.slave_mode.is_set or self.slave_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slave_mode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-list"):
                    if (self.interface_list is None):
                        self.interface_list = SubscriberRedundancy.Groups.Group.InterfaceList()
                        self.interface_list.parent = self
                        self._children_name_map["interface_list"] = "interface-list"
                    return self.interface_list

                if (child_yang_name == "peer"):
                    if (self.peer is None):
                        self.peer = SubscriberRedundancy.Groups.Group.Peer()
                        self.peer.parent = self
                        self._children_name_map["peer"] = "peer"
                    return self.peer

                if (child_yang_name == "revertive-timer"):
                    if (self.revertive_timer is None):
                        self.revertive_timer = SubscriberRedundancy.Groups.Group.RevertiveTimer()
                        self.revertive_timer.parent = self
                        self._children_name_map["revertive_timer"] = "revertive-timer"
                    return self.revertive_timer

                if (child_yang_name == "state-control-route"):
                    if (self.state_control_route is None):
                        self.state_control_route = SubscriberRedundancy.Groups.Group.StateControlRoute()
                        self.state_control_route.parent = self
                        self._children_name_map["state_control_route"] = "state-control-route"
                    return self.state_control_route

                if (child_yang_name == "virtual-mac"):
                    if (self.virtual_mac is None):
                        self.virtual_mac = SubscriberRedundancy.Groups.Group.VirtualMac()
                        self.virtual_mac.parent = self
                        self._children_name_map["virtual_mac"] = "virtual-mac"
                    return self.virtual_mac

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-list" or name == "peer" or name == "revertive-timer" or name == "state-control-route" or name == "virtual-mac" or name == "group-id" or name == "access-tracking-object" or name == "core-tracking-object" or name == "description" or name == "disable-tracking-object" or name == "enable" or name == "enable-fast-switchover" or name == "hold-timer" or name == "l2tp-source-ip-address" or name == "preferred-role" or name == "redundancy-disable" or name == "slave-mode"):
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
                if(value_path == "enable-fast-switchover"):
                    self.enable_fast_switchover = value
                    self.enable_fast_switchover.value_namespace = name_space
                    self.enable_fast_switchover.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-timer"):
                    self.hold_timer = value
                    self.hold_timer.value_namespace = name_space
                    self.hold_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "l2tp-source-ip-address"):
                    self.l2tp_source_ip_address = value
                    self.l2tp_source_ip_address.value_namespace = name_space
                    self.l2tp_source_ip_address.value_namespace_prefix = name_space_prefix
                if(value_path == "preferred-role"):
                    self.preferred_role = value
                    self.preferred_role.value_namespace = name_space
                    self.preferred_role.value_namespace_prefix = name_space_prefix
                if(value_path == "redundancy-disable"):
                    self.redundancy_disable = value
                    self.redundancy_disable.value_namespace = name_space
                    self.redundancy_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "slave-mode"):
                    self.slave_mode = value
                    self.slave_mode.value_namespace = name_space
                    self.slave_mode.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/%s" % self.get_segment_path()
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
                c = SubscriberRedundancy.Groups.Group()
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

        _prefix = 'subscriber-srg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancy.RevertiveTimer, self).__init__()

            self.yang_name = "revertive-timer"
            self.yang_parent_name = "subscriber-redundancy"

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
                        super(SubscriberRedundancy.RevertiveTimer, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberRedundancy.RevertiveTimer, self).__setattr__(name, value)

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
                path_buffer = "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/%s" % self.get_segment_path()
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
            self.slave_mode.is_set or
            self.source_interface.is_set or
            self.virtual_mac_prefix.is_set or
            (self.groups is not None and self.groups.has_data()) or
            (self.revertive_timer is not None and self.revertive_timer.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.hold_timer.yfilter != YFilter.not_set or
            self.preferred_role.yfilter != YFilter.not_set or
            self.redundancy_disable.yfilter != YFilter.not_set or
            self.slave_mode.yfilter != YFilter.not_set or
            self.source_interface.yfilter != YFilter.not_set or
            self.virtual_mac_prefix.yfilter != YFilter.not_set or
            (self.groups is not None and self.groups.has_operation()) or
            (self.revertive_timer is not None and self.revertive_timer.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy" + path_buffer

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
        if (self.slave_mode.is_set or self.slave_mode.yfilter != YFilter.not_set):
            leaf_name_data.append(self.slave_mode.get_name_leafdata())
        if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
            leaf_name_data.append(self.source_interface.get_name_leafdata())
        if (self.virtual_mac_prefix.is_set or self.virtual_mac_prefix.yfilter != YFilter.not_set):
            leaf_name_data.append(self.virtual_mac_prefix.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "groups"):
            if (self.groups is None):
                self.groups = SubscriberRedundancy.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
            return self.groups

        if (child_yang_name == "revertive-timer"):
            if (self.revertive_timer is None):
                self.revertive_timer = SubscriberRedundancy.RevertiveTimer()
                self.revertive_timer.parent = self
                self._children_name_map["revertive_timer"] = "revertive-timer"
            return self.revertive_timer

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "groups" or name == "revertive-timer" or name == "enable" or name == "hold-timer" or name == "preferred-role" or name == "redundancy-disable" or name == "slave-mode" or name == "source-interface" or name == "virtual-mac-prefix"):
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
        if(value_path == "slave-mode"):
            self.slave_mode = value
            self.slave_mode.value_namespace = name_space
            self.slave_mode.value_namespace_prefix = name_space_prefix
        if(value_path == "source-interface"):
            self.source_interface = value
            self.source_interface.value_namespace = name_space
            self.source_interface.value_namespace_prefix = name_space_prefix
        if(value_path == "virtual-mac-prefix"):
            self.virtual_mac_prefix = value
            self.virtual_mac_prefix.value_namespace = name_space
            self.virtual_mac_prefix.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = SubscriberRedundancy()
        return self._top_entity

