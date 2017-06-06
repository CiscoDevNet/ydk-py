


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoCefMib.Ceffib' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceffib',
            False, 
            [
            _MetaInfoClassMember('cefLMPrefixSpinLock', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                An advisory lock used to allow cooperating SNMP
                Command Generator applications to coordinate their
                use of the Set operation in creating Longest
                Match Prefix Entries in cefLMPrefixTable.
                
                When creating a new longest prefix match entry,
                the value of cefLMPrefixSpinLock should be retrieved.  
                The destination address should be determined to be
                unique by the SNMP Command Generator application by
                consulting the cefLMPrefixTable. Finally, the longest 
                prefix entry may be created (Set), including the
                advisory lock.
                       
                If another SNMP Command Generator application has
                altered the longest prefix entry in the meantime, 
                then the spin lock's value will have changed, 
                and so this creation will fail because it will specify
                the wrong value for the spin lock.
                
                Since this is an advisory lock, the use of this lock
                is not enforced, but not using this lock may lead
                to conflict with the another SNMP command responder 
                application which may also be acting on the
                cefLMPrefixTable.
                ''',
                'ceflmprefixspinlock',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefFIB',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefcc' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefcc',
            False, 
            [
            _MetaInfoClassMember('cefInconsistencyReset', REFERENCE_ENUM_CLASS, 'CefccactionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefccactionEnum', 
                [], [], 
                '''                Setting the value of this object to ccActionStart(1)
                will reset all the active consistency checkers.
                
                The Management station should poll the 
                cefInconsistencyResetStatus object to get the 
                state of inconsistency reset operation.
                
                This operation once started, cannot be aborted.
                Hence, the value of this object cannot be set to
                ccActionAbort(2).
                
                The value of this object can't be set to ccActionStart(1), 
                if the value of object cefInconsistencyResetStatus
                is ccStatusRunning(2).
                ''',
                'cefinconsistencyreset',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyResetStatus', REFERENCE_ENUM_CLASS, 'CefccstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefccstatusEnum', 
                [], [], 
                '''                Indicates the status of the consistency reset
                request.
                ''',
                'cefinconsistencyresetstatus',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('entLastInconsistencyDetectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time an
                inconsistency is detecetd.
                ''',
                'entlastinconsistencydetecttime',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCC',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefnotifcntl' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefnotifcntl',
            False, 
            [
            _MetaInfoClassMember('cefInconsistencyNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether cefInconsistencyDetection notification
                should be generated for this managed device.
                ''',
                'cefinconsistencynotifenable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefNotifThrottlingInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                This object controls the generation of the
                cefInconsistencyDetection notification.
                
                If this object has a value of zero,
                then the throttle control is disabled.
                
                If this object has a non-zero value, then the agent
                must not generate more than one 
                cefInconsistencyDetection 'notification-event' in the 
                indicated period, where a 'notification-event' is the
                transmission of a single trap
                or inform PDU to a list of notification destinations.
                
                If additional inconsistency is detected within the 
                throttling period, then notification-events
                for these inconsistencies should be suppressed by the agent
                until the current throttling period expires.  At the end of a
                throttling period, one notification-event should be generated
                if any inconsistency was detected since the start of the 
                throttling period. In such a case,  another throttling period
                is started right away.
                
                An NMS should periodically poll cefInconsistencyRecordTable
                to detect any missed cefInconsistencyDetection
                notification-events, e.g., due to throttling or transmission
                loss.
                 
                If cefNotifThrottlingInterval notification generation
                is enabled, the suggested default throttling period is
                60 seconds, but generation of the cefInconsistencyDetection
                notification should be disabled by default.
                
                If the agent is capable of storing non-volatile
                configuration, then the value of this object must be
                restored after a re-initialization of the management
                system.
                
                The actual transmission of notifications is controlled
                via the MIB modules in RFC 3413.
                ''',
                'cefnotifthrottlinginterval',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPeerFIBStateChangeNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether or not a notification should be
                generated on the detection of CEF FIB peer state change.
                ''',
                'cefpeerfibstatechangenotifenable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPeerStateChangeNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether or not a notification should be
                generated on the detection of CEF peer state change.
                ''',
                'cefpeerstatechangenotifenable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefResourceFailureNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether or not a notification should be
                generated on the detection of CEF resource Failure.
                ''',
                'cefresourcefailurenotifenable',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefNotifCntl',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                The version of IP forwarding.
                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBSummaryFwdPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of forwarding Prefixes
                in FIB for the IP version specified
                by cefFIBIpVersion object.
                ''',
                'ceffibsummaryfwdprefixes',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefFIBSummaryEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Ceffibsummarytable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceffibsummarytable',
            False, 
            [
            _MetaInfoClassMember('cefFIBSummaryEntry', REFERENCE_LIST, 'Ceffibsummaryentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contains the FIB summary related
                attributes for the managed entity.
                
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'ceffibsummaryentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefFIBSummaryTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefprefixtable.Cefprefixentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefprefixtable.Cefprefixentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The Network Prefix Type.
                This object specifies the address type
                used for cefPrefixAddr.
                
                Prefix entries are only valid for the address
                type of ipv4(1) and ipv6(2).
                ''',
                'cefprefixtype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Network Prefix Address.
                The type of this address is determined by
                the value of the cefPrefixType object.
                This object is a Prefix Address containing the 
                prefix with length specified by cefPrefixLen. 
                Any bits beyond the length specified by
                cefPrefixLen are zeroed.
                ''',
                'cefprefixaddr',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                Length in bits of the FIB Address prefix.
                ''',
                'cefprefixlen',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If CEF accounting is set to enable per prefix
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'perPrefix' 
                accounting), then this object represents the 
                number of bytes switched to this prefix.
                ''',
                'cefprefixbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixExternalNRBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If CEF accounting is set to enable nonRecursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents 
                the number of non-recursive bytes in the external
                bucket switched using this prefix.
                ''',
                'cefprefixexternalnrbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixExternalNRHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If CEF accounting is set to enable nonRecursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents 
                the number of non-recursive bytes in the external
                bucket switched using this prefix.
                
                This object is a 64-bit version of 
                cefPrefixExternalNRBytes.
                ''',
                'cefprefixexternalnrhcbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixExternalNRHCPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If CEF accounting is set to enable non-recursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents the number
                of non-recursive packets in the external bucket
                switched using this prefix.
                
                This object is a 64-bit version of 
                cefPrefixExternalNRPkts.
                ''',
                'cefprefixexternalnrhcpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixExternalNRPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If CEF accounting is set to enable non-recursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents the number
                of non-recursive packets in the external bucket
                switched using this prefix.
                ''',
                'cefprefixexternalnrpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixForwardingInfo', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the associated forwarding element
                selection entries in cefFESelectionTable.
                The value of this object is index value (cefFESelectionName)
                of cefFESelectionTable.
                ''',
                'cefprefixforwardinginfo',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If CEF accounting is set to enable per prefix
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'perPrefix' 
                accounting), then this object represents the 
                number of bytes switched to this prefix.
                
                This object is a 64-bit version of 
                cefPrefixBytes.
                ''',
                'cefprefixhcbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixHCPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If CEF accounting is set to enable per prefix
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'perPrefix' 
                accounting), then this object represents the 
                number of packets switched to this prefix. 
                
                This object is a 64-bit version of 
                cefPrefixPkts.
                ''',
                'cefprefixhcpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixInternalNRBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If CEF accounting is set to enable nonRecursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents 
                the number of non-recursive bytes in the internal
                bucket switched using this prefix.
                ''',
                'cefprefixinternalnrbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixInternalNRHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If CEF accounting is set to enable nonRecursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents 
                the number of non-recursive bytes in the internal
                bucket switched using this prefix.
                
                This object is a 64-bit version of 
                cefPrefixInternalNRBytes.
                ''',
                'cefprefixinternalnrhcbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixInternalNRHCPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If CEF accounting is set to enable non-recursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents the number
                of non-recursive packets in the internal bucket
                switched using this prefix.
                
                This object is a 64-bit version of 
                cefPrefixInternalNRPkts.
                ''',
                'cefprefixinternalnrhcpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixInternalNRPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If CEF accounting is set to enable non-recursive
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'nonRecursive' 
                accounting), then this object represents the number
                of non-recursive packets in the internal bucket
                switched using this prefix.
                ''',
                'cefprefixinternalnrpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If CEF accounting is set to enable per prefix
                accounting (value of cefCfgAccountingMap object in 
                the cefCfgEntry is set to enable 'perPrefix' 
                accounting), then this object represents the 
                number of packets switched to this prefix.
                ''',
                'cefprefixpkts',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPrefixEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefprefixtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefprefixtable',
            False, 
            [
            _MetaInfoClassMember('cefPrefixEntry', REFERENCE_LIST, 'Cefprefixentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefprefixtable.Cefprefixentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contains the forwarding 
                prefix attributes. 
                
                CEF prefix based non-recursive stats are maintained
                in internal and external buckets (depending upon the 
                value of cefIntNonrecursiveAccouting object in the 
                CefIntEntry).
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefprefixentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPrefixTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefLMPrefixDestAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The Destination Address Type.
                This object specifies the address type
                used for cefLMPrefixDestAddr.
                
                Longest Match Prefix entries are only valid 
                for the address type of ipv4(1) and ipv6(2).
                ''',
                'ceflmprefixdestaddrtype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefLMPrefixDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Destination Address.
                The type of this address is determined by
                the value of the cefLMPrefixDestAddrType object.
                ''',
                'ceflmprefixdestaddr',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefLMPrefixAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Network Prefix Address. Index to the cefPrefixTable.
                The type of this address is determined by
                the value of the cefLMPrefixDestAddrType object.
                ''',
                'ceflmprefixaddr',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefLMPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The Network Prefix Length. Index to the cefPrefixTable.
                ''',
                'ceflmprefixlen',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefLMPrefixRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry.  Once the entry 
                status is set to active(1), the associated entry 
                cannot be modified until the request completes
                (cefLMPrefixState transitions to matchFound(2) 
                or noMatchFound(3)).
                
                Once the longest match request has been created
                (i.e. the cefLMPrefixRowStatus has been made active),
                the entry cannot be modified - the only operation
                possible after this is to delete the row.
                ''',
                'ceflmprefixrowstatus',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefLMPrefixState', REFERENCE_ENUM_CLASS, 'CefprefixsearchstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefprefixsearchstateEnum', 
                [], [], 
                '''                Indicates the state of this prefix search request.
                ''',
                'ceflmprefixstate',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefLMPrefixEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Ceflmprefixtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceflmprefixtable',
            False, 
            [
            _MetaInfoClassMember('cefLMPrefixEntry', REFERENCE_LIST, 'Ceflmprefixentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry', 
                [], [], 
                '''                If CEF is enabled on the managed device, then each
                entry represents a longest Match Prefix request.
                
                A management station wishing to get the longest
                Match prefix for a given destination address
                should create the associate instance of the
                row status. The row status should be set to
                active(1) to initiate the request. Note that 
                this entire procedure may be initiated via a 
                single set request which specifies a row status 
                of createAndGo(4).
                
                Once the request completes, the management station 
                should retrieve the values of the objects of 
                interest, and should then delete the entry.  In order 
                to prevent old entries from clogging the table, 
                entries will be aged out, but an entry will never be 
                deleted within 5 minutes of completion.
                Entries are lost after an agent restart.
                
                I.e. to find out the longest prefix match for 
                destination address of A.B.C.D on entity whose
                entityPhysicalIndex is 1, the Management station
                will create an entry in cefLMPrefixTable with
                cefLMPrefixRowStatus.1(entPhysicalIndex).1(ipv4).A.B.C.D
                set to createAndGo(4). Management Station may query the
                value of objects cefLMPrefix and cefLMPrefixLen
                to find out the corresponding prefix entry from the
                cefPrefixTable once the value of cefLMPrefixState
                is set to matchFound(2).
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'ceflmprefixentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefLMPrefixTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefpathtable.Cefpathentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefpathtable.Cefpathentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cefprefixtype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'cefprefixaddr',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                ''',
                'cefprefixlen',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPathId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this prefix path entry.
                ''',
                'cefpathid',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPathInterface', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Interface associated with this CEF path.
                
                A value of zero for this object will indicate
                that no interface is associated with this path 
                entry.
                ''',
                'cefpathinterface',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPathNextHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Next hop address associated with this CEF path.
                
                The value of this object is only relevant
                for attached next hop and recursive next hop  
                path types (when the object cefPathType is
                set to attachedNexthop(4) or recursiveNexthop(5)).
                and will be set to zero for other path types.
                
                The type of this address is determined by
                the value of the cefPrefixType object.
                ''',
                'cefpathnexthopaddr',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPathRecurseVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                The recursive vrf name associated with this path.
                
                The value of this object is only relevant
                for recursive next hop path types (when the 
                object cefPathType is set to recursiveNexthop(5)),
                and '0x00' will be returned for other path types.
                ''',
                'cefpathrecursevrfname',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPathType', REFERENCE_ENUM_CLASS, 'CefpathtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefpathtypeEnum', 
                [], [], 
                '''                Type for this CEF Path.
                ''',
                'cefpathtype',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPathEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefpathtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefpathtable',
            False, 
            [
            _MetaInfoClassMember('cefPathEntry', REFERENCE_LIST, 'Cefpathentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpathtable.Cefpathentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contain a CEF prefix path.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefpathentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPathTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjSummaryLinkType', REFERENCE_ENUM_CLASS, 'CefadjlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefadjlinktypeEnum', 
                [], [], 
                '''                The link type of the adjacency.
                ''',
                'cefadjsummarylinktype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjSummaryComplete', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of complete adjacencies.
                
                The total number of adjacencies which can be used 
                to switch traffic to a neighbour.
                ''',
                'cefadjsummarycomplete',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjSummaryFixup', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of adjacencies for which
                the Layer 2 encapsulation string (header) may be 
                updated (fixed up) at packet switch time.
                ''',
                'cefadjsummaryfixup',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjSummaryIncomplete', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of incomplete adjacencies.
                
                The total number of adjacencies which cannot be 
                used to switch traffic in their current state.
                ''',
                'cefadjsummaryincomplete',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjSummaryRedirect', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of adjacencies for which 
                ip redirect (or icmp redirection) is enabled.
                The value of this object is only relevant for
                ipv4 and ipv6 link type (when the index object 
                cefAdjSummaryLinkType value is ipv4(1) or ipv6(2))
                and will be set to zero for other link types.
                ''',
                'cefadjsummaryredirect',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefAdjSummaryEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefadjsummarytable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefadjsummarytable',
            False, 
            [
            _MetaInfoClassMember('cefAdjSummaryEntry', REFERENCE_LIST, 'Cefadjsummaryentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contains the CEF Adjacency  
                summary related attributes for the
                Managed entity. A row exists for
                each adjacency link type.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefadjsummaryentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefAdjSummaryTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefadjtable.Cefadjentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefadjtable.Cefadjentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjNextHopAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Address type for the cefAdjNextHopAddr.
                This object specifies the address type
                used for cefAdjNextHopAddr. 
                
                Adjacency entries are only valid for the 
                address type of ipv4(1) and ipv6(2).
                ''',
                'cefadjnexthopaddrtype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjNextHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The next Hop address for this adjacency.
                The type of this address is determined by
                the value of the cefAdjNextHopAddrType object.
                ''',
                'cefadjnexthopaddr',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjConnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In cases where cefLinkType, interface and the
                next hop address are not able to uniquely define
                an adjacency entry (e.g. ATM and Frame Relay
                Bundles), this object is a unique identifier
                to differentiate between these adjacency entries. 
                
                In all the other cases the value of this 
                index object will be 0.
                ''',
                'cefadjconnid',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjSummaryLinkType', REFERENCE_ENUM_CLASS, 'CefadjlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefadjlinktypeEnum', 
                [], [], 
                '''                ''',
                'cefadjsummarylinktype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefAdjBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bytes transmitted using this adjacency.
                ''',
                'cefadjbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjEncap', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The layer 2 encapsulation string to be used
                for sending the packet out using this adjacency.
                ''',
                'cefadjencap',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjFixup', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For the cases, where the encapsulation string
                is decided at packet switch time, the adjacency 
                encapsulation string specified by object cefAdjEncap 
                require a fixup. I.e. for the adjacencies out of IP 
                Tunnels, the string prepended is an IP header which has 
                fields which can only be setup at packet switch time.
                
                The value of this object represent the kind of fixup
                applied to the packet.
                
                If the encapsulation string doesn't require any fixup,
                then the value of this object will be of zero length.
                ''',
                'cefadjfixup',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjForwardingInfo', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object selects a forwarding info entry 
                defined in the cefFESelectionTable. The 
                selected target is defined by an entry in the
                cefFESelectionTable whose index value (cefFESelectionName) 
                is equal to this object.
                
                The value of this object will be of zero length if
                this adjacency entry is the last forwarding 
                element in the forwarding path.
                ''',
                'cefadjforwardinginfo',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes transmitted using this adjacency.
                This object is a 64-bit version of cefAdjBytes.
                ''',
                'cefadjhcbytes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjHCPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of pkts transmitted using this adjacency.
                This object is a 64-bit version of cefAdjPkts.
                ''',
                'cefadjhcpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjMTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Layer 3 MTU which can be transmitted using 
                this adjacency.
                ''',
                'cefadjmtu',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pkts transmitted using this adjacency.
                ''',
                'cefadjpkts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjSource', REFERENCE_BITS, 'Cefadjacencysource' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'Cefadjacencysource', 
                [], [], 
                '''                If the adjacency is created because some neighbour
                discovery mechanism has discovered a neighbour
                and all the information required to build a frame header to
                encapsulate traffic to the neighbour is available
                then the source of adjacency is set to the mechanism
                by which the adjacency is learned.
                ''',
                'cefadjsource',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefAdjEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefadjtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefadjtable',
            False, 
            [
            _MetaInfoClassMember('cefAdjEntry', REFERENCE_LIST, 'Cefadjentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefadjtable.Cefadjentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contains the adjacency 
                attributes. Adjacency entries may exist
                for all the interfaces on which packets
                can be switched out of the device.
                The interface is instantiated by ifIndex.  
                Therefore, the interface index must have been
                assigned, according to the applicable procedures,
                before it can be meaningfully used.
                Generally, this means that the interface must exist.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefadjentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefAdjTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFESelectionName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The locally arbitrary, but unique identifier used
                to select a set of forwarding element lists.
                ''',
                'ceffeselectionname',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFESelectionId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Secondary index to identify a forwarding elements List 
                in this Table.
                ''',
                'ceffeselectionid',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFESelectionAdjConnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represent the connection id for
                the adjacency associated with this forwarding 
                Element List.
                
                The value of this object will be irrelevant and will
                be set to zero if the forwarding element list doesn't 
                contain an adjacency forwarding element. 
                
                In cases where cefFESelectionAdjLinkType, interface 
                and the next hop address are not able to uniquely 
                define an adjacency entry (e.g. ATM and Frame Relay
                Bundles), this object is a unique identifier
                to differentiate between these adjacency entries.
                ''',
                'ceffeselectionadjconnid',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionAdjInterface', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object represent the interface for
                the adjacency associated with this forwarding 
                Element List.
                
                The value of this object will be irrelevant and will
                be set to zero if the forwarding element list doesn't 
                contain an adjacency forwarding element.
                ''',
                'ceffeselectionadjinterface',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionAdjLinkType', REFERENCE_ENUM_CLASS, 'CefadjlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefadjlinktypeEnum', 
                [], [], 
                '''                This object represent the link type for
                the adjacency associated with this forwarding 
                Element List.
                
                The value of this object will be irrelevant and will
                be set to unknown(5) if the forwarding element list 
                doesn't contain an adjacency forwarding element.
                ''',
                'ceffeselectionadjlinktype',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionAdjNextHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object represent the next hop address for
                the adjacency associated with this forwarding 
                Element List.
                
                The value of this object will be irrelevant and will
                be set to zero if the forwarding element list doesn't 
                contain an adjacency forwarding element.
                ''',
                'ceffeselectionadjnexthopaddr',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionAdjNextHopAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object represent the next hop address type for
                the adjacency associated with this forwarding 
                Element List.
                
                The value of this object will be irrelevant and will
                be set to unknown(0) if the forwarding element list 
                doesn't contain an adjacency forwarding element.
                ''',
                'ceffeselectionadjnexthopaddrtype',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionLabels', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object represent the MPLS Labels 
                associated with this forwarding Element List.
                
                The value of this object will be irrelevant and will
                be set to zero length if the forwarding element list 
                doesn't contain a label forwarding element. A zero 
                length label list will indicate that there is no label
                forwarding element associated with this selection entry.
                ''',
                'ceffeselectionlabels',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionSpecial', REFERENCE_ENUM_CLASS, 'CefforwardingelementspecialtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefforwardingelementspecialtypeEnum', 
                [], [], 
                '''                Special processing for a destination
                is indicated through the use of special 
                forwarding element. 
                
                If the forwarding element list contains the 
                special forwarding element, then this object 
                represents the type of special forwarding element.
                ''',
                'ceffeselectionspecial',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                This object represent the Vrf name for
                the lookup associated with this forwarding 
                Element List.
                
                The value of this object will be irrelevant and will
                be set to a string containing the single octet
                0x00 if the forwarding element list 
                doesn't contain a lookup forwarding element.
                ''',
                'ceffeselectionvrfname',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionWeight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represent the weighting for 
                load balancing between multiple Forwarding Element
                Lists. The value of this object will be zero if
                load balancing is associated with this selection
                entry.
                ''',
                'ceffeselectionweight',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefFESelectionEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Ceffeselectiontable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Ceffeselectiontable',
            False, 
            [
            _MetaInfoClassMember('cefFESelectionEntry', REFERENCE_LIST, 'Ceffeselectionentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contain a CEF forwarding element
                selection list.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'ceffeselectionentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefFESelectionTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefcfgtable.Cefcfgentry.CefcfgloadsharingalgorithmEnum' : _MetaInfoEnum('CefcfgloadsharingalgorithmEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'none':'none',
            'original':'original',
            'tunnel':'tunnel',
            'universal':'universal',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefcfgtable.Cefcfgentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefcfgtable.Cefcfgentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefCfgAccountingMap', REFERENCE_BITS, 'Cefcfgaccountingmap' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcfgtable.Cefcfgentry.Cefcfgaccountingmap', 
                [], [], 
                '''                This object represents a bitmap of network
                accounting options.
                
                CEF network accounting is disabled by default.
                
                CEF network accounting can be enabled 
                by selecting one or more of the following
                CEF accounting option for the value
                of this object.
                 
                 nonRecursive(0):  enables accounting through 
                                   nonrecursive prefixes.
                
                 perPrefix(1):     enables the collection of the numbers 
                                   of pkts and bytes express forwarded
                                   to a destination (prefix)
                
                 prefixLength(2):  enables accounting through 
                                   prefixlength.        
                
                 Once the accounting is enabled, the corresponding stats
                 can be retrieved from the cefPrefixTable and
                 cefStatsPrefixLenTable.
                 
                ''',
                'cefcfgaccountingmap',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgAdminState', REFERENCE_ENUM_CLASS, 'CefadminstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefadminstatusEnum', 
                [], [], 
                '''                The desired state of CEF.
                ''',
                'cefcfgadminstate',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgDistributionAdminState', REFERENCE_ENUM_CLASS, 'CefadminstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefadminstatusEnum', 
                [], [], 
                '''                The desired state of CEF distribution.
                ''',
                'cefcfgdistributionadminstate',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgDistributionOperState', REFERENCE_ENUM_CLASS, 'CefoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefoperstatusEnum', 
                [], [], 
                '''                The current operational state of CEF distribution.
                
                If the cefCfgDistributionAdminState is disabled(2), then
                cefDistributionOperState will eventually go to the down(2)
                state unless some error has occurred.  
                
                If cefCfgDistributionAdminState is changed to enabled(1) 
                then cefCfgDistributionOperState should change to up(1) 
                only if the CEF entity is ready to forward the packets 
                using Distributed Cisco Express Forwarding (dCEF) else 
                it should remain in the down(2) state. The up(1) state 
                for this object indicates that CEF entity is forwarding
                the packet using Distributed Cisco Express Forwarding.
                ''',
                'cefcfgdistributionoperstate',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgLoadSharingAlgorithm', REFERENCE_ENUM_CLASS, 'CefcfgloadsharingalgorithmEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcfgtable.Cefcfgentry.CefcfgloadsharingalgorithmEnum', 
                [], [], 
                '''                Indicates the CEF Load balancing algorithm.
                
                Setting this object to none(1) will disable
                the Load sharing for the specified entry.
                
                CEF load balancing can be enabled by setting 
                this object to one of following Algorithms:
                
                 original(2)  : This algorithm is based on a 
                                source and destination hash 
                
                 tunnel(3)    : This algorithm is used in 
                                tunnels environments or in
                                environments where there are
                                only a few source 
                                  
                 universal(4)  : This algorithm uses a source and 
                                 destination and ID hash
                
                If the value of this object is set to 'tunnel'
                or 'universal', then the FIXED ID for these
                algorithms may be specified by the managed 
                object cefLoadSharingID. 
                ''',
                'cefcfgloadsharingalgorithm',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgLoadSharingID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Fixed ID associated with the managed object
                cefCfgLoadSharingAlgorithm. The hash of this object
                value may be used by the Load Sharing Algorithm.
                
                The value of this object is not relevant and will
                be set to zero if the value of managed object 
                cefCfgLoadSharingAlgorithm is set to none(1) or original(2).
                The default value of this object is calculated by
                the device at the time of initialization.
                ''',
                'cefcfgloadsharingid',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgOperState', REFERENCE_ENUM_CLASS, 'CefoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefoperstatusEnum', 
                [], [], 
                '''                The current operational state of CEF.
                
                If the cefCfgAdminState is disabled(2), then
                cefOperState will eventually go to the down(2)
                state unless some error has occurred. 
                
                If cefCfgAdminState is changed to enabled(1) then 
                cefCfgOperState should change to up(1) only if the 
                CEF entity is ready to forward the packets using 
                Cisco Express Forwarding (CEF) else it should remain 
                in the down(2) state. The up(1) state for this object 
                indicates that CEF entity is forwarding the packet
                using Cisco Express Forwarding.
                ''',
                'cefcfgoperstate',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgTrafficStatsLoadInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The interval time over which the CEF traffic statistics
                are collected.
                ''',
                'cefcfgtrafficstatsloadinterval',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgTrafficStatsUpdateRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The frequency with which the line card sends the
                traffic load statistics to the Router Processor.
                
                Setting the value of this object to 0 will disable
                the CEF traffic statistics collection.
                ''',
                'cefcfgtrafficstatsupdaterate',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCfgEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefcfgtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefcfgtable',
            False, 
            [
            _MetaInfoClassMember('cefCfgEntry', REFERENCE_LIST, 'Cefcfgentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcfgtable.Cefcfgentry', 
                [], [], 
                '''                If the Managed device supports CEF, 
                each entry contains the CEF config 
                parameter for the managed entity.
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefcfgentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCfgTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefresourcetable.Cefresourceentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefresourcetable.Cefresourceentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefResourceFailureReason', REFERENCE_ENUM_CLASS, 'CeffailurereasonEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CeffailurereasonEnum', 
                [], [], 
                '''                The CEF resource failure reason which may lead to CEF
                being disabled on the managed entity.
                ''',
                'cefresourcefailurereason',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefResourceMemoryUsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of bytes from
                the Processor Memory Pool that
                are currently in use by CEF on the
                managed entity.
                ''',
                'cefresourcememoryused',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefResourceEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefresourcetable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefresourcetable',
            False, 
            [
            _MetaInfoClassMember('cefResourceEntry', REFERENCE_LIST, 'Cefresourceentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefresourcetable.Cefresourceentry', 
                [], [], 
                '''                If the Managed device supports CEF,
                each entry contains the CEF Resource 
                parameters for the managed entity.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefresourceentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefResourceTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefinttable.Cefintentry.CefintloadsharingEnum' : _MetaInfoEnum('CefintloadsharingEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'perPacket':'perPacket',
            'perDestination':'perDestination',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefinttable.Cefintentry.CefintnonrecursiveaccoutingEnum' : _MetaInfoEnum('CefintnonrecursiveaccoutingEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'internal':'internal',
            'external':'external',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefinttable.Cefintentry.CefintswitchingstateEnum' : _MetaInfoEnum('CefintswitchingstateEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'cefEnabled':'cefEnabled',
            'distCefEnabled':'distCefEnabled',
            'cefDisabled':'cefDisabled',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefinttable.Cefintentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefinttable.Cefintentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefIntLoadSharing', REFERENCE_ENUM_CLASS, 'CefintloadsharingEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinttable.Cefintentry.CefintloadsharingEnum', 
                [], [], 
                '''                The status of load sharing on the
                interface.
                
                perPacket(1) : Router to send data packets
                               over successive equal-cost paths
                               without regard to individual hosts
                               or user sessions.
                
                perDestination(2) : Router to use multiple, equal-cost
                                    paths to achieve load sharing
                
                Load sharing is enabled by default 
                for an interface when CEF is enabled.
                ''',
                'cefintloadsharing',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefIntNonrecursiveAccouting', REFERENCE_ENUM_CLASS, 'CefintnonrecursiveaccoutingEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinttable.Cefintentry.CefintnonrecursiveaccoutingEnum', 
                [], [], 
                '''                The CEF accounting mode for the interface.
                CEF prefix based non-recursive accounting 
                on an interface can be configured to store 
                the stats for non-recursive prefixes in a internal 
                or external bucket.
                
                internal(1)  :  Count input traffic in the nonrecursive
                                internal bucket
                
                external(2)  :  Count input traffic in the nonrecursive
                                external bucket
                
                The value of this object will only be effective if 
                value of the object cefAccountingMap is set to enable
                nonRecursive(1) accounting.
                ''',
                'cefintnonrecursiveaccouting',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefIntSwitchingState', REFERENCE_ENUM_CLASS, 'CefintswitchingstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinttable.Cefintentry.CefintswitchingstateEnum', 
                [], [], 
                '''                The CEF switching State for the interface. 
                If CEF is enabled but distributed CEF(dCEF) is
                disabled then CEF is in cefEnabled(1) state.
                
                If distributed CEF is enabled, then CEF is in 
                distCefEnabled(2) state. The cefDisabled(3) state
                indicates that CEF is disabled.
                
                The CEF switching state is only applicable to the
                received packet on the interface.
                ''',
                'cefintswitchingstate',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefIntEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefinttable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefinttable',
            False, 
            [
            _MetaInfoClassMember('cefIntEntry', REFERENCE_LIST, 'Cefintentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinttable.Cefintentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device, 
                each entry contains the CEF attributes 
                associated with an interface.
                The interface is instantiated by ifIndex.  
                Therefore, the interface index must have been
                assigned, according to the applicable procedures,
                before it can be meaningfully used.
                Generally, this means that the interface must exist.
                
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefintentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefIntTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefpeertable.Cefpeerentry.CefpeeroperstateEnum' : _MetaInfoEnum('CefpeeroperstateEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'peerDisabled':'peerDisabled',
            'peerUp':'peerUp',
            'peerHold':'peerHold',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefpeertable.Cefpeerentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefpeertable.Cefpeerentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('entPeerPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The entity index for the CEF peer entity.
                Only the entities of 'module' 
                entPhysicalClass are included here.
                ''',
                'entpeerphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPeerNumberOfResets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the session with CEF peer entity 
                has been reset.
                ''',
                'cefpeernumberofresets',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPeerOperState', REFERENCE_ENUM_CLASS, 'CefpeeroperstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpeertable.Cefpeerentry.CefpeeroperstateEnum', 
                [], [], 
                '''                The current CEF operational state of the CEF peer entity.
                
                Cef peer entity oper state will be peerDisabled(1) in 
                the following condition:
                
                   : Cef Peer entity encounters fatal error i.e. resource
                     allocation failure, ipc failure etc
                
                   : When a reload/delete request is received from the Cef 
                     Peer Entity
                
                Once the peer entity is up and no fatal error is encountered,
                then the value of this object will transits to the peerUp(3) 
                state.
                
                If the Cef Peer entity is in held stage, then the value
                of this object will be peerHold(3). Cef peer entity can only
                transit to peerDisabled(1) state from the peerHold(3) state.
                ''',
                'cefpeeroperstate',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPeerEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefpeertable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefpeertable',
            False, 
            [
            _MetaInfoClassMember('cefPeerEntry', REFERENCE_LIST, 'Cefpeerentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpeertable.Cefpeerentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contains the CEF related attributes 
                associated with a CEF peer entity.
                
                entPhysicalIndex and entPeerPhysicalIndex are
                also indexes for this table which represents
                entities of 'module' entPhysicalClass which are
                capable of running CEF.
                ''',
                'cefpeerentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPeerTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry.CefpeerfiboperstateEnum' : _MetaInfoEnum('CefpeerfiboperstateEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'peerFIBDown':'peerFIBDown',
            'peerFIBUp':'peerFIBUp',
            'peerFIBReloadRequest':'peerFIBReloadRequest',
            'peerFIBReloading':'peerFIBReloading',
            'peerFIBSynced':'peerFIBSynced',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('entPeerPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entpeerphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefPeerFIBOperState', REFERENCE_ENUM_CLASS, 'CefpeerfiboperstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry.CefpeerfiboperstateEnum', 
                [], [], 
                '''                The current CEF FIB Operational State for the 
                CEF peer entity.
                ''',
                'cefpeerfiboperstate',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPeerFIBEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefpeerfibtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefpeerfibtable',
            False, 
            [
            _MetaInfoClassMember('cefPeerFIBEntry', REFERENCE_LIST, 'Cefpeerfibentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry contains the CEF FIB State 
                associated a CEF peer entity.
                
                entPhysicalIndex and entPeerPhysicalIndex are
                also indexes for this table which represents
                entities of 'module' entPhysicalClass which are
                capable of running CEF.
                ''',
                'cefpeerfibentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefPeerFIBTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefccglobaltable.Cefccglobalentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefccglobaltable.Cefccglobalentry',
            False, 
            [
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefCCGlobalAutoRepairDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indiactes how long the consistency checker 
                waits to fix an inconsistency.
                
                The value of this object has no effect when the
                value of object cefCCGlobalAutoRepairEnabled
                is 'false'.
                ''',
                'cefccglobalautorepairdelay',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCGlobalAutoRepairEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Once an inconsistency has been detected, 
                CEF has the ability to repair the problem. 
                This object indicates the status of auto-repair 
                function for the consistency checkers.
                ''',
                'cefccglobalautorepairenabled',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCGlobalAutoRepairHoldDown', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates how long the consistency checker
                waits to re-enable auto-repair after 
                auto-repair runs.
                
                The value of this object has no effect when the
                value of object cefCCGlobalAutoRepairEnabled
                is 'false'.
                ''',
                'cefccglobalautorepairholddown',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCGlobalErrorMsgEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables the consistency checker to generate 
                an error message when it detects an inconsistency.
                ''',
                'cefccglobalerrormsgenabled',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCGlobalFullScanAction', REFERENCE_ENUM_CLASS, 'CefccactionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefccactionEnum', 
                [], [], 
                '''                Setting the value of this object to ccActionStart(1)
                will start the full scan consistency checkers.
                
                The Management station should poll the 
                cefCCGlobalFullScanStatus object to get the 
                state of full-scan operation.
                
                Once the full-scan operation completes (value
                of cefCCGlobalFullScanStatus object is ccStatusDone(3)), 
                the Management station should retrieve the values of the
                related stats object from the cefCCTypeTable.
                
                Setting the value of this object to ccActionAbort(2) will 
                abort the full-scan operation.
                
                The value of this object can't be set to ccActionStart(1), 
                if the value of object cefCCGlobalFullScanStatus
                is ccStatusRunning(2).
                
                The value of this object will be set to cefActionNone(1)
                when the full scan consistency checkers have never
                been activated.
                
                A Management Station cannot set the value of
                this object to cefActionNone(1).
                ''',
                'cefccglobalfullscanaction',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCGlobalFullScanStatus', REFERENCE_ENUM_CLASS, 'CefccstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefccstatusEnum', 
                [], [], 
                '''                Indicates the status of the full scan consistency
                checker request.
                ''',
                'cefccglobalfullscanstatus',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCCGlobalEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefccglobaltable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefccglobaltable',
            False, 
            [
            _MetaInfoClassMember('cefCCGlobalEntry', REFERENCE_LIST, 'Cefccglobalentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefccglobaltable.Cefccglobalentry', 
                [], [], 
                '''                If the managed device supports CEF,
                each entry contains the global consistency 
                checker parameter for the managed device.
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                ''',
                'cefccglobalentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCCGlobalTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefcctypetable.Cefcctypeentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefcctypetable.Cefcctypeentry',
            False, 
            [
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefCCType', REFERENCE_ENUM_CLASS, 'CefcctypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefcctypeEnum', 
                [], [], 
                '''                Type of the consistency checker.
                ''',
                'cefcctype',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefCCCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of prefixes to check per scan.
                
                The default value for this object 
                depends upon the consistency checker type.
                
                The value of this object will be irrelevant 
                for some of the consistency checkers and
                will be set to 0.
                
                A Management Station cannot set the value of
                this object to 0.
                ''',
                'cefcccount',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables the passive consistency checker.
                Passive consistency checkers are disabled
                by default.
                
                Full-scan consistency checkers are always enabled.
                An attempt to set this object to 'false' for
                an active consistency checker will result in
                'wrongValue' error.
                ''',
                'cefccenabled',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCPeriod', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The period between scans for the consistency
                checker.
                ''',
                'cefccperiod',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCQueriesChecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefix consistency queries processed by this 
                consistency checker.
                ''',
                'cefccquerieschecked',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCQueriesIgnored', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefix consistency queries for which
                the consistency checks were not performed by this 
                consistency checker. This may be because of some
                internal error or resource failure.
                ''',
                'cefccqueriesignored',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCQueriesIterated', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefix consistency queries iterated back to
                the master database by this consistency checker.
                ''',
                'cefccqueriesiterated',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCQueriesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefix consistency queries sent to CEF
                forwarding databases by this consistency checker.
                ''',
                'cefccqueriessent',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCCTypeEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefcctypetable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefcctypetable',
            False, 
            [
            _MetaInfoClassMember('cefCCTypeEntry', REFERENCE_LIST, 'Cefcctypeentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcctypetable.Cefcctypeentry', 
                [], [], 
                '''                If the managed device supports CEF,
                each entry contains the consistency 
                checker statistics for a consistency 
                checker type.
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                ''',
                'cefcctypeentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefCCTypeTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry.CefinconsistencyreasonEnum' : _MetaInfoEnum('CefinconsistencyreasonEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB',
        {
            'missing':'missing',
            'checksumErr':'checksumErr',
            'unknown':'unknown',
        }, 'CISCO-CEF-MIB', _yang_ns._namespaces['CISCO-CEF-MIB']),
    'CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry',
            False, 
            [
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefInconsistencyRecId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this inconsistency record entry.
                ''',
                'cefinconsistencyrecid',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefInconsistencyCCType', REFERENCE_ENUM_CLASS, 'CefcctypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefcctypeEnum', 
                [], [], 
                '''                The type of consistency checker who generated this
                inconsistency record.
                ''',
                'cefinconsistencycctype',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyEntity', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The entity for which this inconsistency record was 
                generated. The value of this object will be 
                irrelevant and will be set to 0 when the inconsisency 
                record is applicable for all the entities.
                ''',
                'cefinconsistencyentity',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyPrefixAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The network prefix address associated with this 
                inconsistency record.
                
                The type of this address is determined by
                the value of the cefInconsistencyPrefixType object.
                ''',
                'cefinconsistencyprefixaddr',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                Length in bits of the inconsistency address prefix.
                ''',
                'cefinconsistencyprefixlen',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyPrefixType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The network prefix type associated with this inconsistency
                record.
                ''',
                'cefinconsistencyprefixtype',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyReason', REFERENCE_ENUM_CLASS, 'CefinconsistencyreasonEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry.CefinconsistencyreasonEnum', 
                [], [], 
                '''                The reason for generating this inconsistency record. 
                
                missing(1):        the prefix is missing
                
                checksumErr(2):    checksum error was found
                
                unknown(3):        reason is unknown
                ''',
                'cefinconsistencyreason',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                Vrf name associated with this inconsistency record.
                ''',
                'cefinconsistencyvrfname',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefInconsistencyRecordEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefinconsistencyrecordtable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefinconsistencyrecordtable',
            False, 
            [
            _MetaInfoClassMember('cefInconsistencyRecordEntry', REFERENCE_LIST, 'Cefinconsistencyrecordentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry', 
                [], [], 
                '''                If the managed device supports CEF,
                each entry contains the inconsistency 
                record.
                ''',
                'cefinconsistencyrecordentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefInconsistencyRecordTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefStatsPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                Length in bits of the Destination IP prefix.
                As 0.0.0.0/0 is a valid prefix, hence 
                0 is a valid prefix length.
                ''',
                'cefstatsprefixlen',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefStatsPrefixDeletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of delete operations performed to the FIB 
                database for the specified IP prefix length.
                ''',
                'cefstatsprefixdeletes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixElements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of elements in the FIB database for the
                specified IP prefix length.
                ''',
                'cefstatsprefixelements',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixHCDeletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of delete operations performed to the FIB 
                database for the specified IP prefix length.
                This object is a 64-bit version of 
                cefStatsPrefixDelete.
                ''',
                'cefstatsprefixhcdeletes',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixHCElements', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of elements in the FIB database for the
                specified IP prefix length.
                This object is a 64-bit version of 
                cefStatsPrefixElements.
                ''',
                'cefstatsprefixhcelements',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixHCInserts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of insert operations performed to the FIB 
                database for the specified IP prefix length.
                This object is a 64-bit version of 
                cefStatsPrefixInsert.
                ''',
                'cefstatsprefixhcinserts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixHCQueries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of queries received in the FIB database
                for the specified IP prefix length.
                This object is a 64-bit version of 
                cefStatsPrefixQueries.
                ''',
                'cefstatsprefixhcqueries',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixInserts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of insert operations performed to the FIB 
                database for the specified IP prefix length.
                ''',
                'cefstatsprefixinserts',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixQueries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of queries received in the FIB database 
                for the specified IP prefix length.
                ''',
                'cefstatsprefixqueries',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefStatsPrefixLenEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefstatsprefixlentable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefstatsprefixlentable',
            False, 
            [
            _MetaInfoClassMember('cefStatsPrefixLenEntry', REFERENCE_LIST, 'Cefstatsprefixlenentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device
                and if CEF accounting is set to enable 
                prefix length based accounting (value of 
                cefCfgAccountingMap object in the 
                cefCfgEntry is set to enable 'prefixLength' 
                accounting), each entry contains the traffic 
                statistics for a prefix length.
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefstatsprefixlenentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefStatsPrefixLenTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefFIBIpVersion', REFERENCE_ENUM_CLASS, 'CefipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefipversionEnum', 
                [], [], 
                '''                ''',
                'ceffibipversion',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefSwitchingIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this switching stats entry.
                ''',
                'cefswitchingindex',
                'CISCO-CEF-MIB', True),
            _MetaInfoClassMember('cefSwitchingDrop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped by CEF.
                ''',
                'cefswitchingdrop',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingHCDrop', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped by CEF.
                This object is a 64-bit version of cefSwitchingDrop.
                ''',
                'cefswitchinghcdrop',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingHCPunt', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that could not be switched
                in the normal path and were punted to the
                next-fastest switching vector.
                This object is a 64-bit version of cefSwitchingPunt.
                ''',
                'cefswitchinghcpunt',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingHCPunt2Host', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that could not be switched
                in the normal path and were punted to the host
                (process switching path).
                
                For most of the switching paths, the value of
                this object may be similar to cefSwitchingPunt.
                This object is a 64-bit version of cefSwitchingPunt2Host.
                ''',
                'cefswitchinghcpunt2host',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingPath', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Switch path where the feature was executed.
                Available switch paths are platform-dependent.
                Following are the examples of switching paths:
                
                   RIB : switching with CEF assistance
                
                   Low-end switching (LES) : CEF switch path
                
                   PAS : CEF turbo switch path.
                ''',
                'cefswitchingpath',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingPunt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets that could not be switched
                in the normal path and were punted to the
                next-fastest switching vector.
                ''',
                'cefswitchingpunt',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingPunt2Host', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets that could not be switched
                in the normal path and were punted to the host
                (process switching path).
                
                For most of the switching paths, the value of
                this object may be similar to cefSwitchingPunt.
                ''',
                'cefswitchingpunt2host',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefSwitchingStatsEntry',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib.Cefswitchingstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib.Cefswitchingstatstable',
            False, 
            [
            _MetaInfoClassMember('cefSwitchingStatsEntry', REFERENCE_LIST, 'Cefswitchingstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry', 
                [], [], 
                '''                If CEF is enabled on the Managed device,
                each entry specifies the switching stats.
                A row may exist for each IP version type
                (v4 and v6) depending upon the IP version
                supported on the device.
                
                entPhysicalIndex is also an index for this
                table which represents entities of
                'module' entPhysicalClass which are capable
                of running CEF.
                ''',
                'cefswitchingstatsentry',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'cefSwitchingStatsTable',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
    'CiscoCefMib' : {
        'meta_info' : _MetaInfoClass('CiscoCefMib',
            False, 
            [
            _MetaInfoClassMember('cefAdjSummaryTable', REFERENCE_CLASS, 'Cefadjsummarytable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefadjsummarytable', 
                [], [], 
                '''                This table contains the summary information
                for the cefAdjTable.
                ''',
                'cefadjsummarytable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefAdjTable', REFERENCE_CLASS, 'Cefadjtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefadjtable', 
                [], [], 
                '''                A list of CEF adjacencies.
                ''',
                'cefadjtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCC', REFERENCE_CLASS, 'Cefcc' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcc', 
                [], [], 
                '''                ''',
                'cefcc',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCGlobalTable', REFERENCE_CLASS, 'Cefccglobaltable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefccglobaltable', 
                [], [], 
                '''                This table contains CEF consistency checker
                (CC) global parameters for the managed device.
                ''',
                'cefccglobaltable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCCTypeTable', REFERENCE_CLASS, 'Cefcctypetable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcctypetable', 
                [], [], 
                '''                This table contains CEF consistency
                checker types specific parameters on the managed device.
                
                All detected inconsistency are signaled to the
                Management Station via cefInconsistencyDetection
                notification.
                ''',
                'cefcctypetable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefCfgTable', REFERENCE_CLASS, 'Cefcfgtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefcfgtable', 
                [], [], 
                '''                This table contains global config parameter 
                of CEF on the Managed device.
                ''',
                'cefcfgtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFESelectionTable', REFERENCE_CLASS, 'Ceffeselectiontable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceffeselectiontable', 
                [], [], 
                '''                A list of forwarding element selection entries.
                ''',
                'ceffeselectiontable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFIB', REFERENCE_CLASS, 'Ceffib' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceffib', 
                [], [], 
                '''                ''',
                'ceffib',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefFIBSummaryTable', REFERENCE_CLASS, 'Ceffibsummarytable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceffibsummarytable', 
                [], [], 
                '''                This table contains the summary information
                for the cefPrefixTable.
                ''',
                'ceffibsummarytable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefInconsistencyRecordTable', REFERENCE_CLASS, 'Cefinconsistencyrecordtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinconsistencyrecordtable', 
                [], [], 
                '''                This table contains CEF inconsistency
                records.
                ''',
                'cefinconsistencyrecordtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefIntTable', REFERENCE_CLASS, 'Cefinttable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefinttable', 
                [], [], 
                '''                This Table contains interface specific
                information of CEF on the Managed
                device.
                ''',
                'cefinttable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefLMPrefixTable', REFERENCE_CLASS, 'Ceflmprefixtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Ceflmprefixtable', 
                [], [], 
                '''                A table of Longest Match Prefix Query requests.
                
                Generator application should utilize the
                cefLMPrefixSpinLock to try to avoid collisions.
                See DESCRIPTION clause of cefLMPrefixSpinLock.
                ''',
                'ceflmprefixtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefNotifCntl', REFERENCE_CLASS, 'Cefnotifcntl' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefnotifcntl', 
                [], [], 
                '''                ''',
                'cefnotifcntl',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPathTable', REFERENCE_CLASS, 'Cefpathtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpathtable', 
                [], [], 
                '''                CEF prefix path is a valid route to reach to a 
                destination IP prefix. Multiple paths may exist 
                out of a router to the same destination prefix. 
                This table specify lists of CEF paths.
                ''',
                'cefpathtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPeerFIBTable', REFERENCE_CLASS, 'Cefpeerfibtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpeerfibtable', 
                [], [], 
                '''                Entity acting as RP (Routing Processor) keep
                the CEF FIB states for the line card entities and
                communicate with the line card entities using
                XDR. This Table contains the CEF FIB State 
                related to peer entities on the managed device.
                ''',
                'cefpeerfibtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPeerTable', REFERENCE_CLASS, 'Cefpeertable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefpeertable', 
                [], [], 
                '''                Entity acting as RP (Routing Processor) keeps
                the CEF states for the line card entities and
                communicates with the line card entities using
                XDR. This Table contains the CEF information 
                related to peer entities on the managed device.
                ''',
                'cefpeertable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefPrefixTable', REFERENCE_CLASS, 'Cefprefixtable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefprefixtable', 
                [], [], 
                '''                A list of CEF forwarding prefixes.
                ''',
                'cefprefixtable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefResourceTable', REFERENCE_CLASS, 'Cefresourcetable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefresourcetable', 
                [], [], 
                '''                This table contains global resource 
                information of CEF on the Managed device.
                ''',
                'cefresourcetable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefStatsPrefixLenTable', REFERENCE_CLASS, 'Cefstatsprefixlentable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefstatsprefixlentable', 
                [], [], 
                '''                This table specifies the CEF stats based
                on the Prefix Length.
                ''',
                'cefstatsprefixlentable',
                'CISCO-CEF-MIB', False),
            _MetaInfoClassMember('cefSwitchingStatsTable', REFERENCE_CLASS, 'Cefswitchingstatstable' , 'ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CiscoCefMib.Cefswitchingstatstable', 
                [], [], 
                '''                This table specifies the CEF switch stats.
                ''',
                'cefswitchingstatstable',
                'CISCO-CEF-MIB', False),
            ],
            'CISCO-CEF-MIB',
            'CISCO-CEF-MIB',
            _yang_ns._namespaces['CISCO-CEF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CEF_MIB'
        ),
    },
}
_meta_table['CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry']['meta_info'].parent =_meta_table['CiscoCefMib.Ceffibsummarytable']['meta_info']
_meta_table['CiscoCefMib.Cefprefixtable.Cefprefixentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefprefixtable']['meta_info']
_meta_table['CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry']['meta_info'].parent =_meta_table['CiscoCefMib.Ceflmprefixtable']['meta_info']
_meta_table['CiscoCefMib.Cefpathtable.Cefpathentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefpathtable']['meta_info']
_meta_table['CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefadjsummarytable']['meta_info']
_meta_table['CiscoCefMib.Cefadjtable.Cefadjentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefadjtable']['meta_info']
_meta_table['CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry']['meta_info'].parent =_meta_table['CiscoCefMib.Ceffeselectiontable']['meta_info']
_meta_table['CiscoCefMib.Cefcfgtable.Cefcfgentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefcfgtable']['meta_info']
_meta_table['CiscoCefMib.Cefresourcetable.Cefresourceentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefresourcetable']['meta_info']
_meta_table['CiscoCefMib.Cefinttable.Cefintentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefinttable']['meta_info']
_meta_table['CiscoCefMib.Cefpeertable.Cefpeerentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefpeertable']['meta_info']
_meta_table['CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefpeerfibtable']['meta_info']
_meta_table['CiscoCefMib.Cefccglobaltable.Cefccglobalentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefccglobaltable']['meta_info']
_meta_table['CiscoCefMib.Cefcctypetable.Cefcctypeentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefcctypetable']['meta_info']
_meta_table['CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefinconsistencyrecordtable']['meta_info']
_meta_table['CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefstatsprefixlentable']['meta_info']
_meta_table['CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry']['meta_info'].parent =_meta_table['CiscoCefMib.Cefswitchingstatstable']['meta_info']
_meta_table['CiscoCefMib.Ceffib']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefcc']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefnotifcntl']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Ceffibsummarytable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefprefixtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Ceflmprefixtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefpathtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefadjsummarytable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefadjtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Ceffeselectiontable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefcfgtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefresourcetable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefinttable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefpeertable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefpeerfibtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefccglobaltable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefcctypetable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefinconsistencyrecordtable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefstatsprefixlentable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
_meta_table['CiscoCefMib.Cefswitchingstatstable']['meta_info'].parent =_meta_table['CiscoCefMib']['meta_info']
