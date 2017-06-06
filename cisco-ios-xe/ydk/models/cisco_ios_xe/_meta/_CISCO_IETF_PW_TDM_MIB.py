


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfPwTdmMib.Cpwctdmobjects' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmobjects',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMCfgIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains the value to be used for
                cpwCTDMCfgIndex when creating entries in the
                cpwCTDMCfgTable. The value 0 indicates that no
                unassigned entries are available.  To obtain the
                value of cpwCTDMCfgIndexNext for a new entry in the
                cpwCTDMCfgTable, the manager issues a management
                protocol retrieval operation. The agent will
                determine through its local policy when this
                index value will be made available for reuse.
                ''',
                'cpwctdmcfgindexnext',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMObjects',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCGenTDMCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index to the generic parameters in the TDM configuration
                table that appears in this MIB module. It is likely that
                multiple TDM PWs of the same characteristic will share
                a single TDM Cfg entry.
                ''',
                'cpwcgentdmcfgindex',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCRelTDMCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index to the relevant TDM configuration table entry
                that appears in one of the related MIB modules
                such as TDMoIP or CESoPSN. It is likely that
                multiple TDM PWs of the same characteristic will share
                a single configuration entry of the relevant type.
                The value 0 implies no entry in other related MIB
                ''',
                'cpwcreltdmcfgindex',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMConfigError', REFERENCE_BITS, 'Cpwctdmconfigerror' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmconfigerror', 
                [], [], 
                '''                Any of the bits are set if the local configuration is
                not compatible with the peer configuration as available
                from the various parameters options.
                
                -tdmTypeIncompatible bit is set if the local configuration
                is not carrying the same TDM type as the peer configuration.
                
                -peerRtpIncompatible bit is set if the local configuration
                is configured to send RTP packets for this PW, and the
                remote is not capable of accepting RTP packets.
                
                -peerPayloadSizeIncompatible bit is set if the local
                configuration is not carrying the same Payload Size as the
                peer configuration.
                ''',
                'cpwctdmconfigerror',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCurrentIndications', REFERENCE_BITS, 'Cpwctdmcurrentindications' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmcurrentindications', 
                [], [], 
                '''                The following defects should be detected and reported
                upon request:
                
                -Stray packets MAY be detected by the PSN and multiplexing
                layers. Stray packets MUST be discarded by the CE-bound IWF
                and their detection MUST NOT affect mechanisms for
                detection of packet loss.
                
                -Malformed packets are detected by mismatch between the
                expected packet size (taking the value of the L bit into
                account) and the actual packet size inferred from the PSN
                and multiplexing layers. Malformed in-order packets MUST be
                discarded by the CE-bound IWF and replacement data
                generated as for lost packets.
                
                -Excessive packet loss rate is detected by computing the
                average packet loss rate over the value of
                cpwCTDMAvePktLossTimeWindow and comparing it with a
                preconfigured threshold [SATOP].
                
                -Buffer overrun is detected in the normal operation state
                when the CE bound IWF's jitter buffer cannot accommodate
                newly arrived packets.
                
                -Remote packet loss is indicated by reception of packets 
                with their R bit set.
                
                -Packet misorder is detected by looking at the Sequence
                number provided by the control word.
                
                -TDM Fault, if L bit in the control word is set, it
                indicates that TDM data carried in the payload is invalid
                due an attachment circuit fault.  When the L bit is set the
                payload MAY be omitted in order to conserve bandwidth.
                
                Note: the algorithm used to capture these indications
                is implementation specific.
                ''',
                'cpwctdmcurrentindications',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is a unique index within the ifTable. It represents
                the interface index of the full link or the interface
                index for the bundle holding the group of
                time slots to be transmitted via this PW connection.
                
                A value of zero indicates an interface index that has yet
                to be determined.
                Once set, if the TDM ifIndex is (for some reason) later
                removed, the agent SHOULD delete the associated PW rows
                (e.g., this cpwCTDMTable entry). If the agent does not
                delete the rows,  the agent MUST set this object to
                zero.
                ''',
                'cpwctdmifindex',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMLastEsTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the most recent occasion at
                which the TDM PW entered the ES or SES state.
                ''',
                'cpwctdmlastestimestamp',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMLatchedIndications', REFERENCE_BITS, 'Cpwctdmlatchedindications' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmlatchedindications', 
                [], [], 
                '''                The state of TDM indicators when the TDM PW last declared
                an error second (either as ES, SES or a second with
                errors inside a UAS) condition. At this time, only LOPS
                can create a failure. Since indicators other than LOPS are
                useful, all are latched here. For bit definitions, see
                cpwCTDMCurrentIndications above.
                
                Note: the algorithm used to latch these indications when
                entering a defect state is implementation specific.
                ''',
                'cpwctdmlatchedindications',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMRate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The parameter represents the bit-rate of the TDM service
                in multiples of the 'basic' 64 Kbit/s rate. It complements
                the definition of cpwVcType used in CISCO-IETF-PW-MIB.
                For structure-agnostic the following should be used:
                a) Satop E1 - 32
                b) Satop T1 emulation:
                   i)   MUST be set to 24 in the basic emulation mode
                   ii)  MUST be set to 25 for the 'Octet-aligned T1'
                        emulation mode
                c) Satop E3 - 535
                d) Satop T3 - 699
                For all kinds of structure-aware emulation, this parameter
                MUST be set to N where N is the number of DS0 channels
                in the corresponding attachment circuit.
                ''',
                'cpwctdmrate',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('1', '900')], [], 
                '''                The number of seconds, including partial seconds,
                that have elapsed since the beginning of the current
                measurement period. If, for some reason, such as an
                adjustment in the system's time-of-day clock, the
                current interval exceeds the maximum value, the
                agent will return the maximum value.
                ''',
                'cpwctdmtimeelapsed',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMValidDayIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '30')], [], 
                '''                The number of previous days for which data
                was collected.
                An agent with TDM capability must be capable of supporting
                at least n intervals. The minimum value of n is 1, The
                default of n is 1 and the maximum value of n is 30.
                ''',
                'cpwctdmvaliddayintervals',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of previous 15-minute intervals for which data
                was collected.
                An agent with TDM capability must be capable of supporting
                at least n intervals. The minimum value of n is 4, The
                default of n is 32 and the maximum value of n is 96.
                The value will be <n> unless the measurement was (re-)
                started within the last (<n>*15) minutes, in which case
                the value will be the number of complete 15 minute
                intervals for which the agent has at least some data.
                In certain cases(e.g., in the case where the agent is
                a proxy) it is possible that some intervals are unavailable.
                In this case, this interval is the maximum interval number
                for which data is available.
                ''',
                'cpwctdmvalidintervals',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmtable',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMEntry', REFERENCE_LIST, 'Cpwctdmentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry', 
                [], [], 
                '''                This table is indexed by the same index that was
                created for the associated entry in the VC Table
                (in the CISCO-IETF-PW-MIB).
                
                  - The CpwVcIndex.
                
                An entry is created in this table by the agent for every
                entry in the cpwVcTable with a cpwVcType equal to one of the
                following:
                e1Satop(12), t1Satop(13), e3Satop(14), t3Satop(15),
                basicCesPsn(16), basicTdmIp(17),  tdmCasCesPsn(18),
                tdmCasTdmIp(19).
                ''',
                'cpwctdmentry',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMTable',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpayloadsuppressionEnum' : _MetaInfoEnum('CpwctdmcfgpayloadsuppressionEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'CISCO-IETF-PW-TDM-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB']),
    'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpktreplacepolicyEnum' : _MetaInfoEnum('CpwctdmcfgpktreplacepolicyEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB',
        {
            'ais':'ais',
            'implementationSpecific':'implementationSpecific',
        }, 'CISCO-IETF-PW-TDM-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB']),
    'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgtimestampmodeEnum' : _MetaInfoEnum('CpwctdmcfgtimestampmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB',
        {
            'notApplicable':'notApplicable',
            'absolute':'absolute',
            'differential':'differential',
        }, 'CISCO-IETF-PW-TDM-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB']),
    'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index to an entry in this table. The value is a copy of
                the assigned cpwCTDMCfgIndexNext.
                ''',
                'cpwctdmcfgindex',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCTDMCfgAlarmThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarms are only reported when the defect state persists
                for the length of time specified by this object.
                The object's unit is millisec
                ''',
                'cpwctdmcfgalarmthreshold',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgAvePktLossTimeWindow', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The length of time over which the average packet
                loss rate should be computed to detect Excessive packet
                loss rate
                ''',
                'cpwctdmcfgavepktlosstimewindow',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgClearAlarmThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alarm MUST be cleared after the corresponding defect is
                undetected for the amount of time specified by this object.
                The object's unit is millisec
                ''',
                'cpwctdmcfgclearalarmthreshold',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgConfErr', REFERENCE_BITS, 'Cpwctdmcfgconferr' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.Cpwctdmcfgconferr', 
                [], [], 
                '''                This object indicates the various configuration errors,
                illegal settings within the cpwCTDMCfg table. The errors
                can be due to several reasons, like Payload size mismatch
                or Jitter Buffer depth value mistmatch. 
                
                payloadSize - This bit is set if there is Payload size
                              mismatch between the local and peer
                              configurations. 
                jtrBfrDepth - This bit is set if there is Jitter Buffer
                              depth value mistmatch.
                other       - This bit is set if the error is not due to
                              payloadSize and jtrBfrDepth mismatch.
                ''',
                'cpwctdmcfgconferr',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgConsecMissPktsOutSynch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of consecutive missing packets that are
                required to enter the LOPS state.
                ''',
                'cpwctdmcfgconsecmisspktsoutsynch',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgConsecPktsInSynch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of consecutive packets with sequential
                sequence numbers that are required to exit the
                Loss of Packets (LOPS) state.
                ''',
                'cpwctdmcfgconsecpktsinsynch',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgExcessivePktLossThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excessive packet loss rate is detected by computing the
                average packetloss rate over a 
                cpwCTDMCfgAvePktLossTimeWindow amount of time and
                comparing it with this threshold value.
                ''',
                'cpwctdmcfgexcessivepktlossthreshold',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgJtrBfrDepth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The size of this buffer SHOULD be locally
                configured to allow accommodation to the PSN-specific
                packet delay variation.
                
                If configured to a value not supported by the
                implementation, the agent MUST return an error code
                'jtrBfrDepth' in 'cpwCTDMConfigError '.
                Jitter buffers are a limited resource to be managed.
                The actual size should be at least twice as big as the
                value of cpwCTDMCfgJtrBfrDepth
                ''',
                'cpwctdmcfgjtrbfrdepth',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgMissingPktsToSes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of missing packets detected (consecutive or not)
                within a 1 second window to cause a Severely Error
                Second (SES) to be counted.
                ''',
                'cpwctdmcfgmissingpktstoses',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgPayloadSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of this object indicates the PayLoad Size (in
                bytes) to be defined during the PW setUp. Upon TX,
                implementation must be capable of carrying that amount of
                bytes. Upon RX, when the LEN field is set to 0, the
                payload of packet  MUST assume this size, and if the actual
                packet size is inconsistent with this length,
                the packet MUST be considered to be malformed.
                ''',
                'cpwctdmcfgpayloadsize',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgPayloadSuppression', REFERENCE_ENUM_CLASS, 'CpwctdmcfgpayloadsuppressionEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpayloadsuppressionEnum', 
                [], [], 
                '''                This object indicates whether the Payload suppression
                is eanbled or disabled.
                Payload MAY be omitted in order to conserve bandwidth.
                
                enable  - Payload suppression is allowed.
                disable - No Payload suppresion under any condition.
                ''',
                'cpwctdmcfgpayloadsuppression',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgPktReorder', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, CE bound packets are queued in the
                jitter buffer, out of order packets are re-ordered. The
                maximum sequence number differential (i.e., the range in
                which re-sequencing can occur) is dependant on the depth
                of the jitter buffer. See cpwCTDMCfgJtrBfrDepth.
                ''',
                'cpwctdmcfgpktreorder',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgPktReplacePolicy', REFERENCE_ENUM_CLASS, 'CpwctdmcfgpktreplacepolicyEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpktreplacepolicyEnum', 
                [], [], 
                '''                This parameter determines the value to be played when CE
                bound packets have over/underflow the jitter buffer, or are
                missing for any reason. This AIS (Alarm Indication Signal)
                pattern is sent (played) on the TDM line.
                
                ais                    - AIS (Alarm Indication Signal)
                                         pattern is sent (played) on
                                         the TDM line. 
                implementationSpecific - Implementation specific pattern is
                                         sent on the TDM line.
                ''',
                'cpwctdmcfgpktreplacepolicy',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                To create a row in this table, a manager must
                set this object to either createAndGo(4) or
                createAndWait(5).
                
                All of the columnar objects have to be set to
                valid values before the row can be activated.
                Default value will be automatically provisioned
                if for those objects not specified during row
                creation. 
                No objects in cascading tables have to be populated with
                related data before the row can be activated.
                
                The following objects cannot be modified if the
                RowStatus is active:
                cpwCTDMCfgPayloadSize, cpwCTDMCfgRtpHdrUsed,
                cpwCTDMCfgJtrBfrDepth, and cpwCTDMCfgPayloadSuppression.
                
                If the RowStatus is active, the following parameters can be
                modified: 
                cpwCTDMCfgConfErr, cpwCTDMCfgPktReorder, 
                cpwCTDMCfgConsecPktsInSynch,
                cpwCTDMCfgConsecMissPktsOutSynch,
                cpwCTDMCfgSetUp2SynchTimeOut, cpwCTDMCfgPktReplacePolicy,
                cpwCTDMCfgAvePktLossTimeWindow, 
                cpwCTDMCfgExcessivePktLossThreshold,
                cpwCTDMCfgAlarmThreshold, cpwCTDMCfgClearAlarmThreshold,
                cpwCTDMCfgMissingPktsToSes, cpwCTDMCfgTimestampMode,
                cpwCTDMCfgStorageType.
                
                A row may be deleted by setting the RowStatus to 'destroy'.
                ''',
                'cpwctdmcfgrowstatus',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgRtpHdrUsed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the value of this object is set to false, then a
                RTP header is not pre-pended to the TDM packet.
                ''',
                'cpwctdmcfgrtphdrused',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgSetUp2SynchTimeOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The amount of time the host should wait before declaring
                the pseudo wire in down state,  if the number of consecutive
                TDM packets that have been received after changing the
                administrative status to up and after finalization of
                signaling (if supported) between the two PEs is smaller
                than cpwCTDMCfgConsecPktsInSynch. Once the the PW has
                OperStatus of 'up' this parameter is no longer valid. This
                parameter is defined to ensure that the host does not
                prematurely inform failure of the PW. In particular PW
                'down' notifications should not be sent before expiration of
                this timer. This parameter is valid only after adminisrative
                changes of the status of the PW. If the PW fails due to
                network impairments a 'down' notification should be sent.
                ''',
                'cpwctdmcfgsetup2synchtimeout',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this row.
                The following are the read-write objects in permanent(4)
                rows, that an agent must allow to be writable:
                cpwCTDMCfgPayloadSize, cpwCTDMCfgPktReorder,
                cpwCTDMCfgRtpHdrUsed, cpwCTDMCfgJtrBfrDepth,
                cpwCTDMCfgPayloadSuppression, cpwCTDMCfgConfErr.
                ''',
                'cpwctdmcfgstoragetype',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMCfgTimestampMode', REFERENCE_ENUM_CLASS, 'CpwctdmcfgtimestampmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgtimestampmodeEnum', 
                [], [], 
                '''                Timestamp generation MAY be used in one of the following
                modes:
                1. Absolute mode: the PSN-bound IWF sets timestamps
                 using the clock recovered from the incoming TDM attachment
                 circuit. As a consequence, the timestamps are closely
                 correlated with the sequence numbers. All TDM 
                 implementations that support usage of the RTP header MUST
                 support this mode.
                2. Differential mode: Both IWFs have access to a common
                 high-quality timing source, and this source is used for
                 timestamp generation. Support of this mode is OPTIONAL.
                ''',
                'cpwctdmcfgtimestampmode',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMCfgEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmcfgtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmcfgtable',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMCfgEntry', REFERENCE_LIST, 'Cpwctdmcfgentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry', 
                [], [], 
                '''                These parameters define the characteristics of a
                TDM PW. They are grouped here to ease NMS burden.
                Once an entry is created here it may be re-used
                by many PWs.
                ''',
                'cpwctdmcfgentry',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMCfgTable',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCTDMPerfCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Error
                Seconds encountered. Any malformed packet, sequence error
                and similar are considered as error second
                ''',
                'cpwctdmperfcurrentess',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentFC', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the number of TDM failure
                events. A failure event begins when the LOPS failure
                is declared, and ends when the failure is cleared. A
                failure event that begins in one period and ends in
                another period is counted only in the period in which
                it begins.
                ''',
                'cpwctdmperfcurrentfc',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentJtrBfrUnderruns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times a packet needed to be played
                out and the jitter buffer was empty.
                ''',
                'cpwctdmperfcurrentjtrbfrunderruns',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentMalformedPkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected with unexpected size, or
                bad headers' stack
                ''',
                'cpwctdmperfcurrentmalformedpkt',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentMisOrderDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected out of order(via control word
                sequence numbers), and could not be re-ordered, or could
                not fit in the jitter buffer.
                ''',
                'cpwctdmperfcurrentmisorderdropped',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentMissingPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of missing packets (as detected via control word
                sequence number gaps).
                ''',
                'cpwctdmperfcurrentmissingpkts',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentPktsReOrder', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected out of sequence (via control
                word sequence number), but successfully re-ordered.
                ''',
                'cpwctdmperfcurrentpktsreorder',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Error Seconds encountered.
                ''',
                'cpwctdmperfcurrentsess',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds encountered. Any consequtive
                five seconds of SES are counted as one UAS
                ''',
                'cpwctdmperfcurrentuass',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMPerfCurrentEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMPerfCurrentEntry', REFERENCE_LIST, 'Cpwctdmperfcurrententry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry', 
                [], [], 
                '''                An entry in this table is created by the agent for every
                cpwCTDMTable entry. After 15 minutes, the contents of this
                table entry are copied to a new entry in the
                cpwCTDMPerfInterval table and the counts in this entry
                are reset to zero.
                ''',
                'cpwctdmperfcurrententry',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMPerfCurrentTable',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCTDMPerfIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates a number (normally between 1 and
                96 to cover a 24 hour period) which identifies the interval
                for which the set of statistics is available. The interval
                identified by 1 is the most recently completed 15 minute
                interval, and the interval identified by N is the interval
                immediately preceding the one identified by N-1.
                The minimum range of N is 1 through 4.The default range
                is 1 through 32. The maximum value of N is 1 through 96.
                ''',
                'cpwctdmperfintervalnumber',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCTDMPerfIntervalDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The duration of a particular interval in seconds.
                Adjustments in the system's time-of-day clock, may
                cause the interval to be greater or less than, the
                normal value. Therefore this actual interval value
                is provided.
                ''',
                'cpwctdmperfintervalduration',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Error
                Seconds encountered.
                ''',
                'cpwctdmperfintervaless',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalFC', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the number of TDM failure
                events. A failure event begins when the LOPS failure
                is declared, and ends when the failure is cleared. A
                failure event that begins in one period and ends in
                another period is counted only in the period in which
                it begins.
                ''',
                'cpwctdmperfintervalfc',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalJtrBfrUnderruns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times a packet needed to be played
                out and the jitter buffer was empty.
                ''',
                'cpwctdmperfintervaljtrbfrunderruns',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalMalformedPkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected with unexpected size, or
                bad headers' stack
                ''',
                'cpwctdmperfintervalmalformedpkt',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalMisOrderDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected out of order(via control word
                sequence numbers), and could not be re-ordered, or could
                not fit in the jitter buffer.
                ''',
                'cpwctdmperfintervalmisorderdropped',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalMissingPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of missing packets (as detected via control
                word sequence number gaps).
                ''',
                'cpwctdmperfintervalmissingpkts',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalPktsReOrder', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected out of sequence (via control
                word sequence number), but successfully re-ordered.
                ''',
                'cpwctdmperfintervalpktsreorder',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Error Seconds encountered.
                ''',
                'cpwctdmperfintervalsess',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds encountered.
                ''',
                'cpwctdmperfintervaluass',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this interval
                is valid.
                ''',
                'cpwctdmperfintervalvaliddata',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMPerfIntervalEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmperfintervaltable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmperfintervaltable',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMPerfIntervalEntry', REFERENCE_LIST, 'Cpwctdmperfintervalentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry', 
                [], [], 
                '''                An entry in this table is created by the agent for
                every cpwCTDMPerfCurrentEntry that is 15 minutes old.
                The contents of the Current entry are copied to the new
                entry here. The Current entry, then resets its counts
                to zero for the next current 15 minute interval.
                ''',
                'cpwctdmperfintervalentry',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMPerfIntervalTable',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of interval, where 1 indicates current day
                measured period and 2 and above indicate previous days
                respectively
                ''',
                'cpwctdmperf1dayintervalnumber',
                'CISCO-IETF-PW-TDM-MIB', True),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The duration of a particular interval in seconds,
                Adjustments in the system's time-of-day clock, may
                cause the interval to be greater or less than, the
                normal value. Therefore this actual interval value
                is provided.
                ''',
                'cpwctdmperf1dayintervalduration',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Error
                Seconds encountered.
                ''',
                'cpwctdmperf1dayintervaless',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalFC', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the number of TDM failure
                events. A failure event begins when the LOPS failure
                is declared, and ends when the failure is cleared.
                ''',
                'cpwctdmperf1dayintervalfc',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalJtrBfrUnderruns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times a packet needed to be played
                out and the jitter buffer was empty.
                ''',
                'cpwctdmperf1dayintervaljtrbfrunderruns',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalMalformedPkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected with unexpected size, or
                bad headers' stack.
                ''',
                'cpwctdmperf1dayintervalmalformedpkt',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalMisOrderDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected out of order(via control word
                sequence numbers), and could not be re-ordered, or could
                not fit in the jitter buffer.
                ''',
                'cpwctdmperf1dayintervalmisorderdropped',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalMissingPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of missing packets (as detected via control word
                sequence number gaps).
                ''',
                'cpwctdmperf1dayintervalmissingpkts',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalPktsReOrder', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets detected out of sequence (via control
                word sequence number), but successfully re-ordered.
                ''',
                'cpwctdmperf1dayintervalpktsreorder',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Severely
                Error Seconds.
                ''',
                'cpwctdmperf1dayintervalsess',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                UnAvailable Seconds.
                When first entering the UAS state, the number
                of SES To UAS is added to this object, then as each
                additional UAS occurs, this object increments by one.
                ''',
                'cpwctdmperf1dayintervaluass',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this interval
                is valid.
                ''',
                'cpwctdmperf1dayintervalvaliddata',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMPerf1DayIntervalEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalEntry', REFERENCE_LIST, 'Cpwctdmperf1Dayintervalentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry', 
                [], [], 
                '''                An entry is created in this table by the agent
                for every entry in the cpwCTDMTable table.
                ''',
                'cpwctdmperf1dayintervalentry',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'cpwCTDMPerf1DayIntervalTable',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
    'CiscoIetfPwTdmMib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwTdmMib',
            False, 
            [
            _MetaInfoClassMember('cpwCTDMCfgTable', REFERENCE_CLASS, 'Cpwctdmcfgtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmcfgtable', 
                [], [], 
                '''                This table contains a set of parameters that may be
                referenced by one or more TDM PWs in cpwCTDMTable.
                ''',
                'cpwctdmcfgtable',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMObjects', REFERENCE_CLASS, 'Cpwctdmobjects' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmobjects', 
                [], [], 
                '''                ''',
                'cpwctdmobjects',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerf1DayIntervalTable', REFERENCE_CLASS, 'Cpwctdmperf1Dayintervaltable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable', 
                [], [], 
                '''                This table provides performance information per TDM PW
                similar to the cpwCTDMPerfIntervalTable above. However,
                these counters represent historical 1 day intervals up to
                one full month. The table consists of real time data, as
                such it is not persistence across re-boot.
                ''',
                'cpwctdmperf1dayintervaltable',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfCurrentTable', REFERENCE_CLASS, 'Cpwctdmperfcurrenttable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable', 
                [], [], 
                '''                This table provides TDM PW performance information.
                This includes current 15 minute interval counts. 
                
                The table includes counters that work together to
                integrate errors and the lack of errors on the TDM PW.
                An error is caused by a missing packet. Missing packet
                can be a result of, packet loss in the network,
                (uncorrectable) packet out of sequence, packet length error,
                jitter buffer overflow, and jitter buffer underflow.
                The result is declaring whether or not the TDM PW is in
                Loss of Packet (LOPS) state.
                ''',
                'cpwctdmperfcurrenttable',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMPerfIntervalTable', REFERENCE_CLASS, 'Cpwctdmperfintervaltable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmperfintervaltable', 
                [], [], 
                '''                This table provides performance information per TDM PW
                similar to the cpwCTDMPerfCurrentTable above. However,
                these counts represent historical 15 minute intervals.
                Typically, this table will have a maximum of 96 entries
                for a 24 hour period, but is not limited to this.
                ''',
                'cpwctdmperfintervaltable',
                'CISCO-IETF-PW-TDM-MIB', False),
            _MetaInfoClassMember('cpwCTDMTable', REFERENCE_CLASS, 'Cpwctdmtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CiscoIetfPwTdmMib.Cpwctdmtable', 
                [], [], 
                '''                This table contains basic information including ifIndex,
                and pointers to entries in the relevant TDM config
                tables for this TDM PW.
                ''',
                'cpwctdmtable',
                'CISCO-IETF-PW-TDM-MIB', False),
            ],
            'CISCO-IETF-PW-TDM-MIB',
            'CISCO-IETF-PW-TDM-MIB',
            _yang_ns._namespaces['CISCO-IETF-PW-TDM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB'
        ),
    },
}
_meta_table['CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib.Cpwctdmtable']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib.Cpwctdmperfintervaltable']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmobjects']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmtable']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmperfintervaltable']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib']['meta_info']
_meta_table['CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable']['meta_info'].parent =_meta_table['CiscoIetfPwTdmMib']['meta_info']
