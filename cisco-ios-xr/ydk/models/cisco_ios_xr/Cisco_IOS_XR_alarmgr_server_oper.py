""" Cisco_IOS_XR_alarmgr_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR alarmgr\-server package operational data.

This module contains definitions
for the following management objects\:
  alarms\: Show Alarms associated with XR

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AlarmClient(Enum):
    """
    AlarmClient

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
    AlarmClientState

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
    AlarmDirection

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
    AlarmEvent

    Alarm event

    .. data:: default = 0

    	Default Alarm Event Type

    .. data:: notification = 1

    	Alarm Notifcation Event Type

    .. data:: last = 2

    	Last Event Type

    """

    default = Enum.YLeaf(0, "default")

    notification = Enum.YLeaf(1, "notification")

    last = Enum.YLeaf(2, "last")


class AlarmGroups(Enum):
    """
    AlarmGroups

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

    .. data:: last = 17

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

    last = Enum.YLeaf(17, "last")


class AlarmNotificationSrc(Enum):
    """
    AlarmNotificationSrc

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
    AlarmServiceAffecting

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
    AlarmSeverity

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
    AlarmStatus

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
    TimingBucket

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
    
    .. attribute:: brief
    
    	A set of brief alarm commands
    	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief>`
    
    .. attribute:: detail
    
    	A set of detail alarm commands
    	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail>`
    
    

    """

    _prefix = 'alarmgr-server-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Alarms, self).__init__()
        self._top_entity = None

        self.yang_name = "alarms"
        self.yang_parent_name = "Cisco-IOS-XR-alarmgr-server-oper"

        self.brief = Alarms.Brief()
        self.brief.parent = self
        self._children_name_map["brief"] = "brief"
        self._children_yang_names.add("brief")

        self.detail = Alarms.Detail()
        self.detail.parent = self
        self._children_name_map["detail"] = "detail"
        self._children_yang_names.add("detail")


    class Detail(Entity):
        """
        A set of detail alarm commands.
        
        .. attribute:: detail_card
        
        	Show detail card scope alarm related data
        	**type**\:   :py:class:`DetailCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard>`
        
        .. attribute:: detail_system
        
        	show detail system scope alarm related data
        	**type**\:   :py:class:`DetailSystem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem>`
        
        

        """

        _prefix = 'alarmgr-server-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Alarms.Detail, self).__init__()

            self.yang_name = "detail"
            self.yang_parent_name = "alarms"

            self.detail_card = Alarms.Detail.DetailCard()
            self.detail_card.parent = self
            self._children_name_map["detail_card"] = "detail-card"
            self._children_yang_names.add("detail-card")

            self.detail_system = Alarms.Detail.DetailSystem()
            self.detail_system.parent = self
            self._children_name_map["detail_system"] = "detail-system"
            self._children_yang_names.add("detail-system")


        class DetailSystem(Entity):
            """
            show detail system scope alarm related data.
            
            .. attribute:: active
            
            	Show the active alarms at this scope
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active>`
            
            .. attribute:: clients
            
            	Show the clients associated with this service
            	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Clients>`
            
            .. attribute:: history
            
            	Show the history alarms at this scope
            	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History>`
            
            .. attribute:: stats
            
            	Show the service statistics
            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Stats>`
            
            .. attribute:: suppressed
            
            	Show the suppressed alarms at this scope
            	**type**\:   :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Detail.DetailSystem, self).__init__()

                self.yang_name = "detail-system"
                self.yang_parent_name = "detail"

                self.active = Alarms.Detail.DetailSystem.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.clients = Alarms.Detail.DetailSystem.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._children_yang_names.add("clients")

                self.history = Alarms.Detail.DetailSystem.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"
                self._children_yang_names.add("history")

                self.stats = Alarms.Detail.DetailSystem.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"
                self._children_yang_names.add("stats")

                self.suppressed = Alarms.Detail.DetailSystem.Suppressed()
                self.suppressed.parent = self
                self._children_name_map["suppressed"] = "suppressed"
                self._children_yang_names.add("suppressed")


            class Active(Entity):
                """
                Show the active alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "detail-system"

                    self.alarm_info = YList(self)

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
                                super(Alarms.Detail.DetailSystem.Active, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Detail.DetailSystem.Active, self).__setattr__(name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn>`
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\:  bool
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting
                    	**type**\:   :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:   :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Active.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "active"

                        self.aid = YLeaf(YType.str, "aid")

                        self.alarm_name = YLeaf(YType.str, "alarm-name")

                        self.clear_time = YLeaf(YType.str, "clear-time")

                        self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                        self.description = YLeaf(YType.str, "description")

                        self.eid = YLeaf(YType.str, "eid")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.interface = YLeaf(YType.str, "interface")

                        self.location = YLeaf(YType.str, "location")

                        self.module = YLeaf(YType.str, "module")

                        self.pending_sync = YLeaf(YType.boolean, "pending-sync")

                        self.reporting_agent_id = YLeaf(YType.uint32, "reporting-agent-id")

                        self.service_affecting = YLeaf(YType.enumeration, "service-affecting")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                        self.status = YLeaf(YType.enumeration, "status")

                        self.tag = YLeaf(YType.str, "tag")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.otn = Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"
                        self._children_yang_names.add("otn")

                        self.tca = Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca()
                        self.tca.parent = self
                        self._children_name_map["tca"] = "tca"
                        self._children_yang_names.add("tca")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aid",
                                        "alarm_name",
                                        "clear_time",
                                        "clear_timestamp",
                                        "description",
                                        "eid",
                                        "group",
                                        "interface",
                                        "location",
                                        "module",
                                        "pending_sync",
                                        "reporting_agent_id",
                                        "service_affecting",
                                        "set_time",
                                        "set_timestamp",
                                        "severity",
                                        "status",
                                        "tag",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Detail.DetailSystem.Active.AlarmInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Detail.DetailSystem.Active.AlarmInfo, self).__setattr__(name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:   :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:   :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "alarm-info"

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.notification_source = YLeaf(YType.enumeration, "notification-source")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direction",
                                            "notification_source") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.direction.is_set or
                                self.notification_source.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direction.yfilter != YFilter.not_set or
                                self.notification_source.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "otn" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/alarm-info/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direction.get_name_leafdata())
                            if (self.notification_source.is_set or self.notification_source.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.notification_source.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "notification-source"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direction"):
                                self.direction = value
                                self.direction.value_namespace = name_space
                                self.direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "notification-source"):
                                self.notification_source = value
                                self.notification_source.value_namespace = name_space
                                self.notification_source.value_namespace_prefix = name_space_prefix


                    class Tca(Entity):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:   :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                        
                        .. attribute:: current_value
                        
                        	Alarm Threshold
                        	**type**\:  str
                        
                        	**length:** 0..20
                        
                        .. attribute:: threshold_value
                        
                        	Alarm Threshold 
                        	**type**\:  str
                        
                        	**length:** 0..20
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca, self).__init__()

                            self.yang_name = "tca"
                            self.yang_parent_name = "alarm-info"

                            self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                            self.current_value = YLeaf(YType.str, "current-value")

                            self.threshold_value = YLeaf(YType.str, "threshold-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bucket_type",
                                            "current_value",
                                            "threshold_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bucket_type.is_set or
                                self.current_value.is_set or
                                self.threshold_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bucket_type.yfilter != YFilter.not_set or
                                self.current_value.yfilter != YFilter.not_set or
                                self.threshold_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tca" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/alarm-info/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bucket_type.get_name_leafdata())
                            if (self.current_value.is_set or self.current_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.current_value.get_name_leafdata())
                            if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bucket-type" or name == "current-value" or name == "threshold-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bucket-type"):
                                self.bucket_type = value
                                self.bucket_type.value_namespace = name_space
                                self.bucket_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "current-value"):
                                self.current_value = value
                                self.current_value.value_namespace = name_space
                                self.current_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-value"):
                                self.threshold_value = value
                                self.threshold_value.value_namespace = name_space
                                self.threshold_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.aid.is_set or
                            self.alarm_name.is_set or
                            self.clear_time.is_set or
                            self.clear_timestamp.is_set or
                            self.description.is_set or
                            self.eid.is_set or
                            self.group.is_set or
                            self.interface.is_set or
                            self.location.is_set or
                            self.module.is_set or
                            self.pending_sync.is_set or
                            self.reporting_agent_id.is_set or
                            self.service_affecting.is_set or
                            self.set_time.is_set or
                            self.set_timestamp.is_set or
                            self.severity.is_set or
                            self.status.is_set or
                            self.tag.is_set or
                            self.type.is_set or
                            (self.otn is not None and self.otn.has_data()) or
                            (self.tca is not None and self.tca.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aid.yfilter != YFilter.not_set or
                            self.alarm_name.yfilter != YFilter.not_set or
                            self.clear_time.yfilter != YFilter.not_set or
                            self.clear_timestamp.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.eid.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.module.yfilter != YFilter.not_set or
                            self.pending_sync.yfilter != YFilter.not_set or
                            self.reporting_agent_id.yfilter != YFilter.not_set or
                            self.service_affecting.yfilter != YFilter.not_set or
                            self.set_time.yfilter != YFilter.not_set or
                            self.set_timestamp.yfilter != YFilter.not_set or
                            self.severity.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.tag.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            (self.otn is not None and self.otn.has_operation()) or
                            (self.tca is not None and self.tca.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aid.is_set or self.aid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aid.get_name_leafdata())
                        if (self.alarm_name.is_set or self.alarm_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_name.get_name_leafdata())
                        if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_time.get_name_leafdata())
                        if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.eid.is_set or self.eid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.eid.get_name_leafdata())
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.module.get_name_leafdata())
                        if (self.pending_sync.is_set or self.pending_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pending_sync.get_name_leafdata())
                        if (self.reporting_agent_id.is_set or self.reporting_agent_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reporting_agent_id.get_name_leafdata())
                        if (self.service_affecting.is_set or self.service_affecting.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_affecting.get_name_leafdata())
                        if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_time.get_name_leafdata())
                        if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                        if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severity.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "otn"):
                            if (self.otn is None):
                                self.otn = Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                            return self.otn

                        if (child_yang_name == "tca"):
                            if (self.tca is None):
                                self.tca = Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                            return self.tca

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "otn" or name == "tca" or name == "aid" or name == "alarm-name" or name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "eid" or name == "group" or name == "interface" or name == "location" or name == "module" or name == "pending-sync" or name == "reporting-agent-id" or name == "service-affecting" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "status" or name == "tag" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aid"):
                            self.aid = value
                            self.aid.value_namespace = name_space
                            self.aid.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-name"):
                            self.alarm_name = value
                            self.alarm_name.value_namespace = name_space
                            self.alarm_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-time"):
                            self.clear_time = value
                            self.clear_time.value_namespace = name_space
                            self.clear_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-timestamp"):
                            self.clear_timestamp = value
                            self.clear_timestamp.value_namespace = name_space
                            self.clear_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "eid"):
                            self.eid = value
                            self.eid.value_namespace = name_space
                            self.eid.value_namespace_prefix = name_space_prefix
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "module"):
                            self.module = value
                            self.module.value_namespace = name_space
                            self.module.value_namespace_prefix = name_space_prefix
                        if(value_path == "pending-sync"):
                            self.pending_sync = value
                            self.pending_sync.value_namespace = name_space
                            self.pending_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "reporting-agent-id"):
                            self.reporting_agent_id = value
                            self.reporting_agent_id.value_namespace = name_space
                            self.reporting_agent_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-affecting"):
                            self.service_affecting = value
                            self.service_affecting.value_namespace = name_space
                            self.service_affecting.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-time"):
                            self.set_time = value
                            self.set_time.value_namespace = name_space
                            self.set_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-timestamp"):
                            self.set_timestamp = value
                            self.set_timestamp.value_namespace = name_space
                            self.set_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "severity"):
                            self.severity = value
                            self.severity.value_namespace = name_space
                            self.severity.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag"):
                            self.tag = value
                            self.tag.value_namespace = name_space
                            self.tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.alarm_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.alarm_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "active" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "alarm-info"):
                        for c in self.alarm_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Detail.DetailSystem.Active.AlarmInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.alarm_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alarm-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class History(Entity):
                """
                Show the history alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "detail-system"

                    self.alarm_info = YList(self)

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
                                super(Alarms.Detail.DetailSystem.History, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Detail.DetailSystem.History, self).__setattr__(name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo.Otn>`
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\:  bool
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting
                    	**type**\:   :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo.Tca>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:   :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.History.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "history"

                        self.aid = YLeaf(YType.str, "aid")

                        self.alarm_name = YLeaf(YType.str, "alarm-name")

                        self.clear_time = YLeaf(YType.str, "clear-time")

                        self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                        self.description = YLeaf(YType.str, "description")

                        self.eid = YLeaf(YType.str, "eid")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.interface = YLeaf(YType.str, "interface")

                        self.location = YLeaf(YType.str, "location")

                        self.module = YLeaf(YType.str, "module")

                        self.pending_sync = YLeaf(YType.boolean, "pending-sync")

                        self.reporting_agent_id = YLeaf(YType.uint32, "reporting-agent-id")

                        self.service_affecting = YLeaf(YType.enumeration, "service-affecting")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                        self.status = YLeaf(YType.enumeration, "status")

                        self.tag = YLeaf(YType.str, "tag")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.otn = Alarms.Detail.DetailSystem.History.AlarmInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"
                        self._children_yang_names.add("otn")

                        self.tca = Alarms.Detail.DetailSystem.History.AlarmInfo.Tca()
                        self.tca.parent = self
                        self._children_name_map["tca"] = "tca"
                        self._children_yang_names.add("tca")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aid",
                                        "alarm_name",
                                        "clear_time",
                                        "clear_timestamp",
                                        "description",
                                        "eid",
                                        "group",
                                        "interface",
                                        "location",
                                        "module",
                                        "pending_sync",
                                        "reporting_agent_id",
                                        "service_affecting",
                                        "set_time",
                                        "set_timestamp",
                                        "severity",
                                        "status",
                                        "tag",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Detail.DetailSystem.History.AlarmInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Detail.DetailSystem.History.AlarmInfo, self).__setattr__(name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:   :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:   :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.History.AlarmInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "alarm-info"

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.notification_source = YLeaf(YType.enumeration, "notification-source")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direction",
                                            "notification_source") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Alarms.Detail.DetailSystem.History.AlarmInfo.Otn, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailSystem.History.AlarmInfo.Otn, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.direction.is_set or
                                self.notification_source.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direction.yfilter != YFilter.not_set or
                                self.notification_source.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "otn" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/alarm-info/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direction.get_name_leafdata())
                            if (self.notification_source.is_set or self.notification_source.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.notification_source.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "notification-source"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direction"):
                                self.direction = value
                                self.direction.value_namespace = name_space
                                self.direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "notification-source"):
                                self.notification_source = value
                                self.notification_source.value_namespace = name_space
                                self.notification_source.value_namespace_prefix = name_space_prefix


                    class Tca(Entity):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:   :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                        
                        .. attribute:: current_value
                        
                        	Alarm Threshold
                        	**type**\:  str
                        
                        	**length:** 0..20
                        
                        .. attribute:: threshold_value
                        
                        	Alarm Threshold 
                        	**type**\:  str
                        
                        	**length:** 0..20
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.History.AlarmInfo.Tca, self).__init__()

                            self.yang_name = "tca"
                            self.yang_parent_name = "alarm-info"

                            self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                            self.current_value = YLeaf(YType.str, "current-value")

                            self.threshold_value = YLeaf(YType.str, "threshold-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bucket_type",
                                            "current_value",
                                            "threshold_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Alarms.Detail.DetailSystem.History.AlarmInfo.Tca, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailSystem.History.AlarmInfo.Tca, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bucket_type.is_set or
                                self.current_value.is_set or
                                self.threshold_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bucket_type.yfilter != YFilter.not_set or
                                self.current_value.yfilter != YFilter.not_set or
                                self.threshold_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tca" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/alarm-info/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bucket_type.get_name_leafdata())
                            if (self.current_value.is_set or self.current_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.current_value.get_name_leafdata())
                            if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bucket-type" or name == "current-value" or name == "threshold-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bucket-type"):
                                self.bucket_type = value
                                self.bucket_type.value_namespace = name_space
                                self.bucket_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "current-value"):
                                self.current_value = value
                                self.current_value.value_namespace = name_space
                                self.current_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-value"):
                                self.threshold_value = value
                                self.threshold_value.value_namespace = name_space
                                self.threshold_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.aid.is_set or
                            self.alarm_name.is_set or
                            self.clear_time.is_set or
                            self.clear_timestamp.is_set or
                            self.description.is_set or
                            self.eid.is_set or
                            self.group.is_set or
                            self.interface.is_set or
                            self.location.is_set or
                            self.module.is_set or
                            self.pending_sync.is_set or
                            self.reporting_agent_id.is_set or
                            self.service_affecting.is_set or
                            self.set_time.is_set or
                            self.set_timestamp.is_set or
                            self.severity.is_set or
                            self.status.is_set or
                            self.tag.is_set or
                            self.type.is_set or
                            (self.otn is not None and self.otn.has_data()) or
                            (self.tca is not None and self.tca.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aid.yfilter != YFilter.not_set or
                            self.alarm_name.yfilter != YFilter.not_set or
                            self.clear_time.yfilter != YFilter.not_set or
                            self.clear_timestamp.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.eid.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.module.yfilter != YFilter.not_set or
                            self.pending_sync.yfilter != YFilter.not_set or
                            self.reporting_agent_id.yfilter != YFilter.not_set or
                            self.service_affecting.yfilter != YFilter.not_set or
                            self.set_time.yfilter != YFilter.not_set or
                            self.set_timestamp.yfilter != YFilter.not_set or
                            self.severity.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.tag.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            (self.otn is not None and self.otn.has_operation()) or
                            (self.tca is not None and self.tca.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aid.is_set or self.aid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aid.get_name_leafdata())
                        if (self.alarm_name.is_set or self.alarm_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_name.get_name_leafdata())
                        if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_time.get_name_leafdata())
                        if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.eid.is_set or self.eid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.eid.get_name_leafdata())
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.module.get_name_leafdata())
                        if (self.pending_sync.is_set or self.pending_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pending_sync.get_name_leafdata())
                        if (self.reporting_agent_id.is_set or self.reporting_agent_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reporting_agent_id.get_name_leafdata())
                        if (self.service_affecting.is_set or self.service_affecting.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_affecting.get_name_leafdata())
                        if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_time.get_name_leafdata())
                        if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                        if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severity.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "otn"):
                            if (self.otn is None):
                                self.otn = Alarms.Detail.DetailSystem.History.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                            return self.otn

                        if (child_yang_name == "tca"):
                            if (self.tca is None):
                                self.tca = Alarms.Detail.DetailSystem.History.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                            return self.tca

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "otn" or name == "tca" or name == "aid" or name == "alarm-name" or name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "eid" or name == "group" or name == "interface" or name == "location" or name == "module" or name == "pending-sync" or name == "reporting-agent-id" or name == "service-affecting" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "status" or name == "tag" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aid"):
                            self.aid = value
                            self.aid.value_namespace = name_space
                            self.aid.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-name"):
                            self.alarm_name = value
                            self.alarm_name.value_namespace = name_space
                            self.alarm_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-time"):
                            self.clear_time = value
                            self.clear_time.value_namespace = name_space
                            self.clear_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-timestamp"):
                            self.clear_timestamp = value
                            self.clear_timestamp.value_namespace = name_space
                            self.clear_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "eid"):
                            self.eid = value
                            self.eid.value_namespace = name_space
                            self.eid.value_namespace_prefix = name_space_prefix
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "module"):
                            self.module = value
                            self.module.value_namespace = name_space
                            self.module.value_namespace_prefix = name_space_prefix
                        if(value_path == "pending-sync"):
                            self.pending_sync = value
                            self.pending_sync.value_namespace = name_space
                            self.pending_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "reporting-agent-id"):
                            self.reporting_agent_id = value
                            self.reporting_agent_id.value_namespace = name_space
                            self.reporting_agent_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-affecting"):
                            self.service_affecting = value
                            self.service_affecting.value_namespace = name_space
                            self.service_affecting.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-time"):
                            self.set_time = value
                            self.set_time.value_namespace = name_space
                            self.set_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-timestamp"):
                            self.set_timestamp = value
                            self.set_timestamp.value_namespace = name_space
                            self.set_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "severity"):
                            self.severity = value
                            self.severity.value_namespace = name_space
                            self.severity.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag"):
                            self.tag = value
                            self.tag.value_namespace = name_space
                            self.tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.alarm_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.alarm_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "history" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "alarm-info"):
                        for c in self.alarm_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Detail.DetailSystem.History.AlarmInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.alarm_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alarm-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Suppressed(Entity):
                """
                Show the suppressed alarms at this scope.
                
                .. attribute:: suppressed_info
                
                	Suppressed Alarm List
                	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Suppressed, self).__init__()

                    self.yang_name = "suppressed"
                    self.yang_parent_name = "detail-system"

                    self.suppressed_info = YList(self)

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
                                super(Alarms.Detail.DetailSystem.Suppressed, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Detail.DetailSystem.Suppressed, self).__setattr__(name, value)


                class SuppressedInfo(Entity):
                    """
                    Suppressed Alarm List
                    
                    .. attribute:: aid
                    
                    	Alarm aid
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: alarm_name
                    
                    	Alarm name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: eid
                    
                    	Alarm eid
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: interface
                    
                    	Alarm interface name
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: module
                    
                    	Alarm module description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: otn
                    
                    	OTN feature specific alarm attributes
                    	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn>`
                    
                    .. attribute:: pending_sync
                    
                    	Pending async flag
                    	**type**\:  bool
                    
                    .. attribute:: reporting_agent_id
                    
                    	Reporting agent id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_affecting
                    
                    	Alarm service affecting 
                    	**type**\:   :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: suppressed_timestamp
                    
                    	Alarm suppressed time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo, self).__init__()

                        self.yang_name = "suppressed-info"
                        self.yang_parent_name = "suppressed"

                        self.aid = YLeaf(YType.str, "aid")

                        self.alarm_name = YLeaf(YType.str, "alarm-name")

                        self.description = YLeaf(YType.str, "description")

                        self.eid = YLeaf(YType.str, "eid")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.interface = YLeaf(YType.str, "interface")

                        self.location = YLeaf(YType.str, "location")

                        self.module = YLeaf(YType.str, "module")

                        self.pending_sync = YLeaf(YType.boolean, "pending-sync")

                        self.reporting_agent_id = YLeaf(YType.uint32, "reporting-agent-id")

                        self.service_affecting = YLeaf(YType.enumeration, "service-affecting")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                        self.status = YLeaf(YType.enumeration, "status")

                        self.suppressed_time = YLeaf(YType.str, "suppressed-time")

                        self.suppressed_timestamp = YLeaf(YType.uint64, "suppressed-timestamp")

                        self.tag = YLeaf(YType.str, "tag")

                        self.otn = Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn()
                        self.otn.parent = self
                        self._children_name_map["otn"] = "otn"
                        self._children_yang_names.add("otn")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aid",
                                        "alarm_name",
                                        "description",
                                        "eid",
                                        "group",
                                        "interface",
                                        "location",
                                        "module",
                                        "pending_sync",
                                        "reporting_agent_id",
                                        "service_affecting",
                                        "set_time",
                                        "set_timestamp",
                                        "severity",
                                        "status",
                                        "suppressed_time",
                                        "suppressed_timestamp",
                                        "tag") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo, self).__setattr__(name, value)


                    class Otn(Entity):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:   :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:   :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn, self).__init__()

                            self.yang_name = "otn"
                            self.yang_parent_name = "suppressed-info"

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.notification_source = YLeaf(YType.enumeration, "notification-source")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direction",
                                            "notification_source") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.direction.is_set or
                                self.notification_source.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direction.yfilter != YFilter.not_set or
                                self.notification_source.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "otn" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/suppressed/suppressed-info/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direction.get_name_leafdata())
                            if (self.notification_source.is_set or self.notification_source.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.notification_source.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "direction" or name == "notification-source"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direction"):
                                self.direction = value
                                self.direction.value_namespace = name_space
                                self.direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "notification-source"):
                                self.notification_source = value
                                self.notification_source.value_namespace = name_space
                                self.notification_source.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.aid.is_set or
                            self.alarm_name.is_set or
                            self.description.is_set or
                            self.eid.is_set or
                            self.group.is_set or
                            self.interface.is_set or
                            self.location.is_set or
                            self.module.is_set or
                            self.pending_sync.is_set or
                            self.reporting_agent_id.is_set or
                            self.service_affecting.is_set or
                            self.set_time.is_set or
                            self.set_timestamp.is_set or
                            self.severity.is_set or
                            self.status.is_set or
                            self.suppressed_time.is_set or
                            self.suppressed_timestamp.is_set or
                            self.tag.is_set or
                            (self.otn is not None and self.otn.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aid.yfilter != YFilter.not_set or
                            self.alarm_name.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.eid.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.module.yfilter != YFilter.not_set or
                            self.pending_sync.yfilter != YFilter.not_set or
                            self.reporting_agent_id.yfilter != YFilter.not_set or
                            self.service_affecting.yfilter != YFilter.not_set or
                            self.set_time.yfilter != YFilter.not_set or
                            self.set_timestamp.yfilter != YFilter.not_set or
                            self.severity.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.suppressed_time.yfilter != YFilter.not_set or
                            self.suppressed_timestamp.yfilter != YFilter.not_set or
                            self.tag.yfilter != YFilter.not_set or
                            (self.otn is not None and self.otn.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "suppressed-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/suppressed/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aid.is_set or self.aid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aid.get_name_leafdata())
                        if (self.alarm_name.is_set or self.alarm_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_name.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.eid.is_set or self.eid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.eid.get_name_leafdata())
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.module.get_name_leafdata())
                        if (self.pending_sync.is_set or self.pending_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pending_sync.get_name_leafdata())
                        if (self.reporting_agent_id.is_set or self.reporting_agent_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reporting_agent_id.get_name_leafdata())
                        if (self.service_affecting.is_set or self.service_affecting.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_affecting.get_name_leafdata())
                        if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_time.get_name_leafdata())
                        if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                        if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severity.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.suppressed_time.is_set or self.suppressed_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.suppressed_time.get_name_leafdata())
                        if (self.suppressed_timestamp.is_set or self.suppressed_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.suppressed_timestamp.get_name_leafdata())
                        if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "otn"):
                            if (self.otn is None):
                                self.otn = Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                            return self.otn

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "otn" or name == "aid" or name == "alarm-name" or name == "description" or name == "eid" or name == "group" or name == "interface" or name == "location" or name == "module" or name == "pending-sync" or name == "reporting-agent-id" or name == "service-affecting" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "status" or name == "suppressed-time" or name == "suppressed-timestamp" or name == "tag"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aid"):
                            self.aid = value
                            self.aid.value_namespace = name_space
                            self.aid.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-name"):
                            self.alarm_name = value
                            self.alarm_name.value_namespace = name_space
                            self.alarm_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "eid"):
                            self.eid = value
                            self.eid.value_namespace = name_space
                            self.eid.value_namespace_prefix = name_space_prefix
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "module"):
                            self.module = value
                            self.module.value_namespace = name_space
                            self.module.value_namespace_prefix = name_space_prefix
                        if(value_path == "pending-sync"):
                            self.pending_sync = value
                            self.pending_sync.value_namespace = name_space
                            self.pending_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "reporting-agent-id"):
                            self.reporting_agent_id = value
                            self.reporting_agent_id.value_namespace = name_space
                            self.reporting_agent_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-affecting"):
                            self.service_affecting = value
                            self.service_affecting.value_namespace = name_space
                            self.service_affecting.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-time"):
                            self.set_time = value
                            self.set_time.value_namespace = name_space
                            self.set_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-timestamp"):
                            self.set_timestamp = value
                            self.set_timestamp.value_namespace = name_space
                            self.set_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "severity"):
                            self.severity = value
                            self.severity.value_namespace = name_space
                            self.severity.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "suppressed-time"):
                            self.suppressed_time = value
                            self.suppressed_time.value_namespace = name_space
                            self.suppressed_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "suppressed-timestamp"):
                            self.suppressed_timestamp = value
                            self.suppressed_timestamp.value_namespace = name_space
                            self.suppressed_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag"):
                            self.tag = value
                            self.tag.value_namespace = name_space
                            self.tag.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.suppressed_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.suppressed_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "suppressed" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "suppressed-info"):
                        for c in self.suppressed_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.suppressed_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "suppressed-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Stats(Entity):
                """
                Show the service statistics.
                
                .. attribute:: active
                
                	Alarms that are currently in the active state
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cache_hit
                
                	Total alarms which had the cache hit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_miss
                
                	Total alarms which had the cache miss
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped
                
                	Alarms that we couldn't keep track due to some error or other
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: dropped_clear_without_set
                
                	Alarms dropped clear without set
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_db_error
                
                	Alarms dropped due to db error
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_duplicate
                
                	Alarms dropped which were duplicate
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_insuff_mem
                
                	Alarms dropped due to insufficient memory
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_invalid_aid
                
                	Alarms dropped due to invalid aid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: history
                
                	Alarms that are cleared. This one is counted over a long period of time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reported
                
                	Alarms that were in all reported to this Alarm Mgr
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: suppressed
                
                	Alarms that are in suppressed state
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sysadmin_active
                
                	Alarms that are currently in the active state(sysadmin plane)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sysadmin_history
                
                	Alarms that are cleared in sysadmin plane. This one is counted over a long period of time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sysadmin_suppressed
                
                	Alarms that are suppressed in sysadmin plane
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "detail-system"

                    self.active = YLeaf(YType.uint64, "active")

                    self.cache_hit = YLeaf(YType.uint32, "cache-hit")

                    self.cache_miss = YLeaf(YType.uint32, "cache-miss")

                    self.dropped = YLeaf(YType.uint64, "dropped")

                    self.dropped_clear_without_set = YLeaf(YType.uint32, "dropped-clear-without-set")

                    self.dropped_db_error = YLeaf(YType.uint32, "dropped-db-error")

                    self.dropped_duplicate = YLeaf(YType.uint32, "dropped-duplicate")

                    self.dropped_insuff_mem = YLeaf(YType.uint32, "dropped-insuff-mem")

                    self.dropped_invalid_aid = YLeaf(YType.uint32, "dropped-invalid-aid")

                    self.history = YLeaf(YType.uint64, "history")

                    self.reported = YLeaf(YType.uint64, "reported")

                    self.suppressed = YLeaf(YType.uint64, "suppressed")

                    self.sysadmin_active = YLeaf(YType.uint64, "sysadmin-active")

                    self.sysadmin_history = YLeaf(YType.uint64, "sysadmin-history")

                    self.sysadmin_suppressed = YLeaf(YType.uint64, "sysadmin-suppressed")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "cache_hit",
                                    "cache_miss",
                                    "dropped",
                                    "dropped_clear_without_set",
                                    "dropped_db_error",
                                    "dropped_duplicate",
                                    "dropped_insuff_mem",
                                    "dropped_invalid_aid",
                                    "history",
                                    "reported",
                                    "suppressed",
                                    "sysadmin_active",
                                    "sysadmin_history",
                                    "sysadmin_suppressed") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Alarms.Detail.DetailSystem.Stats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Detail.DetailSystem.Stats, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active.is_set or
                        self.cache_hit.is_set or
                        self.cache_miss.is_set or
                        self.dropped.is_set or
                        self.dropped_clear_without_set.is_set or
                        self.dropped_db_error.is_set or
                        self.dropped_duplicate.is_set or
                        self.dropped_insuff_mem.is_set or
                        self.dropped_invalid_aid.is_set or
                        self.history.is_set or
                        self.reported.is_set or
                        self.suppressed.is_set or
                        self.sysadmin_active.is_set or
                        self.sysadmin_history.is_set or
                        self.sysadmin_suppressed.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.cache_hit.yfilter != YFilter.not_set or
                        self.cache_miss.yfilter != YFilter.not_set or
                        self.dropped.yfilter != YFilter.not_set or
                        self.dropped_clear_without_set.yfilter != YFilter.not_set or
                        self.dropped_db_error.yfilter != YFilter.not_set or
                        self.dropped_duplicate.yfilter != YFilter.not_set or
                        self.dropped_insuff_mem.yfilter != YFilter.not_set or
                        self.dropped_invalid_aid.yfilter != YFilter.not_set or
                        self.history.yfilter != YFilter.not_set or
                        self.reported.yfilter != YFilter.not_set or
                        self.suppressed.yfilter != YFilter.not_set or
                        self.sysadmin_active.yfilter != YFilter.not_set or
                        self.sysadmin_history.yfilter != YFilter.not_set or
                        self.sysadmin_suppressed.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "stats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.cache_hit.is_set or self.cache_hit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cache_hit.get_name_leafdata())
                    if (self.cache_miss.is_set or self.cache_miss.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cache_miss.get_name_leafdata())
                    if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped.get_name_leafdata())
                    if (self.dropped_clear_without_set.is_set or self.dropped_clear_without_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_clear_without_set.get_name_leafdata())
                    if (self.dropped_db_error.is_set or self.dropped_db_error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_db_error.get_name_leafdata())
                    if (self.dropped_duplicate.is_set or self.dropped_duplicate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_duplicate.get_name_leafdata())
                    if (self.dropped_insuff_mem.is_set or self.dropped_insuff_mem.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_insuff_mem.get_name_leafdata())
                    if (self.dropped_invalid_aid.is_set or self.dropped_invalid_aid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_invalid_aid.get_name_leafdata())
                    if (self.history.is_set or self.history.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.history.get_name_leafdata())
                    if (self.reported.is_set or self.reported.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reported.get_name_leafdata())
                    if (self.suppressed.is_set or self.suppressed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.suppressed.get_name_leafdata())
                    if (self.sysadmin_active.is_set or self.sysadmin_active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sysadmin_active.get_name_leafdata())
                    if (self.sysadmin_history.is_set or self.sysadmin_history.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sysadmin_history.get_name_leafdata())
                    if (self.sysadmin_suppressed.is_set or self.sysadmin_suppressed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sysadmin_suppressed.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active" or name == "cache-hit" or name == "cache-miss" or name == "dropped" or name == "dropped-clear-without-set" or name == "dropped-db-error" or name == "dropped-duplicate" or name == "dropped-insuff-mem" or name == "dropped-invalid-aid" or name == "history" or name == "reported" or name == "suppressed" or name == "sysadmin-active" or name == "sysadmin-history" or name == "sysadmin-suppressed"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "cache-hit"):
                        self.cache_hit = value
                        self.cache_hit.value_namespace = name_space
                        self.cache_hit.value_namespace_prefix = name_space_prefix
                    if(value_path == "cache-miss"):
                        self.cache_miss = value
                        self.cache_miss.value_namespace = name_space
                        self.cache_miss.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped"):
                        self.dropped = value
                        self.dropped.value_namespace = name_space
                        self.dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-clear-without-set"):
                        self.dropped_clear_without_set = value
                        self.dropped_clear_without_set.value_namespace = name_space
                        self.dropped_clear_without_set.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-db-error"):
                        self.dropped_db_error = value
                        self.dropped_db_error.value_namespace = name_space
                        self.dropped_db_error.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-duplicate"):
                        self.dropped_duplicate = value
                        self.dropped_duplicate.value_namespace = name_space
                        self.dropped_duplicate.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-insuff-mem"):
                        self.dropped_insuff_mem = value
                        self.dropped_insuff_mem.value_namespace = name_space
                        self.dropped_insuff_mem.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-invalid-aid"):
                        self.dropped_invalid_aid = value
                        self.dropped_invalid_aid.value_namespace = name_space
                        self.dropped_invalid_aid.value_namespace_prefix = name_space_prefix
                    if(value_path == "history"):
                        self.history = value
                        self.history.value_namespace = name_space
                        self.history.value_namespace_prefix = name_space_prefix
                    if(value_path == "reported"):
                        self.reported = value
                        self.reported.value_namespace = name_space
                        self.reported.value_namespace_prefix = name_space_prefix
                    if(value_path == "suppressed"):
                        self.suppressed = value
                        self.suppressed.value_namespace = name_space
                        self.suppressed.value_namespace_prefix = name_space_prefix
                    if(value_path == "sysadmin-active"):
                        self.sysadmin_active = value
                        self.sysadmin_active.value_namespace = name_space
                        self.sysadmin_active.value_namespace_prefix = name_space_prefix
                    if(value_path == "sysadmin-history"):
                        self.sysadmin_history = value
                        self.sysadmin_history.value_namespace = name_space
                        self.sysadmin_history.value_namespace_prefix = name_space_prefix
                    if(value_path == "sysadmin-suppressed"):
                        self.sysadmin_suppressed = value
                        self.sysadmin_suppressed.value_namespace = name_space
                        self.sysadmin_suppressed.value_namespace_prefix = name_space_prefix


            class Clients(Entity):
                """
                Show the clients associated with this service.
                
                .. attribute:: client_info
                
                	Client List
                	**type**\: list of    :py:class:`ClientInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Clients.ClientInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailSystem.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "detail-system"

                    self.client_info = YList(self)

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
                                super(Alarms.Detail.DetailSystem.Clients, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Detail.DetailSystem.Clients, self).__setattr__(name, value)


                class ClientInfo(Entity):
                    """
                    Client List
                    
                    .. attribute:: connect_count
                    
                    	Number of times the agent connected to the alarm mgr
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connect_timestamp
                    
                    	Agent connect timestamp
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: filter_disp
                    
                    	The current subscription status of the client
                    	**type**\:  bool
                    
                    .. attribute:: filter_group
                    
                    	The filter used for alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: filter_severity
                    
                    	The filter used for alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: filter_state
                    
                    	The filter used for alarm bi\-state state+
                    	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                    
                    .. attribute:: get_count
                    
                    	Number of times the agent queried for alarms
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: handle
                    
                    	The client handle through which interface
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: id
                    
                    	Alarms agent id of the client
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: location
                    
                    	The location of this client
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: name
                    
                    	Alarm client
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: report_count
                    
                    	Number of times the agent reported alarms
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	The current state of the client
                    	**type**\:   :py:class:`AlarmClientState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientState>`
                    
                    .. attribute:: subscribe_count
                    
                    	Number of times the agent subscribed for alarms
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscriber_id
                    
                    	Alarms agent subscriber id of the client
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	The type of the client
                    	**type**\:   :py:class:`AlarmClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClient>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailSystem.Clients.ClientInfo, self).__init__()

                        self.yang_name = "client-info"
                        self.yang_parent_name = "clients"

                        self.connect_count = YLeaf(YType.uint32, "connect-count")

                        self.connect_timestamp = YLeaf(YType.str, "connect-timestamp")

                        self.filter_disp = YLeaf(YType.boolean, "filter-disp")

                        self.filter_group = YLeaf(YType.enumeration, "filter-group")

                        self.filter_severity = YLeaf(YType.enumeration, "filter-severity")

                        self.filter_state = YLeaf(YType.enumeration, "filter-state")

                        self.get_count = YLeaf(YType.uint32, "get-count")

                        self.handle = YLeaf(YType.str, "handle")

                        self.id = YLeaf(YType.uint32, "id")

                        self.location = YLeaf(YType.str, "location")

                        self.name = YLeaf(YType.str, "name")

                        self.report_count = YLeaf(YType.uint32, "report-count")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.subscribe_count = YLeaf(YType.uint32, "subscribe-count")

                        self.subscriber_id = YLeaf(YType.uint32, "subscriber-id")

                        self.type = YLeaf(YType.enumeration, "type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("connect_count",
                                        "connect_timestamp",
                                        "filter_disp",
                                        "filter_group",
                                        "filter_severity",
                                        "filter_state",
                                        "get_count",
                                        "handle",
                                        "id",
                                        "location",
                                        "name",
                                        "report_count",
                                        "state",
                                        "subscribe_count",
                                        "subscriber_id",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Detail.DetailSystem.Clients.ClientInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Detail.DetailSystem.Clients.ClientInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.connect_count.is_set or
                            self.connect_timestamp.is_set or
                            self.filter_disp.is_set or
                            self.filter_group.is_set or
                            self.filter_severity.is_set or
                            self.filter_state.is_set or
                            self.get_count.is_set or
                            self.handle.is_set or
                            self.id.is_set or
                            self.location.is_set or
                            self.name.is_set or
                            self.report_count.is_set or
                            self.state.is_set or
                            self.subscribe_count.is_set or
                            self.subscriber_id.is_set or
                            self.type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.connect_count.yfilter != YFilter.not_set or
                            self.connect_timestamp.yfilter != YFilter.not_set or
                            self.filter_disp.yfilter != YFilter.not_set or
                            self.filter_group.yfilter != YFilter.not_set or
                            self.filter_severity.yfilter != YFilter.not_set or
                            self.filter_state.yfilter != YFilter.not_set or
                            self.get_count.yfilter != YFilter.not_set or
                            self.handle.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.report_count.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.subscribe_count.yfilter != YFilter.not_set or
                            self.subscriber_id.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/clients/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.connect_count.is_set or self.connect_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connect_count.get_name_leafdata())
                        if (self.connect_timestamp.is_set or self.connect_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connect_timestamp.get_name_leafdata())
                        if (self.filter_disp.is_set or self.filter_disp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.filter_disp.get_name_leafdata())
                        if (self.filter_group.is_set or self.filter_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.filter_group.get_name_leafdata())
                        if (self.filter_severity.is_set or self.filter_severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.filter_severity.get_name_leafdata())
                        if (self.filter_state.is_set or self.filter_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.filter_state.get_name_leafdata())
                        if (self.get_count.is_set or self.get_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.get_count.get_name_leafdata())
                        if (self.handle.is_set or self.handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.handle.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.report_count.is_set or self.report_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.report_count.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.subscribe_count.is_set or self.subscribe_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscribe_count.get_name_leafdata())
                        if (self.subscriber_id.is_set or self.subscriber_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscriber_id.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "connect-count" or name == "connect-timestamp" or name == "filter-disp" or name == "filter-group" or name == "filter-severity" or name == "filter-state" or name == "get-count" or name == "handle" or name == "id" or name == "location" or name == "name" or name == "report-count" or name == "state" or name == "subscribe-count" or name == "subscriber-id" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "connect-count"):
                            self.connect_count = value
                            self.connect_count.value_namespace = name_space
                            self.connect_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "connect-timestamp"):
                            self.connect_timestamp = value
                            self.connect_timestamp.value_namespace = name_space
                            self.connect_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "filter-disp"):
                            self.filter_disp = value
                            self.filter_disp.value_namespace = name_space
                            self.filter_disp.value_namespace_prefix = name_space_prefix
                        if(value_path == "filter-group"):
                            self.filter_group = value
                            self.filter_group.value_namespace = name_space
                            self.filter_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "filter-severity"):
                            self.filter_severity = value
                            self.filter_severity.value_namespace = name_space
                            self.filter_severity.value_namespace_prefix = name_space_prefix
                        if(value_path == "filter-state"):
                            self.filter_state = value
                            self.filter_state.value_namespace = name_space
                            self.filter_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "get-count"):
                            self.get_count = value
                            self.get_count.value_namespace = name_space
                            self.get_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "handle"):
                            self.handle = value
                            self.handle.value_namespace = name_space
                            self.handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "report-count"):
                            self.report_count = value
                            self.report_count.value_namespace = name_space
                            self.report_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscribe-count"):
                            self.subscribe_count = value
                            self.subscribe_count.value_namespace = name_space
                            self.subscribe_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscriber-id"):
                            self.subscriber_id = value
                            self.subscriber_id.value_namespace = name_space
                            self.subscriber_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.client_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "clients" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "client-info"):
                        for c in self.client_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Detail.DetailSystem.Clients.ClientInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.active is not None and self.active.has_data()) or
                    (self.clients is not None and self.clients.has_data()) or
                    (self.history is not None and self.history.has_data()) or
                    (self.stats is not None and self.stats.has_data()) or
                    (self.suppressed is not None and self.suppressed.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.active is not None and self.active.has_operation()) or
                    (self.clients is not None and self.clients.has_operation()) or
                    (self.history is not None and self.history.has_operation()) or
                    (self.stats is not None and self.stats.has_operation()) or
                    (self.suppressed is not None and self.suppressed.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "detail-system" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "active"):
                    if (self.active is None):
                        self.active = Alarms.Detail.DetailSystem.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"
                    return self.active

                if (child_yang_name == "clients"):
                    if (self.clients is None):
                        self.clients = Alarms.Detail.DetailSystem.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                    return self.clients

                if (child_yang_name == "history"):
                    if (self.history is None):
                        self.history = Alarms.Detail.DetailSystem.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"
                    return self.history

                if (child_yang_name == "stats"):
                    if (self.stats is None):
                        self.stats = Alarms.Detail.DetailSystem.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                    return self.stats

                if (child_yang_name == "suppressed"):
                    if (self.suppressed is None):
                        self.suppressed = Alarms.Detail.DetailSystem.Suppressed()
                        self.suppressed.parent = self
                        self._children_name_map["suppressed"] = "suppressed"
                    return self.suppressed

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active" or name == "clients" or name == "history" or name == "stats" or name == "suppressed"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class DetailCard(Entity):
            """
            Show detail card scope alarm related data.
            
            .. attribute:: detail_locations
            
            	Table of DetailLocation
            	**type**\:   :py:class:`DetailLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Detail.DetailCard, self).__init__()

                self.yang_name = "detail-card"
                self.yang_parent_name = "detail"

                self.detail_locations = Alarms.Detail.DetailCard.DetailLocations()
                self.detail_locations.parent = self
                self._children_name_map["detail_locations"] = "detail-locations"
                self._children_yang_names.add("detail-locations")


            class DetailLocations(Entity):
                """
                Table of DetailLocation
                
                .. attribute:: detail_location
                
                	Specify a card location for alarms
                	**type**\: list of    :py:class:`DetailLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Detail.DetailCard.DetailLocations, self).__init__()

                    self.yang_name = "detail-locations"
                    self.yang_parent_name = "detail-card"

                    self.detail_location = YList(self)

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
                                super(Alarms.Detail.DetailCard.DetailLocations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Detail.DetailCard.DetailLocations, self).__setattr__(name, value)


                class DetailLocation(Entity):
                    """
                    Specify a card location for alarms.
                    
                    .. attribute:: node_id  <key>
                    
                    	NodeID of the Location
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: active
                    
                    	Show the active alarms at this scope
                    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active>`
                    
                    .. attribute:: clients
                    
                    	Show the clients associated with this service
                    	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients>`
                    
                    .. attribute:: history
                    
                    	Show the history alarms at this scope
                    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History>`
                    
                    .. attribute:: stats
                    
                    	Show the service statistics
                    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats>`
                    
                    .. attribute:: suppressed
                    
                    	Show the suppressed alarms at this scope
                    	**type**\:   :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation, self).__init__()

                        self.yang_name = "detail-location"
                        self.yang_parent_name = "detail-locations"

                        self.node_id = YLeaf(YType.str, "node-id")

                        self.active = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"
                        self._children_yang_names.add("active")

                        self.clients = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                        self._children_yang_names.add("clients")

                        self.history = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"
                        self._children_yang_names.add("history")

                        self.stats = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                        self._children_yang_names.add("stats")

                        self.suppressed = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed()
                        self.suppressed.parent = self
                        self._children_name_map["suppressed"] = "suppressed"
                        self._children_yang_names.add("suppressed")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("node_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation, self).__setattr__(name, value)


                    class Active(Entity):
                        """
                        Show the active alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active, self).__init__()

                            self.yang_name = "active"
                            self.yang_parent_name = "detail-location"

                            self.alarm_info = YList(self)

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
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active, self).__setattr__(name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn>`
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\:  bool
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting
                            	**type**\:   :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:   :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "active"

                                self.aid = YLeaf(YType.str, "aid")

                                self.alarm_name = YLeaf(YType.str, "alarm-name")

                                self.clear_time = YLeaf(YType.str, "clear-time")

                                self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                                self.description = YLeaf(YType.str, "description")

                                self.eid = YLeaf(YType.str, "eid")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.interface = YLeaf(YType.str, "interface")

                                self.location = YLeaf(YType.str, "location")

                                self.module = YLeaf(YType.str, "module")

                                self.pending_sync = YLeaf(YType.boolean, "pending-sync")

                                self.reporting_agent_id = YLeaf(YType.uint32, "reporting-agent-id")

                                self.service_affecting = YLeaf(YType.enumeration, "service-affecting")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.tag = YLeaf(YType.str, "tag")

                                self.type = YLeaf(YType.enumeration, "type")

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                                self._children_yang_names.add("otn")

                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                                self._children_yang_names.add("tca")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("aid",
                                                "alarm_name",
                                                "clear_time",
                                                "clear_timestamp",
                                                "description",
                                                "eid",
                                                "group",
                                                "interface",
                                                "location",
                                                "module",
                                                "pending_sync",
                                                "reporting_agent_id",
                                                "service_affecting",
                                                "set_time",
                                                "set_timestamp",
                                                "severity",
                                                "status",
                                                "tag",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo, self).__setattr__(name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:   :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:   :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "alarm-info"

                                    self.direction = YLeaf(YType.enumeration, "direction")

                                    self.notification_source = YLeaf(YType.enumeration, "notification-source")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("direction",
                                                    "notification_source") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.direction.is_set or
                                        self.notification_source.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.direction.yfilter != YFilter.not_set or
                                        self.notification_source.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "otn" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.direction.get_name_leafdata())
                                    if (self.notification_source.is_set or self.notification_source.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.notification_source.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "direction" or name == "notification-source"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "direction"):
                                        self.direction = value
                                        self.direction.value_namespace = name_space
                                        self.direction.value_namespace_prefix = name_space_prefix
                                    if(value_path == "notification-source"):
                                        self.notification_source = value
                                        self.notification_source.value_namespace = name_space
                                        self.notification_source.value_namespace_prefix = name_space_prefix


                            class Tca(Entity):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:   :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                                
                                .. attribute:: current_value
                                
                                	Alarm Threshold
                                	**type**\:  str
                                
                                	**length:** 0..20
                                
                                .. attribute:: threshold_value
                                
                                	Alarm Threshold 
                                	**type**\:  str
                                
                                	**length:** 0..20
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca, self).__init__()

                                    self.yang_name = "tca"
                                    self.yang_parent_name = "alarm-info"

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.current_value = YLeaf(YType.str, "current-value")

                                    self.threshold_value = YLeaf(YType.str, "threshold-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bucket_type",
                                                    "current_value",
                                                    "threshold_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.bucket_type.is_set or
                                        self.current_value.is_set or
                                        self.threshold_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bucket_type.yfilter != YFilter.not_set or
                                        self.current_value.yfilter != YFilter.not_set or
                                        self.threshold_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tca" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_type.get_name_leafdata())
                                    if (self.current_value.is_set or self.current_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.current_value.get_name_leafdata())
                                    if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.threshold_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bucket-type" or name == "current-value" or name == "threshold-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bucket-type"):
                                        self.bucket_type = value
                                        self.bucket_type.value_namespace = name_space
                                        self.bucket_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "current-value"):
                                        self.current_value = value
                                        self.current_value.value_namespace = name_space
                                        self.current_value.value_namespace_prefix = name_space_prefix
                                    if(value_path == "threshold-value"):
                                        self.threshold_value = value
                                        self.threshold_value.value_namespace = name_space
                                        self.threshold_value.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.aid.is_set or
                                    self.alarm_name.is_set or
                                    self.clear_time.is_set or
                                    self.clear_timestamp.is_set or
                                    self.description.is_set or
                                    self.eid.is_set or
                                    self.group.is_set or
                                    self.interface.is_set or
                                    self.location.is_set or
                                    self.module.is_set or
                                    self.pending_sync.is_set or
                                    self.reporting_agent_id.is_set or
                                    self.service_affecting.is_set or
                                    self.set_time.is_set or
                                    self.set_timestamp.is_set or
                                    self.severity.is_set or
                                    self.status.is_set or
                                    self.tag.is_set or
                                    self.type.is_set or
                                    (self.otn is not None and self.otn.has_data()) or
                                    (self.tca is not None and self.tca.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aid.yfilter != YFilter.not_set or
                                    self.alarm_name.yfilter != YFilter.not_set or
                                    self.clear_time.yfilter != YFilter.not_set or
                                    self.clear_timestamp.yfilter != YFilter.not_set or
                                    self.description.yfilter != YFilter.not_set or
                                    self.eid.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.module.yfilter != YFilter.not_set or
                                    self.pending_sync.yfilter != YFilter.not_set or
                                    self.reporting_agent_id.yfilter != YFilter.not_set or
                                    self.service_affecting.yfilter != YFilter.not_set or
                                    self.set_time.yfilter != YFilter.not_set or
                                    self.set_timestamp.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.tag.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set or
                                    (self.otn is not None and self.otn.has_operation()) or
                                    (self.tca is not None and self.tca.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "alarm-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aid.is_set or self.aid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aid.get_name_leafdata())
                                if (self.alarm_name.is_set or self.alarm_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.alarm_name.get_name_leafdata())
                                if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_time.get_name_leafdata())
                                if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.description.get_name_leafdata())
                                if (self.eid.is_set or self.eid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.eid.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.module.get_name_leafdata())
                                if (self.pending_sync.is_set or self.pending_sync.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pending_sync.get_name_leafdata())
                                if (self.reporting_agent_id.is_set or self.reporting_agent_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reporting_agent_id.get_name_leafdata())
                                if (self.service_affecting.is_set or self.service_affecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_affecting.get_name_leafdata())
                                if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_time.get_name_leafdata())
                                if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.severity.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
                                if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tag.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "otn"):
                                    if (self.otn is None):
                                        self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn()
                                        self.otn.parent = self
                                        self._children_name_map["otn"] = "otn"
                                    return self.otn

                                if (child_yang_name == "tca"):
                                    if (self.tca is None):
                                        self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca()
                                        self.tca.parent = self
                                        self._children_name_map["tca"] = "tca"
                                    return self.tca

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "otn" or name == "tca" or name == "aid" or name == "alarm-name" or name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "eid" or name == "group" or name == "interface" or name == "location" or name == "module" or name == "pending-sync" or name == "reporting-agent-id" or name == "service-affecting" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "status" or name == "tag" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aid"):
                                    self.aid = value
                                    self.aid.value_namespace = name_space
                                    self.aid.value_namespace_prefix = name_space_prefix
                                if(value_path == "alarm-name"):
                                    self.alarm_name = value
                                    self.alarm_name.value_namespace = name_space
                                    self.alarm_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "clear-time"):
                                    self.clear_time = value
                                    self.clear_time.value_namespace = name_space
                                    self.clear_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "clear-timestamp"):
                                    self.clear_timestamp = value
                                    self.clear_timestamp.value_namespace = name_space
                                    self.clear_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "description"):
                                    self.description = value
                                    self.description.value_namespace = name_space
                                    self.description.value_namespace_prefix = name_space_prefix
                                if(value_path == "eid"):
                                    self.eid = value
                                    self.eid.value_namespace = name_space
                                    self.eid.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "module"):
                                    self.module = value
                                    self.module.value_namespace = name_space
                                    self.module.value_namespace_prefix = name_space_prefix
                                if(value_path == "pending-sync"):
                                    self.pending_sync = value
                                    self.pending_sync.value_namespace = name_space
                                    self.pending_sync.value_namespace_prefix = name_space_prefix
                                if(value_path == "reporting-agent-id"):
                                    self.reporting_agent_id = value
                                    self.reporting_agent_id.value_namespace = name_space
                                    self.reporting_agent_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-affecting"):
                                    self.service_affecting = value
                                    self.service_affecting.value_namespace = name_space
                                    self.service_affecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-time"):
                                    self.set_time = value
                                    self.set_time.value_namespace = name_space
                                    self.set_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-timestamp"):
                                    self.set_timestamp = value
                                    self.set_timestamp.value_namespace = name_space
                                    self.set_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix
                                if(value_path == "status"):
                                    self.status = value
                                    self.status.value_namespace = name_space
                                    self.status.value_namespace_prefix = name_space_prefix
                                if(value_path == "tag"):
                                    self.tag = value
                                    self.tag.value_namespace = name_space
                                    self.tag.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.alarm_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.alarm_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "active" + path_buffer

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

                            if (child_yang_name == "alarm-info"):
                                for c in self.alarm_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.alarm_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "alarm-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class History(Entity):
                        """
                        Show the history alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "detail-location"

                            self.alarm_info = YList(self)

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
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History, self).__setattr__(name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn>`
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\:  bool
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting
                            	**type**\:   :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:   :py:class:`AlarmEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEvent>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "history"

                                self.aid = YLeaf(YType.str, "aid")

                                self.alarm_name = YLeaf(YType.str, "alarm-name")

                                self.clear_time = YLeaf(YType.str, "clear-time")

                                self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                                self.description = YLeaf(YType.str, "description")

                                self.eid = YLeaf(YType.str, "eid")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.interface = YLeaf(YType.str, "interface")

                                self.location = YLeaf(YType.str, "location")

                                self.module = YLeaf(YType.str, "module")

                                self.pending_sync = YLeaf(YType.boolean, "pending-sync")

                                self.reporting_agent_id = YLeaf(YType.uint32, "reporting-agent-id")

                                self.service_affecting = YLeaf(YType.enumeration, "service-affecting")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.tag = YLeaf(YType.str, "tag")

                                self.type = YLeaf(YType.enumeration, "type")

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                                self._children_yang_names.add("otn")

                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca()
                                self.tca.parent = self
                                self._children_name_map["tca"] = "tca"
                                self._children_yang_names.add("tca")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("aid",
                                                "alarm_name",
                                                "clear_time",
                                                "clear_timestamp",
                                                "description",
                                                "eid",
                                                "group",
                                                "interface",
                                                "location",
                                                "module",
                                                "pending_sync",
                                                "reporting_agent_id",
                                                "service_affecting",
                                                "set_time",
                                                "set_timestamp",
                                                "severity",
                                                "status",
                                                "tag",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo, self).__setattr__(name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:   :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:   :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "alarm-info"

                                    self.direction = YLeaf(YType.enumeration, "direction")

                                    self.notification_source = YLeaf(YType.enumeration, "notification-source")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("direction",
                                                    "notification_source") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.direction.is_set or
                                        self.notification_source.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.direction.yfilter != YFilter.not_set or
                                        self.notification_source.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "otn" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.direction.get_name_leafdata())
                                    if (self.notification_source.is_set or self.notification_source.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.notification_source.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "direction" or name == "notification-source"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "direction"):
                                        self.direction = value
                                        self.direction.value_namespace = name_space
                                        self.direction.value_namespace_prefix = name_space_prefix
                                    if(value_path == "notification-source"):
                                        self.notification_source = value
                                        self.notification_source.value_namespace = name_space
                                        self.notification_source.value_namespace_prefix = name_space_prefix


                            class Tca(Entity):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:   :py:class:`TimingBucket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucket>`
                                
                                .. attribute:: current_value
                                
                                	Alarm Threshold
                                	**type**\:  str
                                
                                	**length:** 0..20
                                
                                .. attribute:: threshold_value
                                
                                	Alarm Threshold 
                                	**type**\:  str
                                
                                	**length:** 0..20
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca, self).__init__()

                                    self.yang_name = "tca"
                                    self.yang_parent_name = "alarm-info"

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.current_value = YLeaf(YType.str, "current-value")

                                    self.threshold_value = YLeaf(YType.str, "threshold-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bucket_type",
                                                    "current_value",
                                                    "threshold_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.bucket_type.is_set or
                                        self.current_value.is_set or
                                        self.threshold_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bucket_type.yfilter != YFilter.not_set or
                                        self.current_value.yfilter != YFilter.not_set or
                                        self.threshold_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tca" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bucket_type.is_set or self.bucket_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bucket_type.get_name_leafdata())
                                    if (self.current_value.is_set or self.current_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.current_value.get_name_leafdata())
                                    if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.threshold_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bucket-type" or name == "current-value" or name == "threshold-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bucket-type"):
                                        self.bucket_type = value
                                        self.bucket_type.value_namespace = name_space
                                        self.bucket_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "current-value"):
                                        self.current_value = value
                                        self.current_value.value_namespace = name_space
                                        self.current_value.value_namespace_prefix = name_space_prefix
                                    if(value_path == "threshold-value"):
                                        self.threshold_value = value
                                        self.threshold_value.value_namespace = name_space
                                        self.threshold_value.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.aid.is_set or
                                    self.alarm_name.is_set or
                                    self.clear_time.is_set or
                                    self.clear_timestamp.is_set or
                                    self.description.is_set or
                                    self.eid.is_set or
                                    self.group.is_set or
                                    self.interface.is_set or
                                    self.location.is_set or
                                    self.module.is_set or
                                    self.pending_sync.is_set or
                                    self.reporting_agent_id.is_set or
                                    self.service_affecting.is_set or
                                    self.set_time.is_set or
                                    self.set_timestamp.is_set or
                                    self.severity.is_set or
                                    self.status.is_set or
                                    self.tag.is_set or
                                    self.type.is_set or
                                    (self.otn is not None and self.otn.has_data()) or
                                    (self.tca is not None and self.tca.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aid.yfilter != YFilter.not_set or
                                    self.alarm_name.yfilter != YFilter.not_set or
                                    self.clear_time.yfilter != YFilter.not_set or
                                    self.clear_timestamp.yfilter != YFilter.not_set or
                                    self.description.yfilter != YFilter.not_set or
                                    self.eid.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.module.yfilter != YFilter.not_set or
                                    self.pending_sync.yfilter != YFilter.not_set or
                                    self.reporting_agent_id.yfilter != YFilter.not_set or
                                    self.service_affecting.yfilter != YFilter.not_set or
                                    self.set_time.yfilter != YFilter.not_set or
                                    self.set_timestamp.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.tag.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set or
                                    (self.otn is not None and self.otn.has_operation()) or
                                    (self.tca is not None and self.tca.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "alarm-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aid.is_set or self.aid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aid.get_name_leafdata())
                                if (self.alarm_name.is_set or self.alarm_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.alarm_name.get_name_leafdata())
                                if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_time.get_name_leafdata())
                                if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.description.get_name_leafdata())
                                if (self.eid.is_set or self.eid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.eid.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.module.get_name_leafdata())
                                if (self.pending_sync.is_set or self.pending_sync.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pending_sync.get_name_leafdata())
                                if (self.reporting_agent_id.is_set or self.reporting_agent_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reporting_agent_id.get_name_leafdata())
                                if (self.service_affecting.is_set or self.service_affecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_affecting.get_name_leafdata())
                                if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_time.get_name_leafdata())
                                if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.severity.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
                                if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tag.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "otn"):
                                    if (self.otn is None):
                                        self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn()
                                        self.otn.parent = self
                                        self._children_name_map["otn"] = "otn"
                                    return self.otn

                                if (child_yang_name == "tca"):
                                    if (self.tca is None):
                                        self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca()
                                        self.tca.parent = self
                                        self._children_name_map["tca"] = "tca"
                                    return self.tca

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "otn" or name == "tca" or name == "aid" or name == "alarm-name" or name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "eid" or name == "group" or name == "interface" or name == "location" or name == "module" or name == "pending-sync" or name == "reporting-agent-id" or name == "service-affecting" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "status" or name == "tag" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aid"):
                                    self.aid = value
                                    self.aid.value_namespace = name_space
                                    self.aid.value_namespace_prefix = name_space_prefix
                                if(value_path == "alarm-name"):
                                    self.alarm_name = value
                                    self.alarm_name.value_namespace = name_space
                                    self.alarm_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "clear-time"):
                                    self.clear_time = value
                                    self.clear_time.value_namespace = name_space
                                    self.clear_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "clear-timestamp"):
                                    self.clear_timestamp = value
                                    self.clear_timestamp.value_namespace = name_space
                                    self.clear_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "description"):
                                    self.description = value
                                    self.description.value_namespace = name_space
                                    self.description.value_namespace_prefix = name_space_prefix
                                if(value_path == "eid"):
                                    self.eid = value
                                    self.eid.value_namespace = name_space
                                    self.eid.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "module"):
                                    self.module = value
                                    self.module.value_namespace = name_space
                                    self.module.value_namespace_prefix = name_space_prefix
                                if(value_path == "pending-sync"):
                                    self.pending_sync = value
                                    self.pending_sync.value_namespace = name_space
                                    self.pending_sync.value_namespace_prefix = name_space_prefix
                                if(value_path == "reporting-agent-id"):
                                    self.reporting_agent_id = value
                                    self.reporting_agent_id.value_namespace = name_space
                                    self.reporting_agent_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-affecting"):
                                    self.service_affecting = value
                                    self.service_affecting.value_namespace = name_space
                                    self.service_affecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-time"):
                                    self.set_time = value
                                    self.set_time.value_namespace = name_space
                                    self.set_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-timestamp"):
                                    self.set_timestamp = value
                                    self.set_timestamp.value_namespace = name_space
                                    self.set_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix
                                if(value_path == "status"):
                                    self.status = value
                                    self.status.value_namespace = name_space
                                    self.status.value_namespace_prefix = name_space_prefix
                                if(value_path == "tag"):
                                    self.tag = value
                                    self.tag.value_namespace = name_space
                                    self.tag.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.alarm_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.alarm_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "history" + path_buffer

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

                            if (child_yang_name == "alarm-info"):
                                for c in self.alarm_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.alarm_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "alarm-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Suppressed(Entity):
                        """
                        Show the suppressed alarms at this scope.
                        
                        .. attribute:: suppressed_info
                        
                        	Suppressed Alarm List
                        	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed, self).__init__()

                            self.yang_name = "suppressed"
                            self.yang_parent_name = "detail-location"

                            self.suppressed_info = YList(self)

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
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed, self).__setattr__(name, value)


                        class SuppressedInfo(Entity):
                            """
                            Suppressed Alarm List
                            
                            .. attribute:: aid
                            
                            	Alarm aid
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: alarm_name
                            
                            	Alarm name
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: eid
                            
                            	Alarm eid
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: interface
                            
                            	Alarm interface name
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: module
                            
                            	Alarm module description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: otn
                            
                            	OTN feature specific alarm attributes
                            	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn>`
                            
                            .. attribute:: pending_sync
                            
                            	Pending async flag
                            	**type**\:  bool
                            
                            .. attribute:: reporting_agent_id
                            
                            	Reporting agent id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_affecting
                            
                            	Alarm service affecting 
                            	**type**\:   :py:class:`AlarmServiceAffecting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffecting>`
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: suppressed_time
                            
                            	Alarm suppressed time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: suppressed_timestamp
                            
                            	Alarm suppressed time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo, self).__init__()

                                self.yang_name = "suppressed-info"
                                self.yang_parent_name = "suppressed"

                                self.aid = YLeaf(YType.str, "aid")

                                self.alarm_name = YLeaf(YType.str, "alarm-name")

                                self.description = YLeaf(YType.str, "description")

                                self.eid = YLeaf(YType.str, "eid")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.interface = YLeaf(YType.str, "interface")

                                self.location = YLeaf(YType.str, "location")

                                self.module = YLeaf(YType.str, "module")

                                self.pending_sync = YLeaf(YType.boolean, "pending-sync")

                                self.reporting_agent_id = YLeaf(YType.uint32, "reporting-agent-id")

                                self.service_affecting = YLeaf(YType.enumeration, "service-affecting")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.suppressed_time = YLeaf(YType.str, "suppressed-time")

                                self.suppressed_timestamp = YLeaf(YType.uint64, "suppressed-timestamp")

                                self.tag = YLeaf(YType.str, "tag")

                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn()
                                self.otn.parent = self
                                self._children_name_map["otn"] = "otn"
                                self._children_yang_names.add("otn")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("aid",
                                                "alarm_name",
                                                "description",
                                                "eid",
                                                "group",
                                                "interface",
                                                "location",
                                                "module",
                                                "pending_sync",
                                                "reporting_agent_id",
                                                "service_affecting",
                                                "set_time",
                                                "set_timestamp",
                                                "severity",
                                                "status",
                                                "suppressed_time",
                                                "suppressed_timestamp",
                                                "tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo, self).__setattr__(name, value)


                            class Otn(Entity):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:   :py:class:`AlarmDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirection>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:   :py:class:`AlarmNotificationSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrc>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn, self).__init__()

                                    self.yang_name = "otn"
                                    self.yang_parent_name = "suppressed-info"

                                    self.direction = YLeaf(YType.enumeration, "direction")

                                    self.notification_source = YLeaf(YType.enumeration, "notification-source")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("direction",
                                                    "notification_source") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.direction.is_set or
                                        self.notification_source.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.direction.yfilter != YFilter.not_set or
                                        self.notification_source.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "otn" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.direction.get_name_leafdata())
                                    if (self.notification_source.is_set or self.notification_source.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.notification_source.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "direction" or name == "notification-source"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "direction"):
                                        self.direction = value
                                        self.direction.value_namespace = name_space
                                        self.direction.value_namespace_prefix = name_space_prefix
                                    if(value_path == "notification-source"):
                                        self.notification_source = value
                                        self.notification_source.value_namespace = name_space
                                        self.notification_source.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.aid.is_set or
                                    self.alarm_name.is_set or
                                    self.description.is_set or
                                    self.eid.is_set or
                                    self.group.is_set or
                                    self.interface.is_set or
                                    self.location.is_set or
                                    self.module.is_set or
                                    self.pending_sync.is_set or
                                    self.reporting_agent_id.is_set or
                                    self.service_affecting.is_set or
                                    self.set_time.is_set or
                                    self.set_timestamp.is_set or
                                    self.severity.is_set or
                                    self.status.is_set or
                                    self.suppressed_time.is_set or
                                    self.suppressed_timestamp.is_set or
                                    self.tag.is_set or
                                    (self.otn is not None and self.otn.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aid.yfilter != YFilter.not_set or
                                    self.alarm_name.yfilter != YFilter.not_set or
                                    self.description.yfilter != YFilter.not_set or
                                    self.eid.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.module.yfilter != YFilter.not_set or
                                    self.pending_sync.yfilter != YFilter.not_set or
                                    self.reporting_agent_id.yfilter != YFilter.not_set or
                                    self.service_affecting.yfilter != YFilter.not_set or
                                    self.set_time.yfilter != YFilter.not_set or
                                    self.set_timestamp.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.suppressed_time.yfilter != YFilter.not_set or
                                    self.suppressed_timestamp.yfilter != YFilter.not_set or
                                    self.tag.yfilter != YFilter.not_set or
                                    (self.otn is not None and self.otn.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "suppressed-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aid.is_set or self.aid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aid.get_name_leafdata())
                                if (self.alarm_name.is_set or self.alarm_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.alarm_name.get_name_leafdata())
                                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.description.get_name_leafdata())
                                if (self.eid.is_set or self.eid.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.eid.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.module.get_name_leafdata())
                                if (self.pending_sync.is_set or self.pending_sync.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pending_sync.get_name_leafdata())
                                if (self.reporting_agent_id.is_set or self.reporting_agent_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reporting_agent_id.get_name_leafdata())
                                if (self.service_affecting.is_set or self.service_affecting.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_affecting.get_name_leafdata())
                                if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_time.get_name_leafdata())
                                if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.severity.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
                                if (self.suppressed_time.is_set or self.suppressed_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppressed_time.get_name_leafdata())
                                if (self.suppressed_timestamp.is_set or self.suppressed_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppressed_timestamp.get_name_leafdata())
                                if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "otn"):
                                    if (self.otn is None):
                                        self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn()
                                        self.otn.parent = self
                                        self._children_name_map["otn"] = "otn"
                                    return self.otn

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "otn" or name == "aid" or name == "alarm-name" or name == "description" or name == "eid" or name == "group" or name == "interface" or name == "location" or name == "module" or name == "pending-sync" or name == "reporting-agent-id" or name == "service-affecting" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "status" or name == "suppressed-time" or name == "suppressed-timestamp" or name == "tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aid"):
                                    self.aid = value
                                    self.aid.value_namespace = name_space
                                    self.aid.value_namespace_prefix = name_space_prefix
                                if(value_path == "alarm-name"):
                                    self.alarm_name = value
                                    self.alarm_name.value_namespace = name_space
                                    self.alarm_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "description"):
                                    self.description = value
                                    self.description.value_namespace = name_space
                                    self.description.value_namespace_prefix = name_space_prefix
                                if(value_path == "eid"):
                                    self.eid = value
                                    self.eid.value_namespace = name_space
                                    self.eid.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "module"):
                                    self.module = value
                                    self.module.value_namespace = name_space
                                    self.module.value_namespace_prefix = name_space_prefix
                                if(value_path == "pending-sync"):
                                    self.pending_sync = value
                                    self.pending_sync.value_namespace = name_space
                                    self.pending_sync.value_namespace_prefix = name_space_prefix
                                if(value_path == "reporting-agent-id"):
                                    self.reporting_agent_id = value
                                    self.reporting_agent_id.value_namespace = name_space
                                    self.reporting_agent_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-affecting"):
                                    self.service_affecting = value
                                    self.service_affecting.value_namespace = name_space
                                    self.service_affecting.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-time"):
                                    self.set_time = value
                                    self.set_time.value_namespace = name_space
                                    self.set_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-timestamp"):
                                    self.set_timestamp = value
                                    self.set_timestamp.value_namespace = name_space
                                    self.set_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix
                                if(value_path == "status"):
                                    self.status = value
                                    self.status.value_namespace = name_space
                                    self.status.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppressed-time"):
                                    self.suppressed_time = value
                                    self.suppressed_time.value_namespace = name_space
                                    self.suppressed_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppressed-timestamp"):
                                    self.suppressed_timestamp = value
                                    self.suppressed_timestamp.value_namespace = name_space
                                    self.suppressed_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "tag"):
                                    self.tag = value
                                    self.tag.value_namespace = name_space
                                    self.tag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.suppressed_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.suppressed_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "suppressed" + path_buffer

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

                            if (child_yang_name == "suppressed-info"):
                                for c in self.suppressed_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.suppressed_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "suppressed-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Stats(Entity):
                        """
                        Show the service statistics.
                        
                        .. attribute:: active
                        
                        	Alarms that are currently in the active state
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: cache_hit
                        
                        	Total alarms which had the cache hit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cache_miss
                        
                        	Total alarms which had the cache miss
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Alarms that we couldn't keep track due to some error or other
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_clear_without_set
                        
                        	Alarms dropped clear without set
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_db_error
                        
                        	Alarms dropped due to db error
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_duplicate
                        
                        	Alarms dropped which were duplicate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_insuff_mem
                        
                        	Alarms dropped due to insufficient memory
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_invalid_aid
                        
                        	Alarms dropped due to invalid aid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: history
                        
                        	Alarms that are cleared. This one is counted over a long period of time
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: reported
                        
                        	Alarms that were in all reported to this Alarm Mgr
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: suppressed
                        
                        	Alarms that are in suppressed state
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sysadmin_active
                        
                        	Alarms that are currently in the active state(sysadmin plane)
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sysadmin_history
                        
                        	Alarms that are cleared in sysadmin plane. This one is counted over a long period of time
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sysadmin_suppressed
                        
                        	Alarms that are suppressed in sysadmin plane
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "detail-location"

                            self.active = YLeaf(YType.uint64, "active")

                            self.cache_hit = YLeaf(YType.uint32, "cache-hit")

                            self.cache_miss = YLeaf(YType.uint32, "cache-miss")

                            self.dropped = YLeaf(YType.uint64, "dropped")

                            self.dropped_clear_without_set = YLeaf(YType.uint32, "dropped-clear-without-set")

                            self.dropped_db_error = YLeaf(YType.uint32, "dropped-db-error")

                            self.dropped_duplicate = YLeaf(YType.uint32, "dropped-duplicate")

                            self.dropped_insuff_mem = YLeaf(YType.uint32, "dropped-insuff-mem")

                            self.dropped_invalid_aid = YLeaf(YType.uint32, "dropped-invalid-aid")

                            self.history = YLeaf(YType.uint64, "history")

                            self.reported = YLeaf(YType.uint64, "reported")

                            self.suppressed = YLeaf(YType.uint64, "suppressed")

                            self.sysadmin_active = YLeaf(YType.uint64, "sysadmin-active")

                            self.sysadmin_history = YLeaf(YType.uint64, "sysadmin-history")

                            self.sysadmin_suppressed = YLeaf(YType.uint64, "sysadmin-suppressed")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("active",
                                            "cache_hit",
                                            "cache_miss",
                                            "dropped",
                                            "dropped_clear_without_set",
                                            "dropped_db_error",
                                            "dropped_duplicate",
                                            "dropped_insuff_mem",
                                            "dropped_invalid_aid",
                                            "history",
                                            "reported",
                                            "suppressed",
                                            "sysadmin_active",
                                            "sysadmin_history",
                                            "sysadmin_suppressed") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.active.is_set or
                                self.cache_hit.is_set or
                                self.cache_miss.is_set or
                                self.dropped.is_set or
                                self.dropped_clear_without_set.is_set or
                                self.dropped_db_error.is_set or
                                self.dropped_duplicate.is_set or
                                self.dropped_insuff_mem.is_set or
                                self.dropped_invalid_aid.is_set or
                                self.history.is_set or
                                self.reported.is_set or
                                self.suppressed.is_set or
                                self.sysadmin_active.is_set or
                                self.sysadmin_history.is_set or
                                self.sysadmin_suppressed.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.active.yfilter != YFilter.not_set or
                                self.cache_hit.yfilter != YFilter.not_set or
                                self.cache_miss.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.dropped_clear_without_set.yfilter != YFilter.not_set or
                                self.dropped_db_error.yfilter != YFilter.not_set or
                                self.dropped_duplicate.yfilter != YFilter.not_set or
                                self.dropped_insuff_mem.yfilter != YFilter.not_set or
                                self.dropped_invalid_aid.yfilter != YFilter.not_set or
                                self.history.yfilter != YFilter.not_set or
                                self.reported.yfilter != YFilter.not_set or
                                self.suppressed.yfilter != YFilter.not_set or
                                self.sysadmin_active.yfilter != YFilter.not_set or
                                self.sysadmin_history.yfilter != YFilter.not_set or
                                self.sysadmin_suppressed.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.active.get_name_leafdata())
                            if (self.cache_hit.is_set or self.cache_hit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cache_hit.get_name_leafdata())
                            if (self.cache_miss.is_set or self.cache_miss.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cache_miss.get_name_leafdata())
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.dropped_clear_without_set.is_set or self.dropped_clear_without_set.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_clear_without_set.get_name_leafdata())
                            if (self.dropped_db_error.is_set or self.dropped_db_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_db_error.get_name_leafdata())
                            if (self.dropped_duplicate.is_set or self.dropped_duplicate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_duplicate.get_name_leafdata())
                            if (self.dropped_insuff_mem.is_set or self.dropped_insuff_mem.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_insuff_mem.get_name_leafdata())
                            if (self.dropped_invalid_aid.is_set or self.dropped_invalid_aid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_invalid_aid.get_name_leafdata())
                            if (self.history.is_set or self.history.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.history.get_name_leafdata())
                            if (self.reported.is_set or self.reported.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reported.get_name_leafdata())
                            if (self.suppressed.is_set or self.suppressed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.suppressed.get_name_leafdata())
                            if (self.sysadmin_active.is_set or self.sysadmin_active.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sysadmin_active.get_name_leafdata())
                            if (self.sysadmin_history.is_set or self.sysadmin_history.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sysadmin_history.get_name_leafdata())
                            if (self.sysadmin_suppressed.is_set or self.sysadmin_suppressed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sysadmin_suppressed.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "active" or name == "cache-hit" or name == "cache-miss" or name == "dropped" or name == "dropped-clear-without-set" or name == "dropped-db-error" or name == "dropped-duplicate" or name == "dropped-insuff-mem" or name == "dropped-invalid-aid" or name == "history" or name == "reported" or name == "suppressed" or name == "sysadmin-active" or name == "sysadmin-history" or name == "sysadmin-suppressed"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "active"):
                                self.active = value
                                self.active.value_namespace = name_space
                                self.active.value_namespace_prefix = name_space_prefix
                            if(value_path == "cache-hit"):
                                self.cache_hit = value
                                self.cache_hit.value_namespace = name_space
                                self.cache_hit.value_namespace_prefix = name_space_prefix
                            if(value_path == "cache-miss"):
                                self.cache_miss = value
                                self.cache_miss.value_namespace = name_space
                                self.cache_miss.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-clear-without-set"):
                                self.dropped_clear_without_set = value
                                self.dropped_clear_without_set.value_namespace = name_space
                                self.dropped_clear_without_set.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-db-error"):
                                self.dropped_db_error = value
                                self.dropped_db_error.value_namespace = name_space
                                self.dropped_db_error.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-duplicate"):
                                self.dropped_duplicate = value
                                self.dropped_duplicate.value_namespace = name_space
                                self.dropped_duplicate.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-insuff-mem"):
                                self.dropped_insuff_mem = value
                                self.dropped_insuff_mem.value_namespace = name_space
                                self.dropped_insuff_mem.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-invalid-aid"):
                                self.dropped_invalid_aid = value
                                self.dropped_invalid_aid.value_namespace = name_space
                                self.dropped_invalid_aid.value_namespace_prefix = name_space_prefix
                            if(value_path == "history"):
                                self.history = value
                                self.history.value_namespace = name_space
                                self.history.value_namespace_prefix = name_space_prefix
                            if(value_path == "reported"):
                                self.reported = value
                                self.reported.value_namespace = name_space
                                self.reported.value_namespace_prefix = name_space_prefix
                            if(value_path == "suppressed"):
                                self.suppressed = value
                                self.suppressed.value_namespace = name_space
                                self.suppressed.value_namespace_prefix = name_space_prefix
                            if(value_path == "sysadmin-active"):
                                self.sysadmin_active = value
                                self.sysadmin_active.value_namespace = name_space
                                self.sysadmin_active.value_namespace_prefix = name_space_prefix
                            if(value_path == "sysadmin-history"):
                                self.sysadmin_history = value
                                self.sysadmin_history.value_namespace = name_space
                                self.sysadmin_history.value_namespace_prefix = name_space_prefix
                            if(value_path == "sysadmin-suppressed"):
                                self.sysadmin_suppressed = value
                                self.sysadmin_suppressed.value_namespace = name_space
                                self.sysadmin_suppressed.value_namespace_prefix = name_space_prefix


                    class Clients(Entity):
                        """
                        Show the clients associated with this
                        service.
                        
                        .. attribute:: client_info
                        
                        	Client List
                        	**type**\: list of    :py:class:`ClientInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "detail-location"

                            self.client_info = YList(self)

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
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients, self).__setattr__(name, value)


                        class ClientInfo(Entity):
                            """
                            Client List
                            
                            .. attribute:: connect_count
                            
                            	Number of times the agent connected to the alarm mgr
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connect_timestamp
                            
                            	Agent connect timestamp
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: filter_disp
                            
                            	The current subscription status of the client
                            	**type**\:  bool
                            
                            .. attribute:: filter_group
                            
                            	The filter used for alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: filter_severity
                            
                            	The filter used for alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: filter_state
                            
                            	The filter used for alarm bi\-state state+
                            	**type**\:   :py:class:`AlarmStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatus>`
                            
                            .. attribute:: get_count
                            
                            	Number of times the agent queried for alarms
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: handle
                            
                            	The client handle through which interface
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: id
                            
                            	Alarms agent id of the client
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: location
                            
                            	The location of this client
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: name
                            
                            	Alarm client
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: report_count
                            
                            	Number of times the agent reported alarms
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	The current state of the client
                            	**type**\:   :py:class:`AlarmClientState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientState>`
                            
                            .. attribute:: subscribe_count
                            
                            	Number of times the agent subscribed for alarms
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_id
                            
                            	Alarms agent subscriber id of the client
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	The type of the client
                            	**type**\:   :py:class:`AlarmClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClient>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo, self).__init__()

                                self.yang_name = "client-info"
                                self.yang_parent_name = "clients"

                                self.connect_count = YLeaf(YType.uint32, "connect-count")

                                self.connect_timestamp = YLeaf(YType.str, "connect-timestamp")

                                self.filter_disp = YLeaf(YType.boolean, "filter-disp")

                                self.filter_group = YLeaf(YType.enumeration, "filter-group")

                                self.filter_severity = YLeaf(YType.enumeration, "filter-severity")

                                self.filter_state = YLeaf(YType.enumeration, "filter-state")

                                self.get_count = YLeaf(YType.uint32, "get-count")

                                self.handle = YLeaf(YType.str, "handle")

                                self.id = YLeaf(YType.uint32, "id")

                                self.location = YLeaf(YType.str, "location")

                                self.name = YLeaf(YType.str, "name")

                                self.report_count = YLeaf(YType.uint32, "report-count")

                                self.state = YLeaf(YType.enumeration, "state")

                                self.subscribe_count = YLeaf(YType.uint32, "subscribe-count")

                                self.subscriber_id = YLeaf(YType.uint32, "subscriber-id")

                                self.type = YLeaf(YType.enumeration, "type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("connect_count",
                                                "connect_timestamp",
                                                "filter_disp",
                                                "filter_group",
                                                "filter_severity",
                                                "filter_state",
                                                "get_count",
                                                "handle",
                                                "id",
                                                "location",
                                                "name",
                                                "report_count",
                                                "state",
                                                "subscribe_count",
                                                "subscriber_id",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.connect_count.is_set or
                                    self.connect_timestamp.is_set or
                                    self.filter_disp.is_set or
                                    self.filter_group.is_set or
                                    self.filter_severity.is_set or
                                    self.filter_state.is_set or
                                    self.get_count.is_set or
                                    self.handle.is_set or
                                    self.id.is_set or
                                    self.location.is_set or
                                    self.name.is_set or
                                    self.report_count.is_set or
                                    self.state.is_set or
                                    self.subscribe_count.is_set or
                                    self.subscriber_id.is_set or
                                    self.type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.connect_count.yfilter != YFilter.not_set or
                                    self.connect_timestamp.yfilter != YFilter.not_set or
                                    self.filter_disp.yfilter != YFilter.not_set or
                                    self.filter_group.yfilter != YFilter.not_set or
                                    self.filter_severity.yfilter != YFilter.not_set or
                                    self.filter_state.yfilter != YFilter.not_set or
                                    self.get_count.yfilter != YFilter.not_set or
                                    self.handle.yfilter != YFilter.not_set or
                                    self.id.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    self.report_count.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set or
                                    self.subscribe_count.yfilter != YFilter.not_set or
                                    self.subscriber_id.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "client-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.connect_count.is_set or self.connect_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.connect_count.get_name_leafdata())
                                if (self.connect_timestamp.is_set or self.connect_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.connect_timestamp.get_name_leafdata())
                                if (self.filter_disp.is_set or self.filter_disp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.filter_disp.get_name_leafdata())
                                if (self.filter_group.is_set or self.filter_group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.filter_group.get_name_leafdata())
                                if (self.filter_severity.is_set or self.filter_severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.filter_severity.get_name_leafdata())
                                if (self.filter_state.is_set or self.filter_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.filter_state.get_name_leafdata())
                                if (self.get_count.is_set or self.get_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.get_count.get_name_leafdata())
                                if (self.handle.is_set or self.handle.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.handle.get_name_leafdata())
                                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.id.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())
                                if (self.report_count.is_set or self.report_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.report_count.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())
                                if (self.subscribe_count.is_set or self.subscribe_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.subscribe_count.get_name_leafdata())
                                if (self.subscriber_id.is_set or self.subscriber_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.subscriber_id.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "connect-count" or name == "connect-timestamp" or name == "filter-disp" or name == "filter-group" or name == "filter-severity" or name == "filter-state" or name == "get-count" or name == "handle" or name == "id" or name == "location" or name == "name" or name == "report-count" or name == "state" or name == "subscribe-count" or name == "subscriber-id" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "connect-count"):
                                    self.connect_count = value
                                    self.connect_count.value_namespace = name_space
                                    self.connect_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "connect-timestamp"):
                                    self.connect_timestamp = value
                                    self.connect_timestamp.value_namespace = name_space
                                    self.connect_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "filter-disp"):
                                    self.filter_disp = value
                                    self.filter_disp.value_namespace = name_space
                                    self.filter_disp.value_namespace_prefix = name_space_prefix
                                if(value_path == "filter-group"):
                                    self.filter_group = value
                                    self.filter_group.value_namespace = name_space
                                    self.filter_group.value_namespace_prefix = name_space_prefix
                                if(value_path == "filter-severity"):
                                    self.filter_severity = value
                                    self.filter_severity.value_namespace = name_space
                                    self.filter_severity.value_namespace_prefix = name_space_prefix
                                if(value_path == "filter-state"):
                                    self.filter_state = value
                                    self.filter_state.value_namespace = name_space
                                    self.filter_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "get-count"):
                                    self.get_count = value
                                    self.get_count.value_namespace = name_space
                                    self.get_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "handle"):
                                    self.handle = value
                                    self.handle.value_namespace = name_space
                                    self.handle.value_namespace_prefix = name_space_prefix
                                if(value_path == "id"):
                                    self.id = value
                                    self.id.value_namespace = name_space
                                    self.id.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix
                                if(value_path == "report-count"):
                                    self.report_count = value
                                    self.report_count.value_namespace = name_space
                                    self.report_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix
                                if(value_path == "subscribe-count"):
                                    self.subscribe_count = value
                                    self.subscribe_count.value_namespace = name_space
                                    self.subscribe_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "subscriber-id"):
                                    self.subscriber_id = value
                                    self.subscriber_id.value_namespace = name_space
                                    self.subscriber_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.client_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.client_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "clients" + path_buffer

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

                            if (child_yang_name == "client-info"):
                                for c in self.client_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.client_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "client-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.node_id.is_set or
                            (self.active is not None and self.active.has_data()) or
                            (self.clients is not None and self.clients.has_data()) or
                            (self.history is not None and self.history.has_data()) or
                            (self.stats is not None and self.stats.has_data()) or
                            (self.suppressed is not None and self.suppressed.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.node_id.yfilter != YFilter.not_set or
                            (self.active is not None and self.active.has_operation()) or
                            (self.clients is not None and self.clients.has_operation()) or
                            (self.history is not None and self.history.has_operation()) or
                            (self.stats is not None and self.stats.has_operation()) or
                            (self.suppressed is not None and self.suppressed.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "detail-location" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-card/detail-locations/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "active"):
                            if (self.active is None):
                                self.active = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active()
                                self.active.parent = self
                                self._children_name_map["active"] = "active"
                            return self.active

                        if (child_yang_name == "clients"):
                            if (self.clients is None):
                                self.clients = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients()
                                self.clients.parent = self
                                self._children_name_map["clients"] = "clients"
                            return self.clients

                        if (child_yang_name == "history"):
                            if (self.history is None):
                                self.history = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History()
                                self.history.parent = self
                                self._children_name_map["history"] = "history"
                            return self.history

                        if (child_yang_name == "stats"):
                            if (self.stats is None):
                                self.stats = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                            return self.stats

                        if (child_yang_name == "suppressed"):
                            if (self.suppressed is None):
                                self.suppressed = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed()
                                self.suppressed.parent = self
                                self._children_name_map["suppressed"] = "suppressed"
                            return self.suppressed

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active" or name == "clients" or name == "history" or name == "stats" or name == "suppressed" or name == "node-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "node-id"):
                            self.node_id = value
                            self.node_id.value_namespace = name_space
                            self.node_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.detail_location:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.detail_location:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail-locations" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-card/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "detail-location"):
                        for c in self.detail_location:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Detail.DetailCard.DetailLocations.DetailLocation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.detail_location.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "detail-location"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.detail_locations is not None and self.detail_locations.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.detail_locations is not None and self.detail_locations.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "detail-card" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "detail-locations"):
                    if (self.detail_locations is None):
                        self.detail_locations = Alarms.Detail.DetailCard.DetailLocations()
                        self.detail_locations.parent = self
                        self._children_name_map["detail_locations"] = "detail-locations"
                    return self.detail_locations

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "detail-locations"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.detail_card is not None and self.detail_card.has_data()) or
                (self.detail_system is not None and self.detail_system.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.detail_card is not None and self.detail_card.has_operation()) or
                (self.detail_system is not None and self.detail_system.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "detail" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "detail-card"):
                if (self.detail_card is None):
                    self.detail_card = Alarms.Detail.DetailCard()
                    self.detail_card.parent = self
                    self._children_name_map["detail_card"] = "detail-card"
                return self.detail_card

            if (child_yang_name == "detail-system"):
                if (self.detail_system is None):
                    self.detail_system = Alarms.Detail.DetailSystem()
                    self.detail_system.parent = self
                    self._children_name_map["detail_system"] = "detail-system"
                return self.detail_system

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "detail-card" or name == "detail-system"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Brief(Entity):
        """
        A set of brief alarm commands.
        
        .. attribute:: brief_card
        
        	Show brief card scope alarm related data
        	**type**\:   :py:class:`BriefCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard>`
        
        .. attribute:: brief_system
        
        	Show brief system scope alarm related data
        	**type**\:   :py:class:`BriefSystem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem>`
        
        

        """

        _prefix = 'alarmgr-server-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Alarms.Brief, self).__init__()

            self.yang_name = "brief"
            self.yang_parent_name = "alarms"

            self.brief_card = Alarms.Brief.BriefCard()
            self.brief_card.parent = self
            self._children_name_map["brief_card"] = "brief-card"
            self._children_yang_names.add("brief-card")

            self.brief_system = Alarms.Brief.BriefSystem()
            self.brief_system.parent = self
            self._children_name_map["brief_system"] = "brief-system"
            self._children_yang_names.add("brief-system")


        class BriefCard(Entity):
            """
            Show brief card scope alarm related data.
            
            .. attribute:: brief_locations
            
            	Table of BriefLocation
            	**type**\:   :py:class:`BriefLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Brief.BriefCard, self).__init__()

                self.yang_name = "brief-card"
                self.yang_parent_name = "brief"

                self.brief_locations = Alarms.Brief.BriefCard.BriefLocations()
                self.brief_locations.parent = self
                self._children_name_map["brief_locations"] = "brief-locations"
                self._children_yang_names.add("brief-locations")


            class BriefLocations(Entity):
                """
                Table of BriefLocation
                
                .. attribute:: brief_location
                
                	Specify a card location for alarms
                	**type**\: list of    :py:class:`BriefLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefCard.BriefLocations, self).__init__()

                    self.yang_name = "brief-locations"
                    self.yang_parent_name = "brief-card"

                    self.brief_location = YList(self)

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
                                super(Alarms.Brief.BriefCard.BriefLocations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Brief.BriefCard.BriefLocations, self).__setattr__(name, value)


                class BriefLocation(Entity):
                    """
                    Specify a card location for alarms.
                    
                    .. attribute:: node_id  <key>
                    
                    	NodeID of the Location
                    	**type**\:  str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: active
                    
                    	Show the active alarms at this scope
                    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active>`
                    
                    .. attribute:: history
                    
                    	Show the history alarms at this scope
                    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History>`
                    
                    .. attribute:: suppressed
                    
                    	Show the suppressed alarms at this scope
                    	**type**\:   :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation, self).__init__()

                        self.yang_name = "brief-location"
                        self.yang_parent_name = "brief-locations"

                        self.node_id = YLeaf(YType.str, "node-id")

                        self.active = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"
                        self._children_yang_names.add("active")

                        self.history = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"
                        self._children_yang_names.add("history")

                        self.suppressed = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed()
                        self.suppressed.parent = self
                        self._children_name_map["suppressed"] = "suppressed"
                        self._children_yang_names.add("suppressed")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("node_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation, self).__setattr__(name, value)


                    class Active(Entity):
                        """
                        Show the active alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active, self).__init__()

                            self.yang_name = "active"
                            self.yang_parent_name = "brief-location"

                            self.alarm_info = YList(self)

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
                                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active, self).__setattr__(name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "active"

                                self.clear_time = YLeaf(YType.str, "clear-time")

                                self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                                self.description = YLeaf(YType.str, "description")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.location = YLeaf(YType.str, "location")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("clear_time",
                                                "clear_timestamp",
                                                "description",
                                                "group",
                                                "location",
                                                "set_time",
                                                "set_timestamp",
                                                "severity") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.clear_time.is_set or
                                    self.clear_timestamp.is_set or
                                    self.description.is_set or
                                    self.group.is_set or
                                    self.location.is_set or
                                    self.set_time.is_set or
                                    self.set_timestamp.is_set or
                                    self.severity.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.clear_time.yfilter != YFilter.not_set or
                                    self.clear_timestamp.yfilter != YFilter.not_set or
                                    self.description.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.set_time.yfilter != YFilter.not_set or
                                    self.set_timestamp.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "alarm-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_time.get_name_leafdata())
                                if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.description.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_time.get_name_leafdata())
                                if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.severity.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "group" or name == "location" or name == "set-time" or name == "set-timestamp" or name == "severity"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "clear-time"):
                                    self.clear_time = value
                                    self.clear_time.value_namespace = name_space
                                    self.clear_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "clear-timestamp"):
                                    self.clear_timestamp = value
                                    self.clear_timestamp.value_namespace = name_space
                                    self.clear_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "description"):
                                    self.description = value
                                    self.description.value_namespace = name_space
                                    self.description.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-time"):
                                    self.set_time = value
                                    self.set_time.value_namespace = name_space
                                    self.set_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-timestamp"):
                                    self.set_timestamp = value
                                    self.set_timestamp.value_namespace = name_space
                                    self.set_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.alarm_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.alarm_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "active" + path_buffer

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

                            if (child_yang_name == "alarm-info"):
                                for c in self.alarm_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.alarm_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "alarm-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class History(Entity):
                        """
                        Show the history alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "brief-location"

                            self.alarm_info = YList(self)

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
                                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History, self).__setattr__(name, value)


                        class AlarmInfo(Entity):
                            """
                            Alarm List
                            
                            .. attribute:: clear_time
                            
                            	Alarm clear time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: clear_timestamp
                            
                            	Alarm clear time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo, self).__init__()

                                self.yang_name = "alarm-info"
                                self.yang_parent_name = "history"

                                self.clear_time = YLeaf(YType.str, "clear-time")

                                self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                                self.description = YLeaf(YType.str, "description")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.location = YLeaf(YType.str, "location")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("clear_time",
                                                "clear_timestamp",
                                                "description",
                                                "group",
                                                "location",
                                                "set_time",
                                                "set_timestamp",
                                                "severity") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.clear_time.is_set or
                                    self.clear_timestamp.is_set or
                                    self.description.is_set or
                                    self.group.is_set or
                                    self.location.is_set or
                                    self.set_time.is_set or
                                    self.set_timestamp.is_set or
                                    self.severity.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.clear_time.yfilter != YFilter.not_set or
                                    self.clear_timestamp.yfilter != YFilter.not_set or
                                    self.description.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.set_time.yfilter != YFilter.not_set or
                                    self.set_timestamp.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "alarm-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_time.get_name_leafdata())
                                if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.description.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_time.get_name_leafdata())
                                if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.severity.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "group" or name == "location" or name == "set-time" or name == "set-timestamp" or name == "severity"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "clear-time"):
                                    self.clear_time = value
                                    self.clear_time.value_namespace = name_space
                                    self.clear_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "clear-timestamp"):
                                    self.clear_timestamp = value
                                    self.clear_timestamp.value_namespace = name_space
                                    self.clear_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "description"):
                                    self.description = value
                                    self.description.value_namespace = name_space
                                    self.description.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-time"):
                                    self.set_time = value
                                    self.set_time.value_namespace = name_space
                                    self.set_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-timestamp"):
                                    self.set_timestamp = value
                                    self.set_timestamp.value_namespace = name_space
                                    self.set_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.alarm_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.alarm_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "history" + path_buffer

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

                            if (child_yang_name == "alarm-info"):
                                for c in self.alarm_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.alarm_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "alarm-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Suppressed(Entity):
                        """
                        Show the suppressed alarms at this scope.
                        
                        .. attribute:: suppressed_info
                        
                        	Suppressed Alarm List
                        	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed, self).__init__()

                            self.yang_name = "suppressed"
                            self.yang_parent_name = "brief-location"

                            self.suppressed_info = YList(self)

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
                                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed, self).__setattr__(name, value)


                        class SuppressedInfo(Entity):
                            """
                            Suppressed Alarm List
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                            
                            .. attribute:: location
                            
                            	Alarm location
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: set_time
                            
                            	Alarm set time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: set_timestamp
                            
                            	Alarm set time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: severity
                            
                            	Alarm severity
                            	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                            
                            .. attribute:: suppressed_time
                            
                            	Alarm suppressed time
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: suppressed_timestamp
                            
                            	Alarm suppressed time(timestamp format)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo, self).__init__()

                                self.yang_name = "suppressed-info"
                                self.yang_parent_name = "suppressed"

                                self.description = YLeaf(YType.str, "description")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.location = YLeaf(YType.str, "location")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                                self.suppressed_time = YLeaf(YType.str, "suppressed-time")

                                self.suppressed_timestamp = YLeaf(YType.uint64, "suppressed-timestamp")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("description",
                                                "group",
                                                "location",
                                                "set_time",
                                                "set_timestamp",
                                                "severity",
                                                "suppressed_time",
                                                "suppressed_timestamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.description.is_set or
                                    self.group.is_set or
                                    self.location.is_set or
                                    self.set_time.is_set or
                                    self.set_timestamp.is_set or
                                    self.severity.is_set or
                                    self.suppressed_time.is_set or
                                    self.suppressed_timestamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.description.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    self.set_time.yfilter != YFilter.not_set or
                                    self.set_timestamp.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set or
                                    self.suppressed_time.yfilter != YFilter.not_set or
                                    self.suppressed_timestamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "suppressed-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.description.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())
                                if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_time.get_name_leafdata())
                                if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.severity.get_name_leafdata())
                                if (self.suppressed_time.is_set or self.suppressed_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppressed_time.get_name_leafdata())
                                if (self.suppressed_timestamp.is_set or self.suppressed_timestamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppressed_timestamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "description" or name == "group" or name == "location" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "suppressed-time" or name == "suppressed-timestamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "description"):
                                    self.description = value
                                    self.description.value_namespace = name_space
                                    self.description.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-time"):
                                    self.set_time = value
                                    self.set_time.value_namespace = name_space
                                    self.set_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-timestamp"):
                                    self.set_timestamp = value
                                    self.set_timestamp.value_namespace = name_space
                                    self.set_timestamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppressed-time"):
                                    self.suppressed_time = value
                                    self.suppressed_time.value_namespace = name_space
                                    self.suppressed_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppressed-timestamp"):
                                    self.suppressed_timestamp = value
                                    self.suppressed_timestamp.value_namespace = name_space
                                    self.suppressed_timestamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.suppressed_info:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.suppressed_info:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "suppressed" + path_buffer

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

                            if (child_yang_name == "suppressed-info"):
                                for c in self.suppressed_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.suppressed_info.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "suppressed-info"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.node_id.is_set or
                            (self.active is not None and self.active.has_data()) or
                            (self.history is not None and self.history.has_data()) or
                            (self.suppressed is not None and self.suppressed.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.node_id.yfilter != YFilter.not_set or
                            (self.active is not None and self.active.has_operation()) or
                            (self.history is not None and self.history.has_operation()) or
                            (self.suppressed is not None and self.suppressed.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "brief-location" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-card/brief-locations/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "active"):
                            if (self.active is None):
                                self.active = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active()
                                self.active.parent = self
                                self._children_name_map["active"] = "active"
                            return self.active

                        if (child_yang_name == "history"):
                            if (self.history is None):
                                self.history = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History()
                                self.history.parent = self
                                self._children_name_map["history"] = "history"
                            return self.history

                        if (child_yang_name == "suppressed"):
                            if (self.suppressed is None):
                                self.suppressed = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed()
                                self.suppressed.parent = self
                                self._children_name_map["suppressed"] = "suppressed"
                            return self.suppressed

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active" or name == "history" or name == "suppressed" or name == "node-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "node-id"):
                            self.node_id = value
                            self.node_id.value_namespace = name_space
                            self.node_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.brief_location:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.brief_location:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "brief-locations" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-card/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "brief-location"):
                        for c in self.brief_location:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Brief.BriefCard.BriefLocations.BriefLocation()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.brief_location.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "brief-location"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.brief_locations is not None and self.brief_locations.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.brief_locations is not None and self.brief_locations.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "brief-card" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "brief-locations"):
                    if (self.brief_locations is None):
                        self.brief_locations = Alarms.Brief.BriefCard.BriefLocations()
                        self.brief_locations.parent = self
                        self._children_name_map["brief_locations"] = "brief-locations"
                    return self.brief_locations

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "brief-locations"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class BriefSystem(Entity):
            """
            Show brief system scope alarm related data.
            
            .. attribute:: active
            
            	Show the active alarms at this scope
            	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Active>`
            
            .. attribute:: history
            
            	Show the history alarms at this scope
            	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.History>`
            
            .. attribute:: suppressed
            
            	Show the suppressed alarms at this scope
            	**type**\:   :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Suppressed>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Alarms.Brief.BriefSystem, self).__init__()

                self.yang_name = "brief-system"
                self.yang_parent_name = "brief"

                self.active = Alarms.Brief.BriefSystem.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
                self._children_yang_names.add("active")

                self.history = Alarms.Brief.BriefSystem.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"
                self._children_yang_names.add("history")

                self.suppressed = Alarms.Brief.BriefSystem.Suppressed()
                self.suppressed.parent = self
                self._children_name_map["suppressed"] = "suppressed"
                self._children_yang_names.add("suppressed")


            class Active(Entity):
                """
                Show the active alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Active.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "brief-system"

                    self.alarm_info = YList(self)

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
                                super(Alarms.Brief.BriefSystem.Active, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Brief.BriefSystem.Active, self).__setattr__(name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.Active.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "active"

                        self.clear_time = YLeaf(YType.str, "clear-time")

                        self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                        self.description = YLeaf(YType.str, "description")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.location = YLeaf(YType.str, "location")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("clear_time",
                                        "clear_timestamp",
                                        "description",
                                        "group",
                                        "location",
                                        "set_time",
                                        "set_timestamp",
                                        "severity") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Brief.BriefSystem.Active.AlarmInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Brief.BriefSystem.Active.AlarmInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.clear_time.is_set or
                            self.clear_timestamp.is_set or
                            self.description.is_set or
                            self.group.is_set or
                            self.location.is_set or
                            self.set_time.is_set or
                            self.set_timestamp.is_set or
                            self.severity.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.clear_time.yfilter != YFilter.not_set or
                            self.clear_timestamp.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.set_time.yfilter != YFilter.not_set or
                            self.set_timestamp.yfilter != YFilter.not_set or
                            self.severity.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/active/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_time.get_name_leafdata())
                        if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_time.get_name_leafdata())
                        if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                        if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severity.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "group" or name == "location" or name == "set-time" or name == "set-timestamp" or name == "severity"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "clear-time"):
                            self.clear_time = value
                            self.clear_time.value_namespace = name_space
                            self.clear_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-timestamp"):
                            self.clear_timestamp = value
                            self.clear_timestamp.value_namespace = name_space
                            self.clear_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-time"):
                            self.set_time = value
                            self.set_time.value_namespace = name_space
                            self.set_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-timestamp"):
                            self.set_timestamp = value
                            self.set_timestamp.value_namespace = name_space
                            self.set_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "severity"):
                            self.severity = value
                            self.severity.value_namespace = name_space
                            self.severity.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.alarm_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.alarm_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "active" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "alarm-info"):
                        for c in self.alarm_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Brief.BriefSystem.Active.AlarmInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.alarm_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alarm-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class History(Entity):
                """
                Show the history alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.History.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "brief-system"

                    self.alarm_info = YList(self)

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
                                super(Alarms.Brief.BriefSystem.History, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Brief.BriefSystem.History, self).__setattr__(name, value)


                class AlarmInfo(Entity):
                    """
                    Alarm List
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: clear_timestamp
                    
                    	Alarm clear time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.History.AlarmInfo, self).__init__()

                        self.yang_name = "alarm-info"
                        self.yang_parent_name = "history"

                        self.clear_time = YLeaf(YType.str, "clear-time")

                        self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                        self.description = YLeaf(YType.str, "description")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.location = YLeaf(YType.str, "location")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("clear_time",
                                        "clear_timestamp",
                                        "description",
                                        "group",
                                        "location",
                                        "set_time",
                                        "set_timestamp",
                                        "severity") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Brief.BriefSystem.History.AlarmInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Brief.BriefSystem.History.AlarmInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.clear_time.is_set or
                            self.clear_timestamp.is_set or
                            self.description.is_set or
                            self.group.is_set or
                            self.location.is_set or
                            self.set_time.is_set or
                            self.set_timestamp.is_set or
                            self.severity.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.clear_time.yfilter != YFilter.not_set or
                            self.clear_timestamp.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.set_time.yfilter != YFilter.not_set or
                            self.set_timestamp.yfilter != YFilter.not_set or
                            self.severity.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "alarm-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/history/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.clear_time.is_set or self.clear_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_time.get_name_leafdata())
                        if (self.clear_timestamp.is_set or self.clear_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clear_timestamp.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_time.get_name_leafdata())
                        if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                        if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severity.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "clear-time" or name == "clear-timestamp" or name == "description" or name == "group" or name == "location" or name == "set-time" or name == "set-timestamp" or name == "severity"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "clear-time"):
                            self.clear_time = value
                            self.clear_time.value_namespace = name_space
                            self.clear_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "clear-timestamp"):
                            self.clear_timestamp = value
                            self.clear_timestamp.value_namespace = name_space
                            self.clear_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-time"):
                            self.set_time = value
                            self.set_time.value_namespace = name_space
                            self.set_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-timestamp"):
                            self.set_timestamp = value
                            self.set_timestamp.value_namespace = name_space
                            self.set_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "severity"):
                            self.severity = value
                            self.severity.value_namespace = name_space
                            self.severity.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.alarm_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.alarm_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "history" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "alarm-info"):
                        for c in self.alarm_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Brief.BriefSystem.History.AlarmInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.alarm_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alarm-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Suppressed(Entity):
                """
                Show the suppressed alarms at this scope.
                
                .. attribute:: suppressed_info
                
                	Suppressed Alarm List
                	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Alarms.Brief.BriefSystem.Suppressed, self).__init__()

                    self.yang_name = "suppressed"
                    self.yang_parent_name = "brief-system"

                    self.suppressed_info = YList(self)

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
                                super(Alarms.Brief.BriefSystem.Suppressed, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Alarms.Brief.BriefSystem.Suppressed, self).__setattr__(name, value)


                class SuppressedInfo(Entity):
                    """
                    Suppressed Alarm List
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroups>`
                    
                    .. attribute:: location
                    
                    	Alarm location
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: set_time
                    
                    	Alarm set time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: set_timestamp
                    
                    	Alarm set time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: severity
                    
                    	Alarm severity
                    	**type**\:   :py:class:`AlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverity>`
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: suppressed_timestamp
                    
                    	Alarm suppressed time(timestamp format)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo, self).__init__()

                        self.yang_name = "suppressed-info"
                        self.yang_parent_name = "suppressed"

                        self.description = YLeaf(YType.str, "description")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.location = YLeaf(YType.str, "location")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                        self.suppressed_time = YLeaf(YType.str, "suppressed-time")

                        self.suppressed_timestamp = YLeaf(YType.uint64, "suppressed-timestamp")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("description",
                                        "group",
                                        "location",
                                        "set_time",
                                        "set_timestamp",
                                        "severity",
                                        "suppressed_time",
                                        "suppressed_timestamp") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.description.is_set or
                            self.group.is_set or
                            self.location.is_set or
                            self.set_time.is_set or
                            self.set_timestamp.is_set or
                            self.severity.is_set or
                            self.suppressed_time.is_set or
                            self.suppressed_timestamp.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.group.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.set_time.yfilter != YFilter.not_set or
                            self.set_timestamp.yfilter != YFilter.not_set or
                            self.severity.yfilter != YFilter.not_set or
                            self.suppressed_time.yfilter != YFilter.not_set or
                            self.suppressed_timestamp.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "suppressed-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/suppressed/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.set_time.is_set or self.set_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_time.get_name_leafdata())
                        if (self.set_timestamp.is_set or self.set_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.set_timestamp.get_name_leafdata())
                        if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severity.get_name_leafdata())
                        if (self.suppressed_time.is_set or self.suppressed_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.suppressed_time.get_name_leafdata())
                        if (self.suppressed_timestamp.is_set or self.suppressed_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.suppressed_timestamp.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "description" or name == "group" or name == "location" or name == "set-time" or name == "set-timestamp" or name == "severity" or name == "suppressed-time" or name == "suppressed-timestamp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "group"):
                            self.group = value
                            self.group.value_namespace = name_space
                            self.group.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-time"):
                            self.set_time = value
                            self.set_time.value_namespace = name_space
                            self.set_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "set-timestamp"):
                            self.set_timestamp = value
                            self.set_timestamp.value_namespace = name_space
                            self.set_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "severity"):
                            self.severity = value
                            self.severity.value_namespace = name_space
                            self.severity.value_namespace_prefix = name_space_prefix
                        if(value_path == "suppressed-time"):
                            self.suppressed_time = value
                            self.suppressed_time.value_namespace = name_space
                            self.suppressed_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "suppressed-timestamp"):
                            self.suppressed_timestamp = value
                            self.suppressed_timestamp.value_namespace = name_space
                            self.suppressed_timestamp.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.suppressed_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.suppressed_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "suppressed" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "suppressed-info"):
                        for c in self.suppressed_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.suppressed_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "suppressed-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.active is not None and self.active.has_data()) or
                    (self.history is not None and self.history.has_data()) or
                    (self.suppressed is not None and self.suppressed.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.active is not None and self.active.has_operation()) or
                    (self.history is not None and self.history.has_operation()) or
                    (self.suppressed is not None and self.suppressed.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "brief-system" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "active"):
                    if (self.active is None):
                        self.active = Alarms.Brief.BriefSystem.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"
                    return self.active

                if (child_yang_name == "history"):
                    if (self.history is None):
                        self.history = Alarms.Brief.BriefSystem.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"
                    return self.history

                if (child_yang_name == "suppressed"):
                    if (self.suppressed is None):
                        self.suppressed = Alarms.Brief.BriefSystem.Suppressed()
                        self.suppressed.parent = self
                        self._children_name_map["suppressed"] = "suppressed"
                    return self.suppressed

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active" or name == "history" or name == "suppressed"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.brief_card is not None and self.brief_card.has_data()) or
                (self.brief_system is not None and self.brief_system.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.brief_card is not None and self.brief_card.has_operation()) or
                (self.brief_system is not None and self.brief_system.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "brief" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "brief-card"):
                if (self.brief_card is None):
                    self.brief_card = Alarms.Brief.BriefCard()
                    self.brief_card.parent = self
                    self._children_name_map["brief_card"] = "brief-card"
                return self.brief_card

            if (child_yang_name == "brief-system"):
                if (self.brief_system is None):
                    self.brief_system = Alarms.Brief.BriefSystem()
                    self.brief_system.parent = self
                    self._children_name_map["brief_system"] = "brief-system"
                return self.brief_system

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "brief-card" or name == "brief-system"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.brief is not None and self.brief.has_data()) or
            (self.detail is not None and self.detail.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.brief is not None and self.brief.has_operation()) or
            (self.detail is not None and self.detail.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-alarmgr-server-oper:alarms" + path_buffer

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

        if (child_yang_name == "brief"):
            if (self.brief is None):
                self.brief = Alarms.Brief()
                self.brief.parent = self
                self._children_name_map["brief"] = "brief"
            return self.brief

        if (child_yang_name == "detail"):
            if (self.detail is None):
                self.detail = Alarms.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
            return self.detail

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "brief" or name == "detail"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Alarms()
        return self._top_entity

