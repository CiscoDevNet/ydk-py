


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CiscoNetsyncESMCCap_Enum' : _MetaInfoEnum('CiscoNetsyncESMCCap_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncESMCCapNone':'NETSYNCESMCCAPNONE',
            'netsyncESMCCapTxRx':'NETSYNCESMCCAPTXRX',
            'netsyncESMCCapTx':'NETSYNCESMCCAPTX',
            'netsyncESMCCapRx':'NETSYNCESMCCAPRX',
            'netsyncESMCCapInvalid':'NETSYNCESMCCAPINVALID',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncQLMode_Enum' : _MetaInfoEnum('CiscoNetsyncQLMode_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncQLModeUnknown':'NETSYNCQLMODEUNKNOWN',
            'netsyncQLModeQlDisabled':'NETSYNCQLMODEQLDISABLED',
            'netsyncQLModeQlEnabled':'NETSYNCQLMODEQLENABLED',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncQualityLevel_Enum' : _MetaInfoEnum('CiscoNetsyncQualityLevel_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncQualityLevelNULL':'NETSYNCQUALITYLEVELNULL',
            'netsyncQualityLevelDNU':'NETSYNCQUALITYLEVELDNU',
            'netsyncQualityLevelDUS':'NETSYNCQUALITYLEVELDUS',
            'netsyncQualityLevelFAILED':'NETSYNCQUALITYLEVELFAILED',
            'netsyncQualityLevelINV0':'NETSYNCQUALITYLEVELINV0',
            'netsyncQualityLevelINV1':'NETSYNCQUALITYLEVELINV1',
            'netsyncQualityLevelINV2':'NETSYNCQUALITYLEVELINV2',
            'netsyncQualityLevelINV3':'NETSYNCQUALITYLEVELINV3',
            'netsyncQualityLevelINV4':'NETSYNCQUALITYLEVELINV4',
            'netsyncQualityLevelINV5':'NETSYNCQUALITYLEVELINV5',
            'netsyncQualityLevelINV6':'NETSYNCQUALITYLEVELINV6',
            'netsyncQualityLevelINV7':'NETSYNCQUALITYLEVELINV7',
            'netsyncQualityLevelINV8':'NETSYNCQUALITYLEVELINV8',
            'netsyncQualityLevelINV9':'NETSYNCQUALITYLEVELINV9',
            'netsyncQualityLevelINV10':'NETSYNCQUALITYLEVELINV10',
            'netsyncQualityLevelINV11':'NETSYNCQUALITYLEVELINV11',
            'netsyncQualityLevelINV12':'NETSYNCQUALITYLEVELINV12',
            'netsyncQualityLevelINV13':'NETSYNCQUALITYLEVELINV13',
            'netsyncQualityLevelINV14':'NETSYNCQUALITYLEVELINV14',
            'netsyncQualityLevelINV15':'NETSYNCQUALITYLEVELINV15',
            'netsyncQualityLevelNSUPP':'NETSYNCQUALITYLEVELNSUPP',
            'netsyncQualityLevelPRC':'NETSYNCQUALITYLEVELPRC',
            'netsyncQualityLevelPROV':'NETSYNCQUALITYLEVELPROV',
            'netsyncQualityLevelPRS':'NETSYNCQUALITYLEVELPRS',
            'netsyncQualityLevelSEC':'NETSYNCQUALITYLEVELSEC',
            'netsyncQualityLevelSMC':'NETSYNCQUALITYLEVELSMC',
            'netsyncQualityLevelSSUA':'NETSYNCQUALITYLEVELSSUA',
            'netsyncQualityLevelSSUB':'NETSYNCQUALITYLEVELSSUB',
            'netsyncQualityLevelST2':'NETSYNCQUALITYLEVELST2',
            'netsyncQualityLevelST3':'NETSYNCQUALITYLEVELST3',
            'netsyncQualityLevelST3E':'NETSYNCQUALITYLEVELST3E',
            'netsyncQualityLevelST4':'NETSYNCQUALITYLEVELST4',
            'netsyncQualityLevelSTU':'NETSYNCQUALITYLEVELSTU',
            'netsyncQualityLevelTNC':'NETSYNCQUALITYLEVELTNC',
            'netsyncQualityLevelUNC':'NETSYNCQUALITYLEVELUNC',
            'netsyncQualityLevelUNK':'NETSYNCQUALITYLEVELUNK',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncClockMode_Enum' : _MetaInfoEnum('CiscoNetsyncClockMode_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncClockModeUnknown':'NETSYNCCLOCKMODEUNKNOWN',
            'netsyncClockModeFreerun':'NETSYNCCLOCKMODEFREERUN',
            'netsyncClockModeHoldover':'NETSYNCCLOCKMODEHOLDOVER',
            'netsyncClockModeLocked':'NETSYNCCLOCKMODELOCKED',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncSSMCap_Enum' : _MetaInfoEnum('CiscoNetsyncSSMCap_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncSSMCapNone':'NETSYNCSSMCAPNONE',
            'netsyncSSMCapTxRx':'NETSYNCSSMCAPTXRX',
            'netsyncSSMCapTx':'NETSYNCSSMCAPTX',
            'netsyncSSMCapRx':'NETSYNCSSMCAPRX',
            'netsyncSSMCapInvalid':'NETSYNCSSMCAPINVALID',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncIfType_Enum' : _MetaInfoEnum('CiscoNetsyncIfType_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncIfTypeUnknown':'NETSYNCIFTYPEUNKNOWN',
            'netsyncIfTypeInternal':'NETSYNCIFTYPEINTERNAL',
            'netsyncIfTypeEthernet':'NETSYNCIFTYPEETHERNET',
            'netsyncIfTypeSonet':'NETSYNCIFTYPESONET',
            'netsyncIfTypeTop':'NETSYNCIFTYPETOP',
            'netsyncIfTypeExt':'NETSYNCIFTYPEEXT',
            'netsyncIfTypeController':'NETSYNCIFTYPECONTROLLER',
            'netsyncIfTypeGps':'NETSYNCIFTYPEGPS',
            'netsyncIfTypeAtm':'NETSYNCIFTYPEATM',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncNetworkOption_Enum' : _MetaInfoEnum('CiscoNetsyncNetworkOption_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncNetworkOptionUnknown':'NETSYNCNETWORKOPTIONUNKNOWN',
            'netsyncNetworkOption1':'NETSYNCNETWORKOPTION1',
            'netsyncNetworkOption2Gen1':'NETSYNCNETWORKOPTION2GEN1',
            'netsyncNetworkOption2Gen2':'NETSYNCNETWORKOPTION2GEN2',
            'netsyncNetworkOption3':'NETSYNCNETWORKOPTION3',
            'netsyncNetworkOptionInvalid':'NETSYNCNETWORKOPTIONINVALID',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CiscoNetsyncEECOption_Enum' : _MetaInfoEnum('CiscoNetsyncEECOption_Enum', 'ydk.models.netsync.CISCO_NETSYNC_MIB',
        {
            'netsyncEECOptionUnknown':'NETSYNCEECOPTIONUNKNOWN',
            'netsyncEECOption1':'NETSYNCEECOPTION1',
            'netsyncEECOption2':'NETSYNCEECOPTION2',
            'netsyncEECOptionInvalid':'NETSYNCEECOPTIONINVALID',
        }, 'CISCO-NETSYNC-MIB', _yang_ns._namespaces['CISCO-NETSYNC-MIB']),
    'CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl',
            False, 
            [
            _MetaInfoClassMember('cnsMIBEnableStatusNotification', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A control object to enable/disable
                ciscoNetsyncSelectedT0Clock, ciscoNetsyncSelectedT4Clock,
                ciscoNetsyncInputSignalFailureStatus,
                ciscoNetsyncInputAlarmStatus notifications at the system
                level.
                This object should hold any of the below values.
                    true - The notif is enabled globally for the system
                    false- The notif is disabled globally for the system
                ''',
                'cnsmibenablestatusnotification',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'ciscoNetsyncMIBNotifControl',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsClkSelGlobalTable.CnsClkSelGlobalEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsClkSelGlobalTable.CnsClkSelGlobalEntry',
            False, 
            [
            _MetaInfoClassMember('cnsClkSelGloProcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An index that uniquely represents a clock selection process.
                
                This index is assigned arbitrarily by the system
                and may not be persistent across reboots.
                ''',
                'cnsclkselgloprocindex',
                'CISCO-NETSYNC-MIB', True),
            _MetaInfoClassMember('cnsClkSelGlobClockMode', REFERENCE_ENUM_CLASS, 'CiscoNetsyncClockMode_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncClockMode_Enum', 
                [], [], 
                '''                This object indicates the operating mode
                of the system clock.
                ''',
                'cnsclkselglobclockmode',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobCurrHoldoverSeconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the duration of
                the current holdover period.
                If a system clock is in holdover mode,
                the object carries the current holdover
                duration in seconds. If the system clock
                is not in holdover, the object carries
                the value 0.
                ''',
                'cnsclkselglobcurrholdoverseconds',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobEECOption', REFERENCE_ENUM_CLASS, 'CiscoNetsyncEECOption_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncEECOption_Enum', 
                [], [], 
                '''                This object indicates the network synchronization
                EEC (Ethernet Equipment Clock) option.
                ''',
                'cnsclkselglobeecoption',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobESMCMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates if global ESMC is enabled.
                With ESMC enabled globally, the system is capable
                of handling ESMC messages.
                ''',
                'cnsclkselglobesmcmode',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobHoldoffTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the global
                holdoff time in the G.781 clock
                selection process.
                ''',
                'cnsclkselglobholdofftime',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobLastHoldoverSeconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the duration of
                the last holdover period in seconds.
                If the holdover duration is less than a second,
                the object will carry the value zero.
                ''',
                'cnsclkselgloblastholdoverseconds',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobNetsyncEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the G.781
                clock selection is enabled or not.
                
                'true'  - G.781 clock selection is enabled
                'false' - G.781 clock selection is disabled
                ''',
                'cnsclkselglobnetsyncenable',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobNetworkOption', REFERENCE_ENUM_CLASS, 'CiscoNetsyncNetworkOption_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncNetworkOption_Enum', 
                [], [], 
                '''                This object indicates the synchronization
                network option.
                ''',
                'cnsclkselglobnetworkoption',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobNofSources', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                This object indicates the number of
                synchronization sources currently
                configured for the G.781
                clock selection process.
                ''',
                'cnsclkselglobnofsources',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobProcessMode', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQLMode_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQLMode_Enum', 
                [], [], 
                '''                This object indicates the QL mode of
                the network synchronization clock selection
                process as described in ITU-T standard G.781
                section 5.12.
                ''',
                'cnsclkselglobprocessmode',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobRevertiveMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the revertive mode
                setting in the G.781 clock selection process.
                
                The switching of clock sources can be made revertive or
                non-revertive. In non-revertive mode, an alternate
                clock source is maintained even after the original clock
                source has recovered from the failure that caused the switch.
                In revertive mode, the clock selection process switches back
                to the original clock source after recovering from the
                failure.
                ''',
                'cnsclkselglobrevertivemode',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobWtrTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the global
                wait-to-restore time in the G.781
                clock selection process.
                ''',
                'cnsclkselglobwtrtime',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsClkSelGlobalEntry',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsClkSelGlobalTable' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsClkSelGlobalTable',
            False, 
            [
            _MetaInfoClassMember('cnsClkSelGlobalEntry', REFERENCE_LIST, 'CnsClkSelGlobalEntry' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsClkSelGlobalTable.CnsClkSelGlobalEntry', 
                [], [], 
                '''                An entry is added to cnsClkSelGlobalTable when G.781 clock
                selection is enabled in the device configuration.  The entry
                is removed when G.781 clock selection is removed from the
                configuration.
                ''',
                'cnsclkselglobalentry',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsClkSelGlobalTable',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsExtOutputTable.CnsExtOutputEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsExtOutputTable.CnsExtOutputEntry',
            False, 
            [
            _MetaInfoClassMember('cnsExtOutListIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely represents an entry in
                this table.  This index is assigned arbitrarily by the
                clock selection process and may not be persistent
                across reboots.
                ''',
                'cnsextoutlistindex',
                'CISCO-NETSYNC-MIB', True),
            _MetaInfoClassMember('cnsExtOutFSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the forced switching flag.
                Forced switching, as described in G.781, is used to
                override the currently selected synchronization source,
                The T4 selected synchronization source is identified by
                cnsExtOutSelNetsyncIndex, which contains the index to
                the clock source in cnsT4ClockSourceTable.
                
                The 'true' value indicates the currently selected
                T4 clock source is a result of the forced switching.
                The 'false' value indicates the currently selected T4
                clock source is not a result of forced switching.
                ''',
                'cnsextoutfsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutIntfType', REFERENCE_ENUM_CLASS, 'CiscoNetsyncIfType_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncIfType_Enum', 
                [], [], 
                '''                This object indicates the interface type
                of the T4 external output.
                ''',
                'cnsextoutintftype',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutMSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the manual switching flag.
                
                The 'true' value indicates the currently selected
                T4 clock source is a result of the manual switch command.
                The command allows a user to select a synchronization source
                assuming it is enabled, not locked out, not in signal fail
                condition, and has a QL better than DNU in QL-enabled mode.
                
                A clock source is enabled when it occupies in row in
                cnsT4ClockSourceTable.  A clock source is not locked out
                when cnsT4ClkSrcLockout contains the value 'false'.
                A clock source is not in signal failure condition when
                cnsT4ClkSrcSignalFailure contains the value 'false'. 
                The QL is identified in cnsT4ClkSrcQualityLevel.
                
                In QL-enabled mode, a manual switch can be 
                performed only to a source which has the highest
                available QL.
                ''',
                'cnsextoutmsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object indicates the name of a
                T4 external output.
                ''',
                'cnsextoutname',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutPriority', ATTRIBUTE, 'int' , None, None, 
                [(1, 1024)], [], 
                '''                This object indicates the priority of the
                selected clock source for a T4 external
                output.
                
                A smaller value represents a higher priority.
                ''',
                'cnsextoutpriority',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutQualityLevel', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the clock quality
                of the T4 external output.
                ''',
                'cnsextoutqualitylevel',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutSelNetsyncIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely represents the selected input clock
                source whose information is reported by a row in
                cnsT4ClockSourceTable. The index lists the value of
                cnsT4ClkSrcNetsyncIndex, which is the input clock source
                of the T4 external output selected by the G.781 clock
                selection process.
                ''',
                'cnsextoutselnetsyncindex',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutSquelch', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not a
                T4 external output is squelched.
                
                Squelching is a sychronization function defined to prevent
                transmission of a timing signal with a quality that is lower
                than the quality of the clock in the receiving networks
                element or SASE. It is also used for the prevention of
                timing loops.
                ''',
                'cnsextoutsquelch',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsExtOutputEntry',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsExtOutputTable' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsExtOutputTable',
            False, 
            [
            _MetaInfoClassMember('cnsExtOutputEntry', REFERENCE_LIST, 'CnsExtOutputEntry' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsExtOutputTable.CnsExtOutputEntry', 
                [], [], 
                '''                An entry is created in the table when a user adds
                a T4 external output in the configuration.  A T4 external
                output configured input clock sources are defined in
                cnsT4ClockSourceTable.
                
                An entry is removed from the table when a user removes
                a T4 external output from the configuration.
                ''',
                'cnsextoutputentry',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsExtOutputTable',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsInputSourceTable.CnsInputSourceEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsInputSourceTable.CnsInputSourceEntry',
            False, 
            [
            _MetaInfoClassMember('cnsInpSrcNetsyncIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely represents an entry in
                this table. This index is assigned arbitrarily
                by the clock selection process and may not be persistent
                across reboots.
                ''',
                'cnsinpsrcnetsyncindex',
                'CISCO-NETSYNC-MIB', True),
            _MetaInfoClassMember('cnsInpSrcAlarm', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not an
                alarm event is currently being reported
                on the input clock source.
                ''',
                'cnsinpsrcalarm',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcAlarmInfo', REFERENCE_BITS, 'CiscoNetsyncAlarmInfo_Bits' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncAlarmInfo_Bits', 
                [], [], 
                '''                This object indicates the alarm reasons of
                an input clock source if an alarm event
                is being reported on it.
                ''',
                'cnsinpsrcalarminfo',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcESMCCap', REFERENCE_ENUM_CLASS, 'CiscoNetsyncESMCCap_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncESMCCap_Enum', 
                [], [], 
                '''                This object indicates the ESMC capability
                of an input clock source configured for the
                T0 clock selection.  This is applicable only to Synchronous
                Ethernet input clock source identified by cnsInpSrcIntfType
                'netsyncIfTypeEthernet'.
                ''',
                'cnsinpsrcesmccap',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcFSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the forced switching flag.
                Forced switching, as described in G.781, is used to
                override the currently selected synchronization source.
                
                The 'true' value indicates the currently selected clock source
                is a result of the forced switching. The 'false' value
                indicates the currently selected clock source is not a result
                of forced switching.
                ''',
                'cnsinpsrcfsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcHoldoffTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the hold-off time value of
                an input clock source.
                
                The hold-off time prevents short activation of signal failure
                is passed to the selection process.  When a signal failure
                event is reported on a clock source, it waits the duration of
                the hold-off time before declaring signal failure on the clock
                source.
                ''',
                'cnsinpsrcholdofftime',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcIntfType', REFERENCE_ENUM_CLASS, 'CiscoNetsyncIfType_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncIfType_Enum', 
                [], [], 
                '''                This object indicates the type of an input
                clock source configured for the T0 clock
                selection.
                ''',
                'cnsinpsrcintftype',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcLockout', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not the lockout
                command has been applied to a clock source.
                
                The 'true' value means the clock source is not
                considered by the selection process.
                ''',
                'cnsinpsrclockout',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcMSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the manual switching flag.
                
                The 'true' value indicates the currently selected clock source
                is a result of the manual switching. The switch allows
                a user to select a synchronization source assuming it is
                enabled, not locked out, not in signal fail condition,
                and has a QL better than DNU in QL-enabled mode.
                
                A clock source is enabled when it occupies a row in
                cnsInputSourceTable.  A clock source is not locked out
                when cnsInpSrcLockout contains the value 'false'.
                A clock source is not in signal failure condition when
                cnsInpSrcSignalFailure contains the value 'false'. 
                The QL is identified in cnsInpSrcQualityLevel.
                
                In QL-enabled mode, a manual switch can be performed only to
                a source which has the highest available QL.
                ''',
                'cnsinpsrcmsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object indicates the name of an input
                clock source configured for the T0 clock
                selection.
                ''',
                'cnsinpsrcname',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcPriority', ATTRIBUTE, 'int' , None, None, 
                [(1, 1024)], [], 
                '''                This object indicates the priority of an input
                clock source configured for the T0 clock
                selection.
                
                A smaller value represents a higher priority.
                ''',
                'cnsinpsrcpriority',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcQualityLevel', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the current clock quality
                level of the input clock source.  This is the
                effective quality which is derived from three values:
                
                1) most recent clock quality level received,
                2) forced clock quality level (entered via configuration)
                3) overridden clock quality level as a result of line protocol
                down, signal failure, or alarms.
                ''',
                'cnsinpsrcqualitylevel',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcQualityLevelRx', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the last clock quality
                level received on the input clock source.
                ''',
                'cnsinpsrcqualitylevelrx',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcQualityLevelRxCfg', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the configured receive
                clock quality level of an input clock source.
                ''',
                'cnsinpsrcqualitylevelrxcfg',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcQualityLevelTx', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the most recent clock
                quality level transmitted on the input clock
                source.
                ''',
                'cnsinpsrcqualityleveltx',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcQualityLevelTxCfg', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the configured transmit
                clock quality level of an input clock source.
                ''',
                'cnsinpsrcqualityleveltxcfg',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcSignalFailure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not a
                signal failure event is currently being
                reported on the input clock source.
                ''',
                'cnsinpsrcsignalfailure',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcSSMCap', REFERENCE_ENUM_CLASS, 'CiscoNetsyncSSMCap_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncSSMCap_Enum', 
                [], [], 
                '''                This object indicates the SSM capability
                of an input clock source configured for the
                T0 clock selection. This is applicable only to
                any synchronous interface clock source except
                SyncE interface, which is identified by cnsInpSrcIntfType
                'netsyncIfTypeEthernet'.
                ''',
                'cnsinpsrcssmcap',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInpSrcWtrTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the wait-to-restore time value
                of an input clock source.
                
                The wait-to-restore time ensures that a previous failed
                synchronization source is only again considered as available
                by the selection process if it is fault-free for a certain time.
                When a signal failure condition is cleared on a clock source,
                it waits the duration of the wait-to-restore time before
                clearing the signal failure status on the clock source.
                ''',
                'cnsinpsrcwtrtime',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsInputSourceEntry',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsInputSourceTable' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsInputSourceTable',
            False, 
            [
            _MetaInfoClassMember('cnsInputSourceEntry', REFERENCE_LIST, 'CnsInputSourceEntry' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsInputSourceTable.CnsInputSourceEntry', 
                [], [], 
                '''                An entry is created in the table when a user adds a T0
                clock source in the configuration. An entry is removed 
                in the table when a user removes a T0 clock source from
                the configuration.
                ''',
                'cnsinputsourceentry',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsInputSourceTable',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsSelectedInputSourceTable.CnsSelectedInputSourceEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsSelectedInputSourceTable.CnsSelectedInputSourceEntry',
            False, 
            [
            _MetaInfoClassMember('cnsSelInpSrcNetsyncIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely represents an entry in
                this table. This index is assigned arbitrarily
                by the clock selection process and may not be persistent
                across reboots.
                ''',
                'cnsselinpsrcnetsyncindex',
                'CISCO-NETSYNC-MIB', True),
            _MetaInfoClassMember('cnsSelInpSrcFSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the forced switching flag. Forced
                switching, as described in G.781, is used to override the
                currently selected synchronization source.
                
                The 'true' value indicates the currently selected clock
                source is a result of the forced switching. The 'false'
                value indicates the currently selected clock source is
                not a result of forced switching.
                ''',
                'cnsselinpsrcfsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelInpSrcIntfType', REFERENCE_ENUM_CLASS, 'CiscoNetsyncIfType_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncIfType_Enum', 
                [], [], 
                '''                This object indicates the type of the
                selected T0 clock.
                ''',
                'cnsselinpsrcintftype',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelInpSrcMSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the manual switching flag.
                The 'true' value indicates the currently selected clock source
                is a result of the manual switch command. The command allows
                a user to select a synchronization source assuming it is
                enabled, not locked out, not in signal fail condition,
                and has a QL better than DNU in QL-enabled mode. Furthermore,
                in QL-enabled mode, a manual switch can be performed only to
                a source which has the highest available QL.
                ''',
                'cnsselinpsrcmsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelInpSrcName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object indicates the name of the
                selected T0 clock.
                ''',
                'cnsselinpsrcname',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelInpSrcPriority', ATTRIBUTE, 'int' , None, None, 
                [(1, 1024)], [], 
                '''                This object indicates the configured
                priority of the selected T0 clock.
                A smaller value represents a higher priority.
                ''',
                'cnsselinpsrcpriority',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelInpSrcQualityLevel', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the selected T0 clock
                source's effective quality level, which
                is the derived clock quality based on the three factors: 
                (a) Received quality level. 
                (b) Configured Rx quality level.  This factor supersedes (a). 
                (c) System overridden quality level as a result of exceptional
                events such as signal failure or ESMC failure.  This factor
                supersedes (a) and (b).
                ''',
                'cnsselinpsrcqualitylevel',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelInpSrcTimestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the timestamp of
                the T0 clock source being selected by
                the G.781 clock selection process.
                ''',
                'cnsselinpsrctimestamp',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsSelectedInputSourceEntry',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsSelectedInputSourceTable' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsSelectedInputSourceTable',
            False, 
            [
            _MetaInfoClassMember('cnsSelectedInputSourceEntry', REFERENCE_LIST, 'CnsSelectedInputSourceEntry' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsSelectedInputSourceTable.CnsSelectedInputSourceEntry', 
                [], [], 
                '''                An entry is created in the table when the G.781 clock
                selection process has successfully selected a T0 clock
                source.  The entry shall remain during the time
                the G.781 clock selection process remains enabled.
                ''',
                'cnsselectedinputsourceentry',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsSelectedInputSourceTable',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsT4ClockSourceTable.CnsT4ClockSourceEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsT4ClockSourceTable.CnsT4ClockSourceEntry',
            False, 
            [
            _MetaInfoClassMember('cnsExtOutListIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cnsextoutlistindex',
                'CISCO-NETSYNC-MIB', True),
            _MetaInfoClassMember('cnsT4ClkSrcNetsyncIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely represents an entry in
                this table.  This index is assigned arbitrarily by the
                clock selection process and may not be persistent
                across reboots.
                ''',
                'cnst4clksrcnetsyncindex',
                'CISCO-NETSYNC-MIB', True),
            _MetaInfoClassMember('cnsT4ClkSrcAlarm', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not an
                alarm event is currently being reported
                on the T4 input clock source.
                ''',
                'cnst4clksrcalarm',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcAlarmInfo', REFERENCE_BITS, 'CiscoNetsyncAlarmInfo_Bits' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncAlarmInfo_Bits', 
                [], [], 
                '''                This object indicates the alarm reasons of
                a T4 input clock source if an alarm event
                is being reported on the clock source.
                ''',
                'cnst4clksrcalarminfo',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcESMCCap', REFERENCE_ENUM_CLASS, 'CiscoNetsyncESMCCap_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncESMCCap_Enum', 
                [], [], 
                '''                This object indicates the ESMC capability
                of an input clock source configured for the
                T4 clock selection.  This is applicable
                only to Synchronous Ethernet input clock source
                identified by cnsT4ClkSrcIntfType 'netsyncIfTypeEthernet'.
                ''',
                'cnst4clksrcesmccap',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcFSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the forced switching flag.
                Forced switching, as described in G.781, is used to
                override the currently selected synchronization source.
                
                The 'true' value indicates the currently selected
                T4 clock source is a result of the forced switching.
                The 'false' value indicates the currently selected
                T4 clock source is not a result of forced switching.
                ''',
                'cnst4clksrcfsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcHoldoffTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the hold-off time value of
                a T4 input clock source.
                
                The hold-off time prevents short activation of signal failure
                is passed to the selection process.  When a signal failure
                event is reported on a clock source, it waits the duration of
                the hold-off time before declaring signal failure on the clock
                source.
                ''',
                'cnst4clksrcholdofftime',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcIntfType', REFERENCE_ENUM_CLASS, 'CiscoNetsyncIfType_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncIfType_Enum', 
                [], [], 
                '''                This object indicates the type of an input
                clock source configured for the T4 clock
                selection.
                ''',
                'cnst4clksrcintftype',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcLockout', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not the lockout
                command has been applied on a T4 clock source.
                
                The 'true' value means the clock source is not
                considered by the selection process.
                ''',
                'cnst4clksrclockout',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcMSW', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates the manual switching flag.
                
                The 'true' value indicates the currently selected
                T4 clock source is a result of the manual switching.
                The switch allows a user to select a 
                synchronization source assuming it is enabled,
                not locked out, not in signal fail condition,
                and has a QL better than DNU in QL-enabled mode.
                
                A clock source is enabled when it occupies a row in 
                cnsT4ClockSourceTable.  A clock source is not locked
                out when cnsT4ClkSrcLockout contains the value 'false'.
                A clock source is not in signal failure condition when
                cnsT4ClkSrcSignalFailure contains the value 'false'.
                The QL is identified in cnsT4ClkSrcQualityLevel.
                
                In QL-enabled mode, a manual switch
                can be performed only to a source which has the
                highest available QL.
                ''',
                'cnst4clksrcmsw',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object indicates the name of a input
                clock source configured for the T4 clock
                selection.
                ''',
                'cnst4clksrcname',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcPriority', ATTRIBUTE, 'int' , None, None, 
                [(1, 1024)], [], 
                '''                This object indicates the priority of an input
                clock source configured for the T4 clock
                selection.
                
                A smaller value represents a higher priority.
                ''',
                'cnst4clksrcpriority',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcQualityLevel', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the current clock quality
                level of the T4 input clock source.  This is the
                effective quality which is derived from three values:
                
                1) most recent clock quality level received,
                2) forced clock quality level (entered via configuration)
                3) overridden clock quality level as a result of line protocol
                down, signal failure, or alarms.
                ''',
                'cnst4clksrcqualitylevel',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcQualityLevelRx', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the last clock quality
                level received on the T4 input clock
                source.
                ''',
                'cnst4clksrcqualitylevelrx',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcQualityLevelRxCfg', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the configured receive
                clock quality level of a T4 input clock source.
                ''',
                'cnst4clksrcqualitylevelrxcfg',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcQualityLevelTx', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the most recent clock
                quality level transmitted on the T4 input
                clock source.
                ''',
                'cnst4clksrcqualityleveltx',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcQualityLevelTxCfg', REFERENCE_ENUM_CLASS, 'CiscoNetsyncQualityLevel_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncQualityLevel_Enum', 
                [], [], 
                '''                This object indicates the configured transmit
                clock quality level of a T4 input clock source.
                ''',
                'cnst4clksrcqualityleveltxcfg',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcSignalFailure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not a
                signal failure event is currently being
                reported on the T4 input clock source.
                ''',
                'cnst4clksrcsignalfailure',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcSSMCap', REFERENCE_ENUM_CLASS, 'CiscoNetsyncSSMCap_Enum' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CiscoNetsyncSSMCap_Enum', 
                [], [], 
                '''                This object indicates the SSM capability
                of an input clock source configured for the
                T4 clock selection. This is applicable only to any
                synchronous interface clock source except SyncE interface,
                which is identified by cnsT4ClkSrcIntfType
                'netsyncIfTypeEthernet'.
                ''',
                'cnst4clksrcssmcap',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClkSrcWtrTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the wait-to-restore time value
                of a T4 input clock source.
                
                The wait-to-restore time ensures that a previous failed
                synchronization source is only again considered as available
                by the selection process if it is fault-free for a certain time.
                When a signal failure condition is cleared on a clock source,
                it waits the duration of the wait-to-restore time before
                clearing the signal failure status on the clock source.
                ''',
                'cnst4clksrcwtrtime',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsT4ClockSourceEntry',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB.CnsT4ClockSourceTable' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB.CnsT4ClockSourceTable',
            False, 
            [
            _MetaInfoClassMember('cnsT4ClockSourceEntry', REFERENCE_LIST, 'CnsT4ClockSourceEntry' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsT4ClockSourceTable.CnsT4ClockSourceEntry', 
                [], [], 
                '''                An entry is created in the table when a user adds a
                clock source to a T4 external output in the configuration.
                The T4 external output is defined in the T4 external
                output table. An entry is removed in the table when a user
                removes a T4 clock source from the configuration.
                ''',
                'cnst4clocksourceentry',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'cnsT4ClockSourceTable',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
    'CISCONETSYNCMIB' : {
        'meta_info' : _MetaInfoClass('CISCONETSYNCMIB',
            False, 
            [
            _MetaInfoClassMember('ciscoNetsyncMIBNotifControl', REFERENCE_CLASS, 'CiscoNetsyncMIBNotifControl' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl', 
                [], [], 
                '''                ''',
                'cisconetsyncmibnotifcontrol',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsClkSelGlobalTable', REFERENCE_CLASS, 'CnsClkSelGlobalTable' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsClkSelGlobalTable', 
                [], [], 
                '''                G.781 clock selection process table.
                This table contains the global parameters for the G.781 clock
                selection process.
                ''',
                'cnsclkselglobaltable',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsExtOutputTable', REFERENCE_CLASS, 'CnsExtOutputTable' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsExtOutputTable', 
                [], [], 
                '''                T4 external output table.
                This table contains a list of T4 external outputs.
                
                Each T4 external output is associated with clock
                source(s) to be found in cnsT4ClockSourceTable.
                The clock selection process considers all the
                available clock sources and select the T4 clock
                source based on the G.781 clock selection algorithm.
                ''',
                'cnsextoutputtable',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsInputSourceTable', REFERENCE_CLASS, 'CnsInputSourceTable' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsInputSourceTable', 
                [], [], 
                '''                T0 clock source table.
                This table contains a list of input sources for input T0 clock
                selection.
                ''',
                'cnsinputsourcetable',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsSelectedInputSourceTable', REFERENCE_CLASS, 'CnsSelectedInputSourceTable' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsSelectedInputSourceTable', 
                [], [], 
                '''                T0 selected clock source table.
                This table contains the selected clock source for the input T0
                clock.
                ''',
                'cnsselectedinputsourcetable',
                'CISCO-NETSYNC-MIB', False),
            _MetaInfoClassMember('cnsT4ClockSourceTable', REFERENCE_CLASS, 'CnsT4ClockSourceTable' , 'ydk.models.netsync.CISCO_NETSYNC_MIB', 'CISCONETSYNCMIB.CnsT4ClockSourceTable', 
                [], [], 
                '''                T4 clock source table.
                This table contains a list of input sources for a specific
                T4 external output. An entry shall be added to
                cnsExtOutputTable first. Then clock sources shall be
                added in this table for the selection process to select
                the appropriate T4 clock source.
                ''',
                'cnst4clocksourcetable',
                'CISCO-NETSYNC-MIB', False),
            ],
            'CISCO-NETSYNC-MIB',
            'CISCO-NETSYNC-MIB',
            _yang_ns._namespaces['CISCO-NETSYNC-MIB'],
        'ydk.models.netsync.CISCO_NETSYNC_MIB'
        ),
    },
}
_meta_table['CISCONETSYNCMIB.CnsClkSelGlobalTable.CnsClkSelGlobalEntry']['meta_info'].parent =_meta_table['CISCONETSYNCMIB.CnsClkSelGlobalTable']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsExtOutputTable.CnsExtOutputEntry']['meta_info'].parent =_meta_table['CISCONETSYNCMIB.CnsExtOutputTable']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsInputSourceTable.CnsInputSourceEntry']['meta_info'].parent =_meta_table['CISCONETSYNCMIB.CnsInputSourceTable']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsSelectedInputSourceTable.CnsSelectedInputSourceEntry']['meta_info'].parent =_meta_table['CISCONETSYNCMIB.CnsSelectedInputSourceTable']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsT4ClockSourceTable.CnsT4ClockSourceEntry']['meta_info'].parent =_meta_table['CISCONETSYNCMIB.CnsT4ClockSourceTable']['meta_info']
_meta_table['CISCONETSYNCMIB.CiscoNetsyncMIBNotifControl']['meta_info'].parent =_meta_table['CISCONETSYNCMIB']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsClkSelGlobalTable']['meta_info'].parent =_meta_table['CISCONETSYNCMIB']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsExtOutputTable']['meta_info'].parent =_meta_table['CISCONETSYNCMIB']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsInputSourceTable']['meta_info'].parent =_meta_table['CISCONETSYNCMIB']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsSelectedInputSourceTable']['meta_info'].parent =_meta_table['CISCONETSYNCMIB']['meta_info']
_meta_table['CISCONETSYNCMIB.CnsT4ClockSourceTable']['meta_info'].parent =_meta_table['CISCONETSYNCMIB']['meta_info']
