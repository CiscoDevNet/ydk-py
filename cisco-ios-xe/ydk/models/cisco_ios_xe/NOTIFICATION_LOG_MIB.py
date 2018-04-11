""" NOTIFICATION_LOG_MIB 

The MIB module for logging SNMP Notifications, that is, Traps
and Informs.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NOTIFICATIONLOGMIB(Entity):
    """
    
    
    .. attribute:: nlmconfig
    
    	
    	**type**\:  :py:class:`Nlmconfig <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfig>`
    
    .. attribute:: nlmstats
    
    	
    	**type**\:  :py:class:`Nlmstats <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmstats>`
    
    .. attribute:: nlmconfiglogtable
    
    	A table of logging control entries
    	**type**\:  :py:class:`Nlmconfiglogtable <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfiglogtable>`
    
    .. attribute:: nlmlogtable
    
    	A table of Notification log entries.  It is an implementation\-specific matter whether entries in this table are preserved across initializations of the management system.  In general one would expect that they are not.  Note that keeping entries across initializations of the management system leads to some confusion with counters and TimeStamps, since both of those are based on sysUpTime, which resets on management initialization.  In this situation, counters apply only after the reset and nlmLogTime for entries made before the reset MUST be set to 0
    	**type**\:  :py:class:`Nlmlogtable <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmlogtable>`
    
    .. attribute:: nlmlogvariabletable
    
    	A table of variables to go with Notification log entries
    	**type**\:  :py:class:`Nlmlogvariabletable <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmlogvariabletable>`
    
    

    """

    _prefix = 'NOTIFICATION-LOG-MIB'
    _revision = '2000-11-27'

    def __init__(self):
        super(NOTIFICATIONLOGMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "NOTIFICATION-LOG-MIB"
        self.yang_parent_name = "NOTIFICATION-LOG-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nlmConfig", ("nlmconfig", NOTIFICATIONLOGMIB.Nlmconfig)), ("nlmStats", ("nlmstats", NOTIFICATIONLOGMIB.Nlmstats)), ("nlmConfigLogTable", ("nlmconfiglogtable", NOTIFICATIONLOGMIB.Nlmconfiglogtable)), ("nlmLogTable", ("nlmlogtable", NOTIFICATIONLOGMIB.Nlmlogtable)), ("nlmLogVariableTable", ("nlmlogvariabletable", NOTIFICATIONLOGMIB.Nlmlogvariabletable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nlmconfig = NOTIFICATIONLOGMIB.Nlmconfig()
        self.nlmconfig.parent = self
        self._children_name_map["nlmconfig"] = "nlmConfig"
        self._children_yang_names.add("nlmConfig")

        self.nlmstats = NOTIFICATIONLOGMIB.Nlmstats()
        self.nlmstats.parent = self
        self._children_name_map["nlmstats"] = "nlmStats"
        self._children_yang_names.add("nlmStats")

        self.nlmconfiglogtable = NOTIFICATIONLOGMIB.Nlmconfiglogtable()
        self.nlmconfiglogtable.parent = self
        self._children_name_map["nlmconfiglogtable"] = "nlmConfigLogTable"
        self._children_yang_names.add("nlmConfigLogTable")

        self.nlmlogtable = NOTIFICATIONLOGMIB.Nlmlogtable()
        self.nlmlogtable.parent = self
        self._children_name_map["nlmlogtable"] = "nlmLogTable"
        self._children_yang_names.add("nlmLogTable")

        self.nlmlogvariabletable = NOTIFICATIONLOGMIB.Nlmlogvariabletable()
        self.nlmlogvariabletable.parent = self
        self._children_name_map["nlmlogvariabletable"] = "nlmLogVariableTable"
        self._children_yang_names.add("nlmLogVariableTable")
        self._segment_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB"


    class Nlmconfig(Entity):
        """
        
        
        .. attribute:: nlmconfigglobalentrylimit
        
        	The maximum number of notification entries that may be held in nlmLogTable for all nlmLogNames added together.  A particular setting does not guarantee that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications MUST be discarded to bring the log down to the new limit \- thus the value of nlmConfigGlobalEntryLimit MUST take precedence over the values of nlmConfigGlobalAgeOut and nlmConfigLogEntryLimit, even if the Notification being discarded has been present for fewer minutes than the value of nlmConfigGlobalAgeOut, or if the named log has fewer entries than that specified in nlmConfigLogEntryLimit.  A value of 0 means no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: nlmconfigglobalageout
        
        	The number of minutes a Notification SHOULD be kept in a log before it is automatically removed.  If an application changes the value of nlmConfigGlobalAgeOut, Notifications older than the new time MAY be discarded to meet the new time.  A value of 0 means no age out.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: minutes
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NOTIFICATIONLOGMIB.Nlmconfig, self).__init__()

            self.yang_name = "nlmConfig"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('nlmconfigglobalentrylimit', YLeaf(YType.uint32, 'nlmConfigGlobalEntryLimit')),
                ('nlmconfigglobalageout', YLeaf(YType.uint32, 'nlmConfigGlobalAgeOut')),
            ])
            self.nlmconfigglobalentrylimit = None
            self.nlmconfigglobalageout = None
            self._segment_path = lambda: "nlmConfig"
            self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NOTIFICATIONLOGMIB.Nlmconfig, ['nlmconfigglobalentrylimit', 'nlmconfigglobalageout'], name, value)


    class Nlmstats(Entity):
        """
        
        
        .. attribute:: nlmstatsglobalnotificationslogged
        
        	The number of Notifications put into the nlmLogTable.  This counts a Notification once for each log entry, so a Notification  put into multiple logs is counted multiple times
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: notifications
        
        .. attribute:: nlmstatsglobalnotificationsbumped
        
        	The number of log entries discarded to make room for a new entry due to lack of resources or the value of nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not include entries discarded due to the value of nlmConfigGlobalAgeOut
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: notifications
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NOTIFICATIONLOGMIB.Nlmstats, self).__init__()

            self.yang_name = "nlmStats"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('nlmstatsglobalnotificationslogged', YLeaf(YType.uint32, 'nlmStatsGlobalNotificationsLogged')),
                ('nlmstatsglobalnotificationsbumped', YLeaf(YType.uint32, 'nlmStatsGlobalNotificationsBumped')),
            ])
            self.nlmstatsglobalnotificationslogged = None
            self.nlmstatsglobalnotificationsbumped = None
            self._segment_path = lambda: "nlmStats"
            self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NOTIFICATIONLOGMIB.Nlmstats, ['nlmstatsglobalnotificationslogged', 'nlmstatsglobalnotificationsbumped'], name, value)


    class Nlmconfiglogtable(Entity):
        """
        A table of logging control entries.
        
        .. attribute:: nlmconfiglogentry
        
        	A logging control entry.  Depending on the entry's storage type entries may be supplied by the system or created and deleted by applications using nlmConfigLogEntryStatus
        	**type**\: list of  		 :py:class:`Nlmconfiglogentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NOTIFICATIONLOGMIB.Nlmconfiglogtable, self).__init__()

            self.yang_name = "nlmConfigLogTable"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("nlmConfigLogEntry", ("nlmconfiglogentry", NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry))])
            self._leafs = OrderedDict()

            self.nlmconfiglogentry = YList(self)
            self._segment_path = lambda: "nlmConfigLogTable"
            self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NOTIFICATIONLOGMIB.Nlmconfiglogtable, [], name, value)


        class Nlmconfiglogentry(Entity):
            """
            A logging control entry.  Depending on the entry's storage type
            entries may be supplied by the system or created and deleted by
            applications using nlmConfigLogEntryStatus.
            
            .. attribute:: nlmlogname  (key)
            
            	The name of the log.  An implementation may allow multiple named logs, up to some implementation\-specific limit (which may be none).  A zero\-length log name is reserved for creation and deletion by the managed system, and MUST be used as the default log name by systems that do not support named logs
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: nlmconfiglogfiltername
            
            	A value of snmpNotifyFilterProfileName as used as an index into the snmpNotifyFilterTable in the SNMP Notification MIB, specifying the locally or remotely originated Notifications to be filtered out and not logged in this log.  A zero\-length value or a name that does not identify an existing entry in snmpNotifyFilterTable indicate no Notifications are to be logged in this log
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: nlmconfiglogentrylimit
            
            	The maximum number of notification entries that can be held in nlmLogTable for this named log.  A particular setting does not guarantee that that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications are discarded to bring the log down to the new limit.  A value of 0 indicates no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmconfiglogadminstatus
            
            	Control to enable or disable the log without otherwise disturbing the log's entry.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\:  :py:class:`Nlmconfiglogadminstatus <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry.Nlmconfiglogadminstatus>`
            
            .. attribute:: nlmconfiglogoperstatus
            
            	The operational status of this log\:  disabled  administratively disabled  operational    administratively enabled and working  noFilter  administratively enabled but either           nlmConfigLogFilterName is zero length           or does not name an existing entry in           snmpNotifyFilterTable
            	**type**\:  :py:class:`Nlmconfiglogoperstatus <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry.Nlmconfiglogoperstatus>`
            
            .. attribute:: nlmconfiglogstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: nlmconfiglogentrystatus
            
            	Control for creating and deleting entries.  Entries may be modified while active.  For non\-null\-named logs, the managed system records the security credentials from the request that sets nlmConfigLogStatus to 'active' and uses that identity to apply access control to the objects in the Notification to decide if that Notification may be logged
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: nlmstatslognotificationslogged
            
            	The number of Notifications put in this named log
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: notifications
            
            .. attribute:: nlmstatslognotificationsbumped
            
            	The number of log entries discarded from this named log to make room for a new entry due to lack of resources or the value of nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not include entries discarded due to the value of nlmConfigGlobalAgeOut
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: notifications
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                super(NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry, self).__init__()

                self.yang_name = "nlmConfigLogEntry"
                self.yang_parent_name = "nlmConfigLogTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nlmlogname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nlmlogname', YLeaf(YType.str, 'nlmLogName')),
                    ('nlmconfiglogfiltername', YLeaf(YType.str, 'nlmConfigLogFilterName')),
                    ('nlmconfiglogentrylimit', YLeaf(YType.uint32, 'nlmConfigLogEntryLimit')),
                    ('nlmconfiglogadminstatus', YLeaf(YType.enumeration, 'nlmConfigLogAdminStatus')),
                    ('nlmconfiglogoperstatus', YLeaf(YType.enumeration, 'nlmConfigLogOperStatus')),
                    ('nlmconfiglogstoragetype', YLeaf(YType.enumeration, 'nlmConfigLogStorageType')),
                    ('nlmconfiglogentrystatus', YLeaf(YType.enumeration, 'nlmConfigLogEntryStatus')),
                    ('nlmstatslognotificationslogged', YLeaf(YType.uint32, 'nlmStatsLogNotificationsLogged')),
                    ('nlmstatslognotificationsbumped', YLeaf(YType.uint32, 'nlmStatsLogNotificationsBumped')),
                ])
                self.nlmlogname = None
                self.nlmconfiglogfiltername = None
                self.nlmconfiglogentrylimit = None
                self.nlmconfiglogadminstatus = None
                self.nlmconfiglogoperstatus = None
                self.nlmconfiglogstoragetype = None
                self.nlmconfiglogentrystatus = None
                self.nlmstatslognotificationslogged = None
                self.nlmstatslognotificationsbumped = None
                self._segment_path = lambda: "nlmConfigLogEntry" + "[nlmLogName='" + str(self.nlmlogname) + "']"
                self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/nlmConfigLogTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry, ['nlmlogname', 'nlmconfiglogfiltername', 'nlmconfiglogentrylimit', 'nlmconfiglogadminstatus', 'nlmconfiglogoperstatus', 'nlmconfiglogstoragetype', 'nlmconfiglogentrystatus', 'nlmstatslognotificationslogged', 'nlmstatslognotificationsbumped'], name, value)

            class Nlmconfiglogadminstatus(Enum):
                """
                Nlmconfiglogadminstatus (Enum Class)

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
                Nlmconfiglogoperstatus (Enum Class)

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
        	**type**\: list of  		 :py:class:`Nlmlogentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmlogtable.Nlmlogentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NOTIFICATIONLOGMIB.Nlmlogtable, self).__init__()

            self.yang_name = "nlmLogTable"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("nlmLogEntry", ("nlmlogentry", NOTIFICATIONLOGMIB.Nlmlogtable.Nlmlogentry))])
            self._leafs = OrderedDict()

            self.nlmlogentry = YList(self)
            self._segment_path = lambda: "nlmLogTable"
            self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NOTIFICATIONLOGMIB.Nlmlogtable, [], name, value)


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
            
            .. attribute:: nlmlogname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`nlmlogname <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry>`
            
            .. attribute:: nlmlogindex  (key)
            
            	A monotonically increasing integer for the sole purpose of indexing entries within the named log.  When it reaches the maximum value, an extremely unlikely event, the agent wraps the value back to 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogtime
            
            	The value of sysUpTime when the entry was placed in the log. If the entry occurred before the most recent management system initialization this object value MUST be set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogdateandtime
            
            	The local date and time when the entry was logged, instantiated only by systems that have date and time capability
            	**type**\: str
            
            .. attribute:: nlmlogengineid
            
            	The identification of the SNMP engine at which the Notification originated.  If the log can contain Notifications from only one engine or the Trap is in SNMPv1 format, this object is a zero\-length string
            	**type**\: str
            
            	**length:** 5..32
            
            .. attribute:: nlmlogenginetaddress
            
            	The transport service address of the SNMP engine from which the Notification was received, formatted according to the corresponding value of nlmLogEngineTDomain. This is used to identify the source of an SNMPv1 trap, since an nlmLogEngineId cannot be extracted from the SNMPv1 trap pdu.  This object MUST always be instantiated, even if the log can contain Notifications from only one engine.  Please be aware that the nlmLogEngineTAddress may not uniquely identify the SNMP engine from which the Notification was received. For example, if an SNMP engine uses DHCP or NAT to obtain ip addresses, the address it uses may be shared with other network devices, and hence will not uniquely identify the SNMP engine
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: nlmlogenginetdomain
            
            	Indicates the kind of transport service by which a Notification was received from an SNMP engine. nlmLogEngineTAddress contains the transport service address of the SNMP engine from which this Notification was received.  Possible values for this object are presently found in the Transport Mappings for SNMPv2 document (RFC 1906 [8])
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogcontextengineid
            
            	If the Notification was received in a protocol which has a contextEngineID element like SNMPv3, this object has that value. Otherwise its value is a zero\-length string
            	**type**\: str
            
            	**length:** 5..32
            
            .. attribute:: nlmlogcontextname
            
            	The name of the SNMP MIB context from which the Notification came. For SNMPv1 Traps this is the community string from the Trap
            	**type**\: str
            
            .. attribute:: nlmlognotificationid
            
            	The NOTIFICATION\-TYPE object identifier of the Notification that occurred
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                super(NOTIFICATIONLOGMIB.Nlmlogtable.Nlmlogentry, self).__init__()

                self.yang_name = "nlmLogEntry"
                self.yang_parent_name = "nlmLogTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nlmlogname','nlmlogindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nlmlogname', YLeaf(YType.str, 'nlmLogName')),
                    ('nlmlogindex', YLeaf(YType.uint32, 'nlmLogIndex')),
                    ('nlmlogtime', YLeaf(YType.uint32, 'nlmLogTime')),
                    ('nlmlogdateandtime', YLeaf(YType.str, 'nlmLogDateAndTime')),
                    ('nlmlogengineid', YLeaf(YType.str, 'nlmLogEngineID')),
                    ('nlmlogenginetaddress', YLeaf(YType.str, 'nlmLogEngineTAddress')),
                    ('nlmlogenginetdomain', YLeaf(YType.str, 'nlmLogEngineTDomain')),
                    ('nlmlogcontextengineid', YLeaf(YType.str, 'nlmLogContextEngineID')),
                    ('nlmlogcontextname', YLeaf(YType.str, 'nlmLogContextName')),
                    ('nlmlognotificationid', YLeaf(YType.str, 'nlmLogNotificationID')),
                ])
                self.nlmlogname = None
                self.nlmlogindex = None
                self.nlmlogtime = None
                self.nlmlogdateandtime = None
                self.nlmlogengineid = None
                self.nlmlogenginetaddress = None
                self.nlmlogenginetdomain = None
                self.nlmlogcontextengineid = None
                self.nlmlogcontextname = None
                self.nlmlognotificationid = None
                self._segment_path = lambda: "nlmLogEntry" + "[nlmLogName='" + str(self.nlmlogname) + "']" + "[nlmLogIndex='" + str(self.nlmlogindex) + "']"
                self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/nlmLogTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NOTIFICATIONLOGMIB.Nlmlogtable.Nlmlogentry, ['nlmlogname', 'nlmlogindex', 'nlmlogtime', 'nlmlogdateandtime', 'nlmlogengineid', 'nlmlogenginetaddress', 'nlmlogenginetdomain', 'nlmlogcontextengineid', 'nlmlogcontextname', 'nlmlognotificationid'], name, value)


    class Nlmlogvariabletable(Entity):
        """
        A table of variables to go with Notification log entries.
        
        .. attribute:: nlmlogvariableentry
        
        	A Notification log entry variable.  Entries appear in this table when there are variables in the varbind list of a Notification in nlmLogTable
        	**type**\: list of  		 :py:class:`Nlmlogvariableentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmlogvariabletable.Nlmlogvariableentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            super(NOTIFICATIONLOGMIB.Nlmlogvariabletable, self).__init__()

            self.yang_name = "nlmLogVariableTable"
            self.yang_parent_name = "NOTIFICATION-LOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("nlmLogVariableEntry", ("nlmlogvariableentry", NOTIFICATIONLOGMIB.Nlmlogvariabletable.Nlmlogvariableentry))])
            self._leafs = OrderedDict()

            self.nlmlogvariableentry = YList(self)
            self._segment_path = lambda: "nlmLogVariableTable"
            self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NOTIFICATIONLOGMIB.Nlmlogvariabletable, [], name, value)


        class Nlmlogvariableentry(Entity):
            """
            A Notification log entry variable.
            
            Entries appear in this table when there are variables in
            the varbind list of a Notification in nlmLogTable.
            
            .. attribute:: nlmlogname  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`nlmlogname <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmconfiglogtable.Nlmconfiglogentry>`
            
            .. attribute:: nlmlogindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nlmlogindex <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmlogtable.Nlmlogentry>`
            
            .. attribute:: nlmlogvariableindex  (key)
            
            	A monotonically increasing integer, starting at 1 for a given nlmLogIndex, for indexing variables within the logged Notification
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogvariableid
            
            	The variable's object identifier
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogvariablevaluetype
            
            	The type of the value.  One and only one of the value objects that follow must be instantiated, based on this type
            	**type**\:  :py:class:`Nlmlogvariablevaluetype <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.Nlmlogvariabletable.Nlmlogvariableentry.Nlmlogvariablevaluetype>`
            
            .. attribute:: nlmlogvariablecounter32val
            
            	The value when nlmLogVariableType is 'counter32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariableunsigned32val
            
            	The value when nlmLogVariableType is 'unsigned32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariabletimeticksval
            
            	The value when nlmLogVariableType is 'timeTicks'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariableinteger32val
            
            	The value when nlmLogVariableType is 'integer32'
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: nlmlogvariableoctetstringval
            
            	The value when nlmLogVariableType is 'octetString'
            	**type**\: str
            
            .. attribute:: nlmlogvariableipaddressval
            
            	The value when nlmLogVariableType is 'ipAddress'. Although this seems to be unfriendly for IPv6, we have to recognize that there are a number of older MIBs that do contain an IPv4 format address, known as IpAddress.  IPv6 addresses are represented using TAddress or InetAddress, and so the underlying datatype is OCTET STRING, and their value would be stored in the nlmLogVariableOctetStringVal column
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: nlmlogvariableoidval
            
            	The value when nlmLogVariableType is 'objectId'
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogvariablecounter64val
            
            	The value when nlmLogVariableType is 'counter64'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: nlmlogvariableopaqueval
            
            	The value when nlmLogVariableType is 'opaque'
            	**type**\: str
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                super(NOTIFICATIONLOGMIB.Nlmlogvariabletable.Nlmlogvariableentry, self).__init__()

                self.yang_name = "nlmLogVariableEntry"
                self.yang_parent_name = "nlmLogVariableTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nlmlogname','nlmlogindex','nlmlogvariableindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nlmlogname', YLeaf(YType.str, 'nlmLogName')),
                    ('nlmlogindex', YLeaf(YType.str, 'nlmLogIndex')),
                    ('nlmlogvariableindex', YLeaf(YType.uint32, 'nlmLogVariableIndex')),
                    ('nlmlogvariableid', YLeaf(YType.str, 'nlmLogVariableID')),
                    ('nlmlogvariablevaluetype', YLeaf(YType.enumeration, 'nlmLogVariableValueType')),
                    ('nlmlogvariablecounter32val', YLeaf(YType.uint32, 'nlmLogVariableCounter32Val')),
                    ('nlmlogvariableunsigned32val', YLeaf(YType.uint32, 'nlmLogVariableUnsigned32Val')),
                    ('nlmlogvariabletimeticksval', YLeaf(YType.uint32, 'nlmLogVariableTimeTicksVal')),
                    ('nlmlogvariableinteger32val', YLeaf(YType.int32, 'nlmLogVariableInteger32Val')),
                    ('nlmlogvariableoctetstringval', YLeaf(YType.str, 'nlmLogVariableOctetStringVal')),
                    ('nlmlogvariableipaddressval', YLeaf(YType.str, 'nlmLogVariableIpAddressVal')),
                    ('nlmlogvariableoidval', YLeaf(YType.str, 'nlmLogVariableOidVal')),
                    ('nlmlogvariablecounter64val', YLeaf(YType.uint64, 'nlmLogVariableCounter64Val')),
                    ('nlmlogvariableopaqueval', YLeaf(YType.str, 'nlmLogVariableOpaqueVal')),
                ])
                self.nlmlogname = None
                self.nlmlogindex = None
                self.nlmlogvariableindex = None
                self.nlmlogvariableid = None
                self.nlmlogvariablevaluetype = None
                self.nlmlogvariablecounter32val = None
                self.nlmlogvariableunsigned32val = None
                self.nlmlogvariabletimeticksval = None
                self.nlmlogvariableinteger32val = None
                self.nlmlogvariableoctetstringval = None
                self.nlmlogvariableipaddressval = None
                self.nlmlogvariableoidval = None
                self.nlmlogvariablecounter64val = None
                self.nlmlogvariableopaqueval = None
                self._segment_path = lambda: "nlmLogVariableEntry" + "[nlmLogName='" + str(self.nlmlogname) + "']" + "[nlmLogIndex='" + str(self.nlmlogindex) + "']" + "[nlmLogVariableIndex='" + str(self.nlmlogvariableindex) + "']"
                self._absolute_path = lambda: "NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/nlmLogVariableTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NOTIFICATIONLOGMIB.Nlmlogvariabletable.Nlmlogvariableentry, ['nlmlogname', 'nlmlogindex', 'nlmlogvariableindex', 'nlmlogvariableid', 'nlmlogvariablevaluetype', 'nlmlogvariablecounter32val', 'nlmlogvariableunsigned32val', 'nlmlogvariabletimeticksval', 'nlmlogvariableinteger32val', 'nlmlogvariableoctetstringval', 'nlmlogvariableipaddressval', 'nlmlogvariableoidval', 'nlmlogvariablecounter64val', 'nlmlogvariableopaqueval'], name, value)

            class Nlmlogvariablevaluetype(Enum):
                """
                Nlmlogvariablevaluetype (Enum Class)

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


    def clone_ptr(self):
        self._top_entity = NOTIFICATIONLOGMIB()
        return self._top_entity

