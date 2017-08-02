""" NOTIFICATION_LOG_MIB 

The MIB module for logging SNMP Notifications, that is, Traps
and Informs.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NotificationLogMib(Entity):
    """
    
    
    .. attribute:: nlmconfig
    
    	
    	**type**\:   :py:class:`Nlmconfig <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfig>`
    
    .. attribute:: nlmconfiglogtable
    
    	A table of logging control entries
    	**type**\:   :py:class:`Nlmconfiglogtable <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable>`
    
    .. attribute:: nlmlogtable
    
    	A table of Notification log entries.  It is an implementation\-specific matter whether entries in this table are preserved across initializations of the management system.  In general one would expect that they are not.  Note that keeping entries across initializations of the management system leads to some confusion with counters and TimeStamps, since both of those are based on sysUpTime, which resets on management initialization.  In this situation, counters apply only after the reset and nlmLogTime for entries made before the reset MUST be set to 0
    	**type**\:   :py:class:`Nlmlogtable <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogtable>`
    
    .. attribute:: nlmlogvariabletable
    
    	A table of variables to go with Notification log entries
    	**type**\:   :py:class:`Nlmlogvariabletable <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogvariabletable>`
    
    .. attribute:: nlmstats
    
    	
    	**type**\:   :py:class:`Nlmstats <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmstats>`
    
    

    """

    _prefix = 'NOTIFICATION-LOG-MIB'
    _revision = '2000-11-27'

    def __init__(self):
        super(NotificationLogMib, self).__init__()
        self._top_entity = None

        self.yang_name = "NOTIFICATION-LOG-MIB"
        self.yang_parent_name = "NOTIFICATION-LOG-MIB"

        self.nlmconfig = NotificationLogMib.Nlmconfig()
        self.nlmconfig.parent = self
        self._children_name_map["nlmconfig"] = "nlmConfig"
        self._children_yang_names.add("nlmConfig")

        self.nlmconfiglogtable = NotificationLogMib.Nlmconfiglogtable()
        self.nlmconfiglogtable.parent = self
        self._children_name_map["nlmconfiglogtable"] = "nlmConfigLogTable"
        self._children_yang_names.add("nlmConfigLogTable")

        self.nlmlogtable = NotificationLogMib.Nlmlogtable()
        self.nlmlogtable.parent = self
        self._children_name_map["nlmlogtable"] = "nlmLogTable"
        self._children_yang_names.add("nlmLogTable")

        self.nlmlogvariabletable = NotificationLogMib.Nlmlogvariabletable()
        self.nlmlogvariabletable.parent = self
        self._children_name_map["nlmlogvariabletable"] = "nlmLogVariableTable"
        self._children_yang_names.add("nlmLogVariableTable")

        self.nlmstats = NotificationLogMib.Nlmstats()
        self.nlmstats.parent = self
        self._children_name_map["nlmstats"] = "nlmStats"
        self._children_yang_names.add("nlmStats")


    class Nlmconfig(Entity):
        """
        
        
        .. attribute:: nlmconfigglobalageout
        
        	The number of minutes a Notification SHOULD be kept in a log before it is automatically removed.  If an application changes the value of nlmConfigGlobalAgeOut, Notifications older than the new time MAY be discarded to meet the new time.  A value of 0 means no age out.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: minutes
        
        .. attribute:: nlmconfigglobalentrylimit
        
        	The maximum number of notification entries that may be held in nlmLogTable for all nlmLogNames added together.  A particular setting does not guarantee that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications MUST be discarded to bring the log down to the new limit \- thus the value of nlmConfigGlobalEntryLimit MUST take precedence over the values of nlmConfigGlobalAgeOut and nlmConfigLogEntryLimit, even if the Notification being discarded has been present for fewer minutes than the value of nlmConfigGlobalAgeOut, or if the named log has fewer entries than that specified in nlmConfigLogEntryLimit.  A value of 0 means no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NotificationLogMib.Nlmconfig, self).__init__()

            self.yang_name = "nlmConfig"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"

            self.nlmconfigglobalageout = YLeaf(YType.uint32, "nlmConfigGlobalAgeOut")

            self.nlmconfigglobalentrylimit = YLeaf(YType.uint32, "nlmConfigGlobalEntryLimit")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("nlmconfigglobalageout",
                            "nlmconfigglobalentrylimit") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NotificationLogMib.Nlmconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NotificationLogMib.Nlmconfig, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.nlmconfigglobalageout.is_set or
                self.nlmconfigglobalentrylimit.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.nlmconfigglobalageout.yfilter != YFilter.not_set or
                self.nlmconfigglobalentrylimit.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nlmConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.nlmconfigglobalageout.is_set or self.nlmconfigglobalageout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nlmconfigglobalageout.get_name_leafdata())
            if (self.nlmconfigglobalentrylimit.is_set or self.nlmconfigglobalentrylimit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nlmconfigglobalentrylimit.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nlmConfigGlobalAgeOut" or name == "nlmConfigGlobalEntryLimit"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "nlmConfigGlobalAgeOut"):
                self.nlmconfigglobalageout = value
                self.nlmconfigglobalageout.value_namespace = name_space
                self.nlmconfigglobalageout.value_namespace_prefix = name_space_prefix
            if(value_path == "nlmConfigGlobalEntryLimit"):
                self.nlmconfigglobalentrylimit = value
                self.nlmconfigglobalentrylimit.value_namespace = name_space
                self.nlmconfigglobalentrylimit.value_namespace_prefix = name_space_prefix


    class Nlmstats(Entity):
        """
        
        
        .. attribute:: nlmstatsglobalnotificationsbumped
        
        	The number of log entries discarded to make room for a new entry due to lack of resources or the value of nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not include entries discarded due to the value of nlmConfigGlobalAgeOut
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: notifications
        
        .. attribute:: nlmstatsglobalnotificationslogged
        
        	The number of Notifications put into the nlmLogTable.  This counts a Notification once for each log entry, so a Notification  put into multiple logs is counted multiple times
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: notifications
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NotificationLogMib.Nlmstats, self).__init__()

            self.yang_name = "nlmStats"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"

            self.nlmstatsglobalnotificationsbumped = YLeaf(YType.uint32, "nlmStatsGlobalNotificationsBumped")

            self.nlmstatsglobalnotificationslogged = YLeaf(YType.uint32, "nlmStatsGlobalNotificationsLogged")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("nlmstatsglobalnotificationsbumped",
                            "nlmstatsglobalnotificationslogged") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NotificationLogMib.Nlmstats, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NotificationLogMib.Nlmstats, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.nlmstatsglobalnotificationsbumped.is_set or
                self.nlmstatsglobalnotificationslogged.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.nlmstatsglobalnotificationsbumped.yfilter != YFilter.not_set or
                self.nlmstatsglobalnotificationslogged.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nlmStats" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.nlmstatsglobalnotificationsbumped.is_set or self.nlmstatsglobalnotificationsbumped.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nlmstatsglobalnotificationsbumped.get_name_leafdata())
            if (self.nlmstatsglobalnotificationslogged.is_set or self.nlmstatsglobalnotificationslogged.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nlmstatsglobalnotificationslogged.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nlmStatsGlobalNotificationsBumped" or name == "nlmStatsGlobalNotificationsLogged"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "nlmStatsGlobalNotificationsBumped"):
                self.nlmstatsglobalnotificationsbumped = value
                self.nlmstatsglobalnotificationsbumped.value_namespace = name_space
                self.nlmstatsglobalnotificationsbumped.value_namespace_prefix = name_space_prefix
            if(value_path == "nlmStatsGlobalNotificationsLogged"):
                self.nlmstatsglobalnotificationslogged = value
                self.nlmstatsglobalnotificationslogged.value_namespace = name_space
                self.nlmstatsglobalnotificationslogged.value_namespace_prefix = name_space_prefix


    class Nlmconfiglogtable(Entity):
        """
        A table of logging control entries.
        
        .. attribute:: nlmconfiglogentry
        
        	A logging control entry.  Depending on the entry's storage type entries may be supplied by the system or created and deleted by applications using nlmConfigLogEntryStatus
        	**type**\: list of    :py:class:`Nlmconfiglogentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NotificationLogMib.Nlmconfiglogtable, self).__init__()

            self.yang_name = "nlmConfigLogTable"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"

            self.nlmconfiglogentry = YList(self)

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
                        super(NotificationLogMib.Nlmconfiglogtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NotificationLogMib.Nlmconfiglogtable, self).__setattr__(name, value)


        class Nlmconfiglogentry(Entity):
            """
            A logging control entry.  Depending on the entry's storage type
            entries may be supplied by the system or created and deleted by
            applications using nlmConfigLogEntryStatus.
            
            .. attribute:: nlmlogname  <key>
            
            	The name of the log.  An implementation may allow multiple named logs, up to some implementation\-specific limit (which may be none).  A zero\-length log name is reserved for creation and deletion by the managed system, and MUST be used as the default log name by systems that do not support named logs
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: nlmconfiglogadminstatus
            
            	Control to enable or disable the log without otherwise disturbing the log's entry.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\:   :py:class:`Nlmconfiglogadminstatus <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.Nlmconfiglogadminstatus>`
            
            .. attribute:: nlmconfiglogentrylimit
            
            	The maximum number of notification entries that can be held in nlmLogTable for this named log.  A particular setting does not guarantee that that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications are discarded to bring the log down to the new limit.  A value of 0 indicates no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmconfiglogentrystatus
            
            	Control for creating and deleting entries.  Entries may be modified while active.  For non\-null\-named logs, the managed system records the security credentials from the request that sets nlmConfigLogStatus to 'active' and uses that identity to apply access control to the objects in the Notification to decide if that Notification may be logged
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: nlmconfiglogfiltername
            
            	A value of snmpNotifyFilterProfileName as used as an index into the snmpNotifyFilterTable in the SNMP Notification MIB, specifying the locally or remotely originated Notifications to be filtered out and not logged in this log.  A zero\-length value or a name that does not identify an existing entry in snmpNotifyFilterTable indicate no Notifications are to be logged in this log
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: nlmconfiglogoperstatus
            
            	The operational status of this log\:  disabled  administratively disabled  operational    administratively enabled and working  noFilter  administratively enabled but either           nlmConfigLogFilterName is zero length           or does not name an existing entry in           snmpNotifyFilterTable
            	**type**\:   :py:class:`Nlmconfiglogoperstatus <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.Nlmconfiglogoperstatus>`
            
            .. attribute:: nlmconfiglogstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: nlmstatslognotificationsbumped
            
            	The number of log entries discarded from this named log to make room for a new entry due to lack of resources or the value of nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not include entries discarded due to the value of nlmConfigGlobalAgeOut
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: notifications
            
            .. attribute:: nlmstatslognotificationslogged
            
            	The number of Notifications put in this named log
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: notifications
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                super(NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry, self).__init__()

                self.yang_name = "nlmConfigLogEntry"
                self.yang_parent_name = "nlmConfigLogTable"

                self.nlmlogname = YLeaf(YType.str, "nlmLogName")

                self.nlmconfiglogadminstatus = YLeaf(YType.enumeration, "nlmConfigLogAdminStatus")

                self.nlmconfiglogentrylimit = YLeaf(YType.uint32, "nlmConfigLogEntryLimit")

                self.nlmconfiglogentrystatus = YLeaf(YType.enumeration, "nlmConfigLogEntryStatus")

                self.nlmconfiglogfiltername = YLeaf(YType.str, "nlmConfigLogFilterName")

                self.nlmconfiglogoperstatus = YLeaf(YType.enumeration, "nlmConfigLogOperStatus")

                self.nlmconfiglogstoragetype = YLeaf(YType.enumeration, "nlmConfigLogStorageType")

                self.nlmstatslognotificationsbumped = YLeaf(YType.uint32, "nlmStatsLogNotificationsBumped")

                self.nlmstatslognotificationslogged = YLeaf(YType.uint32, "nlmStatsLogNotificationsLogged")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nlmlogname",
                                "nlmconfiglogadminstatus",
                                "nlmconfiglogentrylimit",
                                "nlmconfiglogentrystatus",
                                "nlmconfiglogfiltername",
                                "nlmconfiglogoperstatus",
                                "nlmconfiglogstoragetype",
                                "nlmstatslognotificationsbumped",
                                "nlmstatslognotificationslogged") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry, self).__setattr__(name, value)

            class Nlmconfiglogadminstatus(Enum):
                """
                Nlmconfiglogadminstatus

                Control to enable or disable the log without otherwise

                disturbing the log's entry.

                Please be aware that contention between multiple managers

                trying to set this object to different values MAY affect the

                reliability and completeness of data seen by each manager.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Nlmconfiglogoperstatus(Enum):
                """
                Nlmconfiglogoperstatus

                The operational status of this log\:

                disabled  administratively disabled

                operational    administratively enabled and working

                noFilter  administratively enabled but either

                          nlmConfigLogFilterName is zero length

                          or does not name an existing entry in

                          snmpNotifyFilterTable

                .. data:: disabled = 1

                .. data:: operational = 2

                .. data:: noFilter = 3

                """

                disabled = Enum.YLeaf(1, "disabled")

                operational = Enum.YLeaf(2, "operational")

                noFilter = Enum.YLeaf(3, "noFilter")


            def has_data(self):
                return (
                    self.nlmlogname.is_set or
                    self.nlmconfiglogadminstatus.is_set or
                    self.nlmconfiglogentrylimit.is_set or
                    self.nlmconfiglogentrystatus.is_set or
                    self.nlmconfiglogfiltername.is_set or
                    self.nlmconfiglogoperstatus.is_set or
                    self.nlmconfiglogstoragetype.is_set or
                    self.nlmstatslognotificationsbumped.is_set or
                    self.nlmstatslognotificationslogged.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nlmlogname.yfilter != YFilter.not_set or
                    self.nlmconfiglogadminstatus.yfilter != YFilter.not_set or
                    self.nlmconfiglogentrylimit.yfilter != YFilter.not_set or
                    self.nlmconfiglogentrystatus.yfilter != YFilter.not_set or
                    self.nlmconfiglogfiltername.yfilter != YFilter.not_set or
                    self.nlmconfiglogoperstatus.yfilter != YFilter.not_set or
                    self.nlmconfiglogstoragetype.yfilter != YFilter.not_set or
                    self.nlmstatslognotificationsbumped.yfilter != YFilter.not_set or
                    self.nlmstatslognotificationslogged.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nlmConfigLogEntry" + "[nlmLogName='" + self.nlmlogname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/nlmConfigLogTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nlmlogname.is_set or self.nlmlogname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogname.get_name_leafdata())
                if (self.nlmconfiglogadminstatus.is_set or self.nlmconfiglogadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmconfiglogadminstatus.get_name_leafdata())
                if (self.nlmconfiglogentrylimit.is_set or self.nlmconfiglogentrylimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmconfiglogentrylimit.get_name_leafdata())
                if (self.nlmconfiglogentrystatus.is_set or self.nlmconfiglogentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmconfiglogentrystatus.get_name_leafdata())
                if (self.nlmconfiglogfiltername.is_set or self.nlmconfiglogfiltername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmconfiglogfiltername.get_name_leafdata())
                if (self.nlmconfiglogoperstatus.is_set or self.nlmconfiglogoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmconfiglogoperstatus.get_name_leafdata())
                if (self.nlmconfiglogstoragetype.is_set or self.nlmconfiglogstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmconfiglogstoragetype.get_name_leafdata())
                if (self.nlmstatslognotificationsbumped.is_set or self.nlmstatslognotificationsbumped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmstatslognotificationsbumped.get_name_leafdata())
                if (self.nlmstatslognotificationslogged.is_set or self.nlmstatslognotificationslogged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmstatslognotificationslogged.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nlmLogName" or name == "nlmConfigLogAdminStatus" or name == "nlmConfigLogEntryLimit" or name == "nlmConfigLogEntryStatus" or name == "nlmConfigLogFilterName" or name == "nlmConfigLogOperStatus" or name == "nlmConfigLogStorageType" or name == "nlmStatsLogNotificationsBumped" or name == "nlmStatsLogNotificationsLogged"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nlmLogName"):
                    self.nlmlogname = value
                    self.nlmlogname.value_namespace = name_space
                    self.nlmlogname.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmConfigLogAdminStatus"):
                    self.nlmconfiglogadminstatus = value
                    self.nlmconfiglogadminstatus.value_namespace = name_space
                    self.nlmconfiglogadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmConfigLogEntryLimit"):
                    self.nlmconfiglogentrylimit = value
                    self.nlmconfiglogentrylimit.value_namespace = name_space
                    self.nlmconfiglogentrylimit.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmConfigLogEntryStatus"):
                    self.nlmconfiglogentrystatus = value
                    self.nlmconfiglogentrystatus.value_namespace = name_space
                    self.nlmconfiglogentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmConfigLogFilterName"):
                    self.nlmconfiglogfiltername = value
                    self.nlmconfiglogfiltername.value_namespace = name_space
                    self.nlmconfiglogfiltername.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmConfigLogOperStatus"):
                    self.nlmconfiglogoperstatus = value
                    self.nlmconfiglogoperstatus.value_namespace = name_space
                    self.nlmconfiglogoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmConfigLogStorageType"):
                    self.nlmconfiglogstoragetype = value
                    self.nlmconfiglogstoragetype.value_namespace = name_space
                    self.nlmconfiglogstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmStatsLogNotificationsBumped"):
                    self.nlmstatslognotificationsbumped = value
                    self.nlmstatslognotificationsbumped.value_namespace = name_space
                    self.nlmstatslognotificationsbumped.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmStatsLogNotificationsLogged"):
                    self.nlmstatslognotificationslogged = value
                    self.nlmstatslognotificationslogged.value_namespace = name_space
                    self.nlmstatslognotificationslogged.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nlmconfiglogentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nlmconfiglogentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nlmConfigLogTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nlmConfigLogEntry"):
                for c in self.nlmconfiglogentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nlmconfiglogentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nlmConfigLogEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nlmlogtable(Entity):
        """
        A table of Notification log entries.
        
        It is an implementation\-specific matter whether entries in this
        table are preserved across initializations of the management
        system.  In general one would expect that they are not.
        
        Note that keeping entries across initializations of the
        management system leads to some confusion with counters and
        TimeStamps, since both of those are based on sysUpTime, which
        resets on management initialization.  In this situation,
        counters apply only after the reset and nlmLogTime for entries
        made before the reset MUST be set to 0.
        
        .. attribute:: nlmlogentry
        
        	A Notification log entry.  Entries appear in this table when Notifications occur and pass filtering by nlmConfigLogFilterName and access control.  They are removed to make way for new entries due to lack of resources or the values of nlmConfigGlobalEntryLimit, nlmConfigGlobalAgeOut, or nlmConfigLogEntryLimit.  If adding an entry would exceed nlmConfigGlobalEntryLimit or system resources in general, the oldest entry in any log SHOULD be removed to make room for the new one.  If adding an entry would exceed nlmConfigLogEntryLimit the oldest entry in that log SHOULD be removed to make room for the new one.  Before the managed system puts a locally\-generated Notification into a non\-null\-named log it assures that the creator of the log has access to the information in the Notification.  If not it does not log that Notification in that log
        	**type**\: list of    :py:class:`Nlmlogentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogtable.Nlmlogentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NotificationLogMib.Nlmlogtable, self).__init__()

            self.yang_name = "nlmLogTable"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"

            self.nlmlogentry = YList(self)

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
                        super(NotificationLogMib.Nlmlogtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NotificationLogMib.Nlmlogtable, self).__setattr__(name, value)


        class Nlmlogentry(Entity):
            """
            A Notification log entry.
            
            Entries appear in this table when Notifications occur and pass
            filtering by nlmConfigLogFilterName and access control.  They are
            removed to make way for new entries due to lack of resources or
            the values of nlmConfigGlobalEntryLimit, nlmConfigGlobalAgeOut, or
            nlmConfigLogEntryLimit.
            
            If adding an entry would exceed nlmConfigGlobalEntryLimit or system
            resources in general, the oldest entry in any log SHOULD be removed
            to make room for the new one.
            
            If adding an entry would exceed nlmConfigLogEntryLimit the oldest
            entry in that log SHOULD be removed to make room for the new one.
            
            Before the managed system puts a locally\-generated Notification
            into a non\-null\-named log it assures that the creator of the log
            has access to the information in the Notification.  If not it
            does not log that Notification in that log.
            
            .. attribute:: nlmlogname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`nlmlogname <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry>`
            
            .. attribute:: nlmlogindex  <key>
            
            	A monotonically increasing integer for the sole purpose of indexing entries within the named log.  When it reaches the maximum value, an extremely unlikely event, the agent wraps the value back to 1
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogcontextengineid
            
            	If the Notification was received in a protocol which has a contextEngineID element like SNMPv3, this object has that value. Otherwise its value is a zero\-length string
            	**type**\:  str
            
            	**length:** 5..32
            
            .. attribute:: nlmlogcontextname
            
            	The name of the SNMP MIB context from which the Notification came. For SNMPv1 Traps this is the community string from the Trap
            	**type**\:  str
            
            .. attribute:: nlmlogdateandtime
            
            	The local date and time when the entry was logged, instantiated only by systems that have date and time capability
            	**type**\:  str
            
            .. attribute:: nlmlogengineid
            
            	The identification of the SNMP engine at which the Notification originated.  If the log can contain Notifications from only one engine or the Trap is in SNMPv1 format, this object is a zero\-length string
            	**type**\:  str
            
            	**length:** 5..32
            
            .. attribute:: nlmlogenginetaddress
            
            	The transport service address of the SNMP engine from which the Notification was received, formatted according to the corresponding value of nlmLogEngineTDomain. This is used to identify the source of an SNMPv1 trap, since an nlmLogEngineId cannot be extracted from the SNMPv1 trap pdu.  This object MUST always be instantiated, even if the log can contain Notifications from only one engine.  Please be aware that the nlmLogEngineTAddress may not uniquely identify the SNMP engine from which the Notification was received. For example, if an SNMP engine uses DHCP or NAT to obtain ip addresses, the address it uses may be shared with other network devices, and hence will not uniquely identify the SNMP engine
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: nlmlogenginetdomain
            
            	Indicates the kind of transport service by which a Notification was received from an SNMP engine. nlmLogEngineTAddress contains the transport service address of the SNMP engine from which this Notification was received.  Possible values for this object are presently found in the Transport Mappings for SNMPv2 document (RFC 1906 [8])
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlognotificationid
            
            	The NOTIFICATION\-TYPE object identifier of the Notification that occurred
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogtime
            
            	The value of sysUpTime when the entry was placed in the log. If the entry occurred before the most recent management system initialization this object value MUST be set to zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                super(NotificationLogMib.Nlmlogtable.Nlmlogentry, self).__init__()

                self.yang_name = "nlmLogEntry"
                self.yang_parent_name = "nlmLogTable"

                self.nlmlogname = YLeaf(YType.str, "nlmLogName")

                self.nlmlogindex = YLeaf(YType.uint32, "nlmLogIndex")

                self.nlmlogcontextengineid = YLeaf(YType.str, "nlmLogContextEngineID")

                self.nlmlogcontextname = YLeaf(YType.str, "nlmLogContextName")

                self.nlmlogdateandtime = YLeaf(YType.str, "nlmLogDateAndTime")

                self.nlmlogengineid = YLeaf(YType.str, "nlmLogEngineID")

                self.nlmlogenginetaddress = YLeaf(YType.str, "nlmLogEngineTAddress")

                self.nlmlogenginetdomain = YLeaf(YType.str, "nlmLogEngineTDomain")

                self.nlmlognotificationid = YLeaf(YType.str, "nlmLogNotificationID")

                self.nlmlogtime = YLeaf(YType.uint32, "nlmLogTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nlmlogname",
                                "nlmlogindex",
                                "nlmlogcontextengineid",
                                "nlmlogcontextname",
                                "nlmlogdateandtime",
                                "nlmlogengineid",
                                "nlmlogenginetaddress",
                                "nlmlogenginetdomain",
                                "nlmlognotificationid",
                                "nlmlogtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NotificationLogMib.Nlmlogtable.Nlmlogentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NotificationLogMib.Nlmlogtable.Nlmlogentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nlmlogname.is_set or
                    self.nlmlogindex.is_set or
                    self.nlmlogcontextengineid.is_set or
                    self.nlmlogcontextname.is_set or
                    self.nlmlogdateandtime.is_set or
                    self.nlmlogengineid.is_set or
                    self.nlmlogenginetaddress.is_set or
                    self.nlmlogenginetdomain.is_set or
                    self.nlmlognotificationid.is_set or
                    self.nlmlogtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nlmlogname.yfilter != YFilter.not_set or
                    self.nlmlogindex.yfilter != YFilter.not_set or
                    self.nlmlogcontextengineid.yfilter != YFilter.not_set or
                    self.nlmlogcontextname.yfilter != YFilter.not_set or
                    self.nlmlogdateandtime.yfilter != YFilter.not_set or
                    self.nlmlogengineid.yfilter != YFilter.not_set or
                    self.nlmlogenginetaddress.yfilter != YFilter.not_set or
                    self.nlmlogenginetdomain.yfilter != YFilter.not_set or
                    self.nlmlognotificationid.yfilter != YFilter.not_set or
                    self.nlmlogtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nlmLogEntry" + "[nlmLogName='" + self.nlmlogname.get() + "']" + "[nlmLogIndex='" + self.nlmlogindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/nlmLogTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nlmlogname.is_set or self.nlmlogname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogname.get_name_leafdata())
                if (self.nlmlogindex.is_set or self.nlmlogindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogindex.get_name_leafdata())
                if (self.nlmlogcontextengineid.is_set or self.nlmlogcontextengineid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogcontextengineid.get_name_leafdata())
                if (self.nlmlogcontextname.is_set or self.nlmlogcontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogcontextname.get_name_leafdata())
                if (self.nlmlogdateandtime.is_set or self.nlmlogdateandtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogdateandtime.get_name_leafdata())
                if (self.nlmlogengineid.is_set or self.nlmlogengineid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogengineid.get_name_leafdata())
                if (self.nlmlogenginetaddress.is_set or self.nlmlogenginetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogenginetaddress.get_name_leafdata())
                if (self.nlmlogenginetdomain.is_set or self.nlmlogenginetdomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogenginetdomain.get_name_leafdata())
                if (self.nlmlognotificationid.is_set or self.nlmlognotificationid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlognotificationid.get_name_leafdata())
                if (self.nlmlogtime.is_set or self.nlmlogtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nlmLogName" or name == "nlmLogIndex" or name == "nlmLogContextEngineID" or name == "nlmLogContextName" or name == "nlmLogDateAndTime" or name == "nlmLogEngineID" or name == "nlmLogEngineTAddress" or name == "nlmLogEngineTDomain" or name == "nlmLogNotificationID" or name == "nlmLogTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nlmLogName"):
                    self.nlmlogname = value
                    self.nlmlogname.value_namespace = name_space
                    self.nlmlogname.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogIndex"):
                    self.nlmlogindex = value
                    self.nlmlogindex.value_namespace = name_space
                    self.nlmlogindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogContextEngineID"):
                    self.nlmlogcontextengineid = value
                    self.nlmlogcontextengineid.value_namespace = name_space
                    self.nlmlogcontextengineid.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogContextName"):
                    self.nlmlogcontextname = value
                    self.nlmlogcontextname.value_namespace = name_space
                    self.nlmlogcontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogDateAndTime"):
                    self.nlmlogdateandtime = value
                    self.nlmlogdateandtime.value_namespace = name_space
                    self.nlmlogdateandtime.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogEngineID"):
                    self.nlmlogengineid = value
                    self.nlmlogengineid.value_namespace = name_space
                    self.nlmlogengineid.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogEngineTAddress"):
                    self.nlmlogenginetaddress = value
                    self.nlmlogenginetaddress.value_namespace = name_space
                    self.nlmlogenginetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogEngineTDomain"):
                    self.nlmlogenginetdomain = value
                    self.nlmlogenginetdomain.value_namespace = name_space
                    self.nlmlogenginetdomain.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogNotificationID"):
                    self.nlmlognotificationid = value
                    self.nlmlognotificationid.value_namespace = name_space
                    self.nlmlognotificationid.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogTime"):
                    self.nlmlogtime = value
                    self.nlmlogtime.value_namespace = name_space
                    self.nlmlogtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nlmlogentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nlmlogentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nlmLogTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nlmLogEntry"):
                for c in self.nlmlogentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NotificationLogMib.Nlmlogtable.Nlmlogentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nlmlogentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nlmLogEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nlmlogvariabletable(Entity):
        """
        A table of variables to go with Notification log entries.
        
        .. attribute:: nlmlogvariableentry
        
        	A Notification log entry variable.  Entries appear in this table when there are variables in the varbind list of a Notification in nlmLogTable
        	**type**\: list of    :py:class:`Nlmlogvariableentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NotificationLogMib.Nlmlogvariabletable, self).__init__()

            self.yang_name = "nlmLogVariableTable"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"

            self.nlmlogvariableentry = YList(self)

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
                        super(NotificationLogMib.Nlmlogvariabletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NotificationLogMib.Nlmlogvariabletable, self).__setattr__(name, value)


        class Nlmlogvariableentry(Entity):
            """
            A Notification log entry variable.
            
            Entries appear in this table when there are variables in
            the varbind list of a Notification in nlmLogTable.
            
            .. attribute:: nlmlogname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`nlmlogname <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry>`
            
            .. attribute:: nlmlogindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nlmlogindex <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogtable.Nlmlogentry>`
            
            .. attribute:: nlmlogvariableindex  <key>
            
            	A monotonically increasing integer, starting at 1 for a given nlmLogIndex, for indexing variables within the logged Notification
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogvariablecounter32val
            
            	The value when nlmLogVariableType is 'counter32'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariablecounter64val
            
            	The value when nlmLogVariableType is 'counter64'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: nlmlogvariableid
            
            	The variable's object identifier
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogvariableinteger32val
            
            	The value when nlmLogVariableType is 'integer32'
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: nlmlogvariableipaddressval
            
            	The value when nlmLogVariableType is 'ipAddress'. Although this seems to be unfriendly for IPv6, we have to recognize that there are a number of older MIBs that do contain an IPv4 format address, known as IpAddress.  IPv6 addresses are represented using TAddress or InetAddress, and so the underlying datatype is OCTET STRING, and their value would be stored in the nlmLogVariableOctetStringVal column
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: nlmlogvariableoctetstringval
            
            	The value when nlmLogVariableType is 'octetString'
            	**type**\:  str
            
            .. attribute:: nlmlogvariableoidval
            
            	The value when nlmLogVariableType is 'objectId'
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogvariableopaqueval
            
            	The value when nlmLogVariableType is 'opaque'
            	**type**\:  str
            
            .. attribute:: nlmlogvariabletimeticksval
            
            	The value when nlmLogVariableType is 'timeTicks'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariableunsigned32val
            
            	The value when nlmLogVariableType is 'unsigned32'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariablevaluetype
            
            	The type of the value.  One and only one of the value objects that follow must be instantiated, based on this type
            	**type**\:   :py:class:`Nlmlogvariablevaluetype <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry.Nlmlogvariablevaluetype>`
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                super(NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry, self).__init__()

                self.yang_name = "nlmLogVariableEntry"
                self.yang_parent_name = "nlmLogVariableTable"

                self.nlmlogname = YLeaf(YType.str, "nlmLogName")

                self.nlmlogindex = YLeaf(YType.str, "nlmLogIndex")

                self.nlmlogvariableindex = YLeaf(YType.uint32, "nlmLogVariableIndex")

                self.nlmlogvariablecounter32val = YLeaf(YType.uint32, "nlmLogVariableCounter32Val")

                self.nlmlogvariablecounter64val = YLeaf(YType.uint64, "nlmLogVariableCounter64Val")

                self.nlmlogvariableid = YLeaf(YType.str, "nlmLogVariableID")

                self.nlmlogvariableinteger32val = YLeaf(YType.int32, "nlmLogVariableInteger32Val")

                self.nlmlogvariableipaddressval = YLeaf(YType.str, "nlmLogVariableIpAddressVal")

                self.nlmlogvariableoctetstringval = YLeaf(YType.str, "nlmLogVariableOctetStringVal")

                self.nlmlogvariableoidval = YLeaf(YType.str, "nlmLogVariableOidVal")

                self.nlmlogvariableopaqueval = YLeaf(YType.str, "nlmLogVariableOpaqueVal")

                self.nlmlogvariabletimeticksval = YLeaf(YType.uint32, "nlmLogVariableTimeTicksVal")

                self.nlmlogvariableunsigned32val = YLeaf(YType.uint32, "nlmLogVariableUnsigned32Val")

                self.nlmlogvariablevaluetype = YLeaf(YType.enumeration, "nlmLogVariableValueType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nlmlogname",
                                "nlmlogindex",
                                "nlmlogvariableindex",
                                "nlmlogvariablecounter32val",
                                "nlmlogvariablecounter64val",
                                "nlmlogvariableid",
                                "nlmlogvariableinteger32val",
                                "nlmlogvariableipaddressval",
                                "nlmlogvariableoctetstringval",
                                "nlmlogvariableoidval",
                                "nlmlogvariableopaqueval",
                                "nlmlogvariabletimeticksval",
                                "nlmlogvariableunsigned32val",
                                "nlmlogvariablevaluetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry, self).__setattr__(name, value)

            class Nlmlogvariablevaluetype(Enum):
                """
                Nlmlogvariablevaluetype

                The type of the value.  One and only one of the value

                objects that follow must be instantiated, based on this type.

                .. data:: counter32 = 1

                .. data:: unsigned32 = 2

                .. data:: timeTicks = 3

                .. data:: integer32 = 4

                .. data:: ipAddress = 5

                .. data:: octetString = 6

                .. data:: objectId = 7

                .. data:: counter64 = 8

                .. data:: opaque = 9

                """

                counter32 = Enum.YLeaf(1, "counter32")

                unsigned32 = Enum.YLeaf(2, "unsigned32")

                timeTicks = Enum.YLeaf(3, "timeTicks")

                integer32 = Enum.YLeaf(4, "integer32")

                ipAddress = Enum.YLeaf(5, "ipAddress")

                octetString = Enum.YLeaf(6, "octetString")

                objectId = Enum.YLeaf(7, "objectId")

                counter64 = Enum.YLeaf(8, "counter64")

                opaque = Enum.YLeaf(9, "opaque")


            def has_data(self):
                return (
                    self.nlmlogname.is_set or
                    self.nlmlogindex.is_set or
                    self.nlmlogvariableindex.is_set or
                    self.nlmlogvariablecounter32val.is_set or
                    self.nlmlogvariablecounter64val.is_set or
                    self.nlmlogvariableid.is_set or
                    self.nlmlogvariableinteger32val.is_set or
                    self.nlmlogvariableipaddressval.is_set or
                    self.nlmlogvariableoctetstringval.is_set or
                    self.nlmlogvariableoidval.is_set or
                    self.nlmlogvariableopaqueval.is_set or
                    self.nlmlogvariabletimeticksval.is_set or
                    self.nlmlogvariableunsigned32val.is_set or
                    self.nlmlogvariablevaluetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nlmlogname.yfilter != YFilter.not_set or
                    self.nlmlogindex.yfilter != YFilter.not_set or
                    self.nlmlogvariableindex.yfilter != YFilter.not_set or
                    self.nlmlogvariablecounter32val.yfilter != YFilter.not_set or
                    self.nlmlogvariablecounter64val.yfilter != YFilter.not_set or
                    self.nlmlogvariableid.yfilter != YFilter.not_set or
                    self.nlmlogvariableinteger32val.yfilter != YFilter.not_set or
                    self.nlmlogvariableipaddressval.yfilter != YFilter.not_set or
                    self.nlmlogvariableoctetstringval.yfilter != YFilter.not_set or
                    self.nlmlogvariableoidval.yfilter != YFilter.not_set or
                    self.nlmlogvariableopaqueval.yfilter != YFilter.not_set or
                    self.nlmlogvariabletimeticksval.yfilter != YFilter.not_set or
                    self.nlmlogvariableunsigned32val.yfilter != YFilter.not_set or
                    self.nlmlogvariablevaluetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nlmLogVariableEntry" + "[nlmLogName='" + self.nlmlogname.get() + "']" + "[nlmLogIndex='" + self.nlmlogindex.get() + "']" + "[nlmLogVariableIndex='" + self.nlmlogvariableindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/nlmLogVariableTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nlmlogname.is_set or self.nlmlogname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogname.get_name_leafdata())
                if (self.nlmlogindex.is_set or self.nlmlogindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogindex.get_name_leafdata())
                if (self.nlmlogvariableindex.is_set or self.nlmlogvariableindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableindex.get_name_leafdata())
                if (self.nlmlogvariablecounter32val.is_set or self.nlmlogvariablecounter32val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariablecounter32val.get_name_leafdata())
                if (self.nlmlogvariablecounter64val.is_set or self.nlmlogvariablecounter64val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariablecounter64val.get_name_leafdata())
                if (self.nlmlogvariableid.is_set or self.nlmlogvariableid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableid.get_name_leafdata())
                if (self.nlmlogvariableinteger32val.is_set or self.nlmlogvariableinteger32val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableinteger32val.get_name_leafdata())
                if (self.nlmlogvariableipaddressval.is_set or self.nlmlogvariableipaddressval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableipaddressval.get_name_leafdata())
                if (self.nlmlogvariableoctetstringval.is_set or self.nlmlogvariableoctetstringval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableoctetstringval.get_name_leafdata())
                if (self.nlmlogvariableoidval.is_set or self.nlmlogvariableoidval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableoidval.get_name_leafdata())
                if (self.nlmlogvariableopaqueval.is_set or self.nlmlogvariableopaqueval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableopaqueval.get_name_leafdata())
                if (self.nlmlogvariabletimeticksval.is_set or self.nlmlogvariabletimeticksval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariabletimeticksval.get_name_leafdata())
                if (self.nlmlogvariableunsigned32val.is_set or self.nlmlogvariableunsigned32val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariableunsigned32val.get_name_leafdata())
                if (self.nlmlogvariablevaluetype.is_set or self.nlmlogvariablevaluetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nlmlogvariablevaluetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nlmLogName" or name == "nlmLogIndex" or name == "nlmLogVariableIndex" or name == "nlmLogVariableCounter32Val" or name == "nlmLogVariableCounter64Val" or name == "nlmLogVariableID" or name == "nlmLogVariableInteger32Val" or name == "nlmLogVariableIpAddressVal" or name == "nlmLogVariableOctetStringVal" or name == "nlmLogVariableOidVal" or name == "nlmLogVariableOpaqueVal" or name == "nlmLogVariableTimeTicksVal" or name == "nlmLogVariableUnsigned32Val" or name == "nlmLogVariableValueType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nlmLogName"):
                    self.nlmlogname = value
                    self.nlmlogname.value_namespace = name_space
                    self.nlmlogname.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogIndex"):
                    self.nlmlogindex = value
                    self.nlmlogindex.value_namespace = name_space
                    self.nlmlogindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableIndex"):
                    self.nlmlogvariableindex = value
                    self.nlmlogvariableindex.value_namespace = name_space
                    self.nlmlogvariableindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableCounter32Val"):
                    self.nlmlogvariablecounter32val = value
                    self.nlmlogvariablecounter32val.value_namespace = name_space
                    self.nlmlogvariablecounter32val.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableCounter64Val"):
                    self.nlmlogvariablecounter64val = value
                    self.nlmlogvariablecounter64val.value_namespace = name_space
                    self.nlmlogvariablecounter64val.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableID"):
                    self.nlmlogvariableid = value
                    self.nlmlogvariableid.value_namespace = name_space
                    self.nlmlogvariableid.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableInteger32Val"):
                    self.nlmlogvariableinteger32val = value
                    self.nlmlogvariableinteger32val.value_namespace = name_space
                    self.nlmlogvariableinteger32val.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableIpAddressVal"):
                    self.nlmlogvariableipaddressval = value
                    self.nlmlogvariableipaddressval.value_namespace = name_space
                    self.nlmlogvariableipaddressval.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableOctetStringVal"):
                    self.nlmlogvariableoctetstringval = value
                    self.nlmlogvariableoctetstringval.value_namespace = name_space
                    self.nlmlogvariableoctetstringval.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableOidVal"):
                    self.nlmlogvariableoidval = value
                    self.nlmlogvariableoidval.value_namespace = name_space
                    self.nlmlogvariableoidval.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableOpaqueVal"):
                    self.nlmlogvariableopaqueval = value
                    self.nlmlogvariableopaqueval.value_namespace = name_space
                    self.nlmlogvariableopaqueval.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableTimeTicksVal"):
                    self.nlmlogvariabletimeticksval = value
                    self.nlmlogvariabletimeticksval.value_namespace = name_space
                    self.nlmlogvariabletimeticksval.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableUnsigned32Val"):
                    self.nlmlogvariableunsigned32val = value
                    self.nlmlogvariableunsigned32val.value_namespace = name_space
                    self.nlmlogvariableunsigned32val.value_namespace_prefix = name_space_prefix
                if(value_path == "nlmLogVariableValueType"):
                    self.nlmlogvariablevaluetype = value
                    self.nlmlogvariablevaluetype.value_namespace = name_space
                    self.nlmlogvariablevaluetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nlmlogvariableentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nlmlogvariableentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nlmLogVariableTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nlmLogVariableEntry"):
                for c in self.nlmlogvariableentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nlmlogvariableentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nlmLogVariableEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.nlmconfig is not None and self.nlmconfig.has_data()) or
            (self.nlmconfiglogtable is not None and self.nlmconfiglogtable.has_data()) or
            (self.nlmlogtable is not None and self.nlmlogtable.has_data()) or
            (self.nlmlogvariabletable is not None and self.nlmlogvariabletable.has_data()) or
            (self.nlmstats is not None and self.nlmstats.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nlmconfig is not None and self.nlmconfig.has_operation()) or
            (self.nlmconfiglogtable is not None and self.nlmconfiglogtable.has_operation()) or
            (self.nlmlogtable is not None and self.nlmlogtable.has_operation()) or
            (self.nlmlogvariabletable is not None and self.nlmlogvariabletable.has_operation()) or
            (self.nlmstats is not None and self.nlmstats.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB" + path_buffer

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

        if (child_yang_name == "nlmConfig"):
            if (self.nlmconfig is None):
                self.nlmconfig = NotificationLogMib.Nlmconfig()
                self.nlmconfig.parent = self
                self._children_name_map["nlmconfig"] = "nlmConfig"
            return self.nlmconfig

        if (child_yang_name == "nlmConfigLogTable"):
            if (self.nlmconfiglogtable is None):
                self.nlmconfiglogtable = NotificationLogMib.Nlmconfiglogtable()
                self.nlmconfiglogtable.parent = self
                self._children_name_map["nlmconfiglogtable"] = "nlmConfigLogTable"
            return self.nlmconfiglogtable

        if (child_yang_name == "nlmLogTable"):
            if (self.nlmlogtable is None):
                self.nlmlogtable = NotificationLogMib.Nlmlogtable()
                self.nlmlogtable.parent = self
                self._children_name_map["nlmlogtable"] = "nlmLogTable"
            return self.nlmlogtable

        if (child_yang_name == "nlmLogVariableTable"):
            if (self.nlmlogvariabletable is None):
                self.nlmlogvariabletable = NotificationLogMib.Nlmlogvariabletable()
                self.nlmlogvariabletable.parent = self
                self._children_name_map["nlmlogvariabletable"] = "nlmLogVariableTable"
            return self.nlmlogvariabletable

        if (child_yang_name == "nlmStats"):
            if (self.nlmstats is None):
                self.nlmstats = NotificationLogMib.Nlmstats()
                self.nlmstats.parent = self
                self._children_name_map["nlmstats"] = "nlmStats"
            return self.nlmstats

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nlmConfig" or name == "nlmConfigLogTable" or name == "nlmLogTable" or name == "nlmLogVariableTable" or name == "nlmStats"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NotificationLogMib()
        return self._top_entity

