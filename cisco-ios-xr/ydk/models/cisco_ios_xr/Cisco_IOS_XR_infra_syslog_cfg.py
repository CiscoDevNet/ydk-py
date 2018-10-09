""" Cisco_IOS_XR_infra_syslog_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-syslog package configuration.

This module contains definitions
for the following management objects\:
  syslog\-service\: Syslog Timestamp Services
  syslog\: syslog

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Facility(Enum):
    """
    Facility (Enum Class)

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

    kern = Enum.YLeaf(0, "kern")

    user = Enum.YLeaf(8, "user")

    mail = Enum.YLeaf(16, "mail")

    daemon = Enum.YLeaf(24, "daemon")

    auth = Enum.YLeaf(32, "auth")

    syslog = Enum.YLeaf(40, "syslog")

    lpr = Enum.YLeaf(48, "lpr")

    news = Enum.YLeaf(56, "news")

    uucp = Enum.YLeaf(64, "uucp")

    cron = Enum.YLeaf(72, "cron")

    authpriv = Enum.YLeaf(80, "authpriv")

    ftp = Enum.YLeaf(88, "ftp")

    local0 = Enum.YLeaf(128, "local0")

    local1 = Enum.YLeaf(136, "local1")

    local2 = Enum.YLeaf(144, "local2")

    local3 = Enum.YLeaf(152, "local3")

    local4 = Enum.YLeaf(160, "local4")

    local5 = Enum.YLeaf(168, "local5")

    local6 = Enum.YLeaf(176, "local6")

    local7 = Enum.YLeaf(184, "local7")

    sys9 = Enum.YLeaf(192, "sys9")

    sys10 = Enum.YLeaf(200, "sys10")

    sys11 = Enum.YLeaf(208, "sys11")

    sys12 = Enum.YLeaf(216, "sys12")

    sys13 = Enum.YLeaf(224, "sys13")

    sys14 = Enum.YLeaf(232, "sys14")


class LogCollectFrequency(Enum):
    """
    LogCollectFrequency (Enum Class)

    Log collect frequency

    .. data:: weekly = 1

    	Collect log in files on a weekly basis

    .. data:: daily = 2

    	Collect log in files on a daily basis

    """

    weekly = Enum.YLeaf(1, "weekly")

    daily = Enum.YLeaf(2, "daily")


class LogMessageSeverity(Enum):
    """
    LogMessageSeverity (Enum Class)

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

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    informational = Enum.YLeaf(6, "informational")

    debug = Enum.YLeaf(7, "debug")


class LogSeverity(Enum):
    """
    LogSeverity (Enum Class)

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

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    informational = Enum.YLeaf(6, "informational")

    debug = Enum.YLeaf(7, "debug")


class LoggingDscp(Enum):
    """
    LoggingDscp (Enum Class)

    Logging dscp

    .. data:: dscp = 1

    	Logging TOS type DSCP

    """

    dscp = Enum.YLeaf(1, "dscp")


class LoggingDscpValue(Enum):
    """
    LoggingDscpValue (Enum Class)

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

    default = Enum.YLeaf(0, "default")

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    ef = Enum.YLeaf(46, "ef")

    cs1 = Enum.YLeaf(8, "cs1")

    cs2 = Enum.YLeaf(16, "cs2")

    cs3 = Enum.YLeaf(24, "cs3")

    cs4 = Enum.YLeaf(32, "cs4")

    cs5 = Enum.YLeaf(40, "cs5")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")


class LoggingLevels(Enum):
    """
    LoggingLevels (Enum Class)

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

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    info = Enum.YLeaf(6, "info")

    debug = Enum.YLeaf(7, "debug")

    disable = Enum.YLeaf(15, "disable")


class LoggingPrecedence(Enum):
    """
    LoggingPrecedence (Enum Class)

    Logging precedence

    .. data:: precedence = 0

    	Logging TOS type precedence

    """

    precedence = Enum.YLeaf(0, "precedence")


class LoggingPrecedenceValue(Enum):
    """
    LoggingPrecedenceValue (Enum Class)

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

    routine = Enum.YLeaf(0, "routine")

    priority = Enum.YLeaf(1, "priority")

    immediate = Enum.YLeaf(2, "immediate")

    flash = Enum.YLeaf(3, "flash")

    flash_override = Enum.YLeaf(4, "flash-override")

    critical = Enum.YLeaf(5, "critical")

    internet = Enum.YLeaf(6, "internet")

    network = Enum.YLeaf(7, "network")


class LoggingTos(Enum):
    """
    LoggingTos (Enum Class)

    Logging tos

    .. data:: precedence = 0

    	Logging TOS type precedence

    .. data:: dscp = 1

    	Logging TOS type DSCP

    """

    precedence = Enum.YLeaf(0, "precedence")

    dscp = Enum.YLeaf(1, "dscp")


class TimeInfo(Enum):
    """
    TimeInfo (Enum Class)

    Time info

    .. data:: disable = 0

    	Exclude

    .. data:: enable = 1

    	Include

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class SyslogService(Entity):
    """
    Syslog Timestamp Services
    
    .. attribute:: timestamps
    
    	Timestamp debug/log messages configuration
    	**type**\:  :py:class:`Timestamps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2017-10-31'

    def __init__(self):
        super(SyslogService, self).__init__()
        self._top_entity = None

        self.yang_name = "syslog-service"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("timestamps", ("timestamps", SyslogService.Timestamps))])
        self._leafs = OrderedDict()

        self.timestamps = SyslogService.Timestamps()
        self.timestamps.parent = self
        self._children_name_map["timestamps"] = "timestamps"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SyslogService, [], name, value)


    class Timestamps(Entity):
        """
        Timestamp debug/log messages configuration
        
        .. attribute:: log
        
        	Timestamp log messages
        	**type**\:  :py:class:`Log <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log>`
        
        .. attribute:: debug
        
        	Timestamp debug messages
        	**type**\:  :py:class:`Debug <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug>`
        
        .. attribute:: enable
        
        	Enable timestamp debug/log messages
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(SyslogService.Timestamps, self).__init__()

            self.yang_name = "timestamps"
            self.yang_parent_name = "syslog-service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("log", ("log", SyslogService.Timestamps.Log)), ("debug", ("debug", SyslogService.Timestamps.Debug))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.log = SyslogService.Timestamps.Log()
            self.log.parent = self
            self._children_name_map["log"] = "log"

            self.debug = SyslogService.Timestamps.Debug()
            self.debug.parent = self
            self._children_name_map["debug"] = "debug"
            self._segment_path = lambda: "timestamps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SyslogService.Timestamps, [u'enable'], name, value)


        class Log(Entity):
            """
            Timestamp log messages
            
            .. attribute:: log_datetime
            
            	Timestamp with date and time
            	**type**\:  :py:class:`LogDatetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime>`
            
            .. attribute:: log_uptime
            
            	Timestamp with systime uptime
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_timestamp_disable
            
            	Disable timestamp log messages
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(SyslogService.Timestamps.Log, self).__init__()

                self.yang_name = "log"
                self.yang_parent_name = "timestamps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("log-datetime", ("log_datetime", SyslogService.Timestamps.Log.LogDatetime))])
                self._leafs = OrderedDict([
                    ('log_uptime', (YLeaf(YType.empty, 'log-uptime'), ['Empty'])),
                    ('log_timestamp_disable', (YLeaf(YType.empty, 'log-timestamp-disable'), ['Empty'])),
                ])
                self.log_uptime = None
                self.log_timestamp_disable = None

                self.log_datetime = SyslogService.Timestamps.Log.LogDatetime()
                self.log_datetime.parent = self
                self._children_name_map["log_datetime"] = "log-datetime"
                self._segment_path = lambda: "log"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SyslogService.Timestamps.Log, [u'log_uptime', u'log_timestamp_disable'], name, value)


            class LogDatetime(Entity):
                """
                Timestamp with date and time
                
                .. attribute:: log_datetime_value
                
                	Set timestamp for log message
                	**type**\:  :py:class:`LogDatetimeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2017-10-31'

                def __init__(self):
                    super(SyslogService.Timestamps.Log.LogDatetime, self).__init__()

                    self.yang_name = "log-datetime"
                    self.yang_parent_name = "log"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("log-datetime-value", ("log_datetime_value", SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue))])
                    self._leafs = OrderedDict()

                    self.log_datetime_value = SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue()
                    self.log_datetime_value.parent = self
                    self._children_name_map["log_datetime_value"] = "log-datetime-value"
                    self._segment_path = lambda: "log-datetime"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/log/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SyslogService.Timestamps.Log.LogDatetime, [], name, value)


                class LogDatetimeValue(Entity):
                    """
                    Set timestamp for log message
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: enable
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**units**\: second
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2017-10-31'

                    def __init__(self):
                        super(SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue, self).__init__()

                        self.yang_name = "log-datetime-value"
                        self.yang_parent_name = "log-datetime"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_stamp_value', (YLeaf(YType.enumeration, 'time-stamp-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                            ('msec', (YLeaf(YType.enumeration, 'msec'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                            ('time_zone', (YLeaf(YType.enumeration, 'time-zone'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                            ('year', (YLeaf(YType.enumeration, 'year'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                        ])
                        self.time_stamp_value = None
                        self.msec = None
                        self.time_zone = None
                        self.year = None
                        self._segment_path = lambda: "log-datetime-value"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/log/log-datetime/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue, [u'time_stamp_value', u'msec', u'time_zone', u'year'], name, value)


        class Debug(Entity):
            """
            Timestamp debug messages
            
            .. attribute:: debug_datetime
            
            	Timestamp with date and time
            	**type**\:  :py:class:`DebugDatetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime>`
            
            .. attribute:: debug_timestamp_disable
            
            	Disable timestamp debug messages
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: debug_uptime
            
            	Timestamp with systime uptime
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(SyslogService.Timestamps.Debug, self).__init__()

                self.yang_name = "debug"
                self.yang_parent_name = "timestamps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("debug-datetime", ("debug_datetime", SyslogService.Timestamps.Debug.DebugDatetime))])
                self._leafs = OrderedDict([
                    ('debug_timestamp_disable', (YLeaf(YType.empty, 'debug-timestamp-disable'), ['Empty'])),
                    ('debug_uptime', (YLeaf(YType.empty, 'debug-uptime'), ['Empty'])),
                ])
                self.debug_timestamp_disable = None
                self.debug_uptime = None

                self.debug_datetime = SyslogService.Timestamps.Debug.DebugDatetime()
                self.debug_datetime.parent = self
                self._children_name_map["debug_datetime"] = "debug-datetime"
                self._segment_path = lambda: "debug"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SyslogService.Timestamps.Debug, [u'debug_timestamp_disable', u'debug_uptime'], name, value)


            class DebugDatetime(Entity):
                """
                Timestamp with date and time
                
                .. attribute:: datetime_value
                
                	Set time format for debug msg
                	**type**\:  :py:class:`DatetimeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2017-10-31'

                def __init__(self):
                    super(SyslogService.Timestamps.Debug.DebugDatetime, self).__init__()

                    self.yang_name = "debug-datetime"
                    self.yang_parent_name = "debug"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("datetime-value", ("datetime_value", SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue))])
                    self._leafs = OrderedDict()

                    self.datetime_value = SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue()
                    self.datetime_value.parent = self
                    self._children_name_map["datetime_value"] = "datetime-value"
                    self._segment_path = lambda: "debug-datetime"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/debug/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SyslogService.Timestamps.Debug.DebugDatetime, [], name, value)


                class DatetimeValue(Entity):
                    """
                    Set time format for debug msg
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: enable
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**units**\: second
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\:  :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2017-10-31'

                    def __init__(self):
                        super(SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue, self).__init__()

                        self.yang_name = "datetime-value"
                        self.yang_parent_name = "debug-datetime"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_stamp_value', (YLeaf(YType.enumeration, 'time-stamp-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                            ('msec', (YLeaf(YType.enumeration, 'msec'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                            ('time_zone', (YLeaf(YType.enumeration, 'time-zone'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                            ('year', (YLeaf(YType.enumeration, 'year'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'TimeInfo', '')])),
                        ])
                        self.time_stamp_value = None
                        self.msec = None
                        self.time_zone = None
                        self.year = None
                        self._segment_path = lambda: "datetime-value"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/debug/debug-datetime/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue, [u'time_stamp_value', u'msec', u'time_zone', u'year'], name, value)

    def clone_ptr(self):
        self._top_entity = SyslogService()
        return self._top_entity

class Syslog(Entity):
    """
    syslog
    
    .. attribute:: monitor_logging
    
    	Set monitor logging
    	**type**\:  :py:class:`MonitorLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging>`
    
    .. attribute:: history_logging
    
    	Set history logging
    	**type**\:  :py:class:`HistoryLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HistoryLogging>`
    
    .. attribute:: logging_facilities
    
    	Modify message logging facilities
    	**type**\:  :py:class:`LoggingFacilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.LoggingFacilities>`
    
    .. attribute:: trap_logging
    
    	Set trap logging
    	**type**\:  :py:class:`TrapLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.TrapLogging>`
    
    .. attribute:: buffered_logging
    
    	Set buffered logging parameters
    	**type**\:  :py:class:`BufferedLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.BufferedLogging>`
    
    .. attribute:: host_server
    
    	Configure logging host
    	**type**\:  :py:class:`HostServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer>`
    
    .. attribute:: console_logging
    
    	Set console logging
    	**type**\:  :py:class:`ConsoleLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging>`
    
    .. attribute:: files
    
    	Configure logging file destination
    	**type**\:  :py:class:`Files <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files>`
    
    .. attribute:: ipv4
    
    	Syslog TOS bit for outgoing messages
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4>`
    
    .. attribute:: archive
    
    	Archive attributes configuration
    	**type**\:  :py:class:`Archive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Archive>`
    
    .. attribute:: ipv6
    
    	Syslog traffic class bit for outgoing messages
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6>`
    
    .. attribute:: source_interface_table
    
    	Configure source interface
    	**type**\:  :py:class:`SourceInterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable>`
    
    .. attribute:: host_name_prefix
    
    	Hostname prefix to add on msgs to servers
    	**type**\: str
    
    .. attribute:: local_log_file_size
    
    	Set size of the local log file
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**default value**\: 32768
    
    .. attribute:: enable_console_logging
    
    	Enabled or disabled
    	**type**\: bool
    
    .. attribute:: suppress_duplicates
    
    	Suppress consecutive duplicate messages
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: correlator
    
    	Configure properties of the event correlator
    	**type**\:  :py:class:`Correlator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator>`
    
    .. attribute:: suppression
    
    	Configure properties of the syslog/alarm suppression
    	**type**\:  :py:class:`Suppression <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression>`
    
    .. attribute:: alarm_logger
    
    	Alarm Logger Properties
    	**type**\:  :py:class:`AlarmLogger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2017-10-31'

    def __init__(self):
        super(Syslog, self).__init__()
        self._top_entity = None

        self.yang_name = "syslog"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("monitor-logging", ("monitor_logging", Syslog.MonitorLogging)), ("history-logging", ("history_logging", Syslog.HistoryLogging)), ("logging-facilities", ("logging_facilities", Syslog.LoggingFacilities)), ("trap-logging", ("trap_logging", Syslog.TrapLogging)), ("buffered-logging", ("buffered_logging", Syslog.BufferedLogging)), ("host-server", ("host_server", Syslog.HostServer)), ("console-logging", ("console_logging", Syslog.ConsoleLogging)), ("files", ("files", Syslog.Files)), ("ipv4", ("ipv4", Syslog.Ipv4)), ("archive", ("archive", Syslog.Archive)), ("ipv6", ("ipv6", Syslog.Ipv6)), ("source-interface-table", ("source_interface_table", Syslog.SourceInterfaceTable)), ("Cisco-IOS-XR-infra-correlator-cfg:correlator", ("correlator", Syslog.Correlator)), ("Cisco-IOS-XR-infra-correlator-cfg:suppression", ("suppression", Syslog.Suppression)), ("Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger", ("alarm_logger", Syslog.AlarmLogger))])
        self._leafs = OrderedDict([
            ('host_name_prefix', (YLeaf(YType.str, 'host-name-prefix'), ['str'])),
            ('local_log_file_size', (YLeaf(YType.uint32, 'local-log-file-size'), ['int'])),
            ('enable_console_logging', (YLeaf(YType.boolean, 'enable-console-logging'), ['bool'])),
            ('suppress_duplicates', (YLeaf(YType.empty, 'suppress-duplicates'), ['Empty'])),
        ])
        self.host_name_prefix = None
        self.local_log_file_size = None
        self.enable_console_logging = None
        self.suppress_duplicates = None

        self.monitor_logging = Syslog.MonitorLogging()
        self.monitor_logging.parent = self
        self._children_name_map["monitor_logging"] = "monitor-logging"

        self.history_logging = Syslog.HistoryLogging()
        self.history_logging.parent = self
        self._children_name_map["history_logging"] = "history-logging"

        self.logging_facilities = Syslog.LoggingFacilities()
        self.logging_facilities.parent = self
        self._children_name_map["logging_facilities"] = "logging-facilities"

        self.trap_logging = Syslog.TrapLogging()
        self.trap_logging.parent = self
        self._children_name_map["trap_logging"] = "trap-logging"

        self.buffered_logging = Syslog.BufferedLogging()
        self.buffered_logging.parent = self
        self._children_name_map["buffered_logging"] = "buffered-logging"

        self.host_server = Syslog.HostServer()
        self.host_server.parent = self
        self._children_name_map["host_server"] = "host-server"

        self.console_logging = Syslog.ConsoleLogging()
        self.console_logging.parent = self
        self._children_name_map["console_logging"] = "console-logging"

        self.files = Syslog.Files()
        self.files.parent = self
        self._children_name_map["files"] = "files"

        self.ipv4 = Syslog.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"

        self.archive = Syslog.Archive()
        self.archive.parent = self
        self._children_name_map["archive"] = "archive"

        self.ipv6 = Syslog.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"

        self.source_interface_table = Syslog.SourceInterfaceTable()
        self.source_interface_table.parent = self
        self._children_name_map["source_interface_table"] = "source-interface-table"

        self.correlator = Syslog.Correlator()
        self.correlator.parent = self
        self._children_name_map["correlator"] = "Cisco-IOS-XR-infra-correlator-cfg:correlator"

        self.suppression = Syslog.Suppression()
        self.suppression.parent = self
        self._children_name_map["suppression"] = "Cisco-IOS-XR-infra-correlator-cfg:suppression"

        self.alarm_logger = Syslog.AlarmLogger()
        self.alarm_logger.parent = self
        self._children_name_map["alarm_logger"] = "Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Syslog, [u'host_name_prefix', u'local_log_file_size', u'enable_console_logging', u'suppress_duplicates'], name, value)


    class MonitorLogging(Entity):
        """
        Set monitor logging
        
        .. attribute:: monitor_discriminator
        
        	Set monitor logging discriminators
        	**type**\:  :py:class:`MonitorDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging.MonitorDiscriminator>`
        
        .. attribute:: logging_level
        
        	Monitor Logging Level
        	**type**\:  :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: debug
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.MonitorLogging, self).__init__()

            self.yang_name = "monitor-logging"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("monitor-discriminator", ("monitor_discriminator", Syslog.MonitorLogging.MonitorDiscriminator))])
            self._leafs = OrderedDict([
                ('logging_level', (YLeaf(YType.enumeration, 'logging-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevels', '')])),
            ])
            self.logging_level = None

            self.monitor_discriminator = Syslog.MonitorLogging.MonitorDiscriminator()
            self.monitor_discriminator.parent = self
            self._children_name_map["monitor_discriminator"] = "monitor-discriminator"
            self._segment_path = lambda: "monitor-logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.MonitorLogging, [u'logging_level'], name, value)


        class MonitorDiscriminator(Entity):
            """
            Set monitor logging discriminators
            
            .. attribute:: match2
            
            	Set monitor logging match2 discriminator
            	**type**\: str
            
            .. attribute:: nomatch1
            
            	Set monitor logging no\-match1 discriminator
            	**type**\: str
            
            .. attribute:: match1
            
            	Set monitor logging match1 discriminator
            	**type**\: str
            
            .. attribute:: nomatch3
            
            	Set monitor logging no\-match3 discriminator
            	**type**\: str
            
            .. attribute:: match3
            
            	Set monitor logging match3 discriminator
            	**type**\: str
            
            .. attribute:: nomatch2
            
            	Set monitor logging no\-match2 discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.MonitorLogging.MonitorDiscriminator, self).__init__()

                self.yang_name = "monitor-discriminator"
                self.yang_parent_name = "monitor-logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('match2', (YLeaf(YType.str, 'match2'), ['str'])),
                    ('nomatch1', (YLeaf(YType.str, 'nomatch1'), ['str'])),
                    ('match1', (YLeaf(YType.str, 'match1'), ['str'])),
                    ('nomatch3', (YLeaf(YType.str, 'nomatch3'), ['str'])),
                    ('match3', (YLeaf(YType.str, 'match3'), ['str'])),
                    ('nomatch2', (YLeaf(YType.str, 'nomatch2'), ['str'])),
                ])
                self.match2 = None
                self.nomatch1 = None
                self.match1 = None
                self.nomatch3 = None
                self.match3 = None
                self.nomatch2 = None
                self._segment_path = lambda: "monitor-discriminator"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/monitor-logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.MonitorLogging.MonitorDiscriminator, [u'match2', u'nomatch1', u'match1', u'nomatch3', u'match3', u'nomatch2'], name, value)


    class HistoryLogging(Entity):
        """
        Set history logging
        
        .. attribute:: history_size
        
        	Logging history size
        	**type**\: int
        
        	**range:** 1..500
        
        	**default value**\: 1
        
        .. attribute:: logging_level
        
        	History logging level
        	**type**\:  :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: warning
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.HistoryLogging, self).__init__()

            self.yang_name = "history-logging"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('history_size', (YLeaf(YType.uint32, 'history-size'), ['int'])),
                ('logging_level', (YLeaf(YType.enumeration, 'logging-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevels', '')])),
            ])
            self.history_size = None
            self.logging_level = None
            self._segment_path = lambda: "history-logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.HistoryLogging, [u'history_size', u'logging_level'], name, value)


    class LoggingFacilities(Entity):
        """
        Modify message logging facilities
        
        .. attribute:: facility_level
        
        	Facility from which logging is done
        	**type**\:  :py:class:`Facility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Facility>`
        
        	**default value**\: local7
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.LoggingFacilities, self).__init__()

            self.yang_name = "logging-facilities"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('facility_level', (YLeaf(YType.enumeration, 'facility-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'Facility', '')])),
            ])
            self.facility_level = None
            self._segment_path = lambda: "logging-facilities"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.LoggingFacilities, [u'facility_level'], name, value)


    class TrapLogging(Entity):
        """
        Set trap logging
        
        .. attribute:: logging_level
        
        	Trap logging level
        	**type**\:  :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: info
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.TrapLogging, self).__init__()

            self.yang_name = "trap-logging"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('logging_level', (YLeaf(YType.enumeration, 'logging-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevels', '')])),
            ])
            self.logging_level = None
            self._segment_path = lambda: "trap-logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.TrapLogging, [u'logging_level'], name, value)


    class BufferedLogging(Entity):
        """
        Set buffered logging parameters
        
        .. attribute:: buffered_discriminator
        
        	Set buffered logging discriminators
        	**type**\:  :py:class:`BufferedDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.BufferedLogging.BufferedDiscriminator>`
        
        .. attribute:: logging_level
        
        	Logging level for Buffered logging
        	**type**\:  :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: debug
        
        .. attribute:: buffer_size
        
        	Logging buffered size
        	**type**\: int
        
        	**range:** 4096..4294967295
        
        	**default value**\: 2097152
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.BufferedLogging, self).__init__()

            self.yang_name = "buffered-logging"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("buffered-discriminator", ("buffered_discriminator", Syslog.BufferedLogging.BufferedDiscriminator))])
            self._leafs = OrderedDict([
                ('logging_level', (YLeaf(YType.enumeration, 'logging-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevels', '')])),
                ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
            ])
            self.logging_level = None
            self.buffer_size = None

            self.buffered_discriminator = Syslog.BufferedLogging.BufferedDiscriminator()
            self.buffered_discriminator.parent = self
            self._children_name_map["buffered_discriminator"] = "buffered-discriminator"
            self._segment_path = lambda: "buffered-logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.BufferedLogging, [u'logging_level', u'buffer_size'], name, value)


        class BufferedDiscriminator(Entity):
            """
            Set buffered logging discriminators
            
            .. attribute:: match2
            
            	Set buffered logging match2 discriminator
            	**type**\: str
            
            .. attribute:: nomatch1
            
            	Set buffered logging no\-match1 discriminator
            	**type**\: str
            
            .. attribute:: match1
            
            	Set buffered logging match1 discriminator
            	**type**\: str
            
            .. attribute:: nomatch3
            
            	Set buffered logging no\-match3 discriminator
            	**type**\: str
            
            .. attribute:: match3
            
            	Set buffered logging match3 discriminator
            	**type**\: str
            
            .. attribute:: nomatch2
            
            	Set buffered logging no\-match2 discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.BufferedLogging.BufferedDiscriminator, self).__init__()

                self.yang_name = "buffered-discriminator"
                self.yang_parent_name = "buffered-logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('match2', (YLeaf(YType.str, 'match2'), ['str'])),
                    ('nomatch1', (YLeaf(YType.str, 'nomatch1'), ['str'])),
                    ('match1', (YLeaf(YType.str, 'match1'), ['str'])),
                    ('nomatch3', (YLeaf(YType.str, 'nomatch3'), ['str'])),
                    ('match3', (YLeaf(YType.str, 'match3'), ['str'])),
                    ('nomatch2', (YLeaf(YType.str, 'nomatch2'), ['str'])),
                ])
                self.match2 = None
                self.nomatch1 = None
                self.match1 = None
                self.nomatch3 = None
                self.match3 = None
                self.nomatch2 = None
                self._segment_path = lambda: "buffered-discriminator"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/buffered-logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.BufferedLogging.BufferedDiscriminator, [u'match2', u'nomatch1', u'match1', u'nomatch3', u'match3', u'nomatch2'], name, value)


    class HostServer(Entity):
        """
        Configure logging host
        
        .. attribute:: vrfs
        
        	VRF table
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.HostServer, self).__init__()

            self.yang_name = "host-server"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrfs", ("vrfs", Syslog.HostServer.Vrfs))])
            self._leafs = OrderedDict()

            self.vrfs = Syslog.HostServer.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._segment_path = lambda: "host-server"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.HostServer, [], name, value)


        class Vrfs(Entity):
            """
            VRF table
            
            .. attribute:: vrf
            
            	VRF specific data
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.HostServer.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "host-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", Syslog.HostServer.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/host-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.HostServer.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                VRF specific data
                
                .. attribute:: vrf_name  (key)
                
                	Name of the VRF instance
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: ipv6s
                
                	List of the IPv6 logging host
                	**type**\:  :py:class:`Ipv6s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6s>`
                
                .. attribute:: hosts
                
                	List of the logging host
                	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts>`
                
                .. attribute:: ipv4s
                
                	List of the IPv4 logging host
                	**type**\:  :py:class:`Ipv4s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4s>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2017-10-31'

                def __init__(self):
                    super(Syslog.HostServer.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([("ipv6s", ("ipv6s", Syslog.HostServer.Vrfs.Vrf.Ipv6s)), ("hosts", ("hosts", Syslog.HostServer.Vrfs.Vrf.Hosts)), ("ipv4s", ("ipv4s", Syslog.HostServer.Vrfs.Vrf.Ipv4s))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ])
                    self.vrf_name = None

                    self.ipv6s = Syslog.HostServer.Vrfs.Vrf.Ipv6s()
                    self.ipv6s.parent = self
                    self._children_name_map["ipv6s"] = "ipv6s"

                    self.hosts = Syslog.HostServer.Vrfs.Vrf.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"

                    self.ipv4s = Syslog.HostServer.Vrfs.Vrf.Ipv4s()
                    self.ipv4s.parent = self
                    self._children_name_map["ipv4s"] = "ipv4s"
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/host-server/vrfs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.HostServer.Vrfs.Vrf, [u'vrf_name'], name, value)


                class Ipv6s(Entity):
                    """
                    List of the IPv6 logging host
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address of the logging host
                    	**type**\: list of  		 :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2017-10-31'

                    def __init__(self):
                        super(Syslog.HostServer.Vrfs.Vrf.Ipv6s, self).__init__()

                        self.yang_name = "ipv6s"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv6", ("ipv6", Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6))])
                        self._leafs = OrderedDict()

                        self.ipv6 = YList(self)
                        self._segment_path = lambda: "ipv6s"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv6s, [], name, value)


                    class Ipv6(Entity):
                        """
                        IPv6 address of the logging host
                        
                        .. attribute:: address  (key)
                        
                        	IPv6 address of the logging host
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\:  :py:class:`Ipv6SeverityPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityPort>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: ipv6_severity_levels
                        
                        	Severity container of the logging host
                        	**type**\:  :py:class:`Ipv6SeverityLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels>`
                        
                        	**status**\: obsolete
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2017-10-31'

                        def __init__(self):
                            super(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "ipv6s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("ipv6-severity-port", ("ipv6_severity_port", Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityPort)), ("ipv6-severity-levels", ("ipv6_severity_levels", Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ])
                            self.address = None

                            self.ipv6_severity_port = None
                            self._children_name_map["ipv6_severity_port"] = "ipv6-severity-port"

                            self.ipv6_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels()
                            self.ipv6_severity_levels.parent = self
                            self._children_name_map["ipv6_severity_levels"] = "ipv6-severity-levels"
                            self._segment_path = lambda: "ipv6" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6, [u'address'], name, value)


                        class Ipv6SeverityPort(Entity):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 6
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 514
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2017-10-31'

                            def __init__(self):
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityPort, self).__init__()

                                self.yang_name = "ipv6-severity-port"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('severity', (YLeaf(YType.uint32, 'severity'), ['int'])),
                                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                ])
                                self.severity = None
                                self.port = None
                                self._segment_path = lambda: "ipv6-severity-port"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityPort, [u'severity', u'port'], name, value)


                        class Ipv6SeverityLevels(Entity):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: ipv6_severity_level
                            
                            	Severity for the logging host
                            	**type**\: list of  		 :py:class:`Ipv6SeverityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel>`
                            
                            	**status**\: obsolete
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2017-10-31'

                            def __init__(self):
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels, self).__init__()

                                self.yang_name = "ipv6-severity-levels"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv6-severity-level", ("ipv6_severity_level", Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel))])
                                self._leafs = OrderedDict()

                                self.ipv6_severity_level = YList(self)
                                self._segment_path = lambda: "ipv6-severity-levels"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels, [], name, value)


                            class Ipv6SeverityLevel(Entity):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  (key)
                                
                                	Severity for the logging host
                                	**type**\:  :py:class:`LogSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverity>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2017-10-31'

                                def __init__(self):
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel, self).__init__()

                                    self.yang_name = "ipv6-severity-level"
                                    self.yang_parent_name = "ipv6-severity-levels"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['severity']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverity', '')])),
                                    ])
                                    self.severity = None
                                    self._segment_path = lambda: "ipv6-severity-level" + "[severity='" + str(self.severity) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv6s.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel, [u'severity'], name, value)


                class Hosts(Entity):
                    """
                    List of the logging host
                    
                    .. attribute:: host
                    
                    	Name of the logging host
                    	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2017-10-31'

                    def __init__(self):
                        super(Syslog.HostServer.Vrfs.Vrf.Hosts, self).__init__()

                        self.yang_name = "hosts"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("host", ("host", Syslog.HostServer.Vrfs.Vrf.Hosts.Host))])
                        self._leafs = OrderedDict()

                        self.host = YList(self)
                        self._segment_path = lambda: "hosts"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Hosts, [], name, value)


                    class Host(Entity):
                        """
                        Name of the logging host
                        
                        .. attribute:: host_name  (key)
                        
                        	Name of the logging host
                        	**type**\: str
                        
                        .. attribute:: host_name_severities
                        
                        	Severity container of the logging host
                        	**type**\:  :py:class:`HostNameSeverities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities>`
                        
                        	**status**\: obsolete
                        
                        .. attribute:: host_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\:  :py:class:`HostSeverityPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2017-10-31'

                        def __init__(self):
                            super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host, self).__init__()

                            self.yang_name = "host"
                            self.yang_parent_name = "hosts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['host_name']
                            self._child_classes = OrderedDict([("host-name-severities", ("host_name_severities", Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities)), ("host-severity-port", ("host_severity_port", Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort))])
                            self._leafs = OrderedDict([
                                ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                            ])
                            self.host_name = None

                            self.host_name_severities = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities()
                            self.host_name_severities.parent = self
                            self._children_name_map["host_name_severities"] = "host-name-severities"

                            self.host_severity_port = None
                            self._children_name_map["host_severity_port"] = "host-severity-port"
                            self._segment_path = lambda: "host" + "[host-name='" + str(self.host_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Hosts.Host, [u'host_name'], name, value)


                        class HostNameSeverities(Entity):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: host_name_severity
                            
                            	Severity for the logging host
                            	**type**\: list of  		 :py:class:`HostNameSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity>`
                            
                            	**status**\: obsolete
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2017-10-31'

                            def __init__(self):
                                super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities, self).__init__()

                                self.yang_name = "host-name-severities"
                                self.yang_parent_name = "host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("host-name-severity", ("host_name_severity", Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity))])
                                self._leafs = OrderedDict()

                                self.host_name_severity = YList(self)
                                self._segment_path = lambda: "host-name-severities"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities, [], name, value)


                            class HostNameSeverity(Entity):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  (key)
                                
                                	Severity for the logging host
                                	**type**\:  :py:class:`LogSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverity>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2017-10-31'

                                def __init__(self):
                                    super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity, self).__init__()

                                    self.yang_name = "host-name-severity"
                                    self.yang_parent_name = "host-name-severities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['severity']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverity', '')])),
                                    ])
                                    self.severity = None
                                    self._segment_path = lambda: "host-name-severity" + "[severity='" + str(self.severity) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity, [u'severity'], name, value)


                        class HostSeverityPort(Entity):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 6
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 514
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2017-10-31'

                            def __init__(self):
                                super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort, self).__init__()

                                self.yang_name = "host-severity-port"
                                self.yang_parent_name = "host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('severity', (YLeaf(YType.uint32, 'severity'), ['int'])),
                                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                ])
                                self.severity = None
                                self.port = None
                                self._segment_path = lambda: "host-severity-port"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort, [u'severity', u'port'], name, value)


                class Ipv4s(Entity):
                    """
                    List of the IPv4 logging host
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address of the logging host
                    	**type**\: list of  		 :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2017-10-31'

                    def __init__(self):
                        super(Syslog.HostServer.Vrfs.Vrf.Ipv4s, self).__init__()

                        self.yang_name = "ipv4s"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4", ("ipv4", Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4))])
                        self._leafs = OrderedDict()

                        self.ipv4 = YList(self)
                        self._segment_path = lambda: "ipv4s"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv4s, [], name, value)


                    class Ipv4(Entity):
                        """
                        IPv4 address of the logging host
                        
                        .. attribute:: address  (key)
                        
                        	IPv4 address of the logging host
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv4_severity_levels
                        
                        	Severity container of the logging host
                        	**type**\:  :py:class:`Ipv4SeverityLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels>`
                        
                        	**status**\: obsolete
                        
                        .. attribute:: ipv4_severity_port
                        
                        	Severity/Port for the logging host
                        	**type**\:  :py:class:`Ipv4SeverityPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityPort>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2017-10-31'

                        def __init__(self):
                            super(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "ipv4s"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("ipv4-severity-levels", ("ipv4_severity_levels", Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels)), ("ipv4-severity-port", ("ipv4_severity_port", Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityPort))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ])
                            self.address = None

                            self.ipv4_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels()
                            self.ipv4_severity_levels.parent = self
                            self._children_name_map["ipv4_severity_levels"] = "ipv4-severity-levels"

                            self.ipv4_severity_port = None
                            self._children_name_map["ipv4_severity_port"] = "ipv4-severity-port"
                            self._segment_path = lambda: "ipv4" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4, [u'address'], name, value)


                        class Ipv4SeverityLevels(Entity):
                            """
                            Severity container of the logging host
                            
                            .. attribute:: ipv4_severity_level
                            
                            	Severity for the logging host
                            	**type**\: list of  		 :py:class:`Ipv4SeverityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel>`
                            
                            	**status**\: obsolete
                            
                            

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2017-10-31'

                            def __init__(self):
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels, self).__init__()

                                self.yang_name = "ipv4-severity-levels"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-severity-level", ("ipv4_severity_level", Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel))])
                                self._leafs = OrderedDict()

                                self.ipv4_severity_level = YList(self)
                                self._segment_path = lambda: "ipv4-severity-levels"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels, [], name, value)


                            class Ipv4SeverityLevel(Entity):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  (key)
                                
                                	Severity for the logging host
                                	**type**\:  :py:class:`LogSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverity>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2017-10-31'

                                def __init__(self):
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel, self).__init__()

                                    self.yang_name = "ipv4-severity-level"
                                    self.yang_parent_name = "ipv4-severity-levels"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['severity']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogSeverity', '')])),
                                    ])
                                    self.severity = None
                                    self._segment_path = lambda: "ipv4-severity-level" + "[severity='" + str(self.severity) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel, [u'severity'], name, value)


                        class Ipv4SeverityPort(Entity):
                            """
                            Severity/Port for the logging host
                            
                            .. attribute:: severity
                            
                            	Severity for the logging host
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 6
                            
                            .. attribute:: port
                            
                            	Port for the logging host
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 514
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-syslog-cfg'
                            _revision = '2017-10-31'

                            def __init__(self):
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityPort, self).__init__()

                                self.yang_name = "ipv4-severity-port"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('severity', (YLeaf(YType.uint32, 'severity'), ['int'])),
                                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                                ])
                                self.severity = None
                                self.port = None
                                self._segment_path = lambda: "ipv4-severity-port"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.HostServer.Vrfs.Vrf.Ipv4s.Ipv4.Ipv4SeverityPort, [u'severity', u'port'], name, value)


    class ConsoleLogging(Entity):
        """
        Set console logging
        
        .. attribute:: console_discriminator
        
        	Set console logging discriminators
        	**type**\:  :py:class:`ConsoleDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging.ConsoleDiscriminator>`
        
        .. attribute:: logging_level
        
        	Console logging level
        	**type**\:  :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: warning
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.ConsoleLogging, self).__init__()

            self.yang_name = "console-logging"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("console-discriminator", ("console_discriminator", Syslog.ConsoleLogging.ConsoleDiscriminator))])
            self._leafs = OrderedDict([
                ('logging_level', (YLeaf(YType.enumeration, 'logging-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingLevels', '')])),
            ])
            self.logging_level = None

            self.console_discriminator = Syslog.ConsoleLogging.ConsoleDiscriminator()
            self.console_discriminator.parent = self
            self._children_name_map["console_discriminator"] = "console-discriminator"
            self._segment_path = lambda: "console-logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.ConsoleLogging, [u'logging_level'], name, value)


        class ConsoleDiscriminator(Entity):
            """
            Set console logging discriminators
            
            .. attribute:: match2
            
            	Set console logging match2 discriminator
            	**type**\: str
            
            .. attribute:: nomatch1
            
            	Set console logging no\-match1 discriminator
            	**type**\: str
            
            .. attribute:: match1
            
            	Set console logging match1 discriminator
            	**type**\: str
            
            .. attribute:: nomatch3
            
            	Set console logging no\-match3 discriminator
            	**type**\: str
            
            .. attribute:: match3
            
            	Set console logging match3 discriminator
            	**type**\: str
            
            .. attribute:: nomatch2
            
            	Set console logging no\-match2 discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.ConsoleLogging.ConsoleDiscriminator, self).__init__()

                self.yang_name = "console-discriminator"
                self.yang_parent_name = "console-logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('match2', (YLeaf(YType.str, 'match2'), ['str'])),
                    ('nomatch1', (YLeaf(YType.str, 'nomatch1'), ['str'])),
                    ('match1', (YLeaf(YType.str, 'match1'), ['str'])),
                    ('nomatch3', (YLeaf(YType.str, 'nomatch3'), ['str'])),
                    ('match3', (YLeaf(YType.str, 'match3'), ['str'])),
                    ('nomatch2', (YLeaf(YType.str, 'nomatch2'), ['str'])),
                ])
                self.match2 = None
                self.nomatch1 = None
                self.match1 = None
                self.nomatch3 = None
                self.match3 = None
                self.nomatch2 = None
                self._segment_path = lambda: "console-discriminator"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/console-logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.ConsoleLogging.ConsoleDiscriminator, [u'match2', u'nomatch1', u'match1', u'nomatch3', u'match3', u'nomatch2'], name, value)


    class Files(Entity):
        """
        Configure logging file destination
        
        .. attribute:: file
        
        	Specify File Name
        	**type**\: list of  		 :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.Files, self).__init__()

            self.yang_name = "files"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("file", ("file", Syslog.Files.File))])
            self._leafs = OrderedDict()

            self.file = YList(self)
            self._segment_path = lambda: "files"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Files, [], name, value)


        class File(Entity):
            """
            Specify File Name
            
            .. attribute:: file_name  (key)
            
            	Name of the file
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: file_specification
            
            	Specifications of the logging file destination
            	**type**\:  :py:class:`FileSpecification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileSpecification>`
            
            .. attribute:: file_log_discriminator
            
            	Set File logging discriminators
            	**type**\:  :py:class:`FileLogDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File.FileLogDiscriminator>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Files.File, self).__init__()

                self.yang_name = "file"
                self.yang_parent_name = "files"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['file_name']
                self._child_classes = OrderedDict([("file-specification", ("file_specification", Syslog.Files.File.FileSpecification)), ("file-log-discriminator", ("file_log_discriminator", Syslog.Files.File.FileLogDiscriminator))])
                self._leafs = OrderedDict([
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                ])
                self.file_name = None

                self.file_specification = Syslog.Files.File.FileSpecification()
                self.file_specification.parent = self
                self._children_name_map["file_specification"] = "file-specification"

                self.file_log_discriminator = Syslog.Files.File.FileLogDiscriminator()
                self.file_log_discriminator.parent = self
                self._children_name_map["file_log_discriminator"] = "file-log-discriminator"
                self._segment_path = lambda: "file" + "[file-name='" + str(self.file_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/files/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Files.File, [u'file_name'], name, value)


            class FileSpecification(Entity):
                """
                Specifications of the logging file destination
                
                .. attribute:: path
                
                	File path
                	**type**\: str
                
                .. attribute:: max_file_size
                
                	Maximum file size (in KB)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**default value**\: 1024
                
                .. attribute:: severity
                
                	Severity of messages
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**default value**\: 6
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2017-10-31'

                def __init__(self):
                    super(Syslog.Files.File.FileSpecification, self).__init__()

                    self.yang_name = "file-specification"
                    self.yang_parent_name = "file"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('path', (YLeaf(YType.str, 'path'), ['str'])),
                        ('max_file_size', (YLeaf(YType.uint32, 'max-file-size'), ['int'])),
                        ('severity', (YLeaf(YType.uint32, 'severity'), ['int'])),
                    ])
                    self.path = None
                    self.max_file_size = None
                    self.severity = None
                    self._segment_path = lambda: "file-specification"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.Files.File.FileSpecification, [u'path', u'max_file_size', u'severity'], name, value)


            class FileLogDiscriminator(Entity):
                """
                Set File logging discriminators
                
                .. attribute:: nomatch2
                
                	Set file logging no match discriminator 2
                	**type**\: str
                
                .. attribute:: match3
                
                	Set file logging match discriminator 3
                	**type**\: str
                
                .. attribute:: nomatch3
                
                	Set file logging no match discriminator 3
                	**type**\: str
                
                .. attribute:: match1
                
                	Set file logging match discriminator 1
                	**type**\: str
                
                .. attribute:: nomatch1
                
                	Set file logging no match discriminator 1
                	**type**\: str
                
                .. attribute:: match2
                
                	Set file logging match discriminator 2
                	**type**\: str
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2017-10-31'

                def __init__(self):
                    super(Syslog.Files.File.FileLogDiscriminator, self).__init__()

                    self.yang_name = "file-log-discriminator"
                    self.yang_parent_name = "file"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nomatch2', (YLeaf(YType.str, 'nomatch2'), ['str'])),
                        ('match3', (YLeaf(YType.str, 'match3'), ['str'])),
                        ('nomatch3', (YLeaf(YType.str, 'nomatch3'), ['str'])),
                        ('match1', (YLeaf(YType.str, 'match1'), ['str'])),
                        ('nomatch1', (YLeaf(YType.str, 'nomatch1'), ['str'])),
                        ('match2', (YLeaf(YType.str, 'match2'), ['str'])),
                    ])
                    self.nomatch2 = None
                    self.match3 = None
                    self.nomatch3 = None
                    self.match1 = None
                    self.nomatch1 = None
                    self.match2 = None
                    self._segment_path = lambda: "file-log-discriminator"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.Files.File.FileLogDiscriminator, [u'nomatch2', u'match3', u'nomatch3', u'match1', u'nomatch1', u'match2'], name, value)


    class Ipv4(Entity):
        """
        Syslog TOS bit for outgoing messages
        
        .. attribute:: dscp
        
        	DSCP value
        	**type**\:  :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Dscp>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        .. attribute:: tos
        
        	Type of service
        	**type**\:  :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Tos>`
        
        .. attribute:: precedence
        
        	Precedence value
        	**type**\:  :py:class:`Precedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv4.Precedence>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dscp", ("dscp", Syslog.Ipv4.Dscp)), ("tos", ("tos", Syslog.Ipv4.Tos)), ("precedence", ("precedence", Syslog.Ipv4.Precedence))])
            self._leafs = OrderedDict()

            self.dscp = None
            self._children_name_map["dscp"] = "dscp"

            self.tos = Syslog.Ipv4.Tos()
            self.tos.parent = self
            self._children_name_map["tos"] = "tos"

            self.precedence = None
            self._children_name_map["precedence"] = "precedence"
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Ipv4, [], name, value)


        class Dscp(Entity):
            """
            DSCP value
            
            .. attribute:: type
            
            	Logging TOS type DSCP
            	**type**\:  :py:class:`LoggingDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscp>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Ipv4.Dscp, self).__init__()

                self.yang_name = "dscp"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscp', '')])),
                    ('unused', (YLeaf(YType.str, 'unused'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValue', ''),'int'])),
                    ('value', (YLeaf(YType.str, 'value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValue', ''),'int'])),
                ])
                self.type = None
                self.unused = None
                self.value = None
                self._segment_path = lambda: "dscp"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Ipv4.Dscp, [u'type', u'unused', u'value'], name, value)


        class Tos(Entity):
            """
            Type of service
            
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\:  :py:class:`LoggingTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingTos>`
            
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Ipv4.Tos, self).__init__()

                self.yang_name = "tos"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingTos', '')])),
                    ('precedence', (YLeaf(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValue', ''),'int'])),
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValue', ''),'int'])),
                ])
                self.type = None
                self.precedence = None
                self.dscp = None
                self._segment_path = lambda: "tos"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Ipv4.Tos, [u'type', u'precedence', u'dscp'], name, value)


        class Precedence(Entity):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\:  :py:class:`LoggingPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedence>`
            
            	**mandatory**\: True
            
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Ipv4.Precedence, self).__init__()

                self.yang_name = "precedence"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedence', '')])),
                    ('value', (YLeaf(YType.str, 'value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValue', ''),'int'])),
                    ('unused', (YLeaf(YType.str, 'unused'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValue', ''),'int'])),
                ])
                self.type = None
                self.value = None
                self.unused = None
                self._segment_path = lambda: "precedence"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Ipv4.Precedence, [u'type', u'value', u'unused'], name, value)


    class Archive(Entity):
        """
        Archive attributes configuration
        
        .. attribute:: size
        
        	The total size of the archive
        	**type**\: int
        
        	**range:** 1..2047
        
        .. attribute:: file_size
        
        	The maximum file size for a single log file
        	**type**\: int
        
        	**range:** 1..2047
        
        .. attribute:: device
        
        	'/disk0\:' or '/disk1\:' or '/harddisk\:'
        	**type**\: str
        
        .. attribute:: threshold
        
        	The size threshold at which a syslog is generated
        	**type**\: int
        
        	**range:** 1..99
        
        	**units**\: percentage
        
        .. attribute:: frequency
        
        	The collection interval for logs
        	**type**\:  :py:class:`LogCollectFrequency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogCollectFrequency>`
        
        .. attribute:: severity
        
        	The minimum severity of log messages to archive
        	**type**\:  :py:class:`LogMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogMessageSeverity>`
        
        .. attribute:: length
        
        	The maximum number of weeks of log to maintain
        	**type**\: int
        
        	**range:** 1..256
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.Archive, self).__init__()

            self.yang_name = "archive"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                ('file_size', (YLeaf(YType.uint32, 'file-size'), ['int'])),
                ('device', (YLeaf(YType.str, 'device'), ['str'])),
                ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                ('frequency', (YLeaf(YType.enumeration, 'frequency'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogCollectFrequency', '')])),
                ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LogMessageSeverity', '')])),
                ('length', (YLeaf(YType.uint32, 'length'), ['int'])),
            ])
            self.size = None
            self.file_size = None
            self.device = None
            self.threshold = None
            self.frequency = None
            self.severity = None
            self.length = None
            self._segment_path = lambda: "archive"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Archive, [u'size', u'file_size', u'device', u'threshold', u'frequency', u'severity', u'length'], name, value)


    class Ipv6(Entity):
        """
        Syslog traffic class bit for outgoing messages
        
        .. attribute:: dscp
        
        	DSCP value
        	**type**\:  :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.Dscp>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        .. attribute:: traffic_class
        
        	Type of traffic class
        	**type**\:  :py:class:`TrafficClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.TrafficClass>`
        
        .. attribute:: precedence
        
        	Precedence value
        	**type**\:  :py:class:`Precedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Ipv6.Precedence>`
        
        	**presence node**\: True
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dscp", ("dscp", Syslog.Ipv6.Dscp)), ("traffic-class", ("traffic_class", Syslog.Ipv6.TrafficClass)), ("precedence", ("precedence", Syslog.Ipv6.Precedence))])
            self._leafs = OrderedDict()

            self.dscp = None
            self._children_name_map["dscp"] = "dscp"

            self.traffic_class = Syslog.Ipv6.TrafficClass()
            self.traffic_class.parent = self
            self._children_name_map["traffic_class"] = "traffic-class"

            self.precedence = None
            self._children_name_map["precedence"] = "precedence"
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Ipv6, [], name, value)


        class Dscp(Entity):
            """
            DSCP value
            
            .. attribute:: type
            
            	Logging TOS type DSCP
            	**type**\:  :py:class:`LoggingDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscp>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Ipv6.Dscp, self).__init__()

                self.yang_name = "dscp"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscp', '')])),
                    ('unused', (YLeaf(YType.str, 'unused'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValue', ''),'int'])),
                    ('value', (YLeaf(YType.str, 'value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValue', ''),'int'])),
                ])
                self.type = None
                self.unused = None
                self.value = None
                self._segment_path = lambda: "dscp"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Ipv6.Dscp, [u'type', u'unused', u'value'], name, value)


        class TrafficClass(Entity):
            """
            Type of traffic class
            
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\:  :py:class:`LoggingTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingTos>`
            
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Ipv6.TrafficClass, self).__init__()

                self.yang_name = "traffic-class"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingTos', '')])),
                    ('precedence', (YLeaf(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValue', ''),'int'])),
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValue', ''),'int'])),
                ])
                self.type = None
                self.precedence = None
                self.dscp = None
                self._segment_path = lambda: "traffic-class"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Ipv6.TrafficClass, [u'type', u'precedence', u'dscp'], name, value)


        class Precedence(Entity):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\:  :py:class:`LoggingPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedence>`
            
            	**mandatory**\: True
            
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.Ipv6.Precedence, self).__init__()

                self.yang_name = "precedence"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedence', '')])),
                    ('value', (YLeaf(YType.str, 'value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingPrecedenceValue', ''),'int'])),
                    ('unused', (YLeaf(YType.str, 'unused'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg', 'LoggingDscpValue', ''),'int'])),
                ])
                self.type = None
                self.value = None
                self.unused = None
                self._segment_path = lambda: "precedence"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Ipv6.Precedence, [u'type', u'value', u'unused'], name, value)


    class SourceInterfaceTable(Entity):
        """
        Configure source interface
        
        .. attribute:: source_interface_values
        
        	Specify interface for source address in logging transactions
        	**type**\:  :py:class:`SourceInterfaceValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2017-10-31'

        def __init__(self):
            super(Syslog.SourceInterfaceTable, self).__init__()

            self.yang_name = "source-interface-table"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("source-interface-values", ("source_interface_values", Syslog.SourceInterfaceTable.SourceInterfaceValues))])
            self._leafs = OrderedDict()

            self.source_interface_values = Syslog.SourceInterfaceTable.SourceInterfaceValues()
            self.source_interface_values.parent = self
            self._children_name_map["source_interface_values"] = "source-interface-values"
            self._segment_path = lambda: "source-interface-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.SourceInterfaceTable, [], name, value)


        class SourceInterfaceValues(Entity):
            """
            Specify interface for source address in logging
            transactions
            
            .. attribute:: source_interface_value
            
            	Source interface
            	**type**\: list of  		 :py:class:`SourceInterfaceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2017-10-31'

            def __init__(self):
                super(Syslog.SourceInterfaceTable.SourceInterfaceValues, self).__init__()

                self.yang_name = "source-interface-values"
                self.yang_parent_name = "source-interface-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("source-interface-value", ("source_interface_value", Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue))])
                self._leafs = OrderedDict()

                self.source_interface_value = YList(self)
                self._segment_path = lambda: "source-interface-values"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/source-interface-table/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.SourceInterfaceTable.SourceInterfaceValues, [], name, value)


            class SourceInterfaceValue(Entity):
                """
                Source interface
                
                .. attribute:: src_interface_name_value  (key)
                
                	Which Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: source_interface_vrfs
                
                	Configure source interface VRF
                	**type**\:  :py:class:`SourceInterfaceVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2017-10-31'

                def __init__(self):
                    super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue, self).__init__()

                    self.yang_name = "source-interface-value"
                    self.yang_parent_name = "source-interface-values"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['src_interface_name_value']
                    self._child_classes = OrderedDict([("source-interface-vrfs", ("source_interface_vrfs", Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs))])
                    self._leafs = OrderedDict([
                        ('src_interface_name_value', (YLeaf(YType.str, 'src-interface-name-value'), ['str'])),
                    ])
                    self.src_interface_name_value = None

                    self.source_interface_vrfs = Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs()
                    self.source_interface_vrfs.parent = self
                    self._children_name_map["source_interface_vrfs"] = "source-interface-vrfs"
                    self._segment_path = lambda: "source-interface-value" + "[src-interface-name-value='" + str(self.src_interface_name_value) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/source-interface-table/source-interface-values/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue, [u'src_interface_name_value'], name, value)


                class SourceInterfaceVrfs(Entity):
                    """
                    Configure source interface VRF
                    
                    .. attribute:: source_interface_vrf
                    
                    	Specify VRF for source interface
                    	**type**\: list of  		 :py:class:`SourceInterfaceVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2017-10-31'

                    def __init__(self):
                        super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs, self).__init__()

                        self.yang_name = "source-interface-vrfs"
                        self.yang_parent_name = "source-interface-value"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source-interface-vrf", ("source_interface_vrf", Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf))])
                        self._leafs = OrderedDict()

                        self.source_interface_vrf = YList(self)
                        self._segment_path = lambda: "source-interface-vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs, [], name, value)


                    class SourceInterfaceVrf(Entity):
                        """
                        Specify VRF for source interface
                        
                        .. attribute:: vrf_name  (key)
                        
                        	Name of the VRF instance
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'infra-syslog-cfg'
                        _revision = '2017-10-31'

                        def __init__(self):
                            super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf, self).__init__()

                            self.yang_name = "source-interface-vrf"
                            self.yang_parent_name = "source-interface-vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None
                            self._segment_path = lambda: "source-interface-vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf, [u'vrf_name'], name, value)


    class Correlator(Entity):
        """
        Configure properties of the event correlator
        
        .. attribute:: rules
        
        	Table of configured rules
        	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules>`
        
        .. attribute:: rule_sets
        
        	Table of configured rulesets
        	**type**\:  :py:class:`RuleSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets>`
        
        .. attribute:: buffer_size
        
        	Configure size of the correlator buffer
        	**type**\: int
        
        	**range:** 1024..52428800
        
        

        """

        _prefix = 'infra-correlator-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Syslog.Correlator, self).__init__()

            self.yang_name = "correlator"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rules", ("rules", Syslog.Correlator.Rules)), ("rule-sets", ("rule_sets", Syslog.Correlator.RuleSets))])
            self._leafs = OrderedDict([
                ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
            ])
            self.buffer_size = None

            self.rules = Syslog.Correlator.Rules()
            self.rules.parent = self
            self._children_name_map["rules"] = "rules"

            self.rule_sets = Syslog.Correlator.RuleSets()
            self.rule_sets.parent = self
            self._children_name_map["rule_sets"] = "rule-sets"
            self._segment_path = lambda: "Cisco-IOS-XR-infra-correlator-cfg:correlator"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Correlator, ['buffer_size'], name, value)


        class Rules(Entity):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of  		 :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Syslog.Correlator.Rules, self).__init__()

                self.yang_name = "rules"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule", ("rule", Syslog.Correlator.Rules.Rule))])
                self._leafs = OrderedDict()

                self.rule = YList(self)
                self._segment_path = lambda: "rules"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Correlator.Rules, [], name, value)


            class Rule(Entity):
                """
                Rule name
                
                .. attribute:: name  (key)
                
                	Rule name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: definition
                
                	Configure a specified correlation rule
                	**type**\:  :py:class:`Definition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Definition>`
                
                .. attribute:: non_stateful
                
                	The Non\-Stateful Rule Type
                	**type**\:  :py:class:`NonStateful <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful>`
                
                .. attribute:: stateful
                
                	The Stateful Rule Type
                	**type**\:  :py:class:`Stateful <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful>`
                
                .. attribute:: apply_to
                
                	Apply the Rules
                	**type**\:  :py:class:`ApplyTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.ApplyTo>`
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:  :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo>`
                
                

                """

                _prefix = 'infra-correlator-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Syslog.Correlator.Rules.Rule, self).__init__()

                    self.yang_name = "rule"
                    self.yang_parent_name = "rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("definition", ("definition", Syslog.Correlator.Rules.Rule.Definition)), ("non-stateful", ("non_stateful", Syslog.Correlator.Rules.Rule.NonStateful)), ("stateful", ("stateful", Syslog.Correlator.Rules.Rule.Stateful)), ("apply-to", ("apply_to", Syslog.Correlator.Rules.Rule.ApplyTo)), ("applied-to", ("applied_to", Syslog.Correlator.Rules.Rule.AppliedTo))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.definition = Syslog.Correlator.Rules.Rule.Definition()
                    self.definition.parent = self
                    self._children_name_map["definition"] = "definition"

                    self.non_stateful = Syslog.Correlator.Rules.Rule.NonStateful()
                    self.non_stateful.parent = self
                    self._children_name_map["non_stateful"] = "non-stateful"

                    self.stateful = Syslog.Correlator.Rules.Rule.Stateful()
                    self.stateful.parent = self
                    self._children_name_map["stateful"] = "stateful"

                    self.apply_to = Syslog.Correlator.Rules.Rule.ApplyTo()
                    self.apply_to.parent = self
                    self._children_name_map["apply_to"] = "apply-to"

                    self.applied_to = Syslog.Correlator.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._segment_path = lambda: "rule" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/rules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.Correlator.Rules.Rule, ['name'], name, value)


                class Definition(Entity):
                    """
                    Configure a specified correlation rule
                    
                    .. attribute:: timeout
                    
                    	Timeout (time the rule is to be active) in milliseconds
                    	**type**\: int
                    
                    	**range:** 1..7200000
                    
                    .. attribute:: category_name_entry1
                    
                    	Root message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry1
                    
                    	Root message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry1
                    
                    	Root message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry2
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry2
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry2
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry3
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry3
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry3
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry4
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry4
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry4
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry5
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry5
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry5
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry6
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry6
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry6
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry7
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry7
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry7
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry8
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry8
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry8
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry9
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry9
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry9
                    
                    	Correlated message code
                    	**type**\: str
                    
                    .. attribute:: category_name_entry10
                    
                    	Correlated message category name
                    	**type**\: str
                    
                    .. attribute:: group_name_entry10
                    
                    	Correlated message group name
                    	**type**\: str
                    
                    .. attribute:: message_code_entry10
                    
                    	Correlated message code
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.Rules.Rule.Definition, self).__init__()

                        self.yang_name = "definition"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                            ('category_name_entry1', (YLeaf(YType.str, 'category-name-entry1'), ['str'])),
                            ('group_name_entry1', (YLeaf(YType.str, 'group-name-entry1'), ['str'])),
                            ('message_code_entry1', (YLeaf(YType.str, 'message-code-entry1'), ['str'])),
                            ('category_name_entry2', (YLeaf(YType.str, 'category-name-entry2'), ['str'])),
                            ('group_name_entry2', (YLeaf(YType.str, 'group-name-entry2'), ['str'])),
                            ('message_code_entry2', (YLeaf(YType.str, 'message-code-entry2'), ['str'])),
                            ('category_name_entry3', (YLeaf(YType.str, 'category-name-entry3'), ['str'])),
                            ('group_name_entry3', (YLeaf(YType.str, 'group-name-entry3'), ['str'])),
                            ('message_code_entry3', (YLeaf(YType.str, 'message-code-entry3'), ['str'])),
                            ('category_name_entry4', (YLeaf(YType.str, 'category-name-entry4'), ['str'])),
                            ('group_name_entry4', (YLeaf(YType.str, 'group-name-entry4'), ['str'])),
                            ('message_code_entry4', (YLeaf(YType.str, 'message-code-entry4'), ['str'])),
                            ('category_name_entry5', (YLeaf(YType.str, 'category-name-entry5'), ['str'])),
                            ('group_name_entry5', (YLeaf(YType.str, 'group-name-entry5'), ['str'])),
                            ('message_code_entry5', (YLeaf(YType.str, 'message-code-entry5'), ['str'])),
                            ('category_name_entry6', (YLeaf(YType.str, 'category-name-entry6'), ['str'])),
                            ('group_name_entry6', (YLeaf(YType.str, 'group-name-entry6'), ['str'])),
                            ('message_code_entry6', (YLeaf(YType.str, 'message-code-entry6'), ['str'])),
                            ('category_name_entry7', (YLeaf(YType.str, 'category-name-entry7'), ['str'])),
                            ('group_name_entry7', (YLeaf(YType.str, 'group-name-entry7'), ['str'])),
                            ('message_code_entry7', (YLeaf(YType.str, 'message-code-entry7'), ['str'])),
                            ('category_name_entry8', (YLeaf(YType.str, 'category-name-entry8'), ['str'])),
                            ('group_name_entry8', (YLeaf(YType.str, 'group-name-entry8'), ['str'])),
                            ('message_code_entry8', (YLeaf(YType.str, 'message-code-entry8'), ['str'])),
                            ('category_name_entry9', (YLeaf(YType.str, 'category-name-entry9'), ['str'])),
                            ('group_name_entry9', (YLeaf(YType.str, 'group-name-entry9'), ['str'])),
                            ('message_code_entry9', (YLeaf(YType.str, 'message-code-entry9'), ['str'])),
                            ('category_name_entry10', (YLeaf(YType.str, 'category-name-entry10'), ['str'])),
                            ('group_name_entry10', (YLeaf(YType.str, 'group-name-entry10'), ['str'])),
                            ('message_code_entry10', (YLeaf(YType.str, 'message-code-entry10'), ['str'])),
                        ])
                        self.timeout = None
                        self.category_name_entry1 = None
                        self.group_name_entry1 = None
                        self.message_code_entry1 = None
                        self.category_name_entry2 = None
                        self.group_name_entry2 = None
                        self.message_code_entry2 = None
                        self.category_name_entry3 = None
                        self.group_name_entry3 = None
                        self.message_code_entry3 = None
                        self.category_name_entry4 = None
                        self.group_name_entry4 = None
                        self.message_code_entry4 = None
                        self.category_name_entry5 = None
                        self.group_name_entry5 = None
                        self.message_code_entry5 = None
                        self.category_name_entry6 = None
                        self.group_name_entry6 = None
                        self.message_code_entry6 = None
                        self.category_name_entry7 = None
                        self.group_name_entry7 = None
                        self.message_code_entry7 = None
                        self.category_name_entry8 = None
                        self.group_name_entry8 = None
                        self.message_code_entry8 = None
                        self.category_name_entry9 = None
                        self.group_name_entry9 = None
                        self.message_code_entry9 = None
                        self.category_name_entry10 = None
                        self.group_name_entry10 = None
                        self.message_code_entry10 = None
                        self._segment_path = lambda: "definition"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.Rules.Rule.Definition, ['timeout', 'category_name_entry1', 'group_name_entry1', 'message_code_entry1', 'category_name_entry2', 'group_name_entry2', 'message_code_entry2', 'category_name_entry3', 'group_name_entry3', 'message_code_entry3', 'category_name_entry4', 'group_name_entry4', 'message_code_entry4', 'category_name_entry5', 'group_name_entry5', 'message_code_entry5', 'category_name_entry6', 'group_name_entry6', 'message_code_entry6', 'category_name_entry7', 'group_name_entry7', 'message_code_entry7', 'category_name_entry8', 'group_name_entry8', 'message_code_entry8', 'category_name_entry9', 'group_name_entry9', 'message_code_entry9', 'category_name_entry10', 'group_name_entry10', 'message_code_entry10'], name, value)


                class NonStateful(Entity):
                    """
                    The Non\-Stateful Rule Type
                    
                    .. attribute:: context_correlation
                    
                    	Enable correlation on alarm context
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: timeout_root_cause
                    
                    	Rootcause Timeout (time to wait for rootcause) in milliseconds
                    	**type**\: int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: non_root_causes
                    
                    	Table of configured non\-rootcause
                    	**type**\:  :py:class:`NonRootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses>`
                    
                    .. attribute:: root_cause
                    
                    	The root cause
                    	**type**\:  :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.RootCause>`
                    
                    .. attribute:: timeout
                    
                    	Timeout (time to wait for active correlation) in milliseconds
                    	**type**\: int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.Rules.Rule.NonStateful, self).__init__()

                        self.yang_name = "non-stateful"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("non-root-causes", ("non_root_causes", Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses)), ("root-cause", ("root_cause", Syslog.Correlator.Rules.Rule.NonStateful.RootCause))])
                        self._leafs = OrderedDict([
                            ('context_correlation', (YLeaf(YType.empty, 'context-correlation'), ['Empty'])),
                            ('timeout_root_cause', (YLeaf(YType.uint32, 'timeout-root-cause'), ['int'])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ])
                        self.context_correlation = None
                        self.timeout_root_cause = None
                        self.timeout = None

                        self.non_root_causes = Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self._children_name_map["non_root_causes"] = "non-root-causes"

                        self.root_cause = Syslog.Correlator.Rules.Rule.NonStateful.RootCause()
                        self.root_cause.parent = self
                        self._children_name_map["root_cause"] = "root-cause"
                        self._segment_path = lambda: "non-stateful"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.Rules.Rule.NonStateful, ['context_correlation', 'timeout_root_cause', 'timeout'], name, value)


                    class NonRootCauses(Entity):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of  		 :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses, self).__init__()

                            self.yang_name = "non-root-causes"
                            self.yang_parent_name = "non-stateful"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("non-root-cause", ("non_root_cause", Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause))])
                            self._leafs = OrderedDict()

                            self.non_root_cause = YList(self)
                            self._segment_path = lambda: "non-root-causes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses, [], name, value)


                        class NonRootCause(Entity):
                            """
                            A non\-rootcause
                            
                            .. attribute:: category  (key)
                            
                            	Correlated message category
                            	**type**\: str
                            
                            .. attribute:: group  (key)
                            
                            	Correlated message group
                            	**type**\: str
                            
                            .. attribute:: message_code  (key)
                            
                            	Correlated message code
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, self).__init__()

                                self.yang_name = "non-root-cause"
                                self.yang_parent_name = "non-root-causes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['category','group','message_code']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('category', (YLeaf(YType.str, 'category'), ['str'])),
                                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                    ('message_code', (YLeaf(YType.str, 'message-code'), ['str'])),
                                ])
                                self.category = None
                                self.group = None
                                self.message_code = None
                                self._segment_path = lambda: "non-root-cause" + "[category='" + str(self.category) + "']" + "[group='" + str(self.group) + "']" + "[message-code='" + str(self.message_code) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, ['category', 'group', 'message_code'], name, value)


                    class RootCause(Entity):
                        """
                        The root cause
                        
                        .. attribute:: category
                        
                        	Root message category
                        	**type**\: str
                        
                        .. attribute:: group
                        
                        	Root message group
                        	**type**\: str
                        
                        .. attribute:: message_code
                        
                        	Root message code
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.NonStateful.RootCause, self).__init__()

                            self.yang_name = "root-cause"
                            self.yang_parent_name = "non-stateful"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.str, 'category'), ['str'])),
                                ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                ('message_code', (YLeaf(YType.str, 'message-code'), ['str'])),
                            ])
                            self.category = None
                            self.group = None
                            self.message_code = None
                            self._segment_path = lambda: "root-cause"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.NonStateful.RootCause, ['category', 'group', 'message_code'], name, value)


                class Stateful(Entity):
                    """
                    The Stateful Rule Type
                    
                    .. attribute:: reparent
                    
                    	Enable reparent of alarm on rootcause alarm clear
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reissue
                    
                    	Enable reissue of non\-bistate alarms on rootcause alarm clear
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: context_correlation
                    
                    	Enable correlation on alarm context
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: timeout_root_cause
                    
                    	Rootcause Timeout (time to wait for rootcause) in milliseconds
                    	**type**\: int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: non_root_causes
                    
                    	Table of configured non\-rootcause
                    	**type**\:  :py:class:`NonRootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses>`
                    
                    .. attribute:: root_cause
                    
                    	The root cause
                    	**type**\:  :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.RootCause>`
                    
                    .. attribute:: timeout
                    
                    	Timeout (time to wait for active correlation) in milliseconds
                    	**type**\: int
                    
                    	**range:** 1..7200000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.Rules.Rule.Stateful, self).__init__()

                        self.yang_name = "stateful"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("non-root-causes", ("non_root_causes", Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses)), ("root-cause", ("root_cause", Syslog.Correlator.Rules.Rule.Stateful.RootCause))])
                        self._leafs = OrderedDict([
                            ('reparent', (YLeaf(YType.empty, 'reparent'), ['Empty'])),
                            ('reissue', (YLeaf(YType.empty, 'reissue'), ['Empty'])),
                            ('context_correlation', (YLeaf(YType.empty, 'context-correlation'), ['Empty'])),
                            ('timeout_root_cause', (YLeaf(YType.uint32, 'timeout-root-cause'), ['int'])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ])
                        self.reparent = None
                        self.reissue = None
                        self.context_correlation = None
                        self.timeout_root_cause = None
                        self.timeout = None

                        self.non_root_causes = Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self._children_name_map["non_root_causes"] = "non-root-causes"

                        self.root_cause = Syslog.Correlator.Rules.Rule.Stateful.RootCause()
                        self.root_cause.parent = self
                        self._children_name_map["root_cause"] = "root-cause"
                        self._segment_path = lambda: "stateful"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.Rules.Rule.Stateful, ['reparent', 'reissue', 'context_correlation', 'timeout_root_cause', 'timeout'], name, value)


                    class NonRootCauses(Entity):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of  		 :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses, self).__init__()

                            self.yang_name = "non-root-causes"
                            self.yang_parent_name = "stateful"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("non-root-cause", ("non_root_cause", Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause))])
                            self._leafs = OrderedDict()

                            self.non_root_cause = YList(self)
                            self._segment_path = lambda: "non-root-causes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses, [], name, value)


                        class NonRootCause(Entity):
                            """
                            A non\-rootcause
                            
                            .. attribute:: category  (key)
                            
                            	Correlated message category
                            	**type**\: str
                            
                            .. attribute:: group  (key)
                            
                            	Correlated message group
                            	**type**\: str
                            
                            .. attribute:: message_code  (key)
                            
                            	Correlated message code
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause, self).__init__()

                                self.yang_name = "non-root-cause"
                                self.yang_parent_name = "non-root-causes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['category','group','message_code']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('category', (YLeaf(YType.str, 'category'), ['str'])),
                                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                    ('message_code', (YLeaf(YType.str, 'message-code'), ['str'])),
                                ])
                                self.category = None
                                self.group = None
                                self.message_code = None
                                self._segment_path = lambda: "non-root-cause" + "[category='" + str(self.category) + "']" + "[group='" + str(self.group) + "']" + "[message-code='" + str(self.message_code) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause, ['category', 'group', 'message_code'], name, value)


                    class RootCause(Entity):
                        """
                        The root cause
                        
                        .. attribute:: category
                        
                        	Root message category
                        	**type**\: str
                        
                        .. attribute:: group
                        
                        	Root message group
                        	**type**\: str
                        
                        .. attribute:: message_code
                        
                        	Root message code
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.Stateful.RootCause, self).__init__()

                            self.yang_name = "root-cause"
                            self.yang_parent_name = "stateful"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.str, 'category'), ['str'])),
                                ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                ('message_code', (YLeaf(YType.str, 'message-code'), ['str'])),
                            ])
                            self.category = None
                            self.group = None
                            self.message_code = None
                            self._segment_path = lambda: "root-cause"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.Stateful.RootCause, ['category', 'group', 'message_code'], name, value)


                class ApplyTo(Entity):
                    """
                    Apply the Rules
                    
                    .. attribute:: contexts
                    
                    	Apply rule to a specified list of contexts, e.g. interfaces
                    	**type**\:  :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.ApplyTo.Contexts>`
                    
                    .. attribute:: locations
                    
                    	Apply rule to a specified list of Locations
                    	**type**\:  :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.ApplyTo.Locations>`
                    
                    .. attribute:: all_of_router
                    
                    	Apply the rule to all of the router
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.Rules.Rule.ApplyTo, self).__init__()

                        self.yang_name = "apply-to"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("contexts", ("contexts", Syslog.Correlator.Rules.Rule.ApplyTo.Contexts)), ("locations", ("locations", Syslog.Correlator.Rules.Rule.ApplyTo.Locations))])
                        self._leafs = OrderedDict([
                            ('all_of_router', (YLeaf(YType.empty, 'all-of-router'), ['Empty'])),
                        ])
                        self.all_of_router = None

                        self.contexts = Syslog.Correlator.Rules.Rule.ApplyTo.Contexts()
                        self.contexts.parent = self
                        self._children_name_map["contexts"] = "contexts"

                        self.locations = Syslog.Correlator.Rules.Rule.ApplyTo.Locations()
                        self.locations.parent = self
                        self._children_name_map["locations"] = "locations"
                        self._segment_path = lambda: "apply-to"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.Rules.Rule.ApplyTo, ['all_of_router'], name, value)


                    class Contexts(Entity):
                        """
                        Apply rule to a specified list of contexts,
                        e.g. interfaces
                        
                        .. attribute:: context
                        
                        	One or more context names
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.ApplyTo.Contexts, self).__init__()

                            self.yang_name = "contexts"
                            self.yang_parent_name = "apply-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('context', (YLeafList(YType.str, 'context'), ['str'])),
                            ])
                            self.context = []
                            self._segment_path = lambda: "contexts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.ApplyTo.Contexts, ['context'], name, value)


                    class Locations(Entity):
                        """
                        Apply rule to a specified list of Locations
                        
                        .. attribute:: location
                        
                        	One or more Locations
                        	**type**\: list of str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.ApplyTo.Locations, self).__init__()

                            self.yang_name = "locations"
                            self.yang_parent_name = "apply-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', (YLeafList(YType.str, 'location'), ['str'])),
                            ])
                            self.location = []
                            self._segment_path = lambda: "locations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.ApplyTo.Locations, ['location'], name, value)


                class AppliedTo(Entity):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: contexts
                    
                    	Table of configured contexts to apply
                    	**type**\:  :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Contexts>`
                    
                    .. attribute:: locations
                    
                    	Table of configured locations to apply
                    	**type**\:  :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Locations>`
                    
                    .. attribute:: all
                    
                    	Apply to all of the router
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.Rules.Rule.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("contexts", ("contexts", Syslog.Correlator.Rules.Rule.AppliedTo.Contexts)), ("locations", ("locations", Syslog.Correlator.Rules.Rule.AppliedTo.Locations))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.contexts = Syslog.Correlator.Rules.Rule.AppliedTo.Contexts()
                        self.contexts.parent = self
                        self._children_name_map["contexts"] = "contexts"

                        self.locations = Syslog.Correlator.Rules.Rule.AppliedTo.Locations()
                        self.locations.parent = self
                        self._children_name_map["locations"] = "locations"
                        self._segment_path = lambda: "applied-to"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.Rules.Rule.AppliedTo, ['all'], name, value)


                    class Contexts(Entity):
                        """
                        Table of configured contexts to apply
                        
                        .. attribute:: context
                        
                        	A context
                        	**type**\: list of  		 :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts, self).__init__()

                            self.yang_name = "contexts"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("context", ("context", Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context))])
                            self._leafs = OrderedDict()

                            self.context = YList(self)
                            self._segment_path = lambda: "contexts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts, [], name, value)


                        class Context(Entity):
                            """
                            A context
                            
                            .. attribute:: context  (key)
                            
                            	Context
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context, self).__init__()

                                self.yang_name = "context"
                                self.yang_parent_name = "contexts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['context']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('context', (YLeaf(YType.str, 'context'), ['str'])),
                                ])
                                self.context = None
                                self._segment_path = lambda: "context" + "[context='" + str(self.context) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context, ['context'], name, value)


                    class Locations(Entity):
                        """
                        Table of configured locations to apply
                        
                        .. attribute:: location
                        
                        	A location
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations, self).__init__()

                            self.yang_name = "locations"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("location", ("location", Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location))])
                            self._leafs = OrderedDict()

                            self.location = YList(self)
                            self._segment_path = lambda: "locations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.Rules.Rule.AppliedTo.Locations, [], name, value)


                        class Location(Entity):
                            """
                            A location
                            
                            .. attribute:: location  (key)
                            
                            	Location
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "locations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                ])
                                self.location = None
                                self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location, ['location'], name, value)


        class RuleSets(Entity):
            """
            Table of configured rulesets
            
            .. attribute:: rule_set
            
            	Ruleset name
            	**type**\: list of  		 :py:class:`RuleSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Syslog.Correlator.RuleSets, self).__init__()

                self.yang_name = "rule-sets"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule-set", ("rule_set", Syslog.Correlator.RuleSets.RuleSet))])
                self._leafs = OrderedDict()

                self.rule_set = YList(self)
                self._segment_path = lambda: "rule-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Correlator.RuleSets, [], name, value)


            class RuleSet(Entity):
                """
                Ruleset name
                
                .. attribute:: name  (key)
                
                	Ruleset name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: rulenames
                
                	Table of configured rulenames
                	**type**\:  :py:class:`Rulenames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.Rulenames>`
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:  :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo>`
                
                

                """

                _prefix = 'infra-correlator-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Syslog.Correlator.RuleSets.RuleSet, self).__init__()

                    self.yang_name = "rule-set"
                    self.yang_parent_name = "rule-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("rulenames", ("rulenames", Syslog.Correlator.RuleSets.RuleSet.Rulenames)), ("applied-to", ("applied_to", Syslog.Correlator.RuleSets.RuleSet.AppliedTo))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.rulenames = Syslog.Correlator.RuleSets.RuleSet.Rulenames()
                    self.rulenames.parent = self
                    self._children_name_map["rulenames"] = "rulenames"

                    self.applied_to = Syslog.Correlator.RuleSets.RuleSet.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._segment_path = lambda: "rule-set" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/rule-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet, ['name'], name, value)


                class Rulenames(Entity):
                    """
                    Table of configured rulenames
                    
                    .. attribute:: rulename
                    
                    	A rulename
                    	**type**\: list of  		 :py:class:`Rulename <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.RuleSets.RuleSet.Rulenames, self).__init__()

                        self.yang_name = "rulenames"
                        self.yang_parent_name = "rule-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rulename", ("rulename", Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename))])
                        self._leafs = OrderedDict()

                        self.rulename = YList(self)
                        self._segment_path = lambda: "rulenames"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.Rulenames, [], name, value)


                    class Rulename(Entity):
                        """
                        A rulename
                        
                        .. attribute:: rulename  (key)
                        
                        	Rule name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename, self).__init__()

                            self.yang_name = "rulename"
                            self.yang_parent_name = "rulenames"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rulename']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rulename', (YLeaf(YType.str, 'rulename'), ['str'])),
                            ])
                            self.rulename = None
                            self._segment_path = lambda: "rulename" + "[rulename='" + str(self.rulename) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename, ['rulename'], name, value)


                class AppliedTo(Entity):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: contexts
                    
                    	Table of configured contexts to apply
                    	**type**\:  :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts>`
                    
                    .. attribute:: locations
                    
                    	Table of configured locations to apply
                    	**type**\:  :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations>`
                    
                    .. attribute:: all
                    
                    	Apply to all of the router
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("contexts", ("contexts", Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts)), ("locations", ("locations", Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.contexts = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts()
                        self.contexts.parent = self
                        self._children_name_map["contexts"] = "contexts"

                        self.locations = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations()
                        self.locations.parent = self
                        self._children_name_map["locations"] = "locations"
                        self._segment_path = lambda: "applied-to"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.AppliedTo, ['all'], name, value)


                    class Contexts(Entity):
                        """
                        Table of configured contexts to apply
                        
                        .. attribute:: context
                        
                        	A context
                        	**type**\: list of  		 :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts, self).__init__()

                            self.yang_name = "contexts"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("context", ("context", Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context))])
                            self._leafs = OrderedDict()

                            self.context = YList(self)
                            self._segment_path = lambda: "contexts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts, [], name, value)


                        class Context(Entity):
                            """
                            A context
                            
                            .. attribute:: context  (key)
                            
                            	Context
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context, self).__init__()

                                self.yang_name = "context"
                                self.yang_parent_name = "contexts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['context']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('context', (YLeaf(YType.str, 'context'), ['str'])),
                                ])
                                self.context = None
                                self._segment_path = lambda: "context" + "[context='" + str(self.context) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context, ['context'], name, value)


                    class Locations(Entity):
                        """
                        Table of configured locations to apply
                        
                        .. attribute:: location
                        
                        	A location
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations, self).__init__()

                            self.yang_name = "locations"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("location", ("location", Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location))])
                            self._leafs = OrderedDict()

                            self.location = YList(self)
                            self._segment_path = lambda: "locations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations, [], name, value)


                        class Location(Entity):
                            """
                            A location
                            
                            .. attribute:: location  (key)
                            
                            	Location
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "locations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                ])
                                self.location = None
                                self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location, ['location'], name, value)


    class Suppression(Entity):
        """
        Configure properties of the syslog/alarm
        suppression
        
        .. attribute:: rules
        
        	Table of configured rules
        	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules>`
        
        

        """

        _prefix = 'infra-correlator-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Syslog.Suppression, self).__init__()

            self.yang_name = "suppression"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rules", ("rules", Syslog.Suppression.Rules))])
            self._leafs = OrderedDict()

            self.rules = Syslog.Suppression.Rules()
            self.rules.parent = self
            self._children_name_map["rules"] = "rules"
            self._segment_path = lambda: "Cisco-IOS-XR-infra-correlator-cfg:suppression"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Suppression, [], name, value)


        class Rules(Entity):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of  		 :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Syslog.Suppression.Rules, self).__init__()

                self.yang_name = "rules"
                self.yang_parent_name = "suppression"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule", ("rule", Syslog.Suppression.Rules.Rule))])
                self._leafs = OrderedDict()

                self.rule = YList(self)
                self._segment_path = lambda: "rules"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Suppression.Rules, [], name, value)


            class Rule(Entity):
                """
                Rule name
                
                .. attribute:: name  (key)
                
                	Rule name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: applied_to
                
                	Applied to the Rule
                	**type**\:  :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo>`
                
                .. attribute:: alarm_causes
                
                	Causes of alarms to be suppressed
                	**type**\:  :py:class:`AlarmCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AlarmCauses>`
                
                .. attribute:: all_alarms
                
                	Suppress all alarms
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-correlator-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Syslog.Suppression.Rules.Rule, self).__init__()

                    self.yang_name = "rule"
                    self.yang_parent_name = "rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("applied-to", ("applied_to", Syslog.Suppression.Rules.Rule.AppliedTo)), ("alarm-causes", ("alarm_causes", Syslog.Suppression.Rules.Rule.AlarmCauses))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('all_alarms', (YLeaf(YType.empty, 'all-alarms'), ['Empty'])),
                    ])
                    self.name = None
                    self.all_alarms = None

                    self.applied_to = Syslog.Suppression.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"

                    self.alarm_causes = Syslog.Suppression.Rules.Rule.AlarmCauses()
                    self.alarm_causes.parent = self
                    self._children_name_map["alarm_causes"] = "alarm-causes"
                    self._segment_path = lambda: "rule" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression/rules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.Suppression.Rules.Rule, ['name', 'all_alarms'], name, value)


                class AppliedTo(Entity):
                    """
                    Applied to the Rule
                    
                    .. attribute:: sources
                    
                    	Table of configured sources to apply
                    	**type**\:  :py:class:`Sources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo.Sources>`
                    
                    .. attribute:: all
                    
                    	Apply to all of the router
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Suppression.Rules.Rule.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sources", ("sources", Syslog.Suppression.Rules.Rule.AppliedTo.Sources))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.sources = Syslog.Suppression.Rules.Rule.AppliedTo.Sources()
                        self.sources.parent = self
                        self._children_name_map["sources"] = "sources"
                        self._segment_path = lambda: "applied-to"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Suppression.Rules.Rule.AppliedTo, ['all'], name, value)


                    class Sources(Entity):
                        """
                        Table of configured sources to apply
                        
                        .. attribute:: source
                        
                        	An alarm source
                        	**type**\: list of  		 :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources, self).__init__()

                            self.yang_name = "sources"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("source", ("source", Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source))])
                            self._leafs = OrderedDict()

                            self.source = YList(self)
                            self._segment_path = lambda: "sources"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Suppression.Rules.Rule.AppliedTo.Sources, [], name, value)


                        class Source(Entity):
                            """
                            An alarm source
                            
                            .. attribute:: source  (key)
                            
                            	Source
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'infra-correlator-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "sources"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['source']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                ])
                                self.source = None
                                self._segment_path = lambda: "source" + "[source='" + str(self.source) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source, ['source'], name, value)


                class AlarmCauses(Entity):
                    """
                    Causes of alarms to be suppressed
                    
                    .. attribute:: alarm_cause
                    
                    	Category, Group and Code of alarm/syslog to be suppressed
                    	**type**\: list of  		 :py:class:`AlarmCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Syslog.Suppression.Rules.Rule.AlarmCauses, self).__init__()

                        self.yang_name = "alarm-causes"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("alarm-cause", ("alarm_cause", Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause))])
                        self._leafs = OrderedDict()

                        self.alarm_cause = YList(self)
                        self._segment_path = lambda: "alarm-causes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Syslog.Suppression.Rules.Rule.AlarmCauses, [], name, value)


                    class AlarmCause(Entity):
                        """
                        Category, Group and Code of alarm/syslog to
                        be suppressed
                        
                        .. attribute:: category  (key)
                        
                        	Category
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: group  (key)
                        
                        	Group
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: code  (key)
                        
                        	Code
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause, self).__init__()

                            self.yang_name = "alarm-cause"
                            self.yang_parent_name = "alarm-causes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['category','group','code']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('category', (YLeaf(YType.str, 'category'), ['str'])),
                                ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                ('code', (YLeaf(YType.str, 'code'), ['str'])),
                            ])
                            self.category = None
                            self.group = None
                            self.code = None
                            self._segment_path = lambda: "alarm-cause" + "[category='" + str(self.category) + "']" + "[group='" + str(self.group) + "']" + "[code='" + str(self.code) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause, ['category', 'group', 'code'], name, value)


    class AlarmLogger(Entity):
        """
        Alarm Logger Properties
        
        .. attribute:: alarm_filter_strings
        
        	List of filter strings
        	**type**\:  :py:class:`AlarmFilterStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger.AlarmFilterStrings>`
        
        .. attribute:: pre_config_suppression
        
        	Suppress events from a card/VM till its configuration is complete
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: severity_level
        
        	Log all events with equal or higher (lower level) severity than this
        	**type**\:  :py:class:`AlarmLoggerSeverityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes.AlarmLoggerSeverityLevel>`
        
        .. attribute:: pre_config_suppression_timeout
        
        	Timeout (in minutes) for pre\-config events suppression (default 15)
        	**type**\: int
        
        	**range:** 1..60
        
        	**units**\: minute
        
        	**default value**\: 15
        
        .. attribute:: buffer_size
        
        	Set size of the local event buffer
        	**type**\: int
        
        	**range:** 1024..1024000
        
        .. attribute:: source_location
        
        	Enable alarm source location in message text
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: threshold
        
        	Configure threshold (%) for capacity alarm
        	**type**\: int
        
        	**range:** 10..100
        
        	**default value**\: 90
        
        

        """

        _prefix = 'infra-alarm-logger-cfg'
        _revision = '2017-02-23'

        def __init__(self):
            super(Syslog.AlarmLogger, self).__init__()

            self.yang_name = "alarm-logger"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alarm-filter-strings", ("alarm_filter_strings", Syslog.AlarmLogger.AlarmFilterStrings))])
            self._leafs = OrderedDict([
                ('pre_config_suppression', (YLeaf(YType.empty, 'pre-config-suppression'), ['Empty'])),
                ('severity_level', (YLeaf(YType.enumeration, 'severity-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes', 'AlarmLoggerSeverityLevel', '')])),
                ('pre_config_suppression_timeout', (YLeaf(YType.uint32, 'pre-config-suppression-timeout'), ['int'])),
                ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
                ('source_location', (YLeaf(YType.empty, 'source-location'), ['Empty'])),
                ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
            ])
            self.pre_config_suppression = None
            self.severity_level = None
            self.pre_config_suppression_timeout = None
            self.buffer_size = None
            self.source_location = None
            self.threshold = None

            self.alarm_filter_strings = Syslog.AlarmLogger.AlarmFilterStrings()
            self.alarm_filter_strings.parent = self
            self._children_name_map["alarm_filter_strings"] = "alarm-filter-strings"
            self._segment_path = lambda: "Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.AlarmLogger, ['pre_config_suppression', 'severity_level', 'pre_config_suppression_timeout', 'buffer_size', 'source_location', 'threshold'], name, value)


        class AlarmFilterStrings(Entity):
            """
            List of filter strings
            
            .. attribute:: alarm_filter_string
            
            	Match string to filter alarms
            	**type**\: list of  		 :py:class:`AlarmFilterString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString>`
            
            

            """

            _prefix = 'infra-alarm-logger-cfg'
            _revision = '2017-02-23'

            def __init__(self):
                super(Syslog.AlarmLogger.AlarmFilterStrings, self).__init__()

                self.yang_name = "alarm-filter-strings"
                self.yang_parent_name = "alarm-logger"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("alarm-filter-string", ("alarm_filter_string", Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString))])
                self._leafs = OrderedDict()

                self.alarm_filter_string = YList(self)
                self._segment_path = lambda: "alarm-filter-strings"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.AlarmLogger.AlarmFilterStrings, [], name, value)


            class AlarmFilterString(Entity):
                """
                Match string to filter alarms
                
                .. attribute:: filter_string  (key)
                
                	Filter String
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                

                """

                _prefix = 'infra-alarm-logger-cfg'
                _revision = '2017-02-23'

                def __init__(self):
                    super(Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString, self).__init__()

                    self.yang_name = "alarm-filter-string"
                    self.yang_parent_name = "alarm-filter-strings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['filter_string']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('filter_string', (YLeaf(YType.str, 'filter-string'), ['str'])),
                    ])
                    self.filter_string = None
                    self._segment_path = lambda: "alarm-filter-string" + "[filter-string='" + str(self.filter_string) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger/alarm-filter-strings/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString, ['filter_string'], name, value)

    def clone_ptr(self):
        self._top_entity = Syslog()
        return self._top_entity

