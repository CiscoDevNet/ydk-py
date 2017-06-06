


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SnmpTargetMib.Snmptargetobjects' : {
        'meta_info' : _MetaInfoClass('SnmpTargetMib.Snmptargetobjects',
            False, 
            [
            _MetaInfoClassMember('snmpTargetSpinLock', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object is used to facilitate modification of table
                entries in the SNMP-TARGET-MIB module by multiple
                
                
                
                
                
                managers.  In particular, it is useful when modifying
                the value of the snmpTargetAddrTagList object.
                
                The procedure for modifying the snmpTargetAddrTagList
                object is as follows:
                
                    1.  Retrieve the value of snmpTargetSpinLock and
                        of snmpTargetAddrTagList.
                
                    2.  Generate a new value for snmpTargetAddrTagList.
                
                    3.  Set the value of snmpTargetSpinLock to the
                        retrieved value, and the value of
                        snmpTargetAddrTagList to the new value.  If
                        the set fails for the snmpTargetSpinLock
                        object, go back to step 1.
                ''',
                'snmptargetspinlock',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpUnavailableContexts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received by the SNMP
                engine which were dropped because the context
                contained in the message was unavailable.
                ''',
                'snmpunavailablecontexts',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpUnknownContexts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received by the SNMP
                engine which were dropped because the context
                contained in the message was unknown.
                ''',
                'snmpunknowncontexts',
                'SNMP-TARGET-MIB', False),
            ],
            'SNMP-TARGET-MIB',
            'snmpTargetObjects',
            _yang_ns._namespaces['SNMP-TARGET-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB'
        ),
    },
    'SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry' : {
        'meta_info' : _MetaInfoClass('SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry',
            False, 
            [
            _MetaInfoClassMember('snmpTargetAddrName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this snmpTargetAddrEntry.
                ''',
                'snmptargetaddrname',
                'SNMP-TARGET-MIB', True),
            _MetaInfoClassMember('snmpTargetAddrParams', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The value of this object identifies an entry in the
                snmpTargetParamsTable.  The identified entry
                contains SNMP parameters to be used when generating
                messages to be sent to this transport address.
                ''',
                'snmptargetaddrparams',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrRetryCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies a default number of retries to be
                attempted when a response is not received for a generated
                message.  An application may provide its own retry count,
                in which case the value of this object is ignored.
                ''',
                'snmptargetaddrretrycount',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                To create a row in this table, a manager must
                set this object to either createAndGo(4) or
                createAndWait(5).
                
                Until instances of all corresponding columns are
                appropriately configured, the value of the
                corresponding instance of the snmpTargetAddrRowStatus
                column is 'notReady'.
                
                In particular, a newly created row cannot be made
                active until the corresponding instances of
                snmpTargetAddrTDomain, snmpTargetAddrTAddress, and
                snmpTargetAddrParams have all been set.
                
                The following objects may not be modified while the
                value of this object is active(1):
                    - snmpTargetAddrTDomain
                    - snmpTargetAddrTAddress
                An attempt to set these objects while the value of
                snmpTargetAddrRowStatus is active(1) will result in
                an inconsistentValue error.
                ''',
                'snmptargetaddrrowstatus',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.
                ''',
                'snmptargetaddrstoragetype',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrTAddress', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object contains a transport address.  The format of
                this address depends on the value of the
                snmpTargetAddrTDomain object.
                ''',
                'snmptargetaddrtaddress',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrTagList', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object contains a list of tag values which are
                used to select target addresses for a particular
                operation.
                ''',
                'snmptargetaddrtaglist',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrTDomain', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object indicates the transport type of the address
                contained in the snmpTargetAddrTAddress object.
                ''',
                'snmptargetaddrtdomain',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetAddrTimeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object should reflect the expected maximum round
                trip time for communicating with the transport address
                defined by this row.  When a message is sent to this
                address, and a response (if one is expected) is not
                received within this time period, an implementation
                may assume that the response will not be delivered.
                
                Note that the time interval that an application waits
                for a response may actually be derived from the value
                of this object.  The method for deriving the actual time
                interval is implementation dependent.  One such method
                
                
                
                
                
                is to derive the expected round trip time based on a
                particular retransmission algorithm and on the number
                of timeouts which have occurred.  The type of message may
                also be considered when deriving expected round trip
                times for retransmissions.  For example, if a message is
                being sent with a securityLevel that indicates both
                authentication and privacy, the derived value may be
                increased to compensate for extra processing time spent
                during authentication and encryption processing.
                ''',
                'snmptargetaddrtimeout',
                'SNMP-TARGET-MIB', False),
            ],
            'SNMP-TARGET-MIB',
            'snmpTargetAddrEntry',
            _yang_ns._namespaces['SNMP-TARGET-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB'
        ),
    },
    'SnmpTargetMib.Snmptargetaddrtable' : {
        'meta_info' : _MetaInfoClass('SnmpTargetMib.Snmptargetaddrtable',
            False, 
            [
            _MetaInfoClassMember('snmpTargetAddrEntry', REFERENCE_LIST, 'Snmptargetaddrentry' , 'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB', 'SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry', 
                [], [], 
                '''                A transport address to be used in the generation
                of SNMP operations.
                
                Entries in the snmpTargetAddrTable are created and
                deleted using the snmpTargetAddrRowStatus object.
                ''',
                'snmptargetaddrentry',
                'SNMP-TARGET-MIB', False),
            ],
            'SNMP-TARGET-MIB',
            'snmpTargetAddrTable',
            _yang_ns._namespaces['SNMP-TARGET-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB'
        ),
    },
    'SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry' : {
        'meta_info' : _MetaInfoClass('SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry',
            False, 
            [
            _MetaInfoClassMember('snmpTargetParamsName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this snmpTargetParamsEntry.
                ''',
                'snmptargetparamsname',
                'SNMP-TARGET-MIB', True),
            _MetaInfoClassMember('snmpTargetParamsMPModel', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The Message Processing Model to be used when generating
                SNMP messages using this entry.
                ''',
                'snmptargetparamsmpmodel',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetParamsRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                To create a row in this table, a manager must
                set this object to either createAndGo(4) or
                createAndWait(5).
                
                Until instances of all corresponding columns are
                appropriately configured, the value of the
                corresponding instance of the snmpTargetParamsRowStatus
                column is 'notReady'.
                
                In particular, a newly created row cannot be made
                
                
                
                
                
                active until the corresponding
                snmpTargetParamsMPModel,
                snmpTargetParamsSecurityModel,
                snmpTargetParamsSecurityName,
                and snmpTargetParamsSecurityLevel have all been set.
                The following objects may not be modified while the
                value of this object is active(1):
                    - snmpTargetParamsMPModel
                    - snmpTargetParamsSecurityModel
                    - snmpTargetParamsSecurityName
                    - snmpTargetParamsSecurityLevel
                An attempt to set these objects while the value of
                snmpTargetParamsRowStatus is active(1) will result in
                an inconsistentValue error.
                ''',
                'snmptargetparamsrowstatus',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetParamsSecurityLevel', REFERENCE_ENUM_CLASS, 'SnmpsecuritylevelEnum' , 'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB', 'SnmpsecuritylevelEnum', 
                [], [], 
                '''                The Level of Security to be used when generating
                SNMP messages using this entry.
                ''',
                'snmptargetparamssecuritylevel',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetParamsSecurityModel', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The Security Model to be used when generating SNMP
                messages using this entry.  An implementation may
                choose to return an inconsistentValue error if an
                attempt is made to set this variable to a value
                for a security model which the implementation does
                
                
                
                
                
                not support.
                ''',
                'snmptargetparamssecuritymodel',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetParamsSecurityName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The securityName which identifies the Principal on
                whose behalf SNMP messages will be generated using
                this entry.
                ''',
                'snmptargetparamssecurityname',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetParamsStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.
                ''',
                'snmptargetparamsstoragetype',
                'SNMP-TARGET-MIB', False),
            ],
            'SNMP-TARGET-MIB',
            'snmpTargetParamsEntry',
            _yang_ns._namespaces['SNMP-TARGET-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB'
        ),
    },
    'SnmpTargetMib.Snmptargetparamstable' : {
        'meta_info' : _MetaInfoClass('SnmpTargetMib.Snmptargetparamstable',
            False, 
            [
            _MetaInfoClassMember('snmpTargetParamsEntry', REFERENCE_LIST, 'Snmptargetparamsentry' , 'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB', 'SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry', 
                [], [], 
                '''                A set of SNMP target information.
                
                Entries in the snmpTargetParamsTable are created and
                deleted using the snmpTargetParamsRowStatus object.
                ''',
                'snmptargetparamsentry',
                'SNMP-TARGET-MIB', False),
            ],
            'SNMP-TARGET-MIB',
            'snmpTargetParamsTable',
            _yang_ns._namespaces['SNMP-TARGET-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB'
        ),
    },
    'SnmpTargetMib' : {
        'meta_info' : _MetaInfoClass('SnmpTargetMib',
            False, 
            [
            _MetaInfoClassMember('snmpTargetAddrTable', REFERENCE_CLASS, 'Snmptargetaddrtable' , 'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB', 'SnmpTargetMib.Snmptargetaddrtable', 
                [], [], 
                '''                A table of transport addresses to be used in the generation
                of SNMP messages.
                ''',
                'snmptargetaddrtable',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetObjects', REFERENCE_CLASS, 'Snmptargetobjects' , 'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB', 'SnmpTargetMib.Snmptargetobjects', 
                [], [], 
                '''                ''',
                'snmptargetobjects',
                'SNMP-TARGET-MIB', False),
            _MetaInfoClassMember('snmpTargetParamsTable', REFERENCE_CLASS, 'Snmptargetparamstable' , 'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB', 'SnmpTargetMib.Snmptargetparamstable', 
                [], [], 
                '''                A table of SNMP target information to be used
                in the generation of SNMP messages.
                ''',
                'snmptargetparamstable',
                'SNMP-TARGET-MIB', False),
            ],
            'SNMP-TARGET-MIB',
            'SNMP-TARGET-MIB',
            _yang_ns._namespaces['SNMP-TARGET-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_TARGET_MIB'
        ),
    },
}
_meta_table['SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry']['meta_info'].parent =_meta_table['SnmpTargetMib.Snmptargetaddrtable']['meta_info']
_meta_table['SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry']['meta_info'].parent =_meta_table['SnmpTargetMib.Snmptargetparamstable']['meta_info']
_meta_table['SnmpTargetMib.Snmptargetobjects']['meta_info'].parent =_meta_table['SnmpTargetMib']['meta_info']
_meta_table['SnmpTargetMib.Snmptargetaddrtable']['meta_info'].parent =_meta_table['SnmpTargetMib']['meta_info']
_meta_table['SnmpTargetMib.Snmptargetparamstable']['meta_info'].parent =_meta_table['SnmpTargetMib']['meta_info']
