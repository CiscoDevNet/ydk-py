


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoAaaSessionMib.Casnactive' : {
        'meta_info' : _MetaInfoClass('CiscoAaaSessionMib.Casnactive',
            False, 
            [
            _MetaInfoClassMember('casnActiveTableEntries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of entries currently in casnActiveTable
                ''',
                'casnactivetableentries',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnActiveTableHighWaterMark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of entries present in casnActiveTable
                since last system re-initialization.
                
                This corresponds to the maximum value reported by
                casnActiveTableEntries.
                ''',
                'casnactivetablehighwatermark',
                'CISCO-AAA-SESSION-MIB', False),
            ],
            'CISCO-AAA-SESSION-MIB',
            'casnActive',
            _yang_ns._namespaces['CISCO-AAA-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB'
        ),
    },
    'CiscoAaaSessionMib.Casngeneral' : {
        'meta_info' : _MetaInfoClass('CiscoAaaSessionMib.Casngeneral',
            False, 
            [
            _MetaInfoClassMember('casnDisconnectedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of sessions which have been disconnected using
                casnDisconnect since last system re-initialization.
                
                This value includes any sessions still in the
                casnActiveTable with a casnDisconnect value of true(1) and
                all previous sessions which terminated as a result of
                setting casnDisconnect.
                ''',
                'casndisconnectedsessions',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnTotalSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of sessions since last system
                re-initialization.
                
                This value includes all sessions currently in the
                casnActiveTable and all previous sessions whether
                terminated via casnDisconnect or via other
                mechanisms.
                ''',
                'casntotalsessions',
                'CISCO-AAA-SESSION-MIB', False),
            ],
            'CISCO-AAA-SESSION-MIB',
            'casnGeneral',
            _yang_ns._namespaces['CISCO-AAA-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB'
        ),
    },
    'CiscoAaaSessionMib.Casnactivetable.Casnactiveentry' : {
        'meta_info' : _MetaInfoClass('CiscoAaaSessionMib.Casnactivetable.Casnactiveentry',
            False, 
            [
            _MetaInfoClassMember('casnSessionId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This is the session identification used by the
                accounting protocol.
                
                This value is unique to a session within the system,
                even if multiple accounting protocols are in use.
                
                The value of this object corresponds to these
                accounting protocol attributes.
                   RADIUS:  attribute 44, Acct-Session-Id
                   TACACS+: attribute 'task_id'
                ''',
                'casnsessionid',
                'CISCO-AAA-SESSION-MIB', True),
            _MetaInfoClassMember('casnCallTrackerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object is the entry index in the
                CISCO-CALL-TRACKER-MIB cctActiveTable of the call
                corresponding to this accounting session.
                
                Using the value of this object to query the
                cctActiveTable will provide more detailed data regarding
                the session represented by this casnActiveEntry.
                ''',
                'casncalltrackerid',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnDisconnect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is used to terminate this session.
                
                Setting the value to true(1) will initiate termination
                of this session.
                
                The entry will be removed once the session has completed
                termination.
                
                Once this object has been set to true(1), the session
                termination process can not be cancelled by setting the
                value false(2).
                ''',
                'casndisconnect',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnIdleTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The elapsed time that this session has been idle.
                
                This is the time since the last user-level data has been
                received or transmitted. Protocol level handshaking
                associated with the call is considered to be idle for
                this object.
                ''',
                'casnidletime',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnIpAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the session or 0.0.0.0 if not
                applicable or unavailable.
                
                RADIUS:  attribute 8, Framed-IP-Address
                TACACS+: attribute 'addr'
                ''',
                'casnipaddr',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnNasPort', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The value of this object identifies a particular
                conceptual row associated with the session identified by
                casnSessionId.  The conceptual row that this object points
                to represents a port that is used to transport a session.
                
                If the port transporting the session cannot be determined,
                the value of this object will be zeroDotZero.
                
                For example, suppose a session is established using an ATM
                PVC.  If the ifIndex of the ATM interface is 7, and the 
                VPI/VCI values of the PVC are 1, 100 respectively, then
                the value of this object might be as follows:
                
                       casnNasPort.15 = atmVclAdminStatus.7.1.100
                                   ^                      ^ ^  ^
                                   |                      | |  |
                   casnSessionId --+                      | |  |
                         ifIndex -------------------------+ |  |
                       atmVclVpi ---------------------------+  |
                       atmVclVci ------------------------------+
                
                where atmVclAdminStatus is the first accessible object
                of the atmVclTable of the ATM-MIB.
                ''',
                'casnnasport',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnUserId', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The User login ID or zero length string if unavailable.
                
                The value of this object corresponds to these
                accounting protocol attributes.
                   RADIUS:  attribute 1, User-Name
                   TACACS+: attribute 'user'
                ''',
                'casnuserid',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnVaiIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The ifIndex of the Virtual Access Interface (VAI)
                that is associated with the PPP session.
                
                This interface may not be represented in the IF-MIB in
                which case the value of this object will be zero.
                ''',
                'casnvaiifindex',
                'CISCO-AAA-SESSION-MIB', False),
            ],
            'CISCO-AAA-SESSION-MIB',
            'casnActiveEntry',
            _yang_ns._namespaces['CISCO-AAA-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB'
        ),
    },
    'CiscoAaaSessionMib.Casnactivetable' : {
        'meta_info' : _MetaInfoClass('CiscoAaaSessionMib.Casnactivetable',
            False, 
            [
            _MetaInfoClassMember('casnActiveEntry', REFERENCE_LIST, 'Casnactiveentry' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB', 'CiscoAaaSessionMib.Casnactivetable.Casnactiveentry', 
                [], [], 
                '''                The information regarding a single accounting session.
                
                Entries are created when a new accounting session
                is begun.
                
                Entries are removed when the accounting session
                is ended.
                
                Initiating termination of a session with the object
                casnDisconnect will cause removal of the entry when
                the session completes termination.
                ''',
                'casnactiveentry',
                'CISCO-AAA-SESSION-MIB', False),
            ],
            'CISCO-AAA-SESSION-MIB',
            'casnActiveTable',
            _yang_ns._namespaces['CISCO-AAA-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB'
        ),
    },
    'CiscoAaaSessionMib' : {
        'meta_info' : _MetaInfoClass('CiscoAaaSessionMib',
            False, 
            [
            _MetaInfoClassMember('casnActive', REFERENCE_CLASS, 'Casnactive' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB', 'CiscoAaaSessionMib.Casnactive', 
                [], [], 
                '''                ''',
                'casnactive',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnActiveTable', REFERENCE_CLASS, 'Casnactivetable' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB', 'CiscoAaaSessionMib.Casnactivetable', 
                [], [], 
                '''                This table contains entries for active AAA accounting
                sessions in the system.
                ''',
                'casnactivetable',
                'CISCO-AAA-SESSION-MIB', False),
            _MetaInfoClassMember('casnGeneral', REFERENCE_CLASS, 'Casngeneral' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB', 'CiscoAaaSessionMib.Casngeneral', 
                [], [], 
                '''                ''',
                'casngeneral',
                'CISCO-AAA-SESSION-MIB', False),
            ],
            'CISCO-AAA-SESSION-MIB',
            'CISCO-AAA-SESSION-MIB',
            _yang_ns._namespaces['CISCO-AAA-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB'
        ),
    },
}
_meta_table['CiscoAaaSessionMib.Casnactivetable.Casnactiveentry']['meta_info'].parent =_meta_table['CiscoAaaSessionMib.Casnactivetable']['meta_info']
_meta_table['CiscoAaaSessionMib.Casnactive']['meta_info'].parent =_meta_table['CiscoAaaSessionMib']['meta_info']
_meta_table['CiscoAaaSessionMib.Casngeneral']['meta_info'].parent =_meta_table['CiscoAaaSessionMib']['meta_info']
_meta_table['CiscoAaaSessionMib.Casnactivetable']['meta_info'].parent =_meta_table['CiscoAaaSessionMib']['meta_info']
