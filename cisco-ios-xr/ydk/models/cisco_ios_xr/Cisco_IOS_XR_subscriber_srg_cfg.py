""" Cisco_IOS_XR_subscriber_srg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\: Subscriber Redundancy configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SrgAddrFamily(Enum):
    """
    SrgAddrFamily (Enum Class)

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
    SubscriberRedundancyGroupRole (Enum Class)

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
    SubscriberRedundancyGroupSlaveMode (Enum Class)

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
    
    .. attribute:: groups
    
    	Table of Group
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups>`
    
    .. attribute:: revertive_timer
    
    	None
    	**type**\:  :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.RevertiveTimer>`
    
    .. attribute:: enable
    
    	Enable Subscriber Redundancy configuration. Deletion of this object also causes deletion of all associated objects under SubscriberRedundancy
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: virtual_mac_prefix
    
    	Virtual MAC Prefix for Subscriber Redundancy
    	**type**\: str
    
    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
    
    .. attribute:: preferred_role
    
    	Set preferred role
    	**type**\:  :py:class:`SubscriberRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupRole>`
    
    .. attribute:: source_interface
    
    	Source Interface for Redundancy Peer Communication
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
    
    .. attribute:: slave_mode
    
    	Set slave
    	**type**\:  :py:class:`SubscriberRedundancyGroupSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupSlaveMode>`
    
    .. attribute:: hold_timer
    
    	Set hold time (in Minutes)
    	**type**\: int
    
    	**range:** 1..65535
    
    	**units**\: minute
    
    .. attribute:: redundancy_disable
    
    	Disable
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'subscriber-srg-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(SubscriberRedundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-srg-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("groups", ("groups", SubscriberRedundancy.Groups)), ("revertive-timer", ("revertive_timer", SubscriberRedundancy.RevertiveTimer))])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('virtual_mac_prefix', (YLeaf(YType.str, 'virtual-mac-prefix'), ['str'])),
            ('preferred_role', (YLeaf(YType.enumeration, 'preferred-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupRole', '')])),
            ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
            ('slave_mode', (YLeaf(YType.enumeration, 'slave-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupSlaveMode', '')])),
            ('hold_timer', (YLeaf(YType.uint32, 'hold-timer'), ['int'])),
            ('redundancy_disable', (YLeaf(YType.empty, 'redundancy-disable'), ['Empty'])),
        ])
        self.enable = None
        self.virtual_mac_prefix = None
        self.preferred_role = None
        self.source_interface = None
        self.slave_mode = None
        self.hold_timer = None
        self.redundancy_disable = None

        self.groups = SubscriberRedundancy.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"

        self.revertive_timer = SubscriberRedundancy.RevertiveTimer()
        self.revertive_timer.parent = self
        self._children_name_map["revertive_timer"] = "revertive-timer"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberRedundancy, ['enable', 'virtual_mac_prefix', 'preferred_role', 'source_interface', 'slave_mode', 'hold_timer', 'redundancy_disable'], name, value)


    class Groups(Entity):
        """
        Table of Group
        
        .. attribute:: group
        
        	Redundancy Group configuration
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group>`
        
        

        """

        _prefix = 'subscriber-srg-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(SubscriberRedundancy.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "subscriber-redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", SubscriberRedundancy.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancy.Groups, [], name, value)


        class Group(Entity):
            """
            Redundancy Group configuration
            
            .. attribute:: group_id  (key)
            
            	Group ID
            	**type**\: int
            
            	**range:** 1..4000
            
            .. attribute:: interface_list
            
            	List of Interfaces for this Group
            	**type**\:  :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList>`
            
            	**presence node**\: True
            
            .. attribute:: peer
            
            	None
            	**type**\:  :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.Peer>`
            
            .. attribute:: revertive_timer
            
            	None
            	**type**\:  :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.RevertiveTimer>`
            
            .. attribute:: virtual_mac
            
            	Virtual MAC Address for this Group
            	**type**\:  :py:class:`VirtualMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.VirtualMac>`
            
            .. attribute:: state_control_route
            
            	None
            	**type**\:  :py:class:`StateControlRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute>`
            
            .. attribute:: disable_tracking_object
            
            	Disable Tracking Object for this Group
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: core_tracking_object
            
            	Core Tracking Object for this Group
            	**type**\: str
            
            .. attribute:: enable
            
            	Enable Redundancy Group configuration. Deletion of this object also causes deletion of all associated objects under Group
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            	**mandatory**\: True
            
            .. attribute:: preferred_role
            
            	Set preferred role
            	**type**\:  :py:class:`SubscriberRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupRole>`
            
            .. attribute:: description
            
            	Description for this Group
            	**type**\: str
            
            .. attribute:: l2tp_source_ip_address
            
            	Enter an IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: slave_mode
            
            	Set Slave Mode
            	**type**\:  :py:class:`SubscriberRedundancyGroupSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupSlaveMode>`
            
            .. attribute:: hold_timer
            
            	Set hold time (in Minutes)
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: minute
            
            .. attribute:: access_tracking_object
            
            	Access Tracking Object for this Group
            	**type**\: str
            
            .. attribute:: enable_fast_switchover
            
            	Enable fast switchover for this Group
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redundancy_disable
            
            	Disable
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'subscriber-srg-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(SubscriberRedundancy.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_id']
                self._child_classes = OrderedDict([("interface-list", ("interface_list", SubscriberRedundancy.Groups.Group.InterfaceList)), ("peer", ("peer", SubscriberRedundancy.Groups.Group.Peer)), ("revertive-timer", ("revertive_timer", SubscriberRedundancy.Groups.Group.RevertiveTimer)), ("virtual-mac", ("virtual_mac", SubscriberRedundancy.Groups.Group.VirtualMac)), ("state-control-route", ("state_control_route", SubscriberRedundancy.Groups.Group.StateControlRoute))])
                self._leafs = OrderedDict([
                    ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ('disable_tracking_object', (YLeaf(YType.empty, 'disable-tracking-object'), ['Empty'])),
                    ('core_tracking_object', (YLeaf(YType.str, 'core-tracking-object'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('preferred_role', (YLeaf(YType.enumeration, 'preferred-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupRole', '')])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('l2tp_source_ip_address', (YLeaf(YType.str, 'l2tp-source-ip-address'), ['str'])),
                    ('slave_mode', (YLeaf(YType.enumeration, 'slave-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupSlaveMode', '')])),
                    ('hold_timer', (YLeaf(YType.uint32, 'hold-timer'), ['int'])),
                    ('access_tracking_object', (YLeaf(YType.str, 'access-tracking-object'), ['str'])),
                    ('enable_fast_switchover', (YLeaf(YType.empty, 'enable-fast-switchover'), ['Empty'])),
                    ('redundancy_disable', (YLeaf(YType.empty, 'redundancy-disable'), ['Empty'])),
                ])
                self.group_id = None
                self.disable_tracking_object = None
                self.core_tracking_object = None
                self.enable = None
                self.preferred_role = None
                self.description = None
                self.l2tp_source_ip_address = None
                self.slave_mode = None
                self.hold_timer = None
                self.access_tracking_object = None
                self.enable_fast_switchover = None
                self.redundancy_disable = None

                self.interface_list = None
                self._children_name_map["interface_list"] = "interface-list"

                self.peer = SubscriberRedundancy.Groups.Group.Peer()
                self.peer.parent = self
                self._children_name_map["peer"] = "peer"

                self.revertive_timer = SubscriberRedundancy.Groups.Group.RevertiveTimer()
                self.revertive_timer.parent = self
                self._children_name_map["revertive_timer"] = "revertive-timer"

                self.virtual_mac = SubscriberRedundancy.Groups.Group.VirtualMac()
                self.virtual_mac.parent = self
                self._children_name_map["virtual_mac"] = "virtual-mac"

                self.state_control_route = SubscriberRedundancy.Groups.Group.StateControlRoute()
                self.state_control_route.parent = self
                self._children_name_map["state_control_route"] = "state-control-route"
                self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberRedundancy.Groups.Group, ['group_id', 'disable_tracking_object', 'core_tracking_object', 'enable', 'preferred_role', 'description', 'l2tp_source_ip_address', 'slave_mode', 'hold_timer', 'access_tracking_object', 'enable_fast_switchover', 'redundancy_disable'], name, value)


            class InterfaceList(Entity):
                """
                List of Interfaces for this Group
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces>`
                
                .. attribute:: interface_ranges
                
                	Table of InterfaceRange
                	**type**\:  :py:class:`InterfaceRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges>`
                
                .. attribute:: enable
                
                	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList 
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.InterfaceList, self).__init__()

                    self.yang_name = "interface-list"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces)), ("interface-ranges", ("interface_ranges", SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.interfaces = SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"

                    self.interface_ranges = SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self._children_name_map["interface_ranges"] = "interface-ranges"
                    self._segment_path = lambda: "interface-list"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList, ['enable'], name, value)


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	Interface for this Group
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "interface-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: interface_id
                        
                        	Interface Id for the interface
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                            ])
                            self.interface_name = None
                            self.interface_id = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)


                class InterfaceRanges(Entity):
                    """
                    Table of InterfaceRange
                    
                    .. attribute:: interface_range
                    
                    	Interface for this Group
                    	**type**\: list of  		 :py:class:`InterfaceRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__init__()

                        self.yang_name = "interface-ranges"
                        self.yang_parent_name = "interface-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-range", ("interface_range", SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange))])
                        self._leafs = OrderedDict()

                        self.interface_range = YList(self)
                        self._segment_path = lambda: "interface-ranges"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges, [], name, value)


                    class InterfaceRange(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: sub_interface_range_start  (key)
                        
                        	Sub Interface Start Range
                        	**type**\: int
                        
                        	**range:** 0..2147483647
                        
                        .. attribute:: sub_interface_range_end  (key)
                        
                        	Sub Interface End Range
                        	**type**\: int
                        
                        	**range:** 0..2147483647
                        
                        .. attribute:: interface_id_range_start
                        
                        	Interface ID Start Range
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: interface_id_range_end
                        
                        	Interface ID End Range
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__init__()

                            self.yang_name = "interface-range"
                            self.yang_parent_name = "interface-ranges"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name','sub_interface_range_start','sub_interface_range_end']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('sub_interface_range_start', (YLeaf(YType.uint32, 'sub-interface-range-start'), ['int'])),
                                ('sub_interface_range_end', (YLeaf(YType.uint32, 'sub-interface-range-end'), ['int'])),
                                ('interface_id_range_start', (YLeaf(YType.uint32, 'interface-id-range-start'), ['int'])),
                                ('interface_id_range_end', (YLeaf(YType.uint32, 'interface-id-range-end'), ['int'])),
                            ])
                            self.interface_name = None
                            self.sub_interface_range_start = None
                            self.sub_interface_range_end = None
                            self.interface_id_range_start = None
                            self.interface_id_range_end = None
                            self._segment_path = lambda: "interface-range" + "[interface-name='" + str(self.interface_name) + "']" + "[sub-interface-range-start='" + str(self.sub_interface_range_start) + "']" + "[sub-interface-range-end='" + str(self.sub_interface_range_end) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, ['interface_name', 'sub_interface_range_start', 'sub_interface_range_end', 'interface_id_range_start', 'interface_id_range_end'], name, value)


            class Peer(Entity):
                """
                None
                
                .. attribute:: ipaddress
                
                	IPv4 or IPv6 Address of SRG Peer
                	**type**\:  :py:class:`Ipaddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.Peer.Ipaddress>`
                
                .. attribute:: route_add_disable
                
                	Set Route add disable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipaddress", ("ipaddress", SubscriberRedundancy.Groups.Group.Peer.Ipaddress))])
                    self._leafs = OrderedDict([
                        ('route_add_disable', (YLeaf(YType.empty, 'route-add-disable'), ['Empty'])),
                    ])
                    self.route_add_disable = None

                    self.ipaddress = SubscriberRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self
                    self._children_name_map["ipaddress"] = "ipaddress"
                    self._segment_path = lambda: "peer"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.Peer, ['route_add_disable'], name, value)


                class Ipaddress(Entity):
                    """
                    IPv4 or IPv6 Address of SRG Peer
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4/IPv6 address
                    	**type**\:  :py:class:`SrgAddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SrgAddrFamily>`
                    
                    .. attribute:: prefix_string
                    
                    	IPv4/IPv6 address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.Peer.Ipaddress, self).__init__()

                        self.yang_name = "ipaddress"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SrgAddrFamily', '')])),
                            ('prefix_string', (YLeaf(YType.str, 'prefix-string'), ['str','str'])),
                        ])
                        self.address_family = None
                        self.prefix_string = None
                        self._segment_path = lambda: "ipaddress"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.Peer.Ipaddress, ['address_family', 'prefix_string'], name, value)


            class RevertiveTimer(Entity):
                """
                None
                
                .. attribute:: max_value
                
                	Value of MAX Revertive Timer
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: value
                
                	Value of revertive time in minutes
                	**type**\: int
                
                	**range:** 1..65535
                
                	**units**\: minute
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.RevertiveTimer, self).__init__()

                    self.yang_name = "revertive-timer"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('max_value', (YLeaf(YType.uint32, 'max-value'), ['int'])),
                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                    ])
                    self.max_value = None
                    self.value = None
                    self._segment_path = lambda: "revertive-timer"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.RevertiveTimer, ['max_value', 'value'], name, value)


            class VirtualMac(Entity):
                """
                Virtual MAC Address for this Group
                
                .. attribute:: address
                
                	Virtual MAC Address for this Group
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: disable
                
                	Disable Virtual MAC Address for this Group
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.VirtualMac, self).__init__()

                    self.yang_name = "virtual-mac"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                    ])
                    self.address = None
                    self.disable = None
                    self._segment_path = lambda: "virtual-mac"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.VirtualMac, ['address', 'disable'], name, value)


            class StateControlRoute(Entity):
                """
                None
                
                .. attribute:: ipv4_routes
                
                	Table of IPv4Route
                	**type**\:  :py:class:`Ipv4Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes>`
                
                .. attribute:: ipv6_route
                
                	None
                	**type**\:  :py:class:`Ipv6Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberRedundancy.Groups.Group.StateControlRoute, self).__init__()

                    self.yang_name = "state-control-route"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv4-routes", ("ipv4_routes", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes)), ("ipv6-route", ("ipv6_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route))])
                    self._leafs = OrderedDict()

                    self.ipv4_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes()
                    self.ipv4_routes.parent = self
                    self._children_name_map["ipv4_routes"] = "ipv4-routes"

                    self.ipv6_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route()
                    self.ipv6_route.parent = self
                    self._children_name_map["ipv6_route"] = "ipv6-route"
                    self._segment_path = lambda: "state-control-route"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute, [], name, value)


                class Ipv4Routes(Entity):
                    """
                    Table of IPv4Route
                    
                    .. attribute:: ipv4_route
                    
                    	None
                    	**type**\: list of  		 :py:class:`Ipv4Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes, self).__init__()

                        self.yang_name = "ipv4-routes"
                        self.yang_parent_name = "state-control-route"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-route", ("ipv4_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route))])
                        self._leafs = OrderedDict()

                        self.ipv4_route = YList(self)
                        self._segment_path = lambda: "ipv4-routes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes, [], name, value)


                    class Ipv4Route(Entity):
                        """
                        None
                        
                        .. attribute:: vrfname  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: prefix_length  (key)
                        
                        	Prefix of the IP Address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prefix_string  (key)
                        
                        	IPv4 address with prefix\-length
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: tagvalue
                        
                        	Tag value
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route, self).__init__()

                            self.yang_name = "ipv4-route"
                            self.yang_parent_name = "ipv4-routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrfname','prefix_length','prefix_string']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrfname', (YLeaf(YType.str, 'vrfname'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('prefix_string', (YLeaf(YType.str, 'prefix-string'), ['str','str'])),
                                ('tagvalue', (YLeaf(YType.uint32, 'tagvalue'), ['int'])),
                            ])
                            self.vrfname = None
                            self.prefix_length = None
                            self.prefix_string = None
                            self.tagvalue = None
                            self._segment_path = lambda: "ipv4-route" + "[vrfname='" + str(self.vrfname) + "']" + "[prefix-length='" + str(self.prefix_length) + "']" + "[prefix-string='" + str(self.prefix_string) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Routes.Ipv4Route, ['vrfname', 'prefix_length', 'prefix_string', 'tagvalue'], name, value)


                class Ipv6Route(Entity):
                    """
                    None
                    
                    .. attribute:: ipv6na_routes
                    
                    	Table of IPv6NARoute
                    	**type**\:  :py:class:`Ipv6naRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes>`
                    
                    .. attribute:: ipv6pd_routes
                    
                    	Table of IPv6PDRoute
                    	**type**\:  :py:class:`Ipv6pdRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route, self).__init__()

                        self.yang_name = "ipv6-route"
                        self.yang_parent_name = "state-control-route"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv6na-routes", ("ipv6na_routes", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes)), ("ipv6pd-routes", ("ipv6pd_routes", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes))])
                        self._leafs = OrderedDict()

                        self.ipv6na_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes()
                        self.ipv6na_routes.parent = self
                        self._children_name_map["ipv6na_routes"] = "ipv6na-routes"

                        self.ipv6pd_routes = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes()
                        self.ipv6pd_routes.parent = self
                        self._children_name_map["ipv6pd_routes"] = "ipv6pd-routes"
                        self._segment_path = lambda: "ipv6-route"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route, [], name, value)


                    class Ipv6naRoutes(Entity):
                        """
                        Table of IPv6NARoute
                        
                        .. attribute:: ipv6na_route
                        
                        	None
                        	**type**\: list of  		 :py:class:`Ipv6naRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes.Ipv6naRoute>`
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes, self).__init__()

                            self.yang_name = "ipv6na-routes"
                            self.yang_parent_name = "ipv6-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv6na-route", ("ipv6na_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes.Ipv6naRoute))])
                            self._leafs = OrderedDict()

                            self.ipv6na_route = YList(self)
                            self._segment_path = lambda: "ipv6na-routes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes, [], name, value)


                        class Ipv6naRoute(Entity):
                            """
                            None
                            
                            .. attribute:: vrfname  (key)
                            
                            	VRF name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_string  (key)
                            
                            	IPv6 address with prefix\-length
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes.Ipv6naRoute, self).__init__()

                                self.yang_name = "ipv6na-route"
                                self.yang_parent_name = "ipv6na-routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vrfname','prefix_length','prefix_string']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('vrfname', (YLeaf(YType.str, 'vrfname'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                    ('prefix_string', (YLeaf(YType.str, 'prefix-string'), ['str','str'])),
                                    ('tagvalue', (YLeaf(YType.uint32, 'tagvalue'), ['int'])),
                                ])
                                self.vrfname = None
                                self.prefix_length = None
                                self.prefix_string = None
                                self.tagvalue = None
                                self._segment_path = lambda: "ipv6na-route" + "[vrfname='" + str(self.vrfname) + "']" + "[prefix-length='" + str(self.prefix_length) + "']" + "[prefix-string='" + str(self.prefix_string) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6naRoutes.Ipv6naRoute, ['vrfname', 'prefix_length', 'prefix_string', 'tagvalue'], name, value)


                    class Ipv6pdRoutes(Entity):
                        """
                        Table of IPv6PDRoute
                        
                        .. attribute:: ipv6pd_route
                        
                        	None
                        	**type**\: list of  		 :py:class:`Ipv6pdRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes.Ipv6pdRoute>`
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes, self).__init__()

                            self.yang_name = "ipv6pd-routes"
                            self.yang_parent_name = "ipv6-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv6pd-route", ("ipv6pd_route", SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes.Ipv6pdRoute))])
                            self._leafs = OrderedDict()

                            self.ipv6pd_route = YList(self)
                            self._segment_path = lambda: "ipv6pd-routes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes, [], name, value)


                        class Ipv6pdRoute(Entity):
                            """
                            None
                            
                            .. attribute:: vrfname  (key)
                            
                            	VRF name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Prefix of the IP Address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_string  (key)
                            
                            	IPv6 address with prefix\-length
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tagvalue
                            
                            	Tag value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'subscriber-srg-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes.Ipv6pdRoute, self).__init__()

                                self.yang_name = "ipv6pd-route"
                                self.yang_parent_name = "ipv6pd-routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vrfname','prefix_length','prefix_string']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('vrfname', (YLeaf(YType.str, 'vrfname'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                    ('prefix_string', (YLeaf(YType.str, 'prefix-string'), ['str','str'])),
                                    ('tagvalue', (YLeaf(YType.uint32, 'tagvalue'), ['int'])),
                                ])
                                self.vrfname = None
                                self.prefix_length = None
                                self.prefix_string = None
                                self.tagvalue = None
                                self._segment_path = lambda: "ipv6pd-route" + "[vrfname='" + str(self.vrfname) + "']" + "[prefix-length='" + str(self.prefix_length) + "']" + "[prefix-string='" + str(self.prefix_string) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6pdRoutes.Ipv6pdRoute, ['vrfname', 'prefix_length', 'prefix_string', 'tagvalue'], name, value)


    class RevertiveTimer(Entity):
        """
        None
        
        .. attribute:: max_value
        
        	Value of MAX Revertive Timer
        	**type**\: int
        
        	**range:** 1..65535
        
        .. attribute:: value
        
        	Value of revertive time in minutes
        	**type**\: int
        
        	**range:** 1..65535
        
        	**units**\: minute
        
        

        """

        _prefix = 'subscriber-srg-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(SubscriberRedundancy.RevertiveTimer, self).__init__()

            self.yang_name = "revertive-timer"
            self.yang_parent_name = "subscriber-redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('max_value', (YLeaf(YType.uint32, 'max-value'), ['int'])),
                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
            ])
            self.max_value = None
            self.value = None
            self._segment_path = lambda: "revertive-timer"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancy.RevertiveTimer, ['max_value', 'value'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberRedundancy()
        return self._top_entity

