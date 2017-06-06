""" Cisco_IOS_XR_alarmgr_server_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR alarmgr\-server package operational data.

This module contains definitions
for the following management objects\:
  alarms\: Show Alarms associated with XR

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AlarmClientEnum(Enum):
    """
    AlarmClientEnum

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

    unknown = 1

    producer = 2

    consumer = 4

    subscriber = 8

    client_last = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmClientEnum']


class AlarmClientStateEnum(Enum):
    """
    AlarmClientStateEnum

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

    start = 0

    init = 1

    connecting = 2

    connected = 3

    registered = 4

    disconnected = 5

    ready = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmClientStateEnum']


class AlarmDirectionEnum(Enum):
    """
    AlarmDirectionEnum

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

    not_specified = 0

    send = 1

    receive = 2

    send_receive = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmDirectionEnum']


class AlarmEventEnum(Enum):
    """
    AlarmEventEnum

    Alarm event

    .. data:: default = 0

    	Default Alarm Event Type

    .. data:: notification = 1

    	Alarm Notifcation Event Type

    .. data:: last = 2

    	Last Event Type

    """

    default = 0

    notification = 1

    last = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmEventEnum']


class AlarmGroupsEnum(Enum):
    """
    AlarmGroupsEnum

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

    unknown = 0

    environ = 1

    ethernet = 2

    fabric = 3

    power = 4

    software = 5

    slice = 6

    cpu = 7

    controller = 8

    sonet = 9

    otn = 10

    sdh_controller = 11

    asic = 12

    fpd_infra = 13

    shelf = 14

    mpa = 15

    ots = 16

    last = 17


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmGroupsEnum']


class AlarmNotificationSrcEnum(Enum):
    """
    AlarmNotificationSrcEnum

    Alarm notification src

    .. data:: not_specified = 0

    	Notification src not specified

    .. data:: near_end = 1

    	Notification src near end

    .. data:: far_end = 2

    	Notification src far end

    """

    not_specified = 0

    near_end = 1

    far_end = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmNotificationSrcEnum']


class AlarmServiceAffectingEnum(Enum):
    """
    AlarmServiceAffectingEnum

    Alarm service affecting

    .. data:: unknown = 0

    	Unknown whether alarm severity is service

    	affecting

    .. data:: not_service_affecting = 1

    	Alarm severity is not service affecting

    .. data:: service_affecting = 2

    	Alarm severity is service affecting

    """

    unknown = 0

    not_service_affecting = 1

    service_affecting = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmServiceAffectingEnum']


class AlarmSeverityEnum(Enum):
    """
    AlarmSeverityEnum

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

    unknown = 0

    not_reported = 1

    not_alarmed = 2

    minor = 3

    major = 4

    critical = 5

    severity_last = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmSeverityEnum']


class AlarmStatusEnum(Enum):
    """
    AlarmStatusEnum

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

    unknown = 0

    set = 1

    clear = 2

    suppress = 3

    last = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['AlarmStatusEnum']


class TimingBucketEnum(Enum):
    """
    TimingBucketEnum

    Timing bucket

    .. data:: not_specified = 0

    	Bucket Type not applicable

    .. data:: fifteen_min = 1

    	Fifteen minute time bucket

    .. data:: one_day = 2

    	One day time bucket

    """

    not_specified = 0

    fifteen_min = 1

    one_day = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['TimingBucketEnum']



class Alarms(object):
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
        self.brief = Alarms.Brief()
        self.brief.parent = self
        self.detail = Alarms.Detail()
        self.detail.parent = self


    class Detail(object):
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
            self.parent = None
            self.detail_card = Alarms.Detail.DetailCard()
            self.detail_card.parent = self
            self.detail_system = Alarms.Detail.DetailSystem()
            self.detail_system.parent = self


        class DetailSystem(object):
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
                self.parent = None
                self.active = Alarms.Detail.DetailSystem.Active()
                self.active.parent = self
                self.clients = Alarms.Detail.DetailSystem.Clients()
                self.clients.parent = self
                self.history = Alarms.Detail.DetailSystem.History()
                self.history.parent = self
                self.stats = Alarms.Detail.DetailSystem.Stats()
                self.stats.parent = self
                self.suppressed = Alarms.Detail.DetailSystem.Suppressed()
                self.suppressed.parent = self


            class Active(object):
                """
                Show the active alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.alarm_info = YList()
                    self.alarm_info.parent = self
                    self.alarm_info.name = 'alarm_info'


                class AlarmInfo(object):
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
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmServiceAffectingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffectingEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:   :py:class:`AlarmEventEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEventEnum>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.aid = None
                        self.alarm_name = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self.eid = None
                        self.group = None
                        self.interface = None
                        self.location = None
                        self.module = None
                        self.otn = Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn()
                        self.otn.parent = self
                        self.pending_sync = None
                        self.reporting_agent_id = None
                        self.service_affecting = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.severity = None
                        self.status = None
                        self.tag = None
                        self.tca = Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca()
                        self.tca.parent = self
                        self.type = None


                    class Otn(object):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:   :py:class:`AlarmDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirectionEnum>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:   :py:class:`AlarmNotificationSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrcEnum>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.direction = None
                            self.notification_source = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:active/Cisco-IOS-XR-alarmgr-server-oper:alarm-info/Cisco-IOS-XR-alarmgr-server-oper:otn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.direction is not None:
                                return True

                            if self.notification_source is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo.Otn']['meta_info']


                    class Tca(object):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:   :py:class:`TimingBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucketEnum>`
                        
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
                            self.parent = None
                            self.bucket_type = None
                            self.current_value = None
                            self.threshold_value = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:active/Cisco-IOS-XR-alarmgr-server-oper:alarm-info/Cisco-IOS-XR-alarmgr-server-oper:tca'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bucket_type is not None:
                                return True

                            if self.current_value is not None:
                                return True

                            if self.threshold_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo.Tca']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:active/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.aid is not None:
                            return True

                        if self.alarm_name is not None:
                            return True

                        if self.clear_time is not None:
                            return True

                        if self.clear_timestamp is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.eid is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.module is not None:
                            return True

                        if self.otn is not None and self.otn._has_data():
                            return True

                        if self.pending_sync is not None:
                            return True

                        if self.reporting_agent_id is not None:
                            return True

                        if self.service_affecting is not None:
                            return True

                        if self.set_time is not None:
                            return True

                        if self.set_timestamp is not None:
                            return True

                        if self.severity is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.tag is not None:
                            return True

                        if self.tca is not None and self.tca._has_data():
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Detail.DetailSystem.Active.AlarmInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.alarm_info is not None:
                        for child_ref in self.alarm_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Detail.DetailSystem.Active']['meta_info']


            class History(object):
                """
                Show the history alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.alarm_info = YList()
                    self.alarm_info.parent = self
                    self.alarm_info.name = 'alarm_info'


                class AlarmInfo(object):
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
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmServiceAffectingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffectingEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                    
                    .. attribute:: tag
                    
                    	Alarm tag description
                    	**type**\:  str
                    
                    	**length:** 0..128
                    
                    .. attribute:: tca
                    
                    	TCA feature specific alarm attributes
                    	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.History.AlarmInfo.Tca>`
                    
                    .. attribute:: type
                    
                    	alarm event type
                    	**type**\:   :py:class:`AlarmEventEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEventEnum>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.aid = None
                        self.alarm_name = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self.eid = None
                        self.group = None
                        self.interface = None
                        self.location = None
                        self.module = None
                        self.otn = Alarms.Detail.DetailSystem.History.AlarmInfo.Otn()
                        self.otn.parent = self
                        self.pending_sync = None
                        self.reporting_agent_id = None
                        self.service_affecting = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.severity = None
                        self.status = None
                        self.tag = None
                        self.tca = Alarms.Detail.DetailSystem.History.AlarmInfo.Tca()
                        self.tca.parent = self
                        self.type = None


                    class Otn(object):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:   :py:class:`AlarmDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirectionEnum>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:   :py:class:`AlarmNotificationSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrcEnum>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.direction = None
                            self.notification_source = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:history/Cisco-IOS-XR-alarmgr-server-oper:alarm-info/Cisco-IOS-XR-alarmgr-server-oper:otn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.direction is not None:
                                return True

                            if self.notification_source is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo.Otn']['meta_info']


                    class Tca(object):
                        """
                        TCA feature specific alarm attributes
                        
                        .. attribute:: bucket_type
                        
                        	Timing Bucket
                        	**type**\:   :py:class:`TimingBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucketEnum>`
                        
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
                            self.parent = None
                            self.bucket_type = None
                            self.current_value = None
                            self.threshold_value = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:history/Cisco-IOS-XR-alarmgr-server-oper:alarm-info/Cisco-IOS-XR-alarmgr-server-oper:tca'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bucket_type is not None:
                                return True

                            if self.current_value is not None:
                                return True

                            if self.threshold_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo.Tca']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:history/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.aid is not None:
                            return True

                        if self.alarm_name is not None:
                            return True

                        if self.clear_time is not None:
                            return True

                        if self.clear_timestamp is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.eid is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.module is not None:
                            return True

                        if self.otn is not None and self.otn._has_data():
                            return True

                        if self.pending_sync is not None:
                            return True

                        if self.reporting_agent_id is not None:
                            return True

                        if self.service_affecting is not None:
                            return True

                        if self.set_time is not None:
                            return True

                        if self.set_timestamp is not None:
                            return True

                        if self.severity is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.tag is not None:
                            return True

                        if self.tca is not None and self.tca._has_data():
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Detail.DetailSystem.History.AlarmInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:history'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.alarm_info is not None:
                        for child_ref in self.alarm_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Detail.DetailSystem.History']['meta_info']


            class Suppressed(object):
                """
                Show the suppressed alarms at this scope.
                
                .. attribute:: suppressed_info
                
                	Suppressed Alarm List
                	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.suppressed_info = YList()
                    self.suppressed_info.parent = self
                    self.suppressed_info.name = 'suppressed_info'


                class SuppressedInfo(object):
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
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmServiceAffectingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffectingEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
                    .. attribute:: status
                    
                    	Alarm status
                    	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                    
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
                        self.parent = None
                        self.aid = None
                        self.alarm_name = None
                        self.description = None
                        self.eid = None
                        self.group = None
                        self.interface = None
                        self.location = None
                        self.module = None
                        self.otn = Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn()
                        self.otn.parent = self
                        self.pending_sync = None
                        self.reporting_agent_id = None
                        self.service_affecting = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.severity = None
                        self.status = None
                        self.suppressed_time = None
                        self.suppressed_timestamp = None
                        self.tag = None


                    class Otn(object):
                        """
                        OTN feature specific alarm attributes
                        
                        .. attribute:: direction
                        
                        	Alarm direction 
                        	**type**\:   :py:class:`AlarmDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirectionEnum>`
                        
                        .. attribute:: notification_source
                        
                        	Source of Alarm
                        	**type**\:   :py:class:`AlarmNotificationSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrcEnum>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.direction = None
                            self.notification_source = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:suppressed/Cisco-IOS-XR-alarmgr-server-oper:suppressed-info/Cisco-IOS-XR-alarmgr-server-oper:otn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.direction is not None:
                                return True

                            if self.notification_source is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo.Otn']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:suppressed/Cisco-IOS-XR-alarmgr-server-oper:suppressed-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.aid is not None:
                            return True

                        if self.alarm_name is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.eid is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.module is not None:
                            return True

                        if self.otn is not None and self.otn._has_data():
                            return True

                        if self.pending_sync is not None:
                            return True

                        if self.reporting_agent_id is not None:
                            return True

                        if self.service_affecting is not None:
                            return True

                        if self.set_time is not None:
                            return True

                        if self.set_timestamp is not None:
                            return True

                        if self.severity is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.suppressed_time is not None:
                            return True

                        if self.suppressed_timestamp is not None:
                            return True

                        if self.tag is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Detail.DetailSystem.Suppressed.SuppressedInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:suppressed'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.suppressed_info is not None:
                        for child_ref in self.suppressed_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Detail.DetailSystem.Suppressed']['meta_info']


            class Stats(object):
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
                    self.parent = None
                    self.active = None
                    self.cache_hit = None
                    self.cache_miss = None
                    self.dropped = None
                    self.dropped_clear_without_set = None
                    self.dropped_db_error = None
                    self.dropped_duplicate = None
                    self.dropped_insuff_mem = None
                    self.dropped_invalid_aid = None
                    self.history = None
                    self.reported = None
                    self.suppressed = None
                    self.sysadmin_active = None
                    self.sysadmin_history = None
                    self.sysadmin_suppressed = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:stats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active is not None:
                        return True

                    if self.cache_hit is not None:
                        return True

                    if self.cache_miss is not None:
                        return True

                    if self.dropped is not None:
                        return True

                    if self.dropped_clear_without_set is not None:
                        return True

                    if self.dropped_db_error is not None:
                        return True

                    if self.dropped_duplicate is not None:
                        return True

                    if self.dropped_insuff_mem is not None:
                        return True

                    if self.dropped_invalid_aid is not None:
                        return True

                    if self.history is not None:
                        return True

                    if self.reported is not None:
                        return True

                    if self.suppressed is not None:
                        return True

                    if self.sysadmin_active is not None:
                        return True

                    if self.sysadmin_history is not None:
                        return True

                    if self.sysadmin_suppressed is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Detail.DetailSystem.Stats']['meta_info']


            class Clients(object):
                """
                Show the clients associated with this service.
                
                .. attribute:: client_info
                
                	Client List
                	**type**\: list of    :py:class:`ClientInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailSystem.Clients.ClientInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_info = YList()
                    self.client_info.parent = self
                    self.client_info.name = 'client_info'


                class ClientInfo(object):
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
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
                    .. attribute:: filter_severity
                    
                    	The filter used for alarm severity
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
                    .. attribute:: filter_state
                    
                    	The filter used for alarm bi\-state state+
                    	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmClientStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientStateEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmClientEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientEnum>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.connect_count = None
                        self.connect_timestamp = None
                        self.filter_disp = None
                        self.filter_group = None
                        self.filter_severity = None
                        self.filter_state = None
                        self.get_count = None
                        self.handle = None
                        self.id = None
                        self.location = None
                        self.name = None
                        self.report_count = None
                        self.state = None
                        self.subscribe_count = None
                        self.subscriber_id = None
                        self.type = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:clients/Cisco-IOS-XR-alarmgr-server-oper:client-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.connect_count is not None:
                            return True

                        if self.connect_timestamp is not None:
                            return True

                        if self.filter_disp is not None:
                            return True

                        if self.filter_group is not None:
                            return True

                        if self.filter_severity is not None:
                            return True

                        if self.filter_state is not None:
                            return True

                        if self.get_count is not None:
                            return True

                        if self.handle is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.report_count is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.subscribe_count is not None:
                            return True

                        if self.subscriber_id is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Detail.DetailSystem.Clients.ClientInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system/Cisco-IOS-XR-alarmgr-server-oper:clients'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client_info is not None:
                        for child_ref in self.client_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Detail.DetailSystem.Clients']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-system'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.clients is not None and self.clients._has_data():
                    return True

                if self.history is not None and self.history._has_data():
                    return True

                if self.stats is not None and self.stats._has_data():
                    return True

                if self.suppressed is not None and self.suppressed._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                return meta._meta_table['Alarms.Detail.DetailSystem']['meta_info']


        class DetailCard(object):
            """
            Show detail card scope alarm related data.
            
            .. attribute:: detail_locations
            
            	Table of DetailLocation
            	**type**\:   :py:class:`DetailLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.detail_locations = Alarms.Detail.DetailCard.DetailLocations()
                self.detail_locations.parent = self


            class DetailLocations(object):
                """
                Table of DetailLocation
                
                .. attribute:: detail_location
                
                	Specify a card location for alarms
                	**type**\: list of    :py:class:`DetailLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detail_location = YList()
                    self.detail_location.parent = self
                    self.detail_location.name = 'detail_location'


                class DetailLocation(object):
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
                        self.parent = None
                        self.node_id = None
                        self.active = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active()
                        self.active.parent = self
                        self.clients = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients()
                        self.clients.parent = self
                        self.history = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History()
                        self.history.parent = self
                        self.stats = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats()
                        self.stats.parent = self
                        self.suppressed = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed()
                        self.suppressed.parent = self


                    class Active(object):
                        """
                        Show the active alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.alarm_info = YList()
                            self.alarm_info.parent = self
                            self.alarm_info.name = 'alarm_info'


                        class AlarmInfo(object):
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
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmServiceAffectingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffectingEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:   :py:class:`AlarmEventEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEventEnum>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.aid = None
                                self.alarm_name = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self.eid = None
                                self.group = None
                                self.interface = None
                                self.location = None
                                self.module = None
                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn()
                                self.otn.parent = self
                                self.pending_sync = None
                                self.reporting_agent_id = None
                                self.service_affecting = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.severity = None
                                self.status = None
                                self.tag = None
                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca()
                                self.tca.parent = self
                                self.type = None


                            class Otn(object):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:   :py:class:`AlarmDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirectionEnum>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:   :py:class:`AlarmNotificationSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrcEnum>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.direction = None
                                    self.notification_source = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:otn'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.direction is not None:
                                        return True

                                    if self.notification_source is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                    return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Otn']['meta_info']


                            class Tca(object):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:   :py:class:`TimingBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucketEnum>`
                                
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
                                    self.parent = None
                                    self.bucket_type = None
                                    self.current_value = None
                                    self.threshold_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:tca'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bucket_type is not None:
                                        return True

                                    if self.current_value is not None:
                                        return True

                                    if self.threshold_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                    return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo.Tca']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.aid is not None:
                                    return True

                                if self.alarm_name is not None:
                                    return True

                                if self.clear_time is not None:
                                    return True

                                if self.clear_timestamp is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.eid is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.module is not None:
                                    return True

                                if self.otn is not None and self.otn._has_data():
                                    return True

                                if self.pending_sync is not None:
                                    return True

                                if self.reporting_agent_id is not None:
                                    return True

                                if self.service_affecting is not None:
                                    return True

                                if self.set_time is not None:
                                    return True

                                if self.set_timestamp is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.tag is not None:
                                    return True

                                if self.tca is not None and self.tca._has_data():
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active.AlarmInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:active'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.alarm_info is not None:
                                for child_ref in self.alarm_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Active']['meta_info']


                    class History(object):
                        """
                        Show the history alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.alarm_info = YList()
                            self.alarm_info.parent = self
                            self.alarm_info.name = 'alarm_info'


                        class AlarmInfo(object):
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
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmServiceAffectingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffectingEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                            
                            .. attribute:: tag
                            
                            	Alarm tag description
                            	**type**\:  str
                            
                            	**length:** 0..128
                            
                            .. attribute:: tca
                            
                            	TCA feature specific alarm attributes
                            	**type**\:   :py:class:`Tca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca>`
                            
                            .. attribute:: type
                            
                            	alarm event type
                            	**type**\:   :py:class:`AlarmEventEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmEventEnum>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.aid = None
                                self.alarm_name = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self.eid = None
                                self.group = None
                                self.interface = None
                                self.location = None
                                self.module = None
                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn()
                                self.otn.parent = self
                                self.pending_sync = None
                                self.reporting_agent_id = None
                                self.service_affecting = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.severity = None
                                self.status = None
                                self.tag = None
                                self.tca = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca()
                                self.tca.parent = self
                                self.type = None


                            class Otn(object):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:   :py:class:`AlarmDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirectionEnum>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:   :py:class:`AlarmNotificationSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrcEnum>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.direction = None
                                    self.notification_source = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:otn'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.direction is not None:
                                        return True

                                    if self.notification_source is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                    return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Otn']['meta_info']


                            class Tca(object):
                                """
                                TCA feature specific alarm attributes
                                
                                .. attribute:: bucket_type
                                
                                	Timing Bucket
                                	**type**\:   :py:class:`TimingBucketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.TimingBucketEnum>`
                                
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
                                    self.parent = None
                                    self.bucket_type = None
                                    self.current_value = None
                                    self.threshold_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:tca'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bucket_type is not None:
                                        return True

                                    if self.current_value is not None:
                                        return True

                                    if self.threshold_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                    return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo.Tca']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.aid is not None:
                                    return True

                                if self.alarm_name is not None:
                                    return True

                                if self.clear_time is not None:
                                    return True

                                if self.clear_timestamp is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.eid is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.module is not None:
                                    return True

                                if self.otn is not None and self.otn._has_data():
                                    return True

                                if self.pending_sync is not None:
                                    return True

                                if self.reporting_agent_id is not None:
                                    return True

                                if self.service_affecting is not None:
                                    return True

                                if self.set_time is not None:
                                    return True

                                if self.set_timestamp is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.tag is not None:
                                    return True

                                if self.tca is not None and self.tca._has_data():
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History.AlarmInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:history'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.alarm_info is not None:
                                for child_ref in self.alarm_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.History']['meta_info']


                    class Suppressed(object):
                        """
                        Show the suppressed alarms at this scope.
                        
                        .. attribute:: suppressed_info
                        
                        	Suppressed Alarm List
                        	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.suppressed_info = YList()
                            self.suppressed_info.parent = self
                            self.suppressed_info.name = 'suppressed_info'


                        class SuppressedInfo(object):
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
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmServiceAffectingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmServiceAffectingEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
                            .. attribute:: status
                            
                            	Alarm status
                            	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                            
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
                                self.parent = None
                                self.aid = None
                                self.alarm_name = None
                                self.description = None
                                self.eid = None
                                self.group = None
                                self.interface = None
                                self.location = None
                                self.module = None
                                self.otn = Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn()
                                self.otn.parent = self
                                self.pending_sync = None
                                self.reporting_agent_id = None
                                self.service_affecting = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.severity = None
                                self.status = None
                                self.suppressed_time = None
                                self.suppressed_timestamp = None
                                self.tag = None


                            class Otn(object):
                                """
                                OTN feature specific alarm attributes
                                
                                .. attribute:: direction
                                
                                	Alarm direction 
                                	**type**\:   :py:class:`AlarmDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmDirectionEnum>`
                                
                                .. attribute:: notification_source
                                
                                	Source of Alarm
                                	**type**\:   :py:class:`AlarmNotificationSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmNotificationSrcEnum>`
                                
                                

                                """

                                _prefix = 'alarmgr-server-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.direction = None
                                    self.notification_source = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:otn'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.direction is not None:
                                        return True

                                    if self.notification_source is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                    return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo.Otn']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:suppressed-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.aid is not None:
                                    return True

                                if self.alarm_name is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.eid is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.module is not None:
                                    return True

                                if self.otn is not None and self.otn._has_data():
                                    return True

                                if self.pending_sync is not None:
                                    return True

                                if self.reporting_agent_id is not None:
                                    return True

                                if self.service_affecting is not None:
                                    return True

                                if self.set_time is not None:
                                    return True

                                if self.set_timestamp is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.suppressed_time is not None:
                                    return True

                                if self.suppressed_timestamp is not None:
                                    return True

                                if self.tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed.SuppressedInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:suppressed'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.suppressed_info is not None:
                                for child_ref in self.suppressed_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Suppressed']['meta_info']


                    class Stats(object):
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
                            self.parent = None
                            self.active = None
                            self.cache_hit = None
                            self.cache_miss = None
                            self.dropped = None
                            self.dropped_clear_without_set = None
                            self.dropped_db_error = None
                            self.dropped_duplicate = None
                            self.dropped_insuff_mem = None
                            self.dropped_invalid_aid = None
                            self.history = None
                            self.reported = None
                            self.suppressed = None
                            self.sysadmin_active = None
                            self.sysadmin_history = None
                            self.sysadmin_suppressed = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.active is not None:
                                return True

                            if self.cache_hit is not None:
                                return True

                            if self.cache_miss is not None:
                                return True

                            if self.dropped is not None:
                                return True

                            if self.dropped_clear_without_set is not None:
                                return True

                            if self.dropped_db_error is not None:
                                return True

                            if self.dropped_duplicate is not None:
                                return True

                            if self.dropped_insuff_mem is not None:
                                return True

                            if self.dropped_invalid_aid is not None:
                                return True

                            if self.history is not None:
                                return True

                            if self.reported is not None:
                                return True

                            if self.suppressed is not None:
                                return True

                            if self.sysadmin_active is not None:
                                return True

                            if self.sysadmin_history is not None:
                                return True

                            if self.sysadmin_suppressed is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Stats']['meta_info']


                    class Clients(object):
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
                            self.parent = None
                            self.client_info = YList()
                            self.client_info.parent = self
                            self.client_info.name = 'client_info'


                        class ClientInfo(object):
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
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
                            .. attribute:: filter_severity
                            
                            	The filter used for alarm severity
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
                            .. attribute:: filter_state
                            
                            	The filter used for alarm bi\-state state+
                            	**type**\:   :py:class:`AlarmStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmStatusEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmClientStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientStateEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmClientEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmClientEnum>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.connect_count = None
                                self.connect_timestamp = None
                                self.filter_disp = None
                                self.filter_group = None
                                self.filter_severity = None
                                self.filter_state = None
                                self.get_count = None
                                self.handle = None
                                self.id = None
                                self.location = None
                                self.name = None
                                self.report_count = None
                                self.state = None
                                self.subscribe_count = None
                                self.subscriber_id = None
                                self.type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:client-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.connect_count is not None:
                                    return True

                                if self.connect_timestamp is not None:
                                    return True

                                if self.filter_disp is not None:
                                    return True

                                if self.filter_group is not None:
                                    return True

                                if self.filter_severity is not None:
                                    return True

                                if self.filter_state is not None:
                                    return True

                                if self.get_count is not None:
                                    return True

                                if self.handle is not None:
                                    return True

                                if self.id is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.report_count is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.subscribe_count is not None:
                                    return True

                                if self.subscriber_id is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients.ClientInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.client_info is not None:
                                for child_ref in self.client_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation.Clients']['meta_info']

                    @property
                    def _common_path(self):
                        if self.node_id is None:
                            raise YPYModelError('Key property node_id is None')

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-card/Cisco-IOS-XR-alarmgr-server-oper:detail-locations/Cisco-IOS-XR-alarmgr-server-oper:detail-location[Cisco-IOS-XR-alarmgr-server-oper:node-id = ' + str(self.node_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_id is not None:
                            return True

                        if self.active is not None and self.active._has_data():
                            return True

                        if self.clients is not None and self.clients._has_data():
                            return True

                        if self.history is not None and self.history._has_data():
                            return True

                        if self.stats is not None and self.stats._has_data():
                            return True

                        if self.suppressed is not None and self.suppressed._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations.DetailLocation']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-card/Cisco-IOS-XR-alarmgr-server-oper:detail-locations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.detail_location is not None:
                        for child_ref in self.detail_location:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Detail.DetailCard.DetailLocations']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail/Cisco-IOS-XR-alarmgr-server-oper:detail-card'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.detail_locations is not None and self.detail_locations._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                return meta._meta_table['Alarms.Detail.DetailCard']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:detail'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.detail_card is not None and self.detail_card._has_data():
                return True

            if self.detail_system is not None and self.detail_system._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
            return meta._meta_table['Alarms.Detail']['meta_info']


    class Brief(object):
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
            self.parent = None
            self.brief_card = Alarms.Brief.BriefCard()
            self.brief_card.parent = self
            self.brief_system = Alarms.Brief.BriefSystem()
            self.brief_system.parent = self


        class BriefCard(object):
            """
            Show brief card scope alarm related data.
            
            .. attribute:: brief_locations
            
            	Table of BriefLocation
            	**type**\:   :py:class:`BriefLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations>`
            
            

            """

            _prefix = 'alarmgr-server-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.brief_locations = Alarms.Brief.BriefCard.BriefLocations()
                self.brief_locations.parent = self


            class BriefLocations(object):
                """
                Table of BriefLocation
                
                .. attribute:: brief_location
                
                	Specify a card location for alarms
                	**type**\: list of    :py:class:`BriefLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.brief_location = YList()
                    self.brief_location.parent = self
                    self.brief_location.name = 'brief_location'


                class BriefLocation(object):
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
                        self.parent = None
                        self.node_id = None
                        self.active = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active()
                        self.active.parent = self
                        self.history = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History()
                        self.history.parent = self
                        self.suppressed = Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed()
                        self.suppressed.parent = self


                    class Active(object):
                        """
                        Show the active alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.alarm_info = YList()
                            self.alarm_info.parent = self
                            self.alarm_info.name = 'alarm_info'


                        class AlarmInfo(object):
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
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self.group = None
                                self.location = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.severity = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.clear_time is not None:
                                    return True

                                if self.clear_timestamp is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.set_time is not None:
                                    return True

                                if self.set_timestamp is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active.AlarmInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:active'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.alarm_info is not None:
                                for child_ref in self.alarm_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Active']['meta_info']


                    class History(object):
                        """
                        Show the history alarms at this scope.
                        
                        .. attribute:: alarm_info
                        
                        	Alarm List
                        	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.alarm_info = YList()
                            self.alarm_info.parent = self
                            self.alarm_info.name = 'alarm_info'


                        class AlarmInfo(object):
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
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
                            

                            """

                            _prefix = 'alarmgr-server-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.clear_time = None
                                self.clear_timestamp = None
                                self.description = None
                                self.group = None
                                self.location = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.severity = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.clear_time is not None:
                                    return True

                                if self.clear_timestamp is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.set_time is not None:
                                    return True

                                if self.set_timestamp is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History.AlarmInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:history'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.alarm_info is not None:
                                for child_ref in self.alarm_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.History']['meta_info']


                    class Suppressed(object):
                        """
                        Show the suppressed alarms at this scope.
                        
                        .. attribute:: suppressed_info
                        
                        	Suppressed Alarm List
                        	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo>`
                        
                        

                        """

                        _prefix = 'alarmgr-server-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.suppressed_info = YList()
                            self.suppressed_info.parent = self
                            self.suppressed_info.name = 'suppressed_info'


                        class SuppressedInfo(object):
                            """
                            Suppressed Alarm List
                            
                            .. attribute:: description
                            
                            	Alarm description
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: group
                            
                            	Alarm group
                            	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                            
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
                            	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                            
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
                                self.parent = None
                                self.description = None
                                self.group = None
                                self.location = None
                                self.set_time = None
                                self.set_timestamp = None
                                self.severity = None
                                self.suppressed_time = None
                                self.suppressed_timestamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:suppressed-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.description is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                if self.set_time is not None:
                                    return True

                                if self.set_timestamp is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                if self.suppressed_time is not None:
                                    return True

                                if self.suppressed_timestamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                                return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed.SuppressedInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-alarmgr-server-oper:suppressed'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.suppressed_info is not None:
                                for child_ref in self.suppressed_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                            return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation.Suppressed']['meta_info']

                    @property
                    def _common_path(self):
                        if self.node_id is None:
                            raise YPYModelError('Key property node_id is None')

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-card/Cisco-IOS-XR-alarmgr-server-oper:brief-locations/Cisco-IOS-XR-alarmgr-server-oper:brief-location[Cisco-IOS-XR-alarmgr-server-oper:node-id = ' + str(self.node_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.node_id is not None:
                            return True

                        if self.active is not None and self.active._has_data():
                            return True

                        if self.history is not None and self.history._has_data():
                            return True

                        if self.suppressed is not None and self.suppressed._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations.BriefLocation']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-card/Cisco-IOS-XR-alarmgr-server-oper:brief-locations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.brief_location is not None:
                        for child_ref in self.brief_location:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Brief.BriefCard.BriefLocations']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-card'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.brief_locations is not None and self.brief_locations._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                return meta._meta_table['Alarms.Brief.BriefCard']['meta_info']


        class BriefSystem(object):
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
                self.parent = None
                self.active = Alarms.Brief.BriefSystem.Active()
                self.active.parent = self
                self.history = Alarms.Brief.BriefSystem.History()
                self.history.parent = self
                self.suppressed = Alarms.Brief.BriefSystem.Suppressed()
                self.suppressed.parent = self


            class Active(object):
                """
                Show the active alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Active.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.alarm_info = YList()
                    self.alarm_info.parent = self
                    self.alarm_info.name = 'alarm_info'


                class AlarmInfo(object):
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
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self.group = None
                        self.location = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.severity = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system/Cisco-IOS-XR-alarmgr-server-oper:active/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.clear_time is not None:
                            return True

                        if self.clear_timestamp is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.set_time is not None:
                            return True

                        if self.set_timestamp is not None:
                            return True

                        if self.severity is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Brief.BriefSystem.Active.AlarmInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system/Cisco-IOS-XR-alarmgr-server-oper:active'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.alarm_info is not None:
                        for child_ref in self.alarm_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Brief.BriefSystem.Active']['meta_info']


            class History(object):
                """
                Show the history alarms at this scope.
                
                .. attribute:: alarm_info
                
                	Alarm List
                	**type**\: list of    :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.History.AlarmInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.alarm_info = YList()
                    self.alarm_info.parent = self
                    self.alarm_info.name = 'alarm_info'


                class AlarmInfo(object):
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
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
                    

                    """

                    _prefix = 'alarmgr-server-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clear_time = None
                        self.clear_timestamp = None
                        self.description = None
                        self.group = None
                        self.location = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.severity = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system/Cisco-IOS-XR-alarmgr-server-oper:history/Cisco-IOS-XR-alarmgr-server-oper:alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.clear_time is not None:
                            return True

                        if self.clear_timestamp is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.set_time is not None:
                            return True

                        if self.set_timestamp is not None:
                            return True

                        if self.severity is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Brief.BriefSystem.History.AlarmInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system/Cisco-IOS-XR-alarmgr-server-oper:history'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.alarm_info is not None:
                        for child_ref in self.alarm_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Brief.BriefSystem.History']['meta_info']


            class Suppressed(object):
                """
                Show the suppressed alarms at this scope.
                
                .. attribute:: suppressed_info
                
                	Suppressed Alarm List
                	**type**\: list of    :py:class:`SuppressedInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo>`
                
                

                """

                _prefix = 'alarmgr-server-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.suppressed_info = YList()
                    self.suppressed_info.parent = self
                    self.suppressed_info.name = 'suppressed_info'


                class SuppressedInfo(object):
                    """
                    Suppressed Alarm List
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: group
                    
                    	Alarm group
                    	**type**\:   :py:class:`AlarmGroupsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmGroupsEnum>`
                    
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
                    	**type**\:   :py:class:`AlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_alarmgr_server_oper.AlarmSeverityEnum>`
                    
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
                        self.parent = None
                        self.description = None
                        self.group = None
                        self.location = None
                        self.set_time = None
                        self.set_timestamp = None
                        self.severity = None
                        self.suppressed_time = None
                        self.suppressed_timestamp = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system/Cisco-IOS-XR-alarmgr-server-oper:suppressed/Cisco-IOS-XR-alarmgr-server-oper:suppressed-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.description is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.set_time is not None:
                            return True

                        if self.set_timestamp is not None:
                            return True

                        if self.severity is not None:
                            return True

                        if self.suppressed_time is not None:
                            return True

                        if self.suppressed_timestamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                        return meta._meta_table['Alarms.Brief.BriefSystem.Suppressed.SuppressedInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system/Cisco-IOS-XR-alarmgr-server-oper:suppressed'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.suppressed_info is not None:
                        for child_ref in self.suppressed_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                    return meta._meta_table['Alarms.Brief.BriefSystem.Suppressed']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief/Cisco-IOS-XR-alarmgr-server-oper:brief-system'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active is not None and self.active._has_data():
                    return True

                if self.history is not None and self.history._has_data():
                    return True

                if self.suppressed is not None and self.suppressed._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
                return meta._meta_table['Alarms.Brief.BriefSystem']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-alarmgr-server-oper:alarms/Cisco-IOS-XR-alarmgr-server-oper:brief'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.brief_card is not None and self.brief_card._has_data():
                return True

            if self.brief_system is not None and self.brief_system._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
            return meta._meta_table['Alarms.Brief']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-alarmgr-server-oper:alarms'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.brief is not None and self.brief._has_data():
            return True

        if self.detail is not None and self.detail._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_alarmgr_server_oper as meta
        return meta._meta_table['Alarms']['meta_info']


