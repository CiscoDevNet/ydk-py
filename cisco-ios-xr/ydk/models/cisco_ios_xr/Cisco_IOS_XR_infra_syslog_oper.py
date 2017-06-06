""" Cisco_IOS_XR_infra_syslog_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-syslog package operational data.

This module contains definitions
for the following management objects\:
  logging\: Logging History data
  syslog\: syslog

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SystemMessageSeverityEnum(Enum):
    """
    SystemMessageSeverityEnum

    System message severity

    .. data:: message_severity_unknown = -1

    	Unknown

    .. data:: message_severity_emergency = 0

    	Emergency

    .. data:: message_severity_alert = 1

    	Alert

    .. data:: message_severity_critical = 2

    	Critical

    .. data:: message_severity_error = 3

    	Error

    .. data:: message_severity_warning = 4

    	Warning

    .. data:: message_severity_notice = 5

    	Notice

    .. data:: message_severity_informational = 6

    	Informational

    .. data:: message_severity_debug = 7

    	Debug

    """

    message_severity_unknown = -1

    message_severity_emergency = 0

    message_severity_alert = 1

    message_severity_critical = 2

    message_severity_error = 3

    message_severity_warning = 4

    message_severity_notice = 5

    message_severity_informational = 6

    message_severity_debug = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
        return meta._meta_table['SystemMessageSeverityEnum']



class Logging(object):
    """
    Logging History data
    
    .. attribute:: history
    
    	Syslog Info 
    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Logging.History>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2016-06-24'

    def __init__(self):
        self.history = Logging.History()
        self.history.parent = self


    class History(object):
        """
        Syslog Info 
        
        .. attribute:: message
        
        	Syslog Message
        	**type**\:  str
        
        .. attribute:: properties
        
        	Syslog Properties
        	**type**\:  str
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            self.parent = None
            self.message = None
            self.properties = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:logging/Cisco-IOS-XR-infra-syslog-oper:history'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.message is not None:
                return True

            if self.properties is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Logging.History']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-oper:logging'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.history is not None and self.history._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
        return meta._meta_table['Logging']['meta_info']


class Syslog(object):
    """
    syslog
    
    .. attribute:: an_remote_servers
    
    	Logging AN remote servers information
    	**type**\:   :py:class:`AnRemoteServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers>`
    
    .. attribute:: logging_files
    
    	Logging Files information
    	**type**\:   :py:class:`LoggingFiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingFiles>`
    
    .. attribute:: logging_statistics
    
    	Logging statistics information
    	**type**\:   :py:class:`LoggingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics>`
    
    .. attribute:: messages
    
    	Message table information
    	**type**\:   :py:class:`Messages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2016-06-24'

    def __init__(self):
        self.an_remote_servers = Syslog.AnRemoteServers()
        self.an_remote_servers.parent = self
        self.logging_files = Syslog.LoggingFiles()
        self.logging_files.parent = self
        self.logging_statistics = Syslog.LoggingStatistics()
        self.logging_statistics.parent = self
        self.messages = Syslog.Messages()
        self.messages.parent = self


    class LoggingFiles(object):
        """
        Logging Files information
        
        .. attribute:: file_log_detail
        
        	Logging Files
        	**type**\: list of    :py:class:`FileLogDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingFiles.FileLogDetail>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            self.parent = None
            self.file_log_detail = YList()
            self.file_log_detail.parent = self
            self.file_log_detail.name = 'file_log_detail'


        class FileLogDetail(object):
            """
            Logging Files
            
            .. attribute:: file_name
            
            	File name for logging messages
            	**type**\:  str
            
            .. attribute:: file_path
            
            	File path for logging messages
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.file_name = None
                self.file_path = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-files/Cisco-IOS-XR-infra-syslog-oper:file-log-detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.file_name is not None:
                    return True

                if self.file_path is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingFiles.FileLogDetail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-files'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.file_log_detail is not None:
                for child_ref in self.file_log_detail:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.LoggingFiles']['meta_info']


    class AnRemoteServers(object):
        """
        Logging AN remote servers information
        
        .. attribute:: an_remote_log_server
        
        	AN Remote Log Servers
        	**type**\: list of    :py:class:`AnRemoteLogServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers.AnRemoteLogServer>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            self.parent = None
            self.an_remote_log_server = YList()
            self.an_remote_log_server.parent = self
            self.an_remote_log_server.name = 'an_remote_log_server'


        class AnRemoteLogServer(object):
            """
            AN Remote Log Servers
            
            .. attribute:: ip_address
            
            	IP Address
            	**type**\:  str
            
            .. attribute:: rh_discriminator
            
            	Remote\-Host Discriminator
            	**type**\:  str
            
            .. attribute:: vrf_name
            
            	VRF Name
            	**type**\:  str
            
            .. attribute:: vrf_severity
            
            	VRF Severity
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.ip_address = None
                self.rh_discriminator = None
                self.vrf_name = None
                self.vrf_severity = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:an-remote-servers/Cisco-IOS-XR-infra-syslog-oper:an-remote-log-server'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ip_address is not None:
                    return True

                if self.rh_discriminator is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vrf_severity is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.AnRemoteServers.AnRemoteLogServer']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:an-remote-servers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.an_remote_log_server is not None:
                for child_ref in self.an_remote_log_server:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.AnRemoteServers']['meta_info']


    class Messages(object):
        """
        Message table information
        
        .. attribute:: message
        
        	A system message
        	**type**\: list of    :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages.Message>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            self.parent = None
            self.message = YList()
            self.message.parent = self
            self.message.name = 'message'


        class Message(object):
            """
            A system message
            
            .. attribute:: message_id  <key>
            
            	Message ID of the system message
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: card_type
            
            	Message card location\: 'RP', 'DRP', 'LC', 'SC', 'SP' or 'UNK' 
            	**type**\:  str
            
            .. attribute:: category
            
            	Message category
            	**type**\:  str
            
            .. attribute:: group
            
            	Message group
            	**type**\:  str
            
            .. attribute:: message_name
            
            	Message name
            	**type**\:  str
            
            .. attribute:: node_name
            
            	Message source location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process_name
            
            	Process name
            	**type**\:  str
            
            .. attribute:: severity
            
            	Message severity
            	**type**\:   :py:class:`SystemMessageSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            .. attribute:: text
            
            	Additional message text
            	**type**\:  str
            
            .. attribute:: time_of_day
            
            	Time of day of event in DDD MMM DD  YYYY HH\:MM \:SS format, e.g Wed Apr 01 2009  15\:50\:26
            	**type**\:  str
            
            .. attribute:: time_stamp
            
            	Time in milliseconds since 00\:00\:00 UTC, January 11970 of when message was generated
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: millisecond
            
            .. attribute:: time_zone
            
            	Time Zone in UTC+/\-HH\:MM format,  e.g UTC+5\:30, UTC\-6
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.message_id = None
                self.card_type = None
                self.category = None
                self.group = None
                self.message_name = None
                self.node_name = None
                self.process_name = None
                self.severity = None
                self.text = None
                self.time_of_day = None
                self.time_stamp = None
                self.time_zone = None

            @property
            def _common_path(self):
                if self.message_id is None:
                    raise YPYModelError('Key property message_id is None')

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:messages/Cisco-IOS-XR-infra-syslog-oper:message[Cisco-IOS-XR-infra-syslog-oper:message-id = ' + str(self.message_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.message_id is not None:
                    return True

                if self.card_type is not None:
                    return True

                if self.category is not None:
                    return True

                if self.group is not None:
                    return True

                if self.message_name is not None:
                    return True

                if self.node_name is not None:
                    return True

                if self.process_name is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.text is not None:
                    return True

                if self.time_of_day is not None:
                    return True

                if self.time_stamp is not None:
                    return True

                if self.time_zone is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.Messages.Message']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:messages'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.message is not None:
                for child_ref in self.message:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.Messages']['meta_info']


    class LoggingStatistics(object):
        """
        Logging statistics information
        
        .. attribute:: buffer_logging_stats
        
        	Buffer logging statistics
        	**type**\:   :py:class:`BufferLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.BufferLoggingStats>`
        
        .. attribute:: console_logging_stats
        
        	Console logging statistics
        	**type**\:   :py:class:`ConsoleLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.ConsoleLoggingStats>`
        
        .. attribute:: file_logging_stat
        
        	File logging statistics
        	**type**\: list of    :py:class:`FileLoggingStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.FileLoggingStat>`
        
        .. attribute:: logging_stats
        
        	Logging statistics
        	**type**\:   :py:class:`LoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.LoggingStats>`
        
        .. attribute:: monitor_logging_stats
        
        	Monitor loggingstatistics
        	**type**\:   :py:class:`MonitorLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.MonitorLoggingStats>`
        
        .. attribute:: remote_logging_stat
        
        	Remote logging statistics
        	**type**\: list of    :py:class:`RemoteLoggingStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.RemoteLoggingStat>`
        
        .. attribute:: tls_remote_logging_stat
        
        	TLS Remote logging statistics
        	**type**\: list of    :py:class:`TlsRemoteLoggingStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.TlsRemoteLoggingStat>`
        
        .. attribute:: trap_logging_stats
        
        	Trap logging statistics
        	**type**\:   :py:class:`TrapLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.TrapLoggingStats>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            self.parent = None
            self.buffer_logging_stats = Syslog.LoggingStatistics.BufferLoggingStats()
            self.buffer_logging_stats.parent = self
            self.console_logging_stats = Syslog.LoggingStatistics.ConsoleLoggingStats()
            self.console_logging_stats.parent = self
            self.file_logging_stat = YList()
            self.file_logging_stat.parent = self
            self.file_logging_stat.name = 'file_logging_stat'
            self.logging_stats = Syslog.LoggingStatistics.LoggingStats()
            self.logging_stats.parent = self
            self.monitor_logging_stats = Syslog.LoggingStatistics.MonitorLoggingStats()
            self.monitor_logging_stats.parent = self
            self.remote_logging_stat = YList()
            self.remote_logging_stat.parent = self
            self.remote_logging_stat.name = 'remote_logging_stat'
            self.tls_remote_logging_stat = YList()
            self.tls_remote_logging_stat.parent = self
            self.tls_remote_logging_stat.name = 'tls_remote_logging_stat'
            self.trap_logging_stats = Syslog.LoggingStatistics.TrapLoggingStats()
            self.trap_logging_stats.parent = self


        class LoggingStats(object):
            """
            Logging statistics
            
            .. attribute:: drop_count
            
            	Number of messages dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: flush_count
            
            	Number of messages flushed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\:  bool
            
            .. attribute:: overrun_count
            
            	Number of messages overrun
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.drop_count = None
                self.flush_count = None
                self.is_log_enabled = None
                self.overrun_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.drop_count is not None:
                    return True

                if self.flush_count is not None:
                    return True

                if self.is_log_enabled is not None:
                    return True

                if self.overrun_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.LoggingStats']['meta_info']


        class ConsoleLoggingStats(object):
            """
            Console logging statistics
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\:  bool
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:   :py:class:`SystemMessageSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.buffer_size = None
                self.is_log_enabled = None
                self.message_count = None
                self.severity = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:console-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.buffer_size is not None:
                    return True

                if self.is_log_enabled is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.severity is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.ConsoleLoggingStats']['meta_info']


        class MonitorLoggingStats(object):
            """
            Monitor loggingstatistics
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\:  bool
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:   :py:class:`SystemMessageSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.buffer_size = None
                self.is_log_enabled = None
                self.message_count = None
                self.severity = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:monitor-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.buffer_size is not None:
                    return True

                if self.is_log_enabled is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.severity is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.MonitorLoggingStats']['meta_info']


        class TrapLoggingStats(object):
            """
            Trap logging statistics
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\:  bool
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:   :py:class:`SystemMessageSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.buffer_size = None
                self.is_log_enabled = None
                self.message_count = None
                self.severity = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:trap-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.buffer_size is not None:
                    return True

                if self.is_log_enabled is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.severity is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.TrapLoggingStats']['meta_info']


        class BufferLoggingStats(object):
            """
            Buffer logging statistics
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\:  bool
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:   :py:class:`SystemMessageSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.buffer_size = None
                self.is_log_enabled = None
                self.message_count = None
                self.severity = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:buffer-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.buffer_size is not None:
                    return True

                if self.is_log_enabled is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.severity is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.BufferLoggingStats']['meta_info']


        class RemoteLoggingStat(object):
            """
            Remote logging statistics
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_host_name
            
            	Remote hostname
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.message_count = None
                self.remote_host_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:remote-logging-stat'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.message_count is not None:
                    return True

                if self.remote_host_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.RemoteLoggingStat']['meta_info']


        class TlsRemoteLoggingStat(object):
            """
            TLS Remote logging statistics
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_host_name
            
            	TLS Remote hostname
            	**type**\:  str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.message_count = None
                self.remote_host_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:tls-remote-logging-stat'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.message_count is not None:
                    return True

                if self.remote_host_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.TlsRemoteLoggingStat']['meta_info']


        class FileLoggingStat(object):
            """
            File logging statistics
            
            .. attribute:: file_name
            
            	File name for logging messages
            	**type**\:  str
            
            .. attribute:: message_count
            
            	Message count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                self.parent = None
                self.file_name = None
                self.message_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:file-logging-stat'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.file_name is not None:
                    return True

                if self.message_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.FileLoggingStat']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.buffer_logging_stats is not None and self.buffer_logging_stats._has_data():
                return True

            if self.console_logging_stats is not None and self.console_logging_stats._has_data():
                return True

            if self.file_logging_stat is not None:
                for child_ref in self.file_logging_stat:
                    if child_ref._has_data():
                        return True

            if self.logging_stats is not None and self.logging_stats._has_data():
                return True

            if self.monitor_logging_stats is not None and self.monitor_logging_stats._has_data():
                return True

            if self.remote_logging_stat is not None:
                for child_ref in self.remote_logging_stat:
                    if child_ref._has_data():
                        return True

            if self.tls_remote_logging_stat is not None:
                for child_ref in self.tls_remote_logging_stat:
                    if child_ref._has_data():
                        return True

            if self.trap_logging_stats is not None and self.trap_logging_stats._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.LoggingStatistics']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-oper:syslog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.an_remote_servers is not None and self.an_remote_servers._has_data():
            return True

        if self.logging_files is not None and self.logging_files._has_data():
            return True

        if self.logging_statistics is not None and self.logging_statistics._has_data():
            return True

        if self.messages is not None and self.messages._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
        return meta._meta_table['Syslog']['meta_info']


