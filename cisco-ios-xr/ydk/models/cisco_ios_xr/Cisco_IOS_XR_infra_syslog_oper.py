""" Cisco_IOS_XR_infra_syslog_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-syslog package operational data.

This module contains definitions
for the following management objects\:
  logging\: Logging History data
  syslog\: syslog

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SystemMessageSeverity(Enum):
    """
    SystemMessageSeverity (Enum Class)

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

    message_severity_unknown = Enum.YLeaf(-1, "message-severity-unknown")

    message_severity_emergency = Enum.YLeaf(0, "message-severity-emergency")

    message_severity_alert = Enum.YLeaf(1, "message-severity-alert")

    message_severity_critical = Enum.YLeaf(2, "message-severity-critical")

    message_severity_error = Enum.YLeaf(3, "message-severity-error")

    message_severity_warning = Enum.YLeaf(4, "message-severity-warning")

    message_severity_notice = Enum.YLeaf(5, "message-severity-notice")

    message_severity_informational = Enum.YLeaf(6, "message-severity-informational")

    message_severity_debug = Enum.YLeaf(7, "message-severity-debug")



class GetSyslog(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Output>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2018-02-23'

    def __init__(self):
        super(GetSyslog, self).__init__()
        self._top_entity = None

        self.yang_name = "get-syslog"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = GetSyslog.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = GetSyslog.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: filters
        
        	A set of filters of syslog messages to be returned
        	**type**\:  :py:class:`Filters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Input.Filters>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(GetSyslog.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("filters", ("filters", GetSyslog.Input.Filters))])
            self._leafs = OrderedDict()

            self.filters = GetSyslog.Input.Filters()
            self.filters.parent = self
            self._children_name_map["filters"] = "filters"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetSyslog.Input, [], name, value)


        class Filters(Entity):
            """
            A set of filters of syslog messages to be returned
            
            .. attribute:: start_time
            
            	Start timestamp of syslog messages to be returned
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: end_time
            
            	End timestamp of syslog messages to be returned
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(GetSyslog.Input.Filters, self).__init__()

                self.yang_name = "filters"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                    ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                ])
                self.start_time = None
                self.end_time = None
                self._segment_path = lambda: "filters"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GetSyslog.Input.Filters, ['start_time', 'end_time'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: data
        
        	Output for RPC operation
        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Output.Data>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(GetSyslog.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("data", ("data", GetSyslog.Output.Data))])
            self._leafs = OrderedDict()

            self.data = GetSyslog.Output.Data()
            self.data.parent = self
            self._children_name_map["data"] = "data"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetSyslog.Output, [], name, value)


        class Data(Entity):
            """
            Output for RPC operation
            
            .. attribute:: syslog
            
            	syslog
            	**type**\:  :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Output.Data.Syslog>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(GetSyslog.Output.Data, self).__init__()

                self.yang_name = "data"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("syslog", ("syslog", GetSyslog.Output.Data.Syslog))])
                self._leafs = OrderedDict()

                self.syslog = GetSyslog.Output.Data.Syslog()
                self.syslog.parent = self
                self._children_name_map["syslog"] = "syslog"
                self._segment_path = lambda: "data"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GetSyslog.Output.Data, [], name, value)


            class Syslog(Entity):
                """
                syslog
                
                .. attribute:: messages
                
                	Message table information
                	**type**\:  :py:class:`Messages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Output.Data.Syslog.Messages>`
                
                

                """

                _prefix = 'infra-syslog-oper'
                _revision = '2018-02-23'

                def __init__(self):
                    super(GetSyslog.Output.Data.Syslog, self).__init__()

                    self.yang_name = "syslog"
                    self.yang_parent_name = "data"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("messages", ("messages", GetSyslog.Output.Data.Syslog.Messages))])
                    self._leafs = OrderedDict()

                    self.messages = GetSyslog.Output.Data.Syslog.Messages()
                    self.messages.parent = self
                    self._children_name_map["messages"] = "messages"
                    self._segment_path = lambda: "syslog"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/output/data/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GetSyslog.Output.Data.Syslog, [], name, value)


                class Messages(Entity):
                    """
                    Message table information
                    
                    .. attribute:: message
                    
                    	A system message
                    	**type**\: list of  		 :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.GetSyslog.Output.Data.Syslog.Messages.Message>`
                    
                    

                    """

                    _prefix = 'infra-syslog-oper'
                    _revision = '2018-02-23'

                    def __init__(self):
                        super(GetSyslog.Output.Data.Syslog.Messages, self).__init__()

                        self.yang_name = "messages"
                        self.yang_parent_name = "syslog"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("message", ("message", GetSyslog.Output.Data.Syslog.Messages.Message))])
                        self._leafs = OrderedDict()

                        self.message = YList(self)
                        self._segment_path = lambda: "messages"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/output/data/syslog/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GetSyslog.Output.Data.Syslog.Messages, [], name, value)


                    class Message(Entity):
                        """
                        A system message
                        
                        .. attribute:: message_id  (key)
                        
                        	Message ID of the system message
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: card_type
                        
                        	Message card location\: 'RP', 'DRP', 'LC', 'SC', 'SP' or 'UNK' 
                        	**type**\: str
                        
                        .. attribute:: node_name
                        
                        	Message source location
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: time_stamp
                        
                        	Time in milliseconds since 00\:00\:00 UTC, January 11970 of when message was generated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: millisecond
                        
                        .. attribute:: time_of_day
                        
                        	Time of day of event in DDD MMM DD  YYYY HH\:MM \:SS format, e.g Wed Apr 01 2009  15\:50\:26
                        	**type**\: str
                        
                        .. attribute:: time_zone
                        
                        	Time Zone in UTC+/\-HH\:MM format,  e.g UTC+5\:30, UTC\-6
                        	**type**\: str
                        
                        .. attribute:: process_name
                        
                        	Process name
                        	**type**\: str
                        
                        .. attribute:: category
                        
                        	Message category
                        	**type**\: str
                        
                        .. attribute:: group
                        
                        	Message group
                        	**type**\: str
                        
                        .. attribute:: message_name
                        
                        	Message name
                        	**type**\: str
                        
                        .. attribute:: severity
                        
                        	Message severity
                        	**type**\:  :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
                        
                        .. attribute:: text
                        
                        	Additional message text
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-syslog-oper'
                        _revision = '2018-02-23'

                        def __init__(self):
                            super(GetSyslog.Output.Data.Syslog.Messages.Message, self).__init__()

                            self.yang_name = "message"
                            self.yang_parent_name = "messages"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['message_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('message_id', (YLeaf(YType.uint32, 'message-id'), ['int'])),
                                ('card_type', (YLeaf(YType.str, 'card-type'), ['str'])),
                                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                ('time_of_day', (YLeaf(YType.str, 'time-of-day'), ['str'])),
                                ('time_zone', (YLeaf(YType.str, 'time-zone'), ['str'])),
                                ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                                ('category', (YLeaf(YType.str, 'category'), ['str'])),
                                ('group', (YLeaf(YType.str, 'group'), ['str'])),
                                ('message_name', (YLeaf(YType.str, 'message-name'), ['str'])),
                                ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverity', '')])),
                                ('text', (YLeaf(YType.str, 'text'), ['str'])),
                            ])
                            self.message_id = None
                            self.card_type = None
                            self.node_name = None
                            self.time_stamp = None
                            self.time_of_day = None
                            self.time_zone = None
                            self.process_name = None
                            self.category = None
                            self.group = None
                            self.message_name = None
                            self.severity = None
                            self.text = None
                            self._segment_path = lambda: "message" + "[message-id='" + str(self.message_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:get-syslog/output/data/syslog/messages/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GetSyslog.Output.Data.Syslog.Messages.Message, ['message_id', u'card_type', u'node_name', u'time_stamp', u'time_of_day', u'time_zone', u'process_name', u'category', u'group', u'message_name', u'severity', u'text'], name, value)

    def clone_ptr(self):
        self._top_entity = GetSyslog()
        return self._top_entity

class Logging(Entity):
    """
    Logging History data
    
    .. attribute:: history
    
    	Syslog Info 
    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Logging.History>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2018-02-23'

    def __init__(self):
        super(Logging, self).__init__()
        self._top_entity = None

        self.yang_name = "logging"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("history", ("history", Logging.History))])
        self._leafs = OrderedDict()

        self.history = Logging.History()
        self.history.parent = self
        self._children_name_map["history"] = "history"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:logging"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Logging, [], name, value)


    class History(Entity):
        """
        Syslog Info 
        
        .. attribute:: properties
        
        	Syslog Properties
        	**type**\: str
        
        .. attribute:: message
        
        	Syslog Message
        	**type**\: str
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(Logging.History, self).__init__()

            self.yang_name = "history"
            self.yang_parent_name = "logging"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('properties', (YLeaf(YType.str, 'properties'), ['str'])),
                ('message', (YLeaf(YType.str, 'message'), ['str'])),
            ])
            self.properties = None
            self.message = None
            self._segment_path = lambda: "history"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:logging/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Logging.History, ['properties', 'message'], name, value)

    def clone_ptr(self):
        self._top_entity = Logging()
        return self._top_entity

class Syslog(Entity):
    """
    syslog
    
    .. attribute:: logging_files
    
    	Logging Files information
    	**type**\:  :py:class:`LoggingFiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingFiles>`
    
    .. attribute:: an_remote_servers
    
    	Logging AN remote servers information
    	**type**\:  :py:class:`AnRemoteServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers>`
    
    .. attribute:: messages
    
    	Message table information
    	**type**\:  :py:class:`Messages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages>`
    
    .. attribute:: logging_statistics
    
    	Logging statistics information
    	**type**\:  :py:class:`LoggingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2018-02-23'

    def __init__(self):
        super(Syslog, self).__init__()
        self._top_entity = None

        self.yang_name = "syslog"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("logging-files", ("logging_files", Syslog.LoggingFiles)), ("an-remote-servers", ("an_remote_servers", Syslog.AnRemoteServers)), ("messages", ("messages", Syslog.Messages)), ("logging-statistics", ("logging_statistics", Syslog.LoggingStatistics))])
        self._leafs = OrderedDict()

        self.logging_files = Syslog.LoggingFiles()
        self.logging_files.parent = self
        self._children_name_map["logging_files"] = "logging-files"

        self.an_remote_servers = Syslog.AnRemoteServers()
        self.an_remote_servers.parent = self
        self._children_name_map["an_remote_servers"] = "an-remote-servers"

        self.messages = Syslog.Messages()
        self.messages.parent = self
        self._children_name_map["messages"] = "messages"

        self.logging_statistics = Syslog.LoggingStatistics()
        self.logging_statistics.parent = self
        self._children_name_map["logging_statistics"] = "logging-statistics"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Syslog, [], name, value)


    class LoggingFiles(Entity):
        """
        Logging Files information
        
        .. attribute:: file_log_detail
        
        	Logging Files
        	**type**\: list of  		 :py:class:`FileLogDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingFiles.FileLogDetail>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(Syslog.LoggingFiles, self).__init__()

            self.yang_name = "logging-files"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("file-log-detail", ("file_log_detail", Syslog.LoggingFiles.FileLogDetail))])
            self._leafs = OrderedDict()

            self.file_log_detail = YList(self)
            self._segment_path = lambda: "logging-files"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.LoggingFiles, [], name, value)


        class FileLogDetail(Entity):
            """
            Logging Files
            
            .. attribute:: file_path
            
            	File path for logging messages
            	**type**\: str
            
            .. attribute:: file_name
            
            	File name for logging messages
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingFiles.FileLogDetail, self).__init__()

                self.yang_name = "file-log-detail"
                self.yang_parent_name = "logging-files"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('file_path', (YLeaf(YType.str, 'file-path'), ['str'])),
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                ])
                self.file_path = None
                self.file_name = None
                self._segment_path = lambda: "file-log-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-files/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingFiles.FileLogDetail, [u'file_path', u'file_name'], name, value)


    class AnRemoteServers(Entity):
        """
        Logging AN remote servers information
        
        .. attribute:: an_remote_log_server
        
        	AN Remote Log Servers
        	**type**\: list of  		 :py:class:`AnRemoteLogServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers.AnRemoteLogServer>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(Syslog.AnRemoteServers, self).__init__()

            self.yang_name = "an-remote-servers"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("an-remote-log-server", ("an_remote_log_server", Syslog.AnRemoteServers.AnRemoteLogServer))])
            self._leafs = OrderedDict()

            self.an_remote_log_server = YList(self)
            self._segment_path = lambda: "an-remote-servers"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.AnRemoteServers, [], name, value)


        class AnRemoteLogServer(Entity):
            """
            AN Remote Log Servers
            
            .. attribute:: ip_address
            
            	IP Address
            	**type**\: str
            
            .. attribute:: vrf_name
            
            	VRF Name
            	**type**\: str
            
            .. attribute:: vrf_severity
            
            	VRF Severity
            	**type**\: str
            
            .. attribute:: rh_discriminator
            
            	Remote\-Host Discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.AnRemoteServers.AnRemoteLogServer, self).__init__()

                self.yang_name = "an-remote-log-server"
                self.yang_parent_name = "an-remote-servers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('vrf_severity', (YLeaf(YType.str, 'vrf-severity'), ['str'])),
                    ('rh_discriminator', (YLeaf(YType.str, 'rh-discriminator'), ['str'])),
                ])
                self.ip_address = None
                self.vrf_name = None
                self.vrf_severity = None
                self.rh_discriminator = None
                self._segment_path = lambda: "an-remote-log-server"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/an-remote-servers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.AnRemoteServers.AnRemoteLogServer, [u'ip_address', u'vrf_name', u'vrf_severity', u'rh_discriminator'], name, value)


    class Messages(Entity):
        """
        Message table information
        
        .. attribute:: message
        
        	A system message
        	**type**\: list of  		 :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages.Message>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(Syslog.Messages, self).__init__()

            self.yang_name = "messages"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("message", ("message", Syslog.Messages.Message))])
            self._leafs = OrderedDict()

            self.message = YList(self)
            self._segment_path = lambda: "messages"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.Messages, [], name, value)


        class Message(Entity):
            """
            A system message
            
            .. attribute:: message_id  (key)
            
            	Message ID of the system message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: card_type
            
            	Message card location\: 'RP', 'DRP', 'LC', 'SC', 'SP' or 'UNK' 
            	**type**\: str
            
            .. attribute:: node_name
            
            	Message source location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: time_stamp
            
            	Time in milliseconds since 00\:00\:00 UTC, January 11970 of when message was generated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: millisecond
            
            .. attribute:: time_of_day
            
            	Time of day of event in DDD MMM DD  YYYY HH\:MM \:SS format, e.g Wed Apr 01 2009  15\:50\:26
            	**type**\: str
            
            .. attribute:: time_zone
            
            	Time Zone in UTC+/\-HH\:MM format,  e.g UTC+5\:30, UTC\-6
            	**type**\: str
            
            .. attribute:: process_name
            
            	Process name
            	**type**\: str
            
            .. attribute:: category
            
            	Message category
            	**type**\: str
            
            .. attribute:: group
            
            	Message group
            	**type**\: str
            
            .. attribute:: message_name
            
            	Message name
            	**type**\: str
            
            .. attribute:: severity
            
            	Message severity
            	**type**\:  :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            .. attribute:: text
            
            	Additional message text
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.Messages.Message, self).__init__()

                self.yang_name = "message"
                self.yang_parent_name = "messages"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message_id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message_id', (YLeaf(YType.uint32, 'message-id'), ['int'])),
                    ('card_type', (YLeaf(YType.str, 'card-type'), ['str'])),
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                    ('time_of_day', (YLeaf(YType.str, 'time-of-day'), ['str'])),
                    ('time_zone', (YLeaf(YType.str, 'time-zone'), ['str'])),
                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                    ('category', (YLeaf(YType.str, 'category'), ['str'])),
                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                    ('message_name', (YLeaf(YType.str, 'message-name'), ['str'])),
                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverity', '')])),
                    ('text', (YLeaf(YType.str, 'text'), ['str'])),
                ])
                self.message_id = None
                self.card_type = None
                self.node_name = None
                self.time_stamp = None
                self.time_of_day = None
                self.time_zone = None
                self.process_name = None
                self.category = None
                self.group = None
                self.message_name = None
                self.severity = None
                self.text = None
                self._segment_path = lambda: "message" + "[message-id='" + str(self.message_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/messages/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.Messages.Message, ['message_id', u'card_type', u'node_name', u'time_stamp', u'time_of_day', u'time_zone', u'process_name', u'category', u'group', u'message_name', u'severity', u'text'], name, value)


    class LoggingStatistics(Entity):
        """
        Logging statistics information
        
        .. attribute:: logging_stats
        
        	Logging statistics
        	**type**\:  :py:class:`LoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.LoggingStats>`
        
        .. attribute:: console_logging_stats
        
        	Console logging statistics
        	**type**\:  :py:class:`ConsoleLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.ConsoleLoggingStats>`
        
        .. attribute:: monitor_logging_stats
        
        	Monitor loggingstatistics
        	**type**\:  :py:class:`MonitorLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.MonitorLoggingStats>`
        
        .. attribute:: trap_logging_stats
        
        	Trap logging statistics
        	**type**\:  :py:class:`TrapLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.TrapLoggingStats>`
        
        .. attribute:: buffer_logging_stats
        
        	Buffer logging statistics
        	**type**\:  :py:class:`BufferLoggingStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.BufferLoggingStats>`
        
        .. attribute:: remote_logging_stat
        
        	Remote logging statistics
        	**type**\: list of  		 :py:class:`RemoteLoggingStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.RemoteLoggingStat>`
        
        .. attribute:: tls_remote_logging_stat
        
        	TLS Remote logging statistics
        	**type**\: list of  		 :py:class:`TlsRemoteLoggingStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.TlsRemoteLoggingStat>`
        
        .. attribute:: file_logging_stat
        
        	File logging statistics
        	**type**\: list of  		 :py:class:`FileLoggingStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.FileLoggingStat>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2018-02-23'

        def __init__(self):
            super(Syslog.LoggingStatistics, self).__init__()

            self.yang_name = "logging-statistics"
            self.yang_parent_name = "syslog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("logging-stats", ("logging_stats", Syslog.LoggingStatistics.LoggingStats)), ("console-logging-stats", ("console_logging_stats", Syslog.LoggingStatistics.ConsoleLoggingStats)), ("monitor-logging-stats", ("monitor_logging_stats", Syslog.LoggingStatistics.MonitorLoggingStats)), ("trap-logging-stats", ("trap_logging_stats", Syslog.LoggingStatistics.TrapLoggingStats)), ("buffer-logging-stats", ("buffer_logging_stats", Syslog.LoggingStatistics.BufferLoggingStats)), ("remote-logging-stat", ("remote_logging_stat", Syslog.LoggingStatistics.RemoteLoggingStat)), ("tls-remote-logging-stat", ("tls_remote_logging_stat", Syslog.LoggingStatistics.TlsRemoteLoggingStat)), ("file-logging-stat", ("file_logging_stat", Syslog.LoggingStatistics.FileLoggingStat))])
            self._leafs = OrderedDict()

            self.logging_stats = Syslog.LoggingStatistics.LoggingStats()
            self.logging_stats.parent = self
            self._children_name_map["logging_stats"] = "logging-stats"

            self.console_logging_stats = Syslog.LoggingStatistics.ConsoleLoggingStats()
            self.console_logging_stats.parent = self
            self._children_name_map["console_logging_stats"] = "console-logging-stats"

            self.monitor_logging_stats = Syslog.LoggingStatistics.MonitorLoggingStats()
            self.monitor_logging_stats.parent = self
            self._children_name_map["monitor_logging_stats"] = "monitor-logging-stats"

            self.trap_logging_stats = Syslog.LoggingStatistics.TrapLoggingStats()
            self.trap_logging_stats.parent = self
            self._children_name_map["trap_logging_stats"] = "trap-logging-stats"

            self.buffer_logging_stats = Syslog.LoggingStatistics.BufferLoggingStats()
            self.buffer_logging_stats.parent = self
            self._children_name_map["buffer_logging_stats"] = "buffer-logging-stats"

            self.remote_logging_stat = YList(self)
            self.tls_remote_logging_stat = YList(self)
            self.file_logging_stat = YList(self)
            self._segment_path = lambda: "logging-statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Syslog.LoggingStatistics, [], name, value)


        class LoggingStats(Entity):
            """
            Logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: drop_count
            
            	Number of messages dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: flush_count
            
            	Number of messages flushed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: overrun_count
            
            	Number of messages overrun
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.LoggingStats, self).__init__()

                self.yang_name = "logging-stats"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_log_enabled', (YLeaf(YType.boolean, 'is-log-enabled'), ['bool'])),
                    ('drop_count', (YLeaf(YType.uint32, 'drop-count'), ['int'])),
                    ('flush_count', (YLeaf(YType.uint32, 'flush-count'), ['int'])),
                    ('overrun_count', (YLeaf(YType.uint32, 'overrun-count'), ['int'])),
                ])
                self.is_log_enabled = None
                self.drop_count = None
                self.flush_count = None
                self.overrun_count = None
                self._segment_path = lambda: "logging-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.LoggingStats, [u'is_log_enabled', u'drop_count', u'flush_count', u'overrun_count'], name, value)


        class ConsoleLoggingStats(Entity):
            """
            Console logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:  :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.ConsoleLoggingStats, self).__init__()

                self.yang_name = "console-logging-stats"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_log_enabled', (YLeaf(YType.boolean, 'is-log-enabled'), ['bool'])),
                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverity', '')])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                    ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
                ])
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None
                self._segment_path = lambda: "console-logging-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.ConsoleLoggingStats, [u'is_log_enabled', u'severity', u'message_count', u'buffer_size'], name, value)


        class MonitorLoggingStats(Entity):
            """
            Monitor loggingstatistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:  :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.MonitorLoggingStats, self).__init__()

                self.yang_name = "monitor-logging-stats"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_log_enabled', (YLeaf(YType.boolean, 'is-log-enabled'), ['bool'])),
                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverity', '')])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                    ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
                ])
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None
                self._segment_path = lambda: "monitor-logging-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.MonitorLoggingStats, [u'is_log_enabled', u'severity', u'message_count', u'buffer_size'], name, value)


        class TrapLoggingStats(Entity):
            """
            Trap logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:  :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.TrapLoggingStats, self).__init__()

                self.yang_name = "trap-logging-stats"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_log_enabled', (YLeaf(YType.boolean, 'is-log-enabled'), ['bool'])),
                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverity', '')])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                    ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
                ])
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None
                self._segment_path = lambda: "trap-logging-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.TrapLoggingStats, [u'is_log_enabled', u'severity', u'message_count', u'buffer_size'], name, value)


        class BufferLoggingStats(Entity):
            """
            Buffer logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\:  :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: byte
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.BufferLoggingStats, self).__init__()

                self.yang_name = "buffer-logging-stats"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_log_enabled', (YLeaf(YType.boolean, 'is-log-enabled'), ['bool'])),
                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper', 'SystemMessageSeverity', '')])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                    ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
                ])
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None
                self._segment_path = lambda: "buffer-logging-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.BufferLoggingStats, [u'is_log_enabled', u'severity', u'message_count', u'buffer_size'], name, value)


        class RemoteLoggingStat(Entity):
            """
            Remote logging statistics
            
            .. attribute:: remote_host_name
            
            	Remote hostname
            	**type**\: str
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.RemoteLoggingStat, self).__init__()

                self.yang_name = "remote-logging-stat"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('remote_host_name', (YLeaf(YType.str, 'remote-host-name'), ['str'])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                ])
                self.remote_host_name = None
                self.message_count = None
                self._segment_path = lambda: "remote-logging-stat"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.RemoteLoggingStat, [u'remote_host_name', u'message_count'], name, value)


        class TlsRemoteLoggingStat(Entity):
            """
            TLS Remote logging statistics
            
            .. attribute:: remote_host_name
            
            	TLS Remote hostname
            	**type**\: str
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.TlsRemoteLoggingStat, self).__init__()

                self.yang_name = "tls-remote-logging-stat"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('remote_host_name', (YLeaf(YType.str, 'remote-host-name'), ['str'])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                ])
                self.remote_host_name = None
                self.message_count = None
                self._segment_path = lambda: "tls-remote-logging-stat"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.TlsRemoteLoggingStat, [u'remote_host_name', u'message_count'], name, value)


        class FileLoggingStat(Entity):
            """
            File logging statistics
            
            .. attribute:: file_name
            
            	File name for logging messages
            	**type**\: str
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2018-02-23'

            def __init__(self):
                super(Syslog.LoggingStatistics.FileLoggingStat, self).__init__()

                self.yang_name = "file-logging-stat"
                self.yang_parent_name = "logging-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('file_name', (YLeaf(YType.str, 'file-name'), ['str'])),
                    ('message_count', (YLeaf(YType.uint32, 'message-count'), ['int'])),
                ])
                self.file_name = None
                self.message_count = None
                self._segment_path = lambda: "file-logging-stat"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Syslog.LoggingStatistics.FileLoggingStat, [u'file_name', u'message_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Syslog()
        return self._top_entity

