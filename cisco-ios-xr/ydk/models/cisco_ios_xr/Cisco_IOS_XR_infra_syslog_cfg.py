""" Cisco_IOS_XR_infra_syslog_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-syslog package configuration.

This module contains definitions
for the following management objects\:
  syslog\-service\: Syslog Timestamp Services
  syslog\: syslog

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class FacilityEnum(Enum):
    """
    FacilityEnum

    Facility

    .. data:: kern = 0

    	Kernel Facility

    .. data:: user = 8

    	User Facility

    .. data:: mail = 16

    	Mail Facility

    .. data:: daemon = 24

    	Daemon Facility

    .. data:: auth = 32

    	Auth Facility

    .. data:: syslog = 40

    	Syslog Facility

    .. data:: lpr = 48

    	Lpr Facility

    .. data:: news = 56

    	News Facility

    .. data:: uucp = 64

    	Uucp Facility

    .. data:: cron = 72

    	Cron Facility

    .. data:: authpriv = 80

    	Authpriv Facility

    .. data:: ftp = 88

    	Ftp Facility

    .. data:: local0 = 128

    	Local0 Facility

    .. data:: local1 = 136

    	Local1 Facility

    .. data:: local2 = 144

    	Local2 Facility

    .. data:: local3 = 152

    	Local3 Facility

    .. data:: local4 = 160

    	Local4 Facility

    .. data:: local5 = 168

    	Local5 Facility

    .. data:: local6 = 176

    	Local6 Facility

    .. data:: local7 = 184

    	Local7 Facility

    .. data:: sys9 = 192

    	System9 Facility

    .. data:: sys10 = 200

    	System10 Facility

    .. data:: sys11 = 208

    	System11 Facility

    .. data:: sys12 = 216

    	System12 Facility

    .. data:: sys13 = 224

    	System13 Facility

    .. data:: sys14 = 232

    	System14 Facility

    """

    kern = 0

    user = 8

    mail = 16

    daemon = 24

    auth = 32

    syslog = 40

    lpr = 48

    news = 56

    uucp = 64

    cron = 72

    authpriv = 80

    ftp = 88

    local0 = 128

    local1 = 136

    local2 = 144

    local3 = 152

    local4 = 160

    local5 = 168

    local6 = 176

    local7 = 184

    sys9 = 192

    sys10 = 200

    sys11 = 208

    sys12 = 216

    sys13 = 224

    sys14 = 232


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['FacilityEnum']


class LogCollectFrequencyEnum(Enum):
    """
    LogCollectFrequencyEnum

    Log collect frequency

    .. data:: weekly = 1

    	Collect log in files on a weekly basis

    .. data:: daily = 2

    	Collect log in files on a daily basis

    """

    weekly = 1

    daily = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LogCollectFrequencyEnum']


class LogMessageSeverityEnum(Enum):
    """
    LogMessageSeverityEnum

    Log message severity

    .. data:: emergency = 0

    	System is unusable                (severity=0)

    .. data:: alert = 1

    	Immediate action needed           (severity=1)

    .. data:: critical = 2

    	Critical conditions               (severity=2)

    .. data:: error = 3

    	Error conditions                  (severity=3)

    .. data:: warning = 4

    	Warning conditions                (severity=4)

    .. data:: notice = 5

    	Normal but significant conditions (severity=5)

    .. data:: informational = 6

    	Informational messages            (severity=6)

    .. data:: debug = 7

    	Debugging messages                (severity=7)

    """

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    informational = 6

    debug = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LogMessageSeverityEnum']


class LogSeverityEnum(Enum):
    """
    LogSeverityEnum

    Log severity

    .. data:: emergency = 0

    	System is unusable                (severity=0)

    .. data:: alert = 1

    	Immediate action needed           (severity=1)

    .. data:: critical = 2

    	Critical conditions               (severity=2)

    .. data:: error = 3

    	Error conditions                  (severity=3)

    .. data:: warning = 4

    	Warning conditions                (severity=4)

    .. data:: notice = 5

    	Normal but significant conditions (severity=5)

    .. data:: informational = 6

    	Informational messages            (severity=6)

    .. data:: debug = 7

    	Debugging messages                (severity=7)

    """

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    informational = 6

    debug = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LogSeverityEnum']


class LoggingDscpEnum(Enum):
    """
    LoggingDscpEnum

    Logging dscp

    .. data:: dscp = 1

    	Logging TOS type DSCP

    """

    dscp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingDscpEnum']


class LoggingDscpValueEnum(Enum):
    """
    LoggingDscpValueEnum

    Logging dscp value

    .. data:: default = 0

    	Applicable to DSCP: bits 000000

    .. data:: af11 = 10

    	Applicable to DSCP: bits 001010

    .. data:: af12 = 12

    	Applicable to DSCP: bits 001100

    .. data:: af13 = 14

    	Applicable to DSCP: bits 001110

    .. data:: af21 = 18

    	Applicable to DSCP: bits 010010

    .. data:: af22 = 20

    	Applicable to DSCP: bits 010100

    .. data:: af23 = 22

    	Applicable to DSCP: bits 010110

    .. data:: af31 = 26

    	Applicable to DSCP: bits 011010

    .. data:: af32 = 28

    	Applicable to DSCP: bits 011100

    .. data:: af33 = 30

    	Applicable to DSCP: bits 011110

    .. data:: af41 = 34

    	Applicable to DSCP: bits 100010

    .. data:: af42 = 36

    	Applicable to DSCP: bits 100100

    .. data:: af43 = 38

    	Applicable to DSCP: bits 100110

    .. data:: ef = 46

    	Applicable to DSCP: bits 101110

    .. data:: cs1 = 8

    	Applicable to DSCP: bits 001000

    .. data:: cs2 = 16

    	Applicable to DSCP: bits 010000

    .. data:: cs3 = 24

    	Applicable to DSCP: bits 011000

    .. data:: cs4 = 32

    	Applicable to DSCP: bits 100000

    .. data:: cs5 = 40

    	Applicable to DSCP: bits 101000

    .. data:: cs6 = 48

    	Applicable to DSCP: bits 110000

    .. data:: cs7 = 56

    	Applicable to DSCP: bits 111000

    """

    default = 0

    af11 = 10

    af12 = 12

    af13 = 14

    af21 = 18

    af22 = 20

    af23 = 22

    af31 = 26

    af32 = 28

    af33 = 30

    af41 = 34

    af42 = 36

    af43 = 38

    ef = 46

    cs1 = 8

    cs2 = 16

    cs3 = 24

    cs4 = 32

    cs5 = 40

    cs6 = 48

    cs7 = 56


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingDscpValueEnum']


class LoggingLevelsEnum(Enum):
    """
    LoggingLevelsEnum

    Logging levels

    .. data:: emergency = 0

    	Emergency Level Msg

    .. data:: alert = 1

    	Alert Level Msg

    .. data:: critical = 2

    	Critical Level Msg

    .. data:: error = 3

    	Error Level Msg

    .. data:: warning = 4

    	Warning Level Msg

    .. data:: notice = 5

    	Notification Level Msg

    .. data:: info = 6

    	Informational Level Msg

    .. data:: debug = 7

    	Debugging Level Msg

    .. data:: disable = 15

    	Disable logging

    """

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    info = 6

    debug = 7

    disable = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingLevelsEnum']


class LoggingPrecedenceEnum(Enum):
    """
    LoggingPrecedenceEnum

    Logging precedence

    .. data:: precedence = 0

    	Logging TOS type precedence

    """

    precedence = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingPrecedenceEnum']


class LoggingPrecedenceValueEnum(Enum):
    """
    LoggingPrecedenceValueEnum

    Logging precedence value

    .. data:: routine = 0

    	Applicable to precedence: value 0

    .. data:: priority = 1

    	Applicable to precedence: value 1

    .. data:: immediate = 2

    	Applicable to precedence: value 2

    .. data:: flash = 3

    	Applicable to precedence: value 3

    .. data:: flash_override = 4

    	Applicable to precedence: value 4

    .. data:: critical = 5

    	Applicable to precedence: value 5

    .. data:: internet = 6

    	Applicable to precedence: value 6

    .. data:: network = 7

    	Applicable to precedence: value 7

    """

    routine = 0

    priority = 1

    immediate = 2

    flash = 3

    flash_override = 4

    critical = 5

    internet = 6

    network = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingPrecedenceValueEnum']


class LoggingTosEnum(Enum):
    """
    LoggingTosEnum

    Logging tos

    .. data:: precedence = 0

    	Logging TOS type precedence

    .. data:: dscp = 1

    	Logging TOS type DSCP

    """

    precedence = 0

    dscp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['LoggingTosEnum']


class TimeInfoEnum(Enum):
    """
    TimeInfoEnum

    Time info

    .. data:: disable = 0

    	Exclude

    .. data:: enable = 1

    	Include

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['TimeInfoEnum']



class SyslogService(object):
    """
    Syslog Timestamp Services
    
    .. attribute:: timestamps
    
    	Timestamp debug/log messages configuration
    	**type**\:   :py:class:`Timestamps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        self.timestamps = SyslogService.Timestamps()
        self.timestamps.parent = self


    class Timestamps(object):
        """
        Timestamp debug/log messages configuration
        
        .. attribute:: debug
        
        	Timestamp debug messages
        	**type**\:   :py:class:`Debug <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug>`
        
        .. attribute:: enable
        
        	Enable timestamp debug/log messages
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log
        
        	Timestamp log messages
        	**type**\:   :py:class:`Log <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:   :py:class:`LogDatetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime>`
            
            .. attribute:: log_timestamp_disable
            
            	Disable timestamp log messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_uptime
            
            	Timestamp with systime uptime
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                	**type**\:   :py:class:`LogDatetimeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    self.parent = None
                    self.log_datetime_value = SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue()
                    self.log_datetime_value.parent = self


                class LogDatetimeValue(object):
                    """
                    Set timestamp for log message
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**units**\: second
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**default value**\: disable
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**default value**\: disable
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:log/Cisco-IOS-XR-infra-syslog-cfg:log-datetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.log_datetime_value is not None and self.log_datetime_value._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['SyslogService.Timestamps.Log.LogDatetime']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:log'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.log_datetime is not None and self.log_datetime._has_data():
                    return True

                if self.log_timestamp_disable is not None:
                    return True

                if self.log_uptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['SyslogService.Timestamps.Log']['meta_info']


        class Debug(object):
            """
            Timestamp debug messages
            
            .. attribute:: debug_datetime
            
            	Timestamp with date and time
            	**type**\:   :py:class:`DebugDatetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime>`
            
            .. attribute:: debug_timestamp_disable
            
            	Disable timestamp debug messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: debug_uptime
            
            	Timestamp with systime uptime
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                	**type**\:   :py:class:`DatetimeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    self.parent = None
                    self.datetime_value = SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue()
                    self.datetime_value.parent = self


                class DatetimeValue(object):
                    """
                    Set time format for debug msg
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**units**\: second
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**default value**\: disable
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\:   :py:class:`TimeInfoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfoEnum>`
                    
                    	**default value**\: disable
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:debug/Cisco-IOS-XR-infra-syslog-cfg:debug-datetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.datetime_value is not None and self.datetime_value._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['SyslogService.Timestamps.Debug.DebugDatetime']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps/Cisco-IOS-XR-infra-syslog-cfg:debug'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.debug_datetime is not None and self.debug_datetime._has_data():
                    return True

                if self.debug_timestamp_disable is not None:
                    return True

                if self.debug_uptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['SyslogService.Timestamps.Debug']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service/Cisco-IOS-XR-infra-syslog-cfg:timestamps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.debug is not None and self.debug._has_data():
                return True

            if self.enable is not None:
                return True

            if self.log is not None and self.log._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['SyslogService.Timestamps']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-cfg:syslog-service'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.timestamps is not None and self.timestamps._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['SyslogService']['meta_info']


class Syslog(object):
    """
    syslog
    
    .. attribute:: alarm_logger
    
    	Alarm Logger Properties
    	**type**\:   :py:class:`AlarmLogger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger>`
    
    .. attribute:: archive
    
    	Archive attributes configuration
    	**type**\:   :py:class:`Archive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Archive>`
    
    .. attribute:: buffered_logging
    
    	Set buffered logging parameters
    	**type**\:   :py:class:`BufferedLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.BufferedLogging>`
    
    .. attribute:: console_logging
    
    	Set console logging
    	**type**\:   :py:class:`ConsoleLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging>`
    
    .. attribute:: correlator
    
    	Configure properties of the event correlator
    	**type**\:   :py:class:`Correlator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator>`
    
    .. attribute:: enable_console_logging
    
    	Enabled or disabled
    	**type**\:  bool
    
    .. attribute:: files
    
    	Configure logging file destination
    	**type**\:   :py:class:`Files <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files>`
    
    .. attribute:: history_logging
    
    	Set history logging
    	**type**\:   :py:class:`HistoryLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HistoryLogging>`
    
    .. attribute:: host_name_prefix
    
    	Hostname prefix to add on msgs to servers
    	**type**\:  str
    
    .. attribute:: host_server
    
    	Configure logging host
    	**type**\:   :py:class:`HostServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer>`
    
    .. attribute:: ipv4
    
    	Syslog TOS bit for outgoing messages
    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4>`
    
    .. attribute:: ipv6
    
    	Syslog traffic class bit for outgoing messages
    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6>`
    
    .. attribute:: local_log_file_size
    
    	Set size of the local log file
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**default value**\: 32768
    
    .. attribute:: logging_facilities
    
    	Modify message logging facilities
    	**type**\:   :py:class:`LoggingFacilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.LoggingFacilities>`
    
    .. attribute:: monitor_logging
    
    	Set monitor logging
    	**type**\:   :py:class:`MonitorLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging>`
    
    .. attribute:: source_interface_table
    
    	Configure source interface
    	**type**\:   :py:class:`SourceInterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable>`
    
    .. attribute:: suppress_duplicates
    
    	Suppress consecutive duplicate messages
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: suppression
    
    	Configure properties of the syslog/alarm suppression
    	**type**\:   :py:class:`Suppression <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression>`
    
    .. attribute:: trap_logging
    
    	Set trap logging
    	**type**\:   :py:class:`TrapLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.TrapLogging>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        self.alarm_logger = Syslog.AlarmLogger()
        self.alarm_logger.parent = self
        self.archive = Syslog.Archive()
        self.archive.parent = self
        self.buffered_logging = Syslog.BufferedLogging()
        self.buffered_logging.parent = self
        self.console_logging = Syslog.ConsoleLogging()
        self.console_logging.parent = self
        self.correlator = Syslog.Correlator()
        self.correlator.parent = self
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
        self.suppression = Syslog.Suppression()
        self.suppression.parent = self
        self.trap_logging = Syslog.TrapLogging()
        self.trap_logging.parent = self


    class MonitorLogging(object):
        """
        Set monitor logging
        
        .. attribute:: logging_level
        
        	Monitor Logging Level
        	**type**\:   :py:class:`LoggingLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        	**default value**\: debug
        
        .. attribute:: monitor_discriminator
        
        	Set monitor logging discriminators
        	**type**\:   :py:class:`MonitorDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging.MonitorDiscriminator>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:  str
            
            .. attribute:: match2
            
            	Set monitor logging match2 discriminator
            	**type**\:  str
            
            .. attribute:: match3
            
            	Set monitor logging match3 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch1
            
            	Set monitor logging no\-match1 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch2
            
            	Set monitor logging no\-match2 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch3
            
            	Set monitor logging no\-match3 discriminator
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.MonitorLogging.MonitorDiscriminator']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:monitor-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.logging_level is not None:
                return True

            if self.monitor_discriminator is not None and self.monitor_discriminator._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.MonitorLogging']['meta_info']


    class HistoryLogging(object):
        """
        Set history logging
        
        .. attribute:: history_size
        
        	Logging history size
        	**type**\:  int
        
        	**range:** 1..500
        
        	**default value**\: 1
        
        .. attribute:: logging_level
        
        	History logging level
        	**type**\:   :py:class:`LoggingLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        	**default value**\: warning
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            if self.history_size is not None:
                return True

            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.HistoryLogging']['meta_info']


    class LoggingFacilities(object):
        """
        Modify message logging facilities
        
        .. attribute:: facility_level
        
        	Facility from which logging is done
        	**type**\:   :py:class:`FacilityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.FacilityEnum>`
        
        	**default value**\: local7
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            if self.facility_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.LoggingFacilities']['meta_info']


    class TrapLogging(object):
        """
        Set trap logging
        
        .. attribute:: logging_level
        
        	Trap logging level
        	**type**\:   :py:class:`LoggingLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        	**default value**\: info
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.TrapLogging']['meta_info']


    class BufferedLogging(object):
        """
        Set buffered logging parameters
        
        .. attribute:: buffer_size
        
        	Logging buffered size
        	**type**\:  int
        
        	**range:** 4096..4294967295
        
        	**default value**\: 2097152
        
        .. attribute:: buffered_discriminator
        
        	Set buffered logging discriminators
        	**type**\:   :py:class:`BufferedDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.BufferedLogging.BufferedDiscriminator>`
        
        .. attribute:: logging_level
        
        	Logging level for Buffered logging
        	**type**\:   :py:class:`LoggingLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        	**default value**\: debug
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:  str
            
            .. attribute:: match2
            
            	Set buffered logging match2 discriminator
            	**type**\:  str
            
            .. attribute:: match3
            
            	Set buffered logging match3 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch1
            
            	Set buffered logging no\-match1 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch2
            
            	Set buffered logging no\-match2 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch3
            
            	Set buffered logging no\-match3 discriminator
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.BufferedLogging.BufferedDiscriminator']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:buffered-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.buffer_size is not None:
                return True

            if self.buffered_discriminator is not None and self.buffered_discriminator._has_data():
                return True

            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.BufferedLogging']['meta_info']


    class HostServer(object):
        """
        Configure logging host
        
        .. attribute:: vrfs
        
        	VRF table
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            self.parent = None
            self.vrfs = Syslog.HostServer.Vrfs()
            self.vrfs.parent = self


        class Vrfs(object):
            """
            VRF table
            
            .. attribute:: vrf
            
            	VRF specific data
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: hosts
                
                	List of the logging host
                	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts>`
                
                .. attribute:: ipv4s
                
                	List of the IPv4 logging host
                	**type**\:   :py:class:`Ipv4S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S>`
                
                .. attribute:: ipv6s
                
                	List of the IPv6 logging host
                	**type**\:   :py:class:`Ipv6S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

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
                    	**type**\: list of    :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

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
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_discriminator
                        
                        	Set IPv6 logging discriminators
                        	**type**\:   :py:class:`Ipv6Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator>`
                        
                        .. attribute:: ipv6_severity_levels
                        
                        	Severity container of the logging host
                        	**type**\:   :py:class:`Ipv6SeverityLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels>`
                        
                        	**status**\: obsolete
                        
                        .. attribute:: ipv6_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\:   :py:class:`Ipv6SeverityPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort>`
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2016-06-22'

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
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 514
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 6
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                if self.port is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort']['meta_info']


                        class Ipv6Discriminator(object):
                            """
                            Set IPv6 logging discriminators
                            
                            .. attribute:: match1
                            
                            	Set IPv6 logging match1 discriminator
                            	**type**\:  str
                            
                            .. attribute:: match2
                            
                            	Set IPv6 logging match2 discriminator
                            	**type**\:  str
                            
                            .. attribute:: match3
                            
                            	Set IPv6 logging match3 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch1
                            
                            	Set IPv6 logging no\-match1 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch2
                            
                            	Set IPv6 logging no\-match2 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch3
                            
                            	Set IPv6 logging no\-match3 discriminator
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator']['meta_info']


                        class Ipv6SeverityLevels(object):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: ipv6_severity_level
                            
                            	Severity for the logging host
                            	**type**\: list of    :py:class:`Ipv6SeverityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel>`
                            
                            	**status**\: obsolete
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                	**type**\:   :py:class:`LogSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverityEnum>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2016-06-22'

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
                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                                if self.ipv6_severity_level is not None:
                                    for child_ref in self.ipv6_severity_level:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                        if self.ipv6 is not None:
                            for child_ref in self.ipv6:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv6S']['meta_info']


                class Hosts(object):
                    """
                    List of the logging host
                    
                    .. attribute:: host
                    
                    	Name of the logging host
                    	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

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
                        	**type**\:  str
                        
                        .. attribute:: host_name_discriminator
                        
                        	Set Hostname logging discriminators
                        	**type**\:   :py:class:`HostNameDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator>`
                        
                        .. attribute:: host_name_severities
                        
                        	Severity container of the logging host
                        	**type**\:   :py:class:`HostNameSeverities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities>`
                        
                        	**status**\: obsolete
                        
                        .. attribute:: host_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\:   :py:class:`HostSeverityPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort>`
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2016-06-22'

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
                            	**type**\: list of    :py:class:`HostNameSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity>`
                            
                            	**status**\: obsolete
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                	**type**\:   :py:class:`LogSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverityEnum>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2016-06-22'

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
                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                                if self.host_name_severity is not None:
                                    for child_ref in self.host_name_severity:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities']['meta_info']


                        class HostNameDiscriminator(object):
                            """
                            Set Hostname logging discriminators
                            
                            .. attribute:: match1
                            
                            	Set hostname logging match1 discriminator
                            	**type**\:  str
                            
                            .. attribute:: match2
                            
                            	Set hostname logging match2 discriminator
                            	**type**\:  str
                            
                            .. attribute:: match3
                            
                            	Set hostname logging match3 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch1
                            
                            	Set hostname logging no\-match1 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch2
                            
                            	Set hostname logging no\-match2 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch3
                            
                            	Set hostname logging no\-match3 discriminator
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator']['meta_info']


                        class HostSeverityPort(object):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 514
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 6
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                if self.port is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                        if self.host is not None:
                            for child_ref in self.host:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Hosts']['meta_info']


                class Ipv4S(object):
                    """
                    List of the IPv4 logging host
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address of the logging host
                    	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

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
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv4_discriminator
                        
                        	Set IPv4 logging discriminators
                        	**type**\:   :py:class:`Ipv4Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator>`
                        
                        .. attribute:: ipv4_severity_levels
                        
                        	Severity container of the logging host
                        	**type**\:   :py:class:`Ipv4SeverityLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels>`
                        
                        	**status**\: obsolete
                        
                        .. attribute:: ipv4_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\:   :py:class:`Ipv4SeverityPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort>`
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2016-06-22'

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
                            	**type**\: list of    :py:class:`Ipv4SeverityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel>`
                            
                            	**status**\: obsolete
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                	**type**\:   :py:class:`LogSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverityEnum>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2016-06-22'

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
                                    if self.severity is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                                if self.ipv4_severity_level is not None:
                                    for child_ref in self.ipv4_severity_level:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels']['meta_info']


                        class Ipv4SeverityPort(object):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 514
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 6
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                if self.port is not None:
                                    return True

                                if self.severity is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort']['meta_info']


                        class Ipv4Discriminator(object):
                            """
                            Set IPv4 logging discriminators
                            
                            .. attribute:: match1
                            
                            	Set IPv4 logging match1 discriminator
                            	**type**\:  str
                            
                            .. attribute:: match2
                            
                            	Set IPv4 logging match2 discriminator
                            	**type**\:  str
                            
                            .. attribute:: match3
                            
                            	Set IPv4 logging match3 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch1
                            
                            	Set IPv4 logging no\-match1 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch2
                            
                            	Set IPv4 logging no\-match2 discriminator
                            	**type**\:  str
                            
                            .. attribute:: nomatch3
                            
                            	Set IPv4 logging no\-match3 discriminator
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2016-06-22'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                        if self.ipv4 is not None:
                            for child_ref in self.ipv4:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.HostServer.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:host-server/Cisco-IOS-XR-infra-syslog-cfg:vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf is not None:
                    for child_ref in self.vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.HostServer.Vrfs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:host-server'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrfs is not None and self.vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.HostServer']['meta_info']


    class ConsoleLogging(object):
        """
        Set console logging
        
        .. attribute:: console_discriminator
        
        	Set console logging discriminators
        	**type**\:   :py:class:`ConsoleDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging.ConsoleDiscriminator>`
        
        .. attribute:: logging_level
        
        	Console logging level
        	**type**\:   :py:class:`LoggingLevelsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevelsEnum>`
        
        	**default value**\: warning
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:  str
            
            .. attribute:: match2
            
            	Set console logging match2 discriminator
            	**type**\:  str
            
            .. attribute:: match3
            
            	Set console logging match3 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch1
            
            	Set console logging no\-match1 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch2
            
            	Set console logging no\-match2 discriminator
            	**type**\:  str
            
            .. attribute:: nomatch3
            
            	Set console logging no\-match3 discriminator
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.ConsoleLogging.ConsoleDiscriminator']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:console-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.console_discriminator is not None and self.console_discriminator._has_data():
                return True

            if self.logging_level is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.ConsoleLogging']['meta_info']


    class Files(object):
        """
        Configure logging file destination
        
        .. attribute:: file
        
        	Specify File Name
        	**type**\: list of    :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: file_log_attributes
            
            	Attributes of the logging file destination
            	**type**\:   :py:class:`FileLogAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileLogAttributes>`
            
            .. attribute:: file_log_discriminator
            
            	Set File logging discriminators
            	**type**\:   :py:class:`FileLogDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileLogDiscriminator>`
            
            .. attribute:: file_specification
            
            	Specifications of the logging file destination
            	**type**\:   :py:class:`FileSpecification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileSpecification>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self.file_name = None
                self.file_log_attributes = Syslog.Files.File.FileLogAttributes()
                self.file_log_attributes.parent = self
                self.file_log_discriminator = Syslog.Files.File.FileLogDiscriminator()
                self.file_log_discriminator.parent = self
                self.file_specification = Syslog.Files.File.FileSpecification()
                self.file_specification.parent = self


            class FileSpecification(object):
                """
                Specifications of the logging file destination
                
                .. attribute:: max_file_size
                
                	Maximum file size (in KB)
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 1024
                
                .. attribute:: path
                
                	File path
                	**type**\:  str
                
                .. attribute:: severity
                
                	Severity of messages
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 6
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

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
                    if self.max_file_size is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.severity is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Files.File.FileSpecification']['meta_info']


            class FileLogAttributes(object):
                """
                Attributes of the logging file destination
                
                .. attribute:: max_file_size
                
                	Maximum file size (in KB)
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 1024
                
                .. attribute:: severity
                
                	Severity of messages
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 6
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    self.parent = None
                    self.max_file_size = None
                    self.severity = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-syslog-cfg:file-log-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.max_file_size is not None:
                        return True

                    if self.severity is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Files.File.FileLogAttributes']['meta_info']


            class FileLogDiscriminator(object):
                """
                Set File logging discriminators
                
                .. attribute:: match1
                
                	Set file logging match discriminator 1
                	**type**\:  str
                
                .. attribute:: match2
                
                	Set file logging match discriminator 2
                	**type**\:  str
                
                .. attribute:: match3
                
                	Set file logging match discriminator 3
                	**type**\:  str
                
                .. attribute:: nomatch1
                
                	Set file logging no match discriminator 1
                	**type**\:  str
                
                .. attribute:: nomatch2
                
                	Set file logging no match discriminator 2
                	**type**\:  str
                
                .. attribute:: nomatch3
                
                	Set file logging no match discriminator 3
                	**type**\:  str
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                if self.file_name is not None:
                    return True

                if self.file_log_attributes is not None and self.file_log_attributes._has_data():
                    return True

                if self.file_log_discriminator is not None and self.file_log_discriminator._has_data():
                    return True

                if self.file_specification is not None and self.file_specification._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Files.File']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:files'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.file is not None:
                for child_ref in self.file:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Files']['meta_info']


    class Ipv4(object):
        """
        Syslog TOS bit for outgoing messages
        
        .. attribute:: dscp
        
        	DSCP value
        	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Dscp>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        .. attribute:: precedence
        
        	Precedence value
        	**type**\:   :py:class:`Precedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Precedence>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        .. attribute:: tos
        
        	Type of service
        	**type**\:   :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Tos>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:   :py:class:`LoggingDscpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self._is_presence = True
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
                if self._is_presence:
                    return True
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv4.Dscp']['meta_info']


        class Tos(object):
            """
            Type of service
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\:   :py:class:`LoggingTosEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingTosEnum>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                if self.dscp is not None:
                    return True

                if self.precedence is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv4.Tos']['meta_info']


        class Precedence(object):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\:   :py:class:`LoggingPrecedenceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self._is_presence = True
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
                if self._is_presence:
                    return True
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv4.Precedence']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv4'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.dscp is not None and self.dscp._has_data():
                return True

            if self.precedence is not None and self.precedence._has_data():
                return True

            if self.tos is not None and self.tos._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Ipv4']['meta_info']


    class Archive(object):
        """
        Archive attributes configuration
        
        .. attribute:: device
        
        	'/disk0\:' or '/disk1\:' or '/harddisk\:'
        	**type**\:  str
        
        .. attribute:: file_size
        
        	The maximum file size for a single log file
        	**type**\:  int
        
        	**range:** 1..2047
        
        .. attribute:: frequency
        
        	The collection interval for logs
        	**type**\:   :py:class:`LogCollectFrequencyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogCollectFrequencyEnum>`
        
        .. attribute:: length
        
        	The maximum number of weeks of log to maintain
        	**type**\:  int
        
        	**range:** 1..256
        
        .. attribute:: severity
        
        	The minimum severity of log messages to archive
        	**type**\:   :py:class:`LogMessageSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogMessageSeverityEnum>`
        
        .. attribute:: size
        
        	The total size of the archive
        	**type**\:  int
        
        	**range:** 1..2047
        
        .. attribute:: threshold
        
        	The size threshold at which a syslog is generated
        	**type**\:  int
        
        	**range:** 1..99
        
        	**units**\: percentage
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Archive']['meta_info']


    class Ipv6(object):
        """
        Syslog traffic class bit for outgoing messages
        
        .. attribute:: dscp
        
        	DSCP value
        	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.Dscp>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        .. attribute:: precedence
        
        	Precedence value
        	**type**\:   :py:class:`Precedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.Precedence>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        .. attribute:: traffic_class
        
        	Type of traffic class
        	**type**\:   :py:class:`TrafficClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.TrafficClass>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\:   :py:class:`LoggingDscpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self._is_presence = True
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
                if self._is_presence:
                    return True
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv6.Dscp']['meta_info']


        class TrafficClass(object):
            """
            Type of traffic class
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\:   :py:class:`LoggingTosEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingTosEnum>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                if self.dscp is not None:
                    return True

                if self.precedence is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv6.TrafficClass']['meta_info']


        class Precedence(object):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\:   :py:class:`LoggingPrecedenceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValueEnum>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                self.parent = None
                self._is_presence = True
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
                if self._is_presence:
                    return True
                if self.type is not None:
                    return True

                if self.unused is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Ipv6.Precedence']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:ipv6'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.dscp is not None and self.dscp._has_data():
                return True

            if self.precedence is not None and self.precedence._has_data():
                return True

            if self.traffic_class is not None and self.traffic_class._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Ipv6']['meta_info']


    class SourceInterfaceTable(object):
        """
        Configure source interface
        
        .. attribute:: source_interface_values
        
        	Specify interface for source address in logging transactions
        	**type**\:   :py:class:`SourceInterfaceValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

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
            	**type**\: list of    :py:class:`SourceInterfaceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

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
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: source_interface_vrfs
                
                	Configure source interface VRF
                	**type**\:   :py:class:`SourceInterfaceVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

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
                    	**type**\: list of    :py:class:`SourceInterfaceVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

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
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2016-06-22'

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
                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                        if self.source_interface_vrf is not None:
                            for child_ref in self.source_interface_vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
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
                    if self.src_interface_name_value is not None:
                        return True

                    if self.source_interface_vrfs is not None and self.source_interface_vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:source-interface-table/Cisco-IOS-XR-infra-syslog-cfg:source-interface-values'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.source_interface_value is not None:
                    for child_ref in self.source_interface_value:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.SourceInterfaceTable.SourceInterfaceValues']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-syslog-cfg:source-interface-table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.source_interface_values is not None and self.source_interface_values._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.SourceInterfaceTable']['meta_info']


    class AlarmLogger(object):
        """
        Alarm Logger Properties
        
        .. attribute:: alarm_filter_strings
        
        	List of filter strings
        	**type**\:   :py:class:`AlarmFilterStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger.AlarmFilterStrings>`
        
        .. attribute:: buffer_size
        
        	Set size of the local event buffer
        	**type**\:  int
        
        	**range:** 1024..1024000
        
        .. attribute:: severity_level
        
        	Log all events with equal or higher (lower level) severity than this
        	**type**\:   :py:class:`AlarmLoggerSeverityLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes.AlarmLoggerSeverityLevelEnum>`
        
        .. attribute:: source_location
        
        	Enable alarm source location in message text
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: threshold
        
        	Configure threshold (%) for capacity alarm
        	**type**\:  int
        
        	**range:** 10..100
        
        	**default value**\: 90
        
        

        """

        _prefix = 'infra-alarm-logger-cfg'
        _revision = '2016-08-10'

        def __init__(self):
            self.parent = None
            self.alarm_filter_strings = Syslog.AlarmLogger.AlarmFilterStrings()
            self.alarm_filter_strings.parent = self
            self.buffer_size = None
            self.severity_level = None
            self.source_location = None
            self.threshold = None


        class AlarmFilterStrings(object):
            """
            List of filter strings
            
            .. attribute:: alarm_filter_string
            
            	Match string to filter alarms
            	**type**\: list of    :py:class:`AlarmFilterString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString>`
            
            

            """

            _prefix = 'infra-alarm-logger-cfg'
            _revision = '2016-08-10'

            def __init__(self):
                self.parent = None
                self.alarm_filter_string = YList()
                self.alarm_filter_string.parent = self
                self.alarm_filter_string.name = 'alarm_filter_string'


            class AlarmFilterString(object):
                """
                Match string to filter alarms
                
                .. attribute:: filter_string  <key>
                
                	Filter String
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                

                """

                _prefix = 'infra-alarm-logger-cfg'
                _revision = '2016-08-10'

                def __init__(self):
                    self.parent = None
                    self.filter_string = None

                @property
                def _common_path(self):
                    if self.filter_string is None:
                        raise YPYModelError('Key property filter_string is None')

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-filter-strings/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-filter-string[Cisco-IOS-XR-infra-alarm-logger-cfg:filter-string = ' + str(self.filter_string) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.filter_string is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-filter-strings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.alarm_filter_string is not None:
                    for child_ref in self.alarm_filter_string:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.AlarmLogger.AlarmFilterStrings']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.alarm_filter_strings is not None and self.alarm_filter_strings._has_data():
                return True

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.AlarmLogger']['meta_info']


    class Correlator(object):
        """
        Configure properties of the event correlator
        
        .. attribute:: buffer_size
        
        	Configure size of the correlator buffer
        	**type**\:  int
        
        	**range:** 1024..52428800
        
        .. attribute:: rule_sets
        
        	Table of configured rulesets
        	**type**\:   :py:class:`RuleSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets>`
        
        .. attribute:: rules
        
        	Table of configured rules
        	**type**\:   :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules>`
        
        

        """

        _prefix = 'infra-correlator-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.buffer_size = None
            self.rule_sets = Syslog.Correlator.RuleSets()
            self.rule_sets.parent = self
            self.rules = Syslog.Correlator.Rules()
            self.rules.parent = self


        class Rules(object):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule = YList()
                self.rule.parent = self
                self.rule.name = 'rule'


            class Rule(object):
                """
                Rule name
                
                .. attribute:: name  <key>
                
                	Rule name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:   :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo>`
                
                .. attribute:: apply_to
                
                	Apply the Rules
                	**type**\:   :py:class:`ApplyTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.ApplyTo>`
                
                .. attribute:: definition
                
                	Configure a specified correlation rule
                	**type**\:   :py:class:`Definition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Definition>`
                
                .. attribute:: non_stateful
                
                	The Non\-Stateful Rule Type
                	**type**\:   :py:class:`NonStateful <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful>`
                
                .. attribute:: stateful
                
                	The Stateful Rule Type
                	**type**\:   :py:class:`Stateful <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful>`
                
                

                """

                _prefix = 'infra-correlator-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.applied_to = Syslog.Correlator.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self.apply_to = Syslog.Correlator.Rules.Rule.ApplyTo()
                    self.apply_to.parent = self
                    self.definition = Syslog.Correlator.Rules.Rule.Definition()
                    self.definition.parent = self
                    self.non_stateful = Syslog.Correlator.Rules.Rule.NonStateful()
                    self.non_stateful.parent = self
                    self.stateful = Syslog.Correlator.Rules.Rule.Stateful()
                    self.stateful.parent = self


                class Definition(object):
                    """
                    Configure a specified correlation rule
                    
                    .. attribute:: category_name_entry1
                    
                    	Root message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry10
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry2
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry3
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry4
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry5
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry6
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry7
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry8
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: category_name_entry9
                    
                    	Correlated message category name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry1
                    
                    	Root message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry10
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry2
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry3
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry4
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry5
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry6
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry7
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry8
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: group_name_entry9
                    
                    	Correlated message group name
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry1
                    
                    	Root message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry10
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry2
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry3
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry4
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry5
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry6
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry7
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry8
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: message_code_entry9
                    
                    	Correlated message code
                    	**type**\:  str
                    
                    .. attribute:: timeout
                    
                    	Timeout (time the rule is to be active) in milliseconds
                    	**type**\:  int
                    
                    	**range:** 1..7200000
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.category_name_entry1 = None
                        self.category_name_entry10 = None
                        self.category_name_entry2 = None
                        self.category_name_entry3 = None
                        self.category_name_entry4 = None
                        self.category_name_entry5 = None
                        self.category_name_entry6 = None
                        self.category_name_entry7 = None
                        self.category_name_entry8 = None
                        self.category_name_entry9 = None
                        self.group_name_entry1 = None
                        self.group_name_entry10 = None
                        self.group_name_entry2 = None
                        self.group_name_entry3 = None
                        self.group_name_entry4 = None
                        self.group_name_entry5 = None
                        self.group_name_entry6 = None
                        self.group_name_entry7 = None
                        self.group_name_entry8 = None
                        self.group_name_entry9 = None
                        self.message_code_entry1 = None
                        self.message_code_entry10 = None
                        self.message_code_entry2 = None
                        self.message_code_entry3 = None
                        self.message_code_entry4 = None
                        self.message_code_entry5 = None
                        self.message_code_entry6 = None
                        self.message_code_entry7 = None
                        self.message_code_entry8 = None
                        self.message_code_entry9 = None
                        self.timeout = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:definition'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.category_name_entry1 is not None:
                            return True

                        if self.category_name_entry10 is not None:
                            return True

                        if self.category_name_entry2 is not None:
                            return True

                        if self.category_name_entry3 is not None:
                            return True

                        if self.category_name_entry4 is not None:
                            return True

                        if self.category_name_entry5 is not None:
                            return True

                        if self.category_name_entry6 is not None:
                            return True

                        if self.category_name_entry7 is not None:
                            return True

                        if self.category_name_entry8 is not None:
                            return True

                        if self.category_name_entry9 is not None:
                            return True

                        if self.group_name_entry1 is not None:
                            return True

                        if self.group_name_entry10 is not None:
                            return True

                        if self.group_name_entry2 is not None:
                            return True

                        if self.group_name_entry3 is not None:
                            return True

                        if self.group_name_entry4 is not None:
                            return True

                        if self.group_name_entry5 is not None:
                            return True

                        if self.group_name_entry6 is not None:
                            return True

                        if self.group_name_entry7 is not None:
                            return True

                        if self.group_name_entry8 is not None:
                            return True

                        if self.group_name_entry9 is not None:
                            return True

                        if self.message_code_entry1 is not None:
                            return True

                        if self.message_code_entry10 is not None:
                            return True

                        if self.message_code_entry2 is not None:
                            return True

                        if self.message_code_entry3 is not None:
                            return True

                        if self.message_code_entry4 is not None:
                            return True

                        if self.message_code_entry5 is not None:
                            return True

                        if self.message_code_entry6 is not None:
                            return True

                        if self.message_code_entry7 is not None:
                            return True

                        if self.message_code_entry8 is not None:
                            return True

                        if self.message_code_entry9 is not None:
                            return True

                        if self.timeout is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.Rules.Rule.Definition']['meta_info']


                class NonStateful(object):
                    """
                    The Non\-Stateful Rule Type
                    
                    .. attribute:: context_correlation
                    
                    	Enable correlation on alarm context
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: non_root_causes
                    
                    	Table of configured non\-rootcause
                    	**type**\:   :py:class:`NonRootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses>`
                    
                    .. attribute:: root_cause
                    
                    	The root cause
                    	**type**\:   :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.RootCause>`
                    
                    .. attribute:: timeout
                    
                    	Timeout (time to wait for active correlation) in milliseconds
                    	**type**\:  int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: timeout_root_cause
                    
                    	Rootcause Timeout (time to wait for rootcause) in milliseconds
                    	**type**\:  int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.context_correlation = None
                        self.non_root_causes = Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self.root_cause = Syslog.Correlator.Rules.Rule.NonStateful.RootCause()
                        self.root_cause.parent = self
                        self.timeout = None
                        self.timeout_root_cause = None


                    class NonRootCauses(object):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of    :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.non_root_cause = YList()
                            self.non_root_cause.parent = self
                            self.non_root_cause.name = 'non_root_cause'


                        class NonRootCause(object):
                            """
                            A non\-rootcause
                            
                            .. attribute:: category  <key>
                            
                            	Correlated message category
                            	**type**\:  str
                            
                            .. attribute:: group  <key>
                            
                            	Correlated message group
                            	**type**\:  str
                            
                            .. attribute:: message_code  <key>
                            
                            	Correlated message code
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.category = None
                                self.group = None
                                self.message_code = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.category is None:
                                    raise YPYModelError('Key property category is None')
                                if self.group is None:
                                    raise YPYModelError('Key property group is None')
                                if self.message_code is None:
                                    raise YPYModelError('Key property message_code is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:non-root-cause[Cisco-IOS-XR-infra-correlator-cfg:category = ' + str(self.category) + '][Cisco-IOS-XR-infra-correlator-cfg:group = ' + str(self.group) + '][Cisco-IOS-XR-infra-correlator-cfg:message-code = ' + str(self.message_code) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.category is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.message_code is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:non-root-causes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.non_root_cause is not None:
                                for child_ref in self.non_root_cause:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses']['meta_info']


                    class RootCause(object):
                        """
                        The root cause
                        
                        .. attribute:: category
                        
                        	Root message category
                        	**type**\:  str
                        
                        .. attribute:: group
                        
                        	Root message group
                        	**type**\:  str
                        
                        .. attribute:: message_code
                        
                        	Root message code
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.group = None
                            self.message_code = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:root-cause'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.group is not None:
                                return True

                            if self.message_code is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.NonStateful.RootCause']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:non-stateful'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.context_correlation is not None:
                            return True

                        if self.non_root_causes is not None and self.non_root_causes._has_data():
                            return True

                        if self.root_cause is not None and self.root_cause._has_data():
                            return True

                        if self.timeout is not None:
                            return True

                        if self.timeout_root_cause is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.Rules.Rule.NonStateful']['meta_info']


                class Stateful(object):
                    """
                    The Stateful Rule Type
                    
                    .. attribute:: context_correlation
                    
                    	Enable correlation on alarm context
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: non_root_causes
                    
                    	Table of configured non\-rootcause
                    	**type**\:   :py:class:`NonRootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses>`
                    
                    .. attribute:: reissue
                    
                    	Enable reissue of non\-bistate alarms on rootcause alarm clear
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reparent
                    
                    	Enable reparent of alarm on rootcause alarm clear
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: root_cause
                    
                    	The root cause
                    	**type**\:   :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.RootCause>`
                    
                    .. attribute:: timeout
                    
                    	Timeout (time to wait for active correlation) in milliseconds
                    	**type**\:  int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: timeout_root_cause
                    
                    	Rootcause Timeout (time to wait for rootcause) in milliseconds
                    	**type**\:  int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.context_correlation = None
                        self.non_root_causes = Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self.reissue = None
                        self.reparent = None
                        self.root_cause = Syslog.Correlator.Rules.Rule.Stateful.RootCause()
                        self.root_cause.parent = self
                        self.timeout = None
                        self.timeout_root_cause = None


                    class NonRootCauses(object):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of    :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.non_root_cause = YList()
                            self.non_root_cause.parent = self
                            self.non_root_cause.name = 'non_root_cause'


                        class NonRootCause(object):
                            """
                            A non\-rootcause
                            
                            .. attribute:: category  <key>
                            
                            	Correlated message category
                            	**type**\:  str
                            
                            .. attribute:: group  <key>
                            
                            	Correlated message group
                            	**type**\:  str
                            
                            .. attribute:: message_code  <key>
                            
                            	Correlated message code
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.category = None
                                self.group = None
                                self.message_code = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.category is None:
                                    raise YPYModelError('Key property category is None')
                                if self.group is None:
                                    raise YPYModelError('Key property group is None')
                                if self.message_code is None:
                                    raise YPYModelError('Key property message_code is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:non-root-cause[Cisco-IOS-XR-infra-correlator-cfg:category = ' + str(self.category) + '][Cisco-IOS-XR-infra-correlator-cfg:group = ' + str(self.group) + '][Cisco-IOS-XR-infra-correlator-cfg:message-code = ' + str(self.message_code) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.category is not None:
                                    return True

                                if self.group is not None:
                                    return True

                                if self.message_code is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:non-root-causes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.non_root_cause is not None:
                                for child_ref in self.non_root_cause:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses']['meta_info']


                    class RootCause(object):
                        """
                        The root cause
                        
                        .. attribute:: category
                        
                        	Root message category
                        	**type**\:  str
                        
                        .. attribute:: group
                        
                        	Root message group
                        	**type**\:  str
                        
                        .. attribute:: message_code
                        
                        	Root message code
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.group = None
                            self.message_code = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:root-cause'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.group is not None:
                                return True

                            if self.message_code is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.Stateful.RootCause']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:stateful'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.context_correlation is not None:
                            return True

                        if self.non_root_causes is not None and self.non_root_causes._has_data():
                            return True

                        if self.reissue is not None:
                            return True

                        if self.reparent is not None:
                            return True

                        if self.root_cause is not None and self.root_cause._has_data():
                            return True

                        if self.timeout is not None:
                            return True

                        if self.timeout_root_cause is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.Rules.Rule.Stateful']['meta_info']


                class ApplyTo(object):
                    """
                    Apply the Rules
                    
                    .. attribute:: all_of_router
                    
                    	Apply the rule to all of the router
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: contexts
                    
                    	Apply rule to a specified list of contexts, e.g. interfaces
                    	**type**\:   :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.ApplyTo.Contexts>`
                    
                    .. attribute:: locations
                    
                    	Apply rule to a specified list of Locations
                    	**type**\:   :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.ApplyTo.Locations>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all_of_router = None
                        self.contexts = Syslog.Correlator.Rules.Rule.ApplyTo.Contexts()
                        self.contexts.parent = self
                        self.locations = Syslog.Correlator.Rules.Rule.ApplyTo.Locations()
                        self.locations.parent = self


                    class Contexts(object):
                        """
                        Apply rule to a specified list of contexts,
                        e.g. interfaces
                        
                        .. attribute:: context
                        
                        	One or more context names
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = YLeafList()
                            self.context.parent = self
                            self.context.name = 'context'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:contexts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.context is not None:
                                for child in self.context:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.ApplyTo.Contexts']['meta_info']


                    class Locations(object):
                        """
                        Apply rule to a specified list of Locations
                        
                        .. attribute:: location
                        
                        	One or more Locations
                        	**type**\:  list of str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.location = YLeafList()
                            self.location.parent = self
                            self.location.name = 'location'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:locations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.location is not None:
                                for child in self.location:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.ApplyTo.Locations']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:apply-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all_of_router is not None:
                            return True

                        if self.contexts is not None and self.contexts._has_data():
                            return True

                        if self.locations is not None and self.locations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.Rules.Rule.ApplyTo']['meta_info']


                class AppliedTo(object):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: all
                    
                    	Apply to all of the router
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: contexts
                    
                    	Table of configured contexts to apply
                    	**type**\:   :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Contexts>`
                    
                    .. attribute:: locations
                    
                    	Table of configured locations to apply
                    	**type**\:   :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Locations>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all = None
                        self.contexts = Syslog.Correlator.Rules.Rule.AppliedTo.Contexts()
                        self.contexts.parent = self
                        self.locations = Syslog.Correlator.Rules.Rule.AppliedTo.Locations()
                        self.locations.parent = self


                    class Contexts(object):
                        """
                        Table of configured contexts to apply
                        
                        .. attribute:: context
                        
                        	A context
                        	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = YList()
                            self.context.parent = self
                            self.context.name = 'context'


                        class Context(object):
                            """
                            A context
                            
                            .. attribute:: context  <key>
                            
                            	Context
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.context = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.context is None:
                                    raise YPYModelError('Key property context is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:context[Cisco-IOS-XR-infra-correlator-cfg:context = ' + str(self.context) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.context is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:contexts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.context is not None:
                                for child_ref in self.context:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Contexts']['meta_info']


                    class Locations(object):
                        """
                        Table of configured locations to apply
                        
                        .. attribute:: location
                        
                        	A location
                        	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.location = YList()
                            self.location.parent = self
                            self.location.name = 'location'


                        class Location(object):
                            """
                            A location
                            
                            .. attribute:: location  <key>
                            
                            	Location
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.location = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.location is None:
                                    raise YPYModelError('Key property location is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:location[Cisco-IOS-XR-infra-correlator-cfg:location = ' + str(self.location) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.location is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:locations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.location is not None:
                                for child_ref in self.location:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.Rules.Rule.AppliedTo.Locations']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:applied-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all is not None:
                            return True

                        if self.contexts is not None and self.contexts._has_data():
                            return True

                        if self.locations is not None and self.locations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.Rules.Rule.AppliedTo']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/Cisco-IOS-XR-infra-correlator-cfg:rules/Cisco-IOS-XR-infra-correlator-cfg:rule[Cisco-IOS-XR-infra-correlator-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.applied_to is not None and self.applied_to._has_data():
                        return True

                    if self.apply_to is not None and self.apply_to._has_data():
                        return True

                    if self.definition is not None and self.definition._has_data():
                        return True

                    if self.non_stateful is not None and self.non_stateful._has_data():
                        return True

                    if self.stateful is not None and self.stateful._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Correlator.Rules.Rule']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/Cisco-IOS-XR-infra-correlator-cfg:rules'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rule is not None:
                    for child_ref in self.rule:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Correlator.Rules']['meta_info']


        class RuleSets(object):
            """
            Table of configured rulesets
            
            .. attribute:: rule_set
            
            	Ruleset name
            	**type**\: list of    :py:class:`RuleSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_set = YList()
                self.rule_set.parent = self
                self.rule_set.name = 'rule_set'


            class RuleSet(object):
                """
                Ruleset name
                
                .. attribute:: name  <key>
                
                	Ruleset name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:   :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo>`
                
                .. attribute:: rulenames
                
                	Table of configured rulenames
                	**type**\:   :py:class:`Rulenames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.Rulenames>`
                
                

                """

                _prefix = 'infra-correlator-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.applied_to = Syslog.Correlator.RuleSets.RuleSet.AppliedTo()
                    self.applied_to.parent = self
                    self.rulenames = Syslog.Correlator.RuleSets.RuleSet.Rulenames()
                    self.rulenames.parent = self


                class Rulenames(object):
                    """
                    Table of configured rulenames
                    
                    .. attribute:: rulename
                    
                    	A rulename
                    	**type**\: list of    :py:class:`Rulename <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.rulename = YList()
                        self.rulename.parent = self
                        self.rulename.name = 'rulename'


                    class Rulename(object):
                        """
                        A rulename
                        
                        .. attribute:: rulename  <key>
                        
                        	Rule name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.rulename = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rulename is None:
                                raise YPYModelError('Key property rulename is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:rulename[Cisco-IOS-XR-infra-correlator-cfg:rulename = ' + str(self.rulename) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rulename is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:rulenames'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rulename is not None:
                            for child_ref in self.rulename:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.Rulenames']['meta_info']


                class AppliedTo(object):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: all
                    
                    	Apply to all of the router
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: contexts
                    
                    	Table of configured contexts to apply
                    	**type**\:   :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts>`
                    
                    .. attribute:: locations
                    
                    	Table of configured locations to apply
                    	**type**\:   :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all = None
                        self.contexts = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts()
                        self.contexts.parent = self
                        self.locations = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations()
                        self.locations.parent = self


                    class Contexts(object):
                        """
                        Table of configured contexts to apply
                        
                        .. attribute:: context
                        
                        	A context
                        	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.context = YList()
                            self.context.parent = self
                            self.context.name = 'context'


                        class Context(object):
                            """
                            A context
                            
                            .. attribute:: context  <key>
                            
                            	Context
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.context = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.context is None:
                                    raise YPYModelError('Key property context is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:context[Cisco-IOS-XR-infra-correlator-cfg:context = ' + str(self.context) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.context is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:contexts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.context is not None:
                                for child_ref in self.context:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts']['meta_info']


                    class Locations(object):
                        """
                        Table of configured locations to apply
                        
                        .. attribute:: location
                        
                        	A location
                        	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.location = YList()
                            self.location.parent = self
                            self.location.name = 'location'


                        class Location(object):
                            """
                            A location
                            
                            .. attribute:: location  <key>
                            
                            	Location
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.location = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.location is None:
                                    raise YPYModelError('Key property location is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:location[Cisco-IOS-XR-infra-correlator-cfg:location = ' + str(self.location) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.location is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:locations'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.location is not None:
                                for child_ref in self.location:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:applied-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all is not None:
                            return True

                        if self.contexts is not None and self.contexts._has_data():
                            return True

                        if self.locations is not None and self.locations._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/Cisco-IOS-XR-infra-correlator-cfg:rule-sets/Cisco-IOS-XR-infra-correlator-cfg:rule-set[Cisco-IOS-XR-infra-correlator-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.applied_to is not None and self.applied_to._has_data():
                        return True

                    if self.rulenames is not None and self.rulenames._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Correlator.RuleSets.RuleSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/Cisco-IOS-XR-infra-correlator-cfg:rule-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rule_set is not None:
                    for child_ref in self.rule_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Correlator.RuleSets']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.buffer_size is not None:
                return True

            if self.rule_sets is not None and self.rule_sets._has_data():
                return True

            if self.rules is not None and self.rules._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Correlator']['meta_info']


    class Suppression(object):
        """
        Configure properties of the syslog/alarm
        suppression
        
        .. attribute:: rules
        
        	Table of configured rules
        	**type**\:   :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules>`
        
        

        """

        _prefix = 'infra-correlator-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rules = Syslog.Suppression.Rules()
            self.rules.parent = self


        class Rules(object):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule = YList()
                self.rule.parent = self
                self.rule.name = 'rule'


            class Rule(object):
                """
                Rule name
                
                .. attribute:: name  <key>
                
                	Rule name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: alarm_causes
                
                	Causes of alarms to be suppressed
                	**type**\:   :py:class:`AlarmCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AlarmCauses>`
                
                .. attribute:: all_alarms
                
                	Suppress all alarms
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: applied_to
                
                	Applied to the Rule
                	**type**\:   :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo>`
                
                

                """

                _prefix = 'infra-correlator-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.alarm_causes = Syslog.Suppression.Rules.Rule.AlarmCauses()
                    self.alarm_causes.parent = self
                    self.all_alarms = None
                    self.applied_to = Syslog.Suppression.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self


                class AppliedTo(object):
                    """
                    Applied to the Rule
                    
                    .. attribute:: all
                    
                    	Apply to all of the router
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: sources
                    
                    	Table of configured sources to apply
                    	**type**\:   :py:class:`Sources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo.Sources>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.all = None
                        self.sources = Syslog.Suppression.Rules.Rule.AppliedTo.Sources()
                        self.sources.parent = self


                    class Sources(object):
                        """
                        Table of configured sources to apply
                        
                        .. attribute:: source
                        
                        	An alarm source
                        	**type**\: list of    :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.source = YList()
                            self.source.parent = self
                            self.source.name = 'source'


                        class Source(object):
                            """
                            An alarm source
                            
                            .. attribute:: source  <key>
                            
                            	Source
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.source = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.source is None:
                                    raise YPYModelError('Key property source is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:source[Cisco-IOS-XR-infra-correlator-cfg:source = ' + str(self.source) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.source is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                                return meta._meta_table['Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:sources'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source is not None:
                                for child_ref in self.source:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Suppression.Rules.Rule.AppliedTo.Sources']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:applied-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all is not None:
                            return True

                        if self.sources is not None and self.sources._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Suppression.Rules.Rule.AppliedTo']['meta_info']


                class AlarmCauses(object):
                    """
                    Causes of alarms to be suppressed
                    
                    .. attribute:: alarm_cause
                    
                    	Category, Group and Code of alarm/syslog to be suppressed
                    	**type**\: list of    :py:class:`AlarmCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.alarm_cause = YList()
                        self.alarm_cause.parent = self
                        self.alarm_cause.name = 'alarm_cause'


                    class AlarmCause(object):
                        """
                        Category, Group and Code of alarm/syslog to
                        be suppressed
                        
                        .. attribute:: category  <key>
                        
                        	Category
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: group  <key>
                        
                        	Group
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: code  <key>
                        
                        	Code
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.category = None
                            self.group = None
                            self.code = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.category is None:
                                raise YPYModelError('Key property category is None')
                            if self.group is None:
                                raise YPYModelError('Key property group is None')
                            if self.code is None:
                                raise YPYModelError('Key property code is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:alarm-cause[Cisco-IOS-XR-infra-correlator-cfg:category = ' + str(self.category) + '][Cisco-IOS-XR-infra-correlator-cfg:group = ' + str(self.group) + '][Cisco-IOS-XR-infra-correlator-cfg:code = ' + str(self.code) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.category is not None:
                                return True

                            if self.group is not None:
                                return True

                            if self.code is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                            return meta._meta_table['Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-cfg:alarm-causes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.alarm_cause is not None:
                            for child_ref in self.alarm_cause:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                        return meta._meta_table['Syslog.Suppression.Rules.Rule.AlarmCauses']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression/Cisco-IOS-XR-infra-correlator-cfg:rules/Cisco-IOS-XR-infra-correlator-cfg:rule[Cisco-IOS-XR-infra-correlator-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.alarm_causes is not None and self.alarm_causes._has_data():
                        return True

                    if self.all_alarms is not None:
                        return True

                    if self.applied_to is not None and self.applied_to._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                    return meta._meta_table['Syslog.Suppression.Rules.Rule']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression/Cisco-IOS-XR-infra-correlator-cfg:rules'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rule is not None:
                    for child_ref in self.rule:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
                return meta._meta_table['Syslog.Suppression.Rules']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.rules is not None and self.rules._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
            return meta._meta_table['Syslog.Suppression']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-cfg:syslog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.alarm_logger is not None and self.alarm_logger._has_data():
            return True

        if self.archive is not None and self.archive._has_data():
            return True

        if self.buffered_logging is not None and self.buffered_logging._has_data():
            return True

        if self.console_logging is not None and self.console_logging._has_data():
            return True

        if self.correlator is not None and self.correlator._has_data():
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

        if self.suppression is not None and self.suppression._has_data():
            return True

        if self.trap_logging is not None and self.trap_logging._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_cfg as meta
        return meta._meta_table['Syslog']['meta_info']


