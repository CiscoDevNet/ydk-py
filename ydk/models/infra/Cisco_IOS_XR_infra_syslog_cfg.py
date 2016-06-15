""" Cisco_IOS_XR_infra_syslog_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-syslog package configuration.

This module contains definitions
for the following management objects\:
  syslog\-service\: Syslog Timestamp Services
  syslog\: syslog

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.infra.Cisco_IOS_XR_infra_alarm_logger_datatypes import AlarmLoggerSeverityLevelEnum

class FacilityEnum(Enum):
    """
    FacilityEnum

    Facility

    .. data:: KERN = 0

    	Kernel Facility

    .. data:: USER = 8

    	User Facility

    .. data:: MAIL = 16

    	Mail Facility

    .. data:: DAEMON = 24

    	Daemon Facility

    .. data:: AUTH = 32

    	Auth Facility

    .. data:: SYSLOG = 40

    	Syslog Facility

    .. data:: LPR = 48

    	Lpr Facility

    .. data:: NEWS = 56

    	News Facility

    .. data:: UUCP = 64

    	Uucp Facility

    .. data:: CRON = 72

    	Cron Facility

    .. data:: AUTHPRIV = 80

    	Authpriv Facility

    .. data:: FTP = 88

    	Ftp Facility

    .. data:: LOCAL0 = 128

    	Local0 Facility

    .. data:: LOCAL1 = 136

    	Local1 Facility

    .. data:: LOCAL2 = 144

    	Local2 Facility

    .. data:: LOCAL3 = 152

    	Local3 Facility

    .. data:: LOCAL4 = 160

    	Local4 Facility

    .. data:: LOCAL5 = 168

    	Local5 Facility

    .. data:: LOCAL6 = 176

    	Local6 Facility

    .. data:: LOCAL7 = 184

    	Local7 Facility

    .. data:: SYS9 = 192

    	System9 Facility

    .. data:: SYS10 = 200

    	System10 Facility

    .. data:: SYS11 = 208

    	System11 Facility

    .. data:: SYS12 = 216

    	System12 Facility

    .. data:: SYS13 = 224

    	System13 Facility

    .. data:: SYS14 = 232

    	System14 Facility

    """

    KERN = 0

    USER = 8

    MAIL = 16

    DAEMON = 24

    AUTH = 32

    SYSLOG = 40

    LPR = 48

    NEWS = 56

    UUCP = 64

    CRON = 72

    AUTHPRIV = 80

    FTP = 88

    LOCAL0 = 128

    LOCAL1 = 136

    LOCAL2 = 144

    LOCAL3 = 152

    LOCAL4 = 160

    LOCAL5 = 168

    LOCAL6 = 176

    LOCAL7 = 184

    SYS9 = 192

    SYS10 = 200

    SYS11 = 208

    SYS12 = 216

    SYS13 = 224

    SYS14 = 232


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['FacilityEnum']


class LogCollectFrequencyEnum(Enum):
    """
    LogCollectFrequencyEnum

    Log collect frequency

    .. data:: WEEKLY = 1

    	Collect log in files on a weekly basis

    .. data:: DAILY = 2

    	Collect log in files on a daily basis

    """

    WEEKLY = 1

    DAILY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LogCollectFrequencyEnum']


class LogMessageSeverityEnum(Enum):
    """
    LogMessageSeverityEnum

    Log message severity

    .. data:: EMERGENCY = 0

    	System is unusable                (severity=0)

    .. data:: ALERT = 1

    	Immediate action needed           (severity=1)

    .. data:: CRITICAL = 2

    	Critical conditions               (severity=2)

    .. data:: ERROR = 3

    	Error conditions                  (severity=3)

    .. data:: WARNING = 4

    	Warning conditions                (severity=4)

    .. data:: NOTICE = 5

    	Normal but significant conditions (severity=5)

    .. data:: INFORMATIONAL = 6

    	Informational messages            (severity=6)

    .. data:: DEBUG = 7

    	Debugging messages                (severity=7)

    """

    EMERGENCY = 0

    ALERT = 1

    CRITICAL = 2

    ERROR = 3

    WARNING = 4

    NOTICE = 5

    INFORMATIONAL = 6

    DEBUG = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LogMessageSeverityEnum']


class LogSeverityEnum(Enum):
    """
    LogSeverityEnum

    Log severity

    .. data:: EMERGENCY = 0

    	System is unusable                (severity=0)

    .. data:: ALERT = 1

    	Immediate action needed           (severity=1)

    .. data:: CRITICAL = 2

    	Critical conditions               (severity=2)

    .. data:: ERROR = 3

    	Error conditions                  (severity=3)

    .. data:: WARNING = 4

    	Warning conditions                (severity=4)

    .. data:: NOTICE = 5

    	Normal but significant conditions (severity=5)

    .. data:: INFORMATIONAL = 6

    	Informational messages            (severity=6)

    .. data:: DEBUG = 7

    	Debugging messages                (severity=7)

    """

    EMERGENCY = 0

    ALERT = 1

    CRITICAL = 2

    ERROR = 3

    WARNING = 4

    NOTICE = 5

    INFORMATIONAL = 6

    DEBUG = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LogSeverityEnum']


class LoggingDscpEnum(Enum):
    """
    LoggingDscpEnum

    Logging dscp

    .. data:: DSCP = 1

    	Logging TOS type DSCP

    """

    DSCP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingDscpEnum']


class LoggingDscpValueEnum(Enum):
    """
    LoggingDscpValueEnum

    Logging dscp value

    .. data:: DEFAULT = 0

    	Applicable to DSCP: bits 000000

    .. data:: AF11 = 10

    	Applicable to DSCP: bits 001010

    .. data:: AF12 = 12

    	Applicable to DSCP: bits 001100

    .. data:: AF13 = 14

    	Applicable to DSCP: bits 001110

    .. data:: AF21 = 18

    	Applicable to DSCP: bits 010010

    .. data:: AF22 = 20

    	Applicable to DSCP: bits 010100

    .. data:: AF23 = 22

    	Applicable to DSCP: bits 010110

    .. data:: AF31 = 26

    	Applicable to DSCP: bits 011010

    .. data:: AF32 = 28

    	Applicable to DSCP: bits 011100

    .. data:: AF33 = 30

    	Applicable to DSCP: bits 011110

    .. data:: AF41 = 34

    	Applicable to DSCP: bits 100010

    .. data:: AF42 = 36

    	Applicable to DSCP: bits 100100

    .. data:: AF43 = 38

    	Applicable to DSCP: bits 100110

    .. data:: EF = 46

    	Applicable to DSCP: bits 101110

    .. data:: CS1 = 8

    	Applicable to DSCP: bits 001000

    .. data:: CS2 = 16

    	Applicable to DSCP: bits 010000

    .. data:: CS3 = 24

    	Applicable to DSCP: bits 011000

    .. data:: CS4 = 32

    	Applicable to DSCP: bits 100000

    .. data:: CS5 = 40

    	Applicable to DSCP: bits 101000

    .. data:: CS6 = 48

    	Applicable to DSCP: bits 110000

    .. data:: CS7 = 56

    	Applicable to DSCP: bits 111000

    """

    DEFAULT = 0

    AF11 = 10

    AF12 = 12

    AF13 = 14

    AF21 = 18

    AF22 = 20

    AF23 = 22

    AF31 = 26

    AF32 = 28

    AF33 = 30

    AF41 = 34

    AF42 = 36

    AF43 = 38

    EF = 46

    CS1 = 8

    CS2 = 16

    CS3 = 24

    CS4 = 32

    CS5 = 40

    CS6 = 48

    CS7 = 56


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingDscpValueEnum']


class LoggingLevelsEnum(Enum):
    """
    LoggingLevelsEnum

    Logging levels

    .. data:: EMERGENCY = 0

    	Emergency Level Msg

    .. data:: ALERT = 1

    	Alert Level Msg

    .. data:: CRITICAL = 2

    	Critical Level Msg

    .. data:: ERROR = 3

    	Error Level Msg

    .. data:: WARNING = 4

    	Warning Level Msg

    .. data:: NOTICE = 5

    	Notification Level Msg

    .. data:: INFO = 6

    	Informational Level Msg

    .. data:: DEBUG = 7

    	Debugging Level Msg

    .. data:: DISABLE = 15

    	Disable logging

    """

    EMERGENCY = 0

    ALERT = 1

    CRITICAL = 2

    ERROR = 3

    WARNING = 4

    NOTICE = 5

    INFO = 6

    DEBUG = 7

    DISABLE = 15


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingLevelsEnum']


class LoggingPrecedenceEnum(Enum):
    """
    LoggingPrecedenceEnum

    Logging precedence

    .. data:: PRECEDENCE = 0

    	Logging TOS type precedence

    """

    PRECEDENCE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingPrecedenceEnum']


class LoggingPrecedenceValueEnum(Enum):
    """
    LoggingPrecedenceValueEnum

    Logging precedence value

    .. data:: ROUTINE = 0

    	Applicable to precedence: value 0

    .. data:: PRIORITY = 1

    	Applicable to precedence: value 1

    .. data:: IMMEDIATE = 2

    	Applicable to precedence: value 2

    .. data:: FLASH = 3

    	Applicable to precedence: value 3

    .. data:: FLASH_OVERRIDE = 4

    	Applicable to precedence: value 4

    .. data:: CRITICAL = 5

    	Applicable to precedence: value 5

    .. data:: INTERNET = 6

    	Applicable to precedence: value 6

    .. data:: NETWORK = 7

    	Applicable to precedence: value 7

    """

    ROUTINE = 0

    PRIORITY = 1

    IMMEDIATE = 2

    FLASH = 3

    FLASH_OVERRIDE = 4

    CRITICAL = 5

    INTERNET = 6

    NETWORK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingPrecedenceValueEnum']


class LoggingTosEnum(Enum):
    """
    LoggingTosEnum

    Logging tos

    .. data:: PRECEDENCE = 0

    	Logging TOS type precedence

    .. data:: DSCP = 1

    	Logging TOS type DSCP

    """

    PRECEDENCE = 0

    DSCP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingTosEnum']


class TimeInfoEnum(Enum):
    """
    TimeInfoEnum

    Time info

    .. data:: DISABLE = 0

    	Exclude

    .. data:: ENABLE = 1

    	Include

    """

    DISABLE = 0

    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['TimeInfoEnum']



class SyslogService(object):
    """
    Syslog Timestamp Services
    
    .. attribute:: timestamps
    
    	Timestamp debug/log messages configuration
    	**type**\: :py:class:`Timestamps <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2015-10-08'

    def __init__(self):
        self.timestamps = SyslogService.Timestamps()
        self.timestamps.parent = self


    class Timestamps(object):
        """
        Timestamp debug/log messages configuration
        
        .. attribute:: debug
        
        	Timestamp debug messages
        	**type**\: :py:class:`Debug <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug>`
        
        .. attribute:: enable
        
        	Enable timestamp debug/log messages
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: log
        
        	Timestamp log messages
        	**type**\: :py:class:`Log <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.debug = SyslogService.Timestamps.Debug()
            self.debug.parent = self
            self.enable = None
            self.log = SyslogService.Timestamps.Log()
            self.log.parent = self


        class Log(object):
            """
            Timestamp log messages
            
            .. attribute:: log_datetime
            
            	Timestamp with date and time
            	**type**\: :py:class:`LogDatetime <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime>`
            
            .. attribute:: log_timestamp_disable
            
            	Disable timestamp log messages
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: log_uptime
            
            	Timestamp with systime uptime
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.log_datetime = SyslogService.Timestamps.Log.LogDatetime()
                self.log_datetime.parent = self
                self.log_timestamp_disable = None
                self.log_uptime = None


            class LogDatetime(object):
                """
                Timestamp with date and time
                
                .. attribute:: log_datetime_value
                
                	Set timestamp for log message
                	**type**\: :py:class:`LogDatetimeValue <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2015-10-08'

                def __init__(self):
                    self.parent = None
                    self.log_datetime_value = SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue()
                    self.log_datetime_value.parent = self


                class LogDatetimeValue(object):
                    """
                    Set timestamp for log message
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2015-10-08'

                    def __init__(self):
                        self.parent = None
                        self.msec = None
                        self.time_stamp_value = None
                        self.time_zone = None
                        self.year = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:log/Cisco-IOS-XR-infra-syslog-cfg:log-datetime/Cisco-IOS-XR-infra-syslog-cfg:log-datetime-value'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.msec is not None:
                            return True

                        if self.time_stamp_value is not None:
                            return True

                        if self.time_zone is not None:
                            return True

                        if self.year is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:log/Cisco-IOS-XR-infra-syslog-cfg:log-datetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.log_datetime_value is not None and self.log_datetime_value._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['SyslogService.Timestamps.Log.LogDatetime']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:log'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.log_datetime is not None and self.log_datetime._has_data():
                    return True

                if self.log_timestamp_disable is not None:
                    return True

                if self.log_uptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['SyslogService.Timestamps.Log']['meta_info']


        class Debug(object):
            """
            Timestamp debug messages
            
            .. attribute:: debug_datetime
            
            	Timestamp with date and time
            	**type**\: :py:class:`DebugDatetime <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime>`
            
            .. attribute:: debug_timestamp_disable
            
            	Disable timestamp debug messages
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: debug_uptime
            
            	Timestamp with systime uptime
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.debug_datetime = SyslogService.Timestamps.Debug.DebugDatetime()
                self.debug_datetime.parent = self
                self.debug_timestamp_disable = None
                self.debug_uptime = None


            class DebugDatetime(object):
                """
                Timestamp with date and time
                
                .. attribute:: datetime_value
                
                	Set time format for debug msg
                	**type**\: :py:class:`DatetimeValue <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2015-10-08'

                def __init__(self):
                    self.parent = None
                    self.datetime_value = SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue()
                    self.datetime_value.parent = self


                class DatetimeValue(object):
                    """
                    Set time format for debug msg
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\: :py:class:`TimeInfoEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2015-10-08'

                    def __init__(self):
                        self.parent = None
                        self.msec = None
                        self.time_stamp_value = None
                        self.time_zone = None
                        self.year = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:debug/Cisco-IOS-XR-infra-syslog-cfg:debug-datetime/Cisco-IOS-XR-infra-syslog-cfg:datetime-value'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.msec is not None:
                            return True

                        if self.time_stamp_value is not None:
                            return True

                        if self.time_zone is not None:
                            return True

                        if self.year is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:debug/Cisco-IOS-XR-infra-syslog-cfg:debug-datetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.datetime_value is not None and self.datetime_value._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['SyslogService.Timestamps.Debug.DebugDatetime']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:debug'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.debug_datetime is not None and self.debug_datetime._has_data():
                    return True

                if self.debug_timestamp_disable is not None:
                    return True

                if self.debug_uptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['SyslogService.Timestamps.Debug']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.debug is not None and self.debug._has_data():
                return True

            if self.enable is not None:
                return True

            if self.log is not None and self.log._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['SyslogService.Timestamps']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.timestamps is not None and self.timestamps._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['SyslogService']['meta_info']


class Syslog(object):
    """
    syslog
    
    .. attribute:: alarm_logger
    
    	Alarm Logger Properties
    	**type**\: :py:class:`AlarmLogger <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger>`
    
    .. attribute:: archive
    
    	Archive attributes configuration
    	**type**\: :py:class:`Archive <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Archive>`
    
    .. attribute:: buffered_logging
    
    	Set buffered logging parameters
    	**type**\: :py:class:`BufferedLogging <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.BufferedLogging>`
    
    .. attribute:: console_logging
    
    	Set console logging
    	**type**\: :py:class:`ConsoleLogging <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging>`
    
    .. attribute:: enable_console_logging
    
    	Enabled or disabled
    	**type**\: bool
    
    .. attribute:: files
    
    	Configure logging file destination
    	**type**\: :py:class:`Files <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files>`
    
    .. attribute:: history_logging
    
    	Set history logging
    	**type**\: :py:class:`HistoryLogging <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HistoryLogging>`
    
    .. attribute:: host_name_prefix
    
    	Hostname prefix to add on msgs to servers
    	**type**\: str
    
    .. attribute:: host_server
    
    	Configure logging host
    	**type**\: :py:class:`HostServer <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer>`
    
    .. attribute:: ipv4
    
    	Syslog TOS bit for outgoing messages
    	**type**\: :py:class:`Ipv4 <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4>`
    
    .. attribute:: ipv6
    
    	Syslog traffic class bit for outgoing messages
    	**type**\: :py:class:`Ipv6 <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6>`
    
    .. attribute:: local_log_file_size
    
    	Set size of the local log file
    	**type**\: int
    
    	**range:** 0..4294967295
    
    .. attribute:: logging_facilities
    
    	Modify message logging facilities
    	**type**\: :py:class:`LoggingFacilities <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.LoggingFacilities>`
    
    .. attribute:: monitor_logging
    
    	Set monitor logging
    	**type**\: :py:class:`MonitorLogging <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging>`
    
    .. attribute:: source_interface_table
    
    	Configure source interface
    	**type**\: :py:class:`SourceInterfaceTable <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable>`
    
    .. attribute:: suppress_duplicates
    
    	Suppress consecutive duplicate messages
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: trap_logging
    
    	Set trap logging
    	**type**\: :py:class:`TrapLogging <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.TrapLogging>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2015-10-08'

    def __init__(self):
        self.alarm_logger = Syslog.AlarmLogger()
        self.alarm_logger.parent = self
        self.archive = Syslog.Archive()
        self.archive.parent = self
        self.buffered_logging = Syslog.BufferedLogging()
        self.buffered_logging.parent = self
        self.console_logging = Syslog.ConsoleLogging()
        self.console_logging.parent = self
        self.enable_console_logging = None
        self.files = Syslog.Files()
        self.files.parent = self
        self.history_logging = Syslog.HistoryLogging()
        self.history_logging.parent = self
        self.host_name_prefix = None
        self.host_server = Syslog.HostServer()
        self.host_server.parent = self
        self.ipv4 = Syslog.Ipv4()
        self.ipv4.parent = self
        self.ipv6 = Syslog.Ipv6()
        self.ipv6.parent = self
        self.local_log_file_size = None
        self.logging_facilities = Syslog.LoggingFacilities()
        self.logging_facilities.parent = self
        self.monitor_logging = Syslog.MonitorLogging()
        self.monitor_logging.parent = self
        self.source_interface_table = Syslog.SourceInterfaceTable()
        self.source_interface_table.parent = self
        self.suppress_duplicates = None
        self.trap_logging = Syslog.TrapLogging()
        self.trap_logging.parent = self


    class MonitorLogging(object):
        """
        Set monitor logging
        
        .. attribute:: logging_level
        
        	Monitor Logging Level
        	**type**\: :py:class:`LoggingLevelsEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        .. attribute:: monitor_discriminator
        
        	Set monitor logging discriminators
        	**type**\: :py:class:`MonitorDiscriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging.MonitorDiscriminator>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.logging_level = None
            self.monitor_discriminator = Syslog.MonitorLogging.MonitorDiscriminator()
            self.monitor_discriminator.parent = self


        class MonitorDiscriminator(object):
            """
            Set monitor logging discriminators
            
            .. attribute:: match1
            
            	Set monitor logging match1 discriminator
            	**type**\: str
            
            .. attribute:: match2
            
            	Set monitor logging match2 discriminator
            	**type**\: str
            
            .. attribute:: match3
            
            	Set monitor logging match3 discriminator
            	**type**\: str
            
            .. attribute:: nomatch1
            
            	Set monitor logging no\-match1 discriminator
            	**type**\: str
            
            .. attribute:: nomatch2
            
            	Set monitor logging no\-match2 discriminator
            	**type**\: str
            
            .. attribute:: nomatch3
            
            	Set monitor logging no\-match3 discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.match1 = None
                self.match2 = None
                self.match3 = None
                self.nomatch1 = None
                self.nomatch2 = None
                self.nomatch3 = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:monitor-logging/Cisco-IOS-XR-infra-syslog-cfg:monitor-discriminator'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.match1 is not None:
                    return True

                if self.match2 is not None:
                    return True

                if self.match3 is not None:
                    return True

                if self.nomatch1 is not None:
                    return True

                if self.nomatch2 is not None:
                    return True

                if self.nomatch3 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.MonitorLogging.MonitorDiscriminator']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:monitor-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.logging_level is not None:
                return True

            if self.monitor_discriminator is not None and self.monitor_discriminator._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.MonitorLogging']['meta_info']


    class HistoryLogging(object):
        """
        Set history logging
        
        .. attribute:: history_size
        
        	Logging history size
        	**type**\: int
        
        	**range:** 1..500
        
        .. attribute:: logging_level
        
        	History logging level
        	**type**\: :py:class:`LoggingLevelsEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.history_size = None
            self.logging_level = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:history-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.history_size is not None:
                return True

            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.HistoryLogging']['meta_info']


    class LoggingFacilities(object):
        """
        Modify message logging facilities
        
        .. attribute:: facility_level
        
        	Facility from which logging is done
        	**type**\: :py:class:`FacilityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.FacilityEnum>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.facility_level = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:logging-facilities'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.facility_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.LoggingFacilities']['meta_info']


    class TrapLogging(object):
        """
        Set trap logging
        
        .. attribute:: logging_level
        
        	Trap logging level
        	**type**\: :py:class:`LoggingLevelsEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.logging_level = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:trap-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.TrapLogging']['meta_info']


    class BufferedLogging(object):
        """
        Set buffered logging parameters
        
        .. attribute:: buffer_size
        
        	Logging buffered size
        	**type**\: int
        
        	**range:** 4096..4294967295
        
        .. attribute:: buffered_discriminator
        
        	Set buffered logging discriminators
        	**type**\: :py:class:`BufferedDiscriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.BufferedLogging.BufferedDiscriminator>`
        
        .. attribute:: logging_level
        
        	Logging level for Buffered logging
        	**type**\: :py:class:`LoggingLevelsEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.buffer_size = None
            self.buffered_discriminator = Syslog.BufferedLogging.BufferedDiscriminator()
            self.buffered_discriminator.parent = self
            self.logging_level = None


        class BufferedDiscriminator(object):
            """
            Set buffered logging discriminators
            
            .. attribute:: match1
            
            	Set buffered logging match1 discriminator
            	**type**\: str
            
            .. attribute:: match2
            
            	Set buffered logging match2 discriminator
            	**type**\: str
            
            .. attribute:: match3
            
            	Set buffered logging match3 discriminator
            	**type**\: str
            
            .. attribute:: nomatch1
            
            	Set buffered logging no\-match1 discriminator
            	**type**\: str
            
            .. attribute:: nomatch2
            
            	Set buffered logging no\-match2 discriminator
            	**type**\: str
            
            .. attribute:: nomatch3
            
            	Set buffered logging no\-match3 discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.match1 = None
                self.match2 = None
                self.match3 = None
                self.nomatch1 = None
                self.nomatch2 = None
                self.nomatch3 = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:buffered-logging/Cisco-IOS-XR-infra-syslog-cfg:buffered-discriminator'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.match1 is not None:
                    return True

                if self.match2 is not None:
                    return True

                if self.match3 is not None:
                    return True

                if self.nomatch1 is not None:
                    return True

                if self.nomatch2 is not None:
                    return True

                if self.nomatch3 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.BufferedLogging.BufferedDiscriminator']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:buffered-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.buffer_size is not None:
                return True

            if self.buffered_discriminator is not None and self.buffered_discriminator._has_data():
                return True

            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.BufferedLogging']['meta_info']


    class HostServer(object):
        """
        Configure logging host
        
        .. attribute:: vrfs
        
        	VRF table
        	**type**\: :py:class:`Vrfs <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.vrfs = Syslog.HostServer.Vrfs()
            self.vrfs.parent = self


        class Vrfs(object):
            """
            VRF table
            
            .. attribute:: vrf
            
            	VRF specific data
            	**type**\: list of :py:class:`Vrf <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.vrf = YList()
                self.vrf.parent = self
                self.vrf.name = 'vrf'


            class Vrf(object):
                """
                VRF specific data
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF instance
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: hosts
                
                	List of the logging host
                	**type**\: :py:class:`Hosts <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts>`
                
                .. attribute:: ipv4s
                
                	List of the IPv4 logging host
                	**type**\: :py:class:`Ipv4S <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S>`
                
                .. attribute:: ipv6s
                
                	List of the IPv6 logging host
                	**type**\: :py:class:`Ipv6S <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2015-10-08'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.hosts = Syslog.HostServer.Vrfs.Vrf.Hosts()
                    self.hosts.parent = self
                    self.ipv4s = Syslog.HostServer.Vrfs.Vrf.Ipv4S()
                    self.ipv4s.parent = self
                    self.ipv6s = Syslog.HostServer.Vrfs.Vrf.Ipv6S()
                    self.ipv6s.parent = self


                class Ipv6S(object):
                    """
                    List of the IPv6 logging host
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address of the logging host
                    	**type**\: list of :py:class:`Ipv6 <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2015-10-08'

                    def __init__(self):
                        self.parent = None
                        self.ipv6 = YList()
                        self.ipv6.parent = self
                        self.ipv6.name = 'ipv6'


                    class Ipv6(object):
                        """
                        IPv6 address of the logging host
                        
                        .. attribute:: address  <key>
                        
                        	IPv6 address of the logging host
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_discriminator
                        
                        	Set IPv6 logging discriminators
                        	**type**\: :py:class:`Ipv6Discriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator>`
                        
                        .. attribute:: ipv6_severity_levels
                        
                        	Severity container of the logging host
                        	**type**\: :py:class:`Ipv6SeverityLevels <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels>`
                        
                        .. attribute:: ipv6_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\: :py:class:`Ipv6SeverityPort <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort>`
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2015-10-08'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.ipv6_discriminator = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator()
                            self.ipv6_discriminator.parent = self
                            self.ipv6_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels()
                            self.ipv6_severity_levels.parent = self
                            self.ipv6_severity_port = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort()
                            self.ipv6_severity_port.parent = self


                        class Ipv6SeverityPort(object):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.port = None
                                self.severity = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv6-severity-port'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.port is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort']['meta_info']


                        class Ipv6Discriminator(object):
                            """
                            Set IPv6 logging discriminators
                            
                            .. attribute:: match1
                            
                            	Set IPv6 logging match1 discriminator
                            	**type**\: str
                            
                            .. attribute:: match2
                            
                            	Set IPv6 logging match2 discriminator
                            	**type**\: str
                            
                            .. attribute:: match3
                            
                            	Set IPv6 logging match3 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch1
                            
                            	Set IPv6 logging no\-match1 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch2
                            
                            	Set IPv6 logging no\-match2 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch3
                            
                            	Set IPv6 logging no\-match3 discriminator
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.match1 = None
                                self.match2 = None
                                self.match3 = None
                                self.nomatch1 = None
                                self.nomatch2 = None
                                self.nomatch3 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv6-discriminator'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.match1 is not None:
                                    return True

                                if self.match2 is not None:
                                    return True

                                if self.match3 is not None:
                                    return True

                                if self.nomatch1 is not None:
                                    return True

                                if self.nomatch2 is not None:
                                    return True

                                if self.nomatch3 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator']['meta_info']


                        class Ipv6SeverityLevels(object):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: ipv6_severity_level
                            
                            	Severity for the logging host
                            	**type**\: list of :py:class:`Ipv6SeverityLevel <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel>`
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.ipv6_severity_level = YList()
                                self.ipv6_severity_level.parent = self
                                self.ipv6_severity_level.name = 'ipv6_severity_level'


                            class Ipv6SeverityLevel(object):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  <key>
                                
                                	Severity for the logging host
                                	**type**\: :py:class:`LogSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LogSeverityEnum>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2015-10-08'

                                def __init__(self):
                                    self.parent = None
                                    self.severity = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.severity is None:
                                        raise YPYModelError('Key property severity is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv6-severity-level[Cisco-IOS-XR-infra-syslog-cfg:severity = ' + str(self.severity) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                    return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv6-severity-levels'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ipv6_severity_level is not None:
                                    for child_ref in self.ipv6_severity_level:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.address is None:
                                raise YPYModelError('Key property address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv6[Cisco-IOS-XR-infra-syslog-cfg:address = ' + str(self.address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.ipv6_discriminator is not None and self.ipv6_discriminator._has_data():
                                return True

                            if self.ipv6_severity_levels is not None and self.ipv6_severity_levels._has_data():
                                return True

                            if self.ipv6_severity_port is not None and self.ipv6_severity_port._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv6s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv6 is not None:
                            for child_ref in self.ipv6:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S']['meta_info']


                class Hosts(object):
                    """
                    List of the logging host
                    
                    .. attribute:: host
                    
                    	Name of the logging host
                    	**type**\: list of :py:class:`Host <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2015-10-08'

                    def __init__(self):
                        self.parent = None
                        self.host = YList()
                        self.host.parent = self
                        self.host.name = 'host'


                    class Host(object):
                        """
                        Name of the logging host
                        
                        .. attribute:: host_name  <key>
                        
                        	Name of the logging host
                        	**type**\: str
                        
                        .. attribute:: host_name_discriminator
                        
                        	Set Hostname logging discriminators
                        	**type**\: :py:class:`HostNameDiscriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator>`
                        
                        .. attribute:: host_name_severities
                        
                        	Severity container of the logging host
                        	**type**\: :py:class:`HostNameSeverities <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities>`
                        
                        .. attribute:: host_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\: :py:class:`HostSeverityPort <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort>`
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2015-10-08'

                        def __init__(self):
                            self.parent = None
                            self.host_name = None
                            self.host_name_discriminator = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator()
                            self.host_name_discriminator.parent = self
                            self.host_name_severities = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities()
                            self.host_name_severities.parent = self
                            self.host_severity_port = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort()
                            self.host_severity_port.parent = self


                        class HostNameSeverities(object):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: host_name_severity
                            
                            	Severity for the logging host
                            	**type**\: list of :py:class:`HostNameSeverity <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity>`
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.host_name_severity = YList()
                                self.host_name_severity.parent = self
                                self.host_name_severity.name = 'host_name_severity'


                            class HostNameSeverity(object):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  <key>
                                
                                	Severity for the logging host
                                	**type**\: :py:class:`LogSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LogSeverityEnum>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2015-10-08'

                                def __init__(self):
                                    self.parent = None
                                    self.severity = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.severity is None:
                                        raise YPYModelError('Key property severity is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:host-name-severity[Cisco-IOS-XR-infra-syslog-cfg:severity = ' + str(self.severity) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                    return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:host-name-severities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.host_name_severity is not None:
                                    for child_ref in self.host_name_severity:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities']['meta_info']


                        class HostNameDiscriminator(object):
                            """
                            Set Hostname logging discriminators
                            
                            .. attribute:: match1
                            
                            	Set hostname logging match1 discriminator
                            	**type**\: str
                            
                            .. attribute:: match2
                            
                            	Set hostname logging match2 discriminator
                            	**type**\: str
                            
                            .. attribute:: match3
                            
                            	Set hostname logging match3 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch1
                            
                            	Set hostname logging no\-match1 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch2
                            
                            	Set hostname logging no\-match2 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch3
                            
                            	Set hostname logging no\-match3 discriminator
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.match1 = None
                                self.match2 = None
                                self.match3 = None
                                self.nomatch1 = None
                                self.nomatch2 = None
                                self.nomatch3 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:host-name-discriminator'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.match1 is not None:
                                    return True

                                if self.match2 is not None:
                                    return True

                                if self.match3 is not None:
                                    return True

                                if self.nomatch1 is not None:
                                    return True

                                if self.nomatch2 is not None:
                                    return True

                                if self.nomatch3 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator']['meta_info']


                        class HostSeverityPort(object):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.port = None
                                self.severity = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:host-severity-port'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.port is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.host_name is None:
                                raise YPYModelError('Key property host_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:host[Cisco-IOS-XR-infra-syslog-cfg:host-name = ' + str(self.host_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.host_name is not None:
                                return True

                            if self.host_name_discriminator is not None and self.host_name_discriminator._has_data():
                                return True

                            if self.host_name_severities is not None and self.host_name_severities._has_data():
                                return True

                            if self.host_severity_port is not None and self.host_severity_port._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:hosts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.host is not None:
                            for child_ref in self.host:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts']['meta_info']


                class Ipv4S(object):
                    """
                    List of the IPv4 logging host
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address of the logging host
                    	**type**\: list of :py:class:`Ipv4 <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2015-10-08'

                    def __init__(self):
                        self.parent = None
                        self.ipv4 = YList()
                        self.ipv4.parent = self
                        self.ipv4.name = 'ipv4'


                    class Ipv4(object):
                        """
                        IPv4 address of the logging host
                        
                        .. attribute:: address  <key>
                        
                        	IPv4 address of the logging host
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv4_discriminator
                        
                        	Set IPv4 logging discriminators
                        	**type**\: :py:class:`Ipv4Discriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator>`
                        
                        .. attribute:: ipv4_severity_levels
                        
                        	Severity container of the logging host
                        	**type**\: :py:class:`Ipv4SeverityLevels <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels>`
                        
                        .. attribute:: ipv4_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\: :py:class:`Ipv4SeverityPort <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort>`
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2015-10-08'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.ipv4_discriminator = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator()
                            self.ipv4_discriminator.parent = self
                            self.ipv4_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels()
                            self.ipv4_severity_levels.parent = self
                            self.ipv4_severity_port = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort()
                            self.ipv4_severity_port.parent = self


                        class Ipv4SeverityLevels(object):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: ipv4_severity_level
                            
                            	Severity for the logging host
                            	**type**\: list of :py:class:`Ipv4SeverityLevel <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel>`
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_severity_level = YList()
                                self.ipv4_severity_level.parent = self
                                self.ipv4_severity_level.name = 'ipv4_severity_level'


                            class Ipv4SeverityLevel(object):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  <key>
                                
                                	Severity for the logging host
                                	**type**\: :py:class:`LogSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LogSeverityEnum>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2015-10-08'

                                def __init__(self):
                                    self.parent = None
                                    self.severity = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.severity is None:
                                        raise YPYModelError('Key property severity is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv4-severity-level[Cisco-IOS-XR-infra-syslog-cfg:severity = ' + str(self.severity) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                    return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv4-severity-levels'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ipv4_severity_level is not None:
                                    for child_ref in self.ipv4_severity_level:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels']['meta_info']


                        class Ipv4SeverityPort(object):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.port = None
                                self.severity = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv4-severity-port'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.port is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort']['meta_info']


                        class Ipv4Discriminator(object):
                            """
                            Set IPv4 logging discriminators
                            
                            .. attribute:: match1
                            
                            	Set IPv4 logging match1 discriminator
                            	**type**\: str
                            
                            .. attribute:: match2
                            
                            	Set IPv4 logging match2 discriminator
                            	**type**\: str
                            
                            .. attribute:: match3
                            
                            	Set IPv4 logging match3 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch1
                            
                            	Set IPv4 logging no\-match1 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch2
                            
                            	Set IPv4 logging no\-match2 discriminator
                            	**type**\: str
                            
                            .. attribute:: nomatch3
                            
                            	Set IPv4 logging no\-match3 discriminator
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2015-10-08'

                            def __init__(self):
                                self.parent = None
                                self.match1 = None
                                self.match2 = None
                                self.match3 = None
                                self.nomatch1 = None
                                self.nomatch2 = None
                                self.nomatch3 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv4-discriminator'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.match1 is not None:
                                    return True

                                if self.match2 is not None:
                                    return True

                                if self.match3 is not None:
                                    return True

                                if self.nomatch1 is not None:
                                    return True

                                if self.nomatch2 is not None:
                                    return True

                                if self.nomatch3 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.address is None:
                                raise YPYModelError('Key property address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv4[Cisco-IOS-XR-infra-syslog-cfg:address = ' + str(self.address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.ipv4_discriminator is not None and self.ipv4_discriminator._has_data():
                                return True

                            if self.ipv4_severity_levels is not None and self.ipv4_severity_levels._has_data():
                                return True

                            if self.ipv4_severity_port is not None and self.ipv4_severity_port._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:ipv4s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv4 is not None:
                            for child_ref in self.ipv4:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:host-server/Cisco-IOS-XR-infra-syslog-cfg:vrfs/Cisco-IOS-XR-infra-syslog-cfg:vrf[Cisco-IOS-XR-infra-syslog-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.vrf_name is not None:
                        return True

                    if self.hosts is not None and self.hosts._has_data():
                        return True

                    if self.ipv4s is not None and self.ipv4s._has_data():
                        return True

                    if self.ipv6s is not None and self.ipv6s._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:host-server/Cisco-IOS-XR-infra-syslog-cfg:vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vrf is not None:
                    for child_ref in self.vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.HostServer.Vrfs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:host-server'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vrfs is not None and self.vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.HostServer']['meta_info']


    class ConsoleLogging(object):
        """
        Set console logging
        
        .. attribute:: console_discriminator
        
        	Set console logging discriminators
        	**type**\: :py:class:`ConsoleDiscriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging.ConsoleDiscriminator>`
        
        .. attribute:: logging_level
        
        	Console logging level
        	**type**\: :py:class:`LoggingLevelsEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.console_discriminator = Syslog.ConsoleLogging.ConsoleDiscriminator()
            self.console_discriminator.parent = self
            self.logging_level = None


        class ConsoleDiscriminator(object):
            """
            Set console logging discriminators
            
            .. attribute:: match1
            
            	Set console logging match1 discriminator
            	**type**\: str
            
            .. attribute:: match2
            
            	Set console logging match2 discriminator
            	**type**\: str
            
            .. attribute:: match3
            
            	Set console logging match3 discriminator
            	**type**\: str
            
            .. attribute:: nomatch1
            
            	Set console logging no\-match1 discriminator
            	**type**\: str
            
            .. attribute:: nomatch2
            
            	Set console logging no\-match2 discriminator
            	**type**\: str
            
            .. attribute:: nomatch3
            
            	Set console logging no\-match3 discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.match1 = None
                self.match2 = None
                self.match3 = None
                self.nomatch1 = None
                self.nomatch2 = None
                self.nomatch3 = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:console-logging/Cisco-IOS-XR-infra-syslog-cfg:console-discriminator'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.match1 is not None:
                    return True

                if self.match2 is not None:
                    return True

                if self.match3 is not None:
                    return True

                if self.nomatch1 is not None:
                    return True

                if self.nomatch2 is not None:
                    return True

                if self.nomatch3 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.ConsoleLogging.ConsoleDiscriminator']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:console-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.console_discriminator is not None and self.console_discriminator._has_data():
                return True

            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.ConsoleLogging']['meta_info']


    class Files(object):
        """
        Configure logging file destination
        
        .. attribute:: file
        
        	Specify File Name
        	**type**\: list of :py:class:`File <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.file = YList()
            self.file.parent = self
            self.file.name = 'file'


        class File(object):
            """
            Specify File Name
            
            .. attribute:: file_name  <key>
            
            	Name of the file
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: file_log_discriminator
            
            	Set File logging discriminators
            	**type**\: :py:class:`FileLogDiscriminator <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileLogDiscriminator>`
            
            .. attribute:: file_specification
            
            	Specifications of the logging file destination
            	**type**\: :py:class:`FileSpecification <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileSpecification>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.file_name = None
                self.file_log_discriminator = Syslog.Files.File.FileLogDiscriminator()
                self.file_log_discriminator.parent = self
                self.file_specification = Syslog.Files.File.FileSpecification()
                self.file_specification.parent = self


            class FileSpecification(object):
                """
                Specifications of the logging file destination
                
                .. attribute:: max_file_size
                
                	Maximum file size (in KB)
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: path
                
                	File path
                	**type**\: str
                
                .. attribute:: severity
                
                	Severity of messages
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2015-10-08'

                def __init__(self):
                    self.parent = None
                    self.max_file_size = None
                    self.path = None
                    self.severity = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:file-specification'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.max_file_size is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.severity is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Files.File.FileSpecification']['meta_info']


            class FileLogDiscriminator(object):
                """
                Set File logging discriminators
                
                .. attribute:: match1
                
                	Set file logging match discriminator 1
                	**type**\: str
                
                .. attribute:: match2
                
                	Set file logging match discriminator 2
                	**type**\: str
                
                .. attribute:: match3
                
                	Set file logging match discriminator 3
                	**type**\: str
                
                .. attribute:: nomatch1
                
                	Set file logging no match discriminator 1
                	**type**\: str
                
                .. attribute:: nomatch2
                
                	Set file logging no match discriminator 2
                	**type**\: str
                
                .. attribute:: nomatch3
                
                	Set file logging no match discriminator 3
                	**type**\: str
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2015-10-08'

                def __init__(self):
                    self.parent = None
                    self.match1 = None
                    self.match2 = None
                    self.match3 = None
                    self.nomatch1 = None
                    self.nomatch2 = None
                    self.nomatch3 = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:file-log-discriminator'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.match1 is not None:
                        return True

                    if self.match2 is not None:
                        return True

                    if self.match3 is not None:
                        return True

                    if self.nomatch1 is not None:
                        return True

                    if self.nomatch2 is not None:
                        return True

                    if self.nomatch3 is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Files.File.FileLogDiscriminator']['meta_info']

            @property
            def _common_path(self):
                if self.file_name is None:
                    raise YPYModelError('Key property file_name is None')

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:files/Cisco-IOS-XR-infra-syslog-cfg:file[Cisco-IOS-XR-infra-syslog-cfg:file-name = ' + str(self.file_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.file_name is not None:
                    return True

                if self.file_log_discriminator is not None and self.file_log_discriminator._has_data():
                    return True

                if self.file_specification is not None and self.file_specification._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Files.File']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:files'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.file is not None:
                for child_ref in self.file:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Files']['meta_info']


    class Ipv4(object):
        """
        Syslog TOS bit for outgoing messages
        
        .. attribute:: dscp
        
        	DSCP value
        	**type**\: :py:class:`Dscp <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Dscp>`
        
        .. attribute:: precedence
        
        	Precedence value
        	**type**\: :py:class:`Precedence <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Precedence>`
        
        .. attribute:: tos
        
        	Type of service
        	**type**\: :py:class:`Tos <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Tos>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.dscp = None
            self.precedence = None
            self.tos = Syslog.Ipv4.Tos()
            self.tos.parent = self


        class Dscp(object):
            """
            DSCP value
            
            .. attribute:: type
            
            	Logging TOS type DSCP
            	**type**\: :py:class:`LoggingDscpEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpEnum>`
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingPrecedenceValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingDscpValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.type = None
                self.unused = None
                self.value = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv4/Cisco-IOS-XR-infra-syslog-cfg:dscp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv4.Dscp']['meta_info']


        class Tos(object):
            """
            Type of service
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingDscpValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingPrecedenceValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\: :py:class:`LoggingTosEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingTosEnum>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.dscp = None
                self.precedence = None
                self.type = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv4/Cisco-IOS-XR-infra-syslog-cfg:tos'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.dscp is not None:
                    return True

                if self.precedence is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv4.Tos']['meta_info']


        class Precedence(object):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\: :py:class:`LoggingPrecedenceEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceEnum>`
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingDscpValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingPrecedenceValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.type = None
                self.unused = None
                self.value = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv4/Cisco-IOS-XR-infra-syslog-cfg:precedence'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv4.Precedence']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv4'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.dscp is not None and self.dscp._has_data():
                return True

            if self.precedence is not None and self.precedence._has_data():
                return True

            if self.tos is not None and self.tos._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Ipv4']['meta_info']


    class Archive(object):
        """
        Archive attributes configuration
        
        .. attribute:: device
        
        	'/disk0\:' or '/disk1\:' or '/harddisk\:'
        	**type**\: str
        
        .. attribute:: file_size
        
        	The maximum file size for a single log file
        	**type**\: int
        
        	**range:** 1..2047
        
        .. attribute:: frequency
        
        	The collection interval for logs
        	**type**\: :py:class:`LogCollectFrequencyEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LogCollectFrequencyEnum>`
        
        .. attribute:: length
        
        	The maximum number of weeks of log to maintain
        	**type**\: int
        
        	**range:** 1..256
        
        .. attribute:: severity
        
        	The minimum severity of log messages to archive
        	**type**\: :py:class:`LogMessageSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LogMessageSeverityEnum>`
        
        .. attribute:: size
        
        	The total size of the archive
        	**type**\: int
        
        	**range:** 1..2047
        
        .. attribute:: threshold
        
        	The size threshold at which a syslog is generated
        	**type**\: int
        
        	**range:** 1..99
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.device = None
            self.file_size = None
            self.frequency = None
            self.length = None
            self.severity = None
            self.size = None
            self.threshold = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:archive'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.device is not None:
                return True

            if self.file_size is not None:
                return True

            if self.frequency is not None:
                return True

            if self.length is not None:
                return True

            if self.severity is not None:
                return True

            if self.size is not None:
                return True

            if self.threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Archive']['meta_info']


    class Ipv6(object):
        """
        Syslog traffic class bit for outgoing messages
        
        .. attribute:: dscp
        
        	DSCP value
        	**type**\: :py:class:`Dscp <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.Dscp>`
        
        .. attribute:: precedence
        
        	Precedence value
        	**type**\: :py:class:`Precedence <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.Precedence>`
        
        .. attribute:: traffic_class
        
        	Type of traffic class
        	**type**\: :py:class:`TrafficClass <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.TrafficClass>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.dscp = None
            self.precedence = None
            self.traffic_class = Syslog.Ipv6.TrafficClass()
            self.traffic_class.parent = self


        class Dscp(object):
            """
            DSCP value
            
            .. attribute:: type
            
            	Logging TOS type DSCP
            	**type**\: :py:class:`LoggingDscpEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpEnum>`
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingPrecedenceValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingDscpValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.type = None
                self.unused = None
                self.value = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv6/Cisco-IOS-XR-infra-syslog-cfg:dscp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv6.Dscp']['meta_info']


        class TrafficClass(object):
            """
            Type of traffic class
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingDscpValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingPrecedenceValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\: :py:class:`LoggingTosEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingTosEnum>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.dscp = None
                self.precedence = None
                self.type = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv6/Cisco-IOS-XR-infra-syslog-cfg:traffic-class'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.dscp is not None:
                    return True

                if self.precedence is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv6.TrafficClass']['meta_info']


        class Precedence(object):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\: :py:class:`LoggingPrecedenceEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceEnum>`
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingDscpValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`LoggingPrecedenceValueEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\: int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.type = None
                self.unused = None
                self.value = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv6/Cisco-IOS-XR-infra-syslog-cfg:precedence'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv6.Precedence']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv6'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.dscp is not None and self.dscp._has_data():
                return True

            if self.precedence is not None and self.precedence._has_data():
                return True

            if self.traffic_class is not None and self.traffic_class._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Ipv6']['meta_info']


    class SourceInterfaceTable(object):
        """
        Configure source interface
        
        .. attribute:: source_interface_values
        
        	Specify interface for source address in logging transactions
        	**type**\: :py:class:`SourceInterfaceValues <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2015-10-08'

        def __init__(self):
            self.parent = None
            self.source_interface_values = Syslog.SourceInterfaceTable.SourceInterfaceValues()
            self.source_interface_values.parent = self


        class SourceInterfaceValues(object):
            """
            Specify interface for source address in logging
            transactions
            
            .. attribute:: source_interface_value
            
            	Source interface
            	**type**\: list of :py:class:`SourceInterfaceValue <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2015-10-08'

            def __init__(self):
                self.parent = None
                self.source_interface_value = YList()
                self.source_interface_value.parent = self
                self.source_interface_value.name = 'source_interface_value'


            class SourceInterfaceValue(object):
                """
                Source interface
                
                .. attribute:: src_interface_name_value  <key>
                
                	Which Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: source_interface_vrfs
                
                	Configure source interface VRF
                	**type**\: :py:class:`SourceInterfaceVrfs <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2015-10-08'

                def __init__(self):
                    self.parent = None
                    self.src_interface_name_value = None
                    self.source_interface_vrfs = Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs()
                    self.source_interface_vrfs.parent = self


                class SourceInterfaceVrfs(object):
                    """
                    Configure source interface VRF
                    
                    .. attribute:: source_interface_vrf
                    
                    	Specify VRF for source interface
                    	**type**\: list of :py:class:`SourceInterfaceVrf <ydk.models.infra.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2015-10-08'

                    def __init__(self):
                        self.parent = None
                        self.source_interface_vrf = YList()
                        self.source_interface_vrf.parent = self
                        self.source_interface_vrf.name = 'source_interface_vrf'


                    class SourceInterfaceVrf(object):
                        """
                        Specify VRF for source interface
                        
                        .. attribute:: vrf_name  <key>
                        
                        	Name of the VRF instance
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2015-10-08'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:source-interface-vrf[Cisco-IOS-XR-infra-syslog-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:source-interface-vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.source_interface_vrf is not None:
                            for child_ref in self.source_interface_vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs']['meta_info']

                @property
                def _common_path(self):
                    if self.src_interface_name_value is None:
                        raise YPYModelError('Key property src_interface_name_value is None')

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:source-interface-table/Cisco-IOS-XR-infra-syslog-cfg:source-interface-values/Cisco-IOS-XR-infra-syslog-cfg:source-interface-value[Cisco-IOS-XR-infra-syslog-cfg:src-interface-name-value = ' + str(self.src_interface_name_value) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.src_interface_name_value is not None:
                        return True

                    if self.source_interface_vrfs is not None and self.source_interface_vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:source-interface-table/Cisco-IOS-XR-infra-syslog-cfg:source-interface-values'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.source_interface_value is not None:
                    for child_ref in self.source_interface_value:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:source-interface-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.source_interface_values is not None and self.source_interface_values._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.SourceInterfaceTable']['meta_info']


    class AlarmLogger(object):
        """
        Alarm Logger Properties
        
        .. attribute:: buffer_size
        
        	Set size of the local event buffer
        	**type**\: int
        
        	**range:** 1024..1024000
        
        .. attribute:: severity_level
        
        	Log all events with equal or higher (lower level) severity than this
        	**type**\: :py:class:`AlarmLoggerSeverityLevelEnum <ydk.models.infra.Cisco_IOS_XR_infra_alarm_logger_datatypes.AlarmLoggerSeverityLevelEnum>`
        
        .. attribute:: source_location
        
        	Enable alarm source location in message text
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: threshold
        
        	Configure threshold (%) for capacity alarm
        	**type**\: int
        
        	**range:** 10..100
        
        

        """

        _prefix = 'infra-alarm-logger-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.buffer_size = None
            self.severity_level = None
            self.source_location = None
            self.threshold = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.buffer_size is not None:
                return True

            if self.severity_level is not None:
                return True

            if self.source_location is not None:
                return True

            if self.threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.AlarmLogger']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-cfg:syslog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.alarm_logger is not None and self.alarm_logger._has_data():
            return True

        if self.archive is not None and self.archive._has_data():
            return True

        if self.buffered_logging is not None and self.buffered_logging._has_data():
            return True

        if self.console_logging is not None and self.console_logging._has_data():
            return True

        if self.enable_console_logging is not None:
            return True

        if self.files is not None and self.files._has_data():
            return True

        if self.history_logging is not None and self.history_logging._has_data():
            return True

        if self.host_name_prefix is not None:
            return True

        if self.host_server is not None and self.host_server._has_data():
            return True

        if self.ipv4 is not None and self.ipv4._has_data():
            return True

        if self.ipv6 is not None and self.ipv6._has_data():
            return True

        if self.local_log_file_size is not None:
            return True

        if self.logging_facilities is not None and self.logging_facilities._has_data():
            return True

        if self.monitor_logging is not None and self.monitor_logging._has_data():
            return True

        if self.source_interface_table is not None and self.source_interface_table._has_data():
            return True

        if self.suppress_duplicates is not None:
            return True

        if self.trap_logging is not None and self.trap_logging._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['Syslog']['meta_info']


