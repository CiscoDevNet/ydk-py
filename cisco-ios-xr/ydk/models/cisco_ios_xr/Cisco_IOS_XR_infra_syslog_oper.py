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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SystemMessageSeverity(Enum):
    """
    SystemMessageSeverity

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



class Logging(Entity):
    """
    Logging History data
    
    .. attribute:: history
    
    	Syslog Info 
    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Logging.History>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2016-06-24'

    def __init__(self):
        super(Logging, self).__init__()
        self._top_entity = None

        self.yang_name = "logging"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-oper"

        self.history = Logging.History()
        self.history.parent = self
        self._children_name_map["history"] = "history"
        self._children_yang_names.add("history")


    class History(Entity):
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
            super(Logging.History, self).__init__()

            self.yang_name = "history"
            self.yang_parent_name = "logging"

            self.message = YLeaf(YType.str, "message")

            self.properties = YLeaf(YType.str, "properties")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("message",
                            "properties") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Logging.History, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Logging.History, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.message.is_set or
                self.properties.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.message.yfilter != YFilter.not_set or
                self.properties.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "history" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-oper:logging/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.message.is_set or self.message.yfilter != YFilter.not_set):
                leaf_name_data.append(self.message.get_name_leafdata())
            if (self.properties.is_set or self.properties.yfilter != YFilter.not_set):
                leaf_name_data.append(self.properties.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "message" or name == "properties"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "message"):
                self.message = value
                self.message.value_namespace = name_space
                self.message.value_namespace_prefix = name_space_prefix
            if(value_path == "properties"):
                self.properties = value
                self.properties.value_namespace = name_space
                self.properties.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.history is not None and self.history.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.history is not None and self.history.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-syslog-oper:logging" + path_buffer

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

        if (child_yang_name == "history"):
            if (self.history is None):
                self.history = Logging.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"
            return self.history

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "history"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Logging()
        return self._top_entity

class Syslog(Entity):
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
        super(Syslog, self).__init__()
        self._top_entity = None

        self.yang_name = "syslog"
        self.yang_parent_name = "Cisco-IOS-XR-infra-syslog-oper"

        self.an_remote_servers = Syslog.AnRemoteServers()
        self.an_remote_servers.parent = self
        self._children_name_map["an_remote_servers"] = "an-remote-servers"
        self._children_yang_names.add("an-remote-servers")

        self.logging_files = Syslog.LoggingFiles()
        self.logging_files.parent = self
        self._children_name_map["logging_files"] = "logging-files"
        self._children_yang_names.add("logging-files")

        self.logging_statistics = Syslog.LoggingStatistics()
        self.logging_statistics.parent = self
        self._children_name_map["logging_statistics"] = "logging-statistics"
        self._children_yang_names.add("logging-statistics")

        self.messages = Syslog.Messages()
        self.messages.parent = self
        self._children_name_map["messages"] = "messages"
        self._children_yang_names.add("messages")


    class LoggingFiles(Entity):
        """
        Logging Files information
        
        .. attribute:: file_log_detail
        
        	Logging Files
        	**type**\: list of    :py:class:`FileLogDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingFiles.FileLogDetail>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            super(Syslog.LoggingFiles, self).__init__()

            self.yang_name = "logging-files"
            self.yang_parent_name = "syslog"

            self.file_log_detail = YList(self)

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
                        super(Syslog.LoggingFiles, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.LoggingFiles, self).__setattr__(name, value)


        class FileLogDetail(Entity):
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
                super(Syslog.LoggingFiles.FileLogDetail, self).__init__()

                self.yang_name = "file-log-detail"
                self.yang_parent_name = "logging-files"

                self.file_name = YLeaf(YType.str, "file-name")

                self.file_path = YLeaf(YType.str, "file-path")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("file_name",
                                "file_path") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingFiles.FileLogDetail, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingFiles.FileLogDetail, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.file_name.is_set or
                    self.file_path.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.file_name.yfilter != YFilter.not_set or
                    self.file_path.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "file-log-detail" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-files/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.file_name.is_set or self.file_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.file_name.get_name_leafdata())
                if (self.file_path.is_set or self.file_path.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.file_path.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file-name" or name == "file-path"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "file-name"):
                    self.file_name = value
                    self.file_name.value_namespace = name_space
                    self.file_name.value_namespace_prefix = name_space_prefix
                if(value_path == "file-path"):
                    self.file_path = value
                    self.file_path.value_namespace = name_space
                    self.file_path.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.file_log_detail:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.file_log_detail:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logging-files" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "file-log-detail"):
                for c in self.file_log_detail:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.LoggingFiles.FileLogDetail()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.file_log_detail.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "file-log-detail"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AnRemoteServers(Entity):
        """
        Logging AN remote servers information
        
        .. attribute:: an_remote_log_server
        
        	AN Remote Log Servers
        	**type**\: list of    :py:class:`AnRemoteLogServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers.AnRemoteLogServer>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            super(Syslog.AnRemoteServers, self).__init__()

            self.yang_name = "an-remote-servers"
            self.yang_parent_name = "syslog"

            self.an_remote_log_server = YList(self)

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
                        super(Syslog.AnRemoteServers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.AnRemoteServers, self).__setattr__(name, value)


        class AnRemoteLogServer(Entity):
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
                super(Syslog.AnRemoteServers.AnRemoteLogServer, self).__init__()

                self.yang_name = "an-remote-log-server"
                self.yang_parent_name = "an-remote-servers"

                self.ip_address = YLeaf(YType.str, "ip-address")

                self.rh_discriminator = YLeaf(YType.str, "rh-discriminator")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_severity = YLeaf(YType.str, "vrf-severity")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ip_address",
                                "rh_discriminator",
                                "vrf_name",
                                "vrf_severity") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.AnRemoteServers.AnRemoteLogServer, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.AnRemoteServers.AnRemoteLogServer, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ip_address.is_set or
                    self.rh_discriminator.is_set or
                    self.vrf_name.is_set or
                    self.vrf_severity.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ip_address.yfilter != YFilter.not_set or
                    self.rh_discriminator.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.vrf_severity.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "an-remote-log-server" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/an-remote-servers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip_address.get_name_leafdata())
                if (self.rh_discriminator.is_set or self.rh_discriminator.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rh_discriminator.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.vrf_severity.is_set or self.vrf_severity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_severity.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ip-address" or name == "rh-discriminator" or name == "vrf-name" or name == "vrf-severity"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ip-address"):
                    self.ip_address = value
                    self.ip_address.value_namespace = name_space
                    self.ip_address.value_namespace_prefix = name_space_prefix
                if(value_path == "rh-discriminator"):
                    self.rh_discriminator = value
                    self.rh_discriminator.value_namespace = name_space
                    self.rh_discriminator.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-severity"):
                    self.vrf_severity = value
                    self.vrf_severity.value_namespace = name_space
                    self.vrf_severity.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.an_remote_log_server:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.an_remote_log_server:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "an-remote-servers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "an-remote-log-server"):
                for c in self.an_remote_log_server:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.AnRemoteServers.AnRemoteLogServer()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.an_remote_log_server.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "an-remote-log-server"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Messages(Entity):
        """
        Message table information
        
        .. attribute:: message
        
        	A system message
        	**type**\: list of    :py:class:`Message <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages.Message>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2016-06-24'

        def __init__(self):
            super(Syslog.Messages, self).__init__()

            self.yang_name = "messages"
            self.yang_parent_name = "syslog"

            self.message = YList(self)

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
                        super(Syslog.Messages, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.Messages, self).__setattr__(name, value)


        class Message(Entity):
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
            	**type**\:   :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
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
                super(Syslog.Messages.Message, self).__init__()

                self.yang_name = "message"
                self.yang_parent_name = "messages"

                self.message_id = YLeaf(YType.int32, "message-id")

                self.card_type = YLeaf(YType.str, "card-type")

                self.category = YLeaf(YType.str, "category")

                self.group = YLeaf(YType.str, "group")

                self.message_name = YLeaf(YType.str, "message-name")

                self.node_name = YLeaf(YType.str, "node-name")

                self.process_name = YLeaf(YType.str, "process-name")

                self.severity = YLeaf(YType.enumeration, "severity")

                self.text = YLeaf(YType.str, "text")

                self.time_of_day = YLeaf(YType.str, "time-of-day")

                self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                self.time_zone = YLeaf(YType.str, "time-zone")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("message_id",
                                "card_type",
                                "category",
                                "group",
                                "message_name",
                                "node_name",
                                "process_name",
                                "severity",
                                "text",
                                "time_of_day",
                                "time_stamp",
                                "time_zone") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.Messages.Message, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.Messages.Message, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.message_id.is_set or
                    self.card_type.is_set or
                    self.category.is_set or
                    self.group.is_set or
                    self.message_name.is_set or
                    self.node_name.is_set or
                    self.process_name.is_set or
                    self.severity.is_set or
                    self.text.is_set or
                    self.time_of_day.is_set or
                    self.time_stamp.is_set or
                    self.time_zone.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.message_id.yfilter != YFilter.not_set or
                    self.card_type.yfilter != YFilter.not_set or
                    self.category.yfilter != YFilter.not_set or
                    self.group.yfilter != YFilter.not_set or
                    self.message_name.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.process_name.yfilter != YFilter.not_set or
                    self.severity.yfilter != YFilter.not_set or
                    self.text.yfilter != YFilter.not_set or
                    self.time_of_day.yfilter != YFilter.not_set or
                    self.time_stamp.yfilter != YFilter.not_set or
                    self.time_zone.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "message" + "[message-id='" + self.message_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/messages/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.message_id.is_set or self.message_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_id.get_name_leafdata())
                if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.card_type.get_name_leafdata())
                if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.category.get_name_leafdata())
                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group.get_name_leafdata())
                if (self.message_name.is_set or self.message_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_name.get_name_leafdata())
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
                if (self.process_name.is_set or self.process_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.process_name.get_name_leafdata())
                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.severity.get_name_leafdata())
                if (self.text.is_set or self.text.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.text.get_name_leafdata())
                if (self.time_of_day.is_set or self.time_of_day.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_of_day.get_name_leafdata())
                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_stamp.get_name_leafdata())
                if (self.time_zone.is_set or self.time_zone.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_zone.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "message-id" or name == "card-type" or name == "category" or name == "group" or name == "message-name" or name == "node-name" or name == "process-name" or name == "severity" or name == "text" or name == "time-of-day" or name == "time-stamp" or name == "time-zone"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "message-id"):
                    self.message_id = value
                    self.message_id.value_namespace = name_space
                    self.message_id.value_namespace_prefix = name_space_prefix
                if(value_path == "card-type"):
                    self.card_type = value
                    self.card_type.value_namespace = name_space
                    self.card_type.value_namespace_prefix = name_space_prefix
                if(value_path == "category"):
                    self.category = value
                    self.category.value_namespace = name_space
                    self.category.value_namespace_prefix = name_space_prefix
                if(value_path == "group"):
                    self.group = value
                    self.group.value_namespace = name_space
                    self.group.value_namespace_prefix = name_space_prefix
                if(value_path == "message-name"):
                    self.message_name = value
                    self.message_name.value_namespace = name_space
                    self.message_name.value_namespace_prefix = name_space_prefix
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "process-name"):
                    self.process_name = value
                    self.process_name.value_namespace = name_space
                    self.process_name.value_namespace_prefix = name_space_prefix
                if(value_path == "severity"):
                    self.severity = value
                    self.severity.value_namespace = name_space
                    self.severity.value_namespace_prefix = name_space_prefix
                if(value_path == "text"):
                    self.text = value
                    self.text.value_namespace = name_space
                    self.text.value_namespace_prefix = name_space_prefix
                if(value_path == "time-of-day"):
                    self.time_of_day = value
                    self.time_of_day.value_namespace = name_space
                    self.time_of_day.value_namespace_prefix = name_space_prefix
                if(value_path == "time-stamp"):
                    self.time_stamp = value
                    self.time_stamp.value_namespace = name_space
                    self.time_stamp.value_namespace_prefix = name_space_prefix
                if(value_path == "time-zone"):
                    self.time_zone = value
                    self.time_zone.value_namespace = name_space
                    self.time_zone.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.message:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.message:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "messages" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "message"):
                for c in self.message:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.Messages.Message()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.message.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "message"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LoggingStatistics(Entity):
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
            super(Syslog.LoggingStatistics, self).__init__()

            self.yang_name = "logging-statistics"
            self.yang_parent_name = "syslog"

            self.buffer_logging_stats = Syslog.LoggingStatistics.BufferLoggingStats()
            self.buffer_logging_stats.parent = self
            self._children_name_map["buffer_logging_stats"] = "buffer-logging-stats"
            self._children_yang_names.add("buffer-logging-stats")

            self.console_logging_stats = Syslog.LoggingStatistics.ConsoleLoggingStats()
            self.console_logging_stats.parent = self
            self._children_name_map["console_logging_stats"] = "console-logging-stats"
            self._children_yang_names.add("console-logging-stats")

            self.logging_stats = Syslog.LoggingStatistics.LoggingStats()
            self.logging_stats.parent = self
            self._children_name_map["logging_stats"] = "logging-stats"
            self._children_yang_names.add("logging-stats")

            self.monitor_logging_stats = Syslog.LoggingStatistics.MonitorLoggingStats()
            self.monitor_logging_stats.parent = self
            self._children_name_map["monitor_logging_stats"] = "monitor-logging-stats"
            self._children_yang_names.add("monitor-logging-stats")

            self.trap_logging_stats = Syslog.LoggingStatistics.TrapLoggingStats()
            self.trap_logging_stats.parent = self
            self._children_name_map["trap_logging_stats"] = "trap-logging-stats"
            self._children_yang_names.add("trap-logging-stats")

            self.file_logging_stat = YList(self)
            self.remote_logging_stat = YList(self)
            self.tls_remote_logging_stat = YList(self)

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
                        super(Syslog.LoggingStatistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Syslog.LoggingStatistics, self).__setattr__(name, value)


        class LoggingStats(Entity):
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
                super(Syslog.LoggingStatistics.LoggingStats, self).__init__()

                self.yang_name = "logging-stats"
                self.yang_parent_name = "logging-statistics"

                self.drop_count = YLeaf(YType.uint32, "drop-count")

                self.flush_count = YLeaf(YType.uint32, "flush-count")

                self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                self.overrun_count = YLeaf(YType.uint32, "overrun-count")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("drop_count",
                                "flush_count",
                                "is_log_enabled",
                                "overrun_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.LoggingStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.LoggingStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.drop_count.is_set or
                    self.flush_count.is_set or
                    self.is_log_enabled.is_set or
                    self.overrun_count.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.drop_count.yfilter != YFilter.not_set or
                    self.flush_count.yfilter != YFilter.not_set or
                    self.is_log_enabled.yfilter != YFilter.not_set or
                    self.overrun_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "logging-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.drop_count.is_set or self.drop_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.drop_count.get_name_leafdata())
                if (self.flush_count.is_set or self.flush_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flush_count.get_name_leafdata())
                if (self.is_log_enabled.is_set or self.is_log_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_log_enabled.get_name_leafdata())
                if (self.overrun_count.is_set or self.overrun_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.overrun_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "drop-count" or name == "flush-count" or name == "is-log-enabled" or name == "overrun-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "drop-count"):
                    self.drop_count = value
                    self.drop_count.value_namespace = name_space
                    self.drop_count.value_namespace_prefix = name_space_prefix
                if(value_path == "flush-count"):
                    self.flush_count = value
                    self.flush_count.value_namespace = name_space
                    self.flush_count.value_namespace_prefix = name_space_prefix
                if(value_path == "is-log-enabled"):
                    self.is_log_enabled = value
                    self.is_log_enabled.value_namespace = name_space
                    self.is_log_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "overrun-count"):
                    self.overrun_count = value
                    self.overrun_count.value_namespace = name_space
                    self.overrun_count.value_namespace_prefix = name_space_prefix


        class ConsoleLoggingStats(Entity):
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
            	**type**\:   :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                super(Syslog.LoggingStatistics.ConsoleLoggingStats, self).__init__()

                self.yang_name = "console-logging-stats"
                self.yang_parent_name = "logging-statistics"

                self.buffer_size = YLeaf(YType.uint32, "buffer-size")

                self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                self.message_count = YLeaf(YType.uint32, "message-count")

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
                    if name in ("buffer_size",
                                "is_log_enabled",
                                "message_count",
                                "severity") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.ConsoleLoggingStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.ConsoleLoggingStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.buffer_size.is_set or
                    self.is_log_enabled.is_set or
                    self.message_count.is_set or
                    self.severity.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.buffer_size.yfilter != YFilter.not_set or
                    self.is_log_enabled.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set or
                    self.severity.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "console-logging-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffer_size.get_name_leafdata())
                if (self.is_log_enabled.is_set or self.is_log_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_log_enabled.get_name_leafdata())
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())
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
                if(name == "buffer-size" or name == "is-log-enabled" or name == "message-count" or name == "severity"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "buffer-size"):
                    self.buffer_size = value
                    self.buffer_size.value_namespace = name_space
                    self.buffer_size.value_namespace_prefix = name_space_prefix
                if(value_path == "is-log-enabled"):
                    self.is_log_enabled = value
                    self.is_log_enabled.value_namespace = name_space
                    self.is_log_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix
                if(value_path == "severity"):
                    self.severity = value
                    self.severity.value_namespace = name_space
                    self.severity.value_namespace_prefix = name_space_prefix


        class MonitorLoggingStats(Entity):
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
            	**type**\:   :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                super(Syslog.LoggingStatistics.MonitorLoggingStats, self).__init__()

                self.yang_name = "monitor-logging-stats"
                self.yang_parent_name = "logging-statistics"

                self.buffer_size = YLeaf(YType.uint32, "buffer-size")

                self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                self.message_count = YLeaf(YType.uint32, "message-count")

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
                    if name in ("buffer_size",
                                "is_log_enabled",
                                "message_count",
                                "severity") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.MonitorLoggingStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.MonitorLoggingStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.buffer_size.is_set or
                    self.is_log_enabled.is_set or
                    self.message_count.is_set or
                    self.severity.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.buffer_size.yfilter != YFilter.not_set or
                    self.is_log_enabled.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set or
                    self.severity.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "monitor-logging-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffer_size.get_name_leafdata())
                if (self.is_log_enabled.is_set or self.is_log_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_log_enabled.get_name_leafdata())
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())
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
                if(name == "buffer-size" or name == "is-log-enabled" or name == "message-count" or name == "severity"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "buffer-size"):
                    self.buffer_size = value
                    self.buffer_size.value_namespace = name_space
                    self.buffer_size.value_namespace_prefix = name_space_prefix
                if(value_path == "is-log-enabled"):
                    self.is_log_enabled = value
                    self.is_log_enabled.value_namespace = name_space
                    self.is_log_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix
                if(value_path == "severity"):
                    self.severity = value
                    self.severity.value_namespace = name_space
                    self.severity.value_namespace_prefix = name_space_prefix


        class TrapLoggingStats(Entity):
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
            	**type**\:   :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                super(Syslog.LoggingStatistics.TrapLoggingStats, self).__init__()

                self.yang_name = "trap-logging-stats"
                self.yang_parent_name = "logging-statistics"

                self.buffer_size = YLeaf(YType.uint32, "buffer-size")

                self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                self.message_count = YLeaf(YType.uint32, "message-count")

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
                    if name in ("buffer_size",
                                "is_log_enabled",
                                "message_count",
                                "severity") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.TrapLoggingStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.TrapLoggingStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.buffer_size.is_set or
                    self.is_log_enabled.is_set or
                    self.message_count.is_set or
                    self.severity.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.buffer_size.yfilter != YFilter.not_set or
                    self.is_log_enabled.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set or
                    self.severity.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trap-logging-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffer_size.get_name_leafdata())
                if (self.is_log_enabled.is_set or self.is_log_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_log_enabled.get_name_leafdata())
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())
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
                if(name == "buffer-size" or name == "is-log-enabled" or name == "message-count" or name == "severity"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "buffer-size"):
                    self.buffer_size = value
                    self.buffer_size.value_namespace = name_space
                    self.buffer_size.value_namespace_prefix = name_space_prefix
                if(value_path == "is-log-enabled"):
                    self.is_log_enabled = value
                    self.is_log_enabled.value_namespace = name_space
                    self.is_log_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix
                if(value_path == "severity"):
                    self.severity = value
                    self.severity.value_namespace = name_space
                    self.severity.value_namespace_prefix = name_space_prefix


        class BufferLoggingStats(Entity):
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
            	**type**\:   :py:class:`SystemMessageSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverity>`
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2016-06-24'

            def __init__(self):
                super(Syslog.LoggingStatistics.BufferLoggingStats, self).__init__()

                self.yang_name = "buffer-logging-stats"
                self.yang_parent_name = "logging-statistics"

                self.buffer_size = YLeaf(YType.uint32, "buffer-size")

                self.is_log_enabled = YLeaf(YType.boolean, "is-log-enabled")

                self.message_count = YLeaf(YType.uint32, "message-count")

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
                    if name in ("buffer_size",
                                "is_log_enabled",
                                "message_count",
                                "severity") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.BufferLoggingStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.BufferLoggingStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.buffer_size.is_set or
                    self.is_log_enabled.is_set or
                    self.message_count.is_set or
                    self.severity.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.buffer_size.yfilter != YFilter.not_set or
                    self.is_log_enabled.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set or
                    self.severity.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "buffer-logging-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.buffer_size.is_set or self.buffer_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffer_size.get_name_leafdata())
                if (self.is_log_enabled.is_set or self.is_log_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_log_enabled.get_name_leafdata())
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())
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
                if(name == "buffer-size" or name == "is-log-enabled" or name == "message-count" or name == "severity"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "buffer-size"):
                    self.buffer_size = value
                    self.buffer_size.value_namespace = name_space
                    self.buffer_size.value_namespace_prefix = name_space_prefix
                if(value_path == "is-log-enabled"):
                    self.is_log_enabled = value
                    self.is_log_enabled.value_namespace = name_space
                    self.is_log_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix
                if(value_path == "severity"):
                    self.severity = value
                    self.severity.value_namespace = name_space
                    self.severity.value_namespace_prefix = name_space_prefix


        class RemoteLoggingStat(Entity):
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
                super(Syslog.LoggingStatistics.RemoteLoggingStat, self).__init__()

                self.yang_name = "remote-logging-stat"
                self.yang_parent_name = "logging-statistics"

                self.message_count = YLeaf(YType.uint32, "message-count")

                self.remote_host_name = YLeaf(YType.str, "remote-host-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("message_count",
                                "remote_host_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.RemoteLoggingStat, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.RemoteLoggingStat, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.message_count.is_set or
                    self.remote_host_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set or
                    self.remote_host_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "remote-logging-stat" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())
                if (self.remote_host_name.is_set or self.remote_host_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_host_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "message-count" or name == "remote-host-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-host-name"):
                    self.remote_host_name = value
                    self.remote_host_name.value_namespace = name_space
                    self.remote_host_name.value_namespace_prefix = name_space_prefix


        class TlsRemoteLoggingStat(Entity):
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
                super(Syslog.LoggingStatistics.TlsRemoteLoggingStat, self).__init__()

                self.yang_name = "tls-remote-logging-stat"
                self.yang_parent_name = "logging-statistics"

                self.message_count = YLeaf(YType.uint32, "message-count")

                self.remote_host_name = YLeaf(YType.str, "remote-host-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("message_count",
                                "remote_host_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.TlsRemoteLoggingStat, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.TlsRemoteLoggingStat, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.message_count.is_set or
                    self.remote_host_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set or
                    self.remote_host_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tls-remote-logging-stat" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())
                if (self.remote_host_name.is_set or self.remote_host_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_host_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "message-count" or name == "remote-host-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-host-name"):
                    self.remote_host_name = value
                    self.remote_host_name.value_namespace = name_space
                    self.remote_host_name.value_namespace_prefix = name_space_prefix


        class FileLoggingStat(Entity):
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
                super(Syslog.LoggingStatistics.FileLoggingStat, self).__init__()

                self.yang_name = "file-logging-stat"
                self.yang_parent_name = "logging-statistics"

                self.file_name = YLeaf(YType.str, "file-name")

                self.message_count = YLeaf(YType.uint32, "message-count")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("file_name",
                                "message_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Syslog.LoggingStatistics.FileLoggingStat, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Syslog.LoggingStatistics.FileLoggingStat, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.file_name.is_set or
                    self.message_count.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.file_name.yfilter != YFilter.not_set or
                    self.message_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "file-logging-stat" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/logging-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.file_name.is_set or self.file_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.file_name.get_name_leafdata())
                if (self.message_count.is_set or self.message_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "file-name" or name == "message-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "file-name"):
                    self.file_name = value
                    self.file_name.value_namespace = name_space
                    self.file_name.value_namespace_prefix = name_space_prefix
                if(value_path == "message-count"):
                    self.message_count = value
                    self.message_count.value_namespace = name_space
                    self.message_count.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.file_logging_stat:
                if (c.has_data()):
                    return True
            for c in self.remote_logging_stat:
                if (c.has_data()):
                    return True
            for c in self.tls_remote_logging_stat:
                if (c.has_data()):
                    return True
            return (
                (self.buffer_logging_stats is not None and self.buffer_logging_stats.has_data()) or
                (self.console_logging_stats is not None and self.console_logging_stats.has_data()) or
                (self.logging_stats is not None and self.logging_stats.has_data()) or
                (self.monitor_logging_stats is not None and self.monitor_logging_stats.has_data()) or
                (self.trap_logging_stats is not None and self.trap_logging_stats.has_data()))

        def has_operation(self):
            for c in self.file_logging_stat:
                if (c.has_operation()):
                    return True
            for c in self.remote_logging_stat:
                if (c.has_operation()):
                    return True
            for c in self.tls_remote_logging_stat:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                (self.buffer_logging_stats is not None and self.buffer_logging_stats.has_operation()) or
                (self.console_logging_stats is not None and self.console_logging_stats.has_operation()) or
                (self.logging_stats is not None and self.logging_stats.has_operation()) or
                (self.monitor_logging_stats is not None and self.monitor_logging_stats.has_operation()) or
                (self.trap_logging_stats is not None and self.trap_logging_stats.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logging-statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "buffer-logging-stats"):
                if (self.buffer_logging_stats is None):
                    self.buffer_logging_stats = Syslog.LoggingStatistics.BufferLoggingStats()
                    self.buffer_logging_stats.parent = self
                    self._children_name_map["buffer_logging_stats"] = "buffer-logging-stats"
                return self.buffer_logging_stats

            if (child_yang_name == "console-logging-stats"):
                if (self.console_logging_stats is None):
                    self.console_logging_stats = Syslog.LoggingStatistics.ConsoleLoggingStats()
                    self.console_logging_stats.parent = self
                    self._children_name_map["console_logging_stats"] = "console-logging-stats"
                return self.console_logging_stats

            if (child_yang_name == "file-logging-stat"):
                for c in self.file_logging_stat:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.LoggingStatistics.FileLoggingStat()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.file_logging_stat.append(c)
                return c

            if (child_yang_name == "logging-stats"):
                if (self.logging_stats is None):
                    self.logging_stats = Syslog.LoggingStatistics.LoggingStats()
                    self.logging_stats.parent = self
                    self._children_name_map["logging_stats"] = "logging-stats"
                return self.logging_stats

            if (child_yang_name == "monitor-logging-stats"):
                if (self.monitor_logging_stats is None):
                    self.monitor_logging_stats = Syslog.LoggingStatistics.MonitorLoggingStats()
                    self.monitor_logging_stats.parent = self
                    self._children_name_map["monitor_logging_stats"] = "monitor-logging-stats"
                return self.monitor_logging_stats

            if (child_yang_name == "remote-logging-stat"):
                for c in self.remote_logging_stat:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.LoggingStatistics.RemoteLoggingStat()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.remote_logging_stat.append(c)
                return c

            if (child_yang_name == "tls-remote-logging-stat"):
                for c in self.tls_remote_logging_stat:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Syslog.LoggingStatistics.TlsRemoteLoggingStat()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tls_remote_logging_stat.append(c)
                return c

            if (child_yang_name == "trap-logging-stats"):
                if (self.trap_logging_stats is None):
                    self.trap_logging_stats = Syslog.LoggingStatistics.TrapLoggingStats()
                    self.trap_logging_stats.parent = self
                    self._children_name_map["trap_logging_stats"] = "trap-logging-stats"
                return self.trap_logging_stats

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "buffer-logging-stats" or name == "console-logging-stats" or name == "file-logging-stat" or name == "logging-stats" or name == "monitor-logging-stats" or name == "remote-logging-stat" or name == "tls-remote-logging-stat" or name == "trap-logging-stats"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.an_remote_servers is not None and self.an_remote_servers.has_data()) or
            (self.logging_files is not None and self.logging_files.has_data()) or
            (self.logging_statistics is not None and self.logging_statistics.has_data()) or
            (self.messages is not None and self.messages.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.an_remote_servers is not None and self.an_remote_servers.has_operation()) or
            (self.logging_files is not None and self.logging_files.has_operation()) or
            (self.logging_statistics is not None and self.logging_statistics.has_operation()) or
            (self.messages is not None and self.messages.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-syslog-oper:syslog" + path_buffer

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

        if (child_yang_name == "an-remote-servers"):
            if (self.an_remote_servers is None):
                self.an_remote_servers = Syslog.AnRemoteServers()
                self.an_remote_servers.parent = self
                self._children_name_map["an_remote_servers"] = "an-remote-servers"
            return self.an_remote_servers

        if (child_yang_name == "logging-files"):
            if (self.logging_files is None):
                self.logging_files = Syslog.LoggingFiles()
                self.logging_files.parent = self
                self._children_name_map["logging_files"] = "logging-files"
            return self.logging_files

        if (child_yang_name == "logging-statistics"):
            if (self.logging_statistics is None):
                self.logging_statistics = Syslog.LoggingStatistics()
                self.logging_statistics.parent = self
                self._children_name_map["logging_statistics"] = "logging-statistics"
            return self.logging_statistics

        if (child_yang_name == "messages"):
            if (self.messages is None):
                self.messages = Syslog.Messages()
                self.messages.parent = self
                self._children_name_map["messages"] = "messages"
            return self.messages

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "an-remote-servers" or name == "logging-files" or name == "logging-statistics" or name == "messages"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Syslog()
        return self._top_entity

