


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EntrystatusEnum' : _MetaInfoEnum('EntrystatusEnum', 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB',
        {
            'valid':'valid',
            'createRequest':'createRequest',
            'underCreation':'underCreation',
            'invalid':'invalid',
        }, 'TOKEN-RING-RMON-MIB', _yang_ns._namespaces['TOKEN-RING-RMON-MIB']),
    'TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry',
            False, 
            [
            _MetaInfoClassMember('tokenRingMLStatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of this object uniquely identifies this
                tokenRingMLStats entry.
                ''',
                'tokenringmlstatsindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('tokenRingMLStatsAbortErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of abort delimiters reported in
                error reporting packets detected by the probe.
                ''',
                'tokenringmlstatsaborterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsACErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of AC (Address Copied)  errors
                reported in error reporting packets detected by
                the probe.
                ''',
                'tokenringmlstatsacerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsBeaconEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times that the ring enters a
                beaconing state (beaconFrameStreamingState,
                beaconBitStreamingState,
                
                
                
                
                
                beaconSetRecoveryModeState, or
                beaconRingSignalLossState) from a non-beaconing
                state.  Note that a change of the source address
                of the beacon packet does not constitute a new
                beacon event.
                ''',
                'tokenringmlstatsbeaconevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsBeaconPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of beacon MAC packets detected
                by the probe.
                ''',
                'tokenringmlstatsbeaconpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsBeaconTime', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The total amount of time that the ring has been
                in the beaconing state.
                ''',
                'tokenringmlstatsbeacontime',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsBurstErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of burst errors reported in
                error reporting packets detected by the probe.
                ''',
                'tokenringmlstatsbursterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsClaimTokenEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times that the ring enters
                the claim token state from normal ring state or
                ring purge state.  The claim token state that
                comes in response to a beacon state is not
                counted.
                ''',
                'tokenringmlstatsclaimtokenevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsClaimTokenPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of claim token MAC packets
                detected by the probe.
                ''',
                'tokenringmlstatsclaimtokenpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsCongestionErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of receive congestion errors
                reported in error reporting packets detected by
                the probe.
                ''',
                'tokenringmlstatscongestionerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsDataSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data
                that this tokenRingMLStats entry is configured to
                analyze.  This source can be any tokenRing
                interface on this device.  In order to identify a
                particular interface, this object shall identify
                the instance of the ifIndex object, defined in
                MIB-II [3], for the desired interface.  For
                example, if an entry were to receive data from
                interface #1, this object would be set to
                ifIndex.1.
                
                The statistics in this group reflect all error
                reports on the local network segment attached to
                the identified interface.
                
                This object may not be modified if the associated
                tokenRingMLStatsStatus object is equal to
                valid(1).
                ''',
                'tokenringmlstatsdatasource',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsDropEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of events in which packets were
                dropped by the probe due to lack of resources.
                Note that this number is not necessarily the
                number of packets dropped; it is just the number
                of times this condition has been detected.  This
                value is the same as the corresponding
                tokenRingPStatsDropEvents.
                ''',
                'tokenringmlstatsdropevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsFrameCopiedErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frame copied errors reported
                in error reporting packets detected by the probe.
                ''',
                'tokenringmlstatsframecopiederrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsFrequencyErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frequency errors reported in
                error reporting packets detected by the probe.
                ''',
                'tokenringmlstatsfrequencyerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsInternalErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of adapter internal errors
                reported in error reporting packets detected by
                the probe.
                ''',
                'tokenringmlstatsinternalerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsLineErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of line errors reported in error
                reporting packets detected by the probe.
                ''',
                'tokenringmlstatslineerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsLostFrameErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of lost frame errors reported in
                error reporting packets detected by the probe.
                ''',
                'tokenringmlstatslostframeerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsMacOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets of data in MAC packets
                (excluding those that were not good frames)
                received on the network (excluding framing bits
                but including FCS octets).
                ''',
                'tokenringmlstatsmacoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsMacPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of MAC packets (excluding
                packets that were not good frames) received.
                ''',
                'tokenringmlstatsmacpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsNAUNChanges', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of NAUN changes detected by the
                probe.
                ''',
                'tokenringmlstatsnaunchanges',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'tokenringmlstatsowner',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsRingPollEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ring poll events detected by
                the probe (i.e. the number of ring polls initiated
                by the active monitor that were detected).
                ''',
                'tokenringmlstatsringpollevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsRingPurgeEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times that the ring enters
                the ring purge state from normal ring state.  The
                ring purge state that comes in response to the
                claim token or beacon state is not counted.
                ''',
                'tokenringmlstatsringpurgeevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsRingPurgePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ring purge MAC packets
                detected by probe.
                ''',
                'tokenringmlstatsringpurgepkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsSoftErrorReports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of soft error report frames
                detected by the probe.
                ''',
                'tokenringmlstatssofterrorreports',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this tokenRingMLStats entry.
                ''',
                'tokenringmlstatsstatus',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsTokenErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of token errors reported in
                error reporting packets detected by the probe.
                ''',
                'tokenringmlstatstokenerrors',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingMLStatsEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringmlstatstable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringmlstatstable',
            False, 
            [
            _MetaInfoClassMember('tokenRingMLStatsEntry', REFERENCE_LIST, 'Tokenringmlstatsentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry', 
                [], [], 
                '''                A collection of Mac-Layer statistics kept for a
                particular Token Ring interface.
                ''',
                'tokenringmlstatsentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingMLStatsTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry',
            False, 
            [
            _MetaInfoClassMember('tokenRingPStatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of this object uniquely identifies this
                tokenRingPStats entry.
                ''',
                'tokenringpstatsindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('tokenRingPStatsDataBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were directed to an LLC broadcast address
                (0xFFFFFFFFFFFF or 0xC000FFFFFFFF).
                ''',
                'tokenringpstatsdatabroadcastpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were directed to a local or global multicast
                or functional address.  Note that this number does
                not include packets directed to the broadcast
                address.
                ''',
                'tokenringpstatsdatamulticastpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets of data in good frames
                received on the network (excluding framing bits
                but including FCS octets) in non-MAC packets.
                ''',
                'tokenringpstatsdataoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of non-MAC packets in good
                frames.  received.
                ''',
                'tokenringpstatsdatapkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts1024to2047Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 1024 and 2047 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts1024to2047octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts128to255Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 128 and 255 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts128to255octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts18to63Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 18 and 63 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts18to63octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts2048to4095Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 2048 and 4095 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts2048to4095octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts256to511Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 256 and 511 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts256to511octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts4096to8191Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 4096 and 8191 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts4096to8191octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts512to1023Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 512 and 1023 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts512to1023octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts64to127Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 64 and 127 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts64to127octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPkts8192to18000Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were between 8192 and 18000 octets in length
                inclusive, excluding framing bits but including
                FCS octets.
                ''',
                'tokenringpstatsdatapkts8192to18000octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataPktsGreaterThan18000Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                that were greater than 18000 octets in length,
                excluding framing bits but including FCS octets.
                ''',
                'tokenringpstatsdatapktsgreaterthan18000octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDataSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data
                that this tokenRingPStats entry is configured to
                analyze.  This source can be any tokenRing
                interface on this device.  In order to identify a
                particular interface, this object shall identify
                the instance of the ifIndex object, defined in
                MIB-II [3], for the desired interface.  For
                example, if an entry were to receive data from
                interface #1, this object would be set to
                ifIndex.1.
                
                The statistics in this group reflect all non-MAC
                packets on the local network segment attached to
                the identified interface.
                
                This object may not be modified if the associated
                tokenRingPStatsStatus object is equal to
                valid(1).
                ''',
                'tokenringpstatsdatasource',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsDropEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of events in which packets were
                dropped by the probe due to lack of resources.
                Note that this number is not necessarily the
                number of packets dropped; it is just the number
                of times this condition has been detected.  This
                value is the same as the corresponding
                tokenRingMLStatsDropEvents
                ''',
                'tokenringpstatsdropevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'tokenringpstatsowner',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this tokenRingPStats entry.
                ''',
                'tokenringpstatsstatus',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingPStatsEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringpstatstable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringpstatstable',
            False, 
            [
            _MetaInfoClassMember('tokenRingPStatsEntry', REFERENCE_LIST, 'Tokenringpstatsentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry', 
                [], [], 
                '''                A collection of promiscuous statistics kept for
                non-MAC packets on a particular Token Ring
                interface.
                ''',
                'tokenringpstatsentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingPStatsTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry',
            False, 
            [
            _MetaInfoClassMember('tokenRingMLHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The history of which this entry is a part.  The
                history identified by a particular value of this
                index is the same history as identified by the
                same value of historyControlIndex.
                ''',
                'tokenringmlhistoryindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('tokenRingMLHistorySampleIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An index that uniquely identifies the particular
                Mac-Layer sample this entry represents among all
                Mac-Layer samples associated with the same
                historyControlEntry.  This index starts at 1 and
                increases by one as each new sample is taken.
                ''',
                'tokenringmlhistorysampleindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('tokenRingMLHistoryAbortErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of abort delimiters reported in
                error reporting packets detected by the probe
                during this sampling interval.
                ''',
                'tokenringmlhistoryaborterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryACErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of AC (Address Copied) errors
                reported in error reporting packets detected by
                the probe during this sampling interval.
                ''',
                'tokenringmlhistoryacerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryActiveStations', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of active stations on the ring
                detected by the probe during this sampling
                
                
                
                
                
                interval.
                ''',
                'tokenringmlhistoryactivestations',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryBeaconEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times that the ring enters a
                beaconing state (beaconFrameStreamingState,
                beaconBitStreamingState,
                beaconSetRecoveryModeState, or
                beaconRingSignalLossState) during this sampling
                interval.  Note that a change of the source
                address of the beacon packet does not constitute a
                new beacon event.
                ''',
                'tokenringmlhistorybeaconevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryBeaconPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of beacon MAC packets detected
                by the probe during this sampling interval.
                ''',
                'tokenringmlhistorybeaconpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryBeaconTime', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The amount of time that the ring has been in the
                beaconing state during this sampling interval.
                ''',
                'tokenringmlhistorybeacontime',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryBurstErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of burst errors reported in
                error reporting packets detected by the probe
                during this sampling interval.
                ''',
                'tokenringmlhistorybursterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryClaimTokenEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times that the ring enters
                the claim token state from normal ring state or
                ring purge state during this sampling interval.
                The claim token state that comes from the beacon
                state is not counted.
                ''',
                'tokenringmlhistoryclaimtokenevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryClaimTokenPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of claim token MAC packets
                detected by the probe during this sampling
                interval.
                ''',
                'tokenringmlhistoryclaimtokenpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryCongestionErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of receive congestion errors
                reported in error reporting packets detected by
                the probe during this sampling interval.
                ''',
                'tokenringmlhistorycongestionerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryDropEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of events in which packets were
                
                
                
                
                
                dropped by the probe due to lack of resources
                during this sampling interval.  Note that this
                number is not necessarily the number of packets
                dropped, it is just the number of times this
                condition has been detected.
                ''',
                'tokenringmlhistorydropevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryFrameCopiedErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frame copied errors reported
                in error reporting packets detected by the probe
                during this sampling interval.
                ''',
                'tokenringmlhistoryframecopiederrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryFrequencyErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frequency errors reported in
                error reporting packets detected by the probe
                during this sampling interval.
                ''',
                'tokenringmlhistoryfrequencyerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryInternalErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of adapter internal errors
                reported in error reporting packets detected by
                the probe during this sampling interval.
                ''',
                'tokenringmlhistoryinternalerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryIntervalStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the start of the
                interval over which this sample was measured.  If
                the probe keeps track of the time of day, it
                should start the first sample of the history at a
                time such that when the next hour of the day
                begins, a sample is started at that instant.  Note
                that following this rule may require the probe to
                delay collecting the first sample of the history,
                as each sample must be of the same interval.  Also
                note that the sample which is currently being
                collected is not accessible in this table until
                the end of its interval.
                ''',
                'tokenringmlhistoryintervalstart',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryLineErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of line errors reported in error
                reporting packets detected by the probe during
                this sampling interval.
                ''',
                'tokenringmlhistorylineerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryLostFrameErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of lost frame errors reported in
                error reporting packets detected by the probe
                during this sampling interval.
                ''',
                'tokenringmlhistorylostframeerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryMacOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets of data in MAC packets
                (excluding those that were not good frames)
                received on the network during this sampling
                interval (excluding framing bits but including FCS
                octets).
                ''',
                'tokenringmlhistorymacoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryMacPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of MAC packets (excluding those
                that were not good frames) received during this
                sampling interval.
                ''',
                'tokenringmlhistorymacpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryNAUNChanges', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of NAUN changes detected by the
                probe during this sampling interval.
                ''',
                'tokenringmlhistorynaunchanges',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryRingPollEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ring poll events detected by
                the probe during this sampling interval.
                ''',
                'tokenringmlhistoryringpollevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryRingPurgeEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times that the ring entered
                the ring purge state from normal ring state during
                this sampling interval.  The ring purge state that
                comes from the claim token or beacon state is not
                counted.
                ''',
                'tokenringmlhistoryringpurgeevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryRingPurgePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Ring Purge MAC packets
                detected by the probe during this sampling
                
                
                
                
                
                interval.
                ''',
                'tokenringmlhistoryringpurgepkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistorySoftErrorReports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of soft error report frames
                detected by the probe during this sampling
                interval.
                ''',
                'tokenringmlhistorysofterrorreports',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryTokenErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of token errors reported in
                error reporting packets detected by the probe
                during this sampling interval.
                ''',
                'tokenringmlhistorytokenerrors',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingMLHistoryEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringmlhistorytable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringmlhistorytable',
            False, 
            [
            _MetaInfoClassMember('tokenRingMLHistoryEntry', REFERENCE_LIST, 'Tokenringmlhistoryentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry', 
                [], [], 
                '''                A collection of Mac-Layer statistics kept for a
                particular Token Ring interface.
                ''',
                'tokenringmlhistoryentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingMLHistoryTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry',
            False, 
            [
            _MetaInfoClassMember('tokenRingPHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The history of which this entry is a part.  The
                history identified by a particular value of this
                index is the same history as identified by the
                same value of historyControlIndex.
                ''',
                'tokenringphistoryindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('tokenRingPHistorySampleIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An index that uniquely identifies the particular
                sample this entry represents among all samples
                associated with the same historyControlEntry.
                This index starts at 1 and increases by one as
                each new sample is taken.
                ''',
                'tokenringphistorysampleindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('tokenRingPHistoryDataBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were directed
                to an LLC broadcast address (0xFFFFFFFFFFFF or
                0xC000FFFFFFFF).
                ''',
                'tokenringphistorydatabroadcastpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were directed
                to a local or global multicast or functional
                address.  Note that this number does not include
                packets directed to the broadcast address.
                ''',
                'tokenringphistorydatamulticastpkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets of data in good frames
                received on the network (excluding framing bits
                but including FCS octets) in non-MAC packets
                during this sampling interval.
                ''',
                'tokenringphistorydataoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval.
                ''',
                'tokenringphistorydatapkts',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts1024to2047Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                1024 and 2047 octets in length inclusive,
                excluding framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts1024to2047octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts128to255Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                128 and 255 octets in length inclusive, excluding
                framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts128to255octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts18to63Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between 18
                and 63 octets in length inclusive, excluding
                framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts18to63octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts2048to4095Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                2048 and 4095 octets in length inclusive,
                excluding framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts2048to4095octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts256to511Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                
                
                
                
                
                256 and 511 octets in length inclusive, excluding
                framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts256to511octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts4096to8191Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                4096 and 8191 octets in length inclusive,
                excluding framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts4096to8191octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts512to1023Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                512 and 1023 octets in length inclusive, excluding
                framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts512to1023octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts64to127Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between 64
                and 127 octets in length inclusive, excluding
                framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts64to127octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPkts8192to18000Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were between
                8192 and 18000 octets in length inclusive,
                excluding framing bits but including FCS octets.
                ''',
                'tokenringphistorydatapkts8192to18000octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDataPktsGreaterThan18000Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good non-MAC frames received
                during this sampling interval that were greater
                than 18000 octets in length, excluding framing
                bits but including FCS octets.
                ''',
                'tokenringphistorydatapktsgreaterthan18000octets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryDropEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of events in which packets were
                dropped by the probe due to lack of resources
                during this sampling interval.  Note that this
                number is not necessarily the number of packets
                dropped, it is just the number of times this
                condition has been detected.
                ''',
                'tokenringphistorydropevents',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryIntervalStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the start of the
                interval over which this sample was measured.  If
                the probe keeps track of the time of day, it
                should start the first sample of the history at a
                time such that when the next hour of the day
                begins, a sample is started at that instant.  Note
                that following this rule may require the probe to
                delay collecting the first sample of the history,
                as each sample must be of the same interval.  Also
                note that the sample which is currently being
                collected is not accessible in this table until
                the end of its interval.
                ''',
                'tokenringphistoryintervalstart',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingPHistoryEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Tokenringphistorytable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Tokenringphistorytable',
            False, 
            [
            _MetaInfoClassMember('tokenRingPHistoryEntry', REFERENCE_LIST, 'Tokenringphistoryentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry', 
                [], [], 
                '''                A collection of promiscuous statistics kept for a
                particular Token Ring interface.
                ''',
                'tokenringphistoryentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'tokenRingPHistoryTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry.RingstationcontrolringstateEnum' : _MetaInfoEnum('RingstationcontrolringstateEnum', 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB',
        {
            'normalOperation':'normalOperation',
            'ringPurgeState':'ringPurgeState',
            'claimTokenState':'claimTokenState',
            'beaconFrameStreamingState':'beaconFrameStreamingState',
            'beaconBitStreamingState':'beaconBitStreamingState',
            'beaconRingSignalLossState':'beaconRingSignalLossState',
            'beaconSetRecoveryModeState':'beaconSetRecoveryModeState',
        }, 'TOKEN-RING-RMON-MIB', _yang_ns._namespaces['TOKEN-RING-RMON-MIB']),
    'TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry',
            False, 
            [
            _MetaInfoClassMember('ringStationControlIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of this object uniquely identifies the
                interface on this remote network monitoring device
                from which ringStation data is collected.  The
                interface identified by a particular value of this
                object is the same interface as identified by the
                same value of the ifIndex object, defined in MIB-
                II [3].
                ''',
                'ringstationcontrolifindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationControlActiveMonitor', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The address of the Active Monitor on this
                segment.  If this address is unknown, this object
                shall be equal to six octets of zero.
                ''',
                'ringstationcontrolactivemonitor',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlActiveStations', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of active ringStationEntries in the
                ringStationTable associated with this
                ringStationControlEntry.
                ''',
                'ringstationcontrolactivestations',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlBeaconNAUN', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The address of the NAUN in the last beacon frame
                received by the probe on this ring.  If no beacon
                frames have been received, this object shall be
                equal to six octets of zero.
                ''',
                'ringstationcontrolbeaconnaun',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlBeaconSender', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The address of the sender of the last beacon
                frame received by the probe on this ring.  If no
                beacon frames have been received, this object
                shall be equal to six octets of zero.
                ''',
                'ringstationcontrolbeaconsender',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlOrderChanges', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of add and delete events in the
                ringStationOrderTable optionally associated with
                this ringStationControlEntry.
                ''',
                'ringstationcontrolorderchanges',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'ringstationcontrolowner',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlRingState', REFERENCE_ENUM_CLASS, 'RingstationcontrolringstateEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry.RingstationcontrolringstateEnum', 
                [], [], 
                '''                The current status of this ring.
                ''',
                'ringstationcontrolringstate',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this ringStationControl entry.
                
                If this object is not equal to valid(1), all
                associated entries in the ringStationTable shall
                be deleted by the agent.
                ''',
                'ringstationcontrolstatus',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlTableSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of ringStationEntries in the
                ringStationTable associated with this
                ringStationControlEntry.
                ''',
                'ringstationcontroltablesize',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationControlEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationcontroltable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationcontroltable',
            False, 
            [
            _MetaInfoClassMember('ringStationControlEntry', REFERENCE_LIST, 'Ringstationcontrolentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry', 
                [], [], 
                '''                A list of parameters that set up the discovery of
                stations on a particular interface and the
                collection of statistics about these stations.
                ''',
                'ringstationcontrolentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationControlTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationtable.Ringstationentry.RingstationstationstatusEnum' : _MetaInfoEnum('RingstationstationstatusEnum', 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB',
        {
            'active':'active',
            'inactive':'inactive',
            'forcedRemoval':'forcedRemoval',
        }, 'TOKEN-RING-RMON-MIB', _yang_ns._namespaces['TOKEN-RING-RMON-MIB']),
    'TokenRingRmonMib.Ringstationtable.Ringstationentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationtable.Ringstationentry',
            False, 
            [
            _MetaInfoClassMember('ringStationIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object uniquely identifies the
                interface on this remote network monitoring device
                on which this station was detected.  The interface
                identified by a particular value of this object is
                the same interface as identified by the same value
                of the ifIndex object, defined in MIB-II [3].
                ''',
                'ringstationifindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationMacAddress', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The physical address of this station.
                ''',
                'ringstationmacaddress',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationAbortErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of abort delimiters reported by
                this station in error reporting packets detected
                by the probe.
                ''',
                'ringstationaborterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationACErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of AC (Address Copied) errors
                reported in error reporting packets sent by the
                nearest active downstream neighbor of this station
                and detected by the probe.
                ''',
                'ringstationacerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationCongestionErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of receive congestion errors
                reported by this station in error reporting
                packets detected by the probe.
                ''',
                'ringstationcongestionerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationDuplicateAddresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this station experienced a
                duplicate address error.
                ''',
                'ringstationduplicateaddresses',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationFrameCopiedErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frame copied errors reported
                by this station in error reporting packets
                detected by the probe.
                ''',
                'ringstationframecopiederrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationFrequencyErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frequency errors reported by
                this station in error reporting packets detected
                by the probe.
                ''',
                'ringstationfrequencyerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationInBeaconErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of beacon frames sent by this
                station and detected by the probe.
                ''',
                'ringstationinbeaconerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationInBurstErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of burst errors reported by this
                station in error reporting packets detected by the
                probe.
                ''',
                'ringstationinbursterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationInLineErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of line errors reported by this
                station in error reporting packets detected by the
                probe.
                ''',
                'ringstationinlineerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationInsertions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the probe detected this
                station inserting onto the ring.
                ''',
                'ringstationinsertions',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationInternalErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of adapter internal errors
                reported by this station in error reporting
                packets detected by the probe.
                ''',
                'ringstationinternalerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationLastEnterTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this station
                last entered the ring.  If the time is unknown,
                this value shall be zero.
                ''',
                'ringstationlastentertime',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationLastExitTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time the probe
                detected that this station last exited the ring.
                If the time is unknown, this value shall be zero.
                ''',
                'ringstationlastexittime',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationLastNAUN', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The physical address of last known NAUN of this
                station.
                ''',
                'ringstationlastnaun',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationLostFrameErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of lost frame errors reported by
                this station in error reporting packets detected
                by the probe.
                ''',
                'ringstationlostframeerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationOutBeaconErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of beacon frames detected by the
                probe that name this station as the NAUN.
                ''',
                'ringstationoutbeaconerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationOutBurstErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of burst errors reported in
                error reporting packets sent by the nearest active
                downstream neighbor of this station and detected
                by the probe.
                ''',
                'ringstationoutbursterrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationOutLineErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of line errors reported in error
                reporting packets sent by the nearest active
                downstream neighbor of this station and detected
                by the probe.
                ''',
                'ringstationoutlineerrors',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationStationStatus', REFERENCE_ENUM_CLASS, 'RingstationstationstatusEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationtable.Ringstationentry.RingstationstationstatusEnum', 
                [], [], 
                '''                The status of this station on the ring.
                ''',
                'ringstationstationstatus',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationTokenErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of token errors reported by this
                station in error reporting frames detected by the
                probe.
                ''',
                'ringstationtokenerrors',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationtable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationtable',
            False, 
            [
            _MetaInfoClassMember('ringStationEntry', REFERENCE_LIST, 'Ringstationentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationtable.Ringstationentry', 
                [], [], 
                '''                A collection of statistics for a particular
                station that has been discovered on a ring
                monitored by this device.
                ''',
                'ringstationentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationordertable.Ringstationorderentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationordertable.Ringstationorderentry',
            False, 
            [
            _MetaInfoClassMember('ringStationOrderIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object uniquely identifies the
                interface on this remote network monitoring device
                on which this station was detected.  The interface
                identified by a particular value of this object is
                the same interface as identified by the same value
                of the ifIndex object, defined in MIB-II [3].
                ''',
                'ringstationorderifindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationOrderOrderIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This index denotes the location of this station
                with respect to other stations on the ring.  This
                index is one more than the number of hops
                downstream that this station is from the rmon
                probe.  The rmon probe itself gets the value one.
                ''',
                'ringstationorderorderindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationOrderMacAddress', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The physical address of this station.
                ''',
                'ringstationordermacaddress',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationOrderEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationordertable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationordertable',
            False, 
            [
            _MetaInfoClassMember('ringStationOrderEntry', REFERENCE_LIST, 'Ringstationorderentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationordertable.Ringstationorderentry', 
                [], [], 
                '''                A collection of statistics for a particular
                
                
                
                
                
                station that is active on a ring monitored by this
                device.  This table will contain information for
                every interface that has a
                ringStationControlStatus equal to valid.
                ''',
                'ringstationorderentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationOrderTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.RingstationconfigcontrolremoveEnum' : _MetaInfoEnum('RingstationconfigcontrolremoveEnum', 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB',
        {
            'stable':'stable',
            'removing':'removing',
        }, 'TOKEN-RING-RMON-MIB', _yang_ns._namespaces['TOKEN-RING-RMON-MIB']),
    'TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.RingstationconfigcontrolupdatestatsEnum' : _MetaInfoEnum('RingstationconfigcontrolupdatestatsEnum', 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB',
        {
            'stable':'stable',
            'updating':'updating',
        }, 'TOKEN-RING-RMON-MIB', _yang_ns._namespaces['TOKEN-RING-RMON-MIB']),
    'TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry',
            False, 
            [
            _MetaInfoClassMember('ringStationConfigControlIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object uniquely identifies the
                
                
                
                
                
                interface on this remote network monitoring device
                on which this station was detected.  The interface
                identified by a particular value of this object is
                the same interface as identified by the same value
                of the ifIndex object, defined in MIB-II [3].
                ''',
                'ringstationconfigcontrolifindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationConfigControlMacAddress', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The physical address of this station.
                ''',
                'ringstationconfigcontrolmacaddress',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationConfigControlRemove', REFERENCE_ENUM_CLASS, 'RingstationconfigcontrolremoveEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.RingstationconfigcontrolremoveEnum', 
                [], [], 
                '''                Setting this object to `removing(2)' causes a
                Remove Station MAC frame to be sent.  The agent
                will set this object to `stable(1)' after
                processing the request.
                ''',
                'ringstationconfigcontrolremove',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationConfigControlUpdateStats', REFERENCE_ENUM_CLASS, 'RingstationconfigcontrolupdatestatsEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.RingstationconfigcontrolupdatestatsEnum', 
                [], [], 
                '''                Setting this object to `updating(2)' causes the
                configuration information associate with this
                entry to be updated.  The agent will set this
                object to `stable(1)' after processing the
                request.
                ''',
                'ringstationconfigcontrolupdatestats',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationConfigControlEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationconfigcontroltable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationconfigcontroltable',
            False, 
            [
            _MetaInfoClassMember('ringStationConfigControlEntry', REFERENCE_LIST, 'Ringstationconfigcontrolentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry', 
                [], [], 
                '''                This entry controls active management of stations
                by the probe.  One entry exists in this table for
                each active station in the ringStationTable.
                ''',
                'ringstationconfigcontrolentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationConfigControlTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry',
            False, 
            [
            _MetaInfoClassMember('ringStationConfigIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object uniquely identifies the
                
                
                
                
                
                interface on this remote network monitoring device
                on which this station was detected.  The interface
                identified by a particular value of this object is
                the same interface as identified by the same value
                of the ifIndex object, defined in MIB-II [3].
                ''',
                'ringstationconfigifindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationConfigMacAddress', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The physical address of this station.
                ''',
                'ringstationconfigmacaddress',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('ringStationConfigFunctionalAddress', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                the functional addresses recognized by this
                station.
                ''',
                'ringstationconfigfunctionaladdress',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationConfigGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The low-order 4 octets of the group address
                recognized by this station.
                ''',
                'ringstationconfiggroupaddress',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationConfigLocation', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The assigned physical location of this station.
                ''',
                'ringstationconfiglocation',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationConfigMicrocode', ATTRIBUTE, 'str' , None, None, 
                [(10, None)], [], 
                '''                The microcode EC level of this station.
                ''',
                'ringstationconfigmicrocode',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationConfigUpdateTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this
                configuration information was last updated
                (completely).
                ''',
                'ringstationconfigupdatetime',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationConfigEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Ringstationconfigtable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Ringstationconfigtable',
            False, 
            [
            _MetaInfoClassMember('ringStationConfigEntry', REFERENCE_LIST, 'Ringstationconfigentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry', 
                [], [], 
                '''                A collection of statistics for a particular
                station that has been discovered on a ring
                monitored by this probe.
                ''',
                'ringstationconfigentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'ringStationConfigTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry',
            False, 
            [
            _MetaInfoClassMember('sourceRoutingStatsIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object uniquely identifies the
                interface on this remote network monitoring device
                on which source routing statistics will be
                detected.  The interface identified by a
                particular value of this object is the same
                interface as identified by the same value of the
                ifIndex object, defined in MIB-II [3].
                ''',
                'sourceroutingstatsifindex',
                'TOKEN-RING-RMON-MIB', True),
            _MetaInfoClassMember('sourceRoutingStats1HopFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 1 hop, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats1hopframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats2HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 2 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats2hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats3HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 3 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats3hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats4HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 4 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats4hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats5HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 5 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats5hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats6HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 6 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats6hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats7HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 7 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats7hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStats8HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had 8 hops, were not All Route Broadcast Frames,
                and whose source or destination were on this ring
                (i.e. frames that had a RIF field and had this
                ring number in the first or last entry of the RIF
                field).
                ''',
                'sourceroutingstats8hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsAllRoutesBroadcastFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good frames received that
                were All Routes Broadcast.
                ''',
                'sourceroutingstatsallroutesbroadcastframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsAllRoutesBroadcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets in good frames
                received that were All Routes Broadcast.
                ''',
                'sourceroutingstatsallroutesbroadcastoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsInFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of frames sent into this ring from
                another ring.
                ''',
                'sourceroutingstatsinframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of octets in good frames sent into this
                ring from another ring.
                ''',
                'sourceroutingstatsinoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsLocalLLCFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received who had no
                RIF field (or had a RIF field that only included
                the local ring's number) and were not All Route
                Broadcast Frames.
                ''',
                'sourceroutingstatslocalllcframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsMoreThan8HopsFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of frames received whose route
                had more than 8 hops, were not All Route Broadcast
                Frames, and whose source or destination were on
                this ring (i.e. frames that had a RIF field and
                had this ring number in the first or last entry of
                the RIF field).
                ''',
                'sourceroutingstatsmorethan8hopsframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsOutFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of frames sent from this ring to
                another ring.
                ''',
                'sourceroutingstatsoutframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of octets in good frames sent from this
                ring to another ring.
                ''',
                'sourceroutingstatsoutoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'sourceroutingstatsowner',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsRingNumber', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The ring number of the ring monitored by this
                entry.  When any object in this entry is created,
                the probe will attempt to discover the ring
                number.  Only after the ring number is discovered
                will this object be created.  After creating an
                object in this entry, the management station
                should poll this object to detect when it is
                created.  Only after this object is created can
                the management station set the
                sourceRoutingStatsStatus entry to valid(1).
                ''',
                'sourceroutingstatsringnumber',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsSingleRouteBroadcastFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good frames received that
                were Single Route Broadcast.
                ''',
                'sourceroutingstatssingleroutebroadcastframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsSingleRoutesBroadcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets in good frames
                received that were Single Route Broadcast.
                ''',
                'sourceroutingstatssingleroutesbroadcastoctets',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this sourceRoutingStats entry.
                ''',
                'sourceroutingstatsstatus',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsThroughFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of frames sent from another ring,
                through this ring, to another ring.
                ''',
                'sourceroutingstatsthroughframes',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsThroughOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of octets in good frames sent another
                ring, through this ring, to another ring.
                ''',
                'sourceroutingstatsthroughoctets',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'sourceRoutingStatsEntry',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib.Sourceroutingstatstable' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib.Sourceroutingstatstable',
            False, 
            [
            _MetaInfoClassMember('sourceRoutingStatsEntry', REFERENCE_LIST, 'Sourceroutingstatsentry' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry', 
                [], [], 
                '''                A collection of source routing statistics kept
                for a particular Token Ring interface.
                ''',
                'sourceroutingstatsentry',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'sourceRoutingStatsTable',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
    'TokenRingRmonMib' : {
        'meta_info' : _MetaInfoClass('TokenRingRmonMib',
            False, 
            [
            _MetaInfoClassMember('ringStationConfigControlTable', REFERENCE_CLASS, 'Ringstationconfigcontroltable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationconfigcontroltable', 
                [], [], 
                '''                A list of ring station configuration control
                entries.
                ''',
                'ringstationconfigcontroltable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationConfigTable', REFERENCE_CLASS, 'Ringstationconfigtable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationconfigtable', 
                [], [], 
                '''                A list of configuration entries for stations on a
                ring monitored by this probe.
                ''',
                'ringstationconfigtable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationControlTable', REFERENCE_CLASS, 'Ringstationcontroltable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationcontroltable', 
                [], [], 
                '''                A list of ringStation table control entries.
                ''',
                'ringstationcontroltable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationOrderTable', REFERENCE_CLASS, 'Ringstationordertable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationordertable', 
                [], [], 
                '''                A list of ring station entries for stations in
                the ring poll, ordered by their ring-order.
                ''',
                'ringstationordertable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('ringStationTable', REFERENCE_CLASS, 'Ringstationtable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Ringstationtable', 
                [], [], 
                '''                A list of ring station entries.  An entry will
                exist for each station that is now or has
                
                
                
                
                
                previously been detected as physically present on
                this ring.
                ''',
                'ringstationtable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('sourceRoutingStatsTable', REFERENCE_CLASS, 'Sourceroutingstatstable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Sourceroutingstatstable', 
                [], [], 
                '''                A list of source routing statistics entries.
                ''',
                'sourceroutingstatstable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLHistoryTable', REFERENCE_CLASS, 'Tokenringmlhistorytable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringmlhistorytable', 
                [], [], 
                '''                A list of Mac-Layer Token Ring statistics
                
                
                
                
                
                entries.
                ''',
                'tokenringmlhistorytable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingMLStatsTable', REFERENCE_CLASS, 'Tokenringmlstatstable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringmlstatstable', 
                [], [], 
                '''                A list of Mac-Layer Token Ring statistics
                
                
                
                
                
                entries.
                ''',
                'tokenringmlstatstable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPHistoryTable', REFERENCE_CLASS, 'Tokenringphistorytable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringphistorytable', 
                [], [], 
                '''                A list of promiscuous Token Ring statistics
                entries.
                ''',
                'tokenringphistorytable',
                'TOKEN-RING-RMON-MIB', False),
            _MetaInfoClassMember('tokenRingPStatsTable', REFERENCE_CLASS, 'Tokenringpstatstable' , 'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TokenRingRmonMib.Tokenringpstatstable', 
                [], [], 
                '''                A list of promiscuous Token Ring statistics
                entries.
                ''',
                'tokenringpstatstable',
                'TOKEN-RING-RMON-MIB', False),
            ],
            'TOKEN-RING-RMON-MIB',
            'TOKEN-RING-RMON-MIB',
            _yang_ns._namespaces['TOKEN-RING-RMON-MIB'],
        'ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB'
        ),
    },
}
_meta_table['TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Tokenringmlstatstable']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Tokenringpstatstable']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Tokenringmlhistorytable']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Tokenringphistorytable']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Ringstationcontroltable']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationtable.Ringstationentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Ringstationtable']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationordertable.Ringstationorderentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Ringstationordertable']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Ringstationconfigcontroltable']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Ringstationconfigtable']['meta_info']
_meta_table['TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry']['meta_info'].parent =_meta_table['TokenRingRmonMib.Sourceroutingstatstable']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringmlstatstable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringpstatstable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringmlhistorytable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Tokenringphistorytable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationcontroltable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationtable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationordertable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationconfigcontroltable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Ringstationconfigtable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
_meta_table['TokenRingRmonMib.Sourceroutingstatstable']['meta_info'].parent =_meta_table['TokenRingRmonMib']['meta_info']
