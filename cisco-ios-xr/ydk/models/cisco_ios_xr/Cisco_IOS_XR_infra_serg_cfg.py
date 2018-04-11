""" Cisco_IOS_XR_infra_serg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package configuration.

This module contains definitions
for the following management objects\:
  session\-redundancy\: Session Redundancy configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SergAddrFamily(Enum):
    """
    SergAddrFamily (Enum Class)

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
    SessionRedundancyGroupRole (Enum Class)

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
    
    .. attribute:: groups
    
    	Table of Group
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups>`
    
    .. attribute:: revertive_timer
    
    	None
    	**type**\:  :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.RevertiveTimer>`
    
    .. attribute:: redundancy_disable
    
    	Disable
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable Session Redundancy configuration. Deletion of this object also causes deletion of all associated objects under SessionRedundancy
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: source_interface
    
    	Source Interface for Redundancy Peer Communication
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
    .. attribute:: preferred_role
    
    	Set preferred role
    	**type**\:  :py:class:`SessionRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancyGroupRole>`
    
    .. attribute:: hold_timer
    
    	Set hold time (in Minutes)
    	**type**\: int
    
    	**range:** 1..65535
    
    	**units**\: minute
    
    

    """

    _prefix = 'infra-serg-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionRedundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("groups", ("groups", SessionRedundancy.Groups)), ("revertive-timer", ("revertive_timer", SessionRedundancy.RevertiveTimer))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('redundancy_disable', YLeaf(YType.empty, 'redundancy-disable')),
            ('enable', YLeaf(YType.empty, 'enable')),
            ('source_interface', YLeaf(YType.str, 'source-interface')),
            ('preferred_role', YLeaf(YType.enumeration, 'preferred-role')),
            ('hold_timer', YLeaf(YType.uint32, 'hold-timer')),
        ])
        self.redundancy_disable = None
        self.enable = None
        self.source_interface = None
        self.preferred_role = None
        self.hold_timer = None

        self.groups = SessionRedundancy.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.revertive_timer = SessionRedundancy.RevertiveTimer()
        self.revertive_timer.parent = self
        self._children_name_map["revertive_timer"] = "revertive-timer"
        self._children_yang_names.add("revertive-timer")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-serg-cfg:session-redundancy"

    def __setattr__(self, name, value):
        self._perform_setattr(SessionRedundancy, ['redundancy_disable', 'enable', 'source_interface', 'preferred_role', 'hold_timer'], name, value)


    class Groups(Entity):
        """
        Table of Group
        
        .. attribute:: group
        
        	Redundancy Group configuration
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancy.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "session-redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("group", ("group", SessionRedundancy.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-cfg:session-redundancy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancy.Groups, [], name, value)


        class Group(Entity):
            """
            Redundancy Group configuration
            
            .. attribute:: group_id  (key)
            
            	Group ID
            	**type**\: int
            
            	**range:** 1..500
            
            .. attribute:: peer
            
            	None
            	**type**\:  :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.Peer>`
            
            .. attribute:: revertive_timer
            
            	None
            	**type**\:  :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.RevertiveTimer>`
            
            .. attribute:: interface_list
            
            	List of Interfaces for this Group
            	**type**\:  :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList>`
            
            .. attribute:: core_tracking_object
            
            	Core Tracking Object for this Group
            	**type**\: str
            
            .. attribute:: disable_tracking_object
            
            	Disable Tracking Object for this Group
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redundancy_disable
            
            	Disable
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable Redundancy Group configuration. Deletion of this object also causes deletion of all associated objects under Group
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: description
            
            	Description for this Group
            	**type**\: str
            
            .. attribute:: access_tracking_object
            
            	Access Tracking Object for this Group
            	**type**\: str
            
            .. attribute:: preferred_role
            
            	Set preferred role
            	**type**\:  :py:class:`SessionRedundancyGroupRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancyGroupRole>`
            
            .. attribute:: hold_timer
            
            	Set hold time (in Minutes)
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: minute
            
            

            """

            _prefix = 'infra-serg-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancy.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_id']
                self._child_container_classes = OrderedDict([("peer", ("peer", SessionRedundancy.Groups.Group.Peer)), ("revertive-timer", ("revertive_timer", SessionRedundancy.Groups.Group.RevertiveTimer)), ("interface-list", ("interface_list", SessionRedundancy.Groups.Group.InterfaceList))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('group_id', YLeaf(YType.uint32, 'group-id')),
                    ('core_tracking_object', YLeaf(YType.str, 'core-tracking-object')),
                    ('disable_tracking_object', YLeaf(YType.empty, 'disable-tracking-object')),
                    ('redundancy_disable', YLeaf(YType.empty, 'redundancy-disable')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                    ('description', YLeaf(YType.str, 'description')),
                    ('access_tracking_object', YLeaf(YType.str, 'access-tracking-object')),
                    ('preferred_role', YLeaf(YType.enumeration, 'preferred-role')),
                    ('hold_timer', YLeaf(YType.uint32, 'hold-timer')),
                ])
                self.group_id = None
                self.core_tracking_object = None
                self.disable_tracking_object = None
                self.redundancy_disable = None
                self.enable = None
                self.description = None
                self.access_tracking_object = None
                self.preferred_role = None
                self.hold_timer = None

                self.peer = SessionRedundancy.Groups.Group.Peer()
                self.peer.parent = self
                self._children_name_map["peer"] = "peer"
                self._children_yang_names.add("peer")

                self.revertive_timer = SessionRedundancy.Groups.Group.RevertiveTimer()
                self.revertive_timer.parent = self
                self._children_name_map["revertive_timer"] = "revertive-timer"
                self._children_yang_names.add("revertive-timer")

                self.interface_list = SessionRedundancy.Groups.Group.InterfaceList()
                self.interface_list.parent = self
                self._children_name_map["interface_list"] = "interface-list"
                self._children_yang_names.add("interface-list")
                self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-cfg:session-redundancy/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SessionRedundancy.Groups.Group, ['group_id', 'core_tracking_object', 'disable_tracking_object', 'redundancy_disable', 'enable', 'description', 'access_tracking_object', 'preferred_role', 'hold_timer'], name, value)


            class Peer(Entity):
                """
                None
                
                .. attribute:: ipaddress
                
                	IPv4 or IPv6 Address of SERG Peer
                	**type**\:  :py:class:`Ipaddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.Peer.Ipaddress>`
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancy.Groups.Group.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("ipaddress", ("ipaddress", SessionRedundancy.Groups.Group.Peer.Ipaddress))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.ipaddress = SessionRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self
                    self._children_name_map["ipaddress"] = "ipaddress"
                    self._children_yang_names.add("ipaddress")
                    self._segment_path = lambda: "peer"


                class Ipaddress(Entity):
                    """
                    IPv4 or IPv6 Address of SERG Peer
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4/IPv6 address
                    	**type**\:  :py:class:`SergAddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SergAddrFamily>`
                    
                    .. attribute:: prefix_string
                    
                    	IPv4/IPv6 address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancy.Groups.Group.Peer.Ipaddress, self).__init__()

                        self.yang_name = "ipaddress"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address_family', YLeaf(YType.enumeration, 'address-family')),
                            ('prefix_string', YLeaf(YType.str, 'prefix-string')),
                        ])
                        self.address_family = None
                        self.prefix_string = None
                        self._segment_path = lambda: "ipaddress"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancy.Groups.Group.Peer.Ipaddress, ['address_family', 'prefix_string'], name, value)


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

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancy.Groups.Group.RevertiveTimer, self).__init__()

                    self.yang_name = "revertive-timer"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('max_value', YLeaf(YType.uint32, 'max-value')),
                        ('value', YLeaf(YType.uint32, 'value')),
                    ])
                    self.max_value = None
                    self.value = None
                    self._segment_path = lambda: "revertive-timer"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancy.Groups.Group.RevertiveTimer, ['max_value', 'value'], name, value)


            class InterfaceList(Entity):
                """
                List of Interfaces for this Group
                
                .. attribute:: interface_ranges
                
                	Table of InterfaceRange
                	**type**\:  :py:class:`InterfaceRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges>`
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.Interfaces>`
                
                .. attribute:: enable
                
                	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList 
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancy.Groups.Group.InterfaceList, self).__init__()

                    self.yang_name = "interface-list"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("interface-ranges", ("interface_ranges", SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges)), ("interfaces", ("interfaces", SessionRedundancy.Groups.Group.InterfaceList.Interfaces))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.enable = None

                    self.interface_ranges = SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self._children_name_map["interface_ranges"] = "interface-ranges"
                    self._children_yang_names.add("interface-ranges")

                    self.interfaces = SessionRedundancy.Groups.Group.InterfaceList.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")
                    self._segment_path = lambda: "interface-list"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancy.Groups.Group.InterfaceList, ['enable'], name, value)


                class InterfaceRanges(Entity):
                    """
                    Table of InterfaceRange
                    
                    .. attribute:: interface_range
                    
                    	Interface for this Group
                    	**type**\: list of  		 :py:class:`InterfaceRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange>`
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges, self).__init__()

                        self.yang_name = "interface-ranges"
                        self.yang_parent_name = "interface-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface-range", ("interface_range", SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange))])
                        self._leafs = OrderedDict()

                        self.interface_range = YList(self)
                        self._segment_path = lambda: "interface-ranges"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges, [], name, value)


                    class InterfaceRange(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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

                        _prefix = 'infra-serg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, self).__init__()

                            self.yang_name = "interface-range"
                            self.yang_parent_name = "interface-ranges"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name','sub_interface_range_start','sub_interface_range_end']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('sub_interface_range_start', YLeaf(YType.uint32, 'sub-interface-range-start')),
                                ('sub_interface_range_end', YLeaf(YType.uint32, 'sub-interface-range-end')),
                                ('interface_id_range_start', YLeaf(YType.uint32, 'interface-id-range-start')),
                                ('interface_id_range_end', YLeaf(YType.uint32, 'interface-id-range-end')),
                            ])
                            self.interface_name = None
                            self.sub_interface_range_start = None
                            self.sub_interface_range_end = None
                            self.interface_id_range_start = None
                            self.interface_id_range_end = None
                            self._segment_path = lambda: "interface-range" + "[interface-name='" + str(self.interface_name) + "']" + "[sub-interface-range-start='" + str(self.sub_interface_range_start) + "']" + "[sub-interface-range-end='" + str(self.sub_interface_range_end) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange, ['interface_name', 'sub_interface_range_start', 'sub_interface_range_end', 'interface_id_range_start', 'interface_id_range_end'], name, value)


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	Interface for this Group
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "interface-list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface", ("interface", SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancy.Groups.Group.InterfaceList.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_id
                        
                        	Interface Id for the interface
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'infra-serg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('interface_id', YLeaf(YType.uint32, 'interface-id')),
                            ])
                            self.interface_name = None
                            self.interface_id = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)


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

        _prefix = 'infra-serg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancy.RevertiveTimer, self).__init__()

            self.yang_name = "revertive-timer"
            self.yang_parent_name = "session-redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('max_value', YLeaf(YType.uint32, 'max-value')),
                ('value', YLeaf(YType.uint32, 'value')),
            ])
            self.max_value = None
            self.value = None
            self._segment_path = lambda: "revertive-timer"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-cfg:session-redundancy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancy.RevertiveTimer, ['max_value', 'value'], name, value)

    def clone_ptr(self):
        self._top_entity = SessionRedundancy()
        return self._top_entity

