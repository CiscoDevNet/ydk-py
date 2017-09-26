""" Cisco_IOS_XR_subscriber_srg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\: Subscriber Redundancy configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"groups" : ("groups", SubscriberRedundancy.Groups), "revertive-timer" : ("revertive_timer", SubscriberRedundancy.RevertiveTimer)}
        self._child_list_classes = {}

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
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy"

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberRedundancy, ['enable', 'hold_timer', 'preferred_role', 'redundancy_disable', 'slave_mode', 'source_interface', 'virtual_mac_prefix'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"group" : ("group", SubscriberRedundancy.Groups.Group)}

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancy.Groups, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interface-list" : ("interface_list", SubscriberRedundancy.Groups.Group.InterfaceList), "peer" : ("peer", SubscriberRedundancy.Groups.Group.Peer), "revertive-timer" : ("revertive_timer", SubscriberRedundancy.Groups.Group.RevertiveTimer), "state-control-route" : ("state_control_route", SubscriberRedundancy.Groups.Group.StateControlRoute), "virtual-mac" : ("virtual_mac", SubscriberRedundancy.Groups.Group.VirtualMac)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "group" + "[group-id='" + self.group_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberRedundancy.Groups.Group, ['group_id', 'access_tracking_object', 'core_tracking_object', 'description', 'disable_tracking_object', 'enable', 'enable_fast_switchover', 'hold_timer', 'l2tp_source_ip_address', 'preferred_role', 'redundancy_disable', 'slave_mode'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interface-ranges" : ("interface_ranges", SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges), "interfaces" : ("interfaces", SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces)}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.empty, "enable")

                    self.interface_ranges = SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self._children_name_map["interface_ranges"] = "interface-ranges"
                    self._children_yang_names.add("interface-ranges")

                    self.interfaces = SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")
                    self._segment_path = lambda: "interface-list"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList, ['enable'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface-range" : ("interface_range", SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange)}

                        self.interface_range = YList(self)
                        self._segment_path = lambda: "interface-ranges"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges, [], name, value)


                    class InterfaceRange(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.sub_interface_range_start = YLeaf(YType.uint32, "sub-interface-range-start")

                            self.sub_interface_range_end = YLeaf(YType.uint32, "sub-interface-range-end")

                            self.interface_id_range_end = YLeaf(YType.uint32, "interface-id-range-end")

                            self.interface_id_range_start = YLeaf(YType.uint32, "interface-id-range-start")
                            self._segment_path = lambda: "interface-range" + "[interface-name='" + self.interface_name.get() + "']" + "[sub-interface-range-start='" + self.sub_interface_range_start.get() + "']" + "[sub-interface-range-end='" + self.sub_interface_range_end.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, ['interface_name', 'sub_interface_range_start', 'sub_interface_range_end', 'interface_id_range_end', 'interface_id_range_start'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface)}

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_id = YLeaf(YType.uint32, "interface-id")
                            self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"ipaddress" : ("ipaddress", SubscriberRedundancy.Groups.Group.Peer.Ipaddress)}
                    self._child_list_classes = {}

                    self.route_add_disable = YLeaf(YType.empty, "route-add-disable")

                    self.ipaddress = SubscriberRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self
                    self._children_name_map["ipaddress"] = "ipaddress"
                    self._children_yang_names.add("ipaddress")
                    self._segment_path = lambda: "peer"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.Peer, ['route_add_disable'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address_family = YLeaf(YType.enumeration, "address-family")

                        self.prefix_string = YLeaf(YType.str, "prefix-string")
                        self._segment_path = lambda: "ipaddress"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.Peer.Ipaddress, ['address_family', 'prefix_string'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.max_value = YLeaf(YType.uint32, "max-value")

                    self.value = YLeaf(YType.uint32, "value")
                    self._segment_path = lambda: "revertive-timer"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.RevertiveTimer, ['max_value', 'value'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"ipv4-routes" : ("ipv4_routes", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes), "ipv6-route" : ("ipv6_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route)}
                    self._child_list_classes = {}

                    self.ipv4_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes()
                    self.ipv4_routes.parent = self
                    self._children_name_map["ipv4_routes"] = "ipv4-routes"
                    self._children_yang_names.add("ipv4-routes")

                    self.ipv6_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route()
                    self.ipv6_route.parent = self
                    self._children_name_map["ipv6_route"] = "ipv6-route"
                    self._children_yang_names.add("ipv6-route")
                    self._segment_path = lambda: "state-control-route"


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"ipv4-route" : ("ipv4_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route)}

                        self.ipv4_route = YList(self)
                        self._segment_path = lambda: "ipv4-routes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes, [], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ipv4-route-data" : ("ipv4_route_data", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData)}
                            self._child_list_classes = {"vrfname" : ("vrfname", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname)}

                            self.prefix_string = YLeaf(YType.str, "prefix-string")

                            self.prefix_length = YLeaf(YType.int32, "prefix-length")

                            self.ipv4_route_data = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData()
                            self.ipv4_route_data.parent = self
                            self._children_name_map["ipv4_route_data"] = "ipv4-route-data"
                            self._children_yang_names.add("ipv4-route-data")

                            self.vrfname = YList(self)
                            self._segment_path = lambda: "ipv4-route" + "[prefix-string='" + self.prefix_string.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route, ['prefix_string', 'prefix_length'], name, value)


                        class Ipv4RouteData(Entity):
                            """
                            Data container.
                            
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData, self).__init__()

                                self.yang_name = "ipv4-route-data"
                                self.yang_parent_name = "ipv4-route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.tagvalue = YLeaf(YType.uint32, "tagvalue")
                                self._segment_path = lambda: "ipv4-route-data"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Ipv4RouteData, ['tagvalue'], name, value)


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
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname, self).__init__()

                                self.yang_name = "vrfname"
                                self.yang_parent_name = "ipv4-route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.vrfname = YLeaf(YType.str, "vrfname")

                                self.tagvalue = YLeaf(YType.uint32, "tagvalue")
                                self._segment_path = lambda: "vrfname" + "[vrfname='" + self.vrfname.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route.Vrfname, ['vrfname', 'tagvalue'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv6na-routes" : ("ipv6na_routes", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes), "ipv6pd-routes" : ("ipv6pd_routes", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes)}
                        self._child_list_classes = {}

                        self.ipv6na_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes()
                        self.ipv6na_routes.parent = self
                        self._children_name_map["ipv6na_routes"] = "ipv6na-routes"
                        self._children_yang_names.add("ipv6na-routes")

                        self.ipv6pd_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes()
                        self.ipv6pd_routes.parent = self
                        self._children_name_map["ipv6pd_routes"] = "ipv6pd-routes"
                        self._children_yang_names.add("ipv6pd-routes")
                        self._segment_path = lambda: "ipv6-route"


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"ipv6na-route" : ("ipv6na_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute)}

                            self.ipv6na_route = YList(self)
                            self._segment_path = lambda: "ipv6na-routes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes, [], name, value)


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
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute, self).__init__()

                                self.yang_name = "ipv6na-route"
                                self.yang_parent_name = "ipv6na-routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.vrfname = YLeaf(YType.str, "vrfname")

                                self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                self.prefix_string = YLeaf(YType.str, "prefix-string")

                                self.tagvalue = YLeaf(YType.uint32, "tagvalue")
                                self._segment_path = lambda: "ipv6na-route" + "[vrfname='" + self.vrfname.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + "[prefix-string='" + self.prefix_string.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoutes.Ipv6NaRoute, ['vrfname', 'prefix_length', 'prefix_string', 'tagvalue'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"ipv6pd-route" : ("ipv6pd_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute)}

                            self.ipv6pd_route = YList(self)
                            self._segment_path = lambda: "ipv6pd-routes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes, [], name, value)


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
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute, self).__init__()

                                self.yang_name = "ipv6pd-route"
                                self.yang_parent_name = "ipv6pd-routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.vrfname = YLeaf(YType.str, "vrfname")

                                self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                self.prefix_string = YLeaf(YType.str, "prefix-string")

                                self.tagvalue = YLeaf(YType.uint32, "tagvalue")
                                self._segment_path = lambda: "ipv6pd-route" + "[vrfname='" + self.vrfname.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + "[prefix-string='" + self.prefix_string.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoutes.Ipv6PdRoute, ['vrfname', 'prefix_length', 'prefix_string', 'tagvalue'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.address = YLeaf(YType.str, "address")

                    self.disable = YLeaf(YType.empty, "disable")
                    self._segment_path = lambda: "virtual-mac"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.VirtualMac, ['address', 'disable'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.max_value = YLeaf(YType.uint32, "max-value")

            self.value = YLeaf(YType.uint32, "value")
            self._segment_path = lambda: "revertive-timer"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancy.RevertiveTimer, ['max_value', 'value'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberRedundancy()
        return self._top_entity

