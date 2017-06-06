


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscosbcperiodicstatsintervalEnum' : _MetaInfoEnum('CiscosbcperiodicstatsintervalEnum', 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB',
        {
            'fiveMinute':'fiveMinute',
            'fifteenMinute':'fifteenMinute',
            'oneHour':'oneHour',
            'oneDay':'oneDay',
        }, 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB']),
    'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object uniquely identifies the sequence number of an
                entity or slot that is configured per device. This index is
                assigned arbitrarily by the engine and is not saved over
                reboots.
                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsInstancePhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the physical entity for which all the
                measurements are maintained. The exact type of this
                entity is described by its entPhysicalVendorType value.
                ''',
                'csbcallstatsinstancephysicalindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbCallStatsInstanceEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceEntry', REFERENCE_LIST, 'Csbcallstatsinstanceentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry', 
                [], [], 
                '''                A conceptual row in csbCallStatsInstanceTable. There is an
                entry in this table for each SBC instance, as identified by a 
                value of csbCallStatsInstanceIndex.
                ''',
                'csbcallstatsinstanceentry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbCallStatsInstanceTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object identifies the index of the name of the SBC
                service configured. This object also acts as an index for the
                table.
                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsActiveTranscodeFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of transcoded
                flows that are actively forwarding media traffic.  In this
                context, a flow is a media stream passing through the device.
                So a single voice call will be counted only once.
                ''',
                'csbcallstatsactivetranscodeflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsAvailableFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of media flows which are
                available.
                ''',
                'csbcallstatsavailableflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsAvailablePktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the remaining capacity that can be
                supported by SBC.
                ''',
                'csbcallstatsavailablepktrate',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsAvailableTranscodeFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of additional transcoded flows
                that this media gateway manager (MGM) entity is currently able
                to configure.
                ''',
                'csbcallstatsavailabletranscodeflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsCallsHigh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum number of calls per second
                processed by the Session Border Controller in past 24 hours.
                ''',
                'csbcallstatscallshigh',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsCallsLow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the minimum calls per second in past 24
                hours.
                ''',
                'csbcallstatscallslow',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsNoMediaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the accumulated No media event
                count.
                ''',
                'csbcallstatsnomediacount',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsPeakFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of peak flows in SBC.
                This is the highest recorded value for the active flows since
                the box was booted/reseted.
                ''',
                'csbcallstatspeakflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsPeakSigFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the peak signaling flow in SBC.
                This is the highest recorded value for the active signaling
                flows. This object is calculated using csbCallStatsUsedFlows.
                ''',
                'csbcallstatspeaksigflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsPeakTranscodeFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the peak number of active transcoded
                flows since the statistics were last reset.  In this context, a
                flow is a media stream passing through the device, so a single
                voice call will be counted once.
                ''',
                'csbcallstatspeaktranscodeflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRate1Sec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average calls per second processed by
                the Session Border Controller.
                ''',
                'csbcallstatsrate1sec',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRouteErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the accumulated route error event
                count. This counter is for the route error of media stream.
                ''',
                'csbcallstatsrouteerrors',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRTPOctetsDiscard', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP octets discarded by
                the SBC.
                ''',
                'csbcallstatsrtpoctetsdiscard',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRTPOctetsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP octets received by
                the SBC.
                ''',
                'csbcallstatsrtpoctetsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRTPOctetsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP octets sent by the
                SBC.
                ''',
                'csbcallstatsrtpoctetssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRTPPktsDiscard', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of RTP packets
                discarded.
                ''',
                'csbcallstatsrtppktsdiscard',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRTPPktsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of RTP packets
                received.
                ''',
                'csbcallstatsrtppktsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsRTPPktsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of RTP packets sent.
                ''',
                'csbcallstatsrtppktssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsSbcName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the configured name of the SBC service.
                The length of this object is zero when value is not assigned
                to it.
                ''',
                'csbcallstatssbcname',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsTotalFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of media support by this
                instance of SBC. The total number of flows include the
                available
                flows and the active flows. This value is since box was
                booted/reseted. Total flows include the active flows and the
                flows allocated but not connected.
                ''',
                'csbcallstatstotalflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsTotalSigFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum number of Signalling Flows
                that can be supported by this instance of SBC.
                ''',
                'csbcallstatstotalsigflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsTotalTranscodeFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the accumulated total number of
                transcoded flows.  This count contains both active flows and
                flows that were allocated but never connected.  In this context,
                a flow is a media stream passing through the device, so a single
                voice call will be counted once.
                ''',
                'csbcallstatstotaltranscodeflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsUnclassifiedPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of unclassified packets
                processed by SBC.
                ''',
                'csbcallstatsunclassifiedpkts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsUsedFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of media flows which are
                used. This is for the flow allocated and connected. The flow
                allocated but not connected is not counted.
                ''',
                'csbcallstatsusedflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsUsedSigFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active signaling flows for
                signaling pinholes.
                ''',
                'csbcallstatsusedsigflows',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbCallStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsEntry', REFERENCE_LIST, 'Csbcallstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry', 
                [], [], 
                '''                An conceptual row in the csbCallStatsGlobalStatsTable. There is
                an entry in this table for the particular service configured on
                SBC identified by a value of csbCallStatsInstanceIndex. The
                other index of this table is csbCallStatsInstanceIndex which is
                defined in csbCallStatsInstanceTable.
                ''',
                'csbcallstatsentry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbCallStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCurrPeriodicStatsInterval', REFERENCE_ENUM_CLASS, 'CiscosbcperiodicstatsintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscosbcperiodicstatsintervalEnum', 
                [], [], 
                '''                This object identifies the interval for which the periodic
                statistics information is to be displayed. The interval
                values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts
                as index for the table.
                ''',
                'csbcurrperiodicstatsinterval',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCurrPeriodicIpsecCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active calls on this adjacency or account which
                are to or from registered subscribers using IPSEC during this
                interval.
                ''',
                'csbcurrperiodicipseccalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsActivatingCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls that have become
                activing during this interval.
                ''',
                'csbcurrperiodicstatsactivatingcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsActiveCallFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active call failures during
                this interval.
                ''',
                'csbcurrperiodicstatsactivecallfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsActiveCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls that have become
                active during this interval.
                ''',
                'csbcurrperiodicstatsactivecalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsActiveE2EmergencyCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls through SBC that have
                been identified as emergency calls (by Number Analysis) and
                have used the e2 interface to obtain location information for
                the caller during this interval.
                ''',
                'csbcurrperiodicstatsactivee2emergencycalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsActiveEmergencyCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls through SBC that have
                been identified as emergency calls (by Number Analysis) during
                this interval.
                ''',
                'csbcurrperiodicstatsactiveemergencycalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsActiveIpv6Calls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This Object indicates the number of calls through SBC that use
                IPv6 signaling.  This statistic totals all calls that traverse
                an IPv6 adjacency on either or both sides of SBC during this
                interval.
                ''',
                'csbcurrperiodicstatsactiveipv6calls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsAudioTranscodedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active audio transcoded calls through
                this adjacency or account during this interval.
                ''',
                'csbcurrperiodicstatsaudiotranscodedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallMediaFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to media failure during this interval.
                ''',
                'csbcurrperiodicstatscallmediafailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallResourceFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to resource failures during this interval.
                ''',
                'csbcurrperiodicstatscallresourcefailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallRoutingFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to routing failures during this interval.
                ''',
                'csbcurrperiodicstatscallroutingfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupCACBandwidthFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC bandwidth limit during this interval.
                ''',
                'csbcurrperiodicstatscallsetupcacbandwidthfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupCACCallLimitFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC call limit during this interval.
                ''',
                'csbcurrperiodicstatscallsetupcaccalllimitfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupCACMediaLimitFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC media limit during this interval.
                ''',
                'csbcurrperiodicstatscallsetupcacmedialimitfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call update failure due
                to policy failure during this interval.
                ''',
                'csbcurrperiodicstatscallsetupcacmediaupdatefailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupCACPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC policy failure during this interval.
                ''',
                'csbcurrperiodicstatscallsetupcacpolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupCACRateLimitFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC call rate limit during this interval.
                ''',
                'csbcurrperiodicstatscallsetupcacratelimitfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupNAPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to NA policy failure during this interval.
                ''',
                'csbcurrperiodicstatscallsetupnapolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to policy failure during this interval.
                ''',
                'csbcurrperiodicstatscallsetuppolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSetupRoutingPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to routing policy failure during this interval.
                ''',
                'csbcurrperiodicstatscallsetuproutingpolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCallSigFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to signaling failure during this interval.
                ''',
                'csbcurrperiodicstatscallsigfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCongestionFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to congestion during this interval.
                ''',
                'csbcurrperiodicstatscongestionfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsCurrentTaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the Lawful intercept taps currently in
                place on calls within the scope of this query during this
                interval.
                ''',
                'csbcurrperiodicstatscurrenttaps',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsDeactivatingCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls that have become
                deactiving during this interval.
                ''',
                'csbcurrperiodicstatsdeactivatingcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsDtmfIw2833Calls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account for which DTMF interworking
                is enabled between DTMF in signaling and DTMF in media via RFC
                2833 during this interval.
                ''',
                'csbcurrperiodicstatsdtmfiw2833calls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsDtmfIw2833InbandCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account for which DTMF interworking
                is enabled between DTMF in media via RFC 2833 and DTMF in media
                via inband DTMF tones during this interval.
                ''',
                'csbcurrperiodicstatsdtmfiw2833inbandcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsDtmfIwInbandCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account for which DTMF interworking
                is enabled between DTMF in signaling and DTMF in media via 
                inband DTMF tones during this interval.
                ''',
                'csbcurrperiodicstatsdtmfiwinbandcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsFailedCallAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of failed call attempts during
                this interval.
                ''',
                'csbcurrperiodicstatsfailedcallattempts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsFaxTranscodedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the the number of active fax
                transcoded calls through this adjacency or account during this
                interval.
                ''',
                'csbcurrperiodicstatsfaxtranscodedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsImsRxActiveCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of active calls which
                use IMS Rx, during this interval.
                ''',
                'csbcurrperiodicstatsimsrxactivecalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsImsRxCallRenegotiationAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call renegotiation attempts
                using IMS Rx during this interval.
                ''',
                'csbcurrperiodicstatsimsrxcallrenegotiationattempts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsImsRxCallRenegotiationFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call renegotiation failures
                owing to IMS Rx failure during this interval.
                ''',
                'csbcurrperiodicstatsimsrxcallrenegotiationfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsImsRxCallSetupFaiures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call Setup failures owing to
                IMS Rx failure during this interval.
                ''',
                'csbcurrperiodicstatsimsrxcallsetupfaiures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsNonSrtpCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account which do not use SRTP on any
                media channels during this interval.
                ''',
                'csbcurrperiodicstatsnonsrtpcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsRtpDisallowedFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call setup failures due to RTP
                being proposed when not permitted during this interval.
                ''',
                'csbcurrperiodicstatsrtpdisallowedfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsSrtpDisallowedFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call setup failures due to SRTP
                being proposed when not permitted during this interval.
                ''',
                'csbcurrperiodicstatssrtpdisallowedfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsSrtpIwCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account that have one or more media
                channels that provide interworking between RTP and SRTP during
                this interval.
                ''',
                'csbcurrperiodicstatssrtpiwcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsSrtpNonIwCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account that have one or more media
                channels which use SRTP. This count does not include media 
                channels that provide interworking between RTP and SRTP during
                this interval.
                ''',
                'csbcurrperiodicstatssrtpnoniwcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTimestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This object indicates the current time at the start of each
                interval.
                ''',
                'csbcurrperiodicstatstimestamp',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTotalCallAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of total call attempts during
                this interval.
                ''',
                'csbcurrperiodicstatstotalcallattempts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTotalCallUpdateFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of call update failures
                during this interval.
                ''',
                'csbcurrperiodicstatstotalcallupdatefailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTotalTapsRequested', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the lawful intercept tap attempts
                requested within the scope of this query during this interval.
                ''',
                'csbcurrperiodicstatstotaltapsrequested',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTotalTapsSucceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the lawful intercept tap attempts that
                have been successfully implemented within the scope of this
                query during this interval.
                ''',
                'csbcurrperiodicstatstotaltapssucceeded',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTranscodedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The object indicates the number of transcoded calls that are
                active during this interval.
                ''',
                'csbcurrperiodicstatstranscodedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTransratedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The object indicates the number of transrated calls that are
                active during this interval.
                ''',
                'csbcurrperiodicstatstransratedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbCurrPeriodicStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable',
            False, 
            [
            _MetaInfoClassMember('csbCurrPeriodicStatsEntry', REFERENCE_LIST, 'Csbcurrperiodicstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry', 
                [], [], 
                '''                An conceptual row in the csbCurrPeriodicStatsTable. There is
                an entry in this table for the particular controller by a value
                of csbH248StatsCtrlrIndex. The other indices of this table are
                csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
                and csbCallStatsServiceIndex defined in csbCallStatsTable.
                ''',
                'csbcurrperiodicstatsentry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbCurrPeriodicStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbHistoryStatsInterval', REFERENCE_ENUM_CLASS, 'CiscosbcperiodicstatsintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscosbcperiodicstatsintervalEnum', 
                [], [], 
                '''                This object identifies the interval for which the history
                statistics information is to be displayed. The interval
                values can be 5 min, 15 mins, 1 hour , 1 day. This object acts
                as index for the table.
                ''',
                'csbhistorystatsinterval',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbHistoryStatsElements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The platform assigns a number starting with one and
                increments it each for each new row. When the maximum         
                number of row is reached the oldest rows are deleted. It is up
                to the platform to determine the number of entries for each
                interval. It is recommended that each platform support at least
                one entry for 5 min, 15 mins, 1 hour and 1 day intervals.
                ''',
                'csbhistorystatselements',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbHistoryStatsActiveCallFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active call failures during
                this interval.
                ''',
                'csbhistorystatsactivecallfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsActiveCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls history during
                this interval.
                ''',
                'csbhistorystatsactivecalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsActiveE2EmergencyCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls through SBC that have
                been identified as emergency calls (by Number Analysis) and
                have used the e2 interface to obtain location information for
                the
                caller.
                ''',
                'csbhistorystatsactivee2emergencycalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsActiveEmergencyCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of calls through SBC that have
                been identified as emergency calls (by Number Analysis)  during
                this interval.
                ''',
                'csbhistorystatsactiveemergencycalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsActiveIpv6Calls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This Object indicates the number of calls through SBC that use
                IPv6 signaling.  This statistic totals all calls that traverse
                an IPv6 adjacency on either or both sides of SBC during this
                interval.
                ''',
                'csbhistorystatsactiveipv6calls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsAudioTranscodedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active audio transcoded calls through
                this adjacency or account during this interval.
                ''',
                'csbhistorystatsaudiotranscodedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallMediaFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to media failure during this interval.
                ''',
                'csbhistorystatscallmediafailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallResourceFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to resource failures during this interval.
                ''',
                'csbhistorystatscallresourcefailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallRoutingFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to routing failures during this interval.
                ''',
                'csbhistorystatscallroutingfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupCACBandwidthFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC bandwidth limit during this interval.
                ''',
                'csbhistorystatscallsetupcacbandwidthfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupCACCallLimitFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC call limit during this interval.
                ''',
                'csbhistorystatscallsetupcaccalllimitfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupCACMediaLimitFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC media limit during this interval.
                ''',
                'csbhistorystatscallsetupcacmedialimitfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupCACMediaUpdateFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call update failure due
                to policy failure during this interval.
                ''',
                'csbhistorystatscallsetupcacmediaupdatefailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupCACPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC policy failure during this interval.
                ''',
                'csbhistorystatscallsetupcacpolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupCACRateLimitFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to CAC call rate limit during this interval.
                ''',
                'csbhistorystatscallsetupcacratelimitfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupNAPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to NA policy failure during this interval.
                ''',
                'csbhistorystatscallsetupnapolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to some policy violations during this interval.
                ''',
                'csbhistorystatscallsetuppolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCallSetupRoutingPolicyFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to routing policy failure during this interval.
                ''',
                'csbhistorystatscallsetuproutingpolicyfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCongestionFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to congestion during this interval.
                ''',
                'csbhistorystatscongestionfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsCurrentTaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the Lawful intercept taps currently in
                place on calls within the scope of this query during this
                interval.
                ''',
                'csbhistorystatscurrenttaps',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsDtmfIw2833Calls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account for which DTMF interworking
                is enabled between DTMF in signaling and DTMF in media via RFC
                2833 during this interval.
                ''',
                'csbhistorystatsdtmfiw2833calls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsDtmfIw2833InbandCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account for which DTMF interworking
                is enabled between DTMF in media via RFC 2833 and DTMF in media
                via inband DTMF tones during this interval.
                ''',
                'csbhistorystatsdtmfiw2833inbandcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsDtmfIwInbandCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account for which DTMF interworking
                is enabled between DTMF in signaling and DTMF in media via
                inband DTMF tones during this interval.
                ''',
                'csbhistorystatsdtmfiwinbandcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsFailedCallAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of failed call attempts during
                this interval.
                ''',
                'csbhistorystatsfailedcallattempts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsFailSigFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of call setup failures due
                to signaling failure during this interval.
                ''',
                'csbhistorystatsfailsigfailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsFaxTranscodedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the the number of active fax
                transcoded calls through this adjacency or account during this
                interval.
                ''',
                'csbhistorystatsfaxtranscodedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsImsRxActiveCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of active calls which
                use IMS Rx, during this interval.
                ''',
                'csbhistorystatsimsrxactivecalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsImsRxCallRenegotiationAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call renegotiation attempts
                using IMS Rx during this interval.
                ''',
                'csbhistorystatsimsrxcallrenegotiationattempts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsImsRxCallRenegotiationFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call renegotiation failures
                owing to IMS Rx failure during this interval.
                ''',
                'csbhistorystatsimsrxcallrenegotiationfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsImsRxCallSetupFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call setup failures owing to
                IMS Rx failure during this interval.
                ''',
                'csbhistorystatsimsrxcallsetupfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsIpsecCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active calls on this adjacency or account which
                are to or from registered subscribers using IPSEC during this
                interval.
                ''',
                'csbhistorystatsipseccalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsNonSrtpCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account which do not use SRTP on any
                media channels during this interval.
                ''',
                'csbhistorystatsnonsrtpcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsRtpDisallowedFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call setup failures due to RTP
                being proposed when not permitted during this interval.
                ''',
                'csbhistorystatsrtpdisallowedfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsSrtpDisallowedFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call setup failures due to SRTP
                being proposed when not permitted during this interval.
                ''',
                'csbhistorystatssrtpdisallowedfailures',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsSrtpIwCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account that have one or more media
                channels that provide interworking between RTP and SRTP during
                this interval.
                ''',
                'csbhistorystatssrtpiwcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsSrtpNonIwCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of active calls
                through this adjacency or account that have one or more media
                channels that use SRTP but no media channels that provide
                interworking between RTP and SRTP during this interval.
                ''',
                'csbhistorystatssrtpnoniwcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsTimestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This object indicates the time at the start of the interval
                when measurements were first collected for this interval in the
                csbCurrPeriodicStatsTable.
                ''',
                'csbhistorystatstimestamp',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsTotalCallAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of total call attempts history
                during this interval.
                ''',
                'csbhistorystatstotalcallattempts',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsTotalCallUpdateFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total call update failures during
                this interval.
                ''',
                'csbhistorystatstotalcallupdatefailure',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsTotalTapsRequested', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the lawful intercept tap attempts
                requested within the scope of this query during this interval.
                ''',
                'csbhistorystatstotaltapsrequested',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsTotalTapsSucceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the lawful intercept tap attempts that
                have been successfully implemented within the scope of this
                query during this interval.
                ''',
                'csbhistorystatstotaltapssucceeded',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistroyStatsTranscodedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The object indicates the number of active transcoded
                calls during this interval.
                ''',
                'csbhistroystatstranscodedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistroyStatsTransratedCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The object indicates the number of active transrated
                calls during this interval.
                ''',
                'csbhistroystatstransratedcalls',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbHistoryStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable',
            False, 
            [
            _MetaInfoClassMember('csbHistoryStatsEntry', REFERENCE_LIST, 'Csbhistorystatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry', 
                [], [], 
                '''                A conceptual row in the csbHistoryStatsTable. The entries in
                this table are updated as interval completes in the
                csbCurrPeriodicStatsTable table and the data is moved from that
                table to this one.
                ''',
                'csbhistorystatsentry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbHistoryStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatsflowtypeEnum' : _MetaInfoEnum('CsbperflowstatsflowtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB',
        {
            'media':'media',
            'signalling':'signalling',
        }, 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB']),
    'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatssideidEnum' : _MetaInfoEnum('CsbperflowstatssideidEnum', 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB',
        {
            'sideA':'sideA',
            'sideB':'sideB',
        }, 'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB']),
    'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbPerFlowStatsVdbeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object identifies the virtual media gateway id. This
                object also acts as an index for the table.
                ''',
                'csbperflowstatsvdbeid',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbPerFlowStatsGateId', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object identifies the gate id. This object also acts as
                an index for the table.
                ''',
                'csbperflowstatsgateid',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbPerFlowStatsFlowPairId', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object identifies the flow pair id. This object also acts
                as an index for the table.
                ''',
                'csbperflowstatsflowpairid',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbPerFlowStatsSideId', REFERENCE_ENUM_CLASS, 'CsbperflowstatssideidEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatssideidEnum', 
                [], [], 
                '''                This object identifies the index corresponding to side of flow
                pair either side A or side B. This object also acts as an index
                for the table.
                ''',
                'csbperflowstatssideid',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbPerFlowStatsAdrStatus', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                This object indicates whether the flow on the current
                FlowPair has subscribed for the NAT latch event.
                ''',
                'csbperflowstatsadrstatus',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsDscpSettings', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the mark packets sent for the
                current FlowPair with, or zero if none set. The DSCP is a 6-bit
                value, which will be present in the top 6 bits of the lowest
                byte of this field.
                ''',
                'csbperflowstatsdscpsettings',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsEPJitter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the End Point jitter per flow in the
                SBC.
                ''',
                'csbperflowstatsepjitter',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsFlowType', REFERENCE_ENUM_CLASS, 'CsbperflowstatsflowtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry.CsbperflowstatsflowtypeEnum', 
                [], [], 
                '''                This object indicates the type of the flow, like media flow,
                signaling flow etc.
                ''',
                'csbperflowstatsflowtype',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsQASettings', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                This object indicates the flow on the current FlowPair has
                subscribed for the media loss event.
                ''',
                'csbperflowstatsqasettings',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTCPPktsLost', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of RTP packets reported as lost by the remote end
                point on this flow. This information is from RTCP packet. Not
                all endpoints report this statistic, if it is not available it
                will be set to zero. This statistic will not be available for
                signaling flows.
                ''',
                'csbperflowstatsrtcppktslost',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTCPPktsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of RTP packets received by the remote end point from
                this MG on this flow. Comparing this with the local number of
                RTP packets sent from this MG to the remote endpoint gives an
                indication of how many outgoing packets were dropped on this
                leg of the call. This information is from RTCP packet. Not all
                endpoints report this statistic, if it is not available it will
                be set to zero. This statistic will not be available for
                signaling flows.
                ''',
                'csbperflowstatsrtcppktsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTCPPktsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of RTP packets sent by the remote end point to this
                MG on this flow. Comparing this with the local number of RTP
                packets received from the remote end point gives an indication
                of how many incoming  packets were dropped on this leg of the
                call. This information is from RTCP packet. Not all endpoints
                report this statistic, if it is not available it will be set to
                zero. This statistic will not be available for signaling flows.
                ''',
                'csbperflowstatsrtcppktssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPOctetsDiscard', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP octets discarded
                per flow by the SBC.
                ''',
                'csbperflowstatsrtpoctetsdiscard',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPOctetsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP octets received
                per flow by the SBC.
                ''',
                'csbperflowstatsrtpoctetsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPOctetsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP octets sent
                per flow by the SBC.
                ''',
                'csbperflowstatsrtpoctetssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPPktsDiscard', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP packets discarded  per
                flow by the SBC.
                ''',
                'csbperflowstatsrtppktsdiscard',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPPktsLost', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP packets lost per flow
                by the SBC.
                ''',
                'csbperflowstatsrtppktslost',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPPktsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP packets received per
                flow by the SBC.
                ''',
                'csbperflowstatsrtppktsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsRTPPktsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of RTP packets sent per flow
                by the SBC.
                ''',
                'csbperflowstatsrtppktssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsTmanPerMbs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum burst size for the
                current FlowPair.
                ''',
                'csbperflowstatstmanpermbs',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsTmanPerSdr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the bandwidth reserved for flow in
                kilobytes/second.
                ''',
                'csbperflowstatstmanpersdr',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbPerFlowStatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable',
            False, 
            [
            _MetaInfoClassMember('csbPerFlowStatsEntry', REFERENCE_LIST, 'Csbperflowstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry', 
                [], [], 
                '''                An conceptual row in the csbPerFlowStatsTable. There is
                an entry in this table for vdbe Id, gate id, flow pair id and
                side id. The other indices of this table are
                csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
                and csbCallStatsServiceIndex defined in csbCallStatsTable.
                ''',
                'csbperflowstatsentry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbPerFlowStatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbH248StatsCtrlrIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                This object identifies the controller index of the H.248
                server. This is also the index for the table.
                ''',
                'csbh248statsctrlrindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbH248StatsEstablishedTime', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This object indicates the H.248 Controller established
                time (the time at which the association became established).
                ''',
                'csbh248statsestablishedtime',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsLT', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the LT value calculated from RTT
                value and Max timeout value. This field specifies the maximum
                delay (in milliseconds) for a response from an MGC plus the
                maximum round trip propagation delay in the network (in
                milliseconds).
                ''',
                'csbh248statslt',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRepliesRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of replies received from the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrepliesrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRepliesRetried', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of replies retried through
                the Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrepliesretried',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRepliesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of replies sent through the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrepliessent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsFailed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests failed on session
                Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestsfailed',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests received through the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsRetried', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests retried through the Session
                Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestsretried',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests sent through the Session
                Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRTT', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the calculated RTT value. This field
                specifies the maximum round trip propagation delay in the 
                network (in milliseconds).
                ''',
                'csbh248statsrtt',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsSegPktsRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of packets received from the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statssegpktsrcvd',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsSegPktsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of packets sent through the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statssegpktssent',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsTMaxTimeoutVal', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object indicates the T-Max timeout value. This field
                specifies the maximum delay (in milliseconds) for a response
                from an MGC before deciding that the request has failed.
                ''',
                'csbh248statstmaxtimeoutval',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbH248StatsEntry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable',
            False, 
            [
            _MetaInfoClassMember('csbH248StatsEntry', REFERENCE_LIST, 'Csbh248Statsentry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry', 
                [], [], 
                '''                An conceptual row in the csbCallStath248Table. There is
                an entry in this table for the particular controller by a value
                of csbH248StatsCtrlrIndex. The other indices of this table are
                csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
                and csbCallStatsServiceIndex defined in csbCallStatsTable.
                ''',
                'csbh248statsentry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbH248StatsTable',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsinstanceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbCallStatsServiceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'csbcallstatsserviceindex',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbH248StatsVdbeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object identifies the virtual media gateway id. This is
                also the index for the table.
                ''',
                'csbh248statsvdbeid',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', True),
            _MetaInfoClassMember('csbH248StatsEstablishedTimeRev1', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This object indicates the H.248 Controller established
                time (the time at which the association became established).
                ''',
                'csbh248statsestablishedtimerev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsLTRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the LT value calculated from RTT
                value and Max timeout value. This field specifies the maximum
                delay (in milliseconds) for a response from an MGC plus the
                maximum round trip propagation delay in the network (in
                milliseconds).
                ''',
                'csbh248statsltrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRepliesRcvdRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of replies received from the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrepliesrcvdrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRepliesRetriedRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of replies retried through
                the Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrepliesretriedrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRepliesSentRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of replies sent through the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrepliessentrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsFailedRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests failed on session
                Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestsfailedrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsRcvdRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests received through the
                Session Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestsrcvdrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsRetriedRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests retried through the Session
                Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestsretriedrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRequestsSentRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the requests sent through the Session
                Controller Interface to an SBE or DBE.
                ''',
                'csbh248statsrequestssentrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRTTRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the calculated RTT value. This field
                specifies the maximum round trip propagation delay in the 
                network (in milliseconds).
                ''',
                'csbh248statsrttrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsSegPktsRcvdRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of response segments received
                by DBE. This field will only be present if segmentation is
                enabled on this association.
                ''',
                'csbh248statssegpktsrcvdrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsSegPktsSentRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of response segments sent by
                DBE. This field will only be present if segmentation is enabled
                on this association.
                ''',
                'csbh248statssegpktssentrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsTMaxTimeoutValRev1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object indicates the T-Max timeout value. This field
                specifies the maximum delay (in milliseconds) for a response
                from an MGC before deciding that the request has failed.
                ''',
                'csbh248statstmaxtimeoutvalrev1',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbH248StatsRev1Entry',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table',
            False, 
            [
            _MetaInfoClassMember('csbH248StatsRev1Entry', REFERENCE_LIST, 'Csbh248Statsrev1Entry' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry', 
                [], [], 
                '''                An conceptual row in the csbCallStath248Table. There is
                an entry in this table for the particular Vdbe by a value
                of csbH248StatsVdbeId. The other indices of this table are
                csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable
                and csbCallStatsServiceIndex defined in csbCallStatsTable.
                ''',
                'csbh248statsrev1entry',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'csbH248StatsRev1Table',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
    'CiscoSessBorderCtrlrCallStatsMib' : {
        'meta_info' : _MetaInfoClass('CiscoSessBorderCtrlrCallStatsMib',
            False, 
            [
            _MetaInfoClassMember('csbCallStatsInstanceTable', REFERENCE_CLASS, 'Csbcallstatsinstancetable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable', 
                [], [], 
                '''                The call stats instance table contains the physical index for
                each of the physical entity (line card, primary, secondary
                cards). The index of the table is instance index which uniquely
                identifies the physical entity present on the box.
                ''',
                'csbcallstatsinstancetable',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCallStatsTable', REFERENCE_CLASS, 'Csbcallstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable', 
                [], [], 
                '''                This table describes the global statistics information in the
                form of a table which contains call specific information like
                call rates, media flows, signaling flows etc. The index of the
                table is service index which corresponds to a particular 
                service configured on the SBC and all the rows of the table
                represents the global information regarding all the call flows
                related to that particular service. The other index of this
                table is csbCallStatsInstanceIndex which is defined in
                csbCallStatsInstanceTable.
                ''',
                'csbcallstatstable',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbCurrPeriodicStatsTable', REFERENCE_CLASS, 'Csbcurrperiodicstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable', 
                [], [], 
                '''                This table is used to collect measurement over several
                different intervals as defined by the
                csbCurrPeriodicStatsInterval object. When a new interval starts
                the objects associated with the interval are reset and count up
                throughout the interval. The index of the table is the interval
                for which the stats information is to be displayed. The interval
                values can be 5 min, 15 mins, 1 hour and one day. The other
                indices of this table are csbCallStatsInstanceIndex
                defined in csbCallStatsInstanceTable and
                csbCallStatsServiceIndex defined in csbCallStatsTable.
                
                The gauge values are reported as :-
                1.If the period being queried is current5mins, this is the value
                at the instant that the query is issued. 
                2.Otherwise, for the other intevals, this is an average value
                during the summary period sampled at 5 minute intervals.
                ''',
                'csbcurrperiodicstatstable',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsRev1Table', REFERENCE_CLASS, 'Csbh248Statsrev1Table' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table', 
                [], [], 
                '''                This table describes the H.248 statistics for SBC. The index of
                the table is service index which corresponds to a particular 
                service configured on the SBC and the index assigned to a
                particular H.248 controller. The other index of this table is
                csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable.
                ''',
                'csbh248statsrev1table',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbH248StatsTable', REFERENCE_CLASS, 'Csbh248Statstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable', 
                [], [], 
                '''                This table describes the H.248 statistics for SBC. The index of
                the table is service index which corresponds to a particular 
                service configured on the SBC and the index assigned to a
                particular H.248 controller. The other index of this table is
                csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable.
                This table is replaced by the csbH248StatsRev1Table.
                ''',
                'csbh248statstable',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbHistoryStatsTable', REFERENCE_CLASS, 'Csbhistorystatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable', 
                [], [], 
                '''                This table provide historical measurement in various interval
                length defined by the csbHistoryStatsInterval object. Each
                interval may contain one or more entries to allow for detailed
                measurment to be collected. It is up to the platform to
                determine the number of intervals to be supported like 
                5 minutes, 15 minutes, 1 hour and 1 day. In addition, the number
                of
                historical entries is also determined by the platform
                resources.
                
                The gauge values are reported as:
                If the period being queried is previous5mins, this is the number
                of calls that were active at the end of the previous 5 minute
                period. Otherwise for the other intevals, this is an average
                value during the summary period, sampled at 5 minute intervals.
                ''',
                'csbhistorystatstable',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            _MetaInfoClassMember('csbPerFlowStatsTable', REFERENCE_CLASS, 'Csbperflowstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB', 'CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable', 
                [], [], 
                '''                This table describes statistics table for each call flow. The
                indices of the table are virtual media gateway id, gate id,
                falow pair id and side id (indices for side A or side B). The
                other indices of this table are csbCallStatsInstanceIndex
                defined in csbCallStatsInstanceTable and
                csbCallStatsServiceIndex defined in csbCallStatsTable.
                ''',
                'csbperflowstatstable',
                'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB', False),
            ],
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            'CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB',
            _yang_ns._namespaces['CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB'
        ),
    },
}
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable.Csbcallstatsinstanceentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable.Csbcallstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable.Csbcurrperiodicstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable.Csbhistorystatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable.Csbperflowstatsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable.Csbh248Statsentry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table.Csbh248Statsrev1Entry']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatsinstancetable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcallstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbcurrperiodicstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbhistorystatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbperflowstatstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statstable']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
_meta_table['CiscoSessBorderCtrlrCallStatsMib.Csbh248Statsrev1Table']['meta_info'].parent =_meta_table['CiscoSessBorderCtrlrCallStatsMib']['meta_info']
