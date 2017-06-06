


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NotificationLogMib.Nlmconfig' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmconfig',
            False, 
            [
            _MetaInfoClassMember('nlmConfigGlobalAgeOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of minutes a Notification SHOULD be kept in a log
                before it is automatically removed.
                
                If an application changes the value of nlmConfigGlobalAgeOut,
                Notifications older than the new time MAY be discarded to meet the
                new time.
                
                A value of 0 means no age out.
                
                Please be aware that contention between multiple managers
                trying to set this object to different values MAY affect the
                reliability and completeness of data seen by each manager.
                ''',
                'nlmconfigglobalageout',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigGlobalEntryLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of notification entries that may be held
                in nlmLogTable for all nlmLogNames added together.  A particular
                setting does not guarantee that much data can be held.
                
                If an application changes the limit while there are
                Notifications in the log, the oldest Notifications MUST be
                discarded to bring the log down to the new limit - thus the
                value of nlmConfigGlobalEntryLimit MUST take precedence over
                the values of nlmConfigGlobalAgeOut and nlmConfigLogEntryLimit,
                even if the Notification being discarded has been present for
                fewer minutes than the value of nlmConfigGlobalAgeOut, or if
                the named log has fewer entries than that specified in
                nlmConfigLogEntryLimit.
                
                A value of 0 means no limit.
                
                Please be aware that contention between multiple managers
                trying to set this object to different values MAY affect the
                reliability and completeness of data seen by each manager.
                ''',
                'nlmconfigglobalentrylimit',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmConfig',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmstats' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmstats',
            False, 
            [
            _MetaInfoClassMember('nlmStatsGlobalNotificationsBumped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of log entries discarded to make room for a new entry
                due to lack of resources or the value of nlmConfigGlobalEntryLimit
                or nlmConfigLogEntryLimit.  This does not include entries discarded
                due to the value of nlmConfigGlobalAgeOut.
                ''',
                'nlmstatsglobalnotificationsbumped',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmStatsGlobalNotificationsLogged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Notifications put into the nlmLogTable.  This
                counts a Notification once for each log entry, so a Notification
                 put into multiple logs is counted multiple times.
                ''',
                'nlmstatsglobalnotificationslogged',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmStats',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogadminstatusEnum' : _MetaInfoEnum('NlmconfiglogadminstatusEnum', 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'NOTIFICATION-LOG-MIB', _yang_ns._namespaces['NOTIFICATION-LOG-MIB']),
    'NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogoperstatusEnum' : _MetaInfoEnum('NlmconfiglogoperstatusEnum', 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB',
        {
            'disabled':'disabled',
            'operational':'operational',
            'noFilter':'noFilter',
        }, 'NOTIFICATION-LOG-MIB', _yang_ns._namespaces['NOTIFICATION-LOG-MIB']),
    'NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry',
            False, 
            [
            _MetaInfoClassMember('nlmLogName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The name of the log.
                
                An implementation may allow multiple named logs, up to some
                implementation-specific limit (which may be none).  A
                zero-length log name is reserved for creation and deletion by
                the managed system, and MUST be used as the default log name by
                systems that do not support named logs.
                ''',
                'nlmlogname',
                'NOTIFICATION-LOG-MIB', True),
            _MetaInfoClassMember('nlmConfigLogAdminStatus', REFERENCE_ENUM_CLASS, 'NlmconfiglogadminstatusEnum' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogadminstatusEnum', 
                [], [], 
                '''                Control to enable or disable the log without otherwise
                disturbing the log's entry.
                
                Please be aware that contention between multiple managers
                trying to set this object to different values MAY affect the
                reliability and completeness of data seen by each manager.
                ''',
                'nlmconfiglogadminstatus',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigLogEntryLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of notification entries that can be held in
                nlmLogTable for this named log.  A particular setting does not
                guarantee that that much data can be held.
                
                If an application changes the limit while there are
                Notifications in the log, the oldest Notifications are discarded
                to bring the log down to the new limit.
                
                A value of 0 indicates no limit.
                
                Please be aware that contention between multiple managers
                trying to set this object to different values MAY affect the
                reliability and completeness of data seen by each manager.
                ''',
                'nlmconfiglogentrylimit',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigLogEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                Control for creating and deleting entries.  Entries may be
                modified while active.
                
                For non-null-named logs, the managed system records the security
                credentials from the request that sets nlmConfigLogStatus
                to 'active' and uses that identity to apply access control to
                the objects in the Notification to decide if that Notification
                may be logged.
                ''',
                'nlmconfiglogentrystatus',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigLogFilterName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                A value of snmpNotifyFilterProfileName as used as an index
                into the snmpNotifyFilterTable in the SNMP Notification MIB,
                specifying the locally or remotely originated Notifications
                to be filtered out and not logged in this log.
                
                A zero-length value or a name that does not identify an
                existing entry in snmpNotifyFilterTable indicate no
                Notifications are to be logged in this log.
                ''',
                'nlmconfiglogfiltername',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigLogOperStatus', REFERENCE_ENUM_CLASS, 'NlmconfiglogoperstatusEnum' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry.NlmconfiglogoperstatusEnum', 
                [], [], 
                '''                The operational status of this log:
                
                disabled  administratively disabled
                
                operational    administratively enabled and working
                
                noFilter  administratively enabled but either
                          nlmConfigLogFilterName is zero length
                          or does not name an existing entry in
                          snmpNotifyFilterTable
                ''',
                'nlmconfiglogoperstatus',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigLogStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type of this conceptual row.
                ''',
                'nlmconfiglogstoragetype',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmStatsLogNotificationsBumped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of log entries discarded from this named log to make
                room for a new entry due to lack of resources or the value of
                nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not
                include entries discarded due to the value of
                nlmConfigGlobalAgeOut.
                ''',
                'nlmstatslognotificationsbumped',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmStatsLogNotificationsLogged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Notifications put in this named log.
                ''',
                'nlmstatslognotificationslogged',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmConfigLogEntry',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmconfiglogtable' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmconfiglogtable',
            False, 
            [
            _MetaInfoClassMember('nlmConfigLogEntry', REFERENCE_LIST, 'Nlmconfiglogentry' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry', 
                [], [], 
                '''                A logging control entry.  Depending on the entry's storage type
                entries may be supplied by the system or created and deleted by
                applications using nlmConfigLogEntryStatus.
                ''',
                'nlmconfiglogentry',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmConfigLogTable',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmlogtable.Nlmlogentry' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmlogtable.Nlmlogentry',
            False, 
            [
            _MetaInfoClassMember('nlmLogName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'nlmlogname',
                'NOTIFICATION-LOG-MIB', True),
            _MetaInfoClassMember('nlmLogIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A monotonically increasing integer for the sole purpose of
                indexing entries within the named log.  When it reaches the
                maximum value, an extremely unlikely event, the agent wraps the
                value back to 1.
                ''',
                'nlmlogindex',
                'NOTIFICATION-LOG-MIB', True),
            _MetaInfoClassMember('nlmLogContextEngineID', ATTRIBUTE, 'str' , None, None, 
                [(5, 32)], [], 
                '''                If the Notification was received in a protocol which has a
                contextEngineID element like SNMPv3, this object has that value.
                Otherwise its value is a zero-length string.
                ''',
                'nlmlogcontextengineid',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogContextName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the SNMP MIB context from which the Notification came.
                For SNMPv1 Traps this is the community string from the Trap.
                ''',
                'nlmlogcontextname',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogDateAndTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The local date and time when the entry was logged, instantiated
                only by systems that have date and time capability.
                ''',
                'nlmlogdateandtime',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogEngineID', ATTRIBUTE, 'str' , None, None, 
                [(5, 32)], [], 
                '''                The identification of the SNMP engine at which the Notification
                originated.
                
                If the log can contain Notifications from only one engine
                or the Trap is in SNMPv1 format, this object is a zero-length
                string.
                ''',
                'nlmlogengineid',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogEngineTAddress', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The transport service address of the SNMP engine from which the
                Notification was received, formatted according to the corresponding
                value of nlmLogEngineTDomain. This is used to identify the source
                of an SNMPv1 trap, since an nlmLogEngineId cannot be extracted
                from the SNMPv1 trap pdu.
                
                This object MUST always be instantiated, even if the log
                can contain Notifications from only one engine.
                
                Please be aware that the nlmLogEngineTAddress may not uniquely
                identify the SNMP engine from which the Notification was received.
                For example, if an SNMP engine uses DHCP or NAT to obtain
                ip addresses, the address it uses may be shared with other
                network devices, and hence will not uniquely identify the
                SNMP engine.
                ''',
                'nlmlogenginetaddress',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogEngineTDomain', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Indicates the kind of transport service by which a Notification
                was received from an SNMP engine. nlmLogEngineTAddress contains
                the transport service address of the SNMP engine from which
                this Notification was received.
                
                Possible values for this object are presently found in the
                Transport Mappings for SNMPv2 document (RFC 1906 [8]).
                ''',
                'nlmlogenginetdomain',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogNotificationID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The NOTIFICATION-TYPE object identifier of the Notification that
                occurred.
                ''',
                'nlmlognotificationid',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the entry was placed in the log. If
                the entry occurred before the most recent management system
                initialization this object value MUST be set to zero.
                ''',
                'nlmlogtime',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmLogEntry',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmlogtable' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmlogtable',
            False, 
            [
            _MetaInfoClassMember('nlmLogEntry', REFERENCE_LIST, 'Nlmlogentry' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmlogtable.Nlmlogentry', 
                [], [], 
                '''                A Notification log entry.
                
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
                
                Before the managed system puts a locally-generated Notification
                into a non-null-named log it assures that the creator of the log
                has access to the information in the Notification.  If not it
                does not log that Notification in that log.
                ''',
                'nlmlogentry',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmLogTable',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry.NlmlogvariablevaluetypeEnum' : _MetaInfoEnum('NlmlogvariablevaluetypeEnum', 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB',
        {
            'counter32':'counter32',
            'unsigned32':'unsigned32',
            'timeTicks':'timeTicks',
            'integer32':'integer32',
            'ipAddress':'ipAddress',
            'octetString':'octetString',
            'objectId':'objectId',
            'counter64':'counter64',
            'opaque':'opaque',
        }, 'NOTIFICATION-LOG-MIB', _yang_ns._namespaces['NOTIFICATION-LOG-MIB']),
    'NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry',
            False, 
            [
            _MetaInfoClassMember('nlmLogName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'nlmlogname',
                'NOTIFICATION-LOG-MIB', True),
            _MetaInfoClassMember('nlmLogIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nlmlogindex',
                'NOTIFICATION-LOG-MIB', True),
            _MetaInfoClassMember('nlmLogVariableIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A monotonically increasing integer, starting at 1 for a given
                nlmLogIndex, for indexing variables within the logged
                Notification.
                ''',
                'nlmlogvariableindex',
                'NOTIFICATION-LOG-MIB', True),
            _MetaInfoClassMember('nlmLogVariableCounter32Val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value when nlmLogVariableType is 'counter32'.
                ''',
                'nlmlogvariablecounter32val',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableCounter64Val', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The value when nlmLogVariableType is 'counter64'.
                ''',
                'nlmlogvariablecounter64val',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The variable's object identifier.
                ''',
                'nlmlogvariableid',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableInteger32Val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value when nlmLogVariableType is 'integer32'.
                ''',
                'nlmlogvariableinteger32val',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableIpAddressVal', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The value when nlmLogVariableType is 'ipAddress'.
                Although this seems to be unfriendly for IPv6, we
                have to recognize that there are a number of older
                MIBs that do contain an IPv4 format address, known
                as IpAddress.
                
                IPv6 addresses are represented using TAddress or
                InetAddress, and so the underlying datatype is
                OCTET STRING, and their value would be stored in
                the nlmLogVariableOctetStringVal column.
                ''',
                'nlmlogvariableipaddressval',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableOctetStringVal', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value when nlmLogVariableType is 'octetString'.
                ''',
                'nlmlogvariableoctetstringval',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableOidVal', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The value when nlmLogVariableType is 'objectId'.
                ''',
                'nlmlogvariableoidval',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableOpaqueVal', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value when nlmLogVariableType is 'opaque'.
                ''',
                'nlmlogvariableopaqueval',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableTimeTicksVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value when nlmLogVariableType is 'timeTicks'.
                ''',
                'nlmlogvariabletimeticksval',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableUnsigned32Val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value when nlmLogVariableType is 'unsigned32'.
                ''',
                'nlmlogvariableunsigned32val',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableValueType', REFERENCE_ENUM_CLASS, 'NlmlogvariablevaluetypeEnum' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry.NlmlogvariablevaluetypeEnum', 
                [], [], 
                '''                The type of the value.  One and only one of the value
                objects that follow must be instantiated, based on this type.
                ''',
                'nlmlogvariablevaluetype',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmLogVariableEntry',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib.Nlmlogvariabletable' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib.Nlmlogvariabletable',
            False, 
            [
            _MetaInfoClassMember('nlmLogVariableEntry', REFERENCE_LIST, 'Nlmlogvariableentry' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry', 
                [], [], 
                '''                A Notification log entry variable.
                
                Entries appear in this table when there are variables in
                the varbind list of a Notification in nlmLogTable.
                ''',
                'nlmlogvariableentry',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'nlmLogVariableTable',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
    'NotificationLogMib' : {
        'meta_info' : _MetaInfoClass('NotificationLogMib',
            False, 
            [
            _MetaInfoClassMember('nlmConfig', REFERENCE_CLASS, 'Nlmconfig' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmconfig', 
                [], [], 
                '''                ''',
                'nlmconfig',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmConfigLogTable', REFERENCE_CLASS, 'Nlmconfiglogtable' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmconfiglogtable', 
                [], [], 
                '''                A table of logging control entries.
                ''',
                'nlmconfiglogtable',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogTable', REFERENCE_CLASS, 'Nlmlogtable' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmlogtable', 
                [], [], 
                '''                A table of Notification log entries.
                
                It is an implementation-specific matter whether entries in this
                table are preserved across initializations of the management
                system.  In general one would expect that they are not.
                
                Note that keeping entries across initializations of the
                management system leads to some confusion with counters and
                TimeStamps, since both of those are based on sysUpTime, which
                resets on management initialization.  In this situation,
                counters apply only after the reset and nlmLogTime for entries
                made before the reset MUST be set to 0.
                ''',
                'nlmlogtable',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmLogVariableTable', REFERENCE_CLASS, 'Nlmlogvariabletable' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmlogvariabletable', 
                [], [], 
                '''                A table of variables to go with Notification log entries.
                ''',
                'nlmlogvariabletable',
                'NOTIFICATION-LOG-MIB', False),
            _MetaInfoClassMember('nlmStats', REFERENCE_CLASS, 'Nlmstats' , 'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB', 'NotificationLogMib.Nlmstats', 
                [], [], 
                '''                ''',
                'nlmstats',
                'NOTIFICATION-LOG-MIB', False),
            ],
            'NOTIFICATION-LOG-MIB',
            'NOTIFICATION-LOG-MIB',
            _yang_ns._namespaces['NOTIFICATION-LOG-MIB'],
        'ydk.models.cisco_ios_xe.NOTIFICATION_LOG_MIB'
        ),
    },
}
_meta_table['NotificationLogMib.Nlmconfiglogtable.Nlmconfiglogentry']['meta_info'].parent =_meta_table['NotificationLogMib.Nlmconfiglogtable']['meta_info']
_meta_table['NotificationLogMib.Nlmlogtable.Nlmlogentry']['meta_info'].parent =_meta_table['NotificationLogMib.Nlmlogtable']['meta_info']
_meta_table['NotificationLogMib.Nlmlogvariabletable.Nlmlogvariableentry']['meta_info'].parent =_meta_table['NotificationLogMib.Nlmlogvariabletable']['meta_info']
_meta_table['NotificationLogMib.Nlmconfig']['meta_info'].parent =_meta_table['NotificationLogMib']['meta_info']
_meta_table['NotificationLogMib.Nlmstats']['meta_info'].parent =_meta_table['NotificationLogMib']['meta_info']
_meta_table['NotificationLogMib.Nlmconfiglogtable']['meta_info'].parent =_meta_table['NotificationLogMib']['meta_info']
_meta_table['NotificationLogMib.Nlmlogtable']['meta_info'].parent =_meta_table['NotificationLogMib']['meta_info']
_meta_table['NotificationLogMib.Nlmlogvariabletable']['meta_info'].parent =_meta_table['NotificationLogMib']['meta_info']
