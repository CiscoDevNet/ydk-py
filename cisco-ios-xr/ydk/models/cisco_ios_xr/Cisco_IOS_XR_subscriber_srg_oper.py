""" Cisco_IOS_XR_subscriber_srg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\-manager\: Subscriber Redundancy Manager
    information
  subscriber\-redundancy\-agent\: subscriber redundancy agent

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrgPeerStatus(Enum):
    """
    SrgPeerStatus

    SRG Peer Status

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


class SrgShowComp(Enum):
    """
    SrgShowComp

    SRG Components

    .. data:: srga = 0

    	SRG Agent

    .. data:: dhcpv4 = 1

    	DHCPv4

    .. data:: dhcpv6 = 2

    	DHCPv6

    .. data:: pppoe = 3

    	PPPoE

    .. data:: ppp = 4

    	PPP

    .. data:: l2tp = 5

    	L2TP

    .. data:: iedge = 6

    	iEdge

    """

    srga = Enum.YLeaf(0, "srga")

    dhcpv4 = Enum.YLeaf(1, "dhcpv4")

    dhcpv6 = Enum.YLeaf(2, "dhcpv6")

    pppoe = Enum.YLeaf(3, "pppoe")

    ppp = Enum.YLeaf(4, "ppp")

    l2tp = Enum.YLeaf(5, "l2tp")

    iedge = Enum.YLeaf(6, "iedge")


class SrgShowImRole(Enum):
    """
    SrgShowImRole

    SRG Interface Management Role

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


class SrgShowRole(Enum):
    """
    SrgShowRole

    SRG Role

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


class SrgShowSessionError(Enum):
    """
    SrgShowSessionError

    SRG Session Error Operation

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


class SrgShowSessionOperation(Enum):
    """
    SrgShowSessionOperation

    SRG Session Operation

    .. data:: none = 0

    	No Operation

    .. data:: update = 1

    	SRG Session Update Operation

    .. data:: delete = 2

    	SRG Session Delete Operation

    .. data:: in_sync = 3

    	SRG Session In Sync

    """

    none = Enum.YLeaf(0, "none")

    update = Enum.YLeaf(1, "update")

    delete = Enum.YLeaf(2, "delete")

    in_sync = Enum.YLeaf(3, "in-sync")


class SrgShowSlaveMode(Enum):
    """
    SrgShowSlaveMode

    SRG Slave Mode

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


class SrgShowSoReason(Enum):
    """
    SrgShowSoReason

    Subscriber Redundancy Switchover Reason

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

    .. data:: srg_show_so_reason_max = 5

    	Unknown Switchover Reason

    """

    internal = Enum.YLeaf(0, "internal")

    admin = Enum.YLeaf(1, "admin")

    peer_up = Enum.YLeaf(2, "peer-up")

    peer_down = Enum.YLeaf(3, "peer-down")

    object_tracking_status_change = Enum.YLeaf(4, "object-tracking-status-change")

    srg_show_so_reason_max = Enum.YLeaf(5, "srg-show-so-reason-max")



class SubscriberRedundancyAgent(Entity):
    """
    subscriber redundancy agent
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes>`
    
    

    """

    _prefix = 'subscriber-srg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberRedundancyAgent, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-redundancy-agent"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-srg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", SubscriberRedundancyAgent.Nodes)}
        self._child_list_classes = {}

        self.nodes = SubscriberRedundancyAgent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent"


    class Nodes(Entity):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyAgent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "subscriber-redundancy-agent"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", SubscriberRedundancyAgent.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancyAgent.Nodes, [], name, value)


        class Node(Entity):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: group_id_xr
            
            	Data for particular subscriber group session
            	**type**\:   :py:class:`GroupIdXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr>`
            
            .. attribute:: group_ids
            
            	Data for particular subscriber group 
            	**type**\:   :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds>`
            
            .. attribute:: group_summaries
            
            	Subscriber data for a particular node
            	**type**\:   :py:class:`GroupSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupSummaries>`
            
            .. attribute:: interfaces
            
            	List of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancyAgent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"group-id-xr" : ("group_id_xr", SubscriberRedundancyAgent.Nodes.Node.GroupIdXr), "group-ids" : ("group_ids", SubscriberRedundancyAgent.Nodes.Node.GroupIds), "group-summaries" : ("group_summaries", SubscriberRedundancyAgent.Nodes.Node.GroupSummaries), "interfaces" : ("interfaces", SubscriberRedundancyAgent.Nodes.Node.Interfaces)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.group_id_xr = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self._children_name_map["group_id_xr"] = "group-id-xr"
                self._children_yang_names.add("group-id-xr")

                self.group_ids = SubscriberRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self._children_name_map["group_ids"] = "group-ids"
                self._children_yang_names.add("group-ids")

                self.group_summaries = SubscriberRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self._children_name_map["group_summaries"] = "group-summaries"
                self._children_yang_names.add("group-summaries")

                self.interfaces = SubscriberRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node, ['node_name'], name, value)


            class GroupIdXr(Entity):
                """
                Data for particular subscriber group session
                
                .. attribute:: group_id
                
                	Group id for subscriber group session
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr, self).__init__()

                    self.yang_name = "group-id-xr"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group-id" : ("group_id", SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId)}

                    self.group_id = YList(self)
                    self._segment_path = lambda: "group-id-xr"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr, [], name, value)


                class GroupId(Entity):
                    """
                    Group id for subscriber group session
                    
                    .. attribute:: group_id  <key>
                    
                    	GroupId
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inner_vlan
                    
                    	Inner VLAN Information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: l2tp_tunnel_id
                    
                    	L2TP Tunnel local ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: negative_acknowledgement_update_all
                    
                    	Negative Acknowledgement Update Flag is Set
                    	**type**\:  bool
                    
                    .. attribute:: outer_vlan
                    
                    	Outer VLAN Information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pppoe_session_id
                    
                    	PPPoE Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: role_master
                    
                    	Master Role is Set
                    	**type**\:  bool
                    
                    .. attribute:: session_detailed_information
                    
                    	More Session Information
                    	**type**\: list of    :py:class:`SessionDetailedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation>`
                    
                    .. attribute:: session_mac_address
                    
                    	Session MAC Address
                    	**type**\:  str
                    
                    .. attribute:: session_sync_error_information
                    
                    	Session Synchroniation Error Information
                    	**type**\: list of    :py:class:`SessionSyncErrorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation>`
                    
                    .. attribute:: valid_mac_address
                    
                    	Holds a Valid MAC Address
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-id-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"session-detailed-information" : ("session_detailed_information", SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation), "session-sync-error-information" : ("session_sync_error_information", SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation)}

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.inner_vlan = YLeaf(YType.uint32, "inner-vlan")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.l2tp_tunnel_id = YLeaf(YType.uint32, "l2tp-tunnel-id")

                        self.negative_acknowledgement_update_all = YLeaf(YType.boolean, "negative-acknowledgement-update-all")

                        self.outer_vlan = YLeaf(YType.uint32, "outer-vlan")

                        self.pppoe_session_id = YLeaf(YType.uint16, "pppoe-session-id")

                        self.role_master = YLeaf(YType.boolean, "role-master")

                        self.session_mac_address = YLeaf(YType.str, "session-mac-address")

                        self.valid_mac_address = YLeaf(YType.boolean, "valid-mac-address")

                        self.session_detailed_information = YList(self)
                        self.session_sync_error_information = YList(self)
                        self._segment_path = lambda: "group-id" + "[group-id='" + self.group_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, ['group_id', 'group_id_xr', 'inner_vlan', 'interface_name', 'l2tp_tunnel_id', 'negative_acknowledgement_update_all', 'outer_vlan', 'pppoe_session_id', 'role_master', 'session_mac_address', 'valid_mac_address'], name, value)


                    class SessionDetailedInformation(Entity):
                        """
                        More Session Information
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SrgShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowComp>`
                        
                        .. attribute:: marked_for_cleanup
                        
                        	Marked For Cleanup
                        	**type**\:  bool
                        
                        .. attribute:: marked_for_sweeping
                        
                        	Marked For Sweeping
                        	**type**\:  bool
                        
                        .. attribute:: operation_
                        
                        	Operation Code
                        	**type**\:   :py:class:`SrgShowSessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSessionOperation>`
                        
                        .. attribute:: tx_list_queue_fail
                        
                        	Tx List Queue Failed
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__init__()

                            self.yang_name = "session-detailed-information"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.component = YLeaf(YType.enumeration, "component")

                            self.marked_for_cleanup = YLeaf(YType.boolean, "marked-for-cleanup")

                            self.marked_for_sweeping = YLeaf(YType.boolean, "marked-for-sweeping")

                            self.operation_ = YLeaf(YType.enumeration, "operation")

                            self.tx_list_queue_fail = YLeaf(YType.boolean, "tx-list-queue-fail")
                            self._segment_path = lambda: "session-detailed-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, ['component', 'marked_for_cleanup', 'marked_for_sweeping', 'operation_', 'tx_list_queue_fail'], name, value)


                    class SessionSyncErrorInformation(Entity):
                        """
                        Session Synchroniation Error Information
                        
                        .. attribute:: last_error_code
                        
                        	Last Error Code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_error_type
                        
                        	Last Error Type
                        	**type**\:   :py:class:`SrgShowSessionError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSessionError>`
                        
                        .. attribute:: sync_error_count
                        
                        	No. of Errors occured during Synchronization
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__init__()

                            self.yang_name = "session-sync-error-information"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.last_error_code = YLeaf(YType.uint32, "last-error-code")

                            self.last_error_type = YLeaf(YType.enumeration, "last-error-type")

                            self.sync_error_count = YLeaf(YType.uint16, "sync-error-count")
                            self._segment_path = lambda: "session-sync-error-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, ['last_error_code', 'last_error_type', 'sync_error_count'], name, value)


            class GroupIds(Entity):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIds, self).__init__()

                    self.yang_name = "group-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group-id" : ("group_id", SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId)}

                    self.group_id = YList(self)
                    self._segment_path = lambda: "group-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIds, [], name, value)


                class GroupId(Entity):
                    """
                    Group id for subscriber group
                    
                    .. attribute:: group_id  <key>
                    
                    	Group Id
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: access_tracking_object_name
                    
                    	Access Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: access_tracking_object_status
                    
                    	Access Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: core_tracking_object_name
                    
                    	Core Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: core_tracking_object_status
                    
                    	Core Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: current_role
                    
                    	Current Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: description
                    
                    	Group Description
                    	**type**\:  str
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\:  bool
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_timer
                    
                    	Switch Over Hold Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_role
                    
                    	Preferred Init Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    .. attribute:: interface_count
                    
                    	No. of Configured Interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2tp_source_ip
                    
                    	L2TP Souce IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: last_switchover_reason
                    
                    	Last Switchover Reason
                    	**type**\:   :py:class:`SrgShowSoReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSoReason>`
                    
                    .. attribute:: last_switchover_time
                    
                    	Last Switchover time
                    	**type**\:  str
                    
                    .. attribute:: negotiating_role
                    
                    	Negotiating Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_current_role
                    
                    	Peer Current Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: peer_init_role
                    
                    	Peer Preferred Init Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_last_down_time
                    
                    	Last Down time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_last_negotiation_time
                    
                    	Last Negotiation time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_last_up_time
                    
                    	Last UP time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_negotiating_role
                    
                    	Peer Negotiating Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: peer_object_tracking_status
                    
                    	Peer Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SrgPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgPeerStatus>`
                    
                    .. attribute:: pending_session_delete_count
                    
                    	Pending Session Delete Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_session_update_count
                    
                    	Pending Session Update Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: revertive_timer
                    
                    	Revertive timer for SWO back
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
                    
                    .. attribute:: slave_update_failure_count
                    
                    	Slave Session update fail count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_count
                    
                    	Switchover Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_hold_time
                    
                    	Switchover Hold Time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: switchover_revert_time
                    
                    	Switchover Revert Time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: tunnel_count
                    
                    	Tunnel Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: virtual_mac_address
                    
                    	Virtual MAC Address
                    	**type**\:  str
                    
                    .. attribute:: virtual_mac_address_disable
                    
                    	Virtual MAC Address Disable
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface)}

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.access_tracking_object_name = YLeaf(YType.str, "access-tracking-object-name")

                        self.access_tracking_object_status = YLeaf(YType.boolean, "access-tracking-object-status")

                        self.core_tracking_object_name = YLeaf(YType.str, "core-tracking-object-name")

                        self.core_tracking_object_status = YLeaf(YType.boolean, "core-tracking-object-status")

                        self.current_role = YLeaf(YType.enumeration, "current-role")

                        self.description = YLeaf(YType.str, "description")

                        self.disabled = YLeaf(YType.boolean, "disabled")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.hold_timer = YLeaf(YType.uint32, "hold-timer")

                        self.init_role = YLeaf(YType.enumeration, "init-role")

                        self.interface_count = YLeaf(YType.uint32, "interface-count")

                        self.l2tp_source_ip = YLeaf(YType.str, "l2tp-source-ip")

                        self.last_switchover_reason = YLeaf(YType.enumeration, "last-switchover-reason")

                        self.last_switchover_time = YLeaf(YType.str, "last-switchover-time")

                        self.negotiating_role = YLeaf(YType.enumeration, "negotiating-role")

                        self.object_tracking_status = YLeaf(YType.boolean, "object-tracking-status")

                        self.peer_current_role = YLeaf(YType.enumeration, "peer-current-role")

                        self.peer_init_role = YLeaf(YType.enumeration, "peer-init-role")

                        self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

                        self.peer_ipv6_address = YLeaf(YType.str, "peer-ipv6-address")

                        self.peer_last_down_time = YLeaf(YType.str, "peer-last-down-time")

                        self.peer_last_negotiation_time = YLeaf(YType.str, "peer-last-negotiation-time")

                        self.peer_last_up_time = YLeaf(YType.str, "peer-last-up-time")

                        self.peer_negotiating_role = YLeaf(YType.enumeration, "peer-negotiating-role")

                        self.peer_object_tracking_status = YLeaf(YType.boolean, "peer-object-tracking-status")

                        self.peer_status = YLeaf(YType.enumeration, "peer-status")

                        self.pending_session_delete_count = YLeaf(YType.uint32, "pending-session-delete-count")

                        self.pending_session_update_count = YLeaf(YType.uint32, "pending-session-update-count")

                        self.revertive_timer = YLeaf(YType.uint32, "revertive-timer")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                        self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

                        self.slave_update_failure_count = YLeaf(YType.uint32, "slave-update-failure-count")

                        self.switchover_count = YLeaf(YType.uint32, "switchover-count")

                        self.switchover_hold_time = YLeaf(YType.uint32, "switchover-hold-time")

                        self.switchover_revert_time = YLeaf(YType.uint32, "switchover-revert-time")

                        self.tunnel_count = YLeaf(YType.uint32, "tunnel-count")

                        self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                        self.virtual_mac_address_disable = YLeaf(YType.boolean, "virtual-mac-address-disable")

                        self.interface = YList(self)
                        self._segment_path = lambda: "group-id" + "[group-id='" + self.group_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId, ['group_id', 'access_tracking_object_name', 'access_tracking_object_status', 'core_tracking_object_name', 'core_tracking_object_status', 'current_role', 'description', 'disabled', 'group_id_xr', 'hold_timer', 'init_role', 'interface_count', 'l2tp_source_ip', 'last_switchover_reason', 'last_switchover_time', 'negotiating_role', 'object_tracking_status', 'peer_current_role', 'peer_init_role', 'peer_ipv4_address', 'peer_ipv6_address', 'peer_last_down_time', 'peer_last_negotiation_time', 'peer_last_up_time', 'peer_negotiating_role', 'peer_object_tracking_status', 'peer_status', 'pending_session_delete_count', 'pending_session_update_count', 'revertive_timer', 'session_count', 'slave_mode', 'slave_update_failure_count', 'switchover_count', 'switchover_hold_time', 'switchover_revert_time', 'tunnel_count', 'virtual_mac_address', 'virtual_mac_address_disable'], name, value)


                    class Interface(Entity):
                        """
                        Interface List
                        
                        .. attribute:: forward_referenced
                        
                        	Forward Referenced
                        	**type**\:  bool
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: interface_synchronization_id
                        
                        	Interface Synchronization ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_count
                        
                        	Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "group-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.forward_referenced = YLeaf(YType.boolean, "forward-referenced")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_synchronization_id = YLeaf(YType.uint32, "interface-synchronization-id")

                            self.session_count = YLeaf(YType.uint32, "session-count")
                            self._segment_path = lambda: "interface"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, ['forward_referenced', 'interface_name', 'interface_synchronization_id', 'session_count'], name, value)


            class GroupSummaries(Entity):
                """
                Subscriber data for a particular node
                
                .. attribute:: group_summary
                
                	Subscriber redundancy agent group summary
                	**type**\: list of    :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries, self).__init__()

                    self.yang_name = "group-summaries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"group-summary" : ("group_summary", SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary)}

                    self.group_summary = YList(self)
                    self._segment_path = lambda: "group-summaries"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries, [], name, value)


                class GroupSummary(Entity):
                    """
                    Subscriber redundancy agent group summary
                    
                    .. attribute:: group_id  <key>
                    
                    	GroupId
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\:  bool
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_count
                    
                    	Interface Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SrgPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgPeerStatus>`
                    
                    .. attribute:: pending_add_session_count
                    
                    	Pending Session Count for Synchornization
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: preferred_role
                    
                    	Preferred Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: role
                    
                    	SRG Role
                    	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__init__()

                        self.yang_name = "group-summary"
                        self.yang_parent_name = "group-summaries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.disabled = YLeaf(YType.boolean, "disabled")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.interface_count = YLeaf(YType.uint32, "interface-count")

                        self.object_tracking_status = YLeaf(YType.boolean, "object-tracking-status")

                        self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

                        self.peer_ipv6_address = YLeaf(YType.str, "peer-ipv6-address")

                        self.peer_status = YLeaf(YType.enumeration, "peer-status")

                        self.pending_add_session_count = YLeaf(YType.uint32, "pending-add-session-count")

                        self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

                        self.role = YLeaf(YType.enumeration, "role")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                        self.slave_mode = YLeaf(YType.enumeration, "slave-mode")
                        self._segment_path = lambda: "group-summary" + "[group-id='" + self.group_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, ['group_id', 'disabled', 'group_id_xr', 'interface_count', 'object_tracking_status', 'peer_ipv4_address', 'peer_ipv6_address', 'peer_status', 'pending_add_session_count', 'preferred_role', 'role', 'session_count', 'slave_mode'], name, value)


            class Interfaces(Entity):
                """
                List of interfaces
                
                .. attribute:: interface
                
                	Specify interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Specify interface name
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: client_status
                    
                    	Interface status for each client
                    	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus>`
                    
                    .. attribute:: forward_referenced
                    
                    	Forward Referenced
                    	**type**\:  bool
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_attribute_update_error_count
                    
                    	Interface Attribute Update Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_add_error_count
                    
                    	Interface Caps Add Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_remove_error_count
                    
                    	Interface Caps Remove Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_disable_error_count
                    
                    	Interface Disable Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_enable_error_count
                    
                    	Interface Enable Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: interface_oper
                    
                    	Interface Batch Operation
                    	**type**\:   :py:class:`InterfaceOper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper>`
                    
                    .. attribute:: interface_status
                    
                    	Interface Status
                    	**type**\:   :py:class:`InterfaceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus>`
                    
                    .. attribute:: interface_synchronization_id
                    
                    	Interface Sync ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SRG Role
                    	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"interface-oper" : ("interface_oper", SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper), "interface-status" : ("interface_status", SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus)}
                        self._child_list_classes = {"client-status" : ("client_status", SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus)}

                        self.interface = YLeaf(YType.str, "interface")

                        self.forward_referenced = YLeaf(YType.boolean, "forward-referenced")

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.interface_attribute_update_error_count = YLeaf(YType.uint32, "interface-attribute-update-error-count")

                        self.interface_caps_add_error_count = YLeaf(YType.uint32, "interface-caps-add-error-count")

                        self.interface_caps_remove_error_count = YLeaf(YType.uint32, "interface-caps-remove-error-count")

                        self.interface_disable_error_count = YLeaf(YType.uint32, "interface-disable-error-count")

                        self.interface_enable_error_count = YLeaf(YType.uint32, "interface-enable-error-count")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_synchronization_id = YLeaf(YType.uint32, "interface-synchronization-id")

                        self.role = YLeaf(YType.enumeration, "role")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                        self.interface_oper = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                        self.interface_oper.parent = self
                        self._children_name_map["interface_oper"] = "interface-oper"
                        self._children_yang_names.add("interface-oper")

                        self.interface_status = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
                        self.interface_status.parent = self
                        self._children_name_map["interface_status"] = "interface-status"
                        self._children_yang_names.add("interface-status")

                        self.client_status = YList(self)
                        self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface, ['interface', 'forward_referenced', 'group_id', 'interface_attribute_update_error_count', 'interface_caps_add_error_count', 'interface_caps_remove_error_count', 'interface_disable_error_count', 'interface_enable_error_count', 'interface_name', 'interface_synchronization_id', 'role', 'session_count'], name, value)


                    class ClientStatus(Entity):
                        """
                        Interface status for each client
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SrgShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowComp>`
                        
                        .. attribute:: session_count
                        
                        	session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_show_idb_client_eoms_pending
                        
                        	SRG SHOW IDB CLIENT EOMS PENDING
                        	**type**\:  bool
                        
                        .. attribute:: srg_show_idb_client_sync_eod_pending
                        
                        	SRG SHOW IDB CLIENT SYNC EOD PENDING
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__init__()

                            self.yang_name = "client-status"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.component = YLeaf(YType.enumeration, "component")

                            self.session_count = YLeaf(YType.uint32, "session-count")

                            self.srg_show_idb_client_eoms_pending = YLeaf(YType.boolean, "srg-show-idb-client-eoms-pending")

                            self.srg_show_idb_client_sync_eod_pending = YLeaf(YType.boolean, "srg-show-idb-client-sync-eod-pending")
                            self._segment_path = lambda: "client-status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, ['component', 'session_count', 'srg_show_idb_client_eoms_pending', 'srg_show_idb_client_sync_eod_pending'], name, value)


                    class InterfaceOper(Entity):
                        """
                        Interface Batch Operation
                        
                        .. attribute:: idb_oper_attr_update
                        
                        	Operational Attribute Update
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_caps_add
                        
                        	Operational Caps Add
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_caps_remove
                        
                        	Operational Caps Remove
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_reg_disable
                        
                        	Operational Registration Disabled
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_reg_enable
                        
                        	Operational Registration Enabled
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__init__()

                            self.yang_name = "interface-oper"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.idb_oper_attr_update = YLeaf(YType.boolean, "idb-oper-attr-update")

                            self.idb_oper_caps_add = YLeaf(YType.boolean, "idb-oper-caps-add")

                            self.idb_oper_caps_remove = YLeaf(YType.boolean, "idb-oper-caps-remove")

                            self.idb_oper_reg_disable = YLeaf(YType.boolean, "idb-oper-reg-disable")

                            self.idb_oper_reg_enable = YLeaf(YType.boolean, "idb-oper-reg-enable")
                            self._segment_path = lambda: "interface-oper"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, ['idb_oper_attr_update', 'idb_oper_caps_add', 'idb_oper_caps_remove', 'idb_oper_reg_disable', 'idb_oper_reg_enable'], name, value)


                    class InterfaceStatus(Entity):
                        """
                        Interface Status
                        
                        .. attribute:: idb_client_eoms_pending
                        
                        	Interface Client EOMS Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_caps_added
                        
                        	Interface State Caps Added
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_fwd_ref
                        
                        	Interface Forward Referenced
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_owned_re_source
                        
                        	Interface State Owned Resource
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_p_end_caps_rem
                        
                        	Interface Caps Remove Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_p_end_reg_disable
                        
                        	Interface Registration Disable Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_registered
                        
                        	Interface State Registered
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_stale
                        
                        	Interface State Stale
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__init__()

                            self.yang_name = "interface-status"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.idb_client_eoms_pending = YLeaf(YType.boolean, "idb-client-eoms-pending")

                            self.idb_state_caps_added = YLeaf(YType.boolean, "idb-state-caps-added")

                            self.idb_state_fwd_ref = YLeaf(YType.boolean, "idb-state-fwd-ref")

                            self.idb_state_owned_re_source = YLeaf(YType.boolean, "idb-state-owned-re-source")

                            self.idb_state_p_end_caps_rem = YLeaf(YType.boolean, "idb-state-p-end-caps-rem")

                            self.idb_state_p_end_reg_disable = YLeaf(YType.boolean, "idb-state-p-end-reg-disable")

                            self.idb_state_registered = YLeaf(YType.boolean, "idb-state-registered")

                            self.idb_state_stale = YLeaf(YType.boolean, "idb-state-stale")
                            self._segment_path = lambda: "interface-status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, ['idb_client_eoms_pending', 'idb_state_caps_added', 'idb_state_fwd_ref', 'idb_state_owned_re_source', 'idb_state_p_end_caps_rem', 'idb_state_p_end_reg_disable', 'idb_state_registered', 'idb_state_stale'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberRedundancyAgent()
        return self._top_entity

class SubscriberRedundancyManager(Entity):
    """
    Subscriber Redundancy Manager information
    
    .. attribute:: groups
    
    	Subscriber Redundancy Manager group table
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Groups>`
    
    .. attribute:: interfaces
    
    	Subscriber Redundancy Manager interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Interfaces>`
    
    .. attribute:: summary
    
    	Subscriber redundancy manager summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Summary>`
    
    

    """

    _prefix = 'subscriber-srg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberRedundancyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-redundancy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-srg-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"groups" : ("groups", SubscriberRedundancyManager.Groups), "interfaces" : ("interfaces", SubscriberRedundancyManager.Interfaces), "summary" : ("summary", SubscriberRedundancyManager.Summary)}
        self._child_list_classes = {}

        self.groups = SubscriberRedundancyManager.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.interfaces = SubscriberRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.summary = SubscriberRedundancyManager.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager"


    class Groups(Entity):
        """
        Subscriber Redundancy Manager group table
        
        .. attribute:: group
        
        	Subscriber redundancy manager group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyManager.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "subscriber-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"group" : ("group", SubscriberRedundancyManager.Groups.Group)}

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancyManager.Groups, [], name, value)


        class Group(Entity):
            """
            Subscriber redundancy manager group
            
            .. attribute:: group  <key>
            
            	Group
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: description
            
            	Group Description
            	**type**\:  str
            
            .. attribute:: disabled
            
            	Disabled by Config
            	**type**\:  bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Interface Count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_name
            
            	Node Information
            	**type**\:  str
            
            .. attribute:: object_tracking_status
            
            	Object Tracking Status (Enabled/Disabled)
            	**type**\:  bool
            
            .. attribute:: peer_ipv4_address
            
            	Peer IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_ipv6_address
            
            	Peer IPv6 Address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: preferred_role
            
            	Preferred Role
            	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
            
            .. attribute:: role
            
            	SRG Role
            	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
            
            .. attribute:: slave_mode
            
            	Slave Mode
            	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
            
            .. attribute:: virtual_mac_address
            
            	Virtual MAC Address
            	**type**\:  str
            
            .. attribute:: virtual_mac_address_disable
            
            	Virtual MAC Address Disable
            	**type**\:  bool
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancyManager.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.group = YLeaf(YType.str, "group")

                self.description = YLeaf(YType.str, "description")

                self.disabled = YLeaf(YType.boolean, "disabled")

                self.group_id = YLeaf(YType.uint32, "group-id")

                self.interface_count = YLeaf(YType.uint32, "interface-count")

                self.node_name = YLeaf(YType.str, "node-name")

                self.object_tracking_status = YLeaf(YType.boolean, "object-tracking-status")

                self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

                self.peer_ipv6_address = YLeaf(YType.str, "peer-ipv6-address")

                self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

                self.role = YLeaf(YType.enumeration, "role")

                self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

                self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                self.virtual_mac_address_disable = YLeaf(YType.boolean, "virtual-mac-address-disable")
                self._segment_path = lambda: "group" + "[group='" + self.group.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberRedundancyManager.Groups.Group, ['group', 'description', 'disabled', 'group_id', 'interface_count', 'node_name', 'object_tracking_status', 'peer_ipv4_address', 'peer_ipv6_address', 'preferred_role', 'role', 'slave_mode', 'virtual_mac_address', 'virtual_mac_address_disable'], name, value)


    class Interfaces(Entity):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	Subscriber redundancy manager interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyManager.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "subscriber-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", SubscriberRedundancyManager.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancyManager.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Subscriber redundancy manager interface
            
            .. attribute:: interface  <key>
            
            	Interface
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: forward_referenced
            
            	Forward Referenced
            	**type**\:  bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_mapping_id
            
            	Interface Mapping ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\:  str
            
            .. attribute:: role
            
            	SRG Role
            	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancyManager.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface = YLeaf(YType.str, "interface")

                self.forward_referenced = YLeaf(YType.boolean, "forward-referenced")

                self.group_id = YLeaf(YType.uint32, "group-id")

                self.interface_mapping_id = YLeaf(YType.uint32, "interface-mapping-id")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.role = YLeaf(YType.enumeration, "role")
                self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberRedundancyManager.Interfaces.Interface, ['interface', 'forward_referenced', 'group_id', 'interface_mapping_id', 'interface_name', 'role'], name, value)


    class Summary(Entity):
        """
        Subscriber redundancy manager summary
        
        .. attribute:: active_state
        
        	Process Active State
        	**type**\:  bool
        
        .. attribute:: disabled
        
        	Disabled by Config
        	**type**\:  bool
        
        .. attribute:: disabled_group_count
        
        	No. of Disabled Groups by Config
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: group_count
        
        	No. of Configured Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: hold_timer
        
        	Switch Over Hold Time
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_count
        
        	No. of Configured Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_group_count
        
        	No. of Master/Active Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_interface_count
        
        	No. of Master/Active Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: preferred_role
        
        	Preferred Role
        	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
        
        .. attribute:: slave_group_count
        
        	No. of Slave Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_interface_count
        
        	No. of Slave Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_mode
        
        	Slave Mode
        	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
        
        .. attribute:: source_interface_ipv4_address
        
        	Source Interface IPv4 Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_ipv6_address
        
        	Source Interface IPv6 Address
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_name
        
        	Source Interface Name
        	**type**\:  str
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\:  str
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyManager.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "subscriber-redundancy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.active_state = YLeaf(YType.boolean, "active-state")

            self.disabled = YLeaf(YType.boolean, "disabled")

            self.disabled_group_count = YLeaf(YType.uint32, "disabled-group-count")

            self.group_count = YLeaf(YType.uint32, "group-count")

            self.hold_timer = YLeaf(YType.uint32, "hold-timer")

            self.interface_count = YLeaf(YType.uint32, "interface-count")

            self.master_group_count = YLeaf(YType.uint32, "master-group-count")

            self.master_interface_count = YLeaf(YType.uint32, "master-interface-count")

            self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

            self.slave_group_count = YLeaf(YType.uint32, "slave-group-count")

            self.slave_interface_count = YLeaf(YType.uint32, "slave-interface-count")

            self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

            self.source_interface_ipv4_address = YLeaf(YType.str, "source-interface-ipv4-address")

            self.source_interface_ipv6_address = YLeaf(YType.str, "source-interface-ipv6-address")

            self.source_interface_name = YLeaf(YType.str, "source-interface-name")

            self.vrf_name = YLeaf(YType.str, "vrf-name")
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberRedundancyManager.Summary, ['active_state', 'disabled', 'disabled_group_count', 'group_count', 'hold_timer', 'interface_count', 'master_group_count', 'master_interface_count', 'preferred_role', 'slave_group_count', 'slave_interface_count', 'slave_mode', 'source_interface_ipv4_address', 'source_interface_ipv6_address', 'source_interface_name', 'vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberRedundancyManager()
        return self._top_entity

