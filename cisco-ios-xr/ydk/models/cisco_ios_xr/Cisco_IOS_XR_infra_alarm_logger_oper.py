""" Cisco_IOS_XR_infra_alarm_logger_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-alarm\-logger package operational data.

This module contains definitions
for the following management objects\:
  alarm\-logger\: Alarm Logger operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AlAlarmBistateEnum(Enum):
    """
    AlAlarmBistateEnum

    Al alarm bistate

    .. data:: not_available = 0

    	not available

    .. data:: active = 1

    	active

    .. data:: clear = 2

    	clear

    """

    not_available = 0

    active = 1

    clear = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_oper as meta
        return meta._meta_table['AlAlarmBistateEnum']


class AlAlarmSeverityEnum(Enum):
    """
    AlAlarmSeverityEnum

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

    unknown = -1

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    informational = 6

    debugging = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_oper as meta
        return meta._meta_table['AlAlarmSeverityEnum']



class AlarmLogger(object):
    """
    Alarm Logger operational data
    
    .. attribute:: alarms
    
    	Table that contains the database of logged alarms
    	**type**\:   :py:class:`Alarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.Alarms>`
    
    .. attribute:: buffer_status
    
    	Describes buffer utilization and parameters configured
    	**type**\:   :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.BufferStatus>`
    
    

    """

    _prefix = 'infra-alarm-logger-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.alarms = AlarmLogger.Alarms()
        self.alarms.parent = self
        self.buffer_status = AlarmLogger.BufferStatus()
        self.buffer_status.parent = self


    class BufferStatus(object):
        """
        Describes buffer utilization and parameters
        configured
        
        .. attribute:: capacity_threshold
        
        	Percentage of the buffer utilization which, when exceeded, triggers the  generation of a notification for the clients of the XML agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: percentage
        
        .. attribute:: log_buffer_size
        
        	Current Logging Buffer Size (Bytes)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: byte
        
        .. attribute:: max_log_buffer_size
        
        	Maximum Logging Buffer Size (Bytes) 
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: byte
        
        .. attribute:: record_count
        
        	Number of Records in the Buffer
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: severity_filter
        
        	Severity Filter
        	**type**\:   :py:class:`AlAlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmSeverityEnum>`
        
        

        """

        _prefix = 'infra-alarm-logger-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.capacity_threshold = None
            self.log_buffer_size = None
            self.max_log_buffer_size = None
            self.record_count = None
            self.severity_filter = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/Cisco-IOS-XR-infra-alarm-logger-oper:buffer-status'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.capacity_threshold is not None:
                return True

            if self.log_buffer_size is not None:
                return True

            if self.max_log_buffer_size is not None:
                return True

            if self.record_count is not None:
                return True

            if self.severity_filter is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_oper as meta
            return meta._meta_table['AlarmLogger.BufferStatus']['meta_info']


    class Alarms(object):
        """
        Table that contains the database of logged
        alarms
        
        .. attribute:: alarm
        
        	One of the logged alarms
        	**type**\: list of    :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.Alarms.Alarm>`
        
        

        """

        _prefix = 'infra-alarm-logger-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.alarm = YList()
            self.alarm.parent = self
            self.alarm.name = 'alarm'


        class Alarm(object):
            """
            One of the logged alarms
            
            .. attribute:: event_id  <key>
            
            	Event ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: additional_text
            
            	Full text of the Alarm
            	**type**\:  str
            
            .. attribute:: category
            
            	Category of the alarm
            	**type**\:  str
            
            .. attribute:: code
            
            	Alarm code which further qualifies the alarm within a message group
            	**type**\:  str
            
            .. attribute:: correlation_id
            
            	Correlation Identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: group
            
            	Group of messages to which this alarm belongs to
            	**type**\:  str
            
            .. attribute:: is_admin
            
            	Indicates the event id admin\-level
            	**type**\:  bool
            
            .. attribute:: severity
            
            	Severity of the alarm
            	**type**\:   :py:class:`AlAlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmSeverityEnum>`
            
            .. attribute:: source_id
            
            	Source Identifier(Location).Indicates the node in which the alarm was generated
            	**type**\:  str
            
            .. attribute:: state
            
            	State of the alarm (bistate alarms only)
            	**type**\:   :py:class:`AlAlarmBistateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmBistateEnum>`
            
            .. attribute:: timestamp
            
            	Time when the alarm was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: millisecond
            
            

            """

            _prefix = 'infra-alarm-logger-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.event_id = None
                self.additional_text = None
                self.category = None
                self.code = None
                self.correlation_id = None
                self.group = None
                self.is_admin = None
                self.severity = None
                self.source_id = None
                self.state = None
                self.timestamp = None

            @property
            def _common_path(self):
                if self.event_id is None:
                    raise YPYModelError('Key property event_id is None')

                return '/Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/Cisco-IOS-XR-infra-alarm-logger-oper:alarms/Cisco-IOS-XR-infra-alarm-logger-oper:alarm[Cisco-IOS-XR-infra-alarm-logger-oper:event-id = ' + str(self.event_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.event_id is not None:
                    return True

                if self.additional_text is not None:
                    return True

                if self.category is not None:
                    return True

                if self.code is not None:
                    return True

                if self.correlation_id is not None:
                    return True

                if self.group is not None:
                    return True

                if self.is_admin is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.source_id is not None:
                    return True

                if self.state is not None:
                    return True

                if self.timestamp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_oper as meta
                return meta._meta_table['AlarmLogger.Alarms.Alarm']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/Cisco-IOS-XR-infra-alarm-logger-oper:alarms'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.alarm is not None:
                for child_ref in self.alarm:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_oper as meta
            return meta._meta_table['AlarmLogger.Alarms']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.alarms is not None and self.alarms._has_data():
            return True

        if self.buffer_status is not None and self.buffer_status._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_oper as meta
        return meta._meta_table['AlarmLogger']['meta_info']


