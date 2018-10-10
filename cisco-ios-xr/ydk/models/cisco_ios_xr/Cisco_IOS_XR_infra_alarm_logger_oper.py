""" Cisco_IOS_XR_infra_alarm_logger_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-alarm\-logger package operational data.

This module contains definitions
for the following management objects\:
  alarm\-logger\: Alarm Logger operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AlAlarmBistate(Enum):
    """
    AlAlarmBistate (Enum Class)

    Al alarm bistate

    .. data:: not_available = 0

    	not available

    .. data:: active = 1

    	active

    .. data:: clear = 2

    	clear

    """

    not_available = Enum.YLeaf(0, "not-available")

    active = Enum.YLeaf(1, "active")

    clear = Enum.YLeaf(2, "clear")


class AlAlarmSeverity(Enum):
    """
    AlAlarmSeverity (Enum Class)

    Al alarm severity

    .. data:: unknown = -1

    	unknown

    .. data:: emergency = 0

    	emergency

    .. data:: alert = 1

    	alert

    .. data:: critical = 2

    	critical

    .. data:: error = 3

    	error

    .. data:: warning = 4

    	warning

    .. data:: notice = 5

    	notice

    .. data:: informational = 6

    	informational

    .. data:: debugging = 7

    	debugging

    """

    unknown = Enum.YLeaf(-1, "unknown")

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    informational = Enum.YLeaf(6, "informational")

    debugging = Enum.YLeaf(7, "debugging")



class AlarmLogger(Entity):
    """
    Alarm Logger operational data
    
    .. attribute:: buffer_status
    
    	Describes buffer utilization and parameters configured
    	**type**\:  :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.BufferStatus>`
    
    .. attribute:: alarms
    
    	Table that contains the database of logged alarms
    	**type**\:  :py:class:`Alarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.Alarms>`
    
    

    """

    _prefix = 'infra-alarm-logger-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(AlarmLogger, self).__init__()
        self._top_entity = None

        self.yang_name = "alarm-logger"
        self.yang_parent_name = "Cisco-IOS-XR-infra-alarm-logger-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("buffer-status", ("buffer_status", AlarmLogger.BufferStatus)), ("alarms", ("alarms", AlarmLogger.Alarms))])
        self._leafs = OrderedDict()

        self.buffer_status = AlarmLogger.BufferStatus()
        self.buffer_status.parent = self
        self._children_name_map["buffer_status"] = "buffer-status"

        self.alarms = AlarmLogger.Alarms()
        self.alarms.parent = self
        self._children_name_map["alarms"] = "alarms"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AlarmLogger, [], name, value)


    class BufferStatus(Entity):
        """
        Describes buffer utilization and parameters
        configured
        
        .. attribute:: log_buffer_size
        
        	Current Logging Buffer Size (Bytes)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: byte
        
        .. attribute:: max_log_buffer_size
        
        	Maximum Logging Buffer Size (Bytes) 
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: byte
        
        .. attribute:: record_count
        
        	Number of Records in the Buffer
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: capacity_threshold
        
        	Percentage of the buffer utilization which, when exceeded, triggers the  generation of a notification for the clients of the XML agent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: percentage
        
        .. attribute:: severity_filter
        
        	Severity Filter
        	**type**\:  :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmSeverity>`
        
        

        """

        _prefix = 'infra-alarm-logger-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(AlarmLogger.BufferStatus, self).__init__()

            self.yang_name = "buffer-status"
            self.yang_parent_name = "alarm-logger"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('log_buffer_size', (YLeaf(YType.uint32, 'log-buffer-size'), ['int'])),
                ('max_log_buffer_size', (YLeaf(YType.uint32, 'max-log-buffer-size'), ['int'])),
                ('record_count', (YLeaf(YType.uint32, 'record-count'), ['int'])),
                ('capacity_threshold', (YLeaf(YType.uint32, 'capacity-threshold'), ['int'])),
                ('severity_filter', (YLeaf(YType.enumeration, 'severity-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverity', '')])),
            ])
            self.log_buffer_size = None
            self.max_log_buffer_size = None
            self.record_count = None
            self.capacity_threshold = None
            self.severity_filter = None
            self._segment_path = lambda: "buffer-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AlarmLogger.BufferStatus, ['log_buffer_size', 'max_log_buffer_size', 'record_count', 'capacity_threshold', 'severity_filter'], name, value)


    class Alarms(Entity):
        """
        Table that contains the database of logged
        alarms
        
        .. attribute:: alarm
        
        	One of the logged alarms
        	**type**\: list of  		 :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.Alarms.Alarm>`
        
        

        """

        _prefix = 'infra-alarm-logger-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(AlarmLogger.Alarms, self).__init__()

            self.yang_name = "alarms"
            self.yang_parent_name = "alarm-logger"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alarm", ("alarm", AlarmLogger.Alarms.Alarm))])
            self._leafs = OrderedDict()

            self.alarm = YList(self)
            self._segment_path = lambda: "alarms"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AlarmLogger.Alarms, [], name, value)


        class Alarm(Entity):
            """
            One of the logged alarms
            
            .. attribute:: event_id  (key)
            
            	Event ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: source_id
            
            	Source Identifier(Location).Indicates the node in which the alarm was generated
            	**type**\: str
            
            .. attribute:: timestamp
            
            	Time when the alarm was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: millisecond
            
            .. attribute:: category
            
            	Category of the alarm
            	**type**\: str
            
            .. attribute:: group
            
            	Group of messages to which this alarm belongs to
            	**type**\: str
            
            .. attribute:: code
            
            	Alarm code which further qualifies the alarm within a message group
            	**type**\: str
            
            .. attribute:: severity
            
            	Severity of the alarm
            	**type**\:  :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmSeverity>`
            
            .. attribute:: state
            
            	State of the alarm (bistate alarms only)
            	**type**\:  :py:class:`AlAlarmBistate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmBistate>`
            
            .. attribute:: correlation_id
            
            	Correlation Identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_admin
            
            	Indicates the event id admin\-level
            	**type**\: bool
            
            .. attribute:: additional_text
            
            	Full text of the Alarm
            	**type**\: str
            
            

            """

            _prefix = 'infra-alarm-logger-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(AlarmLogger.Alarms.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "alarms"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['event_id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('event_id', (YLeaf(YType.uint32, 'event-id'), ['int'])),
                    ('source_id', (YLeaf(YType.str, 'source-id'), ['str'])),
                    ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                    ('category', (YLeaf(YType.str, 'category'), ['str'])),
                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                    ('code', (YLeaf(YType.str, 'code'), ['str'])),
                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmSeverity', '')])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper', 'AlAlarmBistate', '')])),
                    ('correlation_id', (YLeaf(YType.uint32, 'correlation-id'), ['int'])),
                    ('is_admin', (YLeaf(YType.boolean, 'is-admin'), ['bool'])),
                    ('additional_text', (YLeaf(YType.str, 'additional-text'), ['str'])),
                ])
                self.event_id = None
                self.source_id = None
                self.timestamp = None
                self.category = None
                self.group = None
                self.code = None
                self.severity = None
                self.state = None
                self.correlation_id = None
                self.is_admin = None
                self.additional_text = None
                self._segment_path = lambda: "alarm" + "[event-id='" + str(self.event_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/alarms/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmLogger.Alarms.Alarm, ['event_id', 'source_id', 'timestamp', 'category', 'group', 'code', 'severity', 'state', 'correlation_id', 'is_admin', 'additional_text'], name, value)

    def clone_ptr(self):
        self._top_entity = AlarmLogger()
        return self._top_entity

