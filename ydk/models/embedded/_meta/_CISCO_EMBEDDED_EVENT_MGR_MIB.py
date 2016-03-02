


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'NotifySource_Enum' : _MetaInfoEnum('NotifySource_Enum', 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB',
        {
            'server':'SERVER',
            'policy':'POLICY',
        }, 'CISCO-EMBEDDED-EVENT-MGR-MIB', _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB']),
    'CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable.CeemEventMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable.CeemEventMapEntry',
            False, 
            [
            _MetaInfoClassMember('ceemEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object uniquely identifies an event.  Events
                are not persisted across reloads.
                ''',
                'ceemeventindex',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', True),
            _MetaInfoClassMember('ceemEventDescrText', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
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
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable',
            False, 
            [
            _MetaInfoClassMember('ceemEventMapEntry', REFERENCE_LIST, 'CeemEventMapEntry' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable.CeemEventMapEntry', 
                [], [], 
                '''                A mapping between an event type and an event description.
                ''',
                'ceemeventmapentry',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemEventMapTable',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB.CeemHistory' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemHistory',
            False, 
            [
            _MetaInfoClassMember('ceemHistoryLastEventEntry', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Index of last entry created in ceemHistoryEventTable.
                ''',
                'ceemhistorylastevententry',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryMaxEventEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 50)], [], 
                '''                The maximum number of entries that can be held in
                ceemHistoryEventTable.
                ''',
                'ceemhistorymaxevententries',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemHistory',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable.CeemHistoryEventEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable.CeemHistoryEventEntry',
            False, 
            [
            _MetaInfoClassMember('ceemHistoryEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                A monotonically increasing non-zero integer uniquely
                identifying a generated event.  When it reaches the 
                maximum value, the agent wraps the value back to 1 
                and may flush all existing entries in the event table.
                ''',
                'ceemhistoryeventindex',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', True),
            _MetaInfoClassMember('ceemHistoryEventType1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype1',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType2', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype2',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType3', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype3',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType4', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the
                ceemEventTable.
                ''',
                'ceemhistoryeventtype4',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype5',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType6', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype6',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType7', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype7',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventType8', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was
                detected. The value corresponds to an entry in the 
                ceemEventTable.
                ''',
                'ceemhistoryeventtype8',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryNotifyType', REFERENCE_ENUM_CLASS, 'NotifySource_Enum' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'NotifySource_Enum', 
                [], [], 
                '''                The notification type that was sent from the Embedded Event
                Manager.  The valid values are server or policy.
                ''',
                'ceemhistorynotifytype',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyExitStatus', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The exit status of the Embedded Event Manager policy
                execution.  This value corresponds to the Posix process 
                exit status.
                ''',
                'ceemhistorypolicyexitstatus',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyIntData1', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Arbitrary integer data that the Embedded Event Manager policy
                can use. Use of this object is optional. If unused by
                a policy, this object will not be instantiated for 
                that policy.
                ''',
                'ceemhistorypolicyintdata1',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryPolicyIntData2', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable',
            False, 
            [
            _MetaInfoClassMember('ceemHistoryEventEntry', REFERENCE_LIST, 'CeemHistoryEventEntry' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable.CeemHistoryEventEntry', 
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
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry.CeemRegisteredPolicyStatus_Enum' : _MetaInfoEnum('CeemRegisteredPolicyStatus_Enum', 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-EMBEDDED-EVENT-MGR-MIB', _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB']),
    'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry.CeemRegisteredPolicyType_Enum' : _MetaInfoEnum('CeemRegisteredPolicyType_Enum', 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB',
        {
            'user':'USER',
            'system':'SYSTEM',
        }, 'CISCO-EMBEDDED-EVENT-MGR-MIB', _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB']),
    'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry',
            False, 
            [
            _MetaInfoClassMember('ceemRegisteredPolicyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype1',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType2', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype2',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType3', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype3',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType4', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype4',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype5',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType6', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype6',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType7', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The type of Embedded Event Manager event which was registered
                by the policy. The value corresponds to an entry in the
                ceemEventMapTable.
                ''',
                'ceemregisteredpolicyeventtype7',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyEventType8', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('ceemRegisteredPolicyStatus', REFERENCE_ENUM_CLASS, 'CeemRegisteredPolicyStatus_Enum' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry.CeemRegisteredPolicyStatus_Enum', 
                [], [], 
                '''                This status indicates whether the policy is enabled or disabled.
                ''',
                'ceemregisteredpolicystatus',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemRegisteredPolicyType', REFERENCE_ENUM_CLASS, 'CeemRegisteredPolicyType_Enum' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry.CeemRegisteredPolicyType_Enum', 
                [], [], 
                '''                This variable indicates whether this is a user or system policy.
                ''',
                'ceemregisteredpolicytype',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            ],
            'CISCO-EMBEDDED-EVENT-MGR-MIB',
            'ceemRegisteredPolicyEntry',
            _yang_ns._namespaces['CISCO-EMBEDDED-EVENT-MGR-MIB'],
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable',
            False, 
            [
            _MetaInfoClassMember('ceemRegisteredPolicyEntry', REFERENCE_LIST, 'CeemRegisteredPolicyEntry' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry', 
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
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
    'CISCOEMBEDDEDEVENTMGRMIB' : {
        'meta_info' : _MetaInfoClass('CISCOEMBEDDEDEVENTMGRMIB',
            False, 
            [
            _MetaInfoClassMember('ceemEventMapTable', REFERENCE_CLASS, 'CeemEventMapTable' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable', 
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
            _MetaInfoClassMember('ceemHistory', REFERENCE_CLASS, 'CeemHistory' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemHistory', 
                [], [], 
                '''                ''',
                'ceemhistory',
                'CISCO-EMBEDDED-EVENT-MGR-MIB', False),
            _MetaInfoClassMember('ceemHistoryEventTable', REFERENCE_CLASS, 'CeemHistoryEventTable' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable', 
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
            _MetaInfoClassMember('ceemRegisteredPolicyTable', REFERENCE_CLASS, 'CeemRegisteredPolicyTable' , 'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB', 'CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable', 
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
        'ydk.models.embedded.CISCO_EMBEDDED_EVENT_MGR_MIB'
        ),
    },
}
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable.CeemEventMapEntry']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable']['meta_info']
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable.CeemHistoryEventEntry']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable']['meta_info']
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable.CeemRegisteredPolicyEntry']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable']['meta_info']
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemEventMapTable']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB']['meta_info']
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemHistory']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB']['meta_info']
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemHistoryEventTable']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB']['meta_info']
_meta_table['CISCOEMBEDDEDEVENTMGRMIB.CeemRegisteredPolicyTable']['meta_info'].parent =_meta_table['CISCOEMBEDDEDEVENTMGRMIB']['meta_info']
