""" NOTIFICATION_LOG_MIB 

The MIB module for logging SNMP Notifications, that is, Traps
and Informs.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class NotificationLogMib(object):
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
        self.nlmconfig = NotificationLogMib.Nlmconfig()
        self.nlmconfig.parent = self
        self.nlmconfiglogtable = NotificationLogMib.Nlmconfiglogtable()
        self.nlmconfiglogtable.parent = self
        self.nlmlogtable = NotificationLogMib.Nlmlogtable()
        self.nlmlogtable.parent = self
        self.nlmlogvariabletable = NotificationLogMib.Nlmlogvariabletable()
        self.nlmlogvariabletable.parent = self
        self.nlmstats = NotificationLogMib.Nlmstats()
        self.nlmstats.parent = self


    class Nlmconfig(object):
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
            self.parent = None
            self.nlmconfigglobalageout = None
            self.nlmconfigglobalentrylimit = None

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nlmconfigglobalageout is not None:
                return True

            if self.nlmconfigglobalentrylimit is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NotificationLogMib.Nlmconfig']['meta_info']


    class Nlmstats(object):
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
            self.parent = None
            self.nlmstatsglobalnotificationsbumped = None
            self.nlmstatsglobalnotificationslogged = None

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nlmstatsglobalnotificationsbumped is not None:
                return True

            if self.nlmstatsglobalnotificationslogged is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NotificationLogMib.Nlmstats']['meta_info']


    class Nlmconfiglogtable(object):
        """
        A table of logging control entries.
        
        .. attribute:: nlmconfiglogentry
        
        	A logging control entry.  Depending on the entry's storage type entries may be supplied by the system or created and deleted by applications using nlmConfigLogEntryStatus
        	**type**\: list of    :py:class:`Nlmconfiglogentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmconfiglogentry = YList()
            self.nlmconfiglogentry.parent = self
            self.nlmconfiglogentry.name = 'nlmconfiglogentry'


        class Nlmconfiglogentry(object):
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
            	**type**\:   :py:class:`NlmconfiglogadminstatusEnum <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogadminstatusEnum>`
            
            .. attribute:: nlmconfiglogentrylimit
            
            	The maximum number of notification entries that can be held in nlmLogTable for this named log.  A particular setting does not guarantee that that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications are discarded to bring the log down to the new limit.  A value of 0 indicates no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmconfiglogentrystatus
            
            	Control for creating and deleting entries.  Entries may be modified while active.  For non\-null\-named logs, the managed system records the security credentials from the request that sets nlmConfigLogStatus to 'active' and uses that identity to apply access control to the objects in the Notification to decide if that Notification may be logged
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: nlmconfiglogfiltername
            
            	A value of snmpNotifyFilterProfileName as used as an index into the snmpNotifyFilterTable in the SNMP Notification MIB, specifying the locally or remotely originated Notifications to be filtered out and not logged in this log.  A zero\-length value or a name that does not identify an existing entry in snmpNotifyFilterTable indicate no Notifications are to be logged in this log
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: nlmconfiglogoperstatus
            
            	The operational status of this log\:  disabled  administratively disabled  operational    administratively enabled and working  noFilter  administratively enabled but either           nlmConfigLogFilterName is zero length           or does not name an existing entry in           snmpNotifyFilterTable
            	**type**\:   :py:class:`NlmconfiglogoperstatusEnum <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogoperstatusEnum>`
            
            .. attribute:: nlmconfiglogstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
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
                self.parent = None
                self.nlmlogname = None
                self.nlmconfiglogadminstatus = None
                self.nlmconfiglogentrylimit = None
                self.nlmconfiglogentrystatus = None
                self.nlmconfiglogfiltername = None
                self.nlmconfiglogoperstatus = None
                self.nlmconfiglogstoragetype = None
                self.nlmstatslognotificationsbumped = None
                self.nlmstatslognotificationslogged = None

            class NlmconfiglogadminstatusEnum(Enum):
                """
                NlmconfiglogadminstatusEnum

                Control to enable or disable the log without otherwise

                disturbing the log's entry.

                Please be aware that contention between multiple managers

                trying to set this object to different values MAY affect the

                reliability and completeness of data seen by each manager.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
                    return meta._meta_table['NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogadminstatusEnum']


            class NlmconfiglogoperstatusEnum(Enum):
                """
                NlmconfiglogoperstatusEnum

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

                disabled = 1

                operational = 2

                noFilter = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
                    return meta._meta_table['NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogoperstatusEnum']


            @property
            def _common_path(self):
                if self.nlmlogname is None:
                    raise YPYModelError('Key property nlmlogname is None')

                return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmConfigLogTable/NOTIFICATION-LOG-MIB:nlmConfigLogEntry[NOTIFICATION-LOG-MIB:nlmLogName = ' + str(self.nlmlogname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nlmlogname is not None:
                    return True

                if self.nlmconfiglogadminstatus is not None:
                    return True

                if self.nlmconfiglogentrylimit is not None:
                    return True

                if self.nlmconfiglogentrystatus is not None:
                    return True

                if self.nlmconfiglogfiltername is not None:
                    return True

                if self.nlmconfiglogoperstatus is not None:
                    return True

                if self.nlmconfiglogstoragetype is not None:
                    return True

                if self.nlmstatslognotificationsbumped is not None:
                    return True

                if self.nlmstatslognotificationslogged is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
                return meta._meta_table['NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry']['meta_info']

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmConfigLogTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nlmconfiglogentry is not None:
                for child_ref in self.nlmconfiglogentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NotificationLogMib.Nlmconfiglogtable']['meta_info']


    class Nlmlogtable(object):
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
            self.parent = None
            self.nlmlogentry = YList()
            self.nlmlogentry.parent = self
            self.nlmlogentry.name = 'nlmlogentry'


        class Nlmlogentry(object):
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
                self.parent = None
                self.nlmlogname = None
                self.nlmlogindex = None
                self.nlmlogcontextengineid = None
                self.nlmlogcontextname = None
                self.nlmlogdateandtime = None
                self.nlmlogengineid = None
                self.nlmlogenginetaddress = None
                self.nlmlogenginetdomain = None
                self.nlmlognotificationid = None
                self.nlmlogtime = None

            @property
            def _common_path(self):
                if self.nlmlogname is None:
                    raise YPYModelError('Key property nlmlogname is None')
                if self.nlmlogindex is None:
                    raise YPYModelError('Key property nlmlogindex is None')

                return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogTable/NOTIFICATION-LOG-MIB:nlmLogEntry[NOTIFICATION-LOG-MIB:nlmLogName = ' + str(self.nlmlogname) + '][NOTIFICATION-LOG-MIB:nlmLogIndex = ' + str(self.nlmlogindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nlmlogname is not None:
                    return True

                if self.nlmlogindex is not None:
                    return True

                if self.nlmlogcontextengineid is not None:
                    return True

                if self.nlmlogcontextname is not None:
                    return True

                if self.nlmlogdateandtime is not None:
                    return True

                if self.nlmlogengineid is not None:
                    return True

                if self.nlmlogenginetaddress is not None:
                    return True

                if self.nlmlogenginetdomain is not None:
                    return True

                if self.nlmlognotificationid is not None:
                    return True

                if self.nlmlogtime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
                return meta._meta_table['NotificationLogMib.Nlmlogtable.Nlmlogentry']['meta_info']

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nlmlogentry is not None:
                for child_ref in self.nlmlogentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NotificationLogMib.Nlmlogtable']['meta_info']


    class Nlmlogvariabletable(object):
        """
        A table of variables to go with Notification log entries.
        
        .. attribute:: nlmlogvariableentry
        
        	A Notification log entry variable.  Entries appear in this table when there are variables in the varbind list of a Notification in nlmLogTable
        	**type**\: list of    :py:class:`Nlmlogvariableentry <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry>`
        
        

        """

        _prefix = 'NOTIFICATION-LOG-MIB'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmlogvariableentry = YList()
            self.nlmlogvariableentry.parent = self
            self.nlmlogvariableentry.name = 'nlmlogvariableentry'


        class Nlmlogvariableentry(object):
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
            	**type**\:   :py:class:`NlmlogvariablevaluetypeEnum <ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB.NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry.NlmlogvariablevaluetypeEnum>`
            
            

            """

            _prefix = 'NOTIFICATION-LOG-MIB'
            _revision = '2000-11-27'

            def __init__(self):
                self.parent = None
                self.nlmlogname = None
                self.nlmlogindex = None
                self.nlmlogvariableindex = None
                self.nlmlogvariablecounter32val = None
                self.nlmlogvariablecounter64val = None
                self.nlmlogvariableid = None
                self.nlmlogvariableinteger32val = None
                self.nlmlogvariableipaddressval = None
                self.nlmlogvariableoctetstringval = None
                self.nlmlogvariableoidval = None
                self.nlmlogvariableopaqueval = None
                self.nlmlogvariabletimeticksval = None
                self.nlmlogvariableunsigned32val = None
                self.nlmlogvariablevaluetype = None

            class NlmlogvariablevaluetypeEnum(Enum):
                """
                NlmlogvariablevaluetypeEnum

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

                counter32 = 1

                unsigned32 = 2

                timeTicks = 3

                integer32 = 4

                ipAddress = 5

                octetString = 6

                objectId = 7

                counter64 = 8

                opaque = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
                    return meta._meta_table['NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry.NlmlogvariablevaluetypeEnum']


            @property
            def _common_path(self):
                if self.nlmlogname is None:
                    raise YPYModelError('Key property nlmlogname is None')
                if self.nlmlogindex is None:
                    raise YPYModelError('Key property nlmlogindex is None')
                if self.nlmlogvariableindex is None:
                    raise YPYModelError('Key property nlmlogvariableindex is None')

                return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogVariableTable/NOTIFICATION-LOG-MIB:nlmLogVariableEntry[NOTIFICATION-LOG-MIB:nlmLogName = ' + str(self.nlmlogname) + '][NOTIFICATION-LOG-MIB:nlmLogIndex = ' + str(self.nlmlogindex) + '][NOTIFICATION-LOG-MIB:nlmLogVariableIndex = ' + str(self.nlmlogvariableindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nlmlogname is not None:
                    return True

                if self.nlmlogindex is not None:
                    return True

                if self.nlmlogvariableindex is not None:
                    return True

                if self.nlmlogvariablecounter32val is not None:
                    return True

                if self.nlmlogvariablecounter64val is not None:
                    return True

                if self.nlmlogvariableid is not None:
                    return True

                if self.nlmlogvariableinteger32val is not None:
                    return True

                if self.nlmlogvariableipaddressval is not None:
                    return True

                if self.nlmlogvariableoctetstringval is not None:
                    return True

                if self.nlmlogvariableoidval is not None:
                    return True

                if self.nlmlogvariableopaqueval is not None:
                    return True

                if self.nlmlogvariabletimeticksval is not None:
                    return True

                if self.nlmlogvariableunsigned32val is not None:
                    return True

                if self.nlmlogvariablevaluetype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
                return meta._meta_table['NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry']['meta_info']

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogVariableTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.nlmlogvariableentry is not None:
                for child_ref in self.nlmlogvariableentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NotificationLogMib.Nlmlogvariabletable']['meta_info']

    @property
    def _common_path(self):

        return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nlmconfig is not None and self.nlmconfig._has_data():
            return True

        if self.nlmconfiglogtable is not None and self.nlmconfiglogtable._has_data():
            return True

        if self.nlmlogtable is not None and self.nlmlogtable._has_data():
            return True

        if self.nlmlogvariabletable is not None and self.nlmlogvariabletable._has_data():
            return True

        if self.nlmstats is not None and self.nlmstats._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _NOTIFICATION_LOG_MIB as meta
        return meta._meta_table['NotificationLogMib']['meta_info']


