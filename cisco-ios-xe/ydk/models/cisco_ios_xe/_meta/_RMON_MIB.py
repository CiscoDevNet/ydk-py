


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EntrystatusEnum' : _MetaInfoEnum('EntrystatusEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'valid':'valid',
            'createRequest':'createRequest',
            'underCreation':'underCreation',
            'invalid':'invalid',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'Rmoneventsv2Identity' : {
        'meta_info' : _MetaInfoClass('Rmoneventsv2Identity',
            False, 
            [
            ],
            'RMON-MIB',
            'rmonEventsV2',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Etherstatstable.Etherstatsentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Etherstatstable.Etherstatsentry',
            False, 
            [
            _MetaInfoClassMember('etherStatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of this object uniquely identifies this
                etherStats entry.
                ''',
                'etherstatsindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('etherStatsBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good packets received that were
                directed to the broadcast address.  Note that this
                does not include multicast packets.
                ''',
                'etherstatsbroadcastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsCollisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The best estimate of the total number of collisions
                on this Ethernet segment.
                
                The value returned will depend on the location of the
                RMON probe. Section 8.2.1.3 (10BASE-5) and section
                10.3.1.3 (10BASE-2) of IEEE standard 802.3 states that a
                station must detect a collision, in the receive mode, if
                three or more stations are transmitting simultaneously.  A
                repeater port must detect a collision when two or more
                stations are transmitting simultaneously.  Thus a probe
                placed on a repeater port could record more collisions
                than a probe connected to a station on the same segment
                would.
                
                Probe location plays a much smaller role when considering
                10BASE-T.  14.2.1.4 (10BASE-T) of IEEE standard 802.3
                defines a collision as the simultaneous presence of signals
                on the DO and RD circuits (transmitting and receiving
                at the same time).  A 10BASE-T station can only detect
                collisions when it is transmitting.  Thus probes placed on
                a station and a repeater, should report the same number of
                collisions.
                
                Note also that an RMON probe inside a repeater should
                ideally report collisions between the repeater and one or
                more other hosts (transmit collisions as defined by IEEE
                802.3k) plus receiver collisions observed on any coax
                segments to which the repeater is connected.
                ''',
                'etherstatscollisions',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsCRCAlignErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received that
                had a length (excluding framing bits, but
                including FCS octets) of between 64 and 1518
                octets, inclusive, but had either a bad
                Frame Check Sequence (FCS) with an integral
                number of octets (FCS Error) or a bad FCS with
                a non-integral number of octets (Alignment Error).
                ''',
                'etherstatscrcalignerrors',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsDataSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data that
                this etherStats entry is configured to analyze.  This
                source can be any ethernet interface on this device.
                In order to identify a particular interface, this object
                shall identify the instance of the ifIndex object,
                defined in RFC 2233 [17], for the desired interface.
                For example, if an entry were to receive data from
                interface #1, this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the identified
                interface.
                
                An agent may or may not be able to tell if fundamental
                changes to the media of the interface have occurred and
                necessitate an invalidation of this entry.  For example, a
                hot-pluggable ethernet card could be pulled out and replaced
                by a token-ring card.  In such a case, if the agent has such
                knowledge of the change, it is recommended that it
                invalidate this entry.
                
                This object may not be modified if the associated
                etherStatsStatus object is equal to valid(1).
                ''',
                'etherstatsdatasource',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsDropEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of events in which packets
                were dropped by the probe due to lack of resources.
                Note that this number is not necessarily the number of
                packets dropped; it is just the number of times this
                condition has been detected.
                ''',
                'etherstatsdropevents',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsFragments', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received that were less than
                64 octets in length (excluding framing bits but including
                FCS octets) and had either a bad Frame Check Sequence
                (FCS) with an integral number of octets (FCS Error) or a
                bad FCS with a non-integral number of octets (Alignment
                Error).
                
                Note that it is entirely normal for etherStatsFragments to
                increment.  This is because it counts both runts (which are
                normal occurrences due to collisions) and noise hits.
                ''',
                'etherstatsfragments',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsJabbers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received that were
                longer than 1518 octets (excluding framing bits,
                but including FCS octets), and had either a bad
                Frame Check Sequence (FCS) with an integral number
                of octets (FCS Error) or a bad FCS with a non-integral
                number of octets (Alignment Error).
                
                Note that this definition of jabber is different
                than the definition in IEEE-802.3 section 8.2.1.5
                (10BASE5) and section 10.3.1.4 (10BASE2).  These
                documents define jabber as the condition where any
                packet exceeds 20 ms.  The allowed range to detect
                jabber is between 20 ms and 150 ms.
                ''',
                'etherstatsjabbers',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of good packets received that were
                directed to a multicast address.  Note that this number
                does not include packets directed to the broadcast
                address.
                ''',
                'etherstatsmulticastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets of data (including
                those in bad packets) received on the
                network (excluding framing bits but including
                FCS octets).
                This object can be used as a reasonable estimate of
                10-Megabit ethernet utilization.  If greater precision is
                desired, the etherStatsPkts and etherStatsOctets objects
                should be sampled before and after a common interval.  The
                differences in the sampled values are Pkts and Octets,
                respectively, and the number of seconds in the interval is
                Interval.  These values are used to calculate the Utilization
                as follows:
                
                                 Pkts * (9.6 + 6.4) + (Octets * .8)
                 Utilization = -------------------------------------
                                         Interval * 10,000
                
                The result of this equation is the value Utilization which
                is the percent utilization of the ethernet segment on a
                scale of 0 to 100 percent.
                ''',
                'etherstatsoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsOversizePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received that were
                longer than 1518 octets (excluding framing bits,
                but including FCS octets) and were otherwise
                well formed.
                ''',
                'etherstatsoversizepkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'etherstatsowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad packets,
                broadcast packets, and multicast packets) received.
                ''',
                'etherstatspkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts1024to1518Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad
                packets) received that were between
                1024 and 1518 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts1024to1518octets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts128to255Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad
                packets) received that were between
                128 and 255 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts128to255octets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts256to511Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad
                packets) received that were between
                256 and 511 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts256to511octets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts512to1023Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad
                packets) received that were between
                512 and 1023 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts512to1023octets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts64Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad
                packets) received that were 64 octets in length
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts64octets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsPkts65to127Octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets (including bad
                packets) received that were between
                65 and 127 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts65to127octets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this etherStats entry.
                ''',
                'etherstatsstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsUndersizePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received that were
                less than 64 octets long (excluding framing bits,
                but including FCS octets) and were otherwise well
                formed.
                ''',
                'etherstatsundersizepkts',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'etherStatsEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Etherstatstable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Etherstatstable',
            False, 
            [
            _MetaInfoClassMember('etherStatsEntry', REFERENCE_LIST, 'Etherstatsentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Etherstatstable.Etherstatsentry', 
                [], [], 
                '''                A collection of statistics kept for a particular
                Ethernet interface.  As an example, an instance of the
                etherStatsPkts object might be named etherStatsPkts.1
                ''',
                'etherstatsentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'etherStatsTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Historycontroltable.Historycontrolentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Historycontroltable.Historycontrolentry',
            False, 
            [
            _MetaInfoClassMember('historyControlIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in the
                historyControl table.  Each such entry defines a
                set of samples at a particular interval for an
                interface on the device.
                ''',
                'historycontrolindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('historyControlBucketsGranted', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The number of discrete sampling intervals
                over which data shall be saved in the part of
                the media-specific table associated with this
                historyControlEntry.
                When the associated historyControlBucketsRequested
                object is created or modified, the probe
                should set this object as closely to the requested
                value as is possible for the particular
                probe implementation and available resources.  The
                probe must not lower this value except as a result
                of a modification to the associated
                historyControlBucketsRequested object.
                
                There will be times when the actual number of
                buckets associated with this entry is less than
                the value of this object.  In this case, at the
                end of each sampling interval, a new bucket will
                be added to the media-specific table.
                
                When the number of buckets reaches the value of
                this object and a new bucket is to be added to the
                media-specific table, the oldest bucket associated
                with this historyControlEntry shall be deleted by
                the agent so that the new bucket can be added.
                
                When the value of this object changes to a value less
                than the current value, entries are deleted
                from the media-specific table associated with this
                historyControlEntry.  Enough of the oldest of these
                entries shall be deleted by the agent so that their
                number remains less than or equal to the new value of
                this object.
                
                When the value of this object changes to a value greater
                than the current value, the number of associated media-
                specific entries may be allowed to grow.
                ''',
                'historycontrolbucketsgranted',
                'RMON-MIB', False),
            _MetaInfoClassMember('historyControlBucketsRequested', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The requested number of discrete time intervals
                over which data is to be saved in the part of the
                media-specific table associated with this
                historyControlEntry.
                
                When this object is created or modified, the probe
                should set historyControlBucketsGranted as closely to
                this object as is possible for the particular probe
                implementation and available resources.
                ''',
                'historycontrolbucketsrequested',
                'RMON-MIB', False),
            _MetaInfoClassMember('historyControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data for
                which historical data was collected and
                placed in a media-specific table on behalf of this
                historyControlEntry.  This source can be any
                interface on this device.  In order to identify
                a particular interface, this object shall identify
                the instance of the ifIndex object, defined
                in  RFC 2233 [17], for the desired interface.
                For example, if an entry were to receive data from
                interface #1, this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the identified
                interface.
                
                An agent may or may not be able to tell if fundamental
                changes to the media of the interface have occurred and
                necessitate an invalidation of this entry.  For example, a
                hot-pluggable ethernet card could be pulled out and replaced
                by a token-ring card.  In such a case, if the agent has such
                knowledge of the change, it is recommended that it
                invalidate this entry.
                
                This object may not be modified if the associated
                historyControlStatus object is equal to valid(1).
                ''',
                'historycontroldatasource',
                'RMON-MIB', False),
            _MetaInfoClassMember('historyControlInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                The interval in seconds over which the data is
                sampled for each bucket in the part of the
                media-specific table associated with this
                historyControlEntry.  This interval can
                be set to any number of seconds between 1 and
                3600 (1 hour).
                
                Because the counters in a bucket may overflow at their
                maximum value with no indication, a prudent manager will
                take into account the possibility of overflow in any of
                the associated counters.  It is important to consider the
                minimum time in which any counter could overflow on a
                particular media type and set the historyControlInterval
                object to a value less than this interval.  This is
                typically most important for the 'octets' counter in any
                media-specific table.  For example, on an Ethernet
                network, the etherHistoryOctets counter could overflow
                in about one hour at the Ethernet's maximum
                utilization.
                
                This object may not be modified if the associated
                historyControlStatus object is equal to valid(1).
                ''',
                'historycontrolinterval',
                'RMON-MIB', False),
            _MetaInfoClassMember('historyControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'historycontrolowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('historyControlStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this historyControl entry.
                
                Each instance of the media-specific table associated
                with this historyControlEntry will be deleted by the agent
                if this historyControlEntry is not equal to valid(1).
                ''',
                'historycontrolstatus',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'historyControlEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Historycontroltable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Historycontroltable',
            False, 
            [
            _MetaInfoClassMember('historyControlEntry', REFERENCE_LIST, 'Historycontrolentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Historycontroltable.Historycontrolentry', 
                [], [], 
                '''                A list of parameters that set up a periodic sampling of
                statistics.  As an example, an instance of the
                historyControlInterval object might be named
                historyControlInterval.2
                ''',
                'historycontrolentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'historyControlTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Etherhistorytable.Etherhistoryentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Etherhistorytable.Etherhistoryentry',
            False, 
            [
            _MetaInfoClassMember('etherHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The history of which this entry is a part.  The
                history identified by a particular value of this
                index is the same history as identified
                by the same value of historyControlIndex.
                ''',
                'etherhistoryindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('etherHistorySampleIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index that uniquely identifies the particular
                sample this entry represents among all samples
                associated with the same historyControlEntry.
                This index starts at 1 and increases by one
                as each new sample is taken.
                ''',
                'etherhistorysampleindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('etherHistoryBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets received during this
                sampling interval that were directed to the
                broadcast address.
                ''',
                'etherhistorybroadcastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryCollisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The best estimate of the total number of collisions
                on this Ethernet segment during this sampling
                interval.
                
                The value returned will depend on the location of the
                RMON probe. Section 8.2.1.3 (10BASE-5) and section
                10.3.1.3 (10BASE-2) of IEEE standard 802.3 states that a
                station must detect a collision, in the receive mode, if
                three or more stations are transmitting simultaneously.  A
                repeater port must detect a collision when two or more
                stations are transmitting simultaneously.  Thus a probe
                placed on a repeater port could record more collisions
                than a probe connected to a station on the same segment
                would.
                
                Probe location plays a much smaller role when considering
                10BASE-T.  14.2.1.4 (10BASE-T) of IEEE standard 802.3
                defines a collision as the simultaneous presence of signals
                on the DO and RD circuits (transmitting and receiving
                at the same time).  A 10BASE-T station can only detect
                collisions when it is transmitting.  Thus probes placed on
                a station and a repeater, should report the same number of
                collisions.
                
                Note also that an RMON probe inside a repeater should
                ideally report collisions between the repeater and one or
                more other hosts (transmit collisions as defined by IEEE
                802.3k) plus receiver collisions observed on any coax
                segments to which the repeater is connected.
                ''',
                'etherhistorycollisions',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryCRCAlignErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets received during this
                sampling interval that had a length (excluding
                framing bits but including FCS octets) between
                64 and 1518 octets, inclusive, but had either a bad Frame
                Check Sequence (FCS) with an integral number of octets
                (FCS Error) or a bad FCS with a non-integral number
                of octets (Alignment Error).
                ''',
                'etherhistorycrcalignerrors',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryDropEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of events in which packets
                were dropped by the probe due to lack of resources
                during this sampling interval.  Note that this number
                is not necessarily the number of packets dropped, it
                is just the number of times this condition has been
                detected.
                ''',
                'etherhistorydropevents',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryFragments', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets received during this
                sampling interval that were less than 64 octets in
                length (excluding framing bits but including FCS
                octets) had either a bad Frame Check Sequence (FCS)
                with an integral number of octets (FCS Error) or a bad
                FCS with a non-integral number of octets (Alignment
                Error).
                
                Note that it is entirely normal for etherHistoryFragments to
                increment.  This is because it counts both runts (which are
                normal occurrences due to collisions) and noise hits.
                ''',
                'etherhistoryfragments',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryIntervalStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the start of the interval
                over which this sample was measured.  If the probe
                keeps track of the time of day, it should start
                the first sample of the history at a time such that
                when the next hour of the day begins, a sample is
                started at that instant.  Note that following this
                rule may require the probe to delay collecting the
                first sample of the history, as each sample must be
                of the same interval.  Also note that the sample which
                is currently being collected is not accessible in this
                table until the end of its interval.
                ''',
                'etherhistoryintervalstart',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryJabbers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets received during this
                sampling interval that were longer than 1518 octets
                (excluding framing bits but including FCS octets),
                and  had either a bad Frame Check Sequence (FCS)
                with an integral number of octets (FCS Error) or
                a bad FCS with a non-integral number of octets
                (Alignment Error).
                
                Note that this definition of jabber is different
                than the definition in IEEE-802.3 section 8.2.1.5
                (10BASE5) and section 10.3.1.4 (10BASE2).  These
                documents define jabber as the condition where any
                packet exceeds 20 ms.  The allowed range to detect
                jabber is between 20 ms and 150 ms.
                ''',
                'etherhistoryjabbers',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets received during this
                sampling interval that were directed to a
                multicast address.  Note that this number does not
                include packets addressed to the broadcast address.
                ''',
                'etherhistorymulticastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets of data (including
                those in bad packets) received on the
                network (excluding framing bits but including
                FCS octets).
                ''',
                'etherhistoryoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryOversizePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets received during this
                sampling interval that were longer than 1518
                octets (excluding framing bits but including
                FCS octets) but were otherwise well formed.
                ''',
                'etherhistoryoversizepkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets (including bad packets)
                received during this sampling interval.
                ''',
                'etherhistorypkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryUndersizePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets received during this
                sampling interval that were less than 64 octets
                long (excluding framing bits but including FCS
                octets) and were otherwise well formed.
                ''',
                'etherhistoryundersizepkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryUtilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                The best estimate of the mean physical layer
                network utilization on this interface during this
                sampling interval, in hundredths of a percent.
                ''',
                'etherhistoryutilization',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'etherHistoryEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Etherhistorytable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Etherhistorytable',
            False, 
            [
            _MetaInfoClassMember('etherHistoryEntry', REFERENCE_LIST, 'Etherhistoryentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Etherhistorytable.Etherhistoryentry', 
                [], [], 
                '''                An historical sample of Ethernet statistics on a particular
                Ethernet interface.  This sample is associated with the
                historyControlEntry which set up the parameters for
                a regular collection of these samples.  As an example, an
                instance of the etherHistoryPkts object might be named
                etherHistoryPkts.2.89
                ''',
                'etherhistoryentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'etherHistoryTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Alarmtable.Alarmentry.AlarmsampletypeEnum' : _MetaInfoEnum('AlarmsampletypeEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'absoluteValue':'absoluteValue',
            'deltaValue':'deltaValue',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Alarmtable.Alarmentry.AlarmstartupalarmEnum' : _MetaInfoEnum('AlarmstartupalarmEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'risingAlarm':'risingAlarm',
            'fallingAlarm':'fallingAlarm',
            'risingOrFallingAlarm':'risingOrFallingAlarm',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Alarmtable.Alarmentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Alarmtable.Alarmentry',
            False, 
            [
            _MetaInfoClassMember('alarmIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in the
                alarm table.  Each such entry defines a
                diagnostic sample at a particular interval
                for an object on the device.
                ''',
                'alarmindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('alarmFallingEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The index of the eventEntry that is
                used when a falling threshold is crossed.  The
                eventEntry identified by a particular value of
                this index is the same as identified by the same value
                of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then
                no association exists.  In particular, if this value
                is zero, no associated event will be generated, as
                zero is not a valid event index.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmfallingeventindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmFallingThreshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A threshold for the sampled statistic.  When the current
                sampled value is less than or equal to this threshold,
                and the value at the last sampling interval was greater than
                this threshold, a single event will be generated.
                A single event will also be generated if the first
                sample after this entry becomes valid is less than or
                equal to this threshold and the associated
                alarmStartupAlarm is equal to fallingAlarm(2) or
                risingOrFallingAlarm(3).
                
                After a falling event is generated, another such event
                will not be generated until the sampled value
                rises above this threshold and reaches the
                alarmRisingThreshold.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmfallingthreshold',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmInterval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The interval in seconds over which the data is
                sampled and compared with the rising and falling
                thresholds.  When setting this variable, care
                should be taken in the case of deltaValue
                sampling - the interval should be set short enough
                that the sampled variable is very unlikely to
                increase or decrease by more than 2^31 - 1 during
                a single sampling interval.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarminterval',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'alarmowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmRisingEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The index of the eventEntry that is
                used when a rising threshold is crossed.  The
                eventEntry identified by a particular value of
                this index is the same as identified by the same value
                of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then
                no association exists.  In particular, if this value
                is zero, no associated event will be generated, as
                zero is not a valid event index.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmrisingeventindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmRisingThreshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A threshold for the sampled statistic.  When the current
                sampled value is greater than or equal to this threshold,
                and the value at the last sampling interval was less than
                this threshold, a single event will be generated.
                A single event will also be generated if the first
                sample after this entry becomes valid is greater than or
                equal to this threshold and the associated
                alarmStartupAlarm is equal to risingAlarm(1) or
                risingOrFallingAlarm(3).
                
                After a rising event is generated, another such event
                will not be generated until the sampled value
                falls below this threshold and reaches the
                alarmFallingThreshold.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmrisingthreshold',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmSampleType', REFERENCE_ENUM_CLASS, 'AlarmsampletypeEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Alarmtable.Alarmentry.AlarmsampletypeEnum', 
                [], [], 
                '''                The method of sampling the selected variable and
                calculating the value to be compared against the
                thresholds.  If the value of this object is
                absoluteValue(1), the value of the selected variable
                will be compared directly with the thresholds at the
                end of the sampling interval.  If the value of this
                object is deltaValue(2), the value of the selected
                variable at the last sample will be subtracted from
                the current value, and the difference compared with
                the thresholds.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmsampletype',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmStartupAlarm', REFERENCE_ENUM_CLASS, 'AlarmstartupalarmEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Alarmtable.Alarmentry.AlarmstartupalarmEnum', 
                [], [], 
                '''                The alarm that may be sent when this entry is first
                set to valid.  If the first sample after this entry
                becomes valid is greater than or equal to the
                risingThreshold and alarmStartupAlarm is equal to
                risingAlarm(1) or risingOrFallingAlarm(3), then a single
                rising alarm will be generated.  If the first sample
                after this entry becomes valid is less than or equal
                to the fallingThreshold and alarmStartupAlarm is equal
                to fallingAlarm(2) or risingOrFallingAlarm(3), then a
                single falling alarm will be generated.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmstartupalarm',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this alarm entry.
                ''',
                'alarmstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmValue', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of the statistic during the last sampling
                period.  For example, if the sample type is deltaValue,
                this value will be the difference between the samples
                at the beginning and end of the period.  If the sample
                type is absoluteValue, this value will be the sampled
                value at the end of the period.
                This is the value that is compared with the rising and
                falling thresholds.
                
                The value during the current sampling period is not
                made available until the period is completed and will
                remain available until the next period completes.
                ''',
                'alarmvalue',
                'RMON-MIB', False),
            _MetaInfoClassMember('alarmVariable', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier of the particular variable to be
                sampled.  Only variables that resolve to an ASN.1 primitive
                type of INTEGER (INTEGER, Integer32, Counter32, Counter64,
                Gauge, or TimeTicks) may be sampled.
                
                Because SNMP access control is articulated entirely
                in terms of the contents of MIB views, no access
                control mechanism exists that can restrict the value of
                this object to identify only those objects that exist
                in a particular MIB view.  Because there is thus no
                acceptable means of restricting the read access that
                could be obtained through the alarm mechanism, the
                probe must only grant write access to this object in
                those views that have read access to all objects on
                the probe.
                
                During a set operation, if the supplied variable name is
                not available in the selected MIB view, a badValue error
                must be returned.  If at any time the variable name of
                an established alarmEntry is no longer available in the
                selected MIB view, the probe must change the status of
                this alarmEntry to invalid(4).
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmvariable',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'alarmEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Alarmtable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Alarmtable',
            False, 
            [
            _MetaInfoClassMember('alarmEntry', REFERENCE_LIST, 'Alarmentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Alarmtable.Alarmentry', 
                [], [], 
                '''                A list of parameters that set up a periodic checking
                for alarm conditions.  For example, an instance of the
                alarmValue object might be named alarmValue.8
                ''',
                'alarmentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'alarmTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hostcontroltable.Hostcontrolentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hostcontroltable.Hostcontrolentry',
            False, 
            [
            _MetaInfoClassMember('hostControlIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in the
                hostControl table.  Each such entry defines
                a function that discovers hosts on a particular interface
                and places statistics about them in the hostTable and
                the hostTimeTable on behalf of this hostControlEntry.
                ''',
                'hostcontrolindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data for
                this instance of the host function.  This source
                can be any interface on this device.  In order
                to identify a particular interface, this object shall
                identify the instance of the ifIndex object, defined
                in RFC 2233 [17], for the desired interface.
                For example, if an entry were to receive data from
                interface #1, this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the identified
                interface.
                
                An agent may or may not be able to tell if fundamental
                changes to the media of the interface have occurred and
                necessitate an invalidation of this entry.  For example, a
                hot-pluggable ethernet card could be pulled out and replaced
                by a token-ring card.  In such a case, if the agent has such
                knowledge of the change, it is recommended that it
                invalidate this entry.
                
                This object may not be modified if the associated
                hostControlStatus object is equal to valid(1).
                ''',
                'hostcontroldatasource',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostControlLastDeleteTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the last entry
                was deleted from the portion of the hostTable
                associated with this hostControlEntry.  If no
                deletions have occurred, this value shall be zero.
                ''',
                'hostcontrollastdeletetime',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'hostcontrolowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostControlStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this hostControl entry.
                
                If this object is not equal to valid(1), all associated
                entries in the hostTable, hostTimeTable, and the
                hostTopNTable shall be deleted by the agent.
                ''',
                'hostcontrolstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostControlTableSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of hostEntries in the hostTable and the
                hostTimeTable associated with this hostControlEntry.
                ''',
                'hostcontroltablesize',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostControlEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hostcontroltable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hostcontroltable',
            False, 
            [
            _MetaInfoClassMember('hostControlEntry', REFERENCE_LIST, 'Hostcontrolentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hostcontroltable.Hostcontrolentry', 
                [], [], 
                '''                A list of parameters that set up the discovery of hosts
                on a particular interface and the collection of statistics
                about these hosts.  For example, an instance of the
                hostControlTableSize object might be named
                hostControlTableSize.1
                ''',
                'hostcontrolentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostControlTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttable.Hostentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttable.Hostentry',
            False, 
            [
            _MetaInfoClassMember('hostIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The set of collected host statistics of which
                this entry is a part.  The set of hosts
                identified by a particular value of this
                index is associated with the hostControlEntry
                as identified by the same value of hostControlIndex.
                ''',
                'hostindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The physical address of this host.
                ''',
                'hostaddress',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostCreationOrder', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that defines the relative ordering of
                the creation time of hosts captured for a
                particular hostControlEntry.  This index shall
                be between 1 and N, where N is the value of
                the associated hostControlTableSize.  The ordering
                of the indexes is based on the order of each entry's
                insertion into the table, in which entries added earlier
                have a lower index value than entries added later.
                
                It is important to note that the order for a
                particular entry may change as an (earlier) entry
                is deleted from the table.  Because this order may
                change, management stations should make use of the
                hostControlLastDeleteTime variable in the
                hostControlEntry associated with the relevant
                portion of the hostTable.  By observing
                this variable, the management station may detect
                the circumstances where a previous association
                between a value of hostCreationOrder
                and a hostEntry may no longer hold.
                ''',
                'hostcreationorder',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets transmitted to this address since
                it was added to the hostTable (excluding framing
                bits but including FCS octets), except for those
                octets in bad packets.
                ''',
                'hostinoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets transmitted to this
                address since it was added to the hostTable.
                ''',
                'hostinpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostOutBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets transmitted by this
                address that were directed to the broadcast address
                since this host was added to the hostTable.
                ''',
                'hostoutbroadcastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostOutErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bad packets transmitted by this address
                since this host was added to the hostTable.
                ''',
                'hostouterrors',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostOutMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets transmitted by this
                address that were directed to a multicast address
                since this host was added to the hostTable.
                Note that this number does not include packets
                directed to the broadcast address.
                ''',
                'hostoutmulticastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets transmitted by this address since
                it was added to the hostTable (excluding framing
                bits but including FCS octets), including those
                octets in bad packets.
                ''',
                'hostoutoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets, including bad packets, transmitted
                by this address since it was added to the hostTable.
                ''',
                'hostoutpkts',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttable',
            False, 
            [
            _MetaInfoClassMember('hostEntry', REFERENCE_LIST, 'Hostentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttable.Hostentry', 
                [], [], 
                '''                A collection of statistics for a particular host that has
                been discovered on an interface of this device.  For example,
                an instance of the hostOutBroadcastPkts object might be
                named hostOutBroadcastPkts.1.6.8.0.32.27.3.176
                ''',
                'hostentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttimetable.Hosttimeentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttimetable.Hosttimeentry',
            False, 
            [
            _MetaInfoClassMember('hostTimeIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The set of collected host statistics of which
                this entry is a part.  The set of hosts
                identified by a particular value of this
                index is associated with the hostControlEntry
                as identified by the same value of hostControlIndex.
                ''',
                'hosttimeindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostTimeCreationOrder', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in
                the hostTime table among those entries associated
                with the same hostControlEntry.  This index shall
                be between 1 and N, where N is the value of
                the associated hostControlTableSize.  The ordering
                of the indexes is based on the order of each entry's
                insertion into the table, in which entries added earlier
                have a lower index value than entries added later.
                Thus the management station has the ability to
                learn of new entries added to this table without
                downloading the entire table.
                
                It is important to note that the index for a
                particular entry may change as an (earlier) entry
                is deleted from the table.  Because this order may
                change, management stations should make use of the
                hostControlLastDeleteTime variable in the
                hostControlEntry associated with the relevant
                portion of the hostTimeTable.  By observing
                this variable, the management station may detect
                the circumstances where a download of the table
                may have missed entries, and where a previous
                association between a value of hostTimeCreationOrder
                and a hostTimeEntry may no longer hold.
                ''',
                'hosttimecreationorder',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostTimeAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The physical address of this host.
                ''',
                'hosttimeaddress',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets transmitted to this address since
                it was added to the hostTimeTable (excluding framing
                bits but including FCS octets), except for those
                octets in bad packets.
                ''',
                'hosttimeinoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets transmitted to this
                address since it was added to the hostTimeTable.
                ''',
                'hosttimeinpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeOutBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets transmitted by this
                address that were directed to the broadcast address
                since this host was added to the hostTimeTable.
                ''',
                'hosttimeoutbroadcastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeOutErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bad packets transmitted by this address
                since this host was added to the hostTimeTable.
                ''',
                'hosttimeouterrors',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeOutMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of good packets transmitted by this
                address that were directed to a multicast address
                since this host was added to the hostTimeTable.
                Note that this number does not include packets directed
                to the broadcast address.
                ''',
                'hosttimeoutmulticastpkts',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets transmitted by this address since
                it was added to the hostTimeTable (excluding framing
                bits but including FCS octets), including those
                octets in bad packets.
                ''',
                'hosttimeoutoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets, including bad packets, transmitted
                by this address since it was added to the hostTimeTable.
                ''',
                'hosttimeoutpkts',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTimeEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttimetable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttimetable',
            False, 
            [
            _MetaInfoClassMember('hostTimeEntry', REFERENCE_LIST, 'Hosttimeentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttimetable.Hosttimeentry', 
                [], [], 
                '''                A collection of statistics for a particular host that has
                been discovered on an interface of this device.  This
                collection includes the relative ordering of the creation
                time of this object.  For example, an instance of the
                hostTimeOutBroadcastPkts object might be named
                hostTimeOutBroadcastPkts.1.687
                ''',
                'hosttimeentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTimeTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttopncontroltable.Hosttopncontrolentry.HosttopnratebaseEnum' : _MetaInfoEnum('HosttopnratebaseEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'hostTopNInPkts':'hostTopNInPkts',
            'hostTopNOutPkts':'hostTopNOutPkts',
            'hostTopNInOctets':'hostTopNInOctets',
            'hostTopNOutOctets':'hostTopNOutOctets',
            'hostTopNOutErrors':'hostTopNOutErrors',
            'hostTopNOutBroadcastPkts':'hostTopNOutBroadcastPkts',
            'hostTopNOutMulticastPkts':'hostTopNOutMulticastPkts',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Hosttopncontroltable.Hosttopncontrolentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttopncontroltable.Hosttopncontrolentry',
            False, 
            [
            _MetaInfoClassMember('hostTopNControlIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry
                in the hostTopNControl table.  Each such
                entry defines one top N report prepared for
                one interface.
                ''',
                'hosttopncontrolindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostTopNDuration', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of seconds that this report has collected
                during the last sampling interval, or if this
                report is currently being collected, the number
                of seconds that this report is being collected
                during this sampling interval.
                
                When the associated hostTopNTimeRemaining object is set,
                this object shall be set by the probe to the same value
                and shall not be modified until the next time
                the hostTopNTimeRemaining is set.
                
                This value shall be zero if no reports have been
                requested for this hostTopNControlEntry.
                ''',
                'hosttopnduration',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNGrantedSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of hosts in the top N table.
                
                When the associated hostTopNRequestedSize object is
                created or modified, the probe should set this
                object as closely to the requested value as is possible
                for the particular implementation and available
                resources. The probe must not lower this value except
                as a result of a set to the associated
                hostTopNRequestedSize object.
                
                Hosts with the highest value of hostTopNRate shall be
                placed in this table in decreasing order of this rate
                until there is no more room or until there are no more
                hosts.
                ''',
                'hosttopngrantedsize',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNHostIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The host table for which a top N report will be prepared
                on behalf of this entry.  The host table identified by a
                particular value of this index is associated with the same
                host table as identified by the same value of
                hostIndex.
                
                This object may not be modified if the associated
                hostTopNStatus object is equal to valid(1).
                ''',
                'hosttopnhostindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'hosttopnowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNRateBase', REFERENCE_ENUM_CLASS, 'HosttopnratebaseEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttopncontroltable.Hosttopncontrolentry.HosttopnratebaseEnum', 
                [], [], 
                '''                The variable for each host that the hostTopNRate
                variable is based upon.
                
                This object may not be modified if the associated
                hostTopNStatus object is equal to valid(1).
                ''',
                'hosttopnratebase',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNRequestedSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of hosts requested for the top N
                table.
                
                When this object is created or modified, the probe
                should set hostTopNGrantedSize as closely to this
                object as is possible for the particular probe
                implementation and available resources.
                ''',
                'hosttopnrequestedsize',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNStartTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when this top N report was
                last started.  In other words, this is the time that
                the associated hostTopNTimeRemaining object was
                modified to start the requested report.
                ''',
                'hosttopnstarttime',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this hostTopNControl entry.
                
                If this object is not equal to valid(1), all associated
                hostTopNEntries shall be deleted by the agent.
                ''',
                'hosttopnstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNTimeRemaining', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of seconds left in the report currently being
                collected.  When this object is modified by the management
                station, a new collection is started, possibly aborting
                a currently running report.  The new value is used
                as the requested duration of this report, which is
                loaded into the associated hostTopNDuration object.
                
                When this object is set to a non-zero value, any
                associated hostTopNEntries shall be made
                inaccessible by the monitor.  While the value of this
                object is non-zero, it decrements by one per second until
                it reaches zero.  During this time, all associated
                hostTopNEntries shall remain inaccessible.  At the time
                that this object decrements to zero, the report is made
                accessible in the hostTopNTable.  Thus, the hostTopN
                table needs to be created only at the end of the collection
                interval.
                ''',
                'hosttopntimeremaining',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTopNControlEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttopncontroltable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttopncontroltable',
            False, 
            [
            _MetaInfoClassMember('hostTopNControlEntry', REFERENCE_LIST, 'Hosttopncontrolentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttopncontroltable.Hosttopncontrolentry', 
                [], [], 
                '''                A set of parameters that control the creation of a report
                of the top N hosts according to several metrics.  For
                example, an instance of the hostTopNDuration object might
                be named hostTopNDuration.3
                ''',
                'hosttopncontrolentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTopNControlTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttopntable.Hosttopnentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttopntable.Hosttopnentry',
            False, 
            [
            _MetaInfoClassMember('hostTopNReport', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object identifies the top N report of which
                this entry is a part.  The set of hosts
                identified by a particular value of this
                object is part of the same report as identified
                by the same value of the hostTopNControlIndex object.
                ''',
                'hosttopnreport',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostTopNIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in
                the hostTopN table among those in the same report.
                This index is between 1 and N, where N is the
                number of entries in this table.  Increasing values
                of hostTopNIndex shall be assigned to entries with
                decreasing values of hostTopNRate until index N
                is assigned to the entry with the lowest value of
                hostTopNRate or there are no more hostTopNEntries.
                ''',
                'hosttopnindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('hostTopNAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The physical address of this host.
                ''',
                'hosttopnaddress',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNRate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The amount of change in the selected variable
                during this sampling interval.  The selected
                variable is this host's instance of the object
                selected by hostTopNRateBase.
                ''',
                'hosttopnrate',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTopNEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Hosttopntable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Hosttopntable',
            False, 
            [
            _MetaInfoClassMember('hostTopNEntry', REFERENCE_LIST, 'Hosttopnentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttopntable.Hosttopnentry', 
                [], [], 
                '''                A set of statistics for a host that is part of a top N
                report.  For example, an instance of the hostTopNRate
                object might be named hostTopNRate.3.10
                ''',
                'hosttopnentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'hostTopNTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Matrixcontroltable.Matrixcontrolentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Matrixcontroltable.Matrixcontrolentry',
            False, 
            [
            _MetaInfoClassMember('matrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in the
                matrixControl table.  Each such entry defines
                a function that discovers conversations on a particular
                interface and places statistics about them in the
                matrixSDTable and the matrixDSTable on behalf of this
                matrixControlEntry.
                ''',
                'matrixcontrolindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of
                the data from which this entry creates a traffic matrix.
                This source can be any interface on this device.  In
                order to identify a particular interface, this object
                shall identify the instance of the ifIndex object,
                defined in RFC 2233 [17], for the desired
                interface.  For example, if an entry were to receive data
                from interface #1, this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the identified
                interface.
                
                An agent may or may not be able to tell if fundamental
                changes to the media of the interface have occurred and
                necessitate an invalidation of this entry.  For example, a
                hot-pluggable ethernet card could be pulled out and replaced
                by a token-ring card.  In such a case, if the agent has such
                knowledge of the change, it is recommended that it
                invalidate this entry.
                
                This object may not be modified if the associated
                matrixControlStatus object is equal to valid(1).
                ''',
                'matrixcontroldatasource',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixControlLastDeleteTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the last entry
                was deleted from the portion of the matrixSDTable
                or matrixDSTable associated with this matrixControlEntry.
                If no deletions have occurred, this value shall be
                zero.
                ''',
                'matrixcontrollastdeletetime',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'matrixcontrolowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixControlStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this matrixControl entry.
                If this object is not equal to valid(1), all associated
                entries in the matrixSDTable and the matrixDSTable
                shall be deleted by the agent.
                ''',
                'matrixcontrolstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixControlTableSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of matrixSDEntries in the matrixSDTable
                for this interface.  This must also be the value of
                the number of entries in the matrixDSTable for this
                interface.
                ''',
                'matrixcontroltablesize',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'matrixControlEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Matrixcontroltable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Matrixcontroltable',
            False, 
            [
            _MetaInfoClassMember('matrixControlEntry', REFERENCE_LIST, 'Matrixcontrolentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Matrixcontroltable.Matrixcontrolentry', 
                [], [], 
                '''                Information about a traffic matrix on a particular
                interface.  For example, an instance of the
                matrixControlLastDeleteTime object might be named
                matrixControlLastDeleteTime.1
                ''',
                'matrixcontrolentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'matrixControlTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Matrixsdtable.Matrixsdentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Matrixsdtable.Matrixsdentry',
            False, 
            [
            _MetaInfoClassMember('matrixSDIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The set of collected matrix statistics of which
                this entry is a part.  The set of matrix statistics
                identified by a particular value of this index
                is associated with the same matrixControlEntry
                as identified by the same value of matrixControlIndex.
                ''',
                'matrixsdindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixSDSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The source physical address.
                ''',
                'matrixsdsourceaddress',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixSDDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination physical address.
                ''',
                'matrixsddestaddress',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixSDErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bad packets transmitted from
                the source address to the destination address.
                ''',
                'matrixsderrors',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixSDOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets (excluding framing bits but
                including FCS octets) contained in all packets
                transmitted from the source address to the
                destination address.
                ''',
                'matrixsdoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixSDPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets transmitted from the source
                address to the destination address (this number includes
                bad packets).
                ''',
                'matrixsdpkts',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'matrixSDEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Matrixsdtable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Matrixsdtable',
            False, 
            [
            _MetaInfoClassMember('matrixSDEntry', REFERENCE_LIST, 'Matrixsdentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Matrixsdtable.Matrixsdentry', 
                [], [], 
                '''                A collection of statistics for communications between
                two addresses on a particular interface.  For example,
                an instance of the matrixSDPkts object might be named
                matrixSDPkts.1.6.8.0.32.27.3.176.6.8.0.32.10.8.113
                ''',
                'matrixsdentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'matrixSDTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Matrixdstable.Matrixdsentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Matrixdstable.Matrixdsentry',
            False, 
            [
            _MetaInfoClassMember('matrixDSIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The set of collected matrix statistics of which
                this entry is a part.  The set of matrix statistics
                identified by a particular value of this index
                is associated with the same matrixControlEntry
                as identified by the same value of matrixControlIndex.
                ''',
                'matrixdsindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixDSDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination physical address.
                ''',
                'matrixdsdestaddress',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixDSSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The source physical address.
                ''',
                'matrixdssourceaddress',
                'RMON-MIB', True),
            _MetaInfoClassMember('matrixDSErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bad packets transmitted from
                the source address to the destination address.
                ''',
                'matrixdserrors',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixDSOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets (excluding framing bits
                but including FCS octets) contained in all packets
                transmitted from the source address to the
                destination address.
                ''',
                'matrixdsoctets',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixDSPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets transmitted from the source
                address to the destination address (this number includes
                bad packets).
                ''',
                'matrixdspkts',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'matrixDSEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Matrixdstable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Matrixdstable',
            False, 
            [
            _MetaInfoClassMember('matrixDSEntry', REFERENCE_LIST, 'Matrixdsentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Matrixdstable.Matrixdsentry', 
                [], [], 
                '''                A collection of statistics for communications between
                two addresses on a particular interface.  For example,
                an instance of the matrixSDPkts object might be named
                matrixSDPkts.1.6.8.0.32.10.8.113.6.8.0.32.27.3.176
                ''',
                'matrixdsentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'matrixDSTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Filtertable.Filterentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Filtertable.Filterentry',
            False, 
            [
            _MetaInfoClassMember('filterIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry
                in the filter table.  Each such entry defines
                one filter that is to be applied to every packet
                received on an interface.
                ''',
                'filterindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('filterChannelIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object identifies the channel of which this filter
                is a part.  The filters identified by a particular value
                of this object are associated with the same channel as
                identified by the same value of the channelIndex object.
                ''',
                'filterchannelindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'filterowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktData', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The data that is to be matched with the input packet.
                For each packet received, this filter and the accompanying
                filterPktDataMask and filterPktDataNotMask will be
                adjusted for the offset.  The only bits relevant to this
                match algorithm are those that have the corresponding
                filterPktDataMask bit equal to one.  The following three
                rules are then applied to every packet:
                
                (1) If the packet is too short and does not have data
                    corresponding to part of the filterPktData, the packet
                    will fail this data match.
                
                (2) For each relevant bit from the packet with the
                    corresponding filterPktDataNotMask bit set to zero, if
                    the bit from the packet is not equal to the corresponding
                    bit from the filterPktData, then the packet will fail
                    this data match.
                
                (3) If for every relevant bit from the packet with the
                    corresponding filterPktDataNotMask bit set to one, the
                    bit from the packet is equal to the corresponding bit
                    from the filterPktData, then the packet will fail this
                    data match.
                
                Any packets that have not failed any of the three matches
                above have passed this data match.  In particular, a zero
                length filter will match any packet.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdata',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktDataMask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The mask that is applied to the match process.
                After adjusting this mask for the offset, only those
                bits in the received packet that correspond to bits set
                in this mask are relevant for further processing by the
                match algorithm.  The offset is applied to filterPktDataMask
                in the same way it is applied to the filter.  For the
                purposes of the matching algorithm, if the associated
                filterPktData object is longer than this mask, this mask is
                conceptually extended with '1' bits until it reaches the
                length of the filterPktData object.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdatamask',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktDataNotMask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The inversion mask that is applied to the match
                process.  After adjusting this mask for the offset,
                those relevant bits in the received packet that correspond
                to bits cleared in this mask must all be equal to their
                corresponding bits in the filterPktData object for the packet
                to be accepted.  In addition, at least one of those relevant
                bits in the received packet that correspond to bits set in
                this mask must be different to its corresponding bit in the
                filterPktData object.
                
                For the purposes of the matching algorithm, if the associated
                filterPktData object is longer than this mask, this mask is
                conceptually extended with '0' bits until it reaches the
                length of the filterPktData object.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdatanotmask',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktDataOffset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The offset from the beginning of each packet where
                a match of packet data will be attempted.  This offset
                is measured from the point in the physical layer
                packet after the framing bits, if any.  For example,
                in an Ethernet frame, this point is at the beginning of
                the destination MAC address.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdataoffset',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktStatus', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The status that is to be matched with the input packet.
                The only bits relevant to this match algorithm are those that
                have the corresponding filterPktStatusMask bit equal to one.
                The following two rules are then applied to every packet:
                
                (1) For each relevant bit from the packet status with the
                    corresponding filterPktStatusNotMask bit set to zero, if
                    the bit from the packet status is not equal to the
                    corresponding bit from the filterPktStatus, then the
                    packet will fail this status match.
                
                (2) If for every relevant bit from the packet status with the
                    corresponding filterPktStatusNotMask bit set to one, the
                    bit from the packet status is equal to the corresponding
                    bit from the filterPktStatus, then the packet will fail
                    this status match.
                
                Any packets that have not failed either of the two matches
                above have passed this status match.  In particular, a zero
                length status filter will match any packet's status.
                
                The value of the packet status is a sum.  This sum
                initially takes the value zero.  Then, for each
                error, E, that has been discovered in this packet,
                2 raised to a value representing E is added to the sum.
                The errors and the bits that represent them are dependent
                on the media type of the interface that this channel
                is receiving packets from.
                
                The errors defined for a packet captured off of an
                Ethernet interface are as follows:
                
                    bit #    Error
                        0    Packet is longer than 1518 octets
                        1    Packet is shorter than 64 octets
                        2    Packet experienced a CRC or Alignment error
                
                For example, an Ethernet fragment would have a
                value of 6 (2^1 + 2^2).
                
                As this MIB is expanded to new media types, this object
                will have other media-specific errors defined.
                
                For the purposes of this status matching algorithm, if the
                packet status is longer than this filterPktStatus object,
                this object is conceptually extended with '0' bits until it
                reaches the size of the packet status.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktStatusMask', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The mask that is applied to the status match process.
                Only those bits in the received packet that correspond to
                bits set in this mask are relevant for further processing
                by the status match algorithm.  For the purposes
                of the matching algorithm, if the associated filterPktStatus
                object is longer than this mask, this mask is conceptually
                extended with '1' bits until it reaches the size of the
                filterPktStatus.  In addition, if a packet status is longer
                than this mask, this mask is conceptually extended with '0'
                bits until it reaches the size of the packet status.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktstatusmask',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterPktStatusNotMask', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The inversion mask that is applied to the status match
                process.  Those relevant bits in the received packet status
                that correspond to bits cleared in this mask must all be
                equal to their corresponding bits in the filterPktStatus
                object for the packet to be accepted.  In addition, at least
                one of those relevant bits in the received packet status
                that correspond to bits set in this mask must be different
                to its corresponding bit in the filterPktStatus object for
                the packet to be accepted.
                
                For the purposes of the matching algorithm, if the associated
                filterPktStatus object or a packet status is longer than this
                mask, this mask is conceptually extended with '0' bits until
                it reaches the longer of the lengths of the filterPktStatus
                object and the packet status.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktstatusnotmask',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this filter entry.
                ''',
                'filterstatus',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'filterEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Filtertable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Filtertable',
            False, 
            [
            _MetaInfoClassMember('filterEntry', REFERENCE_LIST, 'Filterentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Filtertable.Filterentry', 
                [], [], 
                '''                A set of parameters for a packet filter applied on a
                particular interface.  As an example, an instance of the
                filterPktData object might be named filterPktData.12
                ''',
                'filterentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'filterTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Channeltable.Channelentry.ChannelaccepttypeEnum' : _MetaInfoEnum('ChannelaccepttypeEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'acceptMatched':'acceptMatched',
            'acceptFailed':'acceptFailed',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Channeltable.Channelentry.ChanneldatacontrolEnum' : _MetaInfoEnum('ChanneldatacontrolEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'on':'on',
            'off':'off',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Channeltable.Channelentry.ChanneleventstatusEnum' : _MetaInfoEnum('ChanneleventstatusEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'eventReady':'eventReady',
            'eventFired':'eventFired',
            'eventAlwaysReady':'eventAlwaysReady',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Channeltable.Channelentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Channeltable.Channelentry',
            False, 
            [
            _MetaInfoClassMember('channelIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in the channel
                table.  Each such entry defines one channel, a logical
                data and event stream.
                
                It is suggested that before creating a channel, an
                application should scan all instances of the
                filterChannelIndex object to make sure that there are no
                pre-existing filters that would be inadvertently be linked
                to the channel.
                ''',
                'channelindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('channelAcceptType', REFERENCE_ENUM_CLASS, 'ChannelaccepttypeEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Channeltable.Channelentry.ChannelaccepttypeEnum', 
                [], [], 
                '''                This object controls the action of the filters
                associated with this channel.  If this object is equal
                to acceptMatched(1), packets will be accepted to this
                channel if they are accepted by both the packet data and
                packet status matches of an associated filter.  If
                this object is equal to acceptFailed(2), packets will
                be accepted to this channel only if they fail either
                the packet data match or the packet status match of
                each of the associated filters.
                
                In particular, a channel with no associated filters will
                match no packets if set to acceptMatched(1) case and will
                match all packets in the acceptFailed(2) case.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelaccepttype',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelDataControl', REFERENCE_ENUM_CLASS, 'ChanneldatacontrolEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Channeltable.Channelentry.ChanneldatacontrolEnum', 
                [], [], 
                '''                This object controls the flow of data through this channel.
                If this object is on(1), data, status and events flow
                through this channel.  If this object is off(2), data,
                status and events will not flow through this channel.
                ''',
                'channeldatacontrol',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                A comment describing this channel.
                ''',
                'channeldescription',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The value of this object identifies the event
                that is configured to be generated when the
                associated channelDataControl is on and a packet
                is matched.  The event identified by a particular value
                of this object is the same event as identified by the
                same value of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then no
                association exists.  In fact, if no event is intended
                for this channel, channelEventIndex must be
                set to zero, a non-existent event index.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channeleventindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelEventStatus', REFERENCE_ENUM_CLASS, 'ChanneleventstatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Channeltable.Channelentry.ChanneleventstatusEnum', 
                [], [], 
                '''                The event status of this channel.
                
                If this channel is configured to generate events
                when packets are matched, a means of controlling
                the flow of those events is often needed.  When
                this object is equal to eventReady(1), a single
                event may be generated, after which this object
                will be set by the probe to eventFired(2).  While
                in the eventFired(2) state, no events will be
                generated until the object is modified to
                eventReady(1) (or eventAlwaysReady(3)).  The
                management station can thus easily respond to a
                notification of an event by re-enabling this object.
                
                If the management station wishes to disable this
                flow control and allow events to be generated
                at will, this object may be set to
                eventAlwaysReady(3).  Disabling the flow control
                is discouraged as it can result in high network
                traffic or other performance problems.
                ''',
                'channeleventstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of this object uniquely identifies the
                interface on this remote network monitoring device to which
                the associated filters are applied to allow data into this
                channel.  The interface identified by a particular value
                of this object is the same interface as identified by the
                same value of the ifIndex object, defined in RFC 2233 [17].
                
                The filters in this group are applied to all packets on
                the local network segment attached to the identified
                interface.
                
                An agent may or may not be able to tell if fundamental
                changes to the media of the interface have occurred and
                necessitate an invalidation of this entry.  For example, a
                hot-pluggable ethernet card could be pulled out and replaced
                by a token-ring card.  In such a case, if the agent has such
                knowledge of the change, it is recommended that it
                invalidate this entry.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelifindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelMatches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this channel has matched a packet.
                Note that this object is updated even when
                channelDataControl is set to off.
                ''',
                'channelmatches',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'channelowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this channel entry.
                ''',
                'channelstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelTurnOffEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The value of this object identifies the event
                that is configured to turn the associated
                channelDataControl from on to off when the event is
                generated.  The event identified by a particular value
                of this object is the same event as identified by the
                same value of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then no
                association exists.  In fact, if no event is intended
                for this channel, channelTurnOffEventIndex must be
                set to zero, a non-existent event index.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelturnoffeventindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelTurnOnEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The value of this object identifies the event
                that is configured to turn the associated
                channelDataControl from off to on when the event is
                generated.  The event identified by a particular value
                of this object is the same event as identified by the
                same value of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then no
                association exists.  In fact, if no event is intended
                for this channel, channelTurnOnEventIndex must be
                set to zero, a non-existent event index.
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelturnoneventindex',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'channelEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Channeltable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Channeltable',
            False, 
            [
            _MetaInfoClassMember('channelEntry', REFERENCE_LIST, 'Channelentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Channeltable.Channelentry', 
                [], [], 
                '''                A set of parameters for a packet channel applied on a
                particular interface.  As an example, an instance of the
                channelMatches object might be named channelMatches.3
                ''',
                'channelentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'channelTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Buffercontroltable.Buffercontrolentry.BuffercontrolfullactionEnum' : _MetaInfoEnum('BuffercontrolfullactionEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'lockWhenFull':'lockWhenFull',
            'wrapWhenFull':'wrapWhenFull',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Buffercontroltable.Buffercontrolentry.BuffercontrolfullstatusEnum' : _MetaInfoEnum('BuffercontrolfullstatusEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'spaceAvailable':'spaceAvailable',
            'full':'full',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Buffercontroltable.Buffercontrolentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Buffercontroltable.Buffercontrolentry',
            False, 
            [
            _MetaInfoClassMember('bufferControlIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry
                in the bufferControl table.  The value of this
                index shall never be zero.  Each such
                entry defines one set of packets that is
                captured and controlled by one or more filters.
                ''',
                'buffercontrolindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('bufferControlCapturedPackets', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of packets currently in this captureBuffer.
                ''',
                'buffercontrolcapturedpackets',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlCaptureSliceSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of octets of each packet
                that will be saved in this capture buffer.
                For example, if a 1500 octet packet is received by
                the probe and this object is set to 500, then only
                500 octets of the packet will be stored in the
                associated capture buffer.  If this variable is set
                to 0, the capture buffer will save as many octets
                as is possible.
                
                This object may not be modified if the associated
                bufferControlStatus object is equal to valid(1).
                ''',
                'buffercontrolcaptureslicesize',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlChannelIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that identifies the channel that is the
                source of packets for this bufferControl table.
                The channel identified by a particular value of this
                index is the same as identified by the same value of
                the channelIndex object.
                
                This object may not be modified if the associated
                bufferControlStatus object is equal to valid(1).
                ''',
                'buffercontrolchannelindex',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlDownloadOffset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The offset of the first octet of each packet
                in this capture buffer that will be returned in
                an SNMP retrieval of that packet.  For example,
                if 500 octets of a packet have been stored in the
                associated capture buffer and this object is set to
                100, then the captureBufferPacket object that
                contains the packet will contain bytes starting
                100 octets into the packet.
                ''',
                'buffercontroldownloadoffset',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlDownloadSliceSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of octets of each packet
                in this capture buffer that will be returned in
                an SNMP retrieval of that packet.  For example,
                if 500 octets of a packet have been stored in the
                associated capture buffer, the associated
                bufferControlDownloadOffset is 0, and this
                object is set to 100, then the captureBufferPacket
                object that contains the packet will contain only
                the first 100 octets of the packet.
                
                A prudent manager will take into account possible
                interoperability or fragmentation problems that may
                occur if the download slice size is set too large.
                In particular, conformant SNMP implementations are not
                required to accept messages whose length exceeds 484
                octets, although they are encouraged to support larger
                datagrams whenever feasible.
                ''',
                'buffercontroldownloadslicesize',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlFullAction', REFERENCE_ENUM_CLASS, 'BuffercontrolfullactionEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Buffercontroltable.Buffercontrolentry.BuffercontrolfullactionEnum', 
                [], [], 
                '''                Controls the action of the buffer when it
                reaches the full status.  When in the lockWhenFull(1)
                state and a packet is added to the buffer that
                fills the buffer, the bufferControlFullStatus will
                be set to full(2) and this buffer will stop capturing
                packets.
                ''',
                'buffercontrolfullaction',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlFullStatus', REFERENCE_ENUM_CLASS, 'BuffercontrolfullstatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Buffercontroltable.Buffercontrolentry.BuffercontrolfullstatusEnum', 
                [], [], 
                '''                This object shows whether the buffer has room to
                accept new packets or if it is full.
                
                If the status is spaceAvailable(1), the buffer is
                accepting new packets normally.  If the status is
                full(2) and the associated bufferControlFullAction
                object is wrapWhenFull, the buffer is accepting new
                packets by deleting enough of the oldest packets
                to make room for new ones as they arrive.  Otherwise,
                if the status is full(2) and the
                bufferControlFullAction object is lockWhenFull,
                then the buffer has stopped collecting packets.
                
                When this object is set to full(2) the probe must
                not later set it to spaceAvailable(1) except in the
                case of a significant gain in resources such as
                an increase of bufferControlOctetsGranted.  In
                particular, the wrap-mode action of deleting old
                packets to make room for newly arrived packets
                must not affect the value of this object.
                ''',
                'buffercontrolfullstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlMaxOctetsGranted', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of octets that can be
                saved in this captureBuffer, including overhead.
                If this variable is -1, the capture buffer will save
                as many octets as possible.
                
                When the bufferControlMaxOctetsRequested object is
                created or modified, the probe should set this object
                as closely to the requested value as is possible for the
                particular probe implementation and available resources.
                However, if the request object has the special value
                of -1, the probe must set this object to -1.
                
                The probe must not lower this value except as a result of
                a modification to the associated
                bufferControlMaxOctetsRequested object.
                
                When this maximum number of octets is reached
                and a new packet is to be added to this
                capture buffer and the corresponding
                bufferControlFullAction is set to wrapWhenFull(2),
                enough of the oldest packets associated with this
                capture buffer shall be deleted by the agent so
                that the new packet can be added.  If the corresponding
                bufferControlFullAction is set to lockWhenFull(1),
                the new packet shall be discarded.  In either case,
                the probe must set bufferControlFullStatus to
                full(2).
                
                When the value of this object changes to a value less
                than the current value, entries are deleted from
                the captureBufferTable associated with this
                bufferControlEntry.  Enough of the
                oldest of these captureBufferEntries shall be
                deleted by the agent so that the number of octets
                used remains less than or equal to the new value of
                this object.
                
                When the value of this object changes to a value greater
                than the current value, the number of associated
                captureBufferEntries may be allowed to grow.
                ''',
                'buffercontrolmaxoctetsgranted',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlMaxOctetsRequested', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The requested maximum number of octets to be
                saved in this captureBuffer, including any
                implementation-specific overhead. If this variable
                is set to -1, the capture buffer will save as many
                octets as is possible.
                
                When this object is created or modified, the probe
                should set bufferControlMaxOctetsGranted as closely
                to this object as is possible for the particular probe
                implementation and available resources.  However, if
                the object has the special value of -1, the probe
                must set bufferControlMaxOctetsGranted to -1.
                ''',
                'buffercontrolmaxoctetsrequested',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'buffercontrolowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this buffer Control Entry.
                ''',
                'buffercontrolstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlTurnOnTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when this capture buffer was
                first turned on.
                ''',
                'buffercontrolturnontime',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'bufferControlEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Buffercontroltable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Buffercontroltable',
            False, 
            [
            _MetaInfoClassMember('bufferControlEntry', REFERENCE_LIST, 'Buffercontrolentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Buffercontroltable.Buffercontrolentry', 
                [], [], 
                '''                A set of parameters that control the collection of a stream
                of packets that have matched filters.  As an example, an
                instance of the bufferControlCaptureSliceSize object might
                be named bufferControlCaptureSliceSize.3
                ''',
                'buffercontrolentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'bufferControlTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Capturebuffertable.Capturebufferentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Capturebuffertable.Capturebufferentry',
            False, 
            [
            _MetaInfoClassMember('captureBufferControlIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The index of the bufferControlEntry with which
                this packet is associated.
                ''',
                'capturebuffercontrolindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('captureBufferIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index that uniquely identifies an entry
                in the captureBuffer table associated with a
                particular bufferControlEntry.  This index will
                start at 1 and increase by one for each new packet
                added with the same captureBufferControlIndex.
                
                Should this value reach 2147483647, the next packet
                added with the same captureBufferControlIndex shall
                cause this value to wrap around to 1.
                ''',
                'capturebufferindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('captureBufferPacketData', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The data inside the packet, starting at the beginning
                of the packet plus any offset specified in the
                associated bufferControlDownloadOffset, including any
                link level headers.  The length of the data in this object
                is the minimum of the length of the captured packet minus
                the offset, the length of the associated
                bufferControlCaptureSliceSize minus the offset, and the
                associated bufferControlDownloadSliceSize.  If this minimum
                is less than zero, this object shall have a length of zero.
                ''',
                'capturebufferpacketdata',
                'RMON-MIB', False),
            _MetaInfoClassMember('captureBufferPacketID', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An index that describes the order of packets
                that are received on a particular interface.
                The packetID of a packet captured on an
                interface is defined to be greater than the
                packetID's of all packets captured previously on
                the same interface.  As the captureBufferPacketID
                object has a maximum positive value of 2^31 - 1,
                any captureBufferPacketID object shall have the
                value of the associated packet's packetID mod 2^31.
                ''',
                'capturebufferpacketid',
                'RMON-MIB', False),
            _MetaInfoClassMember('captureBufferPacketLength', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The actual length (off the wire) of the packet stored
                in this entry, including FCS octets.
                ''',
                'capturebufferpacketlength',
                'RMON-MIB', False),
            _MetaInfoClassMember('captureBufferPacketStatus', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A value which indicates the error status of this packet.
                
                The value of this object is defined in the same way as
                filterPktStatus.  The value is a sum.  This sum
                initially takes the value zero.  Then, for each
                error, E, that has been discovered in this packet,
                2 raised to a value representing E is added to the sum.
                
                The errors defined for a packet captured off of an
                Ethernet interface are as follows:
                
                    bit #    Error
                        0    Packet is longer than 1518 octets
                        1    Packet is shorter than 64 octets
                        2    Packet experienced a CRC or Alignment error
                        3    First packet in this capture buffer after
                             it was detected that some packets were
                             not processed correctly.
                        4    Packet's order in buffer is only approximate
                             (May only be set for packets sent from
                             the probe)
                
                For example, an Ethernet fragment would have a
                value of 6 (2^1 + 2^2).
                
                As this MIB is expanded to new media types, this object
                will have other media-specific errors defined.
                ''',
                'capturebufferpacketstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('captureBufferPacketTime', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of milliseconds that had passed since
                this capture buffer was first turned on when this
                packet was captured.
                ''',
                'capturebufferpackettime',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'captureBufferEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Capturebuffertable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Capturebuffertable',
            False, 
            [
            _MetaInfoClassMember('captureBufferEntry', REFERENCE_LIST, 'Capturebufferentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Capturebuffertable.Capturebufferentry', 
                [], [], 
                '''                A packet captured off of an attached network.  As an
                example, an instance of the captureBufferPacketData
                object might be named captureBufferPacketData.3.1783
                ''',
                'capturebufferentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'captureBufferTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Eventtable.Evententry.EventtypeEnum' : _MetaInfoEnum('EventtypeEnum', 'ydk.models.cisco_ios_xe.RMON_MIB',
        {
            'none':'none',
            'log':'log',
            'snmptrap':'snmptrap',
            'logandtrap':'logandtrap',
        }, 'RMON-MIB', _yang_ns._namespaces['RMON-MIB']),
    'RmonMib.Eventtable.Evententry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Eventtable.Evententry',
            False, 
            [
            _MetaInfoClassMember('eventIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in the
                event table.  Each such entry defines one event that
                is to be generated when the appropriate conditions
                occur.
                ''',
                'eventindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('eventCommunity', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                If an SNMP trap is to be sent, it will be sent to
                the SNMP community specified by this octet string.
                ''',
                'eventcommunity',
                'RMON-MIB', False),
            _MetaInfoClassMember('eventDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                A comment describing this event entry.
                ''',
                'eventdescription',
                'RMON-MIB', False),
            _MetaInfoClassMember('eventLastTimeSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this event
                entry last generated an event.  If this entry has
                not generated any events, this value will be
                zero.
                ''',
                'eventlasttimesent',
                'RMON-MIB', False),
            _MetaInfoClassMember('eventOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                
                If this object contains a string starting with 'monitor'
                and has associated entries in the log table, all connected
                management stations should retrieve those log entries,
                as they may have significance to all management stations
                connected to this device
                ''',
                'eventowner',
                'RMON-MIB', False),
            _MetaInfoClassMember('eventStatus', REFERENCE_ENUM_CLASS, 'EntrystatusEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'EntrystatusEnum', 
                [], [], 
                '''                The status of this event entry.
                
                If this object is not equal to valid(1), all associated
                log entries shall be deleted by the agent.
                ''',
                'eventstatus',
                'RMON-MIB', False),
            _MetaInfoClassMember('eventType', REFERENCE_ENUM_CLASS, 'EventtypeEnum' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Eventtable.Evententry.EventtypeEnum', 
                [], [], 
                '''                The type of notification that the probe will make
                about this event.  In the case of log, an entry is
                made in the log table for each event.  In the case of
                snmp-trap, an SNMP trap is sent to one or more
                management stations.
                ''',
                'eventtype',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'eventEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Eventtable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Eventtable',
            False, 
            [
            _MetaInfoClassMember('eventEntry', REFERENCE_LIST, 'Evententry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Eventtable.Evententry', 
                [], [], 
                '''                A set of parameters that describe an event to be generated
                when certain conditions are met.  As an example, an instance
                of the eventLastTimeSent object might be named
                eventLastTimeSent.6
                ''',
                'evententry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'eventTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Logtable.Logentry' : {
        'meta_info' : _MetaInfoClass('RmonMib.Logtable.Logentry',
            False, 
            [
            _MetaInfoClassMember('logEventIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The event entry that generated this log
                entry.  The log identified by a particular
                value of this index is associated with the same
                eventEntry as identified by the same value
                of eventIndex.
                ''',
                'logeventindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('logIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index that uniquely identifies an entry
                in the log table amongst those generated by the
                same eventEntries.  These indexes are
                assigned beginning with 1 and increase by one
                with each new log entry.  The association
                between values of logIndex and logEntries
                is fixed for the lifetime of each logEntry.
                The agent may choose to delete the oldest
                instances of logEntry as required because of
                lack of memory.  It is an implementation-specific
                matter as to when this deletion may occur.
                ''',
                'logindex',
                'RMON-MIB', True),
            _MetaInfoClassMember('logDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An implementation dependent description of the
                event that activated this log entry.
                ''',
                'logdescription',
                'RMON-MIB', False),
            _MetaInfoClassMember('logTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when this log entry was created.
                ''',
                'logtime',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'logEntry',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib.Logtable' : {
        'meta_info' : _MetaInfoClass('RmonMib.Logtable',
            False, 
            [
            _MetaInfoClassMember('logEntry', REFERENCE_LIST, 'Logentry' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Logtable.Logentry', 
                [], [], 
                '''                A set of data describing an event that has been
                logged.  For example, an instance of the logDescription
                object might be named logDescription.6.47
                ''',
                'logentry',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'logTable',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
    'RmonMib' : {
        'meta_info' : _MetaInfoClass('RmonMib',
            False, 
            [
            _MetaInfoClassMember('alarmTable', REFERENCE_CLASS, 'Alarmtable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Alarmtable', 
                [], [], 
                '''                A list of alarm entries.
                ''',
                'alarmtable',
                'RMON-MIB', False),
            _MetaInfoClassMember('bufferControlTable', REFERENCE_CLASS, 'Buffercontroltable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Buffercontroltable', 
                [], [], 
                '''                A list of buffers control entries.
                ''',
                'buffercontroltable',
                'RMON-MIB', False),
            _MetaInfoClassMember('captureBufferTable', REFERENCE_CLASS, 'Capturebuffertable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Capturebuffertable', 
                [], [], 
                '''                A list of packets captured off of a channel.
                ''',
                'capturebuffertable',
                'RMON-MIB', False),
            _MetaInfoClassMember('channelTable', REFERENCE_CLASS, 'Channeltable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Channeltable', 
                [], [], 
                '''                A list of packet channel entries.
                ''',
                'channeltable',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherHistoryTable', REFERENCE_CLASS, 'Etherhistorytable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Etherhistorytable', 
                [], [], 
                '''                A list of Ethernet history entries.
                ''',
                'etherhistorytable',
                'RMON-MIB', False),
            _MetaInfoClassMember('etherStatsTable', REFERENCE_CLASS, 'Etherstatstable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Etherstatstable', 
                [], [], 
                '''                A list of Ethernet statistics entries.
                ''',
                'etherstatstable',
                'RMON-MIB', False),
            _MetaInfoClassMember('eventTable', REFERENCE_CLASS, 'Eventtable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Eventtable', 
                [], [], 
                '''                A list of events to be generated.
                ''',
                'eventtable',
                'RMON-MIB', False),
            _MetaInfoClassMember('filterTable', REFERENCE_CLASS, 'Filtertable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Filtertable', 
                [], [], 
                '''                A list of packet filter entries.
                ''',
                'filtertable',
                'RMON-MIB', False),
            _MetaInfoClassMember('historyControlTable', REFERENCE_CLASS, 'Historycontroltable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Historycontroltable', 
                [], [], 
                '''                A list of history control entries.
                ''',
                'historycontroltable',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostControlTable', REFERENCE_CLASS, 'Hostcontroltable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hostcontroltable', 
                [], [], 
                '''                A list of host table control entries.
                ''',
                'hostcontroltable',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTable', REFERENCE_CLASS, 'Hosttable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttable', 
                [], [], 
                '''                A list of host entries.
                ''',
                'hosttable',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTimeTable', REFERENCE_CLASS, 'Hosttimetable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttimetable', 
                [], [], 
                '''                A list of time-ordered host table entries.
                ''',
                'hosttimetable',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNControlTable', REFERENCE_CLASS, 'Hosttopncontroltable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttopncontroltable', 
                [], [], 
                '''                A list of top N host control entries.
                ''',
                'hosttopncontroltable',
                'RMON-MIB', False),
            _MetaInfoClassMember('hostTopNTable', REFERENCE_CLASS, 'Hosttopntable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Hosttopntable', 
                [], [], 
                '''                A list of top N host entries.
                ''',
                'hosttopntable',
                'RMON-MIB', False),
            _MetaInfoClassMember('logTable', REFERENCE_CLASS, 'Logtable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Logtable', 
                [], [], 
                '''                A list of events that have been logged.
                ''',
                'logtable',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixControlTable', REFERENCE_CLASS, 'Matrixcontroltable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Matrixcontroltable', 
                [], [], 
                '''                A list of information entries for the
                traffic matrix on each interface.
                ''',
                'matrixcontroltable',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixDSTable', REFERENCE_CLASS, 'Matrixdstable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Matrixdstable', 
                [], [], 
                '''                A list of traffic matrix entries indexed by
                destination and source MAC address.
                ''',
                'matrixdstable',
                'RMON-MIB', False),
            _MetaInfoClassMember('matrixSDTable', REFERENCE_CLASS, 'Matrixsdtable' , 'ydk.models.cisco_ios_xe.RMON_MIB', 'RmonMib.Matrixsdtable', 
                [], [], 
                '''                A list of traffic matrix entries indexed by
                source and destination MAC address.
                ''',
                'matrixsdtable',
                'RMON-MIB', False),
            ],
            'RMON-MIB',
            'RMON-MIB',
            _yang_ns._namespaces['RMON-MIB'],
        'ydk.models.cisco_ios_xe.RMON_MIB'
        ),
    },
}
_meta_table['RmonMib.Etherstatstable.Etherstatsentry']['meta_info'].parent =_meta_table['RmonMib.Etherstatstable']['meta_info']
_meta_table['RmonMib.Historycontroltable.Historycontrolentry']['meta_info'].parent =_meta_table['RmonMib.Historycontroltable']['meta_info']
_meta_table['RmonMib.Etherhistorytable.Etherhistoryentry']['meta_info'].parent =_meta_table['RmonMib.Etherhistorytable']['meta_info']
_meta_table['RmonMib.Alarmtable.Alarmentry']['meta_info'].parent =_meta_table['RmonMib.Alarmtable']['meta_info']
_meta_table['RmonMib.Hostcontroltable.Hostcontrolentry']['meta_info'].parent =_meta_table['RmonMib.Hostcontroltable']['meta_info']
_meta_table['RmonMib.Hosttable.Hostentry']['meta_info'].parent =_meta_table['RmonMib.Hosttable']['meta_info']
_meta_table['RmonMib.Hosttimetable.Hosttimeentry']['meta_info'].parent =_meta_table['RmonMib.Hosttimetable']['meta_info']
_meta_table['RmonMib.Hosttopncontroltable.Hosttopncontrolentry']['meta_info'].parent =_meta_table['RmonMib.Hosttopncontroltable']['meta_info']
_meta_table['RmonMib.Hosttopntable.Hosttopnentry']['meta_info'].parent =_meta_table['RmonMib.Hosttopntable']['meta_info']
_meta_table['RmonMib.Matrixcontroltable.Matrixcontrolentry']['meta_info'].parent =_meta_table['RmonMib.Matrixcontroltable']['meta_info']
_meta_table['RmonMib.Matrixsdtable.Matrixsdentry']['meta_info'].parent =_meta_table['RmonMib.Matrixsdtable']['meta_info']
_meta_table['RmonMib.Matrixdstable.Matrixdsentry']['meta_info'].parent =_meta_table['RmonMib.Matrixdstable']['meta_info']
_meta_table['RmonMib.Filtertable.Filterentry']['meta_info'].parent =_meta_table['RmonMib.Filtertable']['meta_info']
_meta_table['RmonMib.Channeltable.Channelentry']['meta_info'].parent =_meta_table['RmonMib.Channeltable']['meta_info']
_meta_table['RmonMib.Buffercontroltable.Buffercontrolentry']['meta_info'].parent =_meta_table['RmonMib.Buffercontroltable']['meta_info']
_meta_table['RmonMib.Capturebuffertable.Capturebufferentry']['meta_info'].parent =_meta_table['RmonMib.Capturebuffertable']['meta_info']
_meta_table['RmonMib.Eventtable.Evententry']['meta_info'].parent =_meta_table['RmonMib.Eventtable']['meta_info']
_meta_table['RmonMib.Logtable.Logentry']['meta_info'].parent =_meta_table['RmonMib.Logtable']['meta_info']
_meta_table['RmonMib.Etherstatstable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Historycontroltable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Etherhistorytable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Alarmtable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Hostcontroltable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Hosttable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Hosttimetable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Hosttopncontroltable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Hosttopntable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Matrixcontroltable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Matrixsdtable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Matrixdstable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Filtertable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Channeltable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Buffercontroltable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Capturebuffertable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Eventtable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
_meta_table['RmonMib.Logtable']['meta_info'].parent =_meta_table['RmonMib']['meta_info']
