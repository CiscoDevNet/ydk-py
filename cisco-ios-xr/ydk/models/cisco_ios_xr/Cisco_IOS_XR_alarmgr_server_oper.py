""" Cisco_IOS_XR_alarmgr_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR alarmgr\-server package operational data.

This module contains definitions
for the following management objects\:
  alarms\: Show Alarms associated with XR

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"brief" : ("brief", Alarms.Brief), "detail" : ("detail", Alarms.Detail)}
        self._child_list_classes = {}

        self.brief = Alarms.Brief()
        self.brief.parent = self
        self._children_name_map["brief"] = "brief"
        self._children_yang_names.add("brief")

        self.detail = Alarms.Detail()
        self.detail.parent = self
        self._children_name_map["detail"] = "detail"
        self._children_yang_names.add("detail")
        self._segment_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"brief-card" : ("brief_card", Alarms.Brief.BriefCard), "brief-system" : ("brief_system", Alarms.Brief.BriefSystem)}
            self._child_list_classes = {}

            self.brief_card = Alarms.Brief.BriefCard()
            self.brief_card.parent = self
            self._children_name_map["brief_card"] = "brief-card"
            self._children_yang_names.add("brief-card")

            self.brief_system = Alarms.Brief.BriefSystem()
            self.brief_system.parent = self
            self._children_name_map["brief_system"] = "brief-system"
            self._children_yang_names.add("brief-system")
            self._segment_path = lambda: "brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"brief-locations" : ("brief_locations", Alarms.Brief.BriefCard.BriefLocations)}
                self._child_list_classes = {}

                self.brief_locations = Alarms.Brief.BriefCard.BriefLocations()
                self.brief_locations.parent = self
                self._children_name_map["brief_locations"] = "brief-locations"
                self._children_yang_names.add("brief-locations")
                self._segment_path = lambda: "brief-card"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"brief-location" : ("brief_location", Alarms.Brief.BriefCard.BriefLocations.BriefLocation)}

                    self.brief_location = YList(self)
                    self._segment_path = lambda: "brief-locations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-card/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"active" : ("active", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active), "history" : ("history", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History), "suppressed" : ("suppressed", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "brief-location" + "[node-id='" + self.node_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-card/brief-locations/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation, ['node_id'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo)}

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "active"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.clear_time = YLeaf(YType.str, "clear-time")

                                self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                                self.description = YLeaf(YType.str, "description")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.location = YLeaf(YType.str, "location")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")
                                self._segment_path = lambda: "alarm-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo, ['clear_time', 'clear_timestamp', 'description', 'group', 'location', 'set_time', 'set_timestamp', 'severity'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo)}

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "history"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.clear_time = YLeaf(YType.str, "clear-time")

                                self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                                self.description = YLeaf(YType.str, "description")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.location = YLeaf(YType.str, "location")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")
                                self._segment_path = lambda: "alarm-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo, ['clear_time', 'clear_timestamp', 'description', 'group', 'location', 'set_time', 'set_timestamp', 'severity'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"suppressed-info" : ("suppressed_info", Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo)}

                            self.suppressed_info = YList(self)
                            self._segment_path = lambda: "suppressed"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.description = YLeaf(YType.str, "description")

                                self.group = YLeaf(YType.enumeration, "group")

                                self.location = YLeaf(YType.str, "location")

                                self.set_time = YLeaf(YType.str, "set-time")

                                self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                                self.severity = YLeaf(YType.enumeration, "severity")

                                self.suppressed_time = YLeaf(YType.str, "suppressed-time")

                                self.suppressed_timestamp = YLeaf(YType.uint64, "suppressed-timestamp")
                                self._segment_path = lambda: "suppressed-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo, ['description', 'group', 'location', 'set_time', 'set_timestamp', 'severity', 'suppressed_time', 'suppressed_timestamp'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", Alarms.Brief.BriefSystem.Active), "history" : ("history", Alarms.Brief.BriefSystem.History), "suppressed" : ("suppressed", Alarms.Brief.BriefSystem.Suppressed)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "brief-system"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Brief.BriefSystem.Active.AlarmInfo)}

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.Active, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.clear_time = YLeaf(YType.str, "clear-time")

                        self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                        self.description = YLeaf(YType.str, "description")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.location = YLeaf(YType.str, "location")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/active/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.Active.AlarmInfo, ['clear_time', 'clear_timestamp', 'description', 'group', 'location', 'set_time', 'set_timestamp', 'severity'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Brief.BriefSystem.History.AlarmInfo)}

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "history"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.History, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.clear_time = YLeaf(YType.str, "clear-time")

                        self.clear_timestamp = YLeaf(YType.uint64, "clear-timestamp")

                        self.description = YLeaf(YType.str, "description")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.location = YLeaf(YType.str, "location")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/history/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.History.AlarmInfo, ['clear_time', 'clear_timestamp', 'description', 'group', 'location', 'set_time', 'set_timestamp', 'severity'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"suppressed-info" : ("suppressed_info", Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo)}

                    self.suppressed_info = YList(self)
                    self._segment_path = lambda: "suppressed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Brief.BriefSystem.Suppressed, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.description = YLeaf(YType.str, "description")

                        self.group = YLeaf(YType.enumeration, "group")

                        self.location = YLeaf(YType.str, "location")

                        self.set_time = YLeaf(YType.str, "set-time")

                        self.set_timestamp = YLeaf(YType.uint64, "set-timestamp")

                        self.severity = YLeaf(YType.enumeration, "severity")

                        self.suppressed_time = YLeaf(YType.str, "suppressed-time")

                        self.suppressed_timestamp = YLeaf(YType.uint64, "suppressed-timestamp")
                        self._segment_path = lambda: "suppressed-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/brief/brief-system/suppressed/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo, ['description', 'group', 'location', 'set_time', 'set_timestamp', 'severity', 'suppressed_time', 'suppressed_timestamp'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"detail-card" : ("detail_card", Alarms.Detail.DetailCard), "detail-system" : ("detail_system", Alarms.Detail.DetailSystem)}
            self._child_list_classes = {}

            self.detail_card = Alarms.Detail.DetailCard()
            self.detail_card.parent = self
            self._children_name_map["detail_card"] = "detail-card"
            self._children_yang_names.add("detail-card")

            self.detail_system = Alarms.Detail.DetailSystem()
            self.detail_system.parent = self
            self._children_name_map["detail_system"] = "detail-system"
            self._children_yang_names.add("detail-system")
            self._segment_path = lambda: "detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"detail-locations" : ("detail_locations", Alarms.Detail.DetailCard.DetailLocations)}
                self._child_list_classes = {}

                self.detail_locations = Alarms.Detail.DetailCard.DetailLocations()
                self.detail_locations.parent = self
                self._children_name_map["detail_locations"] = "detail-locations"
                self._children_yang_names.add("detail-locations")
                self._segment_path = lambda: "detail-card"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"detail-location" : ("detail_location", Alarms.Detail.DetailCard.DetailLocations.DetailLocation)}

                    self.detail_location = YList(self)
                    self._segment_path = lambda: "detail-locations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-card/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"active" : ("active", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active), "clients" : ("clients", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients), "history" : ("history", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History), "stats" : ("stats", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats), "suppressed" : ("suppressed", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "detail-location" + "[node-id='" + self.node_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-card/detail-locations/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation, ['node_id'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo)}

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "active"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"otn" : ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn), "tca" : ("tca", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "alarm-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo, ['aid', 'alarm_name', 'clear_time', 'clear_timestamp', 'description', 'eid', 'group', 'interface', 'location', 'module', 'pending_sync', 'reporting_agent_id', 'service_affecting', 'set_time', 'set_timestamp', 'severity', 'status', 'tag', 'type'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.direction = YLeaf(YType.enumeration, "direction")

                                    self.notification_source = YLeaf(YType.enumeration, "notification-source")
                                    self._segment_path = lambda: "otn"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.current_value = YLeaf(YType.str, "current-value")

                                    self.threshold_value = YLeaf(YType.str, "threshold-value")
                                    self._segment_path = lambda: "tca"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca, ['bucket_type', 'current_value', 'threshold_value'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"client-info" : ("client_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo)}

                            self.client_info = YList(self)
                            self._segment_path = lambda: "clients"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "client-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo, ['connect_count', 'connect_timestamp', 'filter_disp', 'filter_group', 'filter_severity', 'filter_state', 'get_count', 'handle', 'id', 'location', 'name', 'report_count', 'state', 'subscribe_count', 'subscriber_id', 'type'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo)}

                            self.alarm_info = YList(self)
                            self._segment_path = lambda: "history"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"otn" : ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn), "tca" : ("tca", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "alarm-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo, ['aid', 'alarm_name', 'clear_time', 'clear_timestamp', 'description', 'eid', 'group', 'interface', 'location', 'module', 'pending_sync', 'reporting_agent_id', 'service_affecting', 'set_time', 'set_timestamp', 'severity', 'status', 'tag', 'type'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.direction = YLeaf(YType.enumeration, "direction")

                                    self.notification_source = YLeaf(YType.enumeration, "notification-source")
                                    self._segment_path = lambda: "otn"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                                    self.current_value = YLeaf(YType.str, "current-value")

                                    self.threshold_value = YLeaf(YType.str, "threshold-value")
                                    self._segment_path = lambda: "tca"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca, ['bucket_type', 'current_value', 'threshold_value'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats, ['active', 'cache_hit', 'cache_miss', 'dropped', 'dropped_clear_without_set', 'dropped_db_error', 'dropped_duplicate', 'dropped_insuff_mem', 'dropped_invalid_aid', 'history', 'reported', 'suppressed', 'sysadmin_active', 'sysadmin_history', 'sysadmin_suppressed'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"suppressed-info" : ("suppressed_info", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo)}

                            self.suppressed_info = YList(self)
                            self._segment_path = lambda: "suppressed"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"otn" : ("otn", Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "suppressed-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo, ['aid', 'alarm_name', 'description', 'eid', 'group', 'interface', 'location', 'module', 'pending_sync', 'reporting_agent_id', 'service_affecting', 'set_time', 'set_timestamp', 'severity', 'status', 'suppressed_time', 'suppressed_timestamp', 'tag'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.direction = YLeaf(YType.enumeration, "direction")

                                    self.notification_source = YLeaf(YType.enumeration, "notification-source")
                                    self._segment_path = lambda: "otn"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn, ['direction', 'notification_source'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"active" : ("active", Alarms.Detail.DetailSystem.Active), "clients" : ("clients", Alarms.Detail.DetailSystem.Clients), "history" : ("history", Alarms.Detail.DetailSystem.History), "stats" : ("stats", Alarms.Detail.DetailSystem.Stats), "suppressed" : ("suppressed", Alarms.Detail.DetailSystem.Suppressed)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "detail-system"
                self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Detail.DetailSystem.Active.AlarmInfo)}

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "active"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Active, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"otn" : ("otn", Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn), "tca" : ("tca", Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Active.AlarmInfo, ['aid', 'alarm_name', 'clear_time', 'clear_timestamp', 'description', 'eid', 'group', 'interface', 'location', 'module', 'pending_sync', 'reporting_agent_id', 'service_affecting', 'set_time', 'set_timestamp', 'severity', 'status', 'tag', 'type'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.notification_source = YLeaf(YType.enumeration, "notification-source")
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/alarm-info/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                            self.current_value = YLeaf(YType.str, "current-value")

                            self.threshold_value = YLeaf(YType.str, "threshold-value")
                            self._segment_path = lambda: "tca"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/active/alarm-info/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca, ['bucket_type', 'current_value', 'threshold_value'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"client-info" : ("client_info", Alarms.Detail.DetailSystem.Clients.ClientInfo)}

                    self.client_info = YList(self)
                    self._segment_path = lambda: "clients"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Clients, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "client-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/clients/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Clients.ClientInfo, ['connect_count', 'connect_timestamp', 'filter_disp', 'filter_group', 'filter_severity', 'filter_state', 'get_count', 'handle', 'id', 'location', 'name', 'report_count', 'state', 'subscribe_count', 'subscriber_id', 'type'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"alarm-info" : ("alarm_info", Alarms.Detail.DetailSystem.History.AlarmInfo)}

                    self.alarm_info = YList(self)
                    self._segment_path = lambda: "history"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.History, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"otn" : ("otn", Alarms.Detail.DetailSystem.History.AlarmInfo.Otn), "tca" : ("tca", Alarms.Detail.DetailSystem.History.AlarmInfo.Tca)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "alarm-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.History.AlarmInfo, ['aid', 'alarm_name', 'clear_time', 'clear_timestamp', 'description', 'eid', 'group', 'interface', 'location', 'module', 'pending_sync', 'reporting_agent_id', 'service_affecting', 'set_time', 'set_timestamp', 'severity', 'status', 'tag', 'type'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.notification_source = YLeaf(YType.enumeration, "notification-source")
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/alarm-info/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.History.AlarmInfo.Otn, ['direction', 'notification_source'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bucket_type = YLeaf(YType.enumeration, "bucket-type")

                            self.current_value = YLeaf(YType.str, "current-value")

                            self.threshold_value = YLeaf(YType.str, "threshold-value")
                            self._segment_path = lambda: "tca"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/history/alarm-info/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.History.AlarmInfo.Tca, ['bucket_type', 'current_value', 'threshold_value'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "stats"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Stats, ['active', 'cache_hit', 'cache_miss', 'dropped', 'dropped_clear_without_set', 'dropped_db_error', 'dropped_duplicate', 'dropped_insuff_mem', 'dropped_invalid_aid', 'history', 'reported', 'suppressed', 'sysadmin_active', 'sysadmin_history', 'sysadmin_suppressed'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"suppressed-info" : ("suppressed_info", Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo)}

                    self.suppressed_info = YList(self)
                    self._segment_path = lambda: "suppressed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Alarms.Detail.DetailSystem.Suppressed, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"otn" : ("otn", Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "suppressed-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/suppressed/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo, ['aid', 'alarm_name', 'description', 'eid', 'group', 'interface', 'location', 'module', 'pending_sync', 'reporting_agent_id', 'service_affecting', 'set_time', 'set_timestamp', 'severity', 'status', 'suppressed_time', 'suppressed_timestamp', 'tag'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.direction = YLeaf(YType.enumeration, "direction")

                            self.notification_source = YLeaf(YType.enumeration, "notification-source")
                            self._segment_path = lambda: "otn"
                            self._absolute_path = lambda: "Cisco-IOS-XR-alarmgr-server-oper:alarms/detail/detail-system/suppressed/suppressed-info/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn, ['direction', 'notification_source'], name, value)

    def clone_ptr(self):
        self._top_entity = Alarms()
        return self._top_entity

