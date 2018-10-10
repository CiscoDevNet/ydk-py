""" Cisco_IOS_XR_infra_serg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package operational data.

This module contains definitions
for the following management objects\:
  session\-redundancy\-manager\: Session Redundancy Manager
    information
  session\-redundancy\-agent\: session redundancy agent

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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

    .. data:: daps = 3

    	DAPS

    """

    serga = Enum.YLeaf(0, "serga")

    ipv6nd = Enum.YLeaf(1, "ipv6nd")

    dhcpv6 = Enum.YLeaf(2, "dhcpv6")

    daps = Enum.YLeaf(3, "daps")


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
    _revision = '2017-09-07'

    def __init__(self):
        super(SessionRedundancyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", SessionRedundancyManager.Interfaces)), ("groups", ("groups", SessionRedundancyManager.Groups)), ("summary", ("summary", SessionRedundancyManager.Summary))])
        self._leafs = OrderedDict()

        self.interfaces = SessionRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.groups = SessionRedundancyManager.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"

        self.summary = SessionRedundancyManager.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SessionRedundancyManager, [], name, value)


    class Interfaces(Entity):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	interface redundancy manager interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SessionRedundancyManager.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "session-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", SessionRedundancyManager.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2017-09-07'

            def __init__(self):
                super(SessionRedundancyManager.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface_mapping_id', (YLeaf(YType.uint32, 'interface-mapping-id'), ['int'])),
                    ('forward_referenced', (YLeaf(YType.boolean, 'forward-referenced'), ['bool'])),
                    ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRole', '')])),
                ])
                self.interface = None
                self.interface_name = None
                self.interface_mapping_id = None
                self.forward_referenced = None
                self.group_id = None
                self.role = None
                self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SessionRedundancyManager.Interfaces.Interface, ['interface', u'interface_name', u'interface_mapping_id', u'forward_referenced', u'group_id', u'role'], name, value)


    class Groups(Entity):
        """
        Session Redundancy Manager group table
        
        .. attribute:: group
        
        	Session redundancy manager group
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SessionRedundancyManager.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "session-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", SessionRedundancyManager.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2017-09-07'

            def __init__(self):
                super(SessionRedundancyManager.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                    ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('disabled', (YLeaf(YType.boolean, 'disabled'), ['bool'])),
                    ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRole', '')])),
                    ('peer_ipv4_address', (YLeaf(YType.str, 'peer-ipv4-address'), ['str'])),
                    ('peer_ipv6_address', (YLeaf(YType.str, 'peer-ipv6-address'), ['str'])),
                    ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                    ('preferred_role', (YLeaf(YType.enumeration, 'preferred-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                    ('slave_mode', (YLeaf(YType.enumeration, 'slave-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveMode', '')])),
                    ('object_tracking_status', (YLeaf(YType.boolean, 'object-tracking-status'), ['bool'])),
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SessionRedundancyManager.Groups.Group, ['group', u'group_id', u'description', u'disabled', u'role', u'peer_ipv4_address', u'peer_ipv6_address', u'interface_count', u'preferred_role', u'slave_mode', u'object_tracking_status', u'node_name'], name, value)


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
        
        .. attribute:: pool_count
        
        	No. of Configured Pools
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SessionRedundancyManager.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "session-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('disabled', (YLeaf(YType.boolean, 'disabled'), ['bool'])),
                ('active_state', (YLeaf(YType.boolean, 'active-state'), ['bool'])),
                ('preferred_role', (YLeaf(YType.enumeration, 'preferred-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                ('slave_mode', (YLeaf(YType.enumeration, 'slave-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveMode', '')])),
                ('hold_timer', (YLeaf(YType.uint32, 'hold-timer'), ['int'])),
                ('source_interface_name', (YLeaf(YType.str, 'source-interface-name'), ['str'])),
                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ('source_interface_ipv4_address', (YLeaf(YType.str, 'source-interface-ipv4-address'), ['str'])),
                ('source_interface_ipv6_address', (YLeaf(YType.str, 'source-interface-ipv6-address'), ['str'])),
                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                ('disabled_group_count', (YLeaf(YType.uint32, 'disabled-group-count'), ['int'])),
                ('master_group_count', (YLeaf(YType.uint32, 'master-group-count'), ['int'])),
                ('slave_group_count', (YLeaf(YType.uint32, 'slave-group-count'), ['int'])),
                ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                ('master_interface_count', (YLeaf(YType.uint32, 'master-interface-count'), ['int'])),
                ('slave_interface_count', (YLeaf(YType.uint32, 'slave-interface-count'), ['int'])),
                ('pool_count', (YLeaf(YType.uint32, 'pool-count'), ['int'])),
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
            self.pool_count = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SessionRedundancyManager.Summary, [u'disabled', u'active_state', u'preferred_role', u'slave_mode', u'hold_timer', u'source_interface_name', u'vrf_name', u'source_interface_ipv4_address', u'source_interface_ipv6_address', u'group_count', u'disabled_group_count', u'master_group_count', u'slave_group_count', u'interface_count', u'master_interface_count', u'slave_interface_count', u'pool_count'], name, value)

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
    _revision = '2017-09-07'

    def __init__(self):
        super(SessionRedundancyAgent, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy-agent"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", SessionRedundancyAgent.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = SessionRedundancyAgent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SessionRedundancyAgent, [], name, value)


    class Nodes(Entity):
        """
        List of nodes for which session data is
        collected
        
        .. attribute:: node
        
        	Session data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SessionRedundancyAgent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "session-redundancy-agent"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SessionRedundancyAgent.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2017-09-07'

            def __init__(self):
                super(SessionRedundancyAgent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("group-id-xr", ("group_id_xr", SessionRedundancyAgent.Nodes.Node.GroupIdXr)), ("client-ids", ("client_ids", SessionRedundancyAgent.Nodes.Node.ClientIds)), ("memory", ("memory", SessionRedundancyAgent.Nodes.Node.Memory)), ("group-ids", ("group_ids", SessionRedundancyAgent.Nodes.Node.GroupIds)), ("interfaces", ("interfaces", SessionRedundancyAgent.Nodes.Node.Interfaces)), ("stats-global", ("stats_global", SessionRedundancyAgent.Nodes.Node.StatsGlobal)), ("group-summaries", ("group_summaries", SessionRedundancyAgent.Nodes.Node.GroupSummaries))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.group_id_xr = SessionRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self._children_name_map["group_id_xr"] = "group-id-xr"

                self.client_ids = SessionRedundancyAgent.Nodes.Node.ClientIds()
                self.client_ids.parent = self
                self._children_name_map["client_ids"] = "client-ids"

                self.memory = SessionRedundancyAgent.Nodes.Node.Memory()
                self.memory.parent = self
                self._children_name_map["memory"] = "memory"

                self.group_ids = SessionRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self._children_name_map["group_ids"] = "group-ids"

                self.interfaces = SessionRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.stats_global = SessionRedundancyAgent.Nodes.Node.StatsGlobal()
                self.stats_global.parent = self
                self._children_name_map["stats_global"] = "stats-global"

                self.group_summaries = SessionRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self._children_name_map["group_summaries"] = "group-summaries"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/nodes/%s" % self._segment_path()
                self._is_frozen = True

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
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupIdXr, self).__init__()

                    self.yang_name = "group-id-xr"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group-id", ("group_id", SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId))])
                    self._leafs = OrderedDict()

                    self.group_id = YList(self)
                    self._segment_path = lambda: "group-id-xr"
                    self._is_frozen = True

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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-id-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_classes = OrderedDict([("session-detailed-information", ("session_detailed_information", SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation)), ("session-sync-error-information", ("session_sync_error_information", SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation))])
                        self._leafs = OrderedDict([
                            ('group_id', (YLeaf(YType.str, 'group-id'), ['str'])),
                            ('group_id_xr', (YLeaf(YType.uint32, 'group-id-xr'), ['int'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('key_index', (YLeaf(YType.str, 'key-index'), ['str'])),
                            ('role_master', (YLeaf(YType.boolean, 'role-master'), ['bool'])),
                            ('negative_acknowledgement_update_all', (YLeaf(YType.boolean, 'negative-acknowledgement-update-all'), ['bool'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, ['group_id', u'group_id_xr', u'interface_name', u'key_index', u'role_master', u'negative_acknowledgement_update_all'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__init__()

                            self.yang_name = "session-detailed-information"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('component', (YLeaf(YType.enumeration, 'component'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowComp', '')])),
                                ('operation_', (YLeaf(YType.enumeration, 'operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSessionOperation', '')])),
                                ('tx_list_queue_fail', (YLeaf(YType.boolean, 'tx-list-queue-fail'), ['bool'])),
                                ('marked_for_sweeping', (YLeaf(YType.boolean, 'marked-for-sweeping'), ['bool'])),
                                ('marked_for_cleanup', (YLeaf(YType.boolean, 'marked-for-cleanup'), ['bool'])),
                            ])
                            self.component = None
                            self.operation_ = None
                            self.tx_list_queue_fail = None
                            self.marked_for_sweeping = None
                            self.marked_for_cleanup = None
                            self._segment_path = lambda: "session-detailed-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, [u'component', u'operation_', u'tx_list_queue_fail', u'marked_for_sweeping', u'marked_for_cleanup'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__init__()

                            self.yang_name = "session-sync-error-information"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sync_error_count', (YLeaf(YType.uint16, 'sync-error-count'), ['int'])),
                                ('last_error_code', (YLeaf(YType.uint32, 'last-error-code'), ['int'])),
                                ('last_error_type', (YLeaf(YType.enumeration, 'last-error-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSessionError', '')])),
                            ])
                            self.sync_error_count = None
                            self.last_error_code = None
                            self.last_error_type = None
                            self._segment_path = lambda: "session-sync-error-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, [u'sync_error_count', u'last_error_code', u'last_error_type'], name, value)


            class ClientIds(Entity):
                """
                Stats Client
                
                .. attribute:: client_id
                
                	Specify stats client
                	**type**\: list of  		 :py:class:`ClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.ClientIds, self).__init__()

                    self.yang_name = "client-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client-id", ("client_id", SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId))])
                    self._leafs = OrderedDict()

                    self.client_id = YList(self)
                    self._segment_path = lambda: "client-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.ClientIds, [], name, value)


                class ClientId(Entity):
                    """
                    Specify stats client
                    
                    .. attribute:: stats_client_id  (key)
                    
                    	Client Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    
                    .. attribute:: tx_list_send_pool_role_ok
                    
                    	TxListSendPoolRoleOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_send_pool_role_not_ok
                    
                    	TxListSendPoolRoleNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_send_pool_update_ok
                    
                    	TxListSendPoolUpdateOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_send_pool_update_not_ok
                    
                    	TxListSendPoolUpdateNotOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_recv_pool_update_ok
                    
                    	TxListRecvPoolUpdateOk
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, self).__init__()

                        self.yang_name = "client-id"
                        self.yang_parent_name = "client-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['stats_client_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('stats_client_id', (YLeaf(YType.uint32, 'stats-client-id'), ['int'])),
                            ('tx_list_start_of_download_add_ok', (YLeaf(YType.uint32, 'tx-list-start-of-download-add-ok'), ['int'])),
                            ('tx_list_start_of_download_add_not_ok', (YLeaf(YType.uint32, 'tx-list-start-of-download-add-not-ok'), ['int'])),
                            ('tx_list_end_of_download_add_ok', (YLeaf(YType.uint32, 'tx-list-end-of-download-add-ok'), ['int'])),
                            ('tx_list_end_of_download_add_not_ok', (YLeaf(YType.uint32, 'tx-list-end-of-download-add-not-ok'), ['int'])),
                            ('tx_list_end_of_message_add_ok', (YLeaf(YType.uint32, 'tx-list-end-of-message-add-ok'), ['int'])),
                            ('tx_list_end_of_message_add_not_ok', (YLeaf(YType.uint32, 'tx-list-end-of-message-add-not-ok'), ['int'])),
                            ('tx_list_clear_all_add_ok', (YLeaf(YType.uint32, 'tx-list-clear-all-add-ok'), ['int'])),
                            ('tx_list_clear_all_add_not_ok', (YLeaf(YType.uint32, 'tx-list-clear-all-add-not-ok'), ['int'])),
                            ('tx_list_clear_selected_add_ok', (YLeaf(YType.uint32, 'tx-list-clear-selected-add-ok'), ['int'])),
                            ('tx_list_clear_selected_add_not_ok', (YLeaf(YType.uint32, 'tx-list-clear-selected-add-not-ok'), ['int'])),
                            ('tx_list_replay_all_add_ok', (YLeaf(YType.uint32, 'tx-list-replay-all-add-ok'), ['int'])),
                            ('tx_list_replay_all_add_not_ok', (YLeaf(YType.uint32, 'tx-list-replay-all-add-not-ok'), ['int'])),
                            ('tx_list_replay_selected_add_ok', (YLeaf(YType.uint32, 'tx-list-replay-selected-add-ok'), ['int'])),
                            ('tx_list_replay_selected_add_not_ok', (YLeaf(YType.uint32, 'tx-list-replay-selected-add-not-ok'), ['int'])),
                            ('tx_list_session_session_add_ok', (YLeaf(YType.uint32, 'tx-list-session-session-add-ok'), ['int'])),
                            ('tx_list_session_session_add_not_ok', (YLeaf(YType.uint32, 'tx-list-session-session-add-not-ok'), ['int'])),
                            ('tx_list_session_session_update_ok', (YLeaf(YType.uint32, 'tx-list-session-session-update-ok'), ['int'])),
                            ('tx_list_session_session_update_not_ok', (YLeaf(YType.uint32, 'tx-list-session-session-update-not-ok'), ['int'])),
                            ('tx_list_session_session_delete', (YLeaf(YType.uint32, 'tx-list-session-session-delete'), ['int'])),
                            ('clean_call_back', (YLeaf(YType.uint32, 'clean-call-back'), ['int'])),
                            ('tx_list_encode_session_session_ok', (YLeaf(YType.uint32, 'tx-list-encode-session-session-ok'), ['int'])),
                            ('tx_list_encode_session_session_partial_write', (YLeaf(YType.uint32, 'tx-list-encode-session-session-partial-write'), ['int'])),
                            ('last_replay_all_count', (YLeaf(YType.uint32, 'last-replay-all-count'), ['int'])),
                            ('tx_list_receive_command_replay_all', (YLeaf(YType.uint32, 'tx-list-receive-command-replay-all'), ['int'])),
                            ('tx_list_receive_command_replay_selected', (YLeaf(YType.uint32, 'tx-list-receive-command-replay-selected'), ['int'])),
                            ('tx_list_receive_session_session_delete_valid', (YLeaf(YType.uint32, 'tx-list-receive-session-session-delete-valid'), ['int'])),
                            ('tx_list_receive_session_session_delete_invalid', (YLeaf(YType.uint32, 'tx-list-receive-session-session-delete-invalid'), ['int'])),
                            ('tx_list_receive_session_session_update_valid', (YLeaf(YType.uint32, 'tx-list-receive-session-session-update-valid'), ['int'])),
                            ('tx_list_receive_session_session_update_invalid', (YLeaf(YType.uint32, 'tx-list-receive-session-session-update-invalid'), ['int'])),
                            ('tx_list_receive_session_session_sod_all', (YLeaf(YType.uint32, 'tx-list-receive-session-session-sod-all'), ['int'])),
                            ('tx_list_receive_session_session_sod_selected', (YLeaf(YType.uint32, 'tx-list-receive-session-session-sod-selected'), ['int'])),
                            ('tx_list_receive_session_session_eod_all', (YLeaf(YType.uint32, 'tx-list-receive-session-session-eod-all'), ['int'])),
                            ('tx_list_receive_session_session_eod_selected', (YLeaf(YType.uint32, 'tx-list-receive-session-session-eod-selected'), ['int'])),
                            ('tx_list_receive_session_session_eoms', (YLeaf(YType.uint32, 'tx-list-receive-session-session-eoms'), ['int'])),
                            ('tx_list_receive_session_session_clear_all', (YLeaf(YType.uint32, 'tx-list-receive-session-session-clear-all'), ['int'])),
                            ('tx_list_receive_session_session_clear_selected', (YLeaf(YType.uint32, 'tx-list-receive-session-session-clear-selected'), ['int'])),
                            ('tx_list_receive_session_session_neg_ack', (YLeaf(YType.uint32, 'tx-list-receive-session-session-neg-ack'), ['int'])),
                            ('tx_list_receive_session_session_neg_ack_not_ok', (YLeaf(YType.uint32, 'tx-list-receive-session-session-neg-ack-not-ok'), ['int'])),
                            ('tx_list_client_registration_ok', (YLeaf(YType.uint32, 'tx-list-client-registration-ok'), ['int'])),
                            ('tx_list_client_registration_not_ok', (YLeaf(YType.uint32, 'tx-list-client-registration-not-ok'), ['int'])),
                            ('tx_list_client_de_registration', (YLeaf(YType.uint32, 'tx-list-client-de-registration'), ['int'])),
                            ('tx_list_client_connection_down', (YLeaf(YType.uint32, 'tx-list-client-connection-down'), ['int'])),
                            ('tx_list_client_cleanup', (YLeaf(YType.uint32, 'tx-list-client-cleanup'), ['int'])),
                            ('tx_list_active_ok', (YLeaf(YType.uint32, 'tx-list-active-ok'), ['int'])),
                            ('tx_list_active_not_ok', (YLeaf(YType.uint32, 'tx-list-active-not-ok'), ['int'])),
                            ('tx_list_de_active_ok', (YLeaf(YType.uint32, 'tx-list-de-active-ok'), ['int'])),
                            ('tx_list_de_active_not_ok', (YLeaf(YType.uint32, 'tx-list-de-active-not-ok'), ['int'])),
                            ('tx_list_send_pool_role_ok', (YLeaf(YType.uint32, 'tx-list-send-pool-role-ok'), ['int'])),
                            ('tx_list_send_pool_role_not_ok', (YLeaf(YType.uint32, 'tx-list-send-pool-role-not-ok'), ['int'])),
                            ('tx_list_send_pool_update_ok', (YLeaf(YType.uint32, 'tx-list-send-pool-update-ok'), ['int'])),
                            ('tx_list_send_pool_update_not_ok', (YLeaf(YType.uint32, 'tx-list-send-pool-update-not-ok'), ['int'])),
                            ('tx_list_recv_pool_update_ok', (YLeaf(YType.uint32, 'tx-list-recv-pool-update-ok'), ['int'])),
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
                        self.tx_list_send_pool_role_ok = None
                        self.tx_list_send_pool_role_not_ok = None
                        self.tx_list_send_pool_update_ok = None
                        self.tx_list_send_pool_update_not_ok = None
                        self.tx_list_recv_pool_update_ok = None
                        self._segment_path = lambda: "client-id" + "[stats-client-id='" + str(self.stats_client_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, ['stats_client_id', u'tx_list_start_of_download_add_ok', u'tx_list_start_of_download_add_not_ok', u'tx_list_end_of_download_add_ok', u'tx_list_end_of_download_add_not_ok', u'tx_list_end_of_message_add_ok', u'tx_list_end_of_message_add_not_ok', u'tx_list_clear_all_add_ok', u'tx_list_clear_all_add_not_ok', u'tx_list_clear_selected_add_ok', u'tx_list_clear_selected_add_not_ok', u'tx_list_replay_all_add_ok', u'tx_list_replay_all_add_not_ok', u'tx_list_replay_selected_add_ok', u'tx_list_replay_selected_add_not_ok', u'tx_list_session_session_add_ok', u'tx_list_session_session_add_not_ok', u'tx_list_session_session_update_ok', u'tx_list_session_session_update_not_ok', u'tx_list_session_session_delete', u'clean_call_back', u'tx_list_encode_session_session_ok', u'tx_list_encode_session_session_partial_write', u'last_replay_all_count', u'tx_list_receive_command_replay_all', u'tx_list_receive_command_replay_selected', u'tx_list_receive_session_session_delete_valid', u'tx_list_receive_session_session_delete_invalid', u'tx_list_receive_session_session_update_valid', u'tx_list_receive_session_session_update_invalid', u'tx_list_receive_session_session_sod_all', u'tx_list_receive_session_session_sod_selected', u'tx_list_receive_session_session_eod_all', u'tx_list_receive_session_session_eod_selected', u'tx_list_receive_session_session_eoms', u'tx_list_receive_session_session_clear_all', u'tx_list_receive_session_session_clear_selected', u'tx_list_receive_session_session_neg_ack', u'tx_list_receive_session_session_neg_ack_not_ok', u'tx_list_client_registration_ok', u'tx_list_client_registration_not_ok', u'tx_list_client_de_registration', u'tx_list_client_connection_down', u'tx_list_client_cleanup', u'tx_list_active_ok', u'tx_list_active_not_ok', u'tx_list_de_active_ok', u'tx_list_de_active_not_ok', u'tx_list_send_pool_role_ok', u'tx_list_send_pool_role_not_ok', u'tx_list_send_pool_update_ok', u'tx_list_send_pool_update_not_ok', u'tx_list_recv_pool_update_ok'], name, value)


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
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.Memory, self).__init__()

                    self.yang_name = "memory"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("memory-info", ("memory_info", SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo)), ("edm-memory-info", ("edm_memory_info", SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo)), ("string-memory-info", ("string_memory_info", SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo))])
                    self._leafs = OrderedDict()

                    self.memory_info = YList(self)
                    self.edm_memory_info = YList(self)
                    self.string_memory_info = YList(self)
                    self._segment_path = lambda: "memory"
                    self._is_frozen = True

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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, self).__init__()

                        self.yang_name = "memory-info"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('structure_name', (YLeaf(YType.str, 'structure-name'), ['str'])),
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('current_count', (YLeaf(YType.uint32, 'current-count'), ['int'])),
                            ('alloc_fails', (YLeaf(YType.uint32, 'alloc-fails'), ['int'])),
                            ('alloc_count', (YLeaf(YType.uint32, 'alloc-count'), ['int'])),
                            ('freed_count', (YLeaf(YType.uint32, 'freed-count'), ['int'])),
                            ('memory_type', (YLeaf(YType.enumeration, 'memory-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowMem', '')])),
                        ])
                        self.structure_name = None
                        self.size = None
                        self.current_count = None
                        self.alloc_fails = None
                        self.alloc_count = None
                        self.freed_count = None
                        self.memory_type = None
                        self._segment_path = lambda: "memory-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, [u'structure_name', u'size', u'current_count', u'alloc_fails', u'alloc_count', u'freed_count', u'memory_type'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, self).__init__()

                        self.yang_name = "edm-memory-info"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                            ('success', (YLeaf(YType.uint32, 'success'), ['int'])),
                            ('failure', (YLeaf(YType.uint32, 'failure'), ['int'])),
                        ])
                        self.size = None
                        self.total = None
                        self.success = None
                        self.failure = None
                        self._segment_path = lambda: "edm-memory-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, [u'size', u'total', u'success', u'failure'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, self).__init__()

                        self.yang_name = "string-memory-info"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                            ('success', (YLeaf(YType.uint32, 'success'), ['int'])),
                            ('failure', (YLeaf(YType.uint32, 'failure'), ['int'])),
                        ])
                        self.size = None
                        self.total = None
                        self.success = None
                        self.failure = None
                        self._segment_path = lambda: "string-memory-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, [u'size', u'total', u'success', u'failure'], name, value)


            class GroupIds(Entity):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of  		 :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupIds, self).__init__()

                    self.yang_name = "group-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group-id", ("group_id", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId))])
                    self._leafs = OrderedDict()

                    self.group_id = YList(self)
                    self._segment_path = lambda: "group-ids"
                    self._is_frozen = True

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
                    
                    .. attribute:: pool_count
                    
                    	No. of Configured Pools
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: client_session_count
                    
                    	Client Session Count
                    	**type**\: list of  		 :py:class:`ClientSessionCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    .. attribute:: pool
                    
                    	Pool List
                    	**type**\: list of  		 :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Pool>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_classes = OrderedDict([("client-session-count", ("client_session_count", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount)), ("interface", ("interface", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface)), ("pool", ("pool", SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Pool))])
                        self._leafs = OrderedDict([
                            ('group_id', (YLeaf(YType.str, 'group-id'), ['str'])),
                            ('group_id_xr', (YLeaf(YType.uint32, 'group-id-xr'), ['int'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('disabled', (YLeaf(YType.boolean, 'disabled'), ['bool'])),
                            ('init_role', (YLeaf(YType.enumeration, 'init-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('negotiating_role', (YLeaf(YType.enumeration, 'negotiating-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('current_role', (YLeaf(YType.enumeration, 'current-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('slave_mode', (YLeaf(YType.enumeration, 'slave-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveMode', '')])),
                            ('hold_timer', (YLeaf(YType.uint32, 'hold-timer'), ['int'])),
                            ('core_tracking_object_name', (YLeaf(YType.str, 'core-tracking-object-name'), ['str'])),
                            ('core_tracking_object_status', (YLeaf(YType.boolean, 'core-tracking-object-status'), ['bool'])),
                            ('access_tracking_object_name', (YLeaf(YType.str, 'access-tracking-object-name'), ['str'])),
                            ('access_tracking_object_status', (YLeaf(YType.boolean, 'access-tracking-object-status'), ['bool'])),
                            ('object_tracking_status', (YLeaf(YType.boolean, 'object-tracking-status'), ['bool'])),
                            ('peer_ipv4_address', (YLeaf(YType.str, 'peer-ipv4-address'), ['str'])),
                            ('peer_ipv6_address', (YLeaf(YType.str, 'peer-ipv6-address'), ['str'])),
                            ('peer_status', (YLeaf(YType.enumeration, 'peer-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergPeerStatus', '')])),
                            ('peer_last_negotiation_time', (YLeaf(YType.str, 'peer-last-negotiation-time'), ['str'])),
                            ('peer_last_up_time', (YLeaf(YType.str, 'peer-last-up-time'), ['str'])),
                            ('peer_last_down_time', (YLeaf(YType.str, 'peer-last-down-time'), ['str'])),
                            ('peer_init_role', (YLeaf(YType.enumeration, 'peer-init-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('peer_negotiating_role', (YLeaf(YType.enumeration, 'peer-negotiating-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('peer_current_role', (YLeaf(YType.enumeration, 'peer-current-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('peer_object_tracking_status', (YLeaf(YType.boolean, 'peer-object-tracking-status'), ['bool'])),
                            ('last_switchover_time', (YLeaf(YType.str, 'last-switchover-time'), ['str'])),
                            ('switchover_count', (YLeaf(YType.uint32, 'switchover-count'), ['int'])),
                            ('last_switchover_reason', (YLeaf(YType.enumeration, 'last-switchover-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSoReason', '')])),
                            ('switchover_hold_time', (YLeaf(YType.uint32, 'switchover-hold-time'), ['int'])),
                            ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ('slave_update_failure_count', (YLeaf(YType.uint32, 'slave-update-failure-count'), ['int'])),
                            ('pending_session_update_count', (YLeaf(YType.uint32, 'pending-session-update-count'), ['int'])),
                            ('pending_session_delete_count', (YLeaf(YType.uint32, 'pending-session-delete-count'), ['int'])),
                            ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                            ('revertive_timer', (YLeaf(YType.uint32, 'revertive-timer'), ['int'])),
                            ('switchover_revert_time', (YLeaf(YType.uint32, 'switchover-revert-time'), ['int'])),
                            ('pool_count', (YLeaf(YType.uint32, 'pool-count'), ['int'])),
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
                        self.pool_count = None

                        self.client_session_count = YList(self)
                        self.interface = YList(self)
                        self.pool = YList(self)
                        self._segment_path = lambda: "group-id" + "[group-id='" + str(self.group_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, ['group_id', u'group_id_xr', u'description', u'disabled', u'init_role', u'negotiating_role', u'current_role', u'slave_mode', u'hold_timer', u'core_tracking_object_name', u'core_tracking_object_status', u'access_tracking_object_name', u'access_tracking_object_status', u'object_tracking_status', u'peer_ipv4_address', u'peer_ipv6_address', u'peer_status', u'peer_last_negotiation_time', u'peer_last_up_time', u'peer_last_down_time', u'peer_init_role', u'peer_negotiating_role', u'peer_current_role', u'peer_object_tracking_status', u'last_switchover_time', u'switchover_count', u'last_switchover_reason', u'switchover_hold_time', u'session_count', u'slave_update_failure_count', u'pending_session_update_count', u'pending_session_delete_count', u'interface_count', u'revertive_timer', u'switchover_revert_time', u'pool_count'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, self).__init__()

                            self.yang_name = "client-session-count"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('component', (YLeaf(YType.enumeration, 'component'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowComp', '')])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ])
                            self.component = None
                            self.session_count = None
                            self._segment_path = lambda: "client-session-count"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, [u'component', u'session_count'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_synchronization_id', (YLeaf(YType.uint32, 'interface-synchronization-id'), ['int'])),
                                ('forward_referenced', (YLeaf(YType.boolean, 'forward-referenced'), ['bool'])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ])
                            self.interface_name = None
                            self.interface_synchronization_id = None
                            self.forward_referenced = None
                            self.session_count = None
                            self._segment_path = lambda: "interface"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, [u'interface_name', u'interface_synchronization_id', u'forward_referenced', u'session_count'], name, value)


                    class Pool(Entity):
                        """
                        Pool List
                        
                        .. attribute:: pool_name
                        
                        	Pool Name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Pool, self).__init__()

                            self.yang_name = "pool"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                            ])
                            self.pool_name = None
                            self._segment_path = lambda: "pool"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Pool, [u'pool_name'], name, value)


            class Interfaces(Entity):
                """
                List of interfaces
                
                .. attribute:: interface
                
                	Specify interface name
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Specify interface name
                    
                    .. attribute:: interface  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_classes = OrderedDict([("interface-oper", ("interface_oper", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper)), ("interface-status", ("interface_status", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus)), ("client-status", ("client_status", SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus))])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface_synchronization_id', (YLeaf(YType.uint32, 'interface-synchronization-id'), ['int'])),
                            ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                            ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRole', '')])),
                            ('forward_referenced', (YLeaf(YType.boolean, 'forward-referenced'), ['bool'])),
                            ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ('interface_enable_error_count', (YLeaf(YType.uint32, 'interface-enable-error-count'), ['int'])),
                            ('interface_disable_error_count', (YLeaf(YType.uint32, 'interface-disable-error-count'), ['int'])),
                            ('interface_caps_add_error_count', (YLeaf(YType.uint32, 'interface-caps-add-error-count'), ['int'])),
                            ('interface_caps_remove_error_count', (YLeaf(YType.uint32, 'interface-caps-remove-error-count'), ['int'])),
                            ('interface_attribute_update_error_count', (YLeaf(YType.uint32, 'interface-attribute-update-error-count'), ['int'])),
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

                        self.interface_status = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
                        self.interface_status.parent = self
                        self._children_name_map["interface_status"] = "interface-status"

                        self.client_status = YList(self)
                        self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, ['interface', u'interface_name', u'interface_synchronization_id', u'group_id', u'role', u'forward_referenced', u'session_count', u'interface_enable_error_count', u'interface_disable_error_count', u'interface_caps_add_error_count', u'interface_caps_remove_error_count', u'interface_attribute_update_error_count'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__init__()

                            self.yang_name = "interface-oper"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('idb_oper_reg_enable', (YLeaf(YType.boolean, 'idb-oper-reg-enable'), ['bool'])),
                                ('idb_oper_reg_disable', (YLeaf(YType.boolean, 'idb-oper-reg-disable'), ['bool'])),
                                ('idb_oper_caps_add', (YLeaf(YType.boolean, 'idb-oper-caps-add'), ['bool'])),
                                ('idb_oper_caps_remove', (YLeaf(YType.boolean, 'idb-oper-caps-remove'), ['bool'])),
                                ('idb_oper_attr_update', (YLeaf(YType.boolean, 'idb-oper-attr-update'), ['bool'])),
                            ])
                            self.idb_oper_reg_enable = None
                            self.idb_oper_reg_disable = None
                            self.idb_oper_caps_add = None
                            self.idb_oper_caps_remove = None
                            self.idb_oper_attr_update = None
                            self._segment_path = lambda: "interface-oper"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, [u'idb_oper_reg_enable', u'idb_oper_reg_disable', u'idb_oper_caps_add', u'idb_oper_caps_remove', u'idb_oper_attr_update'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__init__()

                            self.yang_name = "interface-status"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('idb_state_fwd_ref', (YLeaf(YType.boolean, 'idb-state-fwd-ref'), ['bool'])),
                                ('idb_state_stale', (YLeaf(YType.boolean, 'idb-state-stale'), ['bool'])),
                                ('idb_state_registered', (YLeaf(YType.boolean, 'idb-state-registered'), ['bool'])),
                                ('idb_state_caps_added', (YLeaf(YType.boolean, 'idb-state-caps-added'), ['bool'])),
                                ('idb_state_owned_re_source', (YLeaf(YType.boolean, 'idb-state-owned-re-source'), ['bool'])),
                                ('idb_client_eoms_pending', (YLeaf(YType.boolean, 'idb-client-eoms-pending'), ['bool'])),
                                ('idb_state_p_end_caps_rem', (YLeaf(YType.boolean, 'idb-state-p-end-caps-rem'), ['bool'])),
                                ('idb_state_p_end_reg_disable', (YLeaf(YType.boolean, 'idb-state-p-end-reg-disable'), ['bool'])),
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
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, [u'idb_state_fwd_ref', u'idb_state_stale', u'idb_state_registered', u'idb_state_caps_added', u'idb_state_owned_re_source', u'idb_client_eoms_pending', u'idb_state_p_end_caps_rem', u'idb_state_p_end_reg_disable'], name, value)


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
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__init__()

                            self.yang_name = "client-status"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('component', (YLeaf(YType.enumeration, 'component'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowComp', '')])),
                                ('serg_show_idb_client_eoms_pending', (YLeaf(YType.boolean, 'serg-show-idb-client-eoms-pending'), ['bool'])),
                                ('serg_show_idb_client_sync_eod_pending', (YLeaf(YType.boolean, 'serg-show-idb-client-sync-eod-pending'), ['bool'])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ])
                            self.component = None
                            self.serg_show_idb_client_eoms_pending = None
                            self.serg_show_idb_client_sync_eod_pending = None
                            self.session_count = None
                            self._segment_path = lambda: "client-status"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, [u'component', u'serg_show_idb_client_eoms_pending', u'serg_show_idb_client_sync_eod_pending', u'session_count'], name, value)


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
                
                .. attribute:: tx_list_send_pool_update_not_ok
                
                	TxListSendPoolUpdateNotOk
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
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal, self).__init__()

                    self.yang_name = "stats-global"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("intf-status-statistics", ("intf_status_statistics", SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics)), ("tx-list-statistics", ("tx_list_statistics", SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics)), ("client-status", ("client_status", SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus)), ("opaque-memory-status", ("opaque_memory_status", SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus)), ("tx-list-over-tcp-status", ("tx_list_over_tcp_status", SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus))])
                    self._leafs = OrderedDict([
                        ('source_interface_name', (YLeaf(YType.str, 'source-interface-name'), ['str'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('source_interface_ipv4_address', (YLeaf(YType.str, 'source-interface-ipv4-address'), ['str'])),
                        ('source_interface_ipv6_address', (YLeaf(YType.str, 'source-interface-ipv6-address'), ['str'])),
                        ('redundancy_role', (YLeaf(YType.str, 'redundancy-role'), ['str'])),
                        ('restart_client_sync_in_progress', (YLeaf(YType.boolean, 'restart-client-sync-in-progress'), ['bool'])),
                        ('client_init_sync_time_stamp', (YLeaf(YType.str, 'client-init-sync-time-stamp'), ['str'])),
                        ('restart_peer_sync_in_progress', (YLeaf(YType.boolean, 'restart-peer-sync-in-progress'), ['bool'])),
                        ('peer_init_sync_time_stamp', (YLeaf(YType.str, 'peer-init-sync-time-stamp'), ['str'])),
                        ('sync_in_progress', (YLeaf(YType.boolean, 'sync-in-progress'), ['bool'])),
                        ('peer_action_timer', (YLeaf(YType.uint32, 'peer-action-timer'), ['int'])),
                        ('retry_timer_remaining', (YLeaf(YType.uint32, 'retry-timer-remaining'), ['int'])),
                        ('tx_list_client_registration_invalid', (YLeaf(YType.uint32, 'tx-list-client-registration-invalid'), ['int'])),
                        ('tx_list_client_de_registration_invalid', (YLeaf(YType.uint32, 'tx-list-client-de-registration-invalid'), ['int'])),
                        ('tx_list_client_connection_up', (YLeaf(YType.uint32, 'tx-list-client-connection-up'), ['int'])),
                        ('tx_list_client_connection_down', (YLeaf(YType.uint32, 'tx-list-client-connection-down'), ['int'])),
                        ('tx_list_client_peer_done', (YLeaf(YType.uint32, 'tx-list-client-peer-done'), ['int'])),
                        ('tx_list_client_message_call_back', (YLeaf(YType.uint32, 'tx-list-client-message-call-back'), ['int'])),
                        ('tx_list_client_receive_valid', (YLeaf(YType.uint32, 'tx-list-client-receive-valid'), ['int'])),
                        ('tx_list_client_receive_invalid', (YLeaf(YType.uint32, 'tx-list-client-receive-invalid'), ['int'])),
                        ('tx_list_client_receive_command_valid', (YLeaf(YType.uint32, 'tx-list-client-receive-command-valid'), ['int'])),
                        ('tx_list_client_receive_command_invalid', (YLeaf(YType.uint32, 'tx-list-client-receive-command-invalid'), ['int'])),
                        ('tx_list_client_receive_session_sessionvalid', (YLeaf(YType.uint32, 'tx-list-client-receive-session-sessionvalid'), ['int'])),
                        ('tx_list_client_receive_session_session_invalid', (YLeaf(YType.uint32, 'tx-list-client-receive-session-session-invalid'), ['int'])),
                        ('tx_list_peer_timer_handler', (YLeaf(YType.uint32, 'tx-list-peer-timer-handler'), ['int'])),
                        ('tx_list_peer_registration_invalid', (YLeaf(YType.uint32, 'tx-list-peer-registration-invalid'), ['int'])),
                        ('tx_list_peer_de_registration_invalid', (YLeaf(YType.uint32, 'tx-list-peer-de-registration-invalid'), ['int'])),
                        ('tx_list_peer_message_call_back_valid', (YLeaf(YType.uint32, 'tx-list-peer-message-call-back-valid'), ['int'])),
                        ('tx_list_peer_message_call_back_invalid', (YLeaf(YType.uint32, 'tx-list-peer-message-call-back-invalid'), ['int'])),
                        ('tx_list_peer_done', (YLeaf(YType.uint32, 'tx-list-peer-done'), ['int'])),
                        ('tx_list_peer_cmd_connection_up_not_ok', (YLeaf(YType.uint32, 'tx-list-peer-cmd-connection-up-not-ok'), ['int'])),
                        ('tx_list_peer_cmd_connection_down_not_ok', (YLeaf(YType.uint32, 'tx-list-peer-cmd-connection-down-not-ok'), ['int'])),
                        ('tx_list_peer_session_connection_up_not_ok', (YLeaf(YType.uint32, 'tx-list-peer-session-connection-up-not-ok'), ['int'])),
                        ('tx_list_peer_session_connection_down_not_ok', (YLeaf(YType.uint32, 'tx-list-peer-session-connection-down-not-ok'), ['int'])),
                        ('tx_list_send_pool_update_not_ok', (YLeaf(YType.uint32, 'tx-list-send-pool-update-not-ok'), ['int'])),
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
                    self.tx_list_send_pool_update_not_ok = None

                    self.intf_status_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics()
                    self.intf_status_statistics.parent = self
                    self._children_name_map["intf_status_statistics"] = "intf-status-statistics"

                    self.tx_list_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics()
                    self.tx_list_statistics.parent = self
                    self._children_name_map["tx_list_statistics"] = "tx-list-statistics"

                    self.client_status = YList(self)
                    self.opaque_memory_status = YList(self)
                    self.tx_list_over_tcp_status = YList(self)
                    self._segment_path = lambda: "stats-global"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal, [u'source_interface_name', u'vrf_name', u'source_interface_ipv4_address', u'source_interface_ipv6_address', u'redundancy_role', u'restart_client_sync_in_progress', u'client_init_sync_time_stamp', u'restart_peer_sync_in_progress', u'peer_init_sync_time_stamp', u'sync_in_progress', u'peer_action_timer', u'retry_timer_remaining', u'tx_list_client_registration_invalid', u'tx_list_client_de_registration_invalid', u'tx_list_client_connection_up', u'tx_list_client_connection_down', u'tx_list_client_peer_done', u'tx_list_client_message_call_back', u'tx_list_client_receive_valid', u'tx_list_client_receive_invalid', u'tx_list_client_receive_command_valid', u'tx_list_client_receive_command_invalid', u'tx_list_client_receive_session_sessionvalid', u'tx_list_client_receive_session_session_invalid', u'tx_list_peer_timer_handler', u'tx_list_peer_registration_invalid', u'tx_list_peer_de_registration_invalid', u'tx_list_peer_message_call_back_valid', u'tx_list_peer_message_call_back_invalid', u'tx_list_peer_done', u'tx_list_peer_cmd_connection_up_not_ok', u'tx_list_peer_cmd_connection_down_not_ok', u'tx_list_peer_session_connection_up_not_ok', u'tx_list_peer_session_connection_down_not_ok', u'tx_list_send_pool_update_not_ok'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, self).__init__()

                        self.yang_name = "intf-status-statistics"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pend_caps_rem_cnt', (YLeaf(YType.uint32, 'pend-caps-rem-cnt'), ['int'])),
                            ('pend_reg_disable_cnt', (YLeaf(YType.uint32, 'pend-reg-disable-cnt'), ['int'])),
                            ('pend_other_batch_oper_cnt', (YLeaf(YType.uint32, 'pend-other-batch-oper-cnt'), ['int'])),
                            ('non_stale_cnt', (YLeaf(YType.uint32, 'non-stale-cnt'), ['int'])),
                            ('grp_bound_cnt', (YLeaf(YType.uint32, 'grp-bound-cnt'), ['int'])),
                        ])
                        self.pend_caps_rem_cnt = None
                        self.pend_reg_disable_cnt = None
                        self.pend_other_batch_oper_cnt = None
                        self.non_stale_cnt = None
                        self.grp_bound_cnt = None
                        self._segment_path = lambda: "intf-status-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, [u'pend_caps_rem_cnt', u'pend_reg_disable_cnt', u'pend_other_batch_oper_cnt', u'non_stale_cnt', u'grp_bound_cnt'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, self).__init__()

                        self.yang_name = "tx-list-statistics"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tx_list_encode_marker_ok', (YLeaf(YType.uint32, 'tx-list-encode-marker-ok'), ['int'])),
                            ('tx_list_encode_marker_partial_write', (YLeaf(YType.uint32, 'tx-list-encode-marker-partial-write'), ['int'])),
                            ('tx_list_clean_marker', (YLeaf(YType.uint32, 'tx-list-clean-marker'), ['int'])),
                            ('tx_list_encode_command_ok', (YLeaf(YType.uint32, 'tx-list-encode-command-ok'), ['int'])),
                            ('tx_list_encode_command_partial_write', (YLeaf(YType.uint32, 'tx-list-encode-command-partial-write'), ['int'])),
                            ('tx_list_clean_command', (YLeaf(YType.uint32, 'tx-list-clean-command'), ['int'])),
                            ('tx_list_encode_negotiation_ok', (YLeaf(YType.uint32, 'tx-list-encode-negotiation-ok'), ['int'])),
                            ('tx_list_encode_negotiation_partial_write', (YLeaf(YType.uint32, 'tx-list-encode-negotiation-partial-write'), ['int'])),
                            ('tx_list_clean_negotiation', (YLeaf(YType.uint32, 'tx-list-clean-negotiation'), ['int'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, [u'tx_list_encode_marker_ok', u'tx_list_encode_marker_partial_write', u'tx_list_clean_marker', u'tx_list_encode_command_ok', u'tx_list_encode_command_partial_write', u'tx_list_clean_command', u'tx_list_encode_negotiation_ok', u'tx_list_encode_negotiation_partial_write', u'tx_list_clean_negotiation'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, self).__init__()

                        self.yang_name = "client-status"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('component', (YLeaf(YType.enumeration, 'component'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowComp', '')])),
                            ('client_connection_status', (YLeaf(YType.boolean, 'client-connection-status'), ['bool'])),
                            ('client_initialization_synchronization_pending', (YLeaf(YType.boolean, 'client-initialization-synchronization-pending'), ['bool'])),
                            ('client_synchronization_end_of_download_pending', (YLeaf(YType.boolean, 'client-synchronization-end-of-download-pending'), ['bool'])),
                            ('up_time_stamp', (YLeaf(YType.str, 'up-time-stamp'), ['str'])),
                            ('down_time_stamp', (YLeaf(YType.str, 'down-time-stamp'), ['str'])),
                            ('clean_up_timer_remaining', (YLeaf(YType.uint32, 'clean-up-timer-remaining'), ['int'])),
                        ])
                        self.component = None
                        self.client_connection_status = None
                        self.client_initialization_synchronization_pending = None
                        self.client_synchronization_end_of_download_pending = None
                        self.up_time_stamp = None
                        self.down_time_stamp = None
                        self.clean_up_timer_remaining = None
                        self._segment_path = lambda: "client-status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, [u'component', u'client_connection_status', u'client_initialization_synchronization_pending', u'client_synchronization_end_of_download_pending', u'up_time_stamp', u'down_time_stamp', u'clean_up_timer_remaining'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, self).__init__()

                        self.yang_name = "opaque-memory-status"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('component', (YLeaf(YType.enumeration, 'component'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowComp', '')])),
                            ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ('opaque_size', (YLeaf(YType.uint32, 'opaque-size'), ['int'])),
                            ('opaque_high_size', (YLeaf(YType.uint32, 'opaque-high-size'), ['int'])),
                            ('opaque_data_size', (YLeaf(YType.uint32, 'opaque-data-size'), ['int'])),
                        ])
                        self.component = None
                        self.session_count = None
                        self.opaque_size = None
                        self.opaque_high_size = None
                        self.opaque_data_size = None
                        self._segment_path = lambda: "opaque-memory-status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, [u'component', u'session_count', u'opaque_size', u'opaque_high_size', u'opaque_data_size'], name, value)


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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, self).__init__()

                        self.yang_name = "tx-list-over-tcp-status"
                        self.yang_parent_name = "stats-global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('messages_sent', (YLeaf(YType.uint32, 'messages-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint32, 'bytes-sent'), ['int'])),
                            ('messages_received', (YLeaf(YType.uint32, 'messages-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint32, 'bytes-received'), ['int'])),
                            ('connect_count', (YLeaf(YType.uint32, 'connect-count'), ['int'])),
                            ('blocked_connect_count', (YLeaf(YType.uint32, 'blocked-connect-count'), ['int'])),
                            ('connect_retry_count', (YLeaf(YType.uint32, 'connect-retry-count'), ['int'])),
                            ('remote_node_down_count', (YLeaf(YType.uint32, 'remote-node-down-count'), ['int'])),
                            ('accept_count', (YLeaf(YType.uint32, 'accept-count'), ['int'])),
                            ('maximum_sent_message_size', (YLeaf(YType.uint32, 'maximum-sent-message-size'), ['int'])),
                            ('maximum_received_message_size', (YLeaf(YType.uint32, 'maximum-received-message-size'), ['int'])),
                            ('peer_pause_count', (YLeaf(YType.uint32, 'peer-pause-count'), ['int'])),
                            ('buffer_full_occurence_count', (YLeaf(YType.uint32, 'buffer-full-occurence-count'), ['int'])),
                            ('mem_move_message_count', (YLeaf(YType.uint32, 'mem-move-message-count'), ['int'])),
                            ('mem_move_bytes_count', (YLeaf(YType.uint32, 'mem-move-bytes-count'), ['int'])),
                            ('socket_read_count', (YLeaf(YType.uint32, 'socket-read-count'), ['int'])),
                            ('socket_write_count', (YLeaf(YType.uint32, 'socket-write-count'), ['int'])),
                            ('active_socket_count', (YLeaf(YType.uint16, 'active-socket-count'), ['int'])),
                            ('maximum_requested_buffer_size', (YLeaf(YType.uint32, 'maximum-requested-buffer-size'), ['int'])),
                            ('buffer_freed_count', (YLeaf(YType.uint16, 'buffer-freed-count'), ['int'])),
                            ('buffer_cache_hit', (YLeaf(YType.uint16, 'buffer-cache-hit'), ['int'])),
                            ('buffer_cache_miss', (YLeaf(YType.uint16, 'buffer-cache-miss'), ['int'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, [u'messages_sent', u'bytes_sent', u'messages_received', u'bytes_received', u'connect_count', u'blocked_connect_count', u'connect_retry_count', u'remote_node_down_count', u'accept_count', u'maximum_sent_message_size', u'maximum_received_message_size', u'peer_pause_count', u'buffer_full_occurence_count', u'mem_move_message_count', u'mem_move_bytes_count', u'socket_read_count', u'socket_write_count', u'active_socket_count', u'maximum_requested_buffer_size', u'buffer_freed_count', u'buffer_cache_hit', u'buffer_cache_miss'], name, value)


            class GroupSummaries(Entity):
                """
                Session data for a particular node
                
                .. attribute:: group_summary
                
                	Session redundancy agent group summary
                	**type**\: list of  		 :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupSummaries, self).__init__()

                    self.yang_name = "group-summaries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group-summary", ("group_summary", SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary))])
                    self._leafs = OrderedDict()

                    self.group_summary = YList(self)
                    self._segment_path = lambda: "group-summaries"
                    self._is_frozen = True

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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__init__()

                        self.yang_name = "group-summary"
                        self.yang_parent_name = "group-summaries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('group_id', (YLeaf(YType.str, 'group-id'), ['str'])),
                            ('group_id_xr', (YLeaf(YType.uint32, 'group-id-xr'), ['int'])),
                            ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRole', '')])),
                            ('disabled', (YLeaf(YType.boolean, 'disabled'), ['bool'])),
                            ('peer_ipv4_address', (YLeaf(YType.str, 'peer-ipv4-address'), ['str'])),
                            ('peer_ipv6_address', (YLeaf(YType.str, 'peer-ipv6-address'), ['str'])),
                            ('peer_status', (YLeaf(YType.enumeration, 'peer-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergPeerStatus', '')])),
                            ('preferred_role', (YLeaf(YType.enumeration, 'preferred-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRole', '')])),
                            ('slave_mode', (YLeaf(YType.enumeration, 'slave-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveMode', '')])),
                            ('object_tracking_status', (YLeaf(YType.boolean, 'object-tracking-status'), ['bool'])),
                            ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                            ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                            ('pending_add_session_count', (YLeaf(YType.uint32, 'pending-add-session-count'), ['int'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, ['group_id', u'group_id_xr', u'role', u'disabled', u'peer_ipv4_address', u'peer_ipv6_address', u'peer_status', u'preferred_role', u'slave_mode', u'object_tracking_status', u'interface_count', u'session_count', u'pending_add_session_count'], name, value)

    def clone_ptr(self):
        self._top_entity = SessionRedundancyAgent()
        return self._top_entity

