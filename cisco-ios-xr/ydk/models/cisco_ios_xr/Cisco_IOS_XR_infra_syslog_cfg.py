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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Facility(Enum):
    """
    Facility

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
    LogCollectFrequency

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
    LogMessageSeverity

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
    LogSeverity

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
    LoggingDscp

    Logging dscp

    .. data:: dscp = 1

    	Logging TOS type DSCP

    """

    dscp = Enum.YLeaf(1, "dscp")


class LoggingDscpValue(Enum):
    """
    LoggingDscpValue

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
    LoggingLevels

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
    LoggingPrecedence

    Logging precedence

    .. data:: precedence = 0

    	Logging TOS type precedence

    """

    precedence = Enum.YLeaf(0, "precedence")


class LoggingPrecedenceValue(Enum):
    """
    LoggingPrecedenceValue

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
    LoggingTos

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
    TimeInfo

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
    	**type**\:   :py:class:`Timestamps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps>`
    
    

    """

    _prefix = 'infra-syslog-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        super(SyslogService, self).__init__()
        self._top_entity = None

        self.yang_name = "syslog-service"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-cfg"

        self.timestamps = SyslogService.Timestamps()
        self.timestamps.parent = self
        self._children_name_map["timestamps"] = "timestamps"
        self._children_yang_names.add("timestamps")


    class Timestamps(Entity):
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
            super(SyslogService.Timestamps, self).__init__()

            self.yang_name = "timestamps"
            self.yang_parent_name = "syslog-service"

            self.enable = YLeaf(YType.empty, "enable")

            self.debug = SyslogService.Timestamps.Debug()
            self.debug.parent = self
            self._children_name_map["debug"] = "debug"
            self._children_yang_names.add("debug")

            self.log = SyslogService.Timestamps.Log()
            self.log.parent = self
            self._children_name_map["log"] = "log"
            self._children_yang_names.add("log")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SyslogService.Timestamps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SyslogService.Timestamps, self).__setattr__(name, value)


        class Log(Entity):
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
                super(SyslogService.Timestamps.Log, self).__init__()

                self.yang_name = "log"
                self.yang_parent_name = "timestamps"

                self.log_timestamp_disable = YLeaf(YType.empty, "log-timestamp-disable")

                self.log_uptime = YLeaf(YType.empty, "log-uptime")

                self.log_datetime = SyslogService.Timestamps.Log.LogDatetime()
                self.log_datetime.parent = self
                self._children_name_map["log_datetime"] = "log-datetime"
                self._children_yang_names.add("log-datetime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("log_timestamp_disable",
                                "log_uptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SyslogService.Timestamps.Log, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SyslogService.Timestamps.Log, self).__setattr__(name, value)


            class LogDatetime(Entity):
                """
                Timestamp with date and time
                
                .. attribute:: log_datetime_value
                
                	Set timestamp for log message
                	**type**\:   :py:class:`LogDatetimeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(SyslogService.Timestamps.Log.LogDatetime, self).__init__()

                    self.yang_name = "log-datetime"
                    self.yang_parent_name = "log"

                    self.log_datetime_value = SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue()
                    self.log_datetime_value.parent = self
                    self._children_name_map["log_datetime_value"] = "log-datetime-value"
                    self._children_yang_names.add("log-datetime-value")


                class LogDatetimeValue(Entity):
                    """
                    Set timestamp for log message
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**units**\: second
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue, self).__init__()

                        self.yang_name = "log-datetime-value"
                        self.yang_parent_name = "log-datetime"

                        self.msec = YLeaf(YType.enumeration, "msec")

                        self.time_stamp_value = YLeaf(YType.enumeration, "time-stamp-value")

                        self.time_zone = YLeaf(YType.enumeration, "time-zone")

                        self.year = YLeaf(YType.enumeration, "year")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("msec",
                                        "time_stamp_value",
                                        "time_zone",
                                        "year") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.msec.is_set or
                            self.time_stamp_value.is_set or
                            self.time_zone.is_set or
                            self.year.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.msec.yfilter != YFilter.not_set or
                            self.time_stamp_value.yfilter != YFilter.not_set or
                            self.time_zone.yfilter != YFilter.not_set or
                            self.year.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "log-datetime-value" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/log/log-datetime/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.msec.is_set or self.msec.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.msec.get_name_leafdata())
                        if (self.time_stamp_value.is_set or self.time_stamp_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_stamp_value.get_name_leafdata())
                        if (self.time_zone.is_set or self.time_zone.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_zone.get_name_leafdata())
                        if (self.year.is_set or self.year.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.year.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "msec" or name == "time-stamp-value" or name == "time-zone" or name == "year"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "msec"):
                            self.msec = value
                            self.msec.value_namespace = name_space
                            self.msec.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-stamp-value"):
                            self.time_stamp_value = value
                            self.time_stamp_value.value_namespace = name_space
                            self.time_stamp_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-zone"):
                            self.time_zone = value
                            self.time_zone.value_namespace = name_space
                            self.time_zone.value_namespace_prefix = name_space_prefix
                        if(value_path == "year"):
                            self.year = value
                            self.year.value_namespace = name_space
                            self.year.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.log_datetime_value is not None and self.log_datetime_value.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.log_datetime_value is not None and self.log_datetime_value.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "log-datetime" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/log/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "log-datetime-value"):
                        if (self.log_datetime_value is None):
                            self.log_datetime_value = SyslogService.Timestamps.Log.LogDatetime.LogDatetimeValue()
                            self.log_datetime_value.parent = self
                            self._children_name_map["log_datetime_value"] = "log-datetime-value"
                        return self.log_datetime_value

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "log-datetime-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.log_timestamp_disable.is_set or
                    self.log_uptime.is_set or
                    (self.log_datetime is not None and self.log_datetime.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.log_timestamp_disable.yfilter != YFilter.not_set or
                    self.log_uptime.yfilter != YFilter.not_set or
                    (self.log_datetime is not None and self.log_datetime.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "log" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.log_timestamp_disable.is_set or self.log_timestamp_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log_timestamp_disable.get_name_leafdata())
                if (self.log_uptime.is_set or self.log_uptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log_uptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "log-datetime"):
                    if (self.log_datetime is None):
                        self.log_datetime = SyslogService.Timestamps.Log.LogDatetime()
                        self.log_datetime.parent = self
                        self._children_name_map["log_datetime"] = "log-datetime"
                    return self.log_datetime

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "log-datetime" or name == "log-timestamp-disable" or name == "log-uptime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "log-timestamp-disable"):
                    self.log_timestamp_disable = value
                    self.log_timestamp_disable.value_namespace = name_space
                    self.log_timestamp_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "log-uptime"):
                    self.log_uptime = value
                    self.log_uptime.value_namespace = name_space
                    self.log_uptime.value_namespace_prefix = name_space_prefix


        class Debug(Entity):
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
                super(SyslogService.Timestamps.Debug, self).__init__()

                self.yang_name = "debug"
                self.yang_parent_name = "timestamps"

                self.debug_timestamp_disable = YLeaf(YType.empty, "debug-timestamp-disable")

                self.debug_uptime = YLeaf(YType.empty, "debug-uptime")

                self.debug_datetime = SyslogService.Timestamps.Debug.DebugDatetime()
                self.debug_datetime.parent = self
                self._children_name_map["debug_datetime"] = "debug-datetime"
                self._children_yang_names.add("debug-datetime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("debug_timestamp_disable",
                                "debug_uptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SyslogService.Timestamps.Debug, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SyslogService.Timestamps.Debug, self).__setattr__(name, value)


            class DebugDatetime(Entity):
                """
                Timestamp with date and time
                
                .. attribute:: datetime_value
                
                	Set time format for debug msg
                	**type**\:   :py:class:`DatetimeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue>`
                
                

                """

                _prefix = 'infra-syslog-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(SyslogService.Timestamps.Debug.DebugDatetime, self).__init__()

                    self.yang_name = "debug-datetime"
                    self.yang_parent_name = "debug"

                    self.datetime_value = SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue()
                    self.datetime_value.parent = self
                    self._children_name_map["datetime_value"] = "datetime-value"
                    self._children_yang_names.add("datetime-value")


                class DatetimeValue(Entity):
                    """
                    Set time format for debug msg
                    
                    .. attribute:: msec
                    
                    	Seconds
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**units**\: second
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_stamp_value
                    
                    	Time
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: enable
                    
                    .. attribute:: time_zone
                    
                    	Timezone
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    .. attribute:: year
                    
                    	Year
                    	**type**\:   :py:class:`TimeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.TimeInfo>`
                    
                    	**default value**\: disable
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue, self).__init__()

                        self.yang_name = "datetime-value"
                        self.yang_parent_name = "debug-datetime"

                        self.msec = YLeaf(YType.enumeration, "msec")

                        self.time_stamp_value = YLeaf(YType.enumeration, "time-stamp-value")

                        self.time_zone = YLeaf(YType.enumeration, "time-zone")

                        self.year = YLeaf(YType.enumeration, "year")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("msec",
                                        "time_stamp_value",
                                        "time_zone",
                                        "year") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.msec.is_set or
                            self.time_stamp_value.is_set or
                            self.time_zone.is_set or
                            self.year.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.msec.yfilter != YFilter.not_set or
                            self.time_stamp_value.yfilter != YFilter.not_set or
                            self.time_zone.yfilter != YFilter.not_set or
                            self.year.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "datetime-value" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/debug/debug-datetime/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.msec.is_set or self.msec.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.msec.get_name_leafdata())
                        if (self.time_stamp_value.is_set or self.time_stamp_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_stamp_value.get_name_leafdata())
                        if (self.time_zone.is_set or self.time_zone.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_zone.get_name_leafdata())
                        if (self.year.is_set or self.year.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.year.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "msec" or name == "time-stamp-value" or name == "time-zone" or name == "year"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "msec"):
                            self.msec = value
                            self.msec.value_namespace = name_space
                            self.msec.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-stamp-value"):
                            self.time_stamp_value = value
                            self.time_stamp_value.value_namespace = name_space
                            self.time_stamp_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-zone"):
                            self.time_zone = value
                            self.time_zone.value_namespace = name_space
                            self.time_zone.value_namespace_prefix = name_space_prefix
                        if(value_path == "year"):
                            self.year = value
                            self.year.value_namespace = name_space
                            self.year.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.datetime_value is not None and self.datetime_value.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.datetime_value is not None and self.datetime_value.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "debug-datetime" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/debug/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "datetime-value"):
                        if (self.datetime_value is None):
                            self.datetime_value = SyslogService.Timestamps.Debug.DebugDatetime.DatetimeValue()
                            self.datetime_value.parent = self
                            self._children_name_map["datetime_value"] = "datetime-value"
                        return self.datetime_value

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "datetime-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.debug_timestamp_disable.is_set or
                    self.debug_uptime.is_set or
                    (self.debug_datetime is not None and self.debug_datetime.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.debug_timestamp_disable.yfilter != YFilter.not_set or
                    self.debug_uptime.yfilter != YFilter.not_set or
                    (self.debug_datetime is not None and self.debug_datetime.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "debug" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/timestamps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.debug_timestamp_disable.is_set or self.debug_timestamp_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.debug_timestamp_disable.get_name_leafdata())
                if (self.debug_uptime.is_set or self.debug_uptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.debug_uptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "debug-datetime"):
                    if (self.debug_datetime is None):
                        self.debug_datetime = SyslogService.Timestamps.Debug.DebugDatetime()
                        self.debug_datetime.parent = self
                        self._children_name_map["debug_datetime"] = "debug-datetime"
                    return self.debug_datetime

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "debug-datetime" or name == "debug-timestamp-disable" or name == "debug-uptime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "debug-timestamp-disable"):
                    self.debug_timestamp_disable = value
                    self.debug_timestamp_disable.value_namespace = name_space
                    self.debug_timestamp_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "debug-uptime"):
                    self.debug_uptime = value
                    self.debug_uptime.value_namespace = name_space
                    self.debug_uptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.enable.is_set or
                (self.debug is not None and self.debug.has_data()) or
                (self.log is not None and self.log.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.debug is not None and self.debug.has_operation()) or
                (self.log is not None and self.log.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "timestamps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "debug"):
                if (self.debug is None):
                    self.debug = SyslogService.Timestamps.Debug()
                    self.debug.parent = self
                    self._children_name_map["debug"] = "debug"
                return self.debug

            if (child_yang_name == "log"):
                if (self.log is None):
                    self.log = SyslogService.Timestamps.Log()
                    self.log.parent = self
                    self._children_name_map["log"] = "log"
                return self.log

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "debug" or name == "log" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.timestamps is not None and self.timestamps.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.timestamps is not None and self.timestamps.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog-service" + path_buffer

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

        if (child_yang_name == "timestamps"):
            if (self.timestamps is None):
                self.timestamps = SyslogService.Timestamps()
                self.timestamps.parent = self
                self._children_name_map["timestamps"] = "timestamps"
            return self.timestamps

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "timestamps"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SyslogService()
        return self._top_entity

class Syslog(Entity):
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
        super(Syslog, self).__init__()
        self._top_entity = None

        self.yang_name = "syslog"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-cfg"

        self.enable_console_logging = YLeaf(YType.boolean, "enable-console-logging")

        self.host_name_prefix = YLeaf(YType.str, "host-name-prefix")

        self.local_log_file_size = YLeaf(YType.uint32, "local-log-file-size")

        self.suppress_duplicates = YLeaf(YType.empty, "suppress-duplicates")

        self.alarm_logger = Syslog.AlarmLogger()
        self.alarm_logger.parent = self
        self._children_name_map["alarm_logger"] = "alarm-logger"
        self._children_yang_names.add("alarm-logger")

        self.archive = Syslog.Archive()
        self.archive.parent = self
        self._children_name_map["archive"] = "archive"
        self._children_yang_names.add("archive")

        self.buffered_logging = Syslog.BufferedLogging()
        self.buffered_logging.parent = self
        self._children_name_map["buffered_logging"] = "buffered-logging"
        self._children_yang_names.add("buffered-logging")

        self.console_logging = Syslog.ConsoleLogging()
        self.console_logging.parent = self
        self._children_name_map["console_logging"] = "console-logging"
        self._children_yang_names.add("console-logging")

        self.correlator = Syslog.Correlator()
        self.correlator.parent = self
        self._children_name_map["correlator"] = "correlator"
        self._children_yang_names.add("correlator")

        self.files = Syslog.Files()
        self.files.parent = self
        self._children_name_map["files"] = "files"
        self._children_yang_names.add("files")

        self.history_logging = Syslog.HistoryLogging()
        self.history_logging.parent = self
        self._children_name_map["history_logging"] = "history-logging"
        self._children_yang_names.add("history-logging")

        self.host_server = Syslog.HostServer()
        self.host_server.parent = self
        self._children_name_map["host_server"] = "host-server"
        self._children_yang_names.add("host-server")

        self.ipv4 = Syslog.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._children_yang_names.add("ipv4")

        self.ipv6 = Syslog.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._children_yang_names.add("ipv6")

        self.logging_facilities = Syslog.LoggingFacilities()
        self.logging_facilities.parent = self
        self._children_name_map["logging_facilities"] = "logging-facilities"
        self._children_yang_names.add("logging-facilities")

        self.monitor_logging = Syslog.MonitorLogging()
        self.monitor_logging.parent = self
        self._children_name_map["monitor_logging"] = "monitor-logging"
        self._children_yang_names.add("monitor-logging")

        self.source_interface_table = Syslog.SourceInterfaceTable()
        self.source_interface_table.parent = self
        self._children_name_map["source_interface_table"] = "source-interface-table"
        self._children_yang_names.add("source-interface-table")

        self.suppression = Syslog.Suppression()
        self.suppression.parent = self
        self._children_name_map["suppression"] = "suppression"
        self._children_yang_names.add("suppression")

        self.trap_logging = Syslog.TrapLogging()
        self.trap_logging.parent = self
        self._children_name_map["trap_logging"] = "trap-logging"
        self._children_yang_names.add("trap-logging")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable_console_logging",
                        "host_name_prefix",
                        "local_log_file_size",
                        "suppress_duplicates") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Syslog, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Syslog, self).__setattr__(name, value)


    class MonitorLogging(Entity):
        """
        Set monitor logging
        
        .. attribute:: logging_level
        
        	Monitor Logging Level
        	**type**\:   :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: debug
        
        .. attribute:: monitor_discriminator
        
        	Set monitor logging discriminators
        	**type**\:   :py:class:`MonitorDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.MonitorLogging.MonitorDiscriminator>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.MonitorLogging, self).__init__()

            self.yang_name = "monitor-logging"
            self.yang_parent_name = "syslog"

            self.logging_level = YLeaf(YType.enumeration, "logging-level")

            self.monitor_discriminator = Syslog.MonitorLogging.MonitorDiscriminator()
            self.monitor_discriminator.parent = self
            self._children_name_map["monitor_discriminator"] = "monitor-discriminator"
            self._children_yang_names.add("monitor-discriminator")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("logging_level") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.MonitorLogging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.MonitorLogging, self).__setattr__(name, value)


        class MonitorDiscriminator(Entity):
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
                super(Syslog.MonitorLogging.MonitorDiscriminator, self).__init__()

                self.yang_name = "monitor-discriminator"
                self.yang_parent_name = "monitor-logging"

                self.match1 = YLeaf(YType.str, "match1")

                self.match2 = YLeaf(YType.str, "match2")

                self.match3 = YLeaf(YType.str, "match3")

                self.nomatch1 = YLeaf(YType.str, "nomatch1")

                self.nomatch2 = YLeaf(YType.str, "nomatch2")

                self.nomatch3 = YLeaf(YType.str, "nomatch3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("match1",
                                "match2",
                                "match3",
                                "nomatch1",
                                "nomatch2",
                                "nomatch3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.MonitorLogging.MonitorDiscriminator, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.MonitorLogging.MonitorDiscriminator, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.match1.is_set or
                    self.match2.is_set or
                    self.match3.is_set or
                    self.nomatch1.is_set or
                    self.nomatch2.is_set or
                    self.nomatch3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.match1.yfilter != YFilter.not_set or
                    self.match2.yfilter != YFilter.not_set or
                    self.match3.yfilter != YFilter.not_set or
                    self.nomatch1.yfilter != YFilter.not_set or
                    self.nomatch2.yfilter != YFilter.not_set or
                    self.nomatch3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "monitor-discriminator" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/monitor-logging/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match1.get_name_leafdata())
                if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match2.get_name_leafdata())
                if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match3.get_name_leafdata())
                if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch1.get_name_leafdata())
                if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch2.get_name_leafdata())
                if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "match1"):
                    self.match1 = value
                    self.match1.value_namespace = name_space
                    self.match1.value_namespace_prefix = name_space_prefix
                if(value_path == "match2"):
                    self.match2 = value
                    self.match2.value_namespace = name_space
                    self.match2.value_namespace_prefix = name_space_prefix
                if(value_path == "match3"):
                    self.match3 = value
                    self.match3.value_namespace = name_space
                    self.match3.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch1"):
                    self.nomatch1 = value
                    self.nomatch1.value_namespace = name_space
                    self.nomatch1.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch2"):
                    self.nomatch2 = value
                    self.nomatch2.value_namespace = name_space
                    self.nomatch2.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch3"):
                    self.nomatch3 = value
                    self.nomatch3.value_namespace = name_space
                    self.nomatch3.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.logging_level.is_set or
                (self.monitor_discriminator is not None and self.monitor_discriminator.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.logging_level.yfilter != YFilter.not_set or
                (self.monitor_discriminator is not None and self.monitor_discriminator.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "monitor-logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.logging_level.is_set or self.logging_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.logging_level.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "monitor-discriminator"):
                if (self.monitor_discriminator is None):
                    self.monitor_discriminator = Syslog.MonitorLogging.MonitorDiscriminator()
                    self.monitor_discriminator.parent = self
                    self._children_name_map["monitor_discriminator"] = "monitor-discriminator"
                return self.monitor_discriminator

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "monitor-discriminator" or name == "logging-level"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "logging-level"):
                self.logging_level = value
                self.logging_level.value_namespace = name_space
                self.logging_level.value_namespace_prefix = name_space_prefix


    class HistoryLogging(Entity):
        """
        Set history logging
        
        .. attribute:: history_size
        
        	Logging history size
        	**type**\:  int
        
        	**range:** 1..500
        
        	**default value**\: 1
        
        .. attribute:: logging_level
        
        	History logging level
        	**type**\:   :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: warning
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.HistoryLogging, self).__init__()

            self.yang_name = "history-logging"
            self.yang_parent_name = "syslog"

            self.history_size = YLeaf(YType.uint32, "history-size")

            self.logging_level = YLeaf(YType.enumeration, "logging-level")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("history_size",
                            "logging_level") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.HistoryLogging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.HistoryLogging, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.history_size.is_set or
                self.logging_level.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.history_size.yfilter != YFilter.not_set or
                self.logging_level.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "history-logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.history_size.is_set or self.history_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.history_size.get_name_leafdata())
            if (self.logging_level.is_set or self.logging_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.logging_level.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "history-size" or name == "logging-level"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "history-size"):
                self.history_size = value
                self.history_size.value_namespace = name_space
                self.history_size.value_namespace_prefix = name_space_prefix
            if(value_path == "logging-level"):
                self.logging_level = value
                self.logging_level.value_namespace = name_space
                self.logging_level.value_namespace_prefix = name_space_prefix


    class LoggingFacilities(Entity):
        """
        Modify message logging facilities
        
        .. attribute:: facility_level
        
        	Facility from which logging is done
        	**type**\:   :py:class:`Facility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Facility>`
        
        	**default value**\: local7
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.LoggingFacilities, self).__init__()

            self.yang_name = "logging-facilities"
            self.yang_parent_name = "syslog"

            self.facility_level = YLeaf(YType.enumeration, "facility-level")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("facility_level") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.LoggingFacilities, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.LoggingFacilities, self).__setattr__(name, value)

        def has_data(self):
            return self.facility_level.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.facility_level.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logging-facilities" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.facility_level.is_set or self.facility_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.facility_level.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "facility-level"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "facility-level"):
                self.facility_level = value
                self.facility_level.value_namespace = name_space
                self.facility_level.value_namespace_prefix = name_space_prefix


    class TrapLogging(Entity):
        """
        Set trap logging
        
        .. attribute:: logging_level
        
        	Trap logging level
        	**type**\:   :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: info
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.TrapLogging, self).__init__()

            self.yang_name = "trap-logging"
            self.yang_parent_name = "syslog"

            self.logging_level = YLeaf(YType.enumeration, "logging-level")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("logging_level") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.TrapLogging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.TrapLogging, self).__setattr__(name, value)

        def has_data(self):
            return self.logging_level.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.logging_level.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "trap-logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.logging_level.is_set or self.logging_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.logging_level.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "logging-level"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "logging-level"):
                self.logging_level = value
                self.logging_level.value_namespace = name_space
                self.logging_level.value_namespace_prefix = name_space_prefix


    class BufferedLogging(Entity):
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
        	**type**\:   :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: debug
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.BufferedLogging, self).__init__()

            self.yang_name = "buffered-logging"
            self.yang_parent_name = "syslog"

            self.buffer_size = YLeaf(YType.uint32, "buffer-size")

            self.logging_level = YLeaf(YType.enumeration, "logging-level")

            self.buffered_discriminator = Syslog.BufferedLogging.BufferedDiscriminator()
            self.buffered_discriminator.parent = self
            self._children_name_map["buffered_discriminator"] = "buffered-discriminator"
            self._children_yang_names.add("buffered-discriminator")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("buffer_size",
                            "logging_level") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.BufferedLogging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.BufferedLogging, self).__setattr__(name, value)


        class BufferedDiscriminator(Entity):
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
                super(Syslog.BufferedLogging.BufferedDiscriminator, self).__init__()

                self.yang_name = "buffered-discriminator"
                self.yang_parent_name = "buffered-logging"

                self.match1 = YLeaf(YType.str, "match1")

                self.match2 = YLeaf(YType.str, "match2")

                self.match3 = YLeaf(YType.str, "match3")

                self.nomatch1 = YLeaf(YType.str, "nomatch1")

                self.nomatch2 = YLeaf(YType.str, "nomatch2")

                self.nomatch3 = YLeaf(YType.str, "nomatch3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("match1",
                                "match2",
                                "match3",
                                "nomatch1",
                                "nomatch2",
                                "nomatch3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.BufferedLogging.BufferedDiscriminator, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.BufferedLogging.BufferedDiscriminator, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.match1.is_set or
                    self.match2.is_set or
                    self.match3.is_set or
                    self.nomatch1.is_set or
                    self.nomatch2.is_set or
                    self.nomatch3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.match1.yfilter != YFilter.not_set or
                    self.match2.yfilter != YFilter.not_set or
                    self.match3.yfilter != YFilter.not_set or
                    self.nomatch1.yfilter != YFilter.not_set or
                    self.nomatch2.yfilter != YFilter.not_set or
                    self.nomatch3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "buffered-discriminator" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/buffered-logging/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match1.get_name_leafdata())
                if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match2.get_name_leafdata())
                if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match3.get_name_leafdata())
                if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch1.get_name_leafdata())
                if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch2.get_name_leafdata())
                if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "match1"):
                    self.match1 = value
                    self.match1.value_namespace = name_space
                    self.match1.value_namespace_prefix = name_space_prefix
                if(value_path == "match2"):
                    self.match2 = value
                    self.match2.value_namespace = name_space
                    self.match2.value_namespace_prefix = name_space_prefix
                if(value_path == "match3"):
                    self.match3 = value
                    self.match3.value_namespace = name_space
                    self.match3.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch1"):
                    self.nomatch1 = value
                    self.nomatch1.value_namespace = name_space
                    self.nomatch1.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch2"):
                    self.nomatch2 = value
                    self.nomatch2.value_namespace = name_space
                    self.nomatch2.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch3"):
                    self.nomatch3 = value
                    self.nomatch3.value_namespace = name_space
                    self.nomatch3.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.buffer_size.is_set or
                self.logging_level.is_set or
                (self.buffered_discriminator is not None and self.buffered_discriminator.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.buffer_size.yfilter != YFilter.not_set or
                self.logging_level.yfilter != YFilter.not_set or
                (self.buffered_discriminator is not None and self.buffered_discriminator.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "buffered-logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.buffer_size.get_name_leafdata())
            if (self.logging_level.is_set or self.logging_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.logging_level.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "buffered-discriminator"):
                if (self.buffered_discriminator is None):
                    self.buffered_discriminator = Syslog.BufferedLogging.BufferedDiscriminator()
                    self.buffered_discriminator.parent = self
                    self._children_name_map["buffered_discriminator"] = "buffered-discriminator"
                return self.buffered_discriminator

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "buffered-discriminator" or name == "buffer-size" or name == "logging-level"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "buffer-size"):
                self.buffer_size = value
                self.buffer_size.value_namespace = name_space
                self.buffer_size.value_namespace_prefix = name_space_prefix
            if(value_path == "logging-level"):
                self.logging_level = value
                self.logging_level.value_namespace = name_space
                self.logging_level.value_namespace_prefix = name_space_prefix


    class HostServer(Entity):
        """
        Configure logging host
        
        .. attribute:: vrfs
        
        	VRF table
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.HostServer, self).__init__()

            self.yang_name = "host-server"
            self.yang_parent_name = "syslog"

            self.vrfs = Syslog.HostServer.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")


        class Vrfs(Entity):
            """
            VRF table
            
            .. attribute:: vrf
            
            	VRF specific data
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.HostServer.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "host-server"

                self.vrf = YList(self)

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
                            super(Syslog.HostServer.Vrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.HostServer.Vrfs, self).__setattr__(name, value)


            class Vrf(Entity):
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
                    super(Syslog.HostServer.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.hosts = Syslog.HostServer.Vrfs.Vrf.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                    self._children_yang_names.add("hosts")

                    self.ipv4s = Syslog.HostServer.Vrfs.Vrf.Ipv4S()
                    self.ipv4s.parent = self
                    self._children_name_map["ipv4s"] = "ipv4s"
                    self._children_yang_names.add("ipv4s")

                    self.ipv6s = Syslog.HostServer.Vrfs.Vrf.Ipv6S()
                    self.ipv6s.parent = self
                    self._children_name_map["ipv6s"] = "ipv6s"
                    self._children_yang_names.add("ipv6s")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.HostServer.Vrfs.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.HostServer.Vrfs.Vrf, self).__setattr__(name, value)


                class Ipv6S(Entity):
                    """
                    List of the IPv6 logging host
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address of the logging host
                    	**type**\: list of    :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(Syslog.HostServer.Vrfs.Vrf.Ipv6S, self).__init__()

                        self.yang_name = "ipv6s"
                        self.yang_parent_name = "vrf"

                        self.ipv6 = YList(self)

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
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv6S, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6S, self).__setattr__(name, value)


                    class Ipv6(Entity):
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
                            super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "ipv6s"

                            self.address = YLeaf(YType.str, "address")

                            self.ipv6_discriminator = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator()
                            self.ipv6_discriminator.parent = self
                            self._children_name_map["ipv6_discriminator"] = "ipv6-discriminator"
                            self._children_yang_names.add("ipv6-discriminator")

                            self.ipv6_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels()
                            self.ipv6_severity_levels.parent = self
                            self._children_name_map["ipv6_severity_levels"] = "ipv6-severity-levels"
                            self._children_yang_names.add("ipv6-severity-levels")

                            self.ipv6_severity_port = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort()
                            self.ipv6_severity_port.parent = self
                            self._children_name_map["ipv6_severity_port"] = "ipv6-severity-port"
                            self._children_yang_names.add("ipv6-severity-port")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6, self).__setattr__(name, value)


                        class Ipv6SeverityPort(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort, self).__init__()

                                self.yang_name = "ipv6-severity-port"
                                self.yang_parent_name = "ipv6"

                                self.port = YLeaf(YType.int32, "port")

                                self.severity = YLeaf(YType.int32, "severity")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("port",
                                                "severity") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.port.is_set or
                                    self.severity.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.port.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-severity-port" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port.get_name_leafdata())
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
                                if(name == "port" or name == "severity"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "port"):
                                    self.port = value
                                    self.port.value_namespace = name_space
                                    self.port.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix


                        class Ipv6Discriminator(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator, self).__init__()

                                self.yang_name = "ipv6-discriminator"
                                self.yang_parent_name = "ipv6"

                                self.match1 = YLeaf(YType.str, "match1")

                                self.match2 = YLeaf(YType.str, "match2")

                                self.match3 = YLeaf(YType.str, "match3")

                                self.nomatch1 = YLeaf(YType.str, "nomatch1")

                                self.nomatch2 = YLeaf(YType.str, "nomatch2")

                                self.nomatch3 = YLeaf(YType.str, "nomatch3")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("match1",
                                                "match2",
                                                "match3",
                                                "nomatch1",
                                                "nomatch2",
                                                "nomatch3") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.match1.is_set or
                                    self.match2.is_set or
                                    self.match3.is_set or
                                    self.nomatch1.is_set or
                                    self.nomatch2.is_set or
                                    self.nomatch3.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.match1.yfilter != YFilter.not_set or
                                    self.match2.yfilter != YFilter.not_set or
                                    self.match3.yfilter != YFilter.not_set or
                                    self.nomatch1.yfilter != YFilter.not_set or
                                    self.nomatch2.yfilter != YFilter.not_set or
                                    self.nomatch3.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-discriminator" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match1.get_name_leafdata())
                                if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match2.get_name_leafdata())
                                if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match3.get_name_leafdata())
                                if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch1.get_name_leafdata())
                                if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch2.get_name_leafdata())
                                if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch3.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "match1"):
                                    self.match1 = value
                                    self.match1.value_namespace = name_space
                                    self.match1.value_namespace_prefix = name_space_prefix
                                if(value_path == "match2"):
                                    self.match2 = value
                                    self.match2.value_namespace = name_space
                                    self.match2.value_namespace_prefix = name_space_prefix
                                if(value_path == "match3"):
                                    self.match3 = value
                                    self.match3.value_namespace = name_space
                                    self.match3.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch1"):
                                    self.nomatch1 = value
                                    self.nomatch1.value_namespace = name_space
                                    self.nomatch1.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch2"):
                                    self.nomatch2 = value
                                    self.nomatch2.value_namespace = name_space
                                    self.nomatch2.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch3"):
                                    self.nomatch3 = value
                                    self.nomatch3.value_namespace = name_space
                                    self.nomatch3.value_namespace_prefix = name_space_prefix


                        class Ipv6SeverityLevels(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels, self).__init__()

                                self.yang_name = "ipv6-severity-levels"
                                self.yang_parent_name = "ipv6"

                                self.ipv6_severity_level = YList(self)

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
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels, self).__setattr__(name, value)


                            class Ipv6SeverityLevel(Entity):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  <key>
                                
                                	Severity for the logging host
                                	**type**\:   :py:class:`LogSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverity>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel, self).__init__()

                                    self.yang_name = "ipv6-severity-level"
                                    self.yang_parent_name = "ipv6-severity-levels"

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
                                        if name in ("severity") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.severity.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.severity.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv6-severity-level" + "[severity='" + self.severity.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
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
                                    if(name == "severity"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "severity"):
                                        self.severity = value
                                        self.severity.value_namespace = name_space
                                        self.severity.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.ipv6_severity_level:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.ipv6_severity_level:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-severity-levels" + path_buffer

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

                                if (child_yang_name == "ipv6-severity-level"):
                                    for c in self.ipv6_severity_level:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels.Ipv6SeverityLevel()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.ipv6_severity_level.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv6-severity-level"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.address.is_set or
                                (self.ipv6_discriminator is not None and self.ipv6_discriminator.has_data()) or
                                (self.ipv6_severity_levels is not None and self.ipv6_severity_levels.has_data()) or
                                (self.ipv6_severity_port is not None and self.ipv6_severity_port.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                (self.ipv6_discriminator is not None and self.ipv6_discriminator.has_operation()) or
                                (self.ipv6_severity_levels is not None and self.ipv6_severity_levels.has_operation()) or
                                (self.ipv6_severity_port is not None and self.ipv6_severity_port.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6" + "[address='" + self.address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv6-discriminator"):
                                if (self.ipv6_discriminator is None):
                                    self.ipv6_discriminator = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6Discriminator()
                                    self.ipv6_discriminator.parent = self
                                    self._children_name_map["ipv6_discriminator"] = "ipv6-discriminator"
                                return self.ipv6_discriminator

                            if (child_yang_name == "ipv6-severity-levels"):
                                if (self.ipv6_severity_levels is None):
                                    self.ipv6_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityLevels()
                                    self.ipv6_severity_levels.parent = self
                                    self._children_name_map["ipv6_severity_levels"] = "ipv6-severity-levels"
                                return self.ipv6_severity_levels

                            if (child_yang_name == "ipv6-severity-port"):
                                if (self.ipv6_severity_port is None):
                                    self.ipv6_severity_port = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6.Ipv6SeverityPort()
                                    self.ipv6_severity_port.parent = self
                                    self._children_name_map["ipv6_severity_port"] = "ipv6-severity-port"
                                return self.ipv6_severity_port

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-discriminator" or name == "ipv6-severity-levels" or name == "ipv6-severity-port" or name == "address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ipv6:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ipv6:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6s" + path_buffer

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

                        if (child_yang_name == "ipv6"):
                            for c in self.ipv6:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Syslog.HostServer.Vrfs.Vrf.Ipv6S.Ipv6()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ipv6.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv6"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Hosts(Entity):
                    """
                    List of the logging host
                    
                    .. attribute:: host
                    
                    	Name of the logging host
                    	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(Syslog.HostServer.Vrfs.Vrf.Hosts, self).__init__()

                        self.yang_name = "hosts"
                        self.yang_parent_name = "vrf"

                        self.host = YList(self)

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
                                    super(Syslog.HostServer.Vrfs.Vrf.Hosts, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.HostServer.Vrfs.Vrf.Hosts, self).__setattr__(name, value)


                    class Host(Entity):
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
                            super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host, self).__init__()

                            self.yang_name = "host"
                            self.yang_parent_name = "hosts"

                            self.host_name = YLeaf(YType.str, "host-name")

                            self.host_name_discriminator = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator()
                            self.host_name_discriminator.parent = self
                            self._children_name_map["host_name_discriminator"] = "host-name-discriminator"
                            self._children_yang_names.add("host-name-discriminator")

                            self.host_name_severities = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities()
                            self.host_name_severities.parent = self
                            self._children_name_map["host_name_severities"] = "host-name-severities"
                            self._children_yang_names.add("host-name-severities")

                            self.host_severity_port = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort()
                            self.host_severity_port.parent = self
                            self._children_name_map["host_severity_port"] = "host-severity-port"
                            self._children_yang_names.add("host-severity-port")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("host_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host, self).__setattr__(name, value)


                        class HostNameSeverities(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities, self).__init__()

                                self.yang_name = "host-name-severities"
                                self.yang_parent_name = "host"

                                self.host_name_severity = YList(self)

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
                                            super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities, self).__setattr__(name, value)


                            class HostNameSeverity(Entity):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  <key>
                                
                                	Severity for the logging host
                                	**type**\:   :py:class:`LogSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverity>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity, self).__init__()

                                    self.yang_name = "host-name-severity"
                                    self.yang_parent_name = "host-name-severities"

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
                                        if name in ("severity") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.severity.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.severity.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "host-name-severity" + "[severity='" + self.severity.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
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
                                    if(name == "severity"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "severity"):
                                        self.severity = value
                                        self.severity.value_namespace = name_space
                                        self.severity.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.host_name_severity:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.host_name_severity:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "host-name-severities" + path_buffer

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

                                if (child_yang_name == "host-name-severity"):
                                    for c in self.host_name_severity:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities.HostNameSeverity()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.host_name_severity.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "host-name-severity"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class HostNameDiscriminator(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator, self).__init__()

                                self.yang_name = "host-name-discriminator"
                                self.yang_parent_name = "host"

                                self.match1 = YLeaf(YType.str, "match1")

                                self.match2 = YLeaf(YType.str, "match2")

                                self.match3 = YLeaf(YType.str, "match3")

                                self.nomatch1 = YLeaf(YType.str, "nomatch1")

                                self.nomatch2 = YLeaf(YType.str, "nomatch2")

                                self.nomatch3 = YLeaf(YType.str, "nomatch3")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("match1",
                                                "match2",
                                                "match3",
                                                "nomatch1",
                                                "nomatch2",
                                                "nomatch3") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.match1.is_set or
                                    self.match2.is_set or
                                    self.match3.is_set or
                                    self.nomatch1.is_set or
                                    self.nomatch2.is_set or
                                    self.nomatch3.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.match1.yfilter != YFilter.not_set or
                                    self.match2.yfilter != YFilter.not_set or
                                    self.match3.yfilter != YFilter.not_set or
                                    self.nomatch1.yfilter != YFilter.not_set or
                                    self.nomatch2.yfilter != YFilter.not_set or
                                    self.nomatch3.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "host-name-discriminator" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match1.get_name_leafdata())
                                if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match2.get_name_leafdata())
                                if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match3.get_name_leafdata())
                                if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch1.get_name_leafdata())
                                if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch2.get_name_leafdata())
                                if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch3.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "match1"):
                                    self.match1 = value
                                    self.match1.value_namespace = name_space
                                    self.match1.value_namespace_prefix = name_space_prefix
                                if(value_path == "match2"):
                                    self.match2 = value
                                    self.match2.value_namespace = name_space
                                    self.match2.value_namespace_prefix = name_space_prefix
                                if(value_path == "match3"):
                                    self.match3 = value
                                    self.match3.value_namespace = name_space
                                    self.match3.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch1"):
                                    self.nomatch1 = value
                                    self.nomatch1.value_namespace = name_space
                                    self.nomatch1.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch2"):
                                    self.nomatch2 = value
                                    self.nomatch2.value_namespace = name_space
                                    self.nomatch2.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch3"):
                                    self.nomatch3 = value
                                    self.nomatch3.value_namespace = name_space
                                    self.nomatch3.value_namespace_prefix = name_space_prefix


                        class HostSeverityPort(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort, self).__init__()

                                self.yang_name = "host-severity-port"
                                self.yang_parent_name = "host"

                                self.port = YLeaf(YType.int32, "port")

                                self.severity = YLeaf(YType.int32, "severity")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("port",
                                                "severity") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.port.is_set or
                                    self.severity.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.port.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "host-severity-port" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port.get_name_leafdata())
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
                                if(name == "port" or name == "severity"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "port"):
                                    self.port = value
                                    self.port.value_namespace = name_space
                                    self.port.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.host_name.is_set or
                                (self.host_name_discriminator is not None and self.host_name_discriminator.has_data()) or
                                (self.host_name_severities is not None and self.host_name_severities.has_data()) or
                                (self.host_severity_port is not None and self.host_severity_port.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.host_name.yfilter != YFilter.not_set or
                                (self.host_name_discriminator is not None and self.host_name_discriminator.has_operation()) or
                                (self.host_name_severities is not None and self.host_name_severities.has_operation()) or
                                (self.host_severity_port is not None and self.host_severity_port.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "host" + "[host-name='" + self.host_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "host-name-discriminator"):
                                if (self.host_name_discriminator is None):
                                    self.host_name_discriminator = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameDiscriminator()
                                    self.host_name_discriminator.parent = self
                                    self._children_name_map["host_name_discriminator"] = "host-name-discriminator"
                                return self.host_name_discriminator

                            if (child_yang_name == "host-name-severities"):
                                if (self.host_name_severities is None):
                                    self.host_name_severities = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostNameSeverities()
                                    self.host_name_severities.parent = self
                                    self._children_name_map["host_name_severities"] = "host-name-severities"
                                return self.host_name_severities

                            if (child_yang_name == "host-severity-port"):
                                if (self.host_severity_port is None):
                                    self.host_severity_port = Syslog.HostServer.Vrfs.Vrf.Hosts.Host.HostSeverityPort()
                                    self.host_severity_port.parent = self
                                    self._children_name_map["host_severity_port"] = "host-severity-port"
                                return self.host_severity_port

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "host-name-discriminator" or name == "host-name-severities" or name == "host-severity-port" or name == "host-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "host-name"):
                                self.host_name = value
                                self.host_name.value_namespace = name_space
                                self.host_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.host:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.host:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hosts" + path_buffer

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

                        if (child_yang_name == "host"):
                            for c in self.host:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Syslog.HostServer.Vrfs.Vrf.Hosts.Host()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.host.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Ipv4S(Entity):
                    """
                    List of the IPv4 logging host
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address of the logging host
                    	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(Syslog.HostServer.Vrfs.Vrf.Ipv4S, self).__init__()

                        self.yang_name = "ipv4s"
                        self.yang_parent_name = "vrf"

                        self.ipv4 = YList(self)

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
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv4S, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4S, self).__setattr__(name, value)


                    class Ipv4(Entity):
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
                            super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "ipv4s"

                            self.address = YLeaf(YType.str, "address")

                            self.ipv4_discriminator = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator()
                            self.ipv4_discriminator.parent = self
                            self._children_name_map["ipv4_discriminator"] = "ipv4-discriminator"
                            self._children_yang_names.add("ipv4-discriminator")

                            self.ipv4_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels()
                            self.ipv4_severity_levels.parent = self
                            self._children_name_map["ipv4_severity_levels"] = "ipv4-severity-levels"
                            self._children_yang_names.add("ipv4-severity-levels")

                            self.ipv4_severity_port = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort()
                            self.ipv4_severity_port.parent = self
                            self._children_name_map["ipv4_severity_port"] = "ipv4-severity-port"
                            self._children_yang_names.add("ipv4-severity-port")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4, self).__setattr__(name, value)


                        class Ipv4SeverityLevels(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels, self).__init__()

                                self.yang_name = "ipv4-severity-levels"
                                self.yang_parent_name = "ipv4"

                                self.ipv4_severity_level = YList(self)

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
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels, self).__setattr__(name, value)


                            class Ipv4SeverityLevel(Entity):
                                """
                                Severity for the logging host
                                
                                .. attribute:: severity  <key>
                                
                                	Severity for the logging host
                                	**type**\:   :py:class:`LogSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogSeverity>`
                                
                                

                                """

                                _prefix = 'infra-syslog-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel, self).__init__()

                                    self.yang_name = "ipv4-severity-level"
                                    self.yang_parent_name = "ipv4-severity-levels"

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
                                        if name in ("severity") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.severity.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.severity.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv4-severity-level" + "[severity='" + self.severity.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
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
                                    if(name == "severity"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "severity"):
                                        self.severity = value
                                        self.severity.value_namespace = name_space
                                        self.severity.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.ipv4_severity_level:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.ipv4_severity_level:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-severity-levels" + path_buffer

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

                                if (child_yang_name == "ipv4-severity-level"):
                                    for c in self.ipv4_severity_level:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels.Ipv4SeverityLevel()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.ipv4_severity_level.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-severity-level"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Ipv4SeverityPort(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort, self).__init__()

                                self.yang_name = "ipv4-severity-port"
                                self.yang_parent_name = "ipv4"

                                self.port = YLeaf(YType.int32, "port")

                                self.severity = YLeaf(YType.int32, "severity")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("port",
                                                "severity") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.port.is_set or
                                    self.severity.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.port.yfilter != YFilter.not_set or
                                    self.severity.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-severity-port" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port.get_name_leafdata())
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
                                if(name == "port" or name == "severity"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "port"):
                                    self.port = value
                                    self.port.value_namespace = name_space
                                    self.port.value_namespace_prefix = name_space_prefix
                                if(value_path == "severity"):
                                    self.severity = value
                                    self.severity.value_namespace = name_space
                                    self.severity.value_namespace_prefix = name_space_prefix


                        class Ipv4Discriminator(Entity):
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
                                super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator, self).__init__()

                                self.yang_name = "ipv4-discriminator"
                                self.yang_parent_name = "ipv4"

                                self.match1 = YLeaf(YType.str, "match1")

                                self.match2 = YLeaf(YType.str, "match2")

                                self.match3 = YLeaf(YType.str, "match3")

                                self.nomatch1 = YLeaf(YType.str, "nomatch1")

                                self.nomatch2 = YLeaf(YType.str, "nomatch2")

                                self.nomatch3 = YLeaf(YType.str, "nomatch3")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("match1",
                                                "match2",
                                                "match3",
                                                "nomatch1",
                                                "nomatch2",
                                                "nomatch3") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.match1.is_set or
                                    self.match2.is_set or
                                    self.match3.is_set or
                                    self.nomatch1.is_set or
                                    self.nomatch2.is_set or
                                    self.nomatch3.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.match1.yfilter != YFilter.not_set or
                                    self.match2.yfilter != YFilter.not_set or
                                    self.match3.yfilter != YFilter.not_set or
                                    self.nomatch1.yfilter != YFilter.not_set or
                                    self.nomatch2.yfilter != YFilter.not_set or
                                    self.nomatch3.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-discriminator" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match1.get_name_leafdata())
                                if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match2.get_name_leafdata())
                                if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.match3.get_name_leafdata())
                                if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch1.get_name_leafdata())
                                if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch2.get_name_leafdata())
                                if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nomatch3.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "match1"):
                                    self.match1 = value
                                    self.match1.value_namespace = name_space
                                    self.match1.value_namespace_prefix = name_space_prefix
                                if(value_path == "match2"):
                                    self.match2 = value
                                    self.match2.value_namespace = name_space
                                    self.match2.value_namespace_prefix = name_space_prefix
                                if(value_path == "match3"):
                                    self.match3 = value
                                    self.match3.value_namespace = name_space
                                    self.match3.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch1"):
                                    self.nomatch1 = value
                                    self.nomatch1.value_namespace = name_space
                                    self.nomatch1.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch2"):
                                    self.nomatch2 = value
                                    self.nomatch2.value_namespace = name_space
                                    self.nomatch2.value_namespace_prefix = name_space_prefix
                                if(value_path == "nomatch3"):
                                    self.nomatch3 = value
                                    self.nomatch3.value_namespace = name_space
                                    self.nomatch3.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.address.is_set or
                                (self.ipv4_discriminator is not None and self.ipv4_discriminator.has_data()) or
                                (self.ipv4_severity_levels is not None and self.ipv4_severity_levels.has_data()) or
                                (self.ipv4_severity_port is not None and self.ipv4_severity_port.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                (self.ipv4_discriminator is not None and self.ipv4_discriminator.has_operation()) or
                                (self.ipv4_severity_levels is not None and self.ipv4_severity_levels.has_operation()) or
                                (self.ipv4_severity_port is not None and self.ipv4_severity_port.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4" + "[address='" + self.address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv4-discriminator"):
                                if (self.ipv4_discriminator is None):
                                    self.ipv4_discriminator = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4Discriminator()
                                    self.ipv4_discriminator.parent = self
                                    self._children_name_map["ipv4_discriminator"] = "ipv4-discriminator"
                                return self.ipv4_discriminator

                            if (child_yang_name == "ipv4-severity-levels"):
                                if (self.ipv4_severity_levels is None):
                                    self.ipv4_severity_levels = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityLevels()
                                    self.ipv4_severity_levels.parent = self
                                    self._children_name_map["ipv4_severity_levels"] = "ipv4-severity-levels"
                                return self.ipv4_severity_levels

                            if (child_yang_name == "ipv4-severity-port"):
                                if (self.ipv4_severity_port is None):
                                    self.ipv4_severity_port = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4.Ipv4SeverityPort()
                                    self.ipv4_severity_port.parent = self
                                    self._children_name_map["ipv4_severity_port"] = "ipv4-severity-port"
                                return self.ipv4_severity_port

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-discriminator" or name == "ipv4-severity-levels" or name == "ipv4-severity-port" or name == "address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ipv4:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ipv4:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4s" + path_buffer

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

                        if (child_yang_name == "ipv4"):
                            for c in self.ipv4:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Syslog.HostServer.Vrfs.Vrf.Ipv4S.Ipv4()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ipv4.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        (self.hosts is not None and self.hosts.has_data()) or
                        (self.ipv4s is not None and self.ipv4s.has_data()) or
                        (self.ipv6s is not None and self.ipv6s.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        (self.hosts is not None and self.hosts.has_operation()) or
                        (self.ipv4s is not None and self.ipv4s.has_operation()) or
                        (self.ipv6s is not None and self.ipv6s.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/host-server/vrfs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "hosts"):
                        if (self.hosts is None):
                            self.hosts = Syslog.HostServer.Vrfs.Vrf.Hosts()
                            self.hosts.parent = self
                            self._children_name_map["hosts"] = "hosts"
                        return self.hosts

                    if (child_yang_name == "ipv4s"):
                        if (self.ipv4s is None):
                            self.ipv4s = Syslog.HostServer.Vrfs.Vrf.Ipv4S()
                            self.ipv4s.parent = self
                            self._children_name_map["ipv4s"] = "ipv4s"
                        return self.ipv4s

                    if (child_yang_name == "ipv6s"):
                        if (self.ipv6s is None):
                            self.ipv6s = Syslog.HostServer.Vrfs.Vrf.Ipv6S()
                            self.ipv6s.parent = self
                            self._children_name_map["ipv6s"] = "ipv6s"
                        return self.ipv6s

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hosts" or name == "ipv4s" or name == "ipv6s" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.vrf:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.vrf:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrfs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/host-server/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "vrf"):
                    for c in self.vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Syslog.HostServer.Vrfs.Vrf()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.vrf.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.vrfs is not None and self.vrfs.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.vrfs is not None and self.vrfs.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "host-server" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrfs"):
                if (self.vrfs is None):
                    self.vrfs = Syslog.HostServer.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                return self.vrfs

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrfs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class ConsoleLogging(Entity):
        """
        Set console logging
        
        .. attribute:: console_discriminator
        
        	Set console logging discriminators
        	**type**\:   :py:class:`ConsoleDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.ConsoleLogging.ConsoleDiscriminator>`
        
        .. attribute:: logging_level
        
        	Console logging level
        	**type**\:   :py:class:`LoggingLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingLevels>`
        
        	**default value**\: warning
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.ConsoleLogging, self).__init__()

            self.yang_name = "console-logging"
            self.yang_parent_name = "syslog"

            self.logging_level = YLeaf(YType.enumeration, "logging-level")

            self.console_discriminator = Syslog.ConsoleLogging.ConsoleDiscriminator()
            self.console_discriminator.parent = self
            self._children_name_map["console_discriminator"] = "console-discriminator"
            self._children_yang_names.add("console-discriminator")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("logging_level") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.ConsoleLogging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.ConsoleLogging, self).__setattr__(name, value)


        class ConsoleDiscriminator(Entity):
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
                super(Syslog.ConsoleLogging.ConsoleDiscriminator, self).__init__()

                self.yang_name = "console-discriminator"
                self.yang_parent_name = "console-logging"

                self.match1 = YLeaf(YType.str, "match1")

                self.match2 = YLeaf(YType.str, "match2")

                self.match3 = YLeaf(YType.str, "match3")

                self.nomatch1 = YLeaf(YType.str, "nomatch1")

                self.nomatch2 = YLeaf(YType.str, "nomatch2")

                self.nomatch3 = YLeaf(YType.str, "nomatch3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("match1",
                                "match2",
                                "match3",
                                "nomatch1",
                                "nomatch2",
                                "nomatch3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.ConsoleLogging.ConsoleDiscriminator, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.ConsoleLogging.ConsoleDiscriminator, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.match1.is_set or
                    self.match2.is_set or
                    self.match3.is_set or
                    self.nomatch1.is_set or
                    self.nomatch2.is_set or
                    self.nomatch3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.match1.yfilter != YFilter.not_set or
                    self.match2.yfilter != YFilter.not_set or
                    self.match3.yfilter != YFilter.not_set or
                    self.nomatch1.yfilter != YFilter.not_set or
                    self.nomatch2.yfilter != YFilter.not_set or
                    self.nomatch3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "console-discriminator" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/console-logging/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match1.get_name_leafdata())
                if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match2.get_name_leafdata())
                if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.match3.get_name_leafdata())
                if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch1.get_name_leafdata())
                if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch2.get_name_leafdata())
                if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nomatch3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "match1"):
                    self.match1 = value
                    self.match1.value_namespace = name_space
                    self.match1.value_namespace_prefix = name_space_prefix
                if(value_path == "match2"):
                    self.match2 = value
                    self.match2.value_namespace = name_space
                    self.match2.value_namespace_prefix = name_space_prefix
                if(value_path == "match3"):
                    self.match3 = value
                    self.match3.value_namespace = name_space
                    self.match3.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch1"):
                    self.nomatch1 = value
                    self.nomatch1.value_namespace = name_space
                    self.nomatch1.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch2"):
                    self.nomatch2 = value
                    self.nomatch2.value_namespace = name_space
                    self.nomatch2.value_namespace_prefix = name_space_prefix
                if(value_path == "nomatch3"):
                    self.nomatch3 = value
                    self.nomatch3.value_namespace = name_space
                    self.nomatch3.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.logging_level.is_set or
                (self.console_discriminator is not None and self.console_discriminator.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.logging_level.yfilter != YFilter.not_set or
                (self.console_discriminator is not None and self.console_discriminator.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "console-logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.logging_level.is_set or self.logging_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.logging_level.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "console-discriminator"):
                if (self.console_discriminator is None):
                    self.console_discriminator = Syslog.ConsoleLogging.ConsoleDiscriminator()
                    self.console_discriminator.parent = self
                    self._children_name_map["console_discriminator"] = "console-discriminator"
                return self.console_discriminator

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "console-discriminator" or name == "logging-level"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "logging-level"):
                self.logging_level = value
                self.logging_level.value_namespace = name_space
                self.logging_level.value_namespace_prefix = name_space_prefix


    class Files(Entity):
        """
        Configure logging file destination
        
        .. attribute:: file
        
        	Specify File Name
        	**type**\: list of    :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Files.File>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.Files, self).__init__()

            self.yang_name = "files"
            self.yang_parent_name = "syslog"

            self.file = YList(self)

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
                        super(Syslog.Files, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.Files, self).__setattr__(name, value)


        class File(Entity):
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
                super(Syslog.Files.File, self).__init__()

                self.yang_name = "file"
                self.yang_parent_name = "files"

                self.file_name = YLeaf(YType.str, "file-name")

                self.file_log_attributes = Syslog.Files.File.FileLogAttributes()
                self.file_log_attributes.parent = self
                self._children_name_map["file_log_attributes"] = "file-log-attributes"
                self._children_yang_names.add("file-log-attributes")

                self.file_log_discriminator = Syslog.Files.File.FileLogDiscriminator()
                self.file_log_discriminator.parent = self
                self._children_name_map["file_log_discriminator"] = "file-log-discriminator"
                self._children_yang_names.add("file-log-discriminator")

                self.file_specification = Syslog.Files.File.FileSpecification()
                self.file_specification.parent = self
                self._children_name_map["file_specification"] = "file-specification"
                self._children_yang_names.add("file-specification")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("file_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Files.File, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Files.File, self).__setattr__(name, value)


            class FileSpecification(Entity):
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
                    super(Syslog.Files.File.FileSpecification, self).__init__()

                    self.yang_name = "file-specification"
                    self.yang_parent_name = "file"

                    self.max_file_size = YLeaf(YType.int32, "max-file-size")

                    self.path = YLeaf(YType.str, "path")

                    self.severity = YLeaf(YType.int32, "severity")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("max_file_size",
                                    "path",
                                    "severity") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.Files.File.FileSpecification, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.Files.File.FileSpecification, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.max_file_size.is_set or
                        self.path.is_set or
                        self.severity.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.max_file_size.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        self.severity.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file-specification" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.max_file_size.is_set or self.max_file_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_file_size.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())
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
                    if(name == "max-file-size" or name == "path" or name == "severity"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "max-file-size"):
                        self.max_file_size = value
                        self.max_file_size.value_namespace = name_space
                        self.max_file_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix
                    if(value_path == "severity"):
                        self.severity = value
                        self.severity.value_namespace = name_space
                        self.severity.value_namespace_prefix = name_space_prefix


            class FileLogAttributes(Entity):
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
                    super(Syslog.Files.File.FileLogAttributes, self).__init__()

                    self.yang_name = "file-log-attributes"
                    self.yang_parent_name = "file"

                    self.max_file_size = YLeaf(YType.int32, "max-file-size")

                    self.severity = YLeaf(YType.int32, "severity")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("max_file_size",
                                    "severity") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.Files.File.FileLogAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.Files.File.FileLogAttributes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.max_file_size.is_set or
                        self.severity.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.max_file_size.yfilter != YFilter.not_set or
                        self.severity.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file-log-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.max_file_size.is_set or self.max_file_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_file_size.get_name_leafdata())
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
                    if(name == "max-file-size" or name == "severity"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "max-file-size"):
                        self.max_file_size = value
                        self.max_file_size.value_namespace = name_space
                        self.max_file_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "severity"):
                        self.severity = value
                        self.severity.value_namespace = name_space
                        self.severity.value_namespace_prefix = name_space_prefix


            class FileLogDiscriminator(Entity):
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
                    super(Syslog.Files.File.FileLogDiscriminator, self).__init__()

                    self.yang_name = "file-log-discriminator"
                    self.yang_parent_name = "file"

                    self.match1 = YLeaf(YType.str, "match1")

                    self.match2 = YLeaf(YType.str, "match2")

                    self.match3 = YLeaf(YType.str, "match3")

                    self.nomatch1 = YLeaf(YType.str, "nomatch1")

                    self.nomatch2 = YLeaf(YType.str, "nomatch2")

                    self.nomatch3 = YLeaf(YType.str, "nomatch3")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("match1",
                                    "match2",
                                    "match3",
                                    "nomatch1",
                                    "nomatch2",
                                    "nomatch3") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.Files.File.FileLogDiscriminator, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.Files.File.FileLogDiscriminator, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.match1.is_set or
                        self.match2.is_set or
                        self.match3.is_set or
                        self.nomatch1.is_set or
                        self.nomatch2.is_set or
                        self.nomatch3.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.match1.yfilter != YFilter.not_set or
                        self.match2.yfilter != YFilter.not_set or
                        self.match3.yfilter != YFilter.not_set or
                        self.nomatch1.yfilter != YFilter.not_set or
                        self.nomatch2.yfilter != YFilter.not_set or
                        self.nomatch3.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "file-log-discriminator" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.match1.is_set or self.match1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.match1.get_name_leafdata())
                    if (self.match2.is_set or self.match2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.match2.get_name_leafdata())
                    if (self.match3.is_set or self.match3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.match3.get_name_leafdata())
                    if (self.nomatch1.is_set or self.nomatch1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nomatch1.get_name_leafdata())
                    if (self.nomatch2.is_set or self.nomatch2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nomatch2.get_name_leafdata())
                    if (self.nomatch3.is_set or self.nomatch3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nomatch3.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "match1" or name == "match2" or name == "match3" or name == "nomatch1" or name == "nomatch2" or name == "nomatch3"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "match1"):
                        self.match1 = value
                        self.match1.value_namespace = name_space
                        self.match1.value_namespace_prefix = name_space_prefix
                    if(value_path == "match2"):
                        self.match2 = value
                        self.match2.value_namespace = name_space
                        self.match2.value_namespace_prefix = name_space_prefix
                    if(value_path == "match3"):
                        self.match3 = value
                        self.match3.value_namespace = name_space
                        self.match3.value_namespace_prefix = name_space_prefix
                    if(value_path == "nomatch1"):
                        self.nomatch1 = value
                        self.nomatch1.value_namespace = name_space
                        self.nomatch1.value_namespace_prefix = name_space_prefix
                    if(value_path == "nomatch2"):
                        self.nomatch2 = value
                        self.nomatch2.value_namespace = name_space
                        self.nomatch2.value_namespace_prefix = name_space_prefix
                    if(value_path == "nomatch3"):
                        self.nomatch3 = value
                        self.nomatch3.value_namespace = name_space
                        self.nomatch3.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.file_name.is_set or
                    (self.file_log_attributes is not None and self.file_log_attributes.has_data()) or
                    (self.file_log_discriminator is not None and self.file_log_discriminator.has_data()) or
                    (self.file_specification is not None and self.file_specification.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.file_name.yfilter != YFilter.not_set or
                    (self.file_log_attributes is not None and self.file_log_attributes.has_operation()) or
                    (self.file_log_discriminator is not None and self.file_log_discriminator.has_operation()) or
                    (self.file_specification is not None and self.file_specification.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "file" + "[file-name='" + self.file_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/files/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.file_name.is_set or self.file_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.file_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "file-log-attributes"):
                    if (self.file_log_attributes is None):
                        self.file_log_attributes = Syslog.Files.File.FileLogAttributes()
                        self.file_log_attributes.parent = self
                        self._children_name_map["file_log_attributes"] = "file-log-attributes"
                    return self.file_log_attributes

                if (child_yang_name == "file-log-discriminator"):
                    if (self.file_log_discriminator is None):
                        self.file_log_discriminator = Syslog.Files.File.FileLogDiscriminator()
                        self.file_log_discriminator.parent = self
                        self._children_name_map["file_log_discriminator"] = "file-log-discriminator"
                    return self.file_log_discriminator

                if (child_yang_name == "file-specification"):
                    if (self.file_specification is None):
                        self.file_specification = Syslog.Files.File.FileSpecification()
                        self.file_specification.parent = self
                        self._children_name_map["file_specification"] = "file-specification"
                    return self.file_specification

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file-log-attributes" or name == "file-log-discriminator" or name == "file-specification" or name == "file-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "file-name"):
                    self.file_name = value
                    self.file_name.value_namespace = name_space
                    self.file_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.file:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.file:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "files" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "file"):
                for c in self.file:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.Files.File()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.file.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "file"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv4(Entity):
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
            super(Syslog.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "syslog"

            self.dscp = None
            self._children_name_map["dscp"] = "dscp"
            self._children_yang_names.add("dscp")

            self.precedence = None
            self._children_name_map["precedence"] = "precedence"
            self._children_yang_names.add("precedence")

            self.tos = Syslog.Ipv4.Tos()
            self.tos.parent = self
            self._children_name_map["tos"] = "tos"
            self._children_yang_names.add("tos")


        class Dscp(Entity):
            """
            DSCP value
            
            .. attribute:: type
            
            	Logging TOS type DSCP
            	**type**\:   :py:class:`LoggingDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscp>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            	**mandatory**\: True
            
            
            ----
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.Ipv4.Dscp, self).__init__()

                self.yang_name = "dscp"
                self.yang_parent_name = "ipv4"
                self.is_presence_container = True

                self.type = YLeaf(YType.enumeration, "type")

                self.unused = YLeaf(YType.str, "unused")

                self.value = YLeaf(YType.str, "value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "unused",
                                "value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Ipv4.Dscp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Ipv4.Dscp, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.unused.is_set or
                    self.value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.unused.yfilter != YFilter.not_set or
                    self.value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dscp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.unused.is_set or self.unused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unused.get_name_leafdata())
                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "unused" or name == "value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "unused"):
                    self.unused = value
                    self.unused.value_namespace = name_space
                    self.unused.value_namespace_prefix = name_space_prefix
                if(value_path == "value"):
                    self.value = value
                    self.value.value_namespace = name_space
                    self.value.value_namespace_prefix = name_space_prefix


        class Tos(Entity):
            """
            Type of service
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\:   :py:class:`LoggingTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingTos>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.Ipv4.Tos, self).__init__()

                self.yang_name = "tos"
                self.yang_parent_name = "ipv4"

                self.dscp = YLeaf(YType.str, "dscp")

                self.precedence = YLeaf(YType.str, "precedence")

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
                    if name in ("dscp",
                                "precedence",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Ipv4.Tos, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Ipv4.Tos, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dscp.is_set or
                    self.precedence.is_set or
                    self.type.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set or
                    self.precedence.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tos" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())
                if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.precedence.get_name_leafdata())
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
                if(name == "dscp" or name == "precedence" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix
                if(value_path == "precedence"):
                    self.precedence = value
                    self.precedence.value_namespace = name_space
                    self.precedence.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix


        class Precedence(Entity):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\:   :py:class:`LoggingPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedence>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            
            ----
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.Ipv4.Precedence, self).__init__()

                self.yang_name = "precedence"
                self.yang_parent_name = "ipv4"
                self.is_presence_container = True

                self.type = YLeaf(YType.enumeration, "type")

                self.unused = YLeaf(YType.str, "unused")

                self.value = YLeaf(YType.str, "value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "unused",
                                "value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Ipv4.Precedence, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Ipv4.Precedence, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.unused.is_set or
                    self.value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.unused.yfilter != YFilter.not_set or
                    self.value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "precedence" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.unused.is_set or self.unused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unused.get_name_leafdata())
                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "unused" or name == "value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "unused"):
                    self.unused = value
                    self.unused.value_namespace = name_space
                    self.unused.value_namespace_prefix = name_space_prefix
                if(value_path == "value"):
                    self.value = value
                    self.value.value_namespace = name_space
                    self.value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.tos is not None and self.tos.has_data()) or
                (self.dscp is not None) or
                (self.precedence is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.dscp is not None and self.dscp.has_operation()) or
                (self.precedence is not None and self.precedence.has_operation()) or
                (self.tos is not None and self.tos.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv4" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dscp"):
                if (self.dscp is None):
                    self.dscp = Syslog.Ipv4.Dscp()
                    self.dscp.parent = self
                    self._children_name_map["dscp"] = "dscp"
                return self.dscp

            if (child_yang_name == "precedence"):
                if (self.precedence is None):
                    self.precedence = Syslog.Ipv4.Precedence()
                    self.precedence.parent = self
                    self._children_name_map["precedence"] = "precedence"
                return self.precedence

            if (child_yang_name == "tos"):
                if (self.tos is None):
                    self.tos = Syslog.Ipv4.Tos()
                    self.tos.parent = self
                    self._children_name_map["tos"] = "tos"
                return self.tos

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dscp" or name == "precedence" or name == "tos"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Archive(Entity):
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
        	**type**\:   :py:class:`LogCollectFrequency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogCollectFrequency>`
        
        .. attribute:: length
        
        	The maximum number of weeks of log to maintain
        	**type**\:  int
        
        	**range:** 1..256
        
        .. attribute:: severity
        
        	The minimum severity of log messages to archive
        	**type**\:   :py:class:`LogMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LogMessageSeverity>`
        
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
            super(Syslog.Archive, self).__init__()

            self.yang_name = "archive"
            self.yang_parent_name = "syslog"

            self.device = YLeaf(YType.str, "device")

            self.file_size = YLeaf(YType.uint32, "file-size")

            self.frequency = YLeaf(YType.enumeration, "frequency")

            self.length = YLeaf(YType.uint32, "length")

            self.severity = YLeaf(YType.enumeration, "severity")

            self.size = YLeaf(YType.uint32, "size")

            self.threshold = YLeaf(YType.uint32, "threshold")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("device",
                            "file_size",
                            "frequency",
                            "length",
                            "severity",
                            "size",
                            "threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.Archive, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.Archive, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.device.is_set or
                self.file_size.is_set or
                self.frequency.is_set or
                self.length.is_set or
                self.severity.is_set or
                self.size.is_set or
                self.threshold.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.device.yfilter != YFilter.not_set or
                self.file_size.yfilter != YFilter.not_set or
                self.frequency.yfilter != YFilter.not_set or
                self.length.yfilter != YFilter.not_set or
                self.severity.yfilter != YFilter.not_set or
                self.size.yfilter != YFilter.not_set or
                self.threshold.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "archive" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.device.is_set or self.device.yfilter != YFilter.not_set):
                leaf_name_data.append(self.device.get_name_leafdata())
            if (self.file_size.is_set or self.file_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.file_size.get_name_leafdata())
            if (self.frequency.is_set or self.frequency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.frequency.get_name_leafdata())
            if (self.length.is_set or self.length.yfilter != YFilter.not_set):
                leaf_name_data.append(self.length.get_name_leafdata())
            if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                leaf_name_data.append(self.severity.get_name_leafdata())
            if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.size.get_name_leafdata())
            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "device" or name == "file-size" or name == "frequency" or name == "length" or name == "severity" or name == "size" or name == "threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "device"):
                self.device = value
                self.device.value_namespace = name_space
                self.device.value_namespace_prefix = name_space_prefix
            if(value_path == "file-size"):
                self.file_size = value
                self.file_size.value_namespace = name_space
                self.file_size.value_namespace_prefix = name_space_prefix
            if(value_path == "frequency"):
                self.frequency = value
                self.frequency.value_namespace = name_space
                self.frequency.value_namespace_prefix = name_space_prefix
            if(value_path == "length"):
                self.length = value
                self.length.value_namespace = name_space
                self.length.value_namespace_prefix = name_space_prefix
            if(value_path == "severity"):
                self.severity = value
                self.severity.value_namespace = name_space
                self.severity.value_namespace_prefix = name_space_prefix
            if(value_path == "size"):
                self.size = value
                self.size.value_namespace = name_space
                self.size.value_namespace_prefix = name_space_prefix
            if(value_path == "threshold"):
                self.threshold = value
                self.threshold.value_namespace = name_space
                self.threshold.value_namespace_prefix = name_space_prefix


    class Ipv6(Entity):
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
            super(Syslog.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "syslog"

            self.dscp = None
            self._children_name_map["dscp"] = "dscp"
            self._children_yang_names.add("dscp")

            self.precedence = None
            self._children_name_map["precedence"] = "precedence"
            self._children_yang_names.add("precedence")

            self.traffic_class = Syslog.Ipv6.TrafficClass()
            self.traffic_class.parent = self
            self._children_name_map["traffic_class"] = "traffic-class"
            self._children_yang_names.add("traffic-class")


        class Dscp(Entity):
            """
            DSCP value
            
            .. attribute:: type
            
            	Logging TOS type DSCP
            	**type**\:   :py:class:`LoggingDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscp>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: value
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            	**mandatory**\: True
            
            
            ----
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.Ipv6.Dscp, self).__init__()

                self.yang_name = "dscp"
                self.yang_parent_name = "ipv6"
                self.is_presence_container = True

                self.type = YLeaf(YType.enumeration, "type")

                self.unused = YLeaf(YType.str, "unused")

                self.value = YLeaf(YType.str, "value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "unused",
                                "value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Ipv6.Dscp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Ipv6.Dscp, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.unused.is_set or
                    self.value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.unused.yfilter != YFilter.not_set or
                    self.value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dscp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.unused.is_set or self.unused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unused.get_name_leafdata())
                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "unused" or name == "value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "unused"):
                    self.unused = value
                    self.unused.value_namespace = name_space
                    self.unused.value_namespace_prefix = name_space_prefix
                if(value_path == "value"):
                    self.value = value
                    self.value.value_namespace = name_space
                    self.value.value_namespace_prefix = name_space_prefix


        class TrafficClass(Entity):
            """
            Type of traffic class
            
            .. attribute:: dscp
            
            	Logging DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	Logging TOS type DSCP or precedence
            	**type**\:   :py:class:`LoggingTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingTos>`
            
            

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.Ipv6.TrafficClass, self).__init__()

                self.yang_name = "traffic-class"
                self.yang_parent_name = "ipv6"

                self.dscp = YLeaf(YType.str, "dscp")

                self.precedence = YLeaf(YType.str, "precedence")

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
                    if name in ("dscp",
                                "precedence",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Ipv6.TrafficClass, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Ipv6.TrafficClass, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dscp.is_set or
                    self.precedence.is_set or
                    self.type.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set or
                    self.precedence.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "traffic-class" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())
                if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.precedence.get_name_leafdata())
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
                if(name == "dscp" or name == "precedence" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix
                if(value_path == "precedence"):
                    self.precedence = value
                    self.precedence.value_namespace = name_space
                    self.precedence.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix


        class Precedence(Entity):
            """
            Precedence value
            
            .. attribute:: type
            
            	Logging TOS type precedence
            	**type**\:   :py:class:`LoggingPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedence>`
            
            	**mandatory**\: True
            
            .. attribute:: unused
            
            	Unused
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: value
            
            	Logging precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`LoggingPrecedenceValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.LoggingPrecedenceValue>`
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            
            ----
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-syslog-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(Syslog.Ipv6.Precedence, self).__init__()

                self.yang_name = "precedence"
                self.yang_parent_name = "ipv6"
                self.is_presence_container = True

                self.type = YLeaf(YType.enumeration, "type")

                self.unused = YLeaf(YType.str, "unused")

                self.value = YLeaf(YType.str, "value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "unused",
                                "value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Ipv6.Precedence, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Ipv6.Precedence, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.type.is_set or
                    self.unused.is_set or
                    self.value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.unused.yfilter != YFilter.not_set or
                    self.value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "precedence" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.unused.is_set or self.unused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unused.get_name_leafdata())
                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "type" or name == "unused" or name == "value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "unused"):
                    self.unused = value
                    self.unused.value_namespace = name_space
                    self.unused.value_namespace_prefix = name_space_prefix
                if(value_path == "value"):
                    self.value = value
                    self.value.value_namespace = name_space
                    self.value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.traffic_class is not None and self.traffic_class.has_data()) or
                (self.dscp is not None) or
                (self.precedence is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.dscp is not None and self.dscp.has_operation()) or
                (self.precedence is not None and self.precedence.has_operation()) or
                (self.traffic_class is not None and self.traffic_class.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dscp"):
                if (self.dscp is None):
                    self.dscp = Syslog.Ipv6.Dscp()
                    self.dscp.parent = self
                    self._children_name_map["dscp"] = "dscp"
                return self.dscp

            if (child_yang_name == "precedence"):
                if (self.precedence is None):
                    self.precedence = Syslog.Ipv6.Precedence()
                    self.precedence.parent = self
                    self._children_name_map["precedence"] = "precedence"
                return self.precedence

            if (child_yang_name == "traffic-class"):
                if (self.traffic_class is None):
                    self.traffic_class = Syslog.Ipv6.TrafficClass()
                    self.traffic_class.parent = self
                    self._children_name_map["traffic_class"] = "traffic-class"
                return self.traffic_class

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dscp" or name == "precedence" or name == "traffic-class"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SourceInterfaceTable(Entity):
        """
        Configure source interface
        
        .. attribute:: source_interface_values
        
        	Specify interface for source address in logging transactions
        	**type**\:   :py:class:`SourceInterfaceValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues>`
        
        

        """

        _prefix = 'infra-syslog-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(Syslog.SourceInterfaceTable, self).__init__()

            self.yang_name = "source-interface-table"
            self.yang_parent_name = "syslog"

            self.source_interface_values = Syslog.SourceInterfaceTable.SourceInterfaceValues()
            self.source_interface_values.parent = self
            self._children_name_map["source_interface_values"] = "source-interface-values"
            self._children_yang_names.add("source-interface-values")


        class SourceInterfaceValues(Entity):
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
                super(Syslog.SourceInterfaceTable.SourceInterfaceValues, self).__init__()

                self.yang_name = "source-interface-values"
                self.yang_parent_name = "source-interface-table"

                self.source_interface_value = YList(self)

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
                            super(Syslog.SourceInterfaceTable.SourceInterfaceValues, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.SourceInterfaceTable.SourceInterfaceValues, self).__setattr__(name, value)


            class SourceInterfaceValue(Entity):
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
                    super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue, self).__init__()

                    self.yang_name = "source-interface-value"
                    self.yang_parent_name = "source-interface-values"

                    self.src_interface_name_value = YLeaf(YType.str, "src-interface-name-value")

                    self.source_interface_vrfs = Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs()
                    self.source_interface_vrfs.parent = self
                    self._children_name_map["source_interface_vrfs"] = "source-interface-vrfs"
                    self._children_yang_names.add("source-interface-vrfs")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("src_interface_name_value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue, self).__setattr__(name, value)


                class SourceInterfaceVrfs(Entity):
                    """
                    Configure source interface VRF
                    
                    .. attribute:: source_interface_vrf
                    
                    	Specify VRF for source interface
                    	**type**\: list of    :py:class:`SourceInterfaceVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf>`
                    
                    

                    """

                    _prefix = 'infra-syslog-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs, self).__init__()

                        self.yang_name = "source-interface-vrfs"
                        self.yang_parent_name = "source-interface-value"

                        self.source_interface_vrf = YList(self)

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
                                    super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs, self).__setattr__(name, value)


                    class SourceInterfaceVrf(Entity):
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
                            super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf, self).__init__()

                            self.yang_name = "source-interface-vrf"
                            self.yang_parent_name = "source-interface-vrfs"

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf, self).__setattr__(name, value)

                        def has_data(self):
                            return self.vrf_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "source-interface-vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.source_interface_vrf:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.source_interface_vrf:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "source-interface-vrfs" + path_buffer

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

                        if (child_yang_name == "source-interface-vrf"):
                            for c in self.source_interface_vrf:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs.SourceInterfaceVrf()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.source_interface_vrf.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "source-interface-vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.src_interface_name_value.is_set or
                        (self.source_interface_vrfs is not None and self.source_interface_vrfs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.src_interface_name_value.yfilter != YFilter.not_set or
                        (self.source_interface_vrfs is not None and self.source_interface_vrfs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "source-interface-value" + "[src-interface-name-value='" + self.src_interface_name_value.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/source-interface-table/source-interface-values/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.src_interface_name_value.is_set or self.src_interface_name_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.src_interface_name_value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "source-interface-vrfs"):
                        if (self.source_interface_vrfs is None):
                            self.source_interface_vrfs = Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue.SourceInterfaceVrfs()
                            self.source_interface_vrfs.parent = self
                            self._children_name_map["source_interface_vrfs"] = "source-interface-vrfs"
                        return self.source_interface_vrfs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-interface-vrfs" or name == "src-interface-name-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "src-interface-name-value"):
                        self.src_interface_name_value = value
                        self.src_interface_name_value.value_namespace = name_space
                        self.src_interface_name_value.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.source_interface_value:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.source_interface_value:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source-interface-values" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/source-interface-table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "source-interface-value"):
                    for c in self.source_interface_value:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Syslog.SourceInterfaceTable.SourceInterfaceValues.SourceInterfaceValue()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.source_interface_value.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "source-interface-value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.source_interface_values is not None and self.source_interface_values.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.source_interface_values is not None and self.source_interface_values.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "source-interface-table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "source-interface-values"):
                if (self.source_interface_values is None):
                    self.source_interface_values = Syslog.SourceInterfaceTable.SourceInterfaceValues()
                    self.source_interface_values.parent = self
                    self._children_name_map["source_interface_values"] = "source-interface-values"
                return self.source_interface_values

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "source-interface-values"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AlarmLogger(Entity):
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
        	**type**\:   :py:class:`AlarmLoggerSeverityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes.AlarmLoggerSeverityLevel>`
        
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
            super(Syslog.AlarmLogger, self).__init__()

            self.yang_name = "alarm-logger"
            self.yang_parent_name = "syslog"

            self.buffer_size = YLeaf(YType.uint32, "buffer-size")

            self.severity_level = YLeaf(YType.enumeration, "severity-level")

            self.source_location = YLeaf(YType.empty, "source-location")

            self.threshold = YLeaf(YType.uint32, "threshold")

            self.alarm_filter_strings = Syslog.AlarmLogger.AlarmFilterStrings()
            self.alarm_filter_strings.parent = self
            self._children_name_map["alarm_filter_strings"] = "alarm-filter-strings"
            self._children_yang_names.add("alarm-filter-strings")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("buffer_size",
                            "severity_level",
                            "source_location",
                            "threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.AlarmLogger, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.AlarmLogger, self).__setattr__(name, value)


        class AlarmFilterStrings(Entity):
            """
            List of filter strings
            
            .. attribute:: alarm_filter_string
            
            	Match string to filter alarms
            	**type**\: list of    :py:class:`AlarmFilterString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString>`
            
            

            """

            _prefix = 'infra-alarm-logger-cfg'
            _revision = '2016-08-10'

            def __init__(self):
                super(Syslog.AlarmLogger.AlarmFilterStrings, self).__init__()

                self.yang_name = "alarm-filter-strings"
                self.yang_parent_name = "alarm-logger"

                self.alarm_filter_string = YList(self)

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
                            super(Syslog.AlarmLogger.AlarmFilterStrings, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.AlarmLogger.AlarmFilterStrings, self).__setattr__(name, value)


            class AlarmFilterString(Entity):
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
                    super(Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString, self).__init__()

                    self.yang_name = "alarm-filter-string"
                    self.yang_parent_name = "alarm-filter-strings"

                    self.filter_string = YLeaf(YType.str, "filter-string")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("filter_string") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString, self).__setattr__(name, value)

                def has_data(self):
                    return self.filter_string.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.filter_string.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "alarm-filter-string" + "[filter-string='" + self.filter_string.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger/alarm-filter-strings/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.filter_string.is_set or self.filter_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.filter_string.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "filter-string"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "filter-string"):
                        self.filter_string = value
                        self.filter_string.value_namespace = name_space
                        self.filter_string.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.alarm_filter_string:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.alarm_filter_string:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "alarm-filter-strings" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "alarm-filter-string"):
                    for c in self.alarm_filter_string:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Syslog.AlarmLogger.AlarmFilterStrings.AlarmFilterString()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.alarm_filter_string.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "alarm-filter-string"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.buffer_size.is_set or
                self.severity_level.is_set or
                self.source_location.is_set or
                self.threshold.is_set or
                (self.alarm_filter_strings is not None and self.alarm_filter_strings.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.buffer_size.yfilter != YFilter.not_set or
                self.severity_level.yfilter != YFilter.not_set or
                self.source_location.yfilter != YFilter.not_set or
                self.threshold.yfilter != YFilter.not_set or
                (self.alarm_filter_strings is not None and self.alarm_filter_strings.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-infra-alarm-logger-cfg:alarm-logger" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.buffer_size.get_name_leafdata())
            if (self.severity_level.is_set or self.severity_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.severity_level.get_name_leafdata())
            if (self.source_location.is_set or self.source_location.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_location.get_name_leafdata())
            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "alarm-filter-strings"):
                if (self.alarm_filter_strings is None):
                    self.alarm_filter_strings = Syslog.AlarmLogger.AlarmFilterStrings()
                    self.alarm_filter_strings.parent = self
                    self._children_name_map["alarm_filter_strings"] = "alarm-filter-strings"
                return self.alarm_filter_strings

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "alarm-filter-strings" or name == "buffer-size" or name == "severity-level" or name == "source-location" or name == "threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "buffer-size"):
                self.buffer_size = value
                self.buffer_size.value_namespace = name_space
                self.buffer_size.value_namespace_prefix = name_space_prefix
            if(value_path == "severity-level"):
                self.severity_level = value
                self.severity_level.value_namespace = name_space
                self.severity_level.value_namespace_prefix = name_space_prefix
            if(value_path == "source-location"):
                self.source_location = value
                self.source_location.value_namespace = name_space
                self.source_location.value_namespace_prefix = name_space_prefix
            if(value_path == "threshold"):
                self.threshold = value
                self.threshold.value_namespace = name_space
                self.threshold.value_namespace_prefix = name_space_prefix


    class Correlator(Entity):
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
            super(Syslog.Correlator, self).__init__()

            self.yang_name = "correlator"
            self.yang_parent_name = "syslog"

            self.buffer_size = YLeaf(YType.uint32, "buffer-size")

            self.rule_sets = Syslog.Correlator.RuleSets()
            self.rule_sets.parent = self
            self._children_name_map["rule_sets"] = "rule-sets"
            self._children_yang_names.add("rule-sets")

            self.rules = Syslog.Correlator.Rules()
            self.rules.parent = self
            self._children_name_map["rules"] = "rules"
            self._children_yang_names.add("rules")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("buffer_size") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Syslog.Correlator, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.Correlator, self).__setattr__(name, value)


        class Rules(Entity):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Syslog.Correlator.Rules, self).__init__()

                self.yang_name = "rules"
                self.yang_parent_name = "correlator"

                self.rule = YList(self)

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
                            super(Syslog.Correlator.Rules, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Correlator.Rules, self).__setattr__(name, value)


            class Rule(Entity):
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
                    super(Syslog.Correlator.Rules.Rule, self).__init__()

                    self.yang_name = "rule"
                    self.yang_parent_name = "rules"

                    self.name = YLeaf(YType.str, "name")

                    self.applied_to = Syslog.Correlator.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._children_yang_names.add("applied-to")

                    self.apply_to = Syslog.Correlator.Rules.Rule.ApplyTo()
                    self.apply_to.parent = self
                    self._children_name_map["apply_to"] = "apply-to"
                    self._children_yang_names.add("apply-to")

                    self.definition = Syslog.Correlator.Rules.Rule.Definition()
                    self.definition.parent = self
                    self._children_name_map["definition"] = "definition"
                    self._children_yang_names.add("definition")

                    self.non_stateful = Syslog.Correlator.Rules.Rule.NonStateful()
                    self.non_stateful.parent = self
                    self._children_name_map["non_stateful"] = "non-stateful"
                    self._children_yang_names.add("non-stateful")

                    self.stateful = Syslog.Correlator.Rules.Rule.Stateful()
                    self.stateful.parent = self
                    self._children_name_map["stateful"] = "stateful"
                    self._children_yang_names.add("stateful")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.Correlator.Rules.Rule, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.Correlator.Rules.Rule, self).__setattr__(name, value)


                class Definition(Entity):
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
                        super(Syslog.Correlator.Rules.Rule.Definition, self).__init__()

                        self.yang_name = "definition"
                        self.yang_parent_name = "rule"

                        self.category_name_entry1 = YLeaf(YType.str, "category-name-entry1")

                        self.category_name_entry10 = YLeaf(YType.str, "category-name-entry10")

                        self.category_name_entry2 = YLeaf(YType.str, "category-name-entry2")

                        self.category_name_entry3 = YLeaf(YType.str, "category-name-entry3")

                        self.category_name_entry4 = YLeaf(YType.str, "category-name-entry4")

                        self.category_name_entry5 = YLeaf(YType.str, "category-name-entry5")

                        self.category_name_entry6 = YLeaf(YType.str, "category-name-entry6")

                        self.category_name_entry7 = YLeaf(YType.str, "category-name-entry7")

                        self.category_name_entry8 = YLeaf(YType.str, "category-name-entry8")

                        self.category_name_entry9 = YLeaf(YType.str, "category-name-entry9")

                        self.group_name_entry1 = YLeaf(YType.str, "group-name-entry1")

                        self.group_name_entry10 = YLeaf(YType.str, "group-name-entry10")

                        self.group_name_entry2 = YLeaf(YType.str, "group-name-entry2")

                        self.group_name_entry3 = YLeaf(YType.str, "group-name-entry3")

                        self.group_name_entry4 = YLeaf(YType.str, "group-name-entry4")

                        self.group_name_entry5 = YLeaf(YType.str, "group-name-entry5")

                        self.group_name_entry6 = YLeaf(YType.str, "group-name-entry6")

                        self.group_name_entry7 = YLeaf(YType.str, "group-name-entry7")

                        self.group_name_entry8 = YLeaf(YType.str, "group-name-entry8")

                        self.group_name_entry9 = YLeaf(YType.str, "group-name-entry9")

                        self.message_code_entry1 = YLeaf(YType.str, "message-code-entry1")

                        self.message_code_entry10 = YLeaf(YType.str, "message-code-entry10")

                        self.message_code_entry2 = YLeaf(YType.str, "message-code-entry2")

                        self.message_code_entry3 = YLeaf(YType.str, "message-code-entry3")

                        self.message_code_entry4 = YLeaf(YType.str, "message-code-entry4")

                        self.message_code_entry5 = YLeaf(YType.str, "message-code-entry5")

                        self.message_code_entry6 = YLeaf(YType.str, "message-code-entry6")

                        self.message_code_entry7 = YLeaf(YType.str, "message-code-entry7")

                        self.message_code_entry8 = YLeaf(YType.str, "message-code-entry8")

                        self.message_code_entry9 = YLeaf(YType.str, "message-code-entry9")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("category_name_entry1",
                                        "category_name_entry10",
                                        "category_name_entry2",
                                        "category_name_entry3",
                                        "category_name_entry4",
                                        "category_name_entry5",
                                        "category_name_entry6",
                                        "category_name_entry7",
                                        "category_name_entry8",
                                        "category_name_entry9",
                                        "group_name_entry1",
                                        "group_name_entry10",
                                        "group_name_entry2",
                                        "group_name_entry3",
                                        "group_name_entry4",
                                        "group_name_entry5",
                                        "group_name_entry6",
                                        "group_name_entry7",
                                        "group_name_entry8",
                                        "group_name_entry9",
                                        "message_code_entry1",
                                        "message_code_entry10",
                                        "message_code_entry2",
                                        "message_code_entry3",
                                        "message_code_entry4",
                                        "message_code_entry5",
                                        "message_code_entry6",
                                        "message_code_entry7",
                                        "message_code_entry8",
                                        "message_code_entry9",
                                        "timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Correlator.Rules.Rule.Definition, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.Rules.Rule.Definition, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.category_name_entry1.is_set or
                            self.category_name_entry10.is_set or
                            self.category_name_entry2.is_set or
                            self.category_name_entry3.is_set or
                            self.category_name_entry4.is_set or
                            self.category_name_entry5.is_set or
                            self.category_name_entry6.is_set or
                            self.category_name_entry7.is_set or
                            self.category_name_entry8.is_set or
                            self.category_name_entry9.is_set or
                            self.group_name_entry1.is_set or
                            self.group_name_entry10.is_set or
                            self.group_name_entry2.is_set or
                            self.group_name_entry3.is_set or
                            self.group_name_entry4.is_set or
                            self.group_name_entry5.is_set or
                            self.group_name_entry6.is_set or
                            self.group_name_entry7.is_set or
                            self.group_name_entry8.is_set or
                            self.group_name_entry9.is_set or
                            self.message_code_entry1.is_set or
                            self.message_code_entry10.is_set or
                            self.message_code_entry2.is_set or
                            self.message_code_entry3.is_set or
                            self.message_code_entry4.is_set or
                            self.message_code_entry5.is_set or
                            self.message_code_entry6.is_set or
                            self.message_code_entry7.is_set or
                            self.message_code_entry8.is_set or
                            self.message_code_entry9.is_set or
                            self.timeout.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.category_name_entry1.yfilter != YFilter.not_set or
                            self.category_name_entry10.yfilter != YFilter.not_set or
                            self.category_name_entry2.yfilter != YFilter.not_set or
                            self.category_name_entry3.yfilter != YFilter.not_set or
                            self.category_name_entry4.yfilter != YFilter.not_set or
                            self.category_name_entry5.yfilter != YFilter.not_set or
                            self.category_name_entry6.yfilter != YFilter.not_set or
                            self.category_name_entry7.yfilter != YFilter.not_set or
                            self.category_name_entry8.yfilter != YFilter.not_set or
                            self.category_name_entry9.yfilter != YFilter.not_set or
                            self.group_name_entry1.yfilter != YFilter.not_set or
                            self.group_name_entry10.yfilter != YFilter.not_set or
                            self.group_name_entry2.yfilter != YFilter.not_set or
                            self.group_name_entry3.yfilter != YFilter.not_set or
                            self.group_name_entry4.yfilter != YFilter.not_set or
                            self.group_name_entry5.yfilter != YFilter.not_set or
                            self.group_name_entry6.yfilter != YFilter.not_set or
                            self.group_name_entry7.yfilter != YFilter.not_set or
                            self.group_name_entry8.yfilter != YFilter.not_set or
                            self.group_name_entry9.yfilter != YFilter.not_set or
                            self.message_code_entry1.yfilter != YFilter.not_set or
                            self.message_code_entry10.yfilter != YFilter.not_set or
                            self.message_code_entry2.yfilter != YFilter.not_set or
                            self.message_code_entry3.yfilter != YFilter.not_set or
                            self.message_code_entry4.yfilter != YFilter.not_set or
                            self.message_code_entry5.yfilter != YFilter.not_set or
                            self.message_code_entry6.yfilter != YFilter.not_set or
                            self.message_code_entry7.yfilter != YFilter.not_set or
                            self.message_code_entry8.yfilter != YFilter.not_set or
                            self.message_code_entry9.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "definition" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.category_name_entry1.is_set or self.category_name_entry1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry1.get_name_leafdata())
                        if (self.category_name_entry10.is_set or self.category_name_entry10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry10.get_name_leafdata())
                        if (self.category_name_entry2.is_set or self.category_name_entry2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry2.get_name_leafdata())
                        if (self.category_name_entry3.is_set or self.category_name_entry3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry3.get_name_leafdata())
                        if (self.category_name_entry4.is_set or self.category_name_entry4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry4.get_name_leafdata())
                        if (self.category_name_entry5.is_set or self.category_name_entry5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry5.get_name_leafdata())
                        if (self.category_name_entry6.is_set or self.category_name_entry6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry6.get_name_leafdata())
                        if (self.category_name_entry7.is_set or self.category_name_entry7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry7.get_name_leafdata())
                        if (self.category_name_entry8.is_set or self.category_name_entry8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry8.get_name_leafdata())
                        if (self.category_name_entry9.is_set or self.category_name_entry9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.category_name_entry9.get_name_leafdata())
                        if (self.group_name_entry1.is_set or self.group_name_entry1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry1.get_name_leafdata())
                        if (self.group_name_entry10.is_set or self.group_name_entry10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry10.get_name_leafdata())
                        if (self.group_name_entry2.is_set or self.group_name_entry2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry2.get_name_leafdata())
                        if (self.group_name_entry3.is_set or self.group_name_entry3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry3.get_name_leafdata())
                        if (self.group_name_entry4.is_set or self.group_name_entry4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry4.get_name_leafdata())
                        if (self.group_name_entry5.is_set or self.group_name_entry5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry5.get_name_leafdata())
                        if (self.group_name_entry6.is_set or self.group_name_entry6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry6.get_name_leafdata())
                        if (self.group_name_entry7.is_set or self.group_name_entry7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry7.get_name_leafdata())
                        if (self.group_name_entry8.is_set or self.group_name_entry8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry8.get_name_leafdata())
                        if (self.group_name_entry9.is_set or self.group_name_entry9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_name_entry9.get_name_leafdata())
                        if (self.message_code_entry1.is_set or self.message_code_entry1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry1.get_name_leafdata())
                        if (self.message_code_entry10.is_set or self.message_code_entry10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry10.get_name_leafdata())
                        if (self.message_code_entry2.is_set or self.message_code_entry2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry2.get_name_leafdata())
                        if (self.message_code_entry3.is_set or self.message_code_entry3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry3.get_name_leafdata())
                        if (self.message_code_entry4.is_set or self.message_code_entry4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry4.get_name_leafdata())
                        if (self.message_code_entry5.is_set or self.message_code_entry5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry5.get_name_leafdata())
                        if (self.message_code_entry6.is_set or self.message_code_entry6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry6.get_name_leafdata())
                        if (self.message_code_entry7.is_set or self.message_code_entry7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry7.get_name_leafdata())
                        if (self.message_code_entry8.is_set or self.message_code_entry8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry8.get_name_leafdata())
                        if (self.message_code_entry9.is_set or self.message_code_entry9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_code_entry9.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "category-name-entry1" or name == "category-name-entry10" or name == "category-name-entry2" or name == "category-name-entry3" or name == "category-name-entry4" or name == "category-name-entry5" or name == "category-name-entry6" or name == "category-name-entry7" or name == "category-name-entry8" or name == "category-name-entry9" or name == "group-name-entry1" or name == "group-name-entry10" or name == "group-name-entry2" or name == "group-name-entry3" or name == "group-name-entry4" or name == "group-name-entry5" or name == "group-name-entry6" or name == "group-name-entry7" or name == "group-name-entry8" or name == "group-name-entry9" or name == "message-code-entry1" or name == "message-code-entry10" or name == "message-code-entry2" or name == "message-code-entry3" or name == "message-code-entry4" or name == "message-code-entry5" or name == "message-code-entry6" or name == "message-code-entry7" or name == "message-code-entry8" or name == "message-code-entry9" or name == "timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "category-name-entry1"):
                            self.category_name_entry1 = value
                            self.category_name_entry1.value_namespace = name_space
                            self.category_name_entry1.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry10"):
                            self.category_name_entry10 = value
                            self.category_name_entry10.value_namespace = name_space
                            self.category_name_entry10.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry2"):
                            self.category_name_entry2 = value
                            self.category_name_entry2.value_namespace = name_space
                            self.category_name_entry2.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry3"):
                            self.category_name_entry3 = value
                            self.category_name_entry3.value_namespace = name_space
                            self.category_name_entry3.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry4"):
                            self.category_name_entry4 = value
                            self.category_name_entry4.value_namespace = name_space
                            self.category_name_entry4.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry5"):
                            self.category_name_entry5 = value
                            self.category_name_entry5.value_namespace = name_space
                            self.category_name_entry5.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry6"):
                            self.category_name_entry6 = value
                            self.category_name_entry6.value_namespace = name_space
                            self.category_name_entry6.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry7"):
                            self.category_name_entry7 = value
                            self.category_name_entry7.value_namespace = name_space
                            self.category_name_entry7.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry8"):
                            self.category_name_entry8 = value
                            self.category_name_entry8.value_namespace = name_space
                            self.category_name_entry8.value_namespace_prefix = name_space_prefix
                        if(value_path == "category-name-entry9"):
                            self.category_name_entry9 = value
                            self.category_name_entry9.value_namespace = name_space
                            self.category_name_entry9.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry1"):
                            self.group_name_entry1 = value
                            self.group_name_entry1.value_namespace = name_space
                            self.group_name_entry1.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry10"):
                            self.group_name_entry10 = value
                            self.group_name_entry10.value_namespace = name_space
                            self.group_name_entry10.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry2"):
                            self.group_name_entry2 = value
                            self.group_name_entry2.value_namespace = name_space
                            self.group_name_entry2.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry3"):
                            self.group_name_entry3 = value
                            self.group_name_entry3.value_namespace = name_space
                            self.group_name_entry3.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry4"):
                            self.group_name_entry4 = value
                            self.group_name_entry4.value_namespace = name_space
                            self.group_name_entry4.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry5"):
                            self.group_name_entry5 = value
                            self.group_name_entry5.value_namespace = name_space
                            self.group_name_entry5.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry6"):
                            self.group_name_entry6 = value
                            self.group_name_entry6.value_namespace = name_space
                            self.group_name_entry6.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry7"):
                            self.group_name_entry7 = value
                            self.group_name_entry7.value_namespace = name_space
                            self.group_name_entry7.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry8"):
                            self.group_name_entry8 = value
                            self.group_name_entry8.value_namespace = name_space
                            self.group_name_entry8.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-name-entry9"):
                            self.group_name_entry9 = value
                            self.group_name_entry9.value_namespace = name_space
                            self.group_name_entry9.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry1"):
                            self.message_code_entry1 = value
                            self.message_code_entry1.value_namespace = name_space
                            self.message_code_entry1.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry10"):
                            self.message_code_entry10 = value
                            self.message_code_entry10.value_namespace = name_space
                            self.message_code_entry10.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry2"):
                            self.message_code_entry2 = value
                            self.message_code_entry2.value_namespace = name_space
                            self.message_code_entry2.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry3"):
                            self.message_code_entry3 = value
                            self.message_code_entry3.value_namespace = name_space
                            self.message_code_entry3.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry4"):
                            self.message_code_entry4 = value
                            self.message_code_entry4.value_namespace = name_space
                            self.message_code_entry4.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry5"):
                            self.message_code_entry5 = value
                            self.message_code_entry5.value_namespace = name_space
                            self.message_code_entry5.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry6"):
                            self.message_code_entry6 = value
                            self.message_code_entry6.value_namespace = name_space
                            self.message_code_entry6.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry7"):
                            self.message_code_entry7 = value
                            self.message_code_entry7.value_namespace = name_space
                            self.message_code_entry7.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry8"):
                            self.message_code_entry8 = value
                            self.message_code_entry8.value_namespace = name_space
                            self.message_code_entry8.value_namespace_prefix = name_space_prefix
                        if(value_path == "message-code-entry9"):
                            self.message_code_entry9 = value
                            self.message_code_entry9.value_namespace = name_space
                            self.message_code_entry9.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix


                class NonStateful(Entity):
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
                        super(Syslog.Correlator.Rules.Rule.NonStateful, self).__init__()

                        self.yang_name = "non-stateful"
                        self.yang_parent_name = "rule"

                        self.context_correlation = YLeaf(YType.empty, "context-correlation")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                        self.timeout_root_cause = YLeaf(YType.uint32, "timeout-root-cause")

                        self.non_root_causes = Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self._children_name_map["non_root_causes"] = "non-root-causes"
                        self._children_yang_names.add("non-root-causes")

                        self.root_cause = Syslog.Correlator.Rules.Rule.NonStateful.RootCause()
                        self.root_cause.parent = self
                        self._children_name_map["root_cause"] = "root-cause"
                        self._children_yang_names.add("root-cause")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("context_correlation",
                                        "timeout",
                                        "timeout_root_cause") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Correlator.Rules.Rule.NonStateful, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.Rules.Rule.NonStateful, self).__setattr__(name, value)


                    class NonRootCauses(Entity):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of    :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses, self).__init__()

                            self.yang_name = "non-root-causes"
                            self.yang_parent_name = "non-stateful"

                            self.non_root_cause = YList(self)

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
                                        super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses, self).__setattr__(name, value)


                        class NonRootCause(Entity):
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
                                super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, self).__init__()

                                self.yang_name = "non-root-cause"
                                self.yang_parent_name = "non-root-causes"

                                self.category = YLeaf(YType.str, "category")

                                self.group = YLeaf(YType.str, "group")

                                self.message_code = YLeaf(YType.str, "message-code")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("category",
                                                "group",
                                                "message_code") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.category.is_set or
                                    self.group.is_set or
                                    self.message_code.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.category.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.message_code.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "non-root-cause" + "[category='" + self.category.get() + "']" + "[group='" + self.group.get() + "']" + "[message-code='" + self.message_code.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.category.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.message_code.is_set or self.message_code.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.message_code.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "category" or name == "group" or name == "message-code"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "category"):
                                    self.category = value
                                    self.category.value_namespace = name_space
                                    self.category.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "message-code"):
                                    self.message_code = value
                                    self.message_code.value_namespace = name_space
                                    self.message_code.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.non_root_cause:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.non_root_cause:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "non-root-causes" + path_buffer

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

                            if (child_yang_name == "non-root-cause"):
                                for c in self.non_root_cause:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.non_root_cause.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "non-root-cause"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class RootCause(Entity):
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
                            super(Syslog.Correlator.Rules.Rule.NonStateful.RootCause, self).__init__()

                            self.yang_name = "root-cause"
                            self.yang_parent_name = "non-stateful"

                            self.category = YLeaf(YType.str, "category")

                            self.group = YLeaf(YType.str, "group")

                            self.message_code = YLeaf(YType.str, "message-code")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("category",
                                            "group",
                                            "message_code") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.Correlator.Rules.Rule.NonStateful.RootCause, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.NonStateful.RootCause, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.category.is_set or
                                self.group.is_set or
                                self.message_code.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.category.yfilter != YFilter.not_set or
                                self.group.yfilter != YFilter.not_set or
                                self.message_code.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "root-cause" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.category.get_name_leafdata())
                            if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group.get_name_leafdata())
                            if (self.message_code.is_set or self.message_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.message_code.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "category" or name == "group" or name == "message-code"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "category"):
                                self.category = value
                                self.category.value_namespace = name_space
                                self.category.value_namespace_prefix = name_space_prefix
                            if(value_path == "group"):
                                self.group = value
                                self.group.value_namespace = name_space
                                self.group.value_namespace_prefix = name_space_prefix
                            if(value_path == "message-code"):
                                self.message_code = value
                                self.message_code.value_namespace = name_space
                                self.message_code.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.context_correlation.is_set or
                            self.timeout.is_set or
                            self.timeout_root_cause.is_set or
                            (self.non_root_causes is not None and self.non_root_causes.has_data()) or
                            (self.root_cause is not None and self.root_cause.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.context_correlation.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set or
                            self.timeout_root_cause.yfilter != YFilter.not_set or
                            (self.non_root_causes is not None and self.non_root_causes.has_operation()) or
                            (self.root_cause is not None and self.root_cause.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "non-stateful" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.context_correlation.is_set or self.context_correlation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.context_correlation.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())
                        if (self.timeout_root_cause.is_set or self.timeout_root_cause.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout_root_cause.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "non-root-causes"):
                            if (self.non_root_causes is None):
                                self.non_root_causes = Syslog.Correlator.Rules.Rule.NonStateful.NonRootCauses()
                                self.non_root_causes.parent = self
                                self._children_name_map["non_root_causes"] = "non-root-causes"
                            return self.non_root_causes

                        if (child_yang_name == "root-cause"):
                            if (self.root_cause is None):
                                self.root_cause = Syslog.Correlator.Rules.Rule.NonStateful.RootCause()
                                self.root_cause.parent = self
                                self._children_name_map["root_cause"] = "root-cause"
                            return self.root_cause

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "non-root-causes" or name == "root-cause" or name == "context-correlation" or name == "timeout" or name == "timeout-root-cause"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "context-correlation"):
                            self.context_correlation = value
                            self.context_correlation.value_namespace = name_space
                            self.context_correlation.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout-root-cause"):
                            self.timeout_root_cause = value
                            self.timeout_root_cause.value_namespace = name_space
                            self.timeout_root_cause.value_namespace_prefix = name_space_prefix


                class Stateful(Entity):
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
                        super(Syslog.Correlator.Rules.Rule.Stateful, self).__init__()

                        self.yang_name = "stateful"
                        self.yang_parent_name = "rule"

                        self.context_correlation = YLeaf(YType.empty, "context-correlation")

                        self.reissue = YLeaf(YType.empty, "reissue")

                        self.reparent = YLeaf(YType.empty, "reparent")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                        self.timeout_root_cause = YLeaf(YType.uint32, "timeout-root-cause")

                        self.non_root_causes = Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self._children_name_map["non_root_causes"] = "non-root-causes"
                        self._children_yang_names.add("non-root-causes")

                        self.root_cause = Syslog.Correlator.Rules.Rule.Stateful.RootCause()
                        self.root_cause.parent = self
                        self._children_name_map["root_cause"] = "root-cause"
                        self._children_yang_names.add("root-cause")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("context_correlation",
                                        "reissue",
                                        "reparent",
                                        "timeout",
                                        "timeout_root_cause") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Correlator.Rules.Rule.Stateful, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.Rules.Rule.Stateful, self).__setattr__(name, value)


                    class NonRootCauses(Entity):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of    :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses, self).__init__()

                            self.yang_name = "non-root-causes"
                            self.yang_parent_name = "stateful"

                            self.non_root_cause = YList(self)

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
                                        super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses, self).__setattr__(name, value)


                        class NonRootCause(Entity):
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
                                super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause, self).__init__()

                                self.yang_name = "non-root-cause"
                                self.yang_parent_name = "non-root-causes"

                                self.category = YLeaf(YType.str, "category")

                                self.group = YLeaf(YType.str, "group")

                                self.message_code = YLeaf(YType.str, "message-code")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("category",
                                                "group",
                                                "message_code") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.category.is_set or
                                    self.group.is_set or
                                    self.message_code.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.category.yfilter != YFilter.not_set or
                                    self.group.yfilter != YFilter.not_set or
                                    self.message_code.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "non-root-cause" + "[category='" + self.category.get() + "']" + "[group='" + self.group.get() + "']" + "[message-code='" + self.message_code.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.category.get_name_leafdata())
                                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group.get_name_leafdata())
                                if (self.message_code.is_set or self.message_code.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.message_code.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "category" or name == "group" or name == "message-code"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "category"):
                                    self.category = value
                                    self.category.value_namespace = name_space
                                    self.category.value_namespace_prefix = name_space_prefix
                                if(value_path == "group"):
                                    self.group = value
                                    self.group.value_namespace = name_space
                                    self.group.value_namespace_prefix = name_space_prefix
                                if(value_path == "message-code"):
                                    self.message_code = value
                                    self.message_code.value_namespace = name_space
                                    self.message_code.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.non_root_cause:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.non_root_cause:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "non-root-causes" + path_buffer

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

                            if (child_yang_name == "non-root-cause"):
                                for c in self.non_root_cause:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses.NonRootCause()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.non_root_cause.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "non-root-cause"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class RootCause(Entity):
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
                            super(Syslog.Correlator.Rules.Rule.Stateful.RootCause, self).__init__()

                            self.yang_name = "root-cause"
                            self.yang_parent_name = "stateful"

                            self.category = YLeaf(YType.str, "category")

                            self.group = YLeaf(YType.str, "group")

                            self.message_code = YLeaf(YType.str, "message-code")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("category",
                                            "group",
                                            "message_code") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.Correlator.Rules.Rule.Stateful.RootCause, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.Stateful.RootCause, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.category.is_set or
                                self.group.is_set or
                                self.message_code.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.category.yfilter != YFilter.not_set or
                                self.group.yfilter != YFilter.not_set or
                                self.message_code.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "root-cause" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.category.get_name_leafdata())
                            if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group.get_name_leafdata())
                            if (self.message_code.is_set or self.message_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.message_code.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "category" or name == "group" or name == "message-code"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "category"):
                                self.category = value
                                self.category.value_namespace = name_space
                                self.category.value_namespace_prefix = name_space_prefix
                            if(value_path == "group"):
                                self.group = value
                                self.group.value_namespace = name_space
                                self.group.value_namespace_prefix = name_space_prefix
                            if(value_path == "message-code"):
                                self.message_code = value
                                self.message_code.value_namespace = name_space
                                self.message_code.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.context_correlation.is_set or
                            self.reissue.is_set or
                            self.reparent.is_set or
                            self.timeout.is_set or
                            self.timeout_root_cause.is_set or
                            (self.non_root_causes is not None and self.non_root_causes.has_data()) or
                            (self.root_cause is not None and self.root_cause.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.context_correlation.yfilter != YFilter.not_set or
                            self.reissue.yfilter != YFilter.not_set or
                            self.reparent.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set or
                            self.timeout_root_cause.yfilter != YFilter.not_set or
                            (self.non_root_causes is not None and self.non_root_causes.has_operation()) or
                            (self.root_cause is not None and self.root_cause.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stateful" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.context_correlation.is_set or self.context_correlation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.context_correlation.get_name_leafdata())
                        if (self.reissue.is_set or self.reissue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reissue.get_name_leafdata())
                        if (self.reparent.is_set or self.reparent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reparent.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())
                        if (self.timeout_root_cause.is_set or self.timeout_root_cause.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout_root_cause.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "non-root-causes"):
                            if (self.non_root_causes is None):
                                self.non_root_causes = Syslog.Correlator.Rules.Rule.Stateful.NonRootCauses()
                                self.non_root_causes.parent = self
                                self._children_name_map["non_root_causes"] = "non-root-causes"
                            return self.non_root_causes

                        if (child_yang_name == "root-cause"):
                            if (self.root_cause is None):
                                self.root_cause = Syslog.Correlator.Rules.Rule.Stateful.RootCause()
                                self.root_cause.parent = self
                                self._children_name_map["root_cause"] = "root-cause"
                            return self.root_cause

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "non-root-causes" or name == "root-cause" or name == "context-correlation" or name == "reissue" or name == "reparent" or name == "timeout" or name == "timeout-root-cause"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "context-correlation"):
                            self.context_correlation = value
                            self.context_correlation.value_namespace = name_space
                            self.context_correlation.value_namespace_prefix = name_space_prefix
                        if(value_path == "reissue"):
                            self.reissue = value
                            self.reissue.value_namespace = name_space
                            self.reissue.value_namespace_prefix = name_space_prefix
                        if(value_path == "reparent"):
                            self.reparent = value
                            self.reparent.value_namespace = name_space
                            self.reparent.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout-root-cause"):
                            self.timeout_root_cause = value
                            self.timeout_root_cause.value_namespace = name_space
                            self.timeout_root_cause.value_namespace_prefix = name_space_prefix


                class ApplyTo(Entity):
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
                        super(Syslog.Correlator.Rules.Rule.ApplyTo, self).__init__()

                        self.yang_name = "apply-to"
                        self.yang_parent_name = "rule"

                        self.all_of_router = YLeaf(YType.empty, "all-of-router")

                        self.contexts = Syslog.Correlator.Rules.Rule.ApplyTo.Contexts()
                        self.contexts.parent = self
                        self._children_name_map["contexts"] = "contexts"
                        self._children_yang_names.add("contexts")

                        self.locations = Syslog.Correlator.Rules.Rule.ApplyTo.Locations()
                        self.locations.parent = self
                        self._children_name_map["locations"] = "locations"
                        self._children_yang_names.add("locations")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("all_of_router") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Correlator.Rules.Rule.ApplyTo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.Rules.Rule.ApplyTo, self).__setattr__(name, value)


                    class Contexts(Entity):
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
                            super(Syslog.Correlator.Rules.Rule.ApplyTo.Contexts, self).__init__()

                            self.yang_name = "contexts"
                            self.yang_parent_name = "apply-to"

                            self.context = YLeafList(YType.str, "context")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("context") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.Correlator.Rules.Rule.ApplyTo.Contexts, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.ApplyTo.Contexts, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.context.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return False

                        def has_operation(self):
                            for leaf in self.context.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.context.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "contexts" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            leaf_name_data.extend(self.context.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "context"):
                                self.context.append(value)


                    class Locations(Entity):
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
                            super(Syslog.Correlator.Rules.Rule.ApplyTo.Locations, self).__init__()

                            self.yang_name = "locations"
                            self.yang_parent_name = "apply-to"

                            self.location = YLeafList(YType.str, "location")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("location") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.Correlator.Rules.Rule.ApplyTo.Locations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.ApplyTo.Locations, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.location.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return False

                        def has_operation(self):
                            for leaf in self.location.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.location.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "locations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            leaf_name_data.extend(self.location.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "location"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "location"):
                                self.location.append(value)

                    def has_data(self):
                        return (
                            self.all_of_router.is_set or
                            (self.contexts is not None and self.contexts.has_data()) or
                            (self.locations is not None and self.locations.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.all_of_router.yfilter != YFilter.not_set or
                            (self.contexts is not None and self.contexts.has_operation()) or
                            (self.locations is not None and self.locations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "apply-to" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.all_of_router.is_set or self.all_of_router.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.all_of_router.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "contexts"):
                            if (self.contexts is None):
                                self.contexts = Syslog.Correlator.Rules.Rule.ApplyTo.Contexts()
                                self.contexts.parent = self
                                self._children_name_map["contexts"] = "contexts"
                            return self.contexts

                        if (child_yang_name == "locations"):
                            if (self.locations is None):
                                self.locations = Syslog.Correlator.Rules.Rule.ApplyTo.Locations()
                                self.locations.parent = self
                                self._children_name_map["locations"] = "locations"
                            return self.locations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "contexts" or name == "locations" or name == "all-of-router"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "all-of-router"):
                            self.all_of_router = value
                            self.all_of_router.value_namespace = name_space
                            self.all_of_router.value_namespace_prefix = name_space_prefix


                class AppliedTo(Entity):
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
                        super(Syslog.Correlator.Rules.Rule.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule"

                        self.all = YLeaf(YType.empty, "all")

                        self.contexts = Syslog.Correlator.Rules.Rule.AppliedTo.Contexts()
                        self.contexts.parent = self
                        self._children_name_map["contexts"] = "contexts"
                        self._children_yang_names.add("contexts")

                        self.locations = Syslog.Correlator.Rules.Rule.AppliedTo.Locations()
                        self.locations.parent = self
                        self._children_name_map["locations"] = "locations"
                        self._children_yang_names.add("locations")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("all") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Correlator.Rules.Rule.AppliedTo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.Rules.Rule.AppliedTo, self).__setattr__(name, value)


                    class Contexts(Entity):
                        """
                        Table of configured contexts to apply
                        
                        .. attribute:: context
                        
                        	A context
                        	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts, self).__init__()

                            self.yang_name = "contexts"
                            self.yang_parent_name = "applied-to"

                            self.context = YList(self)

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
                                        super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts, self).__setattr__(name, value)


                        class Context(Entity):
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
                                super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context, self).__init__()

                                self.yang_name = "context"
                                self.yang_parent_name = "contexts"

                                self.context = YLeaf(YType.str, "context")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("context") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context, self).__setattr__(name, value)

                            def has_data(self):
                                return self.context.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.context.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "context" + "[context='" + self.context.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.context.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "context"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "context"):
                                    self.context = value
                                    self.context.value_namespace = name_space
                                    self.context.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.context:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.context:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "contexts" + path_buffer

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

                            if (child_yang_name == "context"):
                                for c in self.context:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Correlator.Rules.Rule.AppliedTo.Contexts.Context()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.context.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Locations(Entity):
                        """
                        Table of configured locations to apply
                        
                        .. attribute:: location
                        
                        	A location
                        	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations, self).__init__()

                            self.yang_name = "locations"
                            self.yang_parent_name = "applied-to"

                            self.location = YList(self)

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
                                        super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations, self).__setattr__(name, value)


                        class Location(Entity):
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
                                super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "locations"

                                self.location = YLeaf(YType.str, "location")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("location") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location, self).__setattr__(name, value)

                            def has_data(self):
                                return self.location.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "location" + "[location='" + self.location.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "location"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.location:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.location:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "locations" + path_buffer

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

                            if (child_yang_name == "location"):
                                for c in self.location:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Correlator.Rules.Rule.AppliedTo.Locations.Location()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.location.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "location"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.all.is_set or
                            (self.contexts is not None and self.contexts.has_data()) or
                            (self.locations is not None and self.locations.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.all.yfilter != YFilter.not_set or
                            (self.contexts is not None and self.contexts.has_operation()) or
                            (self.locations is not None and self.locations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "applied-to" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.all.is_set or self.all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.all.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "contexts"):
                            if (self.contexts is None):
                                self.contexts = Syslog.Correlator.Rules.Rule.AppliedTo.Contexts()
                                self.contexts.parent = self
                                self._children_name_map["contexts"] = "contexts"
                            return self.contexts

                        if (child_yang_name == "locations"):
                            if (self.locations is None):
                                self.locations = Syslog.Correlator.Rules.Rule.AppliedTo.Locations()
                                self.locations.parent = self
                                self._children_name_map["locations"] = "locations"
                            return self.locations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "contexts" or name == "locations" or name == "all"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "all"):
                            self.all = value
                            self.all.value_namespace = name_space
                            self.all.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.applied_to is not None and self.applied_to.has_data()) or
                        (self.apply_to is not None and self.apply_to.has_data()) or
                        (self.definition is not None and self.definition.has_data()) or
                        (self.non_stateful is not None and self.non_stateful.has_data()) or
                        (self.stateful is not None and self.stateful.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.applied_to is not None and self.applied_to.has_operation()) or
                        (self.apply_to is not None and self.apply_to.has_operation()) or
                        (self.definition is not None and self.definition.has_operation()) or
                        (self.non_stateful is not None and self.non_stateful.has_operation()) or
                        (self.stateful is not None and self.stateful.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/rules/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "applied-to"):
                        if (self.applied_to is None):
                            self.applied_to = Syslog.Correlator.Rules.Rule.AppliedTo()
                            self.applied_to.parent = self
                            self._children_name_map["applied_to"] = "applied-to"
                        return self.applied_to

                    if (child_yang_name == "apply-to"):
                        if (self.apply_to is None):
                            self.apply_to = Syslog.Correlator.Rules.Rule.ApplyTo()
                            self.apply_to.parent = self
                            self._children_name_map["apply_to"] = "apply-to"
                        return self.apply_to

                    if (child_yang_name == "definition"):
                        if (self.definition is None):
                            self.definition = Syslog.Correlator.Rules.Rule.Definition()
                            self.definition.parent = self
                            self._children_name_map["definition"] = "definition"
                        return self.definition

                    if (child_yang_name == "non-stateful"):
                        if (self.non_stateful is None):
                            self.non_stateful = Syslog.Correlator.Rules.Rule.NonStateful()
                            self.non_stateful.parent = self
                            self._children_name_map["non_stateful"] = "non-stateful"
                        return self.non_stateful

                    if (child_yang_name == "stateful"):
                        if (self.stateful is None):
                            self.stateful = Syslog.Correlator.Rules.Rule.Stateful()
                            self.stateful.parent = self
                            self._children_name_map["stateful"] = "stateful"
                        return self.stateful

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "applied-to" or name == "apply-to" or name == "definition" or name == "non-stateful" or name == "stateful" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rule:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.rule:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rules" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rule"):
                    for c in self.rule:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Syslog.Correlator.Rules.Rule()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rule.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RuleSets(Entity):
            """
            Table of configured rulesets
            
            .. attribute:: rule_set
            
            	Ruleset name
            	**type**\: list of    :py:class:`RuleSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Syslog.Correlator.RuleSets, self).__init__()

                self.yang_name = "rule-sets"
                self.yang_parent_name = "correlator"

                self.rule_set = YList(self)

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
                            super(Syslog.Correlator.RuleSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Correlator.RuleSets, self).__setattr__(name, value)


            class RuleSet(Entity):
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
                    super(Syslog.Correlator.RuleSets.RuleSet, self).__init__()

                    self.yang_name = "rule-set"
                    self.yang_parent_name = "rule-sets"

                    self.name = YLeaf(YType.str, "name")

                    self.applied_to = Syslog.Correlator.RuleSets.RuleSet.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._children_yang_names.add("applied-to")

                    self.rulenames = Syslog.Correlator.RuleSets.RuleSet.Rulenames()
                    self.rulenames.parent = self
                    self._children_name_map["rulenames"] = "rulenames"
                    self._children_yang_names.add("rulenames")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.Correlator.RuleSets.RuleSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.Correlator.RuleSets.RuleSet, self).__setattr__(name, value)


                class Rulenames(Entity):
                    """
                    Table of configured rulenames
                    
                    .. attribute:: rulename
                    
                    	A rulename
                    	**type**\: list of    :py:class:`Rulename <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Syslog.Correlator.RuleSets.RuleSet.Rulenames, self).__init__()

                        self.yang_name = "rulenames"
                        self.yang_parent_name = "rule-set"

                        self.rulename = YList(self)

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
                                    super(Syslog.Correlator.RuleSets.RuleSet.Rulenames, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.RuleSets.RuleSet.Rulenames, self).__setattr__(name, value)


                    class Rulename(Entity):
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
                            super(Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename, self).__init__()

                            self.yang_name = "rulename"
                            self.yang_parent_name = "rulenames"

                            self.rulename = YLeaf(YType.str, "rulename")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("rulename") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename, self).__setattr__(name, value)

                        def has_data(self):
                            return self.rulename.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.rulename.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rulename" + "[rulename='" + self.rulename.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.rulename.is_set or self.rulename.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rulename.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "rulename"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "rulename"):
                                self.rulename = value
                                self.rulename.value_namespace = name_space
                                self.rulename.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.rulename:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.rulename:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rulenames" + path_buffer

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

                        if (child_yang_name == "rulename"):
                            for c in self.rulename:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Syslog.Correlator.RuleSets.RuleSet.Rulenames.Rulename()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rulename.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rulename"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class AppliedTo(Entity):
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
                        super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule-set"

                        self.all = YLeaf(YType.empty, "all")

                        self.contexts = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts()
                        self.contexts.parent = self
                        self._children_name_map["contexts"] = "contexts"
                        self._children_yang_names.add("contexts")

                        self.locations = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations()
                        self.locations.parent = self
                        self._children_name_map["locations"] = "locations"
                        self._children_yang_names.add("locations")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("all") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo, self).__setattr__(name, value)


                    class Contexts(Entity):
                        """
                        Table of configured contexts to apply
                        
                        .. attribute:: context
                        
                        	A context
                        	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts, self).__init__()

                            self.yang_name = "contexts"
                            self.yang_parent_name = "applied-to"

                            self.context = YList(self)

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
                                        super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts, self).__setattr__(name, value)


                        class Context(Entity):
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
                                super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context, self).__init__()

                                self.yang_name = "context"
                                self.yang_parent_name = "contexts"

                                self.context = YLeaf(YType.str, "context")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("context") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context, self).__setattr__(name, value)

                            def has_data(self):
                                return self.context.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.context.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "context" + "[context='" + self.context.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.context.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "context"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "context"):
                                    self.context = value
                                    self.context.value_namespace = name_space
                                    self.context.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.context:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.context:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "contexts" + path_buffer

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

                            if (child_yang_name == "context"):
                                for c in self.context:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts.Context()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.context.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "context"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Locations(Entity):
                        """
                        Table of configured locations to apply
                        
                        .. attribute:: location
                        
                        	A location
                        	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations, self).__init__()

                            self.yang_name = "locations"
                            self.yang_parent_name = "applied-to"

                            self.location = YList(self)

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
                                        super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations, self).__setattr__(name, value)


                        class Location(Entity):
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
                                super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "locations"

                                self.location = YLeaf(YType.str, "location")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("location") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location, self).__setattr__(name, value)

                            def has_data(self):
                                return self.location.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "location" + "[location='" + self.location.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "location"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.location:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.location:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "locations" + path_buffer

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

                            if (child_yang_name == "location"):
                                for c in self.location:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations.Location()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.location.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "location"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.all.is_set or
                            (self.contexts is not None and self.contexts.has_data()) or
                            (self.locations is not None and self.locations.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.all.yfilter != YFilter.not_set or
                            (self.contexts is not None and self.contexts.has_operation()) or
                            (self.locations is not None and self.locations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "applied-to" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.all.is_set or self.all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.all.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "contexts"):
                            if (self.contexts is None):
                                self.contexts = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Contexts()
                                self.contexts.parent = self
                                self._children_name_map["contexts"] = "contexts"
                            return self.contexts

                        if (child_yang_name == "locations"):
                            if (self.locations is None):
                                self.locations = Syslog.Correlator.RuleSets.RuleSet.AppliedTo.Locations()
                                self.locations.parent = self
                                self._children_name_map["locations"] = "locations"
                            return self.locations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "contexts" or name == "locations" or name == "all"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "all"):
                            self.all = value
                            self.all.value_namespace = name_space
                            self.all.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.applied_to is not None and self.applied_to.has_data()) or
                        (self.rulenames is not None and self.rulenames.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.applied_to is not None and self.applied_to.has_operation()) or
                        (self.rulenames is not None and self.rulenames.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule-set" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/rule-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "applied-to"):
                        if (self.applied_to is None):
                            self.applied_to = Syslog.Correlator.RuleSets.RuleSet.AppliedTo()
                            self.applied_to.parent = self
                            self._children_name_map["applied_to"] = "applied-to"
                        return self.applied_to

                    if (child_yang_name == "rulenames"):
                        if (self.rulenames is None):
                            self.rulenames = Syslog.Correlator.RuleSets.RuleSet.Rulenames()
                            self.rulenames.parent = self
                            self._children_name_map["rulenames"] = "rulenames"
                        return self.rulenames

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "applied-to" or name == "rulenames" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rule_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.rule_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:correlator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rule-set"):
                    for c in self.rule_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Syslog.Correlator.RuleSets.RuleSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rule_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.buffer_size.is_set or
                (self.rule_sets is not None and self.rule_sets.has_data()) or
                (self.rules is not None and self.rules.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.buffer_size.yfilter != YFilter.not_set or
                (self.rule_sets is not None and self.rule_sets.has_operation()) or
                (self.rules is not None and self.rules.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-infra-correlator-cfg:correlator" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.buffer_size.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-sets"):
                if (self.rule_sets is None):
                    self.rule_sets = Syslog.Correlator.RuleSets()
                    self.rule_sets.parent = self
                    self._children_name_map["rule_sets"] = "rule-sets"
                return self.rule_sets

            if (child_yang_name == "rules"):
                if (self.rules is None):
                    self.rules = Syslog.Correlator.Rules()
                    self.rules.parent = self
                    self._children_name_map["rules"] = "rules"
                return self.rules

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-sets" or name == "rules" or name == "buffer-size"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "buffer-size"):
                self.buffer_size = value
                self.buffer_size.value_namespace = name_space
                self.buffer_size.value_namespace_prefix = name_space_prefix


    class Suppression(Entity):
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
            super(Syslog.Suppression, self).__init__()

            self.yang_name = "suppression"
            self.yang_parent_name = "syslog"

            self.rules = Syslog.Suppression.Rules()
            self.rules.parent = self
            self._children_name_map["rules"] = "rules"
            self._children_yang_names.add("rules")


        class Rules(Entity):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule>`
            
            

            """

            _prefix = 'infra-correlator-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Syslog.Suppression.Rules, self).__init__()

                self.yang_name = "rules"
                self.yang_parent_name = "suppression"

                self.rule = YList(self)

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
                            super(Syslog.Suppression.Rules, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Suppression.Rules, self).__setattr__(name, value)


            class Rule(Entity):
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
                    super(Syslog.Suppression.Rules.Rule, self).__init__()

                    self.yang_name = "rule"
                    self.yang_parent_name = "rules"

                    self.name = YLeaf(YType.str, "name")

                    self.all_alarms = YLeaf(YType.empty, "all-alarms")

                    self.alarm_causes = Syslog.Suppression.Rules.Rule.AlarmCauses()
                    self.alarm_causes.parent = self
                    self._children_name_map["alarm_causes"] = "alarm-causes"
                    self._children_yang_names.add("alarm-causes")

                    self.applied_to = Syslog.Suppression.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._children_yang_names.add("applied-to")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "all_alarms") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Syslog.Suppression.Rules.Rule, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Syslog.Suppression.Rules.Rule, self).__setattr__(name, value)


                class AppliedTo(Entity):
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
                        super(Syslog.Suppression.Rules.Rule.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule"

                        self.all = YLeaf(YType.empty, "all")

                        self.sources = Syslog.Suppression.Rules.Rule.AppliedTo.Sources()
                        self.sources.parent = self
                        self._children_name_map["sources"] = "sources"
                        self._children_yang_names.add("sources")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("all") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Syslog.Suppression.Rules.Rule.AppliedTo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Suppression.Rules.Rule.AppliedTo, self).__setattr__(name, value)


                    class Sources(Entity):
                        """
                        Table of configured sources to apply
                        
                        .. attribute:: source
                        
                        	An alarm source
                        	**type**\: list of    :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source>`
                        
                        

                        """

                        _prefix = 'infra-correlator-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources, self).__init__()

                            self.yang_name = "sources"
                            self.yang_parent_name = "applied-to"

                            self.source = YList(self)

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
                                        super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources, self).__setattr__(name, value)


                        class Source(Entity):
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
                                super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "sources"

                                self.source = YLeaf(YType.str, "source")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("source") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source, self).__setattr__(name, value)

                            def has_data(self):
                                return self.source.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.source.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "source" + "[source='" + self.source.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "source"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "source"):
                                    self.source = value
                                    self.source.value_namespace = name_space
                                    self.source.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.source:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.source:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sources" + path_buffer

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

                            if (child_yang_name == "source"):
                                for c in self.source:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Syslog.Suppression.Rules.Rule.AppliedTo.Sources.Source()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.source.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "source"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.all.is_set or
                            (self.sources is not None and self.sources.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.all.yfilter != YFilter.not_set or
                            (self.sources is not None and self.sources.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "applied-to" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.all.is_set or self.all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.all.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sources"):
                            if (self.sources is None):
                                self.sources = Syslog.Suppression.Rules.Rule.AppliedTo.Sources()
                                self.sources.parent = self
                                self._children_name_map["sources"] = "sources"
                            return self.sources

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sources" or name == "all"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "all"):
                            self.all = value
                            self.all.value_namespace = name_space
                            self.all.value_namespace_prefix = name_space_prefix


                class AlarmCauses(Entity):
                    """
                    Causes of alarms to be suppressed
                    
                    .. attribute:: alarm_cause
                    
                    	Category, Group and Code of alarm/syslog to be suppressed
                    	**type**\: list of    :py:class:`AlarmCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_cfg.Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause>`
                    
                    

                    """

                    _prefix = 'infra-correlator-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Syslog.Suppression.Rules.Rule.AlarmCauses, self).__init__()

                        self.yang_name = "alarm-causes"
                        self.yang_parent_name = "rule"

                        self.alarm_cause = YList(self)

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
                                    super(Syslog.Suppression.Rules.Rule.AlarmCauses, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Syslog.Suppression.Rules.Rule.AlarmCauses, self).__setattr__(name, value)


                    class AlarmCause(Entity):
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
                            super(Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause, self).__init__()

                            self.yang_name = "alarm-cause"
                            self.yang_parent_name = "alarm-causes"

                            self.category = YLeaf(YType.str, "category")

                            self.group = YLeaf(YType.str, "group")

                            self.code = YLeaf(YType.str, "code")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("category",
                                            "group",
                                            "code") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.category.is_set or
                                self.group.is_set or
                                self.code.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.category.yfilter != YFilter.not_set or
                                self.group.yfilter != YFilter.not_set or
                                self.code.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "alarm-cause" + "[category='" + self.category.get() + "']" + "[group='" + self.group.get() + "']" + "[code='" + self.code.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.category.get_name_leafdata())
                            if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group.get_name_leafdata())
                            if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.code.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "category" or name == "group" or name == "code"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "category"):
                                self.category = value
                                self.category.value_namespace = name_space
                                self.category.value_namespace_prefix = name_space_prefix
                            if(value_path == "group"):
                                self.group = value
                                self.group.value_namespace = name_space
                                self.group.value_namespace_prefix = name_space_prefix
                            if(value_path == "code"):
                                self.code = value
                                self.code.value_namespace = name_space
                                self.code.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.alarm_cause:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.alarm_cause:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "alarm-causes" + path_buffer

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

                        if (child_yang_name == "alarm-cause"):
                            for c in self.alarm_cause:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Syslog.Suppression.Rules.Rule.AlarmCauses.AlarmCause()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.alarm_cause.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "alarm-cause"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.all_alarms.is_set or
                        (self.alarm_causes is not None and self.alarm_causes.has_data()) or
                        (self.applied_to is not None and self.applied_to.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.all_alarms.yfilter != YFilter.not_set or
                        (self.alarm_causes is not None and self.alarm_causes.has_operation()) or
                        (self.applied_to is not None and self.applied_to.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression/rules/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.all_alarms.is_set or self.all_alarms.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.all_alarms.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "alarm-causes"):
                        if (self.alarm_causes is None):
                            self.alarm_causes = Syslog.Suppression.Rules.Rule.AlarmCauses()
                            self.alarm_causes.parent = self
                            self._children_name_map["alarm_causes"] = "alarm-causes"
                        return self.alarm_causes

                    if (child_yang_name == "applied-to"):
                        if (self.applied_to is None):
                            self.applied_to = Syslog.Suppression.Rules.Rule.AppliedTo()
                            self.applied_to.parent = self
                            self._children_name_map["applied_to"] = "applied-to"
                        return self.applied_to

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alarm-causes" or name == "applied-to" or name == "name" or name == "all-alarms"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "all-alarms"):
                        self.all_alarms = value
                        self.all_alarms.value_namespace = name_space
                        self.all_alarms.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rule:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.rule:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rules" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/Cisco-IOS-XR-infra-correlator-cfg:suppression/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rule"):
                    for c in self.rule:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Syslog.Suppression.Rules.Rule()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rule.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.rules is not None and self.rules.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.rules is not None and self.rules.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-infra-correlator-cfg:suppression" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rules"):
                if (self.rules is None):
                    self.rules = Syslog.Suppression.Rules()
                    self.rules.parent = self
                    self._children_name_map["rules"] = "rules"
                return self.rules

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rules"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.enable_console_logging.is_set or
            self.host_name_prefix.is_set or
            self.local_log_file_size.is_set or
            self.suppress_duplicates.is_set or
            (self.alarm_logger is not None and self.alarm_logger.has_data()) or
            (self.archive is not None and self.archive.has_data()) or
            (self.buffered_logging is not None and self.buffered_logging.has_data()) or
            (self.console_logging is not None and self.console_logging.has_data()) or
            (self.correlator is not None and self.correlator.has_data()) or
            (self.files is not None and self.files.has_data()) or
            (self.history_logging is not None and self.history_logging.has_data()) or
            (self.host_server is not None and self.host_server.has_data()) or
            (self.ipv4 is not None and self.ipv4.has_data()) or
            (self.ipv6 is not None and self.ipv6.has_data()) or
            (self.logging_facilities is not None and self.logging_facilities.has_data()) or
            (self.monitor_logging is not None and self.monitor_logging.has_data()) or
            (self.source_interface_table is not None and self.source_interface_table.has_data()) or
            (self.suppression is not None and self.suppression.has_data()) or
            (self.trap_logging is not None and self.trap_logging.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable_console_logging.yfilter != YFilter.not_set or
            self.host_name_prefix.yfilter != YFilter.not_set or
            self.local_log_file_size.yfilter != YFilter.not_set or
            self.suppress_duplicates.yfilter != YFilter.not_set or
            (self.alarm_logger is not None and self.alarm_logger.has_operation()) or
            (self.archive is not None and self.archive.has_operation()) or
            (self.buffered_logging is not None and self.buffered_logging.has_operation()) or
            (self.console_logging is not None and self.console_logging.has_operation()) or
            (self.correlator is not None and self.correlator.has_operation()) or
            (self.files is not None and self.files.has_operation()) or
            (self.history_logging is not None and self.history_logging.has_operation()) or
            (self.host_server is not None and self.host_server.has_operation()) or
            (self.ipv4 is not None and self.ipv4.has_operation()) or
            (self.ipv6 is not None and self.ipv6.has_operation()) or
            (self.logging_facilities is not None and self.logging_facilities.has_operation()) or
            (self.monitor_logging is not None and self.monitor_logging.has_operation()) or
            (self.source_interface_table is not None and self.source_interface_table.has_operation()) or
            (self.suppression is not None and self.suppression.has_operation()) or
            (self.trap_logging is not None and self.trap_logging.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-syslog-cfg:syslog" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable_console_logging.is_set or self.enable_console_logging.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable_console_logging.get_name_leafdata())
        if (self.host_name_prefix.is_set or self.host_name_prefix.yfilter != YFilter.not_set):
            leaf_name_data.append(self.host_name_prefix.get_name_leafdata())
        if (self.local_log_file_size.is_set or self.local_log_file_size.yfilter != YFilter.not_set):
            leaf_name_data.append(self.local_log_file_size.get_name_leafdata())
        if (self.suppress_duplicates.is_set or self.suppress_duplicates.yfilter != YFilter.not_set):
            leaf_name_data.append(self.suppress_duplicates.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "alarm-logger"):
            if (self.alarm_logger is None):
                self.alarm_logger = Syslog.AlarmLogger()
                self.alarm_logger.parent = self
                self._children_name_map["alarm_logger"] = "alarm-logger"
            return self.alarm_logger

        if (child_yang_name == "archive"):
            if (self.archive is None):
                self.archive = Syslog.Archive()
                self.archive.parent = self
                self._children_name_map["archive"] = "archive"
            return self.archive

        if (child_yang_name == "buffered-logging"):
            if (self.buffered_logging is None):
                self.buffered_logging = Syslog.BufferedLogging()
                self.buffered_logging.parent = self
                self._children_name_map["buffered_logging"] = "buffered-logging"
            return self.buffered_logging

        if (child_yang_name == "console-logging"):
            if (self.console_logging is None):
                self.console_logging = Syslog.ConsoleLogging()
                self.console_logging.parent = self
                self._children_name_map["console_logging"] = "console-logging"
            return self.console_logging

        if (child_yang_name == "correlator"):
            if (self.correlator is None):
                self.correlator = Syslog.Correlator()
                self.correlator.parent = self
                self._children_name_map["correlator"] = "correlator"
            return self.correlator

        if (child_yang_name == "files"):
            if (self.files is None):
                self.files = Syslog.Files()
                self.files.parent = self
                self._children_name_map["files"] = "files"
            return self.files

        if (child_yang_name == "history-logging"):
            if (self.history_logging is None):
                self.history_logging = Syslog.HistoryLogging()
                self.history_logging.parent = self
                self._children_name_map["history_logging"] = "history-logging"
            return self.history_logging

        if (child_yang_name == "host-server"):
            if (self.host_server is None):
                self.host_server = Syslog.HostServer()
                self.host_server.parent = self
                self._children_name_map["host_server"] = "host-server"
            return self.host_server

        if (child_yang_name == "ipv4"):
            if (self.ipv4 is None):
                self.ipv4 = Syslog.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
            return self.ipv4

        if (child_yang_name == "ipv6"):
            if (self.ipv6 is None):
                self.ipv6 = Syslog.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
            return self.ipv6

        if (child_yang_name == "logging-facilities"):
            if (self.logging_facilities is None):
                self.logging_facilities = Syslog.LoggingFacilities()
                self.logging_facilities.parent = self
                self._children_name_map["logging_facilities"] = "logging-facilities"
            return self.logging_facilities

        if (child_yang_name == "monitor-logging"):
            if (self.monitor_logging is None):
                self.monitor_logging = Syslog.MonitorLogging()
                self.monitor_logging.parent = self
                self._children_name_map["monitor_logging"] = "monitor-logging"
            return self.monitor_logging

        if (child_yang_name == "source-interface-table"):
            if (self.source_interface_table is None):
                self.source_interface_table = Syslog.SourceInterfaceTable()
                self.source_interface_table.parent = self
                self._children_name_map["source_interface_table"] = "source-interface-table"
            return self.source_interface_table

        if (child_yang_name == "suppression"):
            if (self.suppression is None):
                self.suppression = Syslog.Suppression()
                self.suppression.parent = self
                self._children_name_map["suppression"] = "suppression"
            return self.suppression

        if (child_yang_name == "trap-logging"):
            if (self.trap_logging is None):
                self.trap_logging = Syslog.TrapLogging()
                self.trap_logging.parent = self
                self._children_name_map["trap_logging"] = "trap-logging"
            return self.trap_logging

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "alarm-logger" or name == "archive" or name == "buffered-logging" or name == "console-logging" or name == "correlator" or name == "files" or name == "history-logging" or name == "host-server" or name == "ipv4" or name == "ipv6" or name == "logging-facilities" or name == "monitor-logging" or name == "source-interface-table" or name == "suppression" or name == "trap-logging" or name == "enable-console-logging" or name == "host-name-prefix" or name == "local-log-file-size" or name == "suppress-duplicates"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable-console-logging"):
            self.enable_console_logging = value
            self.enable_console_logging.value_namespace = name_space
            self.enable_console_logging.value_namespace_prefix = name_space_prefix
        if(value_path == "host-name-prefix"):
            self.host_name_prefix = value
            self.host_name_prefix.value_namespace = name_space
            self.host_name_prefix.value_namespace_prefix = name_space_prefix
        if(value_path == "local-log-file-size"):
            self.local_log_file_size = value
            self.local_log_file_size.value_namespace = name_space
            self.local_log_file_size.value_namespace_prefix = name_space_prefix
        if(value_path == "suppress-duplicates"):
            self.suppress_duplicates = value
            self.suppress_duplicates.value_namespace = name_space
            self.suppress_duplicates.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Syslog()
        return self._top_entity

