


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NotifysourceEnum' : _MetaInfoEnum('NotifysourceEnum', 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB',
        {
            'server':'server',
            'policy':'policy',
        }, 'CISCO-EMBEDDED-EVENT-MGR-MIB', _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB']),
    'CiscoEmbeddedEventMgrMib.Ceemhistory' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemhistory',
            False, 
            [
            _MetaInfoClassMember('ceemHistoryLastEventEntry', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Index of last entry created in ceemHistoryEventTable.
                ''',
                'ceemhistorylastevententry',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryMaxEventEntries', ATTRIBUTE, 'int' , None, None, 
                [('0', '50')], [], 
                '''                The maximum number of entries that can be held in
                ceemHistoryEventTable.
                ''',
                'ceemhistorymaxevententries',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemHistory',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib.Ceemeventmaptable.Ceemeventmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemeventmaptable.Ceemeventmapentry',
            False, 
            [
            _MetaInfoClassMember('ceemEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object uniquely identifies an event.  Events
                are not persisted across reloads.
                ''',
                'ceemeventindex',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', True),
            _MetaInfoClassMember('ceemEventDescrText', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies a human-readable
                message describing information about the 
                Embedded Event Manager event.
                ''',
                'ceemeventdescrtext',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemEventName', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                The name of the Embedded Event Manager event.
                ''',
                'ceemeventname',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemEventMapEntry',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib.Ceemeventmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemeventmaptable',
            False, 
            [
            _MetaInfoClassMember('ceemEventMapEntry', REFERENCE_LIST, 'Ceemeventmapentry' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemeventmaptable.Ceemeventmapentry', 
                [], [], 
                '''                A mapping between an event type and an event description.
                ''',
                'ceemeventmapentry',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemEventMapTable',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable.Ceemhistoryevententry' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable.Ceemhistoryevententry',
            False, 
            [
            _MetaInfoClassMember('ceemHistoryEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A monotonically increasing non-zero integer uniquely
                identifying a generated event.  When it reaches the 
                maximum value, the agent wraps the value back to 1 
                and may flush all existing entries in the event table.
                ''',
                'ceemhistoryeventindex',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', True),
            _MetaInfoClassMember('ceemHistoryEventType1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype1',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype2',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType3', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype3',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the
                ceemEventTable.
                ''',
                'ceemhistoryeventtype4',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType5', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype5',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype6',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType7', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype7',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType8', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype8',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryNotifyType', REFERENCE_ENUM_CLASS, 'NotifysourceEnum' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'NotifysourceEnum', 
                [], [], 
                '''                The notification type that was sent from the Embedded Event
                Manager.  The valid values are server or policy.
                ''',
                'ceemhistorynotifytype',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyExitStatus', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The exit status of the Embedded Event Manager policy
                execution.  This value corresponds to the Posix process 
                exit status.
                ''',
                'ceemhistorypolicyexitstatus',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyIntData1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Arbitrary integer data that the Embedded Event Manager policy
                can use. Use of this object is optional. If unused by
                a policy, this object will not be instantiated for 
                that policy.
                ''',
                'ceemhistorypolicyintdata1',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyIntData2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Arbitrary integer data that the Embedded Event Manager policy
                can use. Use of this object is optional. If unused by
                a policy, this object will not be instantiated for 
                that policy.
                ''',
                'ceemhistorypolicyintdata2',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyName', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The name of the Embedded Event Manager policy that was
                triggered because of an Embedded Event Manager event. The
                name must be a valid Embedded Event Manager policy name. 
                It must be in the form of a valid Posix filename.
                ''',
                'ceemhistorypolicyname',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyPath', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The file path on the router where the Embedded Event Manager
                policy that was triggered is stored.  If the size of the 
                file path string is larger than 128, the end characters 
                will be truncated.
                ''',
                'ceemhistorypolicypath',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyStrData', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Arbitrary string data the Embedded Event Manager policy can
                use.  Use of this object is optional.  If unused by
                a policy, this object will not be instantiated for 
                that policy.
                ''',
                'ceemhistorypolicystrdata',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemHistoryEventEntry',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable',
            False, 
            [
            _MetaInfoClassMember('ceemHistoryEventEntry', REFERENCE_LIST, 'Ceemhistoryevententry' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable.Ceemhistoryevententry', 
                [], [], 
                '''                Information about an Embedded Event Manager event which has
                been generated by this router.  It provides up to four event
                types to support complex event specifications that are
                triggered when multiple events are published within a certain
                period of time.
                ''',
                'ceemhistoryevententry',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemHistoryEventTable',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry.CeemregisteredpolicystatusEnum' : _MetaInfoEnum('CeemregisteredpolicystatusEnum', 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-EMBEDDED-EVENT-MGR-MIB', _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB']),
    'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry.CeemregisteredpolicytypeEnum' : _MetaInfoEnum('CeemregisteredpolicytypeEnum', 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB',
        {
            'user':'user',
            'system':'system',
        }, 'CISCO-EMBEDDED-EVENT-MGR-MIB', _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB']),
    'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry',
            False, 
            [
            _MetaInfoClassMember('ceemRegisteredPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A monotonically increasing non-zero integer uniquely
                identifying a policy registration.  When it reaches the
                maximum value, the agent wraps the value back to 1 upon 
                receiving the next policy registration.
                ''',
                'ceemregisteredpolicyindex',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', True),
            _MetaInfoClassMember('ceemRegisteredPolicyEnabledTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The time the policy was last enabled.  It is stored as a
                32-bit count of seconds since 0000 UTC, 1 January, 1970.
                ''',
                'ceemregisteredpolicyenabledtime',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype1',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype2',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType3', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype3',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype4',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType5', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype5',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype6',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType7', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype7',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType8', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype8',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyName', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The name of the Embedded Event Manager policy that was
                registered.  The name must be a valid Embedded Event 
                Manager policy name. It must be in the form of a valid 
                Posix filename.
                ''',
                'ceemregisteredpolicyname',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyNotifFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This flag indicates if an SNMP notification will be sent when
                policy is triggered.
                ''',
                'ceemregisteredpolicynotifflag',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyRegTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The time the policy was registered.  It is stored as a
                32-bit count of seconds since 0000 UTC, 1 January, 1970.
                ''',
                'ceemregisteredpolicyregtime',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyRunCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the policy has been run.
                ''',
                'ceemregisteredpolicyruncount',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyRunTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The last time the policy was run.  It is stored as a
                32-bit count of seconds since 0000 UTC, 1 January, 1970.
                ''',
                'ceemregisteredpolicyruntime',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyStatus', REFERENCE_ENUM_CLASS, 'CeemregisteredpolicystatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry.CeemregisteredpolicystatusEnum', 
                [], [], 
                '''                This status indicates whether the policy is enabled or disabled.
                ''',
                'ceemregisteredpolicystatus',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyType', REFERENCE_ENUM_CLASS, 'CeemregisteredpolicytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry.CeemregisteredpolicytypeEnum', 
                [], [], 
                '''                This variable indicates whether this is a user or system policy.
                ''',
                'ceemregisteredpolicytype',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemRegisteredPolicyEntry',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable',
            False, 
            [
            _MetaInfoClassMember('ceemRegisteredPolicyEntry', REFERENCE_LIST, 'Ceemregisteredpolicyentry' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry', 
                [], [], 
                '''                An entry in the table of Embedded Event Manager policies that are
                registered.  It provides up to four event types to support complex 
                event specifications that are triggered when multiple events are 
                published within a certain period of time.  A row in this table 
                cannot be created or deleted by SNMP operations on columns of the 
                table.
                ''',
                'ceemregisteredpolicyentry',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemRegisteredPolicyTable',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CiscoEmbeddedEventMgrMib' : {
        'meta_info' : _MetaInfoClass('CiscoEmbeddedEventMgrMib',
            False, 
            [
            _MetaInfoClassMember('ceemEventMapTable', REFERENCE_CLASS, 'Ceemeventmaptable' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemeventmaptable', 
                [], [], 
                '''                A table containing information about ceemEventIndex
                value mapping.  Each conceptual row specifies a 
                unique mapping between a ceemEventIndex value, and a 
                Embedded Event Manager event type.  Rows are added 
                dynamically as the Embedded Event Manager server learns
                of new event types.  This occurs when Embedded Event 
                Manager Event Detectors register with the Embedded 
                Event Manager server.
                ''',
                'ceemeventmaptable',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistory', REFERENCE_CLASS, 'Ceemhistory' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemhistory', 
                [], [], 
                '''                ''',
                'ceemhistory',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventTable', REFERENCE_CLASS, 'Ceemhistoryeventtable' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable', 
                [], [], 
                '''                A table of Embedded Event Manager events generated by this
                router.  Conceptual row entries are dynamically added into 
                this table when Embedded Event Manager events occur.
                
                Entries are stored in FIFO order.  When the maximum number 
                of entries has been reached in the table, the oldest entry 
                in the table is removed immediately.  
                
                When a table is reduced to a smaller size N, the oldest
                entries are immediately removed from the table leaving 
                a maximum of N entries.
                ''',
                'ceemhistoryeventtable',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyTable', REFERENCE_CLASS, 'Ceemregisteredpolicytable' , 'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable', 
                [], [], 
                '''                A table of Embedded Event Manager policies registered on a system.
                The number of entries depends on the configuration of the system.  The 
                maximum number is implementation dependent.
                ''',
                'ceemregisteredpolicytable',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
}
_meta_table['CiscoEmbeddedEventMgrMib.Ceemeventmaptable.Ceemeventmapentry']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib.Ceemeventmaptable']['meta_info']
_meta_table['CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable.Ceemhistoryevententry']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable']['meta_info']
_meta_table['CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable.Ceemregisteredpolicyentry']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable']['meta_info']
_meta_table['CiscoEmbeddedEventMgrMib.Ceemhistory']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib']['meta_info']
_meta_table['CiscoEmbeddedEventMgrMib.Ceemeventmaptable']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib']['meta_info']
_meta_table['CiscoEmbeddedEventMgrMib.Ceemhistoryeventtable']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib']['meta_info']
_meta_table['CiscoEmbeddedEventMgrMib.Ceemregisteredpolicytable']['meta_info'].parent =_meta_table['CiscoEmbeddedEventMgrMib']['meta_info']
