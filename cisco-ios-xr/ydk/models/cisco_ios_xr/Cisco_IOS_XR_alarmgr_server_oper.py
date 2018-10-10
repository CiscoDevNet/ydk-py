""" Cisco_IOS_XR_alarmgr_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR alarmgr\-server package operational data.

This module contains definitions
for the following management objects\:
  alarms\: Show Alarms associated with XR

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AlarmClient(Enum):
    """
    AlarmClient (Enum Class)

    Alarm client

    .. data:: unknown = 1

    	Client type unknown

    .. data:: producer = 2

    	Client type producer

    .. data:: consumer = 4

    	Client type consumer

    .. data:: subscriber = 8

    	Client type subscriber

    .. data:: client_last = 16

    	Client type last

    """

    unknown = Enum.YLeaf(1, "unknown")

    producer = Enum.YLeaf(2, "producer")

    consumer = Enum.YLeaf(4, "consumer")

    subscriber = Enum.YLeaf(8, "subscriber")

    client_last = Enum.YLeaf(16, "client-last")


class AlarmClientState(Enum):
    """
    AlarmClientState (Enum Class)

    Alarm client state

    .. data:: start = 0

    	Starting state. Should be 0

    .. data:: init = 1

    	Client initalized

    .. data:: connecting = 2

    	Sent connect request

    .. data:: connected = 3

    	Initial connected

    .. data:: registered = 4

    	Has sent registration message

    .. data:: disconnected = 5

    	Has been disconnected due to request of error

    .. data:: ready = 6

    	The client is ready

    """

    start = Enum.YLeaf(0, "start")

    init = Enum.YLeaf(1, "init")

    connecting = Enum.YLeaf(2, "connecting")

    connected = Enum.YLeaf(3, "connected")

    registered = Enum.YLeaf(4, "registered")

    disconnected = Enum.YLeaf(5, "disconnected")

    ready = Enum.YLeaf(6, "ready")


class AlarmDirection(Enum):
    """
    AlarmDirection (Enum Class)

    Alarm direction

    .. data:: not_specified = 0

    	Direction Not Specified

    .. data:: send = 1

    	Direction Send

    .. data:: receive = 2

    	Direction Receive

    .. data:: send_receive = 3

    	Direction Send and Receive

    """

    not_specified = Enum.YLeaf(0, "not-specified")

    send = Enum.YLeaf(1, "send")

    receive = Enum.YLeaf(2, "receive")

    send_receive = Enum.YLeaf(3, "send-receive")


class AlarmEvent(Enum):
    """
    AlarmEvent (Enum Class)

    Alarm event

    .. data:: default = 0

    	Default Alarm Event Type

    .. data:: notification = 1

    	Alarm Notifcation Event Type

    .. data:: condition = 2

    	Alarm Type Condition

    .. data:: last = 3

    	Last Event Type

    """

    default = Enum.YLeaf(0, "default")

    notification = Enum.YLeaf(1, "notification")

    condition = Enum.YLeaf(2, "condition")

    last = Enum.YLeaf(3, "last")


class AlarmGroups(Enum):
    """
    AlarmGroups (Enum Class)

    Alarm groups

    .. data:: unknown = 0

    	An unknown alarm group

    .. data:: environ = 1

    	Environomental alarm group

    .. data:: ethernet = 2

    	Ethernet alarm group

    .. data:: fabric = 3

    	Fabric related alarm group

    .. data:: power = 4

    	Power and PEM group of alarms

    .. data:: software = 5

    	Software group of alarms

    .. data:: slice = 6

    	Slice group of alarms

    .. data:: cpu = 7

    	CPU group of alarms

    .. data:: controller = 8

    	Controller group of alarms

    .. data:: sonet = 9

    	Sonet group of alarms

    .. data:: otn = 10

    	OTN group of alarms

    .. data:: sdh_controller = 11

    	SDH group of alarms

    .. data:: asic = 12

    	ASIC group of alarms

    .. data:: fpd_infra = 13

    	FPD group of alarms

    .. data:: shelf = 14

    	Shelf group of alarms

    .. data:: mpa = 15

    	MPA group of alarms

    .. data:: ots = 16

    	OTS group of alarms

    .. data:: timing = 17

    	Timing group of alarms

    .. data:: last = 18

    	Last unused group

    """

    unknown = Enum.YLeaf(0, "unknown")

    environ = Enum.YLeaf(1, "environ")

    ethernet = Enum.YLeaf(2, "ethernet")

    fabric = Enum.YLeaf(3, "fabric")

    power = Enum.YLeaf(4, "power")

    software = Enum.YLeaf(5, "software")

    slice = Enum.YLeaf(6, "slice")

    cpu = Enum.YLeaf(7, "cpu")

    controller = Enum.YLeaf(8, "controller")

    sonet = Enum.YLeaf(9, "sonet")

    otn = Enum.YLeaf(10, "otn")

    sdh_controller = Enum.YLeaf(11, "sdh-controller")

    asic = Enum.YLeaf(12, "asic")

    fpd_infra = Enum.YLeaf(13, "fpd-infra")

    shelf = Enum.YLeaf(14, "shelf")

    mpa = Enum.YLeaf(15, "mpa")

    ots = Enum.YLeaf(16, "ots")

    timing = Enum.YLeaf(17, "timing")

    last = Enum.YLeaf(18, "last")


class AlarmNotificationSrc(Enum):
    """
    AlarmNotificationSrc (Enum Class)

    Alarm notification src

    .. data:: not_specified = 0

    	Notification src not specified

    .. data:: near_end = 1

    	Notification src near end

    .. data:: far_end = 2

    	Notification src far end

    """

    not_specified = Enum.YLeaf(0, "not-specified")

    near_end = Enum.YLeaf(1, "near-end")

    far_end = Enum.YLeaf(2, "far-end")


class AlarmServiceAffecting(Enum):
    """
    AlarmServiceAffecting (Enum Class)

    Alarm service affecting

    .. data:: unknown = 0

    	Unknown whether alarm severity is service

    	affecting

    .. data:: not_service_affecting = 1

    	Alarm severity is not service affecting

    .. data:: service_affecting = 2

    	Alarm severity is service affecting

    """

    unknown = Enum.YLeaf(0, "unknown")

    not_service_affecting = Enum.YLeaf(1, "not-service-affecting")

    service_affecting = Enum.YLeaf(2, "service-affecting")


class AlarmSeverity(Enum):
    """
    AlarmSeverity (Enum Class)

    Alarm severity

    .. data:: unknown = 0

    	Unknown severity level

    .. data:: not_reported = 1

    	Severity level not reported will not raise an

    	alarm

    .. data:: not_alarmed = 2

    	Severity level of info to cater to events such

    	as Performance TCAS

    .. data:: minor = 3

    	Severity level of minor fault not traffic

    	affecting

    .. data:: major = 4

    	Severity level of major fault leading to

    	service disruption

    .. data:: critical = 5

    	Severity level of critical leading to drops

    	,route loss, loss of service etc.

    .. data:: severity_last = 6

    	Last severity level

    """

    unknown = Enum.YLeaf(0, "unknown")

    not_reported = Enum.YLeaf(1, "not-reported")

    not_alarmed = Enum.YLeaf(2, "not-alarmed")

    minor = Enum.YLeaf(3, "minor")

    major = Enum.YLeaf(4, "major")

    critical = Enum.YLeaf(5, "critical")

    severity_last = Enum.YLeaf(6, "severity-last")


class AlarmStatus(Enum):
    """
    AlarmStatus (Enum Class)

    Alarm status

    .. data:: unknown = 0

    	Unknown alarm status level

    .. data:: set = 1

    	Status of active alarm that is SET by the

    	controller

    .. data:: clear = 2

    	Status of cleared alarm that is done by the

    	controller

    .. data:: suppress = 3

    	Status of suppressed alarm that is done by the

    	controller

    .. data:: last = 4

    	Last status level

    """

    unknown = Enum.YLeaf(0, "unknown")

    set = Enum.YLeaf(1, "set")

    clear = Enum.YLeaf(2, "clear")

    suppress = Enum.YLeaf(3, "suppress")

    last = Enum.YLeaf(4, "last")


class TimingBucket(Enum):
    """
    TimingBucket (Enum Class)

    Timing bucket

    .. data:: not_specified = 0

    	Bucket Type not applicable

    .. data:: fifteen_min = 1

    	Fifteen minute time bucket

    .. data:: one_day = 2

    	One day time bucket

    """

    not_specified = Enum.YLeaf(0, "not-specified")

    fifteen_min = Enum.YLeaf(1, "fifteen-min")

    one_day = Enum.YLeaf(2, "one-day")



class Alarms(Entity):
    """
    Show Alarms associated with XR
    
    .. attribute:: detail
    
    	A set of detail alarm commands
    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail>`
    
    .. attribute:: brief
    
    	A set of brief alarm commands
    	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief>`
    
    

    """

    _prefix = 'alarmgr-server-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Alarms, self).__init__()
        self._top_entity = None

        self.yang_name = "alarms"
        self.yang_parent_name = "Cisco-IOS-XR-alarmgr-server-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("detail", ("detail", Alarms.Detail)), ("brief", ("brief", Alarms.Brief))])
        self._leafs = OrderedDict()

        self.detail = Alarms.Detail()
        self.detail.parent = self
        self._children_name_map["detail"] = "detail"

        self.brief = Alarms.Brief()
        self.brief.parent = self
        self._children_name_map["brief"] = "brief"
        self._segment_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Alarms, [], name, value)


    class Detail(Entity):
        """
        A set of detail alarm commands.
        
        .. attribute:: detail_system
        
        	show detail system scope alarm related data
        	**type**\:  :py:class:`DetailSystem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem>`
        
        .. attribute:: detail_card
        
        	Show detail card scope alarm related data
        	**type**\:  :py:class:`DetailCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard>`
        
        

        """

        _prefix = 'alarmgr-server-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Alarms.Detail, self).__init__()

            self.yang_name = "detail"
            self.yang_parent_name = "alarms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("detail-system", ("detail_system", Alarms.Detail.DetailSystem)), ("detail-card", ("detail_card", Alarms.Detail.DetailCard))])
            self._leafs = OrderedDict()

            self.detail_system = Alarms.Detail.DetailSystem()
            self.detail_system.parent = self
            self._children_name_map["detail_system"] = "detail-system"

            self.detail_card = Alarms.Detail.DetailCard()
            self.detail_card.parent = self
            self._children_name_map["detail_card"] = "detail-card"
            self._segment_path = lambda: "detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Alarms.Detail, [], name, value)


        class DetailSystem(Entity):
            """
            show detail system scope alarm related data.
            
            .. attribute:: conditions
            
            	Show the Conditions present at this scope
            	**type**\:  :py:class:`Conditions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Conditions>`
            
            .. attribute:: active
            
            	Show the active alarms at this scope
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active>`
            
            .. attribute:: history
            
            	Show the history alarms at this scope
            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History>`
            
            .. attribute:: suppressed
            
            	Show the suppressed alarms at this scope
            	**type**\:  :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed>`
            
            .. attribute:: stats
            
            	Show the service statistics
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Stats>`
            
            .. attribute:: clients
            
            	Show the clients associated with this service
            	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Clients>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Detail.DetailSystem, self).__init__()

                self.yang_name = "detail-system"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("conditions", ("conditions", Alarms.Detail.DetailSystem.Conditions)), ("active", ("active", Alarms.Detail.DetailSystem.Active)), ("history", ("history", Alarms.Detail.DetailSystem.History)), ("suppressed", ("suppressed", Alarms.Detail.DetailSystem.Suppressed)), ("stats", ("stats", Alarms.Detail.DetailSystem.Stats)), ("clients", ("clients", Alarms.Detail.DetailSystem.Clients))])
                self._leafs = OrderedDict()

                self.conditions = Alarms.Detail.DetailSystem.Conditions()
                self.conditions.parent = self
                self._children_name_map["conditions"] = "conditions"

                self.active = Alarms.Detail.DetailSystem.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"

                self.history = Alarms.Detail.DetailSystem.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"

                self.suppressed = Alarms.Detail.DetailSystem.Suppressed()
                self.suppressed.parent = self
                self._children_name_map["suppressed"] = "suppressed"

                self.stats = Alarms.Detail.DetailSystem.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"

                self.clients = Alarms.Detail.DetailSystem.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._segment_path = lambda: "detail-system"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Alarms.Detail.DetailSystem, [], name, value)


            class Conditions(Entity):
                """
                Show the Conditions present at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Conditions.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Conditions, self).__init__()

                    self.yang_name = "conditions"
                    self.yang_parent_name = "detail-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Detail.DetailSystem.Conditions.AlarmInfo))])
                    self._leafs = OrderedDict()

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "conditions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Conditions, [], name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Otn>`
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:  :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Tca>`
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\: bool
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting
                    	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:  :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Conditions.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "conditions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Otn)), ("tca", ("tca", Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Tca))])
                        self._leafs = OrderedDict([
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                            ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                            ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                            ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEvent', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                        ])
                        self.description = None
                        self.location = None
                        self.aid = None
                        self.tag = None
                        self.module = None
                        self.eid = None
                        self.reporting_agent_id = None
                        self.pending_sync = None
                        self.severity = None
                        self.status = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.service_affecting = None
                        self.type = None
                        self.interface = None
                        self.alarm_name = None

                        self.otn = Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"

                        self.tca = Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Tca()
                        self.tca.parent = self
                        self._children_name_map["tca"] = "tca"
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/conditions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Conditions.AlarmInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'service_affecting', 'type', 'interface', 'alarm_name'], name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                            ])
                            self.direction = None
                            self.notification_source = None
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/conditions/alarm-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


                    class Tca(Entity):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: threshold_value
                        
                        	Alarm Threshold 
                        	**type**\: str
                        
                        	**length:** 0..20
                        
                        .. attribute:: current_value
                        
                        	Alarm Threshold
                        	**type**\: str
                        
                        	**length:** 0..20
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:  :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Tca, self).__init__()

                            self.yang_name = "tca"
                            self.yang_parent_name = "alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['str'])),
                                ('current_value', (YLeaf(YType.str, 'current-value'), ['str'])),
                                ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucket', '')])),
                            ])
                            self.threshold_value = None
                            self.current_value = None
                            self.bucket_type = None
                            self._segment_path = lambda: "tca"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/conditions/alarm-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Conditions.AlarmInfo.Tca, ['threshold_value', 'current_value', 'bucket_type'], name, value)


            class Active(Entity):
                """
                Show the active alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "detail-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Detail.DetailSystem.Active.AlarmInfo))])
                    self._leafs = OrderedDict()

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Active, [], name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn>`
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:  :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca>`
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\: bool
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting
                    	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:  :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Active.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn)), ("tca", ("tca", Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca))])
                        self._leafs = OrderedDict([
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                            ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                            ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                            ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEvent', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                        ])
                        self.description = None
                        self.location = None
                        self.aid = None
                        self.tag = None
                        self.module = None
                        self.eid = None
                        self.reporting_agent_id = None
                        self.pending_sync = None
                        self.severity = None
                        self.status = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.service_affecting = None
                        self.type = None
                        self.interface = None
                        self.alarm_name = None

                        self.otn = Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"

                        self.tca = Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca()
                        self.tca.parent = self
                        self._children_name_map["tca"] = "tca"
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Active.AlarmInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'service_affecting', 'type', 'interface', 'alarm_name'], name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                            ])
                            self.direction = None
                            self.notification_source = None
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/alarm-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


                    class Tca(Entity):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: threshold_value
                        
                        	Alarm Threshold 
                        	**type**\: str
                        
                        	**length:** 0..20
                        
                        .. attribute:: current_value
                        
                        	Alarm Threshold
                        	**type**\: str
                        
                        	**length:** 0..20
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:  :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca, self).__init__()

                            self.yang_name = "tca"
                            self.yang_parent_name = "alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['str'])),
                                ('current_value', (YLeaf(YType.str, 'current-value'), ['str'])),
                                ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucket', '')])),
                            ])
                            self.threshold_value = None
                            self.current_value = None
                            self.bucket_type = None
                            self._segment_path = lambda: "tca"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/alarm-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca, ['threshold_value', 'current_value', 'bucket_type'], name, value)


            class History(Entity):
                """
                Show the history alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "detail-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Detail.DetailSystem.History.AlarmInfo))])
                    self._leafs = OrderedDict()

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "history"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.History, [], name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo.Otn>`
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:  :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo.Tca>`
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\: bool
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting
                    	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:  :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.History.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailSystem.History.AlarmInfo.Otn)), ("tca", ("tca", Alarms.Detail.DetailSystem.History.AlarmInfo.Tca))])
                        self._leafs = OrderedDict([
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                            ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                            ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                            ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEvent', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                        ])
                        self.description = None
                        self.location = None
                        self.aid = None
                        self.tag = None
                        self.module = None
                        self.eid = None
                        self.reporting_agent_id = None
                        self.pending_sync = None
                        self.severity = None
                        self.status = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.service_affecting = None
                        self.type = None
                        self.interface = None
                        self.alarm_name = None

                        self.otn = Alarms.Detail.DetailSystem.History.AlarmInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"

                        self.tca = Alarms.Detail.DetailSystem.History.AlarmInfo.Tca()
                        self.tca.parent = self
                        self._children_name_map["tca"] = "tca"
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.History.AlarmInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'service_affecting', 'type', 'interface', 'alarm_name'], name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.History.AlarmInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                            ])
                            self.direction = None
                            self.notification_source = None
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/alarm-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.History.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


                    class Tca(Entity):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: threshold_value
                        
                        	Alarm Threshold 
                        	**type**\: str
                        
                        	**length:** 0..20
                        
                        .. attribute:: current_value
                        
                        	Alarm Threshold
                        	**type**\: str
                        
                        	**length:** 0..20
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:  :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.History.AlarmInfo.Tca, self).__init__()

                            self.yang_name = "tca"
                            self.yang_parent_name = "alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['str'])),
                                ('current_value', (YLeaf(YType.str, 'current-value'), ['str'])),
                                ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucket', '')])),
                            ])
                            self.threshold_value = None
                            self.current_value = None
                            self.bucket_type = None
                            self._segment_path = lambda: "tca"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/alarm-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.History.AlarmInfo.Tca, ['threshold_value', 'current_value', 'bucket_type'], name, value)


            class Suppressed(Entity):
                """
                Show the suppressed alarms at this scope.
                
                .. attribute:: suppressed_info
                
                	Suppressed Alarm List
                	**type**\: list of  		 :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Suppressed, self).__init__()

                    self.yang_name = "suppressed"
                    self.yang_parent_name = "detail-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("suppressed-info", ("suppressed_info", Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo))])
                    self._leafs = OrderedDict()

                    self.suppressed_info = YList(self)
                    self._segment_path = lambda: "suppressed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Suppressed, [], name, value)


                class SuppressedInfo(Entity):
                    """
                    Suppressed Alarm List
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn>`
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\: bool
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: suppressed_timestamp
                    
                    	Alarm suppressed time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting 
                    	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo, self).__init__()

                        self.yang_name = "suppressed-info"
                        self.yang_parent_name = "suppressed"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn))])
                        self._leafs = OrderedDict([
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                            ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('suppressed_time', (YLeaf(YType.str, 'suppressed-time'), ['str'])),
                            ('suppressed_timestamp', (YLeaf(YType.uint64, 'suppressed-timestamp'), ['int'])),
                            ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                        ])
                        self.description = None
                        self.location = None
                        self.aid = None
                        self.tag = None
                        self.module = None
                        self.eid = None
                        self.reporting_agent_id = None
                        self.pending_sync = None
                        self.severity = None
                        self.status = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.suppressed_time = None
                        self.suppressed_timestamp = None
                        self.service_affecting = None
                        self.interface = None
                        self.alarm_name = None

                        self.otn = Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"
                        self._segment_path = lambda: "suppressed-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/suppressed/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'suppressed_time', 'suppressed_timestamp', 'service_affecting', 'interface', 'alarm_name'], name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "suppressed-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                            ])
                            self.direction = None
                            self.notification_source = None
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/suppressed/suppressed-info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn, ['direction', 'notification_source'], name, value)


            class Stats(Entity):
                """
                Show the service statistics.
                
                .. attribute:: reported
                
                	Alarms that were in all reported to this Alarm Mgr
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: dropped
                
                	Alarms that we couldn't keep track due to some error or other
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: active
                
                	Alarms that are currently in the active state
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: history
                
                	Alarms that are cleared. This one is counted over a long period of time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: suppressed
                
                	Alarms that are in suppressed state
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sysadmin_active
                
                	Alarms that are currently in the active state(sysadmin plane)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sysadmin_history
                
                	Alarms that are cleared in sysadmin plane. This one is counted over a long period of time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sysadmin_suppressed
                
                	Alarms that are suppressed in sysadmin plane
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: dropped_invalid_aid
                
                	Alarms dropped due to invalid aid
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_insuff_mem
                
                	Alarms dropped due to insufficient memory
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_db_error
                
                	Alarms dropped due to db error
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_clear_without_set
                
                	Alarms dropped clear without set
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_duplicate
                
                	Alarms dropped which were duplicate
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_hit
                
                	Total alarms which had the cache hit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_miss
                
                	Total alarms which had the cache miss
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "detail-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('reported', (YLeaf(YType.uint64, 'reported'), ['int'])),
                        ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                        ('active', (YLeaf(YType.uint64, 'active'), ['int'])),
                        ('history', (YLeaf(YType.uint64, 'history'), ['int'])),
                        ('suppressed', (YLeaf(YType.uint64, 'suppressed'), ['int'])),
                        ('sysadmin_active', (YLeaf(YType.uint64, 'sysadmin-active'), ['int'])),
                        ('sysadmin_history', (YLeaf(YType.uint64, 'sysadmin-history'), ['int'])),
                        ('sysadmin_suppressed', (YLeaf(YType.uint64, 'sysadmin-suppressed'), ['int'])),
                        ('dropped_invalid_aid', (YLeaf(YType.uint32, 'dropped-invalid-aid'), ['int'])),
                        ('dropped_insuff_mem', (YLeaf(YType.uint32, 'dropped-insuff-mem'), ['int'])),
                        ('dropped_db_error', (YLeaf(YType.uint32, 'dropped-db-error'), ['int'])),
                        ('dropped_clear_without_set', (YLeaf(YType.uint32, 'dropped-clear-without-set'), ['int'])),
                        ('dropped_duplicate', (YLeaf(YType.uint32, 'dropped-duplicate'), ['int'])),
                        ('cache_hit', (YLeaf(YType.uint32, 'cache-hit'), ['int'])),
                        ('cache_miss', (YLeaf(YType.uint32, 'cache-miss'), ['int'])),
                    ])
                    self.reported = None
                    self.dropped = None
                    self.active = None
                    self.history = None
                    self.suppressed = None
                    self.sysadmin_active = None
                    self.sysadmin_history = None
                    self.sysadmin_suppressed = None
                    self.dropped_invalid_aid = None
                    self.dropped_insuff_mem = None
                    self.dropped_db_error = None
                    self.dropped_clear_without_set = None
                    self.dropped_duplicate = None
                    self.cache_hit = None
                    self.cache_miss = None
                    self._segment_path = lambda: "stats"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Stats, ['reported', 'dropped', 'active', 'history', 'suppressed', 'sysadmin_active', 'sysadmin_history', 'sysadmin_suppressed', 'dropped_invalid_aid', 'dropped_insuff_mem', 'dropped_db_error', 'dropped_clear_without_set', 'dropped_duplicate', 'cache_hit', 'cache_miss'], name, value)


            class Clients(Entity):
                """
                Show the clients associated with this service.
                
                .. attribute:: client_info
                
                	Client List
                	**type**\: list of  		 :py:class:`ClientInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Clients.ClientInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "detail-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client-info", ("client_info", Alarms.Detail.DetailSystem.Clients.ClientInfo))])
                    self._leafs = OrderedDict()

                    self.client_info = YList(self)
                    self._segment_path = lambda: "clients"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Clients, [], name, value)


                class ClientInfo(Entity):
                    """
                    Client List
                    
                    .. attribute:: name
                    
                    	Alarm client
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: id
                    
                    	Alarms agent id of the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: location
                    
                    	The location of this client
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: handle
                    
                    	The client handle through which interface
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: state
                    
                    	The current state of the client
                    	**type**\:  :py:class:`AlarmClientState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientState>`
                    
                    .. attribute:: type
                    
                    	The type of the client
                    	**type**\:  :py:class:`AlarmClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClient>`
                    
                    .. attribute:: filter_disp
                    
                    	The current subscription status of the client
                    	**type**\: bool
                    
                    .. attribute:: subscriber_id
                    
                    	Alarms agent subscriber id of the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: filter_severity
                    
                    	The filter used for alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: filter_state
                    
                    	The filter used for alarm bi\-state state+
                    	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: filter_group
                    
                    	The filter used for alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: connect_count
                    
                    	Number of times the agent connected to the alarm mgr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connect_timestamp
                    
                    	Agent connect timestamp
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: get_count
                    
                    	Number of times the agent queried for alarms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscribe_count
                    
                    	Number of times the agent subscribed for alarms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: report_count
                    
                    	Number of times the agent reported alarms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Clients.ClientInfo, self).__init__()

                        self.yang_name = "client-info"
                        self.yang_parent_name = "clients"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('handle', (YLeaf(YType.str, 'handle'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClientState', '')])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClient', '')])),
                            ('filter_disp', (YLeaf(YType.boolean, 'filter-disp'), ['bool'])),
                            ('subscriber_id', (YLeaf(YType.uint32, 'subscriber-id'), ['int'])),
                            ('filter_severity', (YLeaf(YType.enumeration, 'filter-severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('filter_state', (YLeaf(YType.enumeration, 'filter-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                            ('filter_group', (YLeaf(YType.enumeration, 'filter-group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('connect_count', (YLeaf(YType.uint32, 'connect-count'), ['int'])),
                            ('connect_timestamp', (YLeaf(YType.str, 'connect-timestamp'), ['str'])),
                            ('get_count', (YLeaf(YType.uint32, 'get-count'), ['int'])),
                            ('subscribe_count', (YLeaf(YType.uint32, 'subscribe-count'), ['int'])),
                            ('report_count', (YLeaf(YType.uint32, 'report-count'), ['int'])),
                        ])
                        self.name = None
                        self.id = None
                        self.location = None
                        self.handle = None
                        self.state = None
                        self.type = None
                        self.filter_disp = None
                        self.subscriber_id = None
                        self.filter_severity = None
                        self.filter_state = None
                        self.filter_group = None
                        self.connect_count = None
                        self.connect_timestamp = None
                        self.get_count = None
                        self.subscribe_count = None
                        self.report_count = None
                        self._segment_path = lambda: "client-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/clients/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Clients.ClientInfo, ['name', 'id', 'location', 'handle', 'state', 'type', 'filter_disp', 'subscriber_id', 'filter_severity', 'filter_state', 'filter_group', 'connect_count', 'connect_timestamp', 'get_count', 'subscribe_count', 'report_count'], name, value)


        class DetailCard(Entity):
            """
            Show detail card scope alarm related data.
            
            .. attribute:: detail_locations
            
            	Table of DetailLocation
            	**type**\:  :py:class:`DetailLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Detail.DetailCard, self).__init__()

                self.yang_name = "detail-card"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail-locations", ("detail_locations", Alarms.Detail.DetailCard.DetailLocations))])
                self._leafs = OrderedDict()

                self.detail_locations = Alarms.Detail.DetailCard.DetailLocations()
                self.detail_locations.parent = self
                self._children_name_map["detail_locations"] = "detail-locations"
                self._segment_path = lambda: "detail-card"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Alarms.Detail.DetailCard, [], name, value)


            class DetailLocations(Entity):
                """
                Table of DetailLocation
                
                .. attribute:: detail_location
                
                	Specify a card location for alarms
                	**type**\: list of  		 :py:class:`DetailLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailCard.DetailLocations, self).__init__()

                    self.yang_name = "detail-locations"
                    self.yang_parent_name = "detail-card"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("detail-location", ("detail_location", Alarms.Detail.DetailCard.DetailLocations.DetailLocation))])
                    self._leafs = OrderedDict()

                    self.detail_location = YList(self)
                    self._segment_path = lambda: "detail-locations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-card/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations, [], name, value)


                class DetailLocation(Entity):
                    """
                    Specify a card location for alarms.
                    
                    .. attribute:: node_id  (key)
                    
                    	NodeID of the Location
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: conditions
                    
                    	Show the conditions present at this scope
                    	**type**\:  :py:class:`Conditions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions>`
                    
                    .. attribute:: active
                    
                    	Show the active alarms at this scope
                    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active>`
                    
                    .. attribute:: history
                    
                    	Show the history alarms at this scope
                    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History>`
                    
                    .. attribute:: suppressed
                    
                    	Show the suppressed alarms at this scope
                    	**type**\:  :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed>`
                    
                    .. attribute:: stats
                    
                    	Show the service statistics
                    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats>`
                    
                    .. attribute:: clients
                    
                    	Show the clients associated with this service
                    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation, self).__init__()

                        self.yang_name = "detail-location"
                        self.yang_parent_name = "detail-locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_id']
                        self._child_classes = OrderedDict([("conditions", ("conditions", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions)), ("active", ("active", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active)), ("history", ("history", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History)), ("suppressed", ("suppressed", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed)), ("stats", ("stats", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats)), ("clients", ("clients", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients))])
                        self._leafs = OrderedDict([
                            ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                        ])
                        self.node_id = None

                        self.conditions = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions()
                        self.conditions.parent = self
                        self._children_name_map["conditions"] = "conditions"

                        self.active = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"

                        self.history = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"

                        self.suppressed = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed()
                        self.suppressed.parent = self
                        self._children_name_map["suppressed"] = "suppressed"

                        self.stats = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"

                        self.clients = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                        self._segment_path = lambda: "detail-location" + "[node-id='" + str(self.node_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-card/detail-locations/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation, ['node_id'], name, value)


                    class Conditions(Entity):
                        """
                        Show the conditions present at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions, self).__init__()

                            self.yang_name = "conditions"
                            self.yang_parent_name = "detail-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo))])
                            self._leafs = OrderedDict()

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "conditions"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions, [], name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Otn>`
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:  :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Tca>`
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\: bool
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting
                            	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:  :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Otn)), ("tca", ("tca", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Tca))])
                                self._leafs = OrderedDict([
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('module', (YLeaf(YType.str, 'module'), ['str'])),
                                    ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                                    ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                                    ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                                    ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                                    ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEvent', '')])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                                ])
                                self.description = None
                                self.location = None
                                self.aid = None
                                self.tag = None
                                self.module = None
                                self.eid = None
                                self.reporting_agent_id = None
                                self.pending_sync = None
                                self.severity = None
                                self.status = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.service_affecting = None
                                self.type = None
                                self.interface = None
                                self.alarm_name = None

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"

                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'service_affecting', 'type', 'interface', 'alarm_name'], name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "alarm-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                        ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                                    ])
                                    self.direction = None
                                    self.notification_source = None
                                    self._segment_path = lambda: "otn"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


                            class Tca(Entity):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: threshold_value
                                
                                	Alarm Threshold 
                                	**type**\: str
                                
                                	**length:** 0..20
                                
                                .. attribute:: current_value
                                
                                	Alarm Threshold
                                	**type**\: str
                                
                                	**length:** 0..20
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:  :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Tca, self).__init__()

                                    self.yang_name = "tca"
                                    self.yang_parent_name = "alarm-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['str'])),
                                        ('current_value', (YLeaf(YType.str, 'current-value'), ['str'])),
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucket', '')])),
                                    ])
                                    self.threshold_value = None
                                    self.current_value = None
                                    self.bucket_type = None
                                    self._segment_path = lambda: "tca"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Conditions.AlarmInfo.Tca, ['threshold_value', 'current_value', 'bucket_type'], name, value)


                    class Active(Entity):
                        """
                        Show the active alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active, self).__init__()

                            self.yang_name = "active"
                            self.yang_parent_name = "detail-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo))])
                            self._leafs = OrderedDict()

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "active"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active, [], name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn>`
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:  :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca>`
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\: bool
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting
                            	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:  :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "active"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn)), ("tca", ("tca", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca))])
                                self._leafs = OrderedDict([
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('module', (YLeaf(YType.str, 'module'), ['str'])),
                                    ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                                    ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                                    ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                                    ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                                    ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEvent', '')])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                                ])
                                self.description = None
                                self.location = None
                                self.aid = None
                                self.tag = None
                                self.module = None
                                self.eid = None
                                self.reporting_agent_id = None
                                self.pending_sync = None
                                self.severity = None
                                self.status = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.service_affecting = None
                                self.type = None
                                self.interface = None
                                self.alarm_name = None

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"

                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'service_affecting', 'type', 'interface', 'alarm_name'], name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "alarm-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                        ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                                    ])
                                    self.direction = None
                                    self.notification_source = None
                                    self._segment_path = lambda: "otn"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


                            class Tca(Entity):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: threshold_value
                                
                                	Alarm Threshold 
                                	**type**\: str
                                
                                	**length:** 0..20
                                
                                .. attribute:: current_value
                                
                                	Alarm Threshold
                                	**type**\: str
                                
                                	**length:** 0..20
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:  :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca, self).__init__()

                                    self.yang_name = "tca"
                                    self.yang_parent_name = "alarm-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['str'])),
                                        ('current_value', (YLeaf(YType.str, 'current-value'), ['str'])),
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucket', '')])),
                                    ])
                                    self.threshold_value = None
                                    self.current_value = None
                                    self.bucket_type = None
                                    self._segment_path = lambda: "tca"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca, ['threshold_value', 'current_value', 'bucket_type'], name, value)


                    class History(Entity):
                        """
                        Show the history alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "detail-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo))])
                            self._leafs = OrderedDict()

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "history"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History, [], name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn>`
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:  :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca>`
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\: bool
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting
                            	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:  :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "history"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn)), ("tca", ("tca", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca))])
                                self._leafs = OrderedDict([
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('module', (YLeaf(YType.str, 'module'), ['str'])),
                                    ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                                    ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                                    ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                                    ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                                    ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmEvent', '')])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                                ])
                                self.description = None
                                self.location = None
                                self.aid = None
                                self.tag = None
                                self.module = None
                                self.eid = None
                                self.reporting_agent_id = None
                                self.pending_sync = None
                                self.severity = None
                                self.status = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.service_affecting = None
                                self.type = None
                                self.interface = None
                                self.alarm_name = None

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"

                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'service_affecting', 'type', 'interface', 'alarm_name'], name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "alarm-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                        ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                                    ])
                                    self.direction = None
                                    self.notification_source = None
                                    self._segment_path = lambda: "otn"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


                            class Tca(Entity):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: threshold_value
                                
                                	Alarm Threshold 
                                	**type**\: str
                                
                                	**length:** 0..20
                                
                                .. attribute:: current_value
                                
                                	Alarm Threshold
                                	**type**\: str
                                
                                	**length:** 0..20
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:  :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca, self).__init__()

                                    self.yang_name = "tca"
                                    self.yang_parent_name = "alarm-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('threshold_value', (YLeaf(YType.str, 'threshold-value'), ['str'])),
                                        ('current_value', (YLeaf(YType.str, 'current-value'), ['str'])),
                                        ('bucket_type', (YLeaf(YType.enumeration, 'bucket-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'TimingBucket', '')])),
                                    ])
                                    self.threshold_value = None
                                    self.current_value = None
                                    self.bucket_type = None
                                    self._segment_path = lambda: "tca"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca, ['threshold_value', 'current_value', 'bucket_type'], name, value)


                    class Suppressed(Entity):
                        """
                        Show the suppressed alarms at this scope.
                        
                        .. attribute:: suppressed_info
                        
                        	Suppressed Alarm List
                        	**type**\: list of  		 :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed, self).__init__()

                            self.yang_name = "suppressed"
                            self.yang_parent_name = "detail-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("suppressed-info", ("suppressed_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo))])
                            self._leafs = OrderedDict()

                            self.suppressed_info = YList(self)
                            self._segment_path = lambda: "suppressed"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed, [], name, value)


                        class SuppressedInfo(Entity):
                            """
                            Suppressed Alarm List
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn>`
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\: bool
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: suppressed_time
                            
                            	Alarm suppressed time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: suppressed_timestamp
                            
                            	Alarm suppressed time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting 
                            	**type**\:  :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo, self).__init__()

                                self.yang_name = "suppressed-info"
                                self.yang_parent_name = "suppressed"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("otn", ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn))])
                                self._leafs = OrderedDict([
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                                    ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                    ('module', (YLeaf(YType.str, 'module'), ['str'])),
                                    ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                                    ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting-agent-id'), ['int'])),
                                    ('pending_sync', (YLeaf(YType.boolean, 'pending-sync'), ['bool'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('suppressed_time', (YLeaf(YType.str, 'suppressed-time'), ['str'])),
                                    ('suppressed_timestamp', (YLeaf(YType.uint64, 'suppressed-timestamp'), ['int'])),
                                    ('service_affecting', (YLeaf(YType.enumeration, 'service-affecting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmServiceAffecting', '')])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('alarm_name', (YLeaf(YType.str, 'alarm-name'), ['str'])),
                                ])
                                self.description = None
                                self.location = None
                                self.aid = None
                                self.tag = None
                                self.module = None
                                self.eid = None
                                self.reporting_agent_id = None
                                self.pending_sync = None
                                self.severity = None
                                self.status = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.suppressed_time = None
                                self.suppressed_timestamp = None
                                self.service_affecting = None
                                self.interface = None
                                self.alarm_name = None

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                                self._segment_path = lambda: "suppressed-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo, ['description', 'location', 'aid', 'tag', 'module', 'eid', 'reporting_agent_id', 'pending_sync', 'severity', 'status', 'group', 'set_time', 'set_timestamp', 'suppressed_time', 'suppressed_timestamp', 'service_affecting', 'interface', 'alarm_name'], name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:  :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:  :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "suppressed-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmDirection', '')])),
                                        ('notification_source', (YLeaf(YType.enumeration, 'notification-source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmNotificationSrc', '')])),
                                    ])
                                    self.direction = None
                                    self.notification_source = None
                                    self._segment_path = lambda: "otn"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn, ['direction', 'notification_source'], name, value)


                    class Stats(Entity):
                        """
                        Show the service statistics.
                        
                        .. attribute:: reported
                        
                        	Alarms that were in all reported to this Alarm Mgr
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped
                        
                        	Alarms that we couldn't keep track due to some error or other
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: active
                        
                        	Alarms that are currently in the active state
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: history
                        
                        	Alarms that are cleared. This one is counted over a long period of time
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: suppressed
                        
                        	Alarms that are in suppressed state
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sysadmin_active
                        
                        	Alarms that are currently in the active state(sysadmin plane)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sysadmin_history
                        
                        	Alarms that are cleared in sysadmin plane. This one is counted over a long period of time
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sysadmin_suppressed
                        
                        	Alarms that are suppressed in sysadmin plane
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_invalid_aid
                        
                        	Alarms dropped due to invalid aid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_insuff_mem
                        
                        	Alarms dropped due to insufficient memory
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_db_error
                        
                        	Alarms dropped due to db error
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_clear_without_set
                        
                        	Alarms dropped clear without set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_duplicate
                        
                        	Alarms dropped which were duplicate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cache_hit
                        
                        	Total alarms which had the cache hit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cache_miss
                        
                        	Total alarms which had the cache miss
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "detail-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reported', (YLeaf(YType.uint64, 'reported'), ['int'])),
                                ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                                ('active', (YLeaf(YType.uint64, 'active'), ['int'])),
                                ('history', (YLeaf(YType.uint64, 'history'), ['int'])),
                                ('suppressed', (YLeaf(YType.uint64, 'suppressed'), ['int'])),
                                ('sysadmin_active', (YLeaf(YType.uint64, 'sysadmin-active'), ['int'])),
                                ('sysadmin_history', (YLeaf(YType.uint64, 'sysadmin-history'), ['int'])),
                                ('sysadmin_suppressed', (YLeaf(YType.uint64, 'sysadmin-suppressed'), ['int'])),
                                ('dropped_invalid_aid', (YLeaf(YType.uint32, 'dropped-invalid-aid'), ['int'])),
                                ('dropped_insuff_mem', (YLeaf(YType.uint32, 'dropped-insuff-mem'), ['int'])),
                                ('dropped_db_error', (YLeaf(YType.uint32, 'dropped-db-error'), ['int'])),
                                ('dropped_clear_without_set', (YLeaf(YType.uint32, 'dropped-clear-without-set'), ['int'])),
                                ('dropped_duplicate', (YLeaf(YType.uint32, 'dropped-duplicate'), ['int'])),
                                ('cache_hit', (YLeaf(YType.uint32, 'cache-hit'), ['int'])),
                                ('cache_miss', (YLeaf(YType.uint32, 'cache-miss'), ['int'])),
                            ])
                            self.reported = None
                            self.dropped = None
                            self.active = None
                            self.history = None
                            self.suppressed = None
                            self.sysadmin_active = None
                            self.sysadmin_history = None
                            self.sysadmin_suppressed = None
                            self.dropped_invalid_aid = None
                            self.dropped_insuff_mem = None
                            self.dropped_db_error = None
                            self.dropped_clear_without_set = None
                            self.dropped_duplicate = None
                            self.cache_hit = None
                            self.cache_miss = None
                            self._segment_path = lambda: "stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats, ['reported', 'dropped', 'active', 'history', 'suppressed', 'sysadmin_active', 'sysadmin_history', 'sysadmin_suppressed', 'dropped_invalid_aid', 'dropped_insuff_mem', 'dropped_db_error', 'dropped_clear_without_set', 'dropped_duplicate', 'cache_hit', 'cache_miss'], name, value)


                    class Clients(Entity):
                        """
                        Show the clients associated with this
                        service.
                        
                        .. attribute:: client_info
                        
                        	Client List
                        	**type**\: list of  		 :py:class:`ClientInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "detail-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("client-info", ("client_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo))])
                            self._leafs = OrderedDict()

                            self.client_info = YList(self)
                            self._segment_path = lambda: "clients"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients, [], name, value)


                        class ClientInfo(Entity):
                            """
                            Client List
                            
                            .. attribute:: name
                            
                            	Alarm client
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: id
                            
                            	Alarms agent id of the client
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: location
                            
                            	The location of this client
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: handle
                            
                            	The client handle through which interface
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: state
                            
                            	The current state of the client
                            	**type**\:  :py:class:`AlarmClientState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientState>`
                            
                            .. attribute:: type
                            
                            	The type of the client
                            	**type**\:  :py:class:`AlarmClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClient>`
                            
                            .. attribute:: filter_disp
                            
                            	The current subscription status of the client
                            	**type**\: bool
                            
                            .. attribute:: subscriber_id
                            
                            	Alarms agent subscriber id of the client
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: filter_severity
                            
                            	The filter used for alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: filter_state
                            
                            	The filter used for alarm bi\-state state+
                            	**type**\:  :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: filter_group
                            
                            	The filter used for alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: connect_count
                            
                            	Number of times the agent connected to the alarm mgr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connect_timestamp
                            
                            	Agent connect timestamp
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: get_count
                            
                            	Number of times the agent queried for alarms
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscribe_count
                            
                            	Number of times the agent subscribed for alarms
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: report_count
                            
                            	Number of times the agent reported alarms
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo, self).__init__()

                                self.yang_name = "client-info"
                                self.yang_parent_name = "clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('handle', (YLeaf(YType.str, 'handle'), ['str'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClientState', '')])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmClient', '')])),
                                    ('filter_disp', (YLeaf(YType.boolean, 'filter-disp'), ['bool'])),
                                    ('subscriber_id', (YLeaf(YType.uint32, 'subscriber-id'), ['int'])),
                                    ('filter_severity', (YLeaf(YType.enumeration, 'filter-severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('filter_state', (YLeaf(YType.enumeration, 'filter-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmStatus', '')])),
                                    ('filter_group', (YLeaf(YType.enumeration, 'filter-group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('connect_count', (YLeaf(YType.uint32, 'connect-count'), ['int'])),
                                    ('connect_timestamp', (YLeaf(YType.str, 'connect-timestamp'), ['str'])),
                                    ('get_count', (YLeaf(YType.uint32, 'get-count'), ['int'])),
                                    ('subscribe_count', (YLeaf(YType.uint32, 'subscribe-count'), ['int'])),
                                    ('report_count', (YLeaf(YType.uint32, 'report-count'), ['int'])),
                                ])
                                self.name = None
                                self.id = None
                                self.location = None
                                self.handle = None
                                self.state = None
                                self.type = None
                                self.filter_disp = None
                                self.subscriber_id = None
                                self.filter_severity = None
                                self.filter_state = None
                                self.filter_group = None
                                self.connect_count = None
                                self.connect_timestamp = None
                                self.get_count = None
                                self.subscribe_count = None
                                self.report_count = None
                                self._segment_path = lambda: "client-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo, ['name', 'id', 'location', 'handle', 'state', 'type', 'filter_disp', 'subscriber_id', 'filter_severity', 'filter_state', 'filter_group', 'connect_count', 'connect_timestamp', 'get_count', 'subscribe_count', 'report_count'], name, value)


    class Brief(Entity):
        """
        A set of brief alarm commands.
        
        .. attribute:: brief_card
        
        	Show brief card scope alarm related data
        	**type**\:  :py:class:`BriefCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard>`
        
        .. attribute:: brief_system
        
        	Show brief system scope alarm related data
        	**type**\:  :py:class:`BriefSystem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem>`
        
        

        """

        _prefix = 'alarmgr-server-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Alarms.Brief, self).__init__()

            self.yang_name = "brief"
            self.yang_parent_name = "alarms"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("brief-card", ("brief_card", Alarms.Brief.BriefCard)), ("brief-system", ("brief_system", Alarms.Brief.BriefSystem))])
            self._leafs = OrderedDict()

            self.brief_card = Alarms.Brief.BriefCard()
            self.brief_card.parent = self
            self._children_name_map["brief_card"] = "brief-card"

            self.brief_system = Alarms.Brief.BriefSystem()
            self.brief_system.parent = self
            self._children_name_map["brief_system"] = "brief-system"
            self._segment_path = lambda: "brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Alarms.Brief, [], name, value)


        class BriefCard(Entity):
            """
            Show brief card scope alarm related data.
            
            .. attribute:: brief_locations
            
            	Table of BriefLocation
            	**type**\:  :py:class:`BriefLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Brief.BriefCard, self).__init__()

                self.yang_name = "brief-card"
                self.yang_parent_name = "brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("brief-locations", ("brief_locations", Alarms.Brief.BriefCard.BriefLocations))])
                self._leafs = OrderedDict()

                self.brief_locations = Alarms.Brief.BriefCard.BriefLocations()
                self.brief_locations.parent = self
                self._children_name_map["brief_locations"] = "brief-locations"
                self._segment_path = lambda: "brief-card"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Alarms.Brief.BriefCard, [], name, value)


            class BriefLocations(Entity):
                """
                Table of BriefLocation
                
                .. attribute:: brief_location
                
                	Specify a card location for alarms
                	**type**\: list of  		 :py:class:`BriefLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefCard.BriefLocations, self).__init__()

                    self.yang_name = "brief-locations"
                    self.yang_parent_name = "brief-card"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("brief-location", ("brief_location", Alarms.Brief.BriefCard.BriefLocations.BriefLocation))])
                    self._leafs = OrderedDict()

                    self.brief_location = YList(self)
                    self._segment_path = lambda: "brief-locations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-card/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations, [], name, value)


                class BriefLocation(Entity):
                    """
                    Specify a card location for alarms.
                    
                    .. attribute:: node_id  (key)
                    
                    	NodeID of the Location
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: conditions
                    
                    	Show the conditions present at this scope
                    	**type**\:  :py:class:`Conditions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions>`
                    
                    .. attribute:: active
                    
                    	Show the active alarms at this scope
                    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active>`
                    
                    .. attribute:: history
                    
                    	Show the history alarms at this scope
                    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History>`
                    
                    .. attribute:: suppressed
                    
                    	Show the suppressed alarms at this scope
                    	**type**\:  :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation, self).__init__()

                        self.yang_name = "brief-location"
                        self.yang_parent_name = "brief-locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_id']
                        self._child_classes = OrderedDict([("conditions", ("conditions", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions)), ("active", ("active", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active)), ("history", ("history", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History)), ("suppressed", ("suppressed", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed))])
                        self._leafs = OrderedDict([
                            ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                        ])
                        self.node_id = None

                        self.conditions = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions()
                        self.conditions.parent = self
                        self._children_name_map["conditions"] = "conditions"

                        self.active = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"

                        self.history = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"

                        self.suppressed = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed()
                        self.suppressed.parent = self
                        self._children_name_map["suppressed"] = "suppressed"
                        self._segment_path = lambda: "brief-location" + "[node-id='" + str(self.node_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-card/brief-locations/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation, ['node_id'], name, value)


                    class Conditions(Entity):
                        """
                        Show the conditions present at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions, self).__init__()

                            self.yang_name = "conditions"
                            self.yang_parent_name = "brief-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions.AlarmInfo))])
                            self._leafs = OrderedDict()

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "conditions"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions, [], name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                                    ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.location = None
                                self.severity = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Conditions.AlarmInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'description'], name, value)


                    class Active(Entity):
                        """
                        Show the active alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active, self).__init__()

                            self.yang_name = "active"
                            self.yang_parent_name = "brief-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo))])
                            self._leafs = OrderedDict()

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "active"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active, [], name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "active"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                                    ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.location = None
                                self.severity = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'description'], name, value)


                    class History(Entity):
                        """
                        Show the history alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "brief-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo))])
                            self._leafs = OrderedDict()

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "history"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History, [], name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "history"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                                    ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.location = None
                                self.severity = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self._segment_path = lambda: "alarm-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'description'], name, value)


                    class Suppressed(Entity):
                        """
                        Show the suppressed alarms at this scope.
                        
                        .. attribute:: suppressed_info
                        
                        	Suppressed Alarm List
                        	**type**\: list of  		 :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed, self).__init__()

                            self.yang_name = "suppressed"
                            self.yang_parent_name = "brief-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("suppressed-info", ("suppressed_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo))])
                            self._leafs = OrderedDict()

                            self.suppressed_info = YList(self)
                            self._segment_path = lambda: "suppressed"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed, [], name, value)


                        class SuppressedInfo(Entity):
                            """
                            Suppressed Alarm List
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: suppressed_time
                            
                            	Alarm suppressed time
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: suppressed_timestamp
                            
                            	Alarm suppressed time(timestamp format)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo, self).__init__()

                                self.yang_name = "suppressed-info"
                                self.yang_parent_name = "suppressed"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                                    ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                                    ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                                    ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                                    ('suppressed_time', (YLeaf(YType.str, 'suppressed-time'), ['str'])),
                                    ('suppressed_timestamp', (YLeaf(YType.uint64, 'suppressed-timestamp'), ['int'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.location = None
                                self.severity = None
                                self.group = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.suppressed_time = None
                                self.suppressed_timestamp = None
                                self.description = None
                                self._segment_path = lambda: "suppressed-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'suppressed_time', 'suppressed_timestamp', 'description'], name, value)


        class BriefSystem(Entity):
            """
            Show brief system scope alarm related data.
            
            .. attribute:: conditions
            
            	Show the conditions present at this scope
            	**type**\:  :py:class:`Conditions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Conditions>`
            
            .. attribute:: active
            
            	Show the active alarms at this scope
            	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Active>`
            
            .. attribute:: history
            
            	Show the history alarms at this scope
            	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.History>`
            
            .. attribute:: suppressed
            
            	Show the suppressed alarms at this scope
            	**type**\:  :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Suppressed>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Brief.BriefSystem, self).__init__()

                self.yang_name = "brief-system"
                self.yang_parent_name = "brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("conditions", ("conditions", Alarms.Brief.BriefSystem.Conditions)), ("active", ("active", Alarms.Brief.BriefSystem.Active)), ("history", ("history", Alarms.Brief.BriefSystem.History)), ("suppressed", ("suppressed", Alarms.Brief.BriefSystem.Suppressed))])
                self._leafs = OrderedDict()

                self.conditions = Alarms.Brief.BriefSystem.Conditions()
                self.conditions.parent = self
                self._children_name_map["conditions"] = "conditions"

                self.active = Alarms.Brief.BriefSystem.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"

                self.history = Alarms.Brief.BriefSystem.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"

                self.suppressed = Alarms.Brief.BriefSystem.Suppressed()
                self.suppressed.parent = self
                self._children_name_map["suppressed"] = "suppressed"
                self._segment_path = lambda: "brief-system"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Alarms.Brief.BriefSystem, [], name, value)


            class Conditions(Entity):
                """
                Show the conditions present at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Conditions.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.Conditions, self).__init__()

                    self.yang_name = "conditions"
                    self.yang_parent_name = "brief-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Brief.BriefSystem.Conditions.AlarmInfo))])
                    self._leafs = OrderedDict()

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "conditions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.Conditions, [], name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.Conditions.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "conditions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                            ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ])
                        self.location = None
                        self.severity = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/conditions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.Conditions.AlarmInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'description'], name, value)


            class Active(Entity):
                """
                Show the active alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Active.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "brief-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Brief.BriefSystem.Active.AlarmInfo))])
                    self._leafs = OrderedDict()

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.Active, [], name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.Active.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "active"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                            ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ])
                        self.location = None
                        self.severity = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/active/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.Active.AlarmInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'description'], name, value)


            class History(Entity):
                """
                Show the history alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of  		 :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.History.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "brief-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Alarms.Brief.BriefSystem.History.AlarmInfo))])
                    self._leafs = OrderedDict()

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "history"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.History, [], name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.History.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('clear_time', (YLeaf(YType.str, 'clear-time'), ['str'])),
                            ('clear_timestamp', (YLeaf(YType.uint64, 'clear-timestamp'), ['int'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ])
                        self.location = None
                        self.severity = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/history/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.History.AlarmInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'clear_time', 'clear_timestamp', 'description'], name, value)


            class Suppressed(Entity):
                """
                Show the suppressed alarms at this scope.
                
                .. attribute:: suppressed_info
                
                	Suppressed Alarm List
                	**type**\: list of  		 :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.Suppressed, self).__init__()

                    self.yang_name = "suppressed"
                    self.yang_parent_name = "brief-system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("suppressed-info", ("suppressed_info", Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo))])
                    self._leafs = OrderedDict()

                    self.suppressed_info = YList(self)
                    self._segment_path = lambda: "suppressed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.Suppressed, [], name, value)


                class SuppressedInfo(Entity):
                    """
                    Suppressed Alarm List
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\: str
                    
                    	**length:** 0..128
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:  :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: suppressed_timestamp
                    
                    	Alarm suppressed time(timestamp format)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo, self).__init__()

                        self.yang_name = "suppressed-info"
                        self.yang_parent_name = "suppressed"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmSeverity', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper', 'AlarmGroups', '')])),
                            ('set_time', (YLeaf(YType.str, 'set-time'), ['str'])),
                            ('set_timestamp', (YLeaf(YType.uint64, 'set-timestamp'), ['int'])),
                            ('suppressed_time', (YLeaf(YType.str, 'suppressed-time'), ['str'])),
                            ('suppressed_timestamp', (YLeaf(YType.uint64, 'suppressed-timestamp'), ['int'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ])
                        self.location = None
                        self.severity = None
                        self.group = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.suppressed_time = None
                        self.suppressed_timestamp = None
                        self.description = None
                        self._segment_path = lambda: "suppressed-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/suppressed/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo, ['location', 'severity', 'group', 'set_time', 'set_timestamp', 'suppressed_time', 'suppressed_timestamp', 'description'], name, value)

    def clone_ptr(self):
        self._top_entity = Alarms()
        return self._top_entity

