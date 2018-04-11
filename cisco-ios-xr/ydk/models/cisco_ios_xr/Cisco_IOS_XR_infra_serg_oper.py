""" Cisco_IOS_XR_infra_serg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package operational data.

This module contains definitions
for the following management objects\:
  session\-redundancy\-manager\: Session Redundancy Manager
    information
  session\-redundancy\-agent\: session redundancy agent

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SergPeerStatus(Enum):
    """
    SergPeerStatus (Enum Class)

    SERG Peer Status

    .. data:: not_configured = 0

    	Peer not configured

    .. data:: initialize = 1

    	Peer initialization

    .. data:: retry = 2

    	Peer retry pending

    .. data:: connect = 3

    	Connection in Progress

    .. data:: listen = 4

    	Listening in Progress

    .. data:: registration = 5

    	Awaiting Registration from Peer

    .. data:: cleanup = 6

    	Peer cleanup in progress

    .. data:: connected = 7

    	Peer Connected

    .. data:: established = 8

    	Peer Established

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    initialize = Enum.YLeaf(1, "initialize")

    retry = Enum.YLeaf(2, "retry")

    connect = Enum.YLeaf(3, "connect")

    listen = Enum.YLeaf(4, "listen")

    registration = Enum.YLeaf(5, "registration")

    cleanup = Enum.YLeaf(6, "cleanup")

    connected = Enum.YLeaf(7, "connected")

    established = Enum.YLeaf(8, "established")


class SergShowComp(Enum):
    """
    SergShowComp (Enum Class)

    SERG Components

    .. data:: serga = 0

    	SERG Agent

    .. data:: ipv6nd = 1

    	IPv6ND

    .. data:: dhcpv6 = 2

    	DHCPv6

    """

    serga = Enum.YLeaf(0, "serga")

    ipv6nd = Enum.YLeaf(1, "ipv6nd")

    dhcpv6 = Enum.YLeaf(2, "dhcpv6")


class SergShowImRole(Enum):
    """
    SergShowImRole (Enum Class)

    SERG Interface Management Role

    .. data:: none = 0

    	Not Determined

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class SergShowMem(Enum):
    """
    SergShowMem (Enum Class)

    SERG Memory Manager type

    .. data:: standard = 0

    	Standard type

    .. data:: chunk = 1

    	Chunk type

    .. data:: edm = 2

    	EDM type

    .. data:: string = 3

    	String type

    .. data:: static = 4

    	Static type

    .. data:: unknown = 5

    	Unknown type

    """

    standard = Enum.YLeaf(0, "standard")

    chunk = Enum.YLeaf(1, "chunk")

    edm = Enum.YLeaf(2, "edm")

    string = Enum.YLeaf(3, "string")

    static = Enum.YLeaf(4, "static")

    unknown = Enum.YLeaf(5, "unknown")


class SergShowRole(Enum):
    """
    SergShowRole (Enum Class)

    SERG Role

    .. data:: none = 0

    	Not Configured

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class SergShowSessionError(Enum):
    """
    SergShowSessionError (Enum Class)

    SERG Session Error Operation

    .. data:: none = 0

    	Invalid Error

    .. data:: hard = 1

    	Hard Error

    .. data:: soft = 2

    	Soft Error

    """

    none = Enum.YLeaf(0, "none")

    hard = Enum.YLeaf(1, "hard")

    soft = Enum.YLeaf(2, "soft")


class SergShowSessionOperation(Enum):
    """
    SergShowSessionOperation (Enum Class)

    SERG Session Operation

    .. data:: none = 0

    	No Operation

    .. data:: update = 1

    	SERG Session Update Operation

    .. data:: delete = 2

    	SERG Session Delete Operation

    .. data:: in_sync = 3

    	SERG Session In Sync

    """

    none = Enum.YLeaf(0, "none")

    update = Enum.YLeaf(1, "update")

    delete = Enum.YLeaf(2, "delete")

    in_sync = Enum.YLeaf(3, "in-sync")


class SergShowSlaveMode(Enum):
    """
    SergShowSlaveMode (Enum Class)

    SERG Slave Mode

    .. data:: none = 0

    	Not Configured

    .. data:: warm = 1

    	Warm Modem

    .. data:: hot = 2

    	Hot Mode

    """

    none = Enum.YLeaf(0, "none")

    warm = Enum.YLeaf(1, "warm")

    hot = Enum.YLeaf(2, "hot")


class SergShowSoReason(Enum):
    """
    SergShowSoReason (Enum Class)

    Session Redundancy Switchover Reason

    .. data:: internal = 0

    	SwitchOver for Internal Reason

    .. data:: admin = 1

    	SwitchOver for Admin

    .. data:: peer_up = 2

    	SwitchOver for Peer UP

    .. data:: peer_down = 3

    	SwitchOver for Peer Down

    .. data:: object_tracking_status_change = 4

    	SwitchOver for Object Tracking status change

    .. data:: serg_show_so_reason_max = 5

    	Unknown Switchover Reason

    """

    internal = Enum.YLeaf(0, "internal")

    admin = Enum.YLeaf(1, "admin")

    peer_up = Enum.YLeaf(2, "peer-up")

    peer_down = Enum.YLeaf(3, "peer-down")

    object_tracking_status_change = Enum.YLeaf(4, "object-tracking-status-change")

    serg_show_so_reason_max = Enum.YLeaf(5, "serg-show-so-reason-max")



class SessionRedundancyManager(Entity):
    """
    Session Redundancy Manager information
    
    .. attribute:: interfaces
    
    	Subscriber Redundancy Manager interface table
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces>`
    
    .. attribute:: groups
    
    	Session Redundancy Manager group table
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups>`
    
    .. attribute:: summary
    
    	Session redundancy manager summary
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Summary>`
    
    

    """

    _prefix = 'infra-serg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionRedundancyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("interfaces", ("interfaces", SessionRedundancyManager.Interfaces)), ("groups", ("groups", SessionRedundancyManager.Groups)), ("summary", ("summary", SessionRedundancyManager.Summary))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.interfaces = SessionRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.groups = SessionRedundancyManager.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.summary = SessionRedundancyManager.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager"


    class Interfaces(Entity):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	interface redundancy manager interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyManager.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "session-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("interface", ("interface", SessionRedundancyManager.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancyManager.Interfaces, [], name, value)


        class Interface(Entity):
            """
            interface redundancy manager interface
            
            .. attribute:: interface  (key)
            
            	Interface
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\: str
            
            .. attribute:: interface_mapping_id
            
            	Interface Mapping ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: forward_referenced
            
            	Forward Referenced
            	**type**\: bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: role
            
            	SERG Role
            	**type**\:  :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancyManager.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', YLeaf(YType.str, 'interface')),
                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                    ('interface_mapping_id', YLeaf(YType.uint32, 'interface-mapping-id')),
                    ('forward_referenced', YLeaf(YType.boolean, 'forward-referenced')),
                    ('group_id', YLeaf(YType.uint32, 'group-id')),
                    ('role', YLeaf(YType.enumeration, 'role')),
                ])
                self.interface = None
                self.interface_name = None
                self.interface_mapping_id = None
                self.forward_referenced = None
                self.group_id = None
                self.role = None
                self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SessionRedundancyManager.Interfaces.Interface, ['interface', 'interface_name', 'interface_mapping_id', 'forward_referenced', 'group_id', 'role'], name, value)


    class Groups(Entity):
        """
        Session Redundancy Manager group table
        
        .. attribute:: group
        
        	Session redundancy manager group
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyManager.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "session-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("group", ("group", SessionRedundancyManager.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancyManager.Groups, [], name, value)


        class Group(Entity):
            """
            Session redundancy manager group
            
            .. attribute:: group  (key)
            
            	Group
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: description
            
            	Group Description
            	**type**\: str
            
            .. attribute:: disabled
            
            	Disabled by Config
            	**type**\: bool
            
            .. attribute:: role
            
            	SERG Role
            	**type**\:  :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
            
            .. attribute:: peer_ipv4_address
            
            	Peer IPv4 Address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_ipv6_address
            
            	Peer IPv6 Address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interface_count
            
            	Interface Count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: preferred_role
            
            	Preferred Role
            	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
            
            .. attribute:: slave_mode
            
            	Slave Mode
            	**type**\:  :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
            
            .. attribute:: object_tracking_status
            
            	Object Tracking Status (Enabled/Disabled)
            	**type**\: bool
            
            .. attribute:: node_name
            
            	Node Information
            	**type**\: str
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancyManager.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('group', YLeaf(YType.str, 'group')),
                    ('group_id', YLeaf(YType.uint32, 'group-id')),
                    ('description', YLeaf(YType.str, 'description')),
                    ('disabled', YLeaf(YType.boolean, 'disabled')),
                    ('role', YLeaf(YType.enumeration, 'role')),
                    ('peer_ipv4_address', YLeaf(YType.str, 'peer-ipv4-address')),
                    ('peer_ipv6_address', YLeaf(YType.str, 'peer-ipv6-address')),
                    ('interface_count', YLeaf(YType.uint32, 'interface-count')),
                    ('preferred_role', YLeaf(YType.enumeration, 'preferred-role')),
                    ('slave_mode', YLeaf(YType.enumeration, 'slave-mode')),
                    ('object_tracking_status', YLeaf(YType.boolean, 'object-tracking-status')),
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.group = None
                self.group_id = None
                self.description = None
                self.disabled = None
                self.role = None
                self.peer_ipv4_address = None
                self.peer_ipv6_address = None
                self.interface_count = None
                self.preferred_role = None
                self.slave_mode = None
                self.object_tracking_status = None
                self.node_name = None
                self._segment_path = lambda: "group" + "[group='" + str(self.group) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SessionRedundancyManager.Groups.Group, ['group', 'group_id', 'description', 'disabled', 'role', 'peer_ipv4_address', 'peer_ipv6_address', 'interface_count', 'preferred_role', 'slave_mode', 'object_tracking_status', 'node_name'], name, value)


    class Summary(Entity):
        """
        Session redundancy manager summary
        
        .. attribute:: disabled
        
        	Disabled by Config
        	**type**\: bool
        
        .. attribute:: active_state
        
        	Process Active State
        	**type**\: bool
        
        .. attribute:: preferred_role
        
        	Preferred Role
        	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
        
        .. attribute:: slave_mode
        
        	Slave Mode
        	**type**\:  :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
        
        .. attribute:: hold_timer
        
        	Switch Over Hold Time
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: source_interface_name
        
        	Source Interface Name
        	**type**\: str
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\: str
        
        .. attribute:: source_interface_ipv4_address
        
        	Source Interface IPv4 Address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_ipv6_address
        
        	Source Interface IPv6 Address
        	**type**\: str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: group_count
        
        	No. of Configured Groups
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: disabled_group_count
        
        	No. of Disabled Groups by Config
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_group_count
        
        	No. of Master/Active Groups
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_group_count
        
        	No. of Slave Groups
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_count
        
        	No. of Configured Interfaces
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_interface_count
        
        	No. of Master/Active Interfaces
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_interface_count
        
        	No. of Slave Interfaces
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyManager.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "session-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('disabled', YLeaf(YType.boolean, 'disabled')),
                ('active_state', YLeaf(YType.boolean, 'active-state')),
                ('preferred_role', YLeaf(YType.enumeration, 'preferred-role')),
                ('slave_mode', YLeaf(YType.enumeration, 'slave-mode')),
                ('hold_timer', YLeaf(YType.uint32, 'hold-timer')),
                ('source_interface_name', YLeaf(YType.str, 'source-interface-name')),
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('source_interface_ipv4_address', YLeaf(YType.str, 'source-interface-ipv4-address')),
                ('source_interface_ipv6_address', YLeaf(YType.str, 'source-interface-ipv6-address')),
                ('group_count', YLeaf(YType.uint32, 'group-count')),
                ('disabled_group_count', YLeaf(YType.uint32, 'disabled-group-count')),
                ('master_group_count', YLeaf(YType.uint32, 'master-group-count')),
                ('slave_group_count', YLeaf(YType.uint32, 'slave-group-count')),
                ('interface_count', YLeaf(YType.uint32, 'interface-count')),
                ('master_interface_count', YLeaf(YType.uint32, 'master-interface-count')),
                ('slave_interface_count', YLeaf(YType.uint32, 'slave-interface-count')),
            ])
            self.disabled = None
            self.active_state = None
            self.preferred_role = None
            self.slave_mode = None
            self.hold_timer = None
            self.source_interface_name = None
            self.vrf_name = None
            self.source_interface_ipv4_address = None
            self.source_interface_ipv6_address = None
            self.group_count = None
            self.disabled_group_count = None
            self.master_group_count = None
            self.slave_group_count = None
            self.interface_count = None
            self.master_interface_count = None
            self.slave_interface_count = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancyManager.Summary, ['disabled', 'active_state', 'preferred_role', 'slave_mode', 'hold_timer', 'source_interface_name', 'vrf_name', 'source_interface_ipv4_address', 'source_interface_ipv6_address', 'group_count', 'disabled_group_count', 'master_group_count', 'slave_group_count', 'interface_count', 'master_interface_count', 'slave_interface_count'], name, value)

    def clone_ptr(self):
        self._top_entity = SessionRedundancyManager()
        return self._top_entity

class SessionRedundancyAgent(Entity):
    """
    session redundancy agent
    
    .. attribute:: nodes
    
    	List of nodes for which session data is collected
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes>`
    
    

    """

    _prefix = 'infra-serg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionRedundancyAgent, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy-agent"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", SessionRedundancyAgent.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = SessionRedundancyAgent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent"


    class Nodes(Entity):
        """
        List of nodes for which session data is
        collected
        
        .. attribute:: node
        
        	Session data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyAgent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "session-redundancy-agent"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", SessionRedundancyAgent.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancyAgent.Nodes, [], name, value)


        class Node(Entity):
            """
            Session data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: group_id_xr
            
            	Data for particular subscriber group session
            	**type**\:  :py:class:`GroupIdXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr>`
            
            .. attribute:: client_ids
            
            	Stats Client
            	**type**\:  :py:class:`ClientIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds>`
            
            .. attribute:: memory
            
            	Show Memory
            	**type**\:  :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory>`
            
            .. attribute:: group_ids
            
            	Data for particular subscriber group 
            	**type**\:  :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds>`
            
            .. attribute:: interfaces
            
            	List of interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces>`
            
            .. attribute:: stats_global
            
            	Stats Global
            	**type**\:  :py:class:`StatsGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal>`
            
            .. attribute:: group_summaries
            
            	Session data for a particular node
            	**type**\:  :py:class:`GroupSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancyAgent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("group-id-xr", ("group_id_xr", SessionRedundancyAgent.Nodes.Node.GroupIdXr)), ("client-ids", ("client_ids", SessionRedundancyAgent.Nodes.Node.ClientIds)), ("memory", ("memory", SessionRedundancyAgent.Nodes.Node.Memory)), ("group-ids", ("group_ids", SessionRedundancyAgent.Nodes.Node.GroupIds)), ("interfaces", ("interfaces", SessionRedundancyAgent.Nodes.Node.Interfaces)), ("stats-global", ("stats_global", SessionRedundancyAgent.Nodes.Node.StatsGlobal)), ("group-summaries", ("group_summaries", SessionRedundancyAgent.Nodes.Node.GroupSummaries))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.group_id_xr = SessionRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self._children_name_map["group_id_xr"] = "group-id-xr"
                self._children_yang_names.add("group-id-xr")

                self.client_ids = SessionRedundancyAgent.Nodes.Node.ClientIds()
                self.client_ids.parent = self
                self._children_name_map["client_ids"] = "client-ids"
                self._children_yang_names.add("client-ids")

                self.memory = SessionRedundancyAgent.Nodes.Node.Memory()
                self.memory.parent = self
                self._children_name_map["memory"] = "memory"
                self._children_yang_names.add("memory")

                self.group_ids = SessionRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self._children_name_map["group_ids"] = "group-ids"
                self._children_yang_names.add("group-ids")

                self.interfaces = SessionRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.stats_global = SessionRedundancyAgent.Nodes.Node.StatsGlobal()
                self.stats_global.parent = self
                self._children_name_map["stats_global"] = "stats-global"
                self._children_yang_names.add("stats-global")

                self.group_summaries = SessionRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self._children_name_map["group_summaries"] = "group-summaries"
                self._children_yang_names.add("group-summaries")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SessionRedundancyAgent.Nodes.Node, ['node_name'], name, value)


            class GroupIdXr(Entity):
                """
                Data for particular subscriber group session
                
                .. attribute:: group_id
                
                	Group id for subscriber group session
                	**type**\: list of  		 :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupIdXr, self).__init__()

                    self.yang_name = "group-id-xr"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("group-id", ("group_id", SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId))])
                    self._leafs = OrderedDict()

                    self.group_id = YList(self)
                    self._segment_path = lambda: "group-id-xr"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr, [], name, value)


                class GroupId(Entity):
                    """
                    Group id for subscriber group session
                    
                    .. attribute:: group_id  (key)
                    
                    	GroupId
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    .. attribute:: key_index
                    
                    	Key index
                    	**type**\: str
                    
                    .. attribute:: role_master
                    
                    	Master Role is Set
                    	**type**\: bool
                    
                    .. attribute:: negative_acknowledgement_update_all
                    
                    	Negative Acknowledgement Update Flag is Set
                    	**type**\: bool
                    
                    .. attribute:: session_detailed_information
                    
                    	More Session Information
                    	**type**\: list of  		 :py:class:`SessionDetailedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation>`
                    
                    .. attribute:: session_sync_error_information
                    
                    	Session Synchroniation Error Information
                    	**type**\: list of  		 :py:class:`SessionSyncErrorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-id-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("session-detailed-information", ("session_detailed_information", SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation)), ("session-sync-error-information", ("session_sync_error_information", SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation))])
                        self._leafs = OrderedDict([
                            ('group_id', YLeaf(YType.str, 'group-id')),
                            ('group_id_xr', YLeaf(YType.uint32, 'group-id-xr')),
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('key_index', YLeaf(YType.str, 'key-index')),
                            ('role_master', YLeaf(YType.boolean, 'role-master')),
                            ('negative_acknowledgement_update_all', YLeaf(YType.boolean, 'negative-acknowledgement-update-all')),
                        ])
                        self.group_id = None
                        self.group_id_xr = None
                        self.interface_name = None
                        self.key_index = None
                        self.role_master = None
                        self.negative_acknowledgement_update_all = None

                        self.session_detailed_information = YList(self)
                        self.session_sync_error_information = YList(self)
                        self._segment_path = lambda: "group-id" + "[group-id='" + str(self.group_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, ['group_id', 'group_id_xr', 'interface_name', 'key_index', 'role_master', 'negative_acknowledgement_update_all'], name, value)


                    class SessionDetailedInformation(Entity):
                        """
                        More Session Information
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:  :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                        
                        .. attribute:: operation_
                        
                        	Operation Code
                        	**type**\:  :py:class:`SergShowSessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSessionOperation>`
                        
                        .. attribute:: tx_list_queue_fail
                        
                        	Tx List Queue Failed
                        	**type**\: bool
                        
                        .. attribute:: marked_for_sweeping
                        
                        	Marked For Sweeping
                        	**type**\: bool
                        
                        .. attribute:: marked_for_cleanup
                        
                        	Marked For Cleanup
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__init__()

                            self.yang_name = "session-detailed-information"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('component', YLeaf(YType.enumeration, 'component')),
                                ('operation_', YLeaf(YType.enumeration, 'operation')),
                                ('tx_list_queue_fail', YLeaf(YType.boolean, 'tx-list-queue-fail')),
                                ('marked_for_sweeping', YLeaf(YType.boolean, 'marked-for-sweeping')),
                                ('marked_for_cleanup', YLeaf(YType.boolean, 'marked-for-cleanup')),
                            ])
                            self.component = None
                            self.operation_ = None
                            self.tx_list_queue_fail = None
                            self.marked_for_sweeping = None
                            self.marked_for_cleanup = None
                            self._segment_path = lambda: "session-detailed-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, ['component', 'operation_', 'tx_list_queue_fail', 'marked_for_sweeping', 'marked_for_cleanup'], name, value)


                    class SessionSyncErrorInformation(Entity):
                        """
                        Session Synchroniation Error Information
                        
                        .. attribute:: sync_error_count
                        
                        	No. of Errors occured during Synchronization
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: last_error_code
                        
                        	Last Error Code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_error_type
                        
                        	Last Error Type
                        	**type**\:  :py:class:`SergShowSessionError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSessionError>`
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__init__()

                            self.yang_name = "session-sync-error-information"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sync_error_count', YLeaf(YType.uint16, 'sync-error-count')),
                                ('last_error_code', YLeaf(YType.uint32, 'last-error-code')),
                                ('last_error_type', YLeaf(YType.enumeration, 'last-error-type')),
                            ])
                            self.sync_error_count = None
                            self.last_error_code = None
                            self.last_error_type = None
                            self._segment_path = lambda: "session-sync-error-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, ['sync_error_count', 'last_error_code', 'last_error_type'], name, value)


            class ClientIds(Entity):
                """
                Stats Client
                
                .. attribute:: client_id
                
                	Specify stats client
                	**type**\: list of  		 :py:class:`ClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.ClientIds, self).__init__()

                    self.yang_name = "client-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("client-id", ("client_id", SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId))])
                    self._leafs = OrderedDict()

                    self.client_id = YList(self)
                    self._segment_path = lambda: "client-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.ClientIds, [], name, value)


                class ClientId(Entity):
                    """
                    Specify stats client
                    
                    .. attribute:: stats_client_id  (key)
                    
                    	Client Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tx_list_start_of_download_add_ok
                    
                    	TxListStartOfDownloadAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_start_of_download_add_not_ok
                    
                    	TxListStartOfDownloadAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_download_add_ok
                    
                    	TxListEndOfDownloadAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_download_add_not_ok
                    
                    	TxListEndOfDownloadAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_message_add_ok
                    
                    	TxListEndOfMessageAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_message_add_not_ok
                    
                    	TxListEndOfMessageAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_all_add_ok
                    
                    	TxListClearAllAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_all_add_not_ok
                    
                    	TxListClearAllAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_selected_add_ok
                    
                    	TxListClearSelectedAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_selected_add_not_ok
                    
                    	TxListClearSelectedAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_all_add_ok
                    
                    	TxListReplayAllAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_all_add_not_ok
                    
                    	TxListReplayAllAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_selected_add_ok
                    
                    	TxListReplaySelectedAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_selected_add_not_ok
                    
                    	TxListReplaySelectedAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_add_ok
                    
                    	TxListSessionSessionAddOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_add_not_ok
                    
                    	TxListSessionSessionAddNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_update_ok
                    
                    	TxListSessionSessionUpdateOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_update_not_ok
                    
                    	TxListSessionSessionUpdateNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_delete
                    
                    	TxListSessionSessionDelete
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: clean_call_back
                    
                    	CleanCallBack
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_session_session_ok
                    
                    	TxListEncodeSessionSessionOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_session_session_partial_write
                    
                    	TxListEncodeSessionSessionPartialWrite
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_replay_all_count
                    
                    	LastReplayAllCount
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_command_replay_all
                    
                    	TxListReceiveCommandReplayAll
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_command_replay_selected
                    
                    	TxListReceiveCommandReplaySelected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_delete_valid
                    
                    	TxListReceiveSessionSessionDeleteValid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_delete_invalid
                    
                    	TxListReceiveSessionSessionDeleteInValid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_update_valid
                    
                    	TxListReceiveSessionSessionUpdateValid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_update_invalid
                    
                    	TxListReceiveSessionSessionUpdateInValid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_sod_all
                    
                    	TxListReceiveSessionSessionSODAll
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_sod_selected
                    
                    	TxListReceiveSessionSessionSODSelected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eod_all
                    
                    	TxListReceiveSessionSessionEODAll
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eod_selected
                    
                    	TxListReceiveSessionSessionEODSelected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eoms
                    
                    	TxListReceiveSessionSessionEOMS
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_clear_all
                    
                    	TxListReceiveSessionSessionClearAll
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_clear_selected
                    
                    	TxListReceiveSessionSessionClearSelected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_neg_ack
                    
                    	TxListReceiveSessionSessionNegAck
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_neg_ack_not_ok
                    
                    	TxListReceiveSessionSessionNegAckNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_registration_ok
                    
                    	TxListClientRegistrationOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_registration_not_ok
                    
                    	TxListClientRegistrationNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_de_registration
                    
                    	TxListClientDeRegistration
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_connection_down
                    
                    	TxListClientConnectionDown
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_cleanup
                    
                    	TxListClientCleanup
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_active_ok
                    
                    	TxListActiveOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_active_not_ok
                    
                    	TxListActiveNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_de_active_ok
                    
                    	TxListDeActiveOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_de_active_not_ok
                    
                    	TxListDeActiveNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, self).__init__()

                        self.yang_name = "client-id"
                        self.yang_parent_name = "client-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['stats_client_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('stats_client_id', YLeaf(YType.int32, 'stats-client-id')),
                            ('tx_list_start_of_download_add_ok', YLeaf(YType.uint32, 'tx-list-start-of-download-add-ok')),
                            ('tx_list_start_of_download_add_not_ok', YLeaf(YType.uint32, 'tx-list-start-of-download-add-not-ok')),
                            ('tx_list_end_of_download_add_ok', YLeaf(YType.uint32, 'tx-list-end-of-download-add-ok')),
                            ('tx_list_end_of_download_add_not_ok', YLeaf(YType.uint32, 'tx-list-end-of-download-add-not-ok')),
                            ('tx_list_end_of_message_add_ok', YLeaf(YType.uint32, 'tx-list-end-of-message-add-ok')),
                            ('tx_list_end_of_message_add_not_ok', YLeaf(YType.uint32, 'tx-list-end-of-message-add-not-ok')),
                            ('tx_list_clear_all_add_ok', YLeaf(YType.uint32, 'tx-list-clear-all-add-ok')),
                            ('tx_list_clear_all_add_not_ok', YLeaf(YType.uint32, 'tx-list-clear-all-add-not-ok')),
                            ('tx_list_clear_selected_add_ok', YLeaf(YType.uint32, 'tx-list-clear-selected-add-ok')),
                            ('tx_list_clear_selected_add_not_ok', YLeaf(YType.uint32, 'tx-list-clear-selected-add-not-ok')),
                            ('tx_list_replay_all_add_ok', YLeaf(YType.uint32, 'tx-list-replay-all-add-ok')),
                            ('tx_list_replay_all_add_not_ok', YLeaf(YType.uint32, 'tx-list-replay-all-add-not-ok')),
                            ('tx_list_replay_selected_add_ok', YLeaf(YType.uint32, 'tx-list-replay-selected-add-ok')),
                            ('tx_list_replay_selected_add_not_ok', YLeaf(YType.uint32, 'tx-list-replay-selected-add-not-ok')),
                            ('tx_list_session_session_add_ok', YLeaf(YType.uint32, 'tx-list-session-session-add-ok')),
                            ('tx_list_session_session_add_not_ok', YLeaf(YType.uint32, 'tx-list-session-session-add-not-ok')),
                            ('tx_list_session_session_update_ok', YLeaf(YType.uint32, 'tx-list-session-session-update-ok')),
                            ('tx_list_session_session_update_not_ok', YLeaf(YType.uint32, 'tx-list-session-session-update-not-ok')),
                            ('tx_list_session_session_delete', YLeaf(YType.uint32, 'tx-list-session-session-delete')),
                            ('clean_call_back', YLeaf(YType.uint32, 'clean-call-back')),
                            ('tx_list_encode_session_session_ok', YLeaf(YType.uint32, 'tx-list-encode-session-session-ok')),
                            ('tx_list_encode_session_session_partial_write', YLeaf(YType.uint32, 'tx-list-encode-session-session-partial-write')),
                            ('last_replay_all_count', YLeaf(YType.uint32, 'last-replay-all-count')),
                            ('tx_list_receive_command_replay_all', YLeaf(YType.uint32, 'tx-list-receive-command-replay-all')),
                            ('tx_list_receive_command_replay_selected', YLeaf(YType.uint32, 'tx-list-receive-command-replay-selected')),
                            ('tx_list_receive_session_session_delete_valid', YLeaf(YType.uint32, 'tx-list-receive-session-session-delete-valid')),
                            ('tx_list_receive_session_session_delete_invalid', YLeaf(YType.uint32, 'tx-list-receive-session-session-delete-invalid')),
                            ('tx_list_receive_session_session_update_valid', YLeaf(YType.uint32, 'tx-list-receive-session-session-update-valid')),
                            ('tx_list_receive_session_session_update_invalid', YLeaf(YType.uint32, 'tx-list-receive-session-session-update-invalid')),
                            ('tx_list_receive_session_session_sod_all', YLeaf(YType.uint32, 'tx-list-receive-session-session-sod-all')),
                            ('tx_list_receive_session_session_sod_selected', YLeaf(YType.uint32, 'tx-list-receive-session-session-sod-selected')),
                            ('tx_list_receive_session_session_eod_all', YLeaf(YType.uint32, 'tx-list-receive-session-session-eod-all')),
                            ('tx_list_receive_session_session_eod_selected', YLeaf(YType.uint32, 'tx-list-receive-session-session-eod-selected')),
                            ('tx_list_receive_session_session_eoms', YLeaf(YType.uint32, 'tx-list-receive-session-session-eoms')),
                            ('tx_list_receive_session_session_clear_all', YLeaf(YType.uint32, 'tx-list-receive-session-session-clear-all')),
                            ('tx_list_receive_session_session_clear_selected', YLeaf(YType.uint32, 'tx-list-receive-session-session-clear-selected')),
                            ('tx_list_receive_session_session_neg_ack', YLeaf(YType.uint32, 'tx-list-receive-session-session-neg-ack')),
                            ('tx_list_receive_session_session_neg_ack_not_ok', YLeaf(YType.uint32, 'tx-list-receive-session-session-neg-ack-not-ok')),
                            ('tx_list_client_registration_ok', YLeaf(YType.uint32, 'tx-list-client-registration-ok')),
                            ('tx_list_client_registration_not_ok', YLeaf(YType.uint32, 'tx-list-client-registration-not-ok')),
                            ('tx_list_client_de_registration', YLeaf(YType.uint32, 'tx-list-client-de-registration')),
                            ('tx_list_client_connection_down', YLeaf(YType.uint32, 'tx-list-client-connection-down')),
                            ('tx_list_client_cleanup', YLeaf(YType.uint32, 'tx-list-client-cleanup')),
                            ('tx_list_active_ok', YLeaf(YType.uint32, 'tx-list-active-ok')),
                            ('tx_list_active_not_ok', YLeaf(YType.uint32, 'tx-list-active-not-ok')),
                            ('tx_list_de_active_ok', YLeaf(YType.uint32, 'tx-list-de-active-ok')),
                            ('tx_list_de_active_not_ok', YLeaf(YType.uint32, 'tx-list-de-active-not-ok')),
                        ])
                        self.stats_client_id = None
                        self.tx_list_start_of_download_add_ok = None
                        self.tx_list_start_of_download_add_not_ok = None
                        self.tx_list_end_of_download_add_ok = None
                        self.tx_list_end_of_download_add_not_ok = None
                        self.tx_list_end_of_message_add_ok = None
                        self.tx_list_end_of_message_add_not_ok = None
                        self.tx_list_clear_all_add_ok = None
                        self.tx_list_clear_all_add_not_ok = None
                        self.tx_list_clear_selected_add_ok = None
                        self.tx_list_clear_selected_add_not_ok = None
                        self.tx_list_replay_all_add_ok = None
                        self.tx_list_replay_all_add_not_ok = None
                        self.tx_list_replay_selected_add_ok = None
                        self.tx_list_replay_selected_add_not_ok = None
                        self.tx_list_session_session_add_ok = None
                        self.tx_list_session_session_add_not_ok = None
                        self.tx_list_session_session_update_ok = None
                        self.tx_list_session_session_update_not_ok = None
                        self.tx_list_session_session_delete = None
                        self.clean_call_back = None
                        self.tx_list_encode_session_session_ok = None
                        self.tx_list_encode_session_session_partial_write = None
                        self.last_replay_all_count = None
                        self.tx_list_receive_command_replay_all = None
                        self.tx_list_receive_command_replay_selected = None
                        self.tx_list_receive_session_session_delete_valid = None
                        self.tx_list_receive_session_session_delete_invalid = None
                        self.tx_list_receive_session_session_update_valid = None
                        self.tx_list_receive_session_session_update_invalid = None
                        self.tx_list_receive_session_session_sod_all = None
                        self.tx_list_receive_session_session_sod_selected = None
                        self.tx_list_receive_session_session_eod_all = None
                        self.tx_list_receive_session_session_eod_selected = None
                        self.tx_list_receive_session_session_eoms = None
                        self.tx_list_receive_session_session_clear_all = None
                        self.tx_list_receive_session_session_clear_selected = None
                        self.tx_list_receive_session_session_neg_ack = None
                        self.tx_list_receive_session_session_neg_ack_not_ok = None
                        self.tx_list_client_registration_ok = None
                        self.tx_list_client_registration_not_ok = None
                        self.tx_list_client_de_registration = None
                        self.tx_list_client_connection_down = None
                        self.tx_list_client_cleanup = None
                        self.tx_list_active_ok = None
                        self.tx_list_active_not_ok = None
                        self.tx_list_de_active_ok = None
                        self.tx_list_de_active_not_ok = None
                        self._segment_path = lambda: "client-id" + "[stats-client-id='" + str(self.stats_client_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, ['stats_client_id', 'tx_list_start_of_download_add_ok', 'tx_list_start_of_download_add_not_ok', 'tx_list_end_of_download_add_ok', 'tx_list_end_of_download_add_not_ok', 'tx_list_end_of_message_add_ok', 'tx_list_end_of_message_add_not_ok', 'tx_list_clear_all_add_ok', 'tx_list_clear_all_add_not_ok', 'tx_list_clear_selected_add_ok', 'tx_list_clear_selected_add_not_ok', 'tx_list_replay_all_add_ok', 'tx_list_replay_all_add_not_ok', 'tx_list_replay_selected_add_ok', 'tx_list_replay_selected_add_not_ok', 'tx_list_session_session_add_ok', 'tx_list_session_session_add_not_ok', 'tx_list_session_session_update_ok', 'tx_list_session_session_update_not_ok', 'tx_list_session_session_delete', 'clean_call_back', 'tx_list_encode_session_session_ok', 'tx_list_encode_session_session_partial_write', 'last_replay_all_count', 'tx_list_receive_command_replay_all', 'tx_list_receive_command_replay_selected', 'tx_list_receive_session_session_delete_valid', 'tx_list_receive_session_session_delete_invalid', 'tx_list_receive_session_session_update_valid', 'tx_list_receive_session_session_update_invalid', 'tx_list_receive_session_session_sod_all', 'tx_list_receive_session_session_sod_selected', 'tx_list_receive_session_session_eod_all', 'tx_list_receive_session_session_eod_selected', 'tx_list_receive_session_session_eoms', 'tx_list_receive_session_session_clear_all', 'tx_list_receive_session_session_clear_selected', 'tx_list_receive_session_session_neg_ack', 'tx_list_receive_session_session_neg_ack_not_ok', 'tx_list_client_registration_ok', 'tx_list_client_registration_not_ok', 'tx_list_client_de_registration', 'tx_list_client_connection_down', 'tx_list_client_cleanup', 'tx_list_active_ok', 'tx_list_active_not_ok', 'tx_list_de_active_ok', 'tx_list_de_active_not_ok'], name, value)


            class Memory(Entity):
                """
                Show Memory
                
                .. attribute:: memory_info
                
                	Memory Info
                	**type**\: list of  		 :py:class:`MemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo>`
                
                .. attribute:: edm_memory_info
                
                	EDM Memory Info
                	**type**\: list of  		 :py:class:`EdmMemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo>`
                
                .. attribute:: string_memory_info
                
                	String Memory Info
                	**type**\: list of  		 :py:class:`StringMemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.Memory, self).__init__()

                    self.yang_name = "memory"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("memory-info", ("memory_info", SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo)), ("edm-memory-info", ("edm_memory_info", SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo)), ("string-memory-info", ("string_memory_info", SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo))])
                    self._leafs = OrderedDict()

                    self.memory_info = YList(self)
                    self.edm_memory_info = YList(self)
                    self.string_memory_info = YList(self)
                    self._segment_path = lambda: "memory"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory, [], name, value)


                class MemoryInfo(Entity):
                    """
                    Memory Info
                    
                    .. attribute:: structure_name
                    
                    	Structure Name
                    	**type**\: str
                    
                    .. attribute:: size
                    
                    	Size of the datastructure
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_count
                    
                    	Current Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: alloc_fails
                    
                    	Allocation Fails
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: alloc_count
                    
                    	Allocated count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: freed_count
                    
                    	Freed Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: memory_type
                    
                    	Memory Type
                    	**type**\:  :py:class:`SergShowMem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowMem>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, self).__init__()

                        self.yang_name = "memory-info"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('structure_name', YLeaf(YType.str, 'structure-name')),
                            ('size', YLeaf(YType.uint32, 'size')),
                            ('current_count', YLeaf(YType.uint32, 'current-count')),
                            ('alloc_fails', YLeaf(YType.uint32, 'alloc-fails')),
                            ('alloc_count', YLeaf(YType.uint32, 'alloc-count')),
                            ('freed_count', YLeaf(YType.uint32, 'freed-count')),
                            ('memory_type', YLeaf(YType.enumeration, 'memory-type')),
                        ])
                        self.structure_name = None
                        self.size = None
                        self.current_count = None
                        self.alloc_fails = None
                        self.alloc_count = None
                        self.freed_count = None
                        self.memory_type = None
                        self._segment_path = lambda: "memory-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, ['structure_name', 'size', 'current_count', 'alloc_fails', 'alloc_count', 'freed_count', 'memory_type'], name, value)


                class EdmMemoryInfo(Entity):
                    """
                    EDM Memory Info
                    
                    .. attribute:: size
                    
                    	Size of the block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total request
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Cache\-hit success
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failure
                    
                    	Cache\-hit failure
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, self).__init__()

                        self.yang_name = "edm-memory-info"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('size', YLeaf(YType.uint32, 'size')),
                            ('total', YLeaf(YType.uint32, 'total')),
                            ('success', YLeaf(YType.uint32, 'success')),
                            ('failure', YLeaf(YType.uint32, 'failure')),
                        ])
                        self.size = None
                        self.total = None
                        self.success = None
                        self.failure = None
                        self._segment_path = lambda: "edm-memory-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, ['size', 'total', 'success', 'failure'], name, value)


                class StringMemoryInfo(Entity):
                    """
                    String Memory Info
                    
                    .. attribute:: size
                    
                    	Size of the block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total request
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Cache\-hit success
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failure
                    
                    	Cache\-hit failure
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, self).__init__()

                        self.yang_name = "string-memory-info"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('size', YLeaf(YType.uint32, 'size')),
                            ('total', YLeaf(YType.uint32, 'total')),
                            ('success', YLeaf(YType.uint32, 'success')),
                            ('failure', YLeaf(YType.uint32, 'failure')),
                        ])
                        self.size = None
                        self.total = None
                        self.success = None
                        self.failure = None
                        self._segment_path = lambda: "string-memory-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, ['size', 'total', 'success', 'failure'], name, value)


            class GroupIds(Entity):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of  		 :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupIds, self).__init__()

                    self.yang_name = "group-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("group-id", ("group_id", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId))])
                    self._leafs = OrderedDict()

                    self.group_id = YList(self)
                    self._segment_path = lambda: "group-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds, [], name, value)


                class GroupId(Entity):
                    """
                    Group id for subscriber group
                    
                    .. attribute:: group_id  (key)
                    
                    	Group Id
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: description
                    
                    	Group Description
                    	**type**\: str
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\: bool
                    
                    .. attribute:: init_role
                    
                    	Preferred Init Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: negotiating_role
                    
                    	Negotiating Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: current_role
                    
                    	Current Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:  :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
                    
                    .. attribute:: hold_timer
                    
                    	Switch Over Hold Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: core_tracking_object_name
                    
                    	Core Object Tracking Name
                    	**type**\: str
                    
                    .. attribute:: core_tracking_object_status
                    
                    	Core Object Tracking Status
                    	**type**\: bool
                    
                    .. attribute:: access_tracking_object_name
                    
                    	Access Object Tracking Name
                    	**type**\: str
                    
                    .. attribute:: access_tracking_object_status
                    
                    	Access Object Tracking Status
                    	**type**\: bool
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\: bool
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:  :py:class:`SergPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergPeerStatus>`
                    
                    .. attribute:: peer_last_negotiation_time
                    
                    	Last Negotiation time of Peer
                    	**type**\: str
                    
                    .. attribute:: peer_last_up_time
                    
                    	Last UP time of Peer
                    	**type**\: str
                    
                    .. attribute:: peer_last_down_time
                    
                    	Last Down time of Peer
                    	**type**\: str
                    
                    .. attribute:: peer_init_role
                    
                    	Peer Preferred Init Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: peer_negotiating_role
                    
                    	Peer Negotiating Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: peer_current_role
                    
                    	Peer Current Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: peer_object_tracking_status
                    
                    	Peer Object Tracking Status
                    	**type**\: bool
                    
                    .. attribute:: last_switchover_time
                    
                    	Last Switchover time
                    	**type**\: str
                    
                    .. attribute:: switchover_count
                    
                    	Switchover Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_switchover_reason
                    
                    	Last Switchover Reason
                    	**type**\:  :py:class:`SergShowSoReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSoReason>`
                    
                    .. attribute:: switchover_hold_time
                    
                    	Switchover Hold Time in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_update_failure_count
                    
                    	Slave Session update fail count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_session_update_count
                    
                    	Pending Session Update Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_session_delete_count
                    
                    	Pending Session Delete Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_count
                    
                    	No. of Configured Interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: revertive_timer
                    
                    	Revertive timer for SWO back
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_revert_time
                    
                    	Switchover Revert Time in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: client_session_count
                    
                    	Client Session Count
                    	**type**\: list of  		 :py:class:`ClientSessionCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("client-session-count", ("client_session_count", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount)), ("interface", ("interface", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface))])
                        self._leafs = OrderedDict([
                            ('group_id', YLeaf(YType.str, 'group-id')),
                            ('group_id_xr', YLeaf(YType.uint32, 'group-id-xr')),
                            ('description', YLeaf(YType.str, 'description')),
                            ('disabled', YLeaf(YType.boolean, 'disabled')),
                            ('init_role', YLeaf(YType.enumeration, 'init-role')),
                            ('negotiating_role', YLeaf(YType.enumeration, 'negotiating-role')),
                            ('current_role', YLeaf(YType.enumeration, 'current-role')),
                            ('slave_mode', YLeaf(YType.enumeration, 'slave-mode')),
                            ('hold_timer', YLeaf(YType.uint32, 'hold-timer')),
                            ('core_tracking_object_name', YLeaf(YType.str, 'core-tracking-object-name')),
                            ('core_tracking_object_status', YLeaf(YType.boolean, 'core-tracking-object-status')),
                            ('access_tracking_object_name', YLeaf(YType.str, 'access-tracking-object-name')),
                            ('access_tracking_object_status', YLeaf(YType.boolean, 'access-tracking-object-status')),
                            ('object_tracking_status', YLeaf(YType.boolean, 'object-tracking-status')),
                            ('peer_ipv4_address', YLeaf(YType.str, 'peer-ipv4-address')),
                            ('peer_ipv6_address', YLeaf(YType.str, 'peer-ipv6-address')),
                            ('peer_status', YLeaf(YType.enumeration, 'peer-status')),
                            ('peer_last_negotiation_time', YLeaf(YType.str, 'peer-last-negotiation-time')),
                            ('peer_last_up_time', YLeaf(YType.str, 'peer-last-up-time')),
                            ('peer_last_down_time', YLeaf(YType.str, 'peer-last-down-time')),
                            ('peer_init_role', YLeaf(YType.enumeration, 'peer-init-role')),
                            ('peer_negotiating_role', YLeaf(YType.enumeration, 'peer-negotiating-role')),
                            ('peer_current_role', YLeaf(YType.enumeration, 'peer-current-role')),
                            ('peer_object_tracking_status', YLeaf(YType.boolean, 'peer-object-tracking-status')),
                            ('last_switchover_time', YLeaf(YType.str, 'last-switchover-time')),
                            ('switchover_count', YLeaf(YType.uint32, 'switchover-count')),
                            ('last_switchover_reason', YLeaf(YType.enumeration, 'last-switchover-reason')),
                            ('switchover_hold_time', YLeaf(YType.uint32, 'switchover-hold-time')),
                            ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ('slave_update_failure_count', YLeaf(YType.uint32, 'slave-update-failure-count')),
                            ('pending_session_update_count', YLeaf(YType.uint32, 'pending-session-update-count')),
                            ('pending_session_delete_count', YLeaf(YType.uint32, 'pending-session-delete-count')),
                            ('interface_count', YLeaf(YType.uint32, 'interface-count')),
                            ('revertive_timer', YLeaf(YType.uint32, 'revertive-timer')),
                            ('switchover_revert_time', YLeaf(YType.uint32, 'switchover-revert-time')),
                        ])
                        self.group_id = None
                        self.group_id_xr = None
                        self.description = None
                        self.disabled = None
                        self.init_role = None
                        self.negotiating_role = None
                        self.current_role = None
                        self.slave_mode = None
                        self.hold_timer = None
                        self.core_tracking_object_name = None
                        self.core_tracking_object_status = None
                        self.access_tracking_object_name = None
                        self.access_tracking_object_status = None
                        self.object_tracking_status = None
                        self.peer_ipv4_address = None
                        self.peer_ipv6_address = None
                        self.peer_status = None
                        self.peer_last_negotiation_time = None
                        self.peer_last_up_time = None
                        self.peer_last_down_time = None
                        self.peer_init_role = None
                        self.peer_negotiating_role = None
                        self.peer_current_role = None
                        self.peer_object_tracking_status = None
                        self.last_switchover_time = None
                        self.switchover_count = None
                        self.last_switchover_reason = None
                        self.switchover_hold_time = None
                        self.session_count = None
                        self.slave_update_failure_count = None
                        self.pending_session_update_count = None
                        self.pending_session_delete_count = None
                        self.interface_count = None
                        self.revertive_timer = None
                        self.switchover_revert_time = None

                        self.client_session_count = YList(self)
                        self.interface = YList(self)
                        self._segment_path = lambda: "group-id" + "[group-id='" + str(self.group_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, ['group_id', 'group_id_xr', 'description', 'disabled', 'init_role', 'negotiating_role', 'current_role', 'slave_mode', 'hold_timer', 'core_tracking_object_name', 'core_tracking_object_status', 'access_tracking_object_name', 'access_tracking_object_status', 'object_tracking_status', 'peer_ipv4_address', 'peer_ipv6_address', 'peer_status', 'peer_last_negotiation_time', 'peer_last_up_time', 'peer_last_down_time', 'peer_init_role', 'peer_negotiating_role', 'peer_current_role', 'peer_object_tracking_status', 'last_switchover_time', 'switchover_count', 'last_switchover_reason', 'switchover_hold_time', 'session_count', 'slave_update_failure_count', 'pending_session_update_count', 'pending_session_delete_count', 'interface_count', 'revertive_timer', 'switchover_revert_time'], name, value)


                    class ClientSessionCount(Entity):
                        """
                        Client Session Count
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:  :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, self).__init__()

                            self.yang_name = "client-session-count"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('component', YLeaf(YType.enumeration, 'component')),
                                ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ])
                            self.component = None
                            self.session_count = None
                            self._segment_path = lambda: "client-session-count"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, ['component', 'session_count'], name, value)


                    class Interface(Entity):
                        """
                        Interface List
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        .. attribute:: interface_synchronization_id
                        
                        	Interface Synchronization ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: forward_referenced
                        
                        	Forward Referenced
                        	**type**\: bool
                        
                        .. attribute:: session_count
                        
                        	Session Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('interface_synchronization_id', YLeaf(YType.uint32, 'interface-synchronization-id')),
                                ('forward_referenced', YLeaf(YType.boolean, 'forward-referenced')),
                                ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ])
                            self.interface_name = None
                            self.interface_synchronization_id = None
                            self.forward_referenced = None
                            self.session_count = None
                            self._segment_path = lambda: "interface"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, ['interface_name', 'interface_synchronization_id', 'forward_referenced', 'session_count'], name, value)


            class Interfaces(Entity):
                """
                List of interfaces
                
                .. attribute:: interface
                
                	Specify interface name
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("interface", ("interface", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Specify interface name
                    
                    .. attribute:: interface  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface_oper
                    
                    	Interface Batch Operation
                    	**type**\:  :py:class:`InterfaceOper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper>`
                    
                    .. attribute:: interface_status
                    
                    	Interface Status
                    	**type**\:  :py:class:`InterfaceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus>`
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    .. attribute:: interface_synchronization_id
                    
                    	Interface Sync ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SERG Role
                    	**type**\:  :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
                    
                    .. attribute:: forward_referenced
                    
                    	Forward Referenced
                    	**type**\: bool
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_enable_error_count
                    
                    	Interface Enable Error Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_disable_error_count
                    
                    	Interface Disable Error Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_add_error_count
                    
                    	Interface Caps Add Error Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_remove_error_count
                    
                    	Interface Caps Remove Error Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_attribute_update_error_count
                    
                    	Interface Attribute Update Error Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: client_status
                    
                    	Interface status for each client
                    	**type**\: list of  		 :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_container_classes = OrderedDict([("interface-oper", ("interface_oper", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper)), ("interface-status", ("interface_status", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus))])
                        self._child_list_classes = OrderedDict([("client-status", ("client_status", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus))])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('interface_synchronization_id', YLeaf(YType.uint32, 'interface-synchronization-id')),
                            ('group_id', YLeaf(YType.uint32, 'group-id')),
                            ('role', YLeaf(YType.enumeration, 'role')),
                            ('forward_referenced', YLeaf(YType.boolean, 'forward-referenced')),
                            ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ('interface_enable_error_count', YLeaf(YType.uint32, 'interface-enable-error-count')),
                            ('interface_disable_error_count', YLeaf(YType.uint32, 'interface-disable-error-count')),
                            ('interface_caps_add_error_count', YLeaf(YType.uint32, 'interface-caps-add-error-count')),
                            ('interface_caps_remove_error_count', YLeaf(YType.uint32, 'interface-caps-remove-error-count')),
                            ('interface_attribute_update_error_count', YLeaf(YType.uint32, 'interface-attribute-update-error-count')),
                        ])
                        self.interface = None
                        self.interface_name = None
                        self.interface_synchronization_id = None
                        self.group_id = None
                        self.role = None
                        self.forward_referenced = None
                        self.session_count = None
                        self.interface_enable_error_count = None
                        self.interface_disable_error_count = None
                        self.interface_caps_add_error_count = None
                        self.interface_caps_remove_error_count = None
                        self.interface_attribute_update_error_count = None

                        self.interface_oper = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                        self.interface_oper.parent = self
                        self._children_name_map["interface_oper"] = "interface-oper"
                        self._children_yang_names.add("interface-oper")

                        self.interface_status = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
                        self.interface_status.parent = self
                        self._children_name_map["interface_status"] = "interface-status"
                        self._children_yang_names.add("interface-status")

                        self.client_status = YList(self)
                        self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, ['interface', 'interface_name', 'interface_synchronization_id', 'group_id', 'role', 'forward_referenced', 'session_count', 'interface_enable_error_count', 'interface_disable_error_count', 'interface_caps_add_error_count', 'interface_caps_remove_error_count', 'interface_attribute_update_error_count'], name, value)


                    class InterfaceOper(Entity):
                        """
                        Interface Batch Operation
                        
                        .. attribute:: idb_oper_reg_enable
                        
                        	Operational Registration Enabled
                        	**type**\: bool
                        
                        .. attribute:: idb_oper_reg_disable
                        
                        	Operational Registration Disabled
                        	**type**\: bool
                        
                        .. attribute:: idb_oper_caps_add
                        
                        	Operational Caps Add
                        	**type**\: bool
                        
                        .. attribute:: idb_oper_caps_remove
                        
                        	Operational Caps Remove
                        	**type**\: bool
                        
                        .. attribute:: idb_oper_attr_update
                        
                        	Operational Attribute Update
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__init__()

                            self.yang_name = "interface-oper"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('idb_oper_reg_enable', YLeaf(YType.boolean, 'idb-oper-reg-enable')),
                                ('idb_oper_reg_disable', YLeaf(YType.boolean, 'idb-oper-reg-disable')),
                                ('idb_oper_caps_add', YLeaf(YType.boolean, 'idb-oper-caps-add')),
                                ('idb_oper_caps_remove', YLeaf(YType.boolean, 'idb-oper-caps-remove')),
                                ('idb_oper_attr_update', YLeaf(YType.boolean, 'idb-oper-attr-update')),
                            ])
                            self.idb_oper_reg_enable = None
                            self.idb_oper_reg_disable = None
                            self.idb_oper_caps_add = None
                            self.idb_oper_caps_remove = None
                            self.idb_oper_attr_update = None
                            self._segment_path = lambda: "interface-oper"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, ['idb_oper_reg_enable', 'idb_oper_reg_disable', 'idb_oper_caps_add', 'idb_oper_caps_remove', 'idb_oper_attr_update'], name, value)


                    class InterfaceStatus(Entity):
                        """
                        Interface Status
                        
                        .. attribute:: idb_state_fwd_ref
                        
                        	Interface Forward Referenced
                        	**type**\: bool
                        
                        .. attribute:: idb_state_stale
                        
                        	Interface State Stale
                        	**type**\: bool
                        
                        .. attribute:: idb_state_registered
                        
                        	Interface State Registered
                        	**type**\: bool
                        
                        .. attribute:: idb_state_caps_added
                        
                        	Interface State Caps Added
                        	**type**\: bool
                        
                        .. attribute:: idb_state_owned_re_source
                        
                        	Interface State Owned Resource
                        	**type**\: bool
                        
                        .. attribute:: idb_client_eoms_pending
                        
                        	Interface Client EOMS Pending
                        	**type**\: bool
                        
                        .. attribute:: idb_state_p_end_caps_rem
                        
                        	Interface Caps Remove Pending
                        	**type**\: bool
                        
                        .. attribute:: idb_state_p_end_reg_disable
                        
                        	Interface Registration Disable Pending
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__init__()

                            self.yang_name = "interface-status"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('idb_state_fwd_ref', YLeaf(YType.boolean, 'idb-state-fwd-ref')),
                                ('idb_state_stale', YLeaf(YType.boolean, 'idb-state-stale')),
                                ('idb_state_registered', YLeaf(YType.boolean, 'idb-state-registered')),
                                ('idb_state_caps_added', YLeaf(YType.boolean, 'idb-state-caps-added')),
                                ('idb_state_owned_re_source', YLeaf(YType.boolean, 'idb-state-owned-re-source')),
                                ('idb_client_eoms_pending', YLeaf(YType.boolean, 'idb-client-eoms-pending')),
                                ('idb_state_p_end_caps_rem', YLeaf(YType.boolean, 'idb-state-p-end-caps-rem')),
                                ('idb_state_p_end_reg_disable', YLeaf(YType.boolean, 'idb-state-p-end-reg-disable')),
                            ])
                            self.idb_state_fwd_ref = None
                            self.idb_state_stale = None
                            self.idb_state_registered = None
                            self.idb_state_caps_added = None
                            self.idb_state_owned_re_source = None
                            self.idb_client_eoms_pending = None
                            self.idb_state_p_end_caps_rem = None
                            self.idb_state_p_end_reg_disable = None
                            self._segment_path = lambda: "interface-status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, ['idb_state_fwd_ref', 'idb_state_stale', 'idb_state_registered', 'idb_state_caps_added', 'idb_state_owned_re_source', 'idb_client_eoms_pending', 'idb_state_p_end_caps_rem', 'idb_state_p_end_reg_disable'], name, value)


                    class ClientStatus(Entity):
                        """
                        Interface status for each client
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:  :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                        
                        .. attribute:: serg_show_idb_client_eoms_pending
                        
                        	SERG SHOW IDB CLIENT EOMS PENDING
                        	**type**\: bool
                        
                        .. attribute:: serg_show_idb_client_sync_eod_pending
                        
                        	SERG SHOW IDB CLIENT SYNC EOD PENDING
                        	**type**\: bool
                        
                        .. attribute:: session_count
                        
                        	session count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__init__()

                            self.yang_name = "client-status"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('component', YLeaf(YType.enumeration, 'component')),
                                ('serg_show_idb_client_eoms_pending', YLeaf(YType.boolean, 'serg-show-idb-client-eoms-pending')),
                                ('serg_show_idb_client_sync_eod_pending', YLeaf(YType.boolean, 'serg-show-idb-client-sync-eod-pending')),
                                ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ])
                            self.component = None
                            self.serg_show_idb_client_eoms_pending = None
                            self.serg_show_idb_client_sync_eod_pending = None
                            self.session_count = None
                            self._segment_path = lambda: "client-status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, ['component', 'serg_show_idb_client_eoms_pending', 'serg_show_idb_client_sync_eod_pending', 'session_count'], name, value)


            class StatsGlobal(Entity):
                """
                Stats Global
                
                .. attribute:: intf_status_statistics
                
                	intf status statistics
                	**type**\:  :py:class:`IntfStatusStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics>`
                
                .. attribute:: tx_list_statistics
                
                	tx list statistics
                	**type**\:  :py:class:`TxListStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics>`
                
                .. attribute:: source_interface_name
                
                	Source Interface Name
                	**type**\: str
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\: str
                
                .. attribute:: source_interface_ipv4_address
                
                	Source Interface IPv4 Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_interface_ipv6_address
                
                	Source Interface IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: redundancy_role
                
                	Redundancy Role
                	**type**\: str
                
                .. attribute:: restart_client_sync_in_progress
                
                	Restart Client Sync In Progress Flag
                	**type**\: bool
                
                .. attribute:: client_init_sync_time_stamp
                
                	Synchronization TimeStamp
                	**type**\: str
                
                .. attribute:: restart_peer_sync_in_progress
                
                	Restart Peer Sync In Progress Flag
                	**type**\: bool
                
                .. attribute:: peer_init_sync_time_stamp
                
                	Synchronization TimeStamp
                	**type**\: str
                
                .. attribute:: sync_in_progress
                
                	Sync In Progress Flag
                	**type**\: bool
                
                .. attribute:: peer_action_timer
                
                	Value in Seconds to trigger the peer actions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retry_timer_remaining
                
                	Value in Seconds to trigger the retry
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: tx_list_client_registration_invalid
                
                	TxListClientRegistrationInvalid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_de_registration_invalid
                
                	TxListClientDeRegistrationInvalid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_connection_up
                
                	TxListClientConnectionUp
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_connection_down
                
                	TxListClientConnectionDown
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_peer_done
                
                	TxListClientPeerDone
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_message_call_back
                
                	TxListClientMessageCallBack
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_valid
                
                	TxListClientReceiveValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_invalid
                
                	TxListClientReceiveInValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_command_valid
                
                	TxListClientReceiveCommandValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_command_invalid
                
                	TxListClientReceiveCommandInValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_session_sessionvalid
                
                	TxListClientReceiveSessionSessionValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_session_session_invalid
                
                	TxListClientReceiveSessionSessionInValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_timer_handler
                
                	TxListPeerTimerHandler
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_registration_invalid
                
                	TxListPeerRegistrationInValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_de_registration_invalid
                
                	TxListPeerDeRegistrationInValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_message_call_back_valid
                
                	TxListPeerMessageCallBackValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_message_call_back_invalid
                
                	TxListPeerMessageCallBackInValid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_done
                
                	TxListPeerDone
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_cmd_connection_up_not_ok
                
                	TxListPeerCmdConnectionUpNotOk
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_cmd_connection_down_not_ok
                
                	TxListPeerCmdConnectionDownNotOk
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_session_connection_up_not_ok
                
                	TxListPeerSessionConnectionUpNotOk
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_session_connection_down_not_ok
                
                	TxListPeerSessionConnectionDownNotOk
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: client_status
                
                	Client Status
                	**type**\: list of  		 :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus>`
                
                .. attribute:: opaque_memory_status
                
                	Opaque memory Stats
                	**type**\: list of  		 :py:class:`OpaqueMemoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus>`
                
                .. attribute:: tx_list_over_tcp_status
                
                	TCP TxList Statistics
                	**type**\: list of  		 :py:class:`TxListOverTcpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal, self).__init__()

                    self.yang_name = "stats-global"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("intf-status-statistics", ("intf_status_statistics", SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics)), ("tx-list-statistics", ("tx_list_statistics", SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics))])
                    self._child_list_classes = OrderedDict([("client-status", ("client_status", SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus)), ("opaque-memory-status", ("opaque_memory_status", SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus)), ("tx-list-over-tcp-status", ("tx_list_over_tcp_status", SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus))])
                    self._leafs = OrderedDict([
                        ('source_interface_name', YLeaf(YType.str, 'source-interface-name')),
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('source_interface_ipv4_address', YLeaf(YType.str, 'source-interface-ipv4-address')),
                        ('source_interface_ipv6_address', YLeaf(YType.str, 'source-interface-ipv6-address')),
                        ('redundancy_role', YLeaf(YType.str, 'redundancy-role')),
                        ('restart_client_sync_in_progress', YLeaf(YType.boolean, 'restart-client-sync-in-progress')),
                        ('client_init_sync_time_stamp', YLeaf(YType.str, 'client-init-sync-time-stamp')),
                        ('restart_peer_sync_in_progress', YLeaf(YType.boolean, 'restart-peer-sync-in-progress')),
                        ('peer_init_sync_time_stamp', YLeaf(YType.str, 'peer-init-sync-time-stamp')),
                        ('sync_in_progress', YLeaf(YType.boolean, 'sync-in-progress')),
                        ('peer_action_timer', YLeaf(YType.uint32, 'peer-action-timer')),
                        ('retry_timer_remaining', YLeaf(YType.uint32, 'retry-timer-remaining')),
                        ('tx_list_client_registration_invalid', YLeaf(YType.uint32, 'tx-list-client-registration-invalid')),
                        ('tx_list_client_de_registration_invalid', YLeaf(YType.uint32, 'tx-list-client-de-registration-invalid')),
                        ('tx_list_client_connection_up', YLeaf(YType.uint32, 'tx-list-client-connection-up')),
                        ('tx_list_client_connection_down', YLeaf(YType.uint32, 'tx-list-client-connection-down')),
                        ('tx_list_client_peer_done', YLeaf(YType.uint32, 'tx-list-client-peer-done')),
                        ('tx_list_client_message_call_back', YLeaf(YType.uint32, 'tx-list-client-message-call-back')),
                        ('tx_list_client_receive_valid', YLeaf(YType.uint32, 'tx-list-client-receive-valid')),
                        ('tx_list_client_receive_invalid', YLeaf(YType.uint32, 'tx-list-client-receive-invalid')),
                        ('tx_list_client_receive_command_valid', YLeaf(YType.uint32, 'tx-list-client-receive-command-valid')),
                        ('tx_list_client_receive_command_invalid', YLeaf(YType.uint32, 'tx-list-client-receive-command-invalid')),
                        ('tx_list_client_receive_session_sessionvalid', YLeaf(YType.uint32, 'tx-list-client-receive-session-sessionvalid')),
                        ('tx_list_client_receive_session_session_invalid', YLeaf(YType.uint32, 'tx-list-client-receive-session-session-invalid')),
                        ('tx_list_peer_timer_handler', YLeaf(YType.uint32, 'tx-list-peer-timer-handler')),
                        ('tx_list_peer_registration_invalid', YLeaf(YType.uint32, 'tx-list-peer-registration-invalid')),
                        ('tx_list_peer_de_registration_invalid', YLeaf(YType.uint32, 'tx-list-peer-de-registration-invalid')),
                        ('tx_list_peer_message_call_back_valid', YLeaf(YType.uint32, 'tx-list-peer-message-call-back-valid')),
                        ('tx_list_peer_message_call_back_invalid', YLeaf(YType.uint32, 'tx-list-peer-message-call-back-invalid')),
                        ('tx_list_peer_done', YLeaf(YType.uint32, 'tx-list-peer-done')),
                        ('tx_list_peer_cmd_connection_up_not_ok', YLeaf(YType.uint32, 'tx-list-peer-cmd-connection-up-not-ok')),
                        ('tx_list_peer_cmd_connection_down_not_ok', YLeaf(YType.uint32, 'tx-list-peer-cmd-connection-down-not-ok')),
                        ('tx_list_peer_session_connection_up_not_ok', YLeaf(YType.uint32, 'tx-list-peer-session-connection-up-not-ok')),
                        ('tx_list_peer_session_connection_down_not_ok', YLeaf(YType.uint32, 'tx-list-peer-session-connection-down-not-ok')),
                    ])
                    self.source_interface_name = None
                    self.vrf_name = None
                    self.source_interface_ipv4_address = None
                    self.source_interface_ipv6_address = None
                    self.redundancy_role = None
                    self.restart_client_sync_in_progress = None
                    self.client_init_sync_time_stamp = None
                    self.restart_peer_sync_in_progress = None
                    self.peer_init_sync_time_stamp = None
                    self.sync_in_progress = None
                    self.peer_action_timer = None
                    self.retry_timer_remaining = None
                    self.tx_list_client_registration_invalid = None
                    self.tx_list_client_de_registration_invalid = None
                    self.tx_list_client_connection_up = None
                    self.tx_list_client_connection_down = None
                    self.tx_list_client_peer_done = None
                    self.tx_list_client_message_call_back = None
                    self.tx_list_client_receive_valid = None
                    self.tx_list_client_receive_invalid = None
                    self.tx_list_client_receive_command_valid = None
                    self.tx_list_client_receive_command_invalid = None
                    self.tx_list_client_receive_session_sessionvalid = None
                    self.tx_list_client_receive_session_session_invalid = None
                    self.tx_list_peer_timer_handler = None
                    self.tx_list_peer_registration_invalid = None
                    self.tx_list_peer_de_registration_invalid = None
                    self.tx_list_peer_message_call_back_valid = None
                    self.tx_list_peer_message_call_back_invalid = None
                    self.tx_list_peer_done = None
                    self.tx_list_peer_cmd_connection_up_not_ok = None
                    self.tx_list_peer_cmd_connection_down_not_ok = None
                    self.tx_list_peer_session_connection_up_not_ok = None
                    self.tx_list_peer_session_connection_down_not_ok = None

                    self.intf_status_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics()
                    self.intf_status_statistics.parent = self
                    self._children_name_map["intf_status_statistics"] = "intf-status-statistics"
                    self._children_yang_names.add("intf-status-statistics")

                    self.tx_list_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics()
                    self.tx_list_statistics.parent = self
                    self._children_name_map["tx_list_statistics"] = "tx-list-statistics"
                    self._children_yang_names.add("tx-list-statistics")

                    self.client_status = YList(self)
                    self.opaque_memory_status = YList(self)
                    self.tx_list_over_tcp_status = YList(self)
                    self._segment_path = lambda: "stats-global"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal, ['source_interface_name', 'vrf_name', 'source_interface_ipv4_address', 'source_interface_ipv6_address', 'redundancy_role', 'restart_client_sync_in_progress', 'client_init_sync_time_stamp', 'restart_peer_sync_in_progress', 'peer_init_sync_time_stamp', 'sync_in_progress', 'peer_action_timer', 'retry_timer_remaining', 'tx_list_client_registration_invalid', 'tx_list_client_de_registration_invalid', 'tx_list_client_connection_up', 'tx_list_client_connection_down', 'tx_list_client_peer_done', 'tx_list_client_message_call_back', 'tx_list_client_receive_valid', 'tx_list_client_receive_invalid', 'tx_list_client_receive_command_valid', 'tx_list_client_receive_command_invalid', 'tx_list_client_receive_session_sessionvalid', 'tx_list_client_receive_session_session_invalid', 'tx_list_peer_timer_handler', 'tx_list_peer_registration_invalid', 'tx_list_peer_de_registration_invalid', 'tx_list_peer_message_call_back_valid', 'tx_list_peer_message_call_back_invalid', 'tx_list_peer_done', 'tx_list_peer_cmd_connection_up_not_ok', 'tx_list_peer_cmd_connection_down_not_ok', 'tx_list_peer_session_connection_up_not_ok', 'tx_list_peer_session_connection_down_not_ok'], name, value)


                class IntfStatusStatistics(Entity):
                    """
                    intf status statistics
                    
                    .. attribute:: pend_caps_rem_cnt
                    
                    	No. of interfaces pending caps remove
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_reg_disable_cnt
                    
                    	No. of interfaces pending red disable
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_other_batch_oper_cnt
                    
                    	No. of interfaces pending for other (except unreg/caps rem) batch oper
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: non_stale_cnt
                    
                    	No. of non stale interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: grp_bound_cnt
                    
                    	No. of interface bound to a group
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, self).__init__()

                        self.yang_name = "intf-status-statistics"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pend_caps_rem_cnt', YLeaf(YType.uint32, 'pend-caps-rem-cnt')),
                            ('pend_reg_disable_cnt', YLeaf(YType.uint32, 'pend-reg-disable-cnt')),
                            ('pend_other_batch_oper_cnt', YLeaf(YType.uint32, 'pend-other-batch-oper-cnt')),
                            ('non_stale_cnt', YLeaf(YType.uint32, 'non-stale-cnt')),
                            ('grp_bound_cnt', YLeaf(YType.uint32, 'grp-bound-cnt')),
                        ])
                        self.pend_caps_rem_cnt = None
                        self.pend_reg_disable_cnt = None
                        self.pend_other_batch_oper_cnt = None
                        self.non_stale_cnt = None
                        self.grp_bound_cnt = None
                        self._segment_path = lambda: "intf-status-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, ['pend_caps_rem_cnt', 'pend_reg_disable_cnt', 'pend_other_batch_oper_cnt', 'non_stale_cnt', 'grp_bound_cnt'], name, value)


                class TxListStatistics(Entity):
                    """
                    tx list statistics
                    
                    .. attribute:: tx_list_encode_marker_ok
                    
                    	TxListEncodeMarkerOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_marker_partial_write
                    
                    	TxListEncodeMarkerPartialWrite
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_marker
                    
                    	TxListCleanMarker
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_command_ok
                    
                    	TxListEncodeCommandOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_command_partial_write
                    
                    	TxListEncodeCommandPartialWrite
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_command
                    
                    	TxListCleanCommand
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_negotiation_ok
                    
                    	TxListEncodeNegotiationOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_negotiation_partial_write
                    
                    	TxListEncodeNegotiationPartialWrite
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_negotiation
                    
                    	TxListCleanNegotiation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, self).__init__()

                        self.yang_name = "tx-list-statistics"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tx_list_encode_marker_ok', YLeaf(YType.uint32, 'tx-list-encode-marker-ok')),
                            ('tx_list_encode_marker_partial_write', YLeaf(YType.uint32, 'tx-list-encode-marker-partial-write')),
                            ('tx_list_clean_marker', YLeaf(YType.uint32, 'tx-list-clean-marker')),
                            ('tx_list_encode_command_ok', YLeaf(YType.uint32, 'tx-list-encode-command-ok')),
                            ('tx_list_encode_command_partial_write', YLeaf(YType.uint32, 'tx-list-encode-command-partial-write')),
                            ('tx_list_clean_command', YLeaf(YType.uint32, 'tx-list-clean-command')),
                            ('tx_list_encode_negotiation_ok', YLeaf(YType.uint32, 'tx-list-encode-negotiation-ok')),
                            ('tx_list_encode_negotiation_partial_write', YLeaf(YType.uint32, 'tx-list-encode-negotiation-partial-write')),
                            ('tx_list_clean_negotiation', YLeaf(YType.uint32, 'tx-list-clean-negotiation')),
                        ])
                        self.tx_list_encode_marker_ok = None
                        self.tx_list_encode_marker_partial_write = None
                        self.tx_list_clean_marker = None
                        self.tx_list_encode_command_ok = None
                        self.tx_list_encode_command_partial_write = None
                        self.tx_list_clean_command = None
                        self.tx_list_encode_negotiation_ok = None
                        self.tx_list_encode_negotiation_partial_write = None
                        self.tx_list_clean_negotiation = None
                        self._segment_path = lambda: "tx-list-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, ['tx_list_encode_marker_ok', 'tx_list_encode_marker_partial_write', 'tx_list_clean_marker', 'tx_list_encode_command_ok', 'tx_list_encode_command_partial_write', 'tx_list_clean_command', 'tx_list_encode_negotiation_ok', 'tx_list_encode_negotiation_partial_write', 'tx_list_clean_negotiation'], name, value)


                class ClientStatus(Entity):
                    """
                    Client Status
                    
                    .. attribute:: component
                    
                    	Component
                    	**type**\:  :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                    
                    .. attribute:: client_connection_status
                    
                    	ClientConnectionStatus
                    	**type**\: bool
                    
                    .. attribute:: client_initialization_synchronization_pending
                    
                    	ClientInitializationSynchronizationPending
                    	**type**\: bool
                    
                    .. attribute:: client_synchronization_end_of_download_pending
                    
                    	ClientSynchronizationEndOfDownloadPending
                    	**type**\: bool
                    
                    .. attribute:: up_time_stamp
                    
                    	UpTimeStamp
                    	**type**\: str
                    
                    .. attribute:: down_time_stamp
                    
                    	DownTimeStamp
                    	**type**\: str
                    
                    .. attribute:: clean_up_timer_remaining
                    
                    	Value in Seconds to trigger the client cleanup
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, self).__init__()

                        self.yang_name = "client-status"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('component', YLeaf(YType.enumeration, 'component')),
                            ('client_connection_status', YLeaf(YType.boolean, 'client-connection-status')),
                            ('client_initialization_synchronization_pending', YLeaf(YType.boolean, 'client-initialization-synchronization-pending')),
                            ('client_synchronization_end_of_download_pending', YLeaf(YType.boolean, 'client-synchronization-end-of-download-pending')),
                            ('up_time_stamp', YLeaf(YType.str, 'up-time-stamp')),
                            ('down_time_stamp', YLeaf(YType.str, 'down-time-stamp')),
                            ('clean_up_timer_remaining', YLeaf(YType.uint32, 'clean-up-timer-remaining')),
                        ])
                        self.component = None
                        self.client_connection_status = None
                        self.client_initialization_synchronization_pending = None
                        self.client_synchronization_end_of_download_pending = None
                        self.up_time_stamp = None
                        self.down_time_stamp = None
                        self.clean_up_timer_remaining = None
                        self._segment_path = lambda: "client-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, ['component', 'client_connection_status', 'client_initialization_synchronization_pending', 'client_synchronization_end_of_download_pending', 'up_time_stamp', 'down_time_stamp', 'clean_up_timer_remaining'], name, value)


                class OpaqueMemoryStatus(Entity):
                    """
                    Opaque memory Stats
                    
                    .. attribute:: component
                    
                    	Component
                    	**type**\:  :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                    
                    .. attribute:: session_count
                    
                    	Session count for each component
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_size
                    
                    	Current Opaque Memory Size for each component
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_high_size
                    
                    	High Watermark of Opaque Data Size for each component
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_data_size
                    
                    	Current Opaque Data Size for each component
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, self).__init__()

                        self.yang_name = "opaque-memory-status"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('component', YLeaf(YType.enumeration, 'component')),
                            ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ('opaque_size', YLeaf(YType.uint32, 'opaque-size')),
                            ('opaque_high_size', YLeaf(YType.uint32, 'opaque-high-size')),
                            ('opaque_data_size', YLeaf(YType.uint32, 'opaque-data-size')),
                        ])
                        self.component = None
                        self.session_count = None
                        self.opaque_size = None
                        self.opaque_high_size = None
                        self.opaque_data_size = None
                        self._segment_path = lambda: "opaque-memory-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, ['component', 'session_count', 'opaque_size', 'opaque_high_size', 'opaque_data_size'], name, value)


                class TxListOverTcpStatus(Entity):
                    """
                    TCP TxList Statistics
                    
                    .. attribute:: messages_sent
                    
                    	Message Sent Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes Sent Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: messages_received
                    
                    	Message Received Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_received
                    
                    	Bytes Received Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: connect_count
                    
                    	Socket Connect Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: blocked_connect_count
                    
                    	Blocked Socket Connect Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connect_retry_count
                    
                    	Socket Connect Retry Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_node_down_count
                    
                    	Remote Peer DisConnect Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accept_count
                    
                    	Socket Accept Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_sent_message_size
                    
                    	Maximum Size of Sent Message
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_received_message_size
                    
                    	Maximum Size of Received Message
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_pause_count
                    
                    	Peer Pause Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: buffer_full_occurence_count
                    
                    	Buffer Full on Write Occurence Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mem_move_message_count
                    
                    	Partial Message Memory Move Occurence Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mem_move_bytes_count
                    
                    	Partial Message Memory Move Byte Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_read_count
                    
                    	Socket Read Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_write_count
                    
                    	Socket Write Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_socket_count
                    
                    	Active Socket Count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: maximum_requested_buffer_size
                    
                    	Maximum Size of Requested Buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: buffer_freed_count
                    
                    	Buffer Free Count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_cache_hit
                    
                    	Buffer Cache Hit Count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_cache_miss
                    
                    	Buffer Cache Miss Count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, self).__init__()

                        self.yang_name = "tx-list-over-tcp-status"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('messages_sent', YLeaf(YType.uint32, 'messages-sent')),
                            ('bytes_sent', YLeaf(YType.uint32, 'bytes-sent')),
                            ('messages_received', YLeaf(YType.uint32, 'messages-received')),
                            ('bytes_received', YLeaf(YType.uint32, 'bytes-received')),
                            ('connect_count', YLeaf(YType.uint32, 'connect-count')),
                            ('blocked_connect_count', YLeaf(YType.uint32, 'blocked-connect-count')),
                            ('connect_retry_count', YLeaf(YType.uint32, 'connect-retry-count')),
                            ('remote_node_down_count', YLeaf(YType.uint32, 'remote-node-down-count')),
                            ('accept_count', YLeaf(YType.uint32, 'accept-count')),
                            ('maximum_sent_message_size', YLeaf(YType.uint32, 'maximum-sent-message-size')),
                            ('maximum_received_message_size', YLeaf(YType.uint32, 'maximum-received-message-size')),
                            ('peer_pause_count', YLeaf(YType.uint32, 'peer-pause-count')),
                            ('buffer_full_occurence_count', YLeaf(YType.uint32, 'buffer-full-occurence-count')),
                            ('mem_move_message_count', YLeaf(YType.uint32, 'mem-move-message-count')),
                            ('mem_move_bytes_count', YLeaf(YType.uint32, 'mem-move-bytes-count')),
                            ('socket_read_count', YLeaf(YType.uint32, 'socket-read-count')),
                            ('socket_write_count', YLeaf(YType.uint32, 'socket-write-count')),
                            ('active_socket_count', YLeaf(YType.uint16, 'active-socket-count')),
                            ('maximum_requested_buffer_size', YLeaf(YType.uint32, 'maximum-requested-buffer-size')),
                            ('buffer_freed_count', YLeaf(YType.uint16, 'buffer-freed-count')),
                            ('buffer_cache_hit', YLeaf(YType.uint16, 'buffer-cache-hit')),
                            ('buffer_cache_miss', YLeaf(YType.uint16, 'buffer-cache-miss')),
                        ])
                        self.messages_sent = None
                        self.bytes_sent = None
                        self.messages_received = None
                        self.bytes_received = None
                        self.connect_count = None
                        self.blocked_connect_count = None
                        self.connect_retry_count = None
                        self.remote_node_down_count = None
                        self.accept_count = None
                        self.maximum_sent_message_size = None
                        self.maximum_received_message_size = None
                        self.peer_pause_count = None
                        self.buffer_full_occurence_count = None
                        self.mem_move_message_count = None
                        self.mem_move_bytes_count = None
                        self.socket_read_count = None
                        self.socket_write_count = None
                        self.active_socket_count = None
                        self.maximum_requested_buffer_size = None
                        self.buffer_freed_count = None
                        self.buffer_cache_hit = None
                        self.buffer_cache_miss = None
                        self._segment_path = lambda: "tx-list-over-tcp-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, ['messages_sent', 'bytes_sent', 'messages_received', 'bytes_received', 'connect_count', 'blocked_connect_count', 'connect_retry_count', 'remote_node_down_count', 'accept_count', 'maximum_sent_message_size', 'maximum_received_message_size', 'peer_pause_count', 'buffer_full_occurence_count', 'mem_move_message_count', 'mem_move_bytes_count', 'socket_read_count', 'socket_write_count', 'active_socket_count', 'maximum_requested_buffer_size', 'buffer_freed_count', 'buffer_cache_hit', 'buffer_cache_miss'], name, value)


            class GroupSummaries(Entity):
                """
                Session data for a particular node
                
                .. attribute:: group_summary
                
                	Session redundancy agent group summary
                	**type**\: list of  		 :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupSummaries, self).__init__()

                    self.yang_name = "group-summaries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("group-summary", ("group_summary", SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary))])
                    self._leafs = OrderedDict()

                    self.group_summary = YList(self)
                    self._segment_path = lambda: "group-summaries"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupSummaries, [], name, value)


                class GroupSummary(Entity):
                    """
                    Session redundancy agent group summary
                    
                    .. attribute:: group_id  (key)
                    
                    	GroupId
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SERG Role
                    	**type**\:  :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\: bool
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:  :py:class:`SergPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergPeerStatus>`
                    
                    .. attribute:: preferred_role
                    
                    	Preferred Role
                    	**type**\:  :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:  :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\: bool
                    
                    .. attribute:: interface_count
                    
                    	Interface Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_add_session_count
                    
                    	Pending Session Count for Synchornization
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__init__()

                        self.yang_name = "group-summary"
                        self.yang_parent_name = "group-summaries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('group_id', YLeaf(YType.str, 'group-id')),
                            ('group_id_xr', YLeaf(YType.uint32, 'group-id-xr')),
                            ('role', YLeaf(YType.enumeration, 'role')),
                            ('disabled', YLeaf(YType.boolean, 'disabled')),
                            ('peer_ipv4_address', YLeaf(YType.str, 'peer-ipv4-address')),
                            ('peer_ipv6_address', YLeaf(YType.str, 'peer-ipv6-address')),
                            ('peer_status', YLeaf(YType.enumeration, 'peer-status')),
                            ('preferred_role', YLeaf(YType.enumeration, 'preferred-role')),
                            ('slave_mode', YLeaf(YType.enumeration, 'slave-mode')),
                            ('object_tracking_status', YLeaf(YType.boolean, 'object-tracking-status')),
                            ('interface_count', YLeaf(YType.uint32, 'interface-count')),
                            ('session_count', YLeaf(YType.uint32, 'session-count')),
                            ('pending_add_session_count', YLeaf(YType.uint32, 'pending-add-session-count')),
                        ])
                        self.group_id = None
                        self.group_id_xr = None
                        self.role = None
                        self.disabled = None
                        self.peer_ipv4_address = None
                        self.peer_ipv6_address = None
                        self.peer_status = None
                        self.preferred_role = None
                        self.slave_mode = None
                        self.object_tracking_status = None
                        self.interface_count = None
                        self.session_count = None
                        self.pending_add_session_count = None
                        self._segment_path = lambda: "group-summary" + "[group-id='" + str(self.group_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, ['group_id', 'group_id_xr', 'role', 'disabled', 'peer_ipv4_address', 'peer_ipv6_address', 'peer_status', 'preferred_role', 'slave_mode', 'object_tracking_status', 'interface_count', 'session_count', 'pending_add_session_count'], name, value)

    def clone_ptr(self):
        self._top_entity = SessionRedundancyAgent()
        return self._top_entity

