


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Dot3ErroriniterrorIdentity' : {
        'meta_info' : _MetaInfoClass('Dot3ErroriniterrorIdentity',
            False, 
            [
            ],
            'EtherLike-MIB',
            'dot3ErrorInitError',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'Dot3TesttdrIdentity' : {
        'meta_info' : _MetaInfoClass('Dot3TesttdrIdentity',
            False, 
            [
            ],
            'EtherLike-MIB',
            'dot3TestTdr',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'Dot3TestloopbackIdentity' : {
        'meta_info' : _MetaInfoClass('Dot3TestloopbackIdentity',
            False, 
            [
            ],
            'EtherLike-MIB',
            'dot3TestLoopBack',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'Dot3ErrorloopbackerrorIdentity' : {
        'meta_info' : _MetaInfoClass('Dot3ErrorloopbackerrorIdentity',
            False, 
            [
            ],
            'EtherLike-MIB',
            'dot3ErrorLoopbackError',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsduplexstatusEnum' : _MetaInfoEnum('Dot3StatsduplexstatusEnum', 'ydk.models.cisco_ios_xe.EtherLike_MIB',
        {
            'unknown':'unknown',
            'halfDuplex':'halfDuplex',
            'fullDuplex':'fullDuplex',
        }, 'EtherLike-MIB', _yang_ns._namespaces['EtherLike-MIB']),
    'EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsratecontrolstatusEnum' : _MetaInfoEnum('Dot3StatsratecontrolstatusEnum', 'ydk.models.cisco_ios_xe.EtherLike_MIB',
        {
            'rateControlOff':'rateControlOff',
            'rateControlOn':'rateControlOn',
            'unknown':'unknown',
        }, 'EtherLike-MIB', _yang_ns._namespaces['EtherLike-MIB']),
    'EtherlikeMib.Dot3Statstable.Dot3Statsentry' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Statstable.Dot3Statsentry',
            False, 
            [
            _MetaInfoClassMember('dot3StatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index value that uniquely identifies an
                interface to an ethernet-like medium.  The
                interface identified by a particular value of
                this index is the same interface as identified
                by the same value of ifIndex.
                ''',
                'dot3statsindex',
                'EtherLike-MIB', True),
            _MetaInfoClassMember('dot3StatsAlignmentErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames received on a particular
                interface that are not an integral number of
                octets in length and do not pass the FCS check.
                
                The count represented by an instance of this
                object is incremented when the alignmentError
                status is returned by the MAC service to the
                LLC (or other MAC user). Received frames for
                which multiple error conditions pertain are,
                according to the conventions of IEEE 802.3
                Layer Management, counted exclusively according
                to the error status presented to the LLC.
                
                This counter does not increment for group
                encoding schemes greater than 4 bits per group.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCStatsAlignmentErrors object for 10 Gb/s
                or faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsalignmenterrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsCarrierSenseErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times that the carrier sense
                condition was lost or never asserted when
                attempting to transmit a frame on a particular
                interface.
                
                The count represented by an instance of this
                object is incremented at most once per
                transmission attempt, even if the carrier sense
                condition fluctuates during a transmission
                attempt.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statscarriersenseerrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsDeferredTransmissions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames for which the first
                transmission attempt on a particular interface
                is delayed because the medium is busy.
                
                The count represented by an instance of this
                object does not include frames involved in
                collisions.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsdeferredtransmissions',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsDuplexStatus', REFERENCE_ENUM_CLASS, 'Dot3StatsduplexstatusEnum' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsduplexstatusEnum', 
                [], [], 
                '''                The current mode of operation of the MAC
                entity.  'unknown' indicates that the current
                duplex mode could not be determined.
                
                Management control of the duplex mode is
                accomplished through the MAU MIB.  When
                an interface does not support autonegotiation,
                or when autonegotiation is not enabled, the
                duplex mode is controlled using
                ifMauDefaultType.  When autonegotiation is
                supported and enabled, duplex mode is controlled
                using ifMauAutoNegAdvertisedBits.  In either
                case, the currently operating duplex mode is
                reflected both in this object and in ifMauType.
                
                Note that this object provides redundant
                information with ifMauType.  Normally, redundant
                objects are discouraged.  However, in this
                instance, it allows a management application to
                determine the duplex status of an interface
                without having to know every possible value of
                ifMauType.  This was felt to be sufficiently
                valuable to justify the redundancy.
                ''',
                'dot3statsduplexstatus',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsEtherChipSet', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                ******** THIS OBJECT IS DEPRECATED ********
                
                This object contains an OBJECT IDENTIFIER
                which identifies the chipset used to
                realize the interface. Ethernet-like
                interfaces are typically built out of
                several different chips. The MIB implementor
                is presented with a decision of which chip
                to identify via this object. The implementor
                should identify the chip which is usually
                called the Medium Access Control chip.
                If no such chip is easily identifiable,
                the implementor should identify the chip
                which actually gathers the transmit
                and receive statistics and error
                indications. This would allow a
                manager station to correlate the
                statistics and the chip generating
                them, giving it the ability to take
                into account any known anomalies
                in the chip.
                
                This object has been deprecated.  Implementation
                feedback indicates that it is of limited use for
                debugging network problems in the field, and
                the administrative overhead involved in
                maintaining a registry of chipset OIDs is not
                justified.
                ''',
                'dot3statsetherchipset',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsExcessiveCollisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames for which transmission on a
                particular interface fails due to excessive
                collisions.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsexcessivecollisions',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsFCSErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames received on a particular
                interface that are an integral number of octets
                in length but do not pass the FCS check.  This
                count does not include frames received with
                frame-too-long or frame-too-short error.
                
                The count represented by an instance of this
                object is incremented when the frameCheckError
                status is returned by the MAC service to the
                LLC (or other MAC user). Received frames for
                which multiple error conditions pertain are,
                according to the conventions of IEEE 802.3
                Layer Management, counted exclusively according
                to the error status presented to the LLC.
                
                Note:  Coding errors detected by the physical
                layer for speeds above 10 Mb/s will cause the
                frame to fail the FCS check.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCStatsFCSErrors object for 10 Gb/s or
                faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsfcserrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsFrameTooLongs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames received on a particular
                interface that exceed the maximum permitted
                frame size.
                
                The count represented by an instance of this
                object is incremented when the frameTooLong
                status is returned by the MAC service to the
                LLC (or other MAC user). Received frames for
                which multiple error conditions pertain are,
                according to the conventions of IEEE 802.3
                Layer Management, counted exclusively according
                to the error status presented to the LLC.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 80 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCStatsFrameTooLongs object for 10 Gb/s
                or faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsframetoolongs',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsInternalMacReceiveErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames for which reception on a
                particular interface fails due to an internal
                MAC sublayer receive error. A frame is only
                counted by an instance of this object if it is
                not counted by the corresponding instance of
                either the dot3StatsFrameTooLongs object, the
                dot3StatsAlignmentErrors object, or the
                dot3StatsFCSErrors object.
                
                The precise meaning of the count represented by
                an instance of this object is implementation-
                specific.  In particular, an instance of this
                object may represent a count of receive errors
                on a particular interface that are not
                otherwise counted.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCStatsInternalMacReceiveErrors object for
                10 Gb/s or faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsinternalmacreceiveerrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsInternalMacTransmitErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames for which transmission on a
                particular interface fails due to an internal
                MAC sublayer transmit error. A frame is only
                counted by an instance of this object if it is
                not counted by the corresponding instance of
                either the dot3StatsLateCollisions object, the
                dot3StatsExcessiveCollisions object, or the
                dot3StatsCarrierSenseErrors object.
                
                The precise meaning of the count represented by
                an instance of this object is implementation-
                specific.  In particular, an instance of this
                object may represent a count of transmission
                errors on a particular interface that are not
                otherwise counted.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCStatsInternalMacTransmitErrors object for
                10 Gb/s or faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsinternalmactransmiterrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsLateCollisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times that a collision is
                detected on a particular interface later than
                one slotTime into the transmission of a packet.
                
                A (late) collision included in a count
                represented by an instance of this object is
                also considered as a (generic) collision for
                purposes of other collision-related
                statistics.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statslatecollisions',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsMultipleCollisionFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames that are involved in more
                than one collision and are subsequently
                transmitted successfully.
                
                A frame that is counted by an instance of this
                object is also counted by the corresponding
                instance of either the ifOutUcastPkts,
                ifOutMulticastPkts, or ifOutBroadcastPkts,
                and is not counted by the corresponding
                instance of the dot3StatsSingleCollisionFrames
                object.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statsmultiplecollisionframes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsRateControlAbility', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                'true' for interfaces operating at speeds above
                1000 Mb/s that support Rate Control through
                lowering the average data rate of the MAC
                sublayer, with frame granularity, and 'false'
                otherwise.
                ''',
                'dot3statsratecontrolability',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsRateControlStatus', REFERENCE_ENUM_CLASS, 'Dot3StatsratecontrolstatusEnum' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsratecontrolstatusEnum', 
                [], [], 
                '''                The current Rate Control mode of operation of
                the MAC sublayer of this interface.
                ''',
                'dot3statsratecontrolstatus',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsSingleCollisionFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of frames that are involved in a single
                collision, and are subsequently transmitted
                successfully.
                
                A frame that is counted by an instance of this
                object is also counted by the corresponding
                instance of either the ifOutUcastPkts,
                ifOutMulticastPkts, or ifOutBroadcastPkts,
                and is not counted by the corresponding
                instance of the dot3StatsMultipleCollisionFrames
                object.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statssinglecollisionframes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsSQETestErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of times that the SQE TEST ERROR
                is received on a particular interface. The
                SQE TEST ERROR is set in accordance with the
                rules for verification of the SQE detection
                mechanism in the PLS Carrier Sense Function as
                described in IEEE Std. 802.3, 2000 Edition,
                section 7.2.4.6.
                
                This counter does not increment on interfaces
                operating at speeds greater than 10 Mb/s, or on
                interfaces operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statssqetesterrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsSymbolErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For an interface operating at 100 Mb/s, the
                number of times there was an invalid data symbol
                when a valid carrier was present.
                
                For an interface operating in half-duplex mode
                at 1000 Mb/s, the number of times the receiving
                media is non-idle (a carrier event) for a period
                of time equal to or greater than slotTime, and
                during which there was at least one occurrence
                of an event that causes the PHY to indicate
                'Data reception error' or 'carrier extend error'
                on the GMII.
                
                For an interface operating in full-duplex mode
                at 1000 Mb/s, the number of times the receiving
                media is non-idle (a carrier event) for a period
                of time equal to or greater than minFrameSize,
                and during which there was at least one
                occurrence of an event that causes the PHY to
                indicate 'Data reception error' on the GMII.
                
                For an interface operating at 10 Gb/s, the
                number of times the receiving media is non-idle
                (a carrier event) for a period of time equal to
                or greater than minFrameSize, and during which
                there was at least one occurrence of an event
                that causes the PHY to indicate 'Receive Error'
                on the XGMII.
                
                The count represented by an instance of this
                object is incremented at most once per carrier
                event, even if multiple symbol errors occur
                during the carrier event.  This count does
                not increment if a collision is present.
                
                This counter does not increment when the
                interface is operating at 10 Mb/s.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCStatsSymbolErrors object for 10 Gb/s
                or faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3statssymbolerrors',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3StatsEntry',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Statstable' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Statstable',
            False, 
            [
            _MetaInfoClassMember('dot3StatsEntry', REFERENCE_LIST, 'Dot3Statsentry' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Statstable.Dot3Statsentry', 
                [], [], 
                '''                Statistics for a particular interface to an
                ethernet-like medium.
                ''',
                'dot3statsentry',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3StatsTable',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Colltable.Dot3Collentry' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Colltable.Dot3Collentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'EtherLike-MIB', True),
            _MetaInfoClassMember('dot3CollCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                The number of per-frame media collisions for
                which a particular collision histogram cell
                represents the frequency on a particular
                interface.
                ''',
                'dot3collcount',
                'EtherLike-MIB', True),
            _MetaInfoClassMember('dot3CollFrequencies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of individual MAC frames for which the
                transmission (successful or otherwise) on a
                particular interface occurs after the
                frame has experienced exactly the number
                of collisions in the associated
                dot3CollCount object.
                
                For example, a frame which is transmitted
                on interface 77 after experiencing
                exactly 4 collisions would be indicated
                by incrementing only dot3CollFrequencies.77.4.
                No other instance of dot3CollFrequencies would
                be incremented in this example.
                
                This counter does not increment when the
                interface is operating in full-duplex mode.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3collfrequencies',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3CollEntry',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Colltable' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Colltable',
            False, 
            [
            _MetaInfoClassMember('dot3CollEntry', REFERENCE_LIST, 'Dot3Collentry' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Colltable.Dot3Collentry', 
                [], [], 
                '''                A cell in the histogram of per-frame
                collisions for a particular interface.  An
                instance of this object represents the
                frequency of individual MAC frames for which
                the transmission (successful or otherwise) on a
                particular interface is accompanied by a
                particular number of media collisions.
                ''',
                'dot3collentry',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3CollTable',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Controltable.Dot3Controlentry' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Controltable.Dot3Controlentry',
            False, 
            [
            _MetaInfoClassMember('dot3StatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'dot3statsindex',
                'EtherLike-MIB', True),
            _MetaInfoClassMember('dot3ControlFunctionsSupported', REFERENCE_BITS, 'Dot3Controlfunctionssupported' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Controltable.Dot3Controlentry.Dot3Controlfunctionssupported', 
                [], [], 
                '''                A list of the possible MAC Control functions
                implemented for this interface.
                ''',
                'dot3controlfunctionssupported',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3ControlInUnknownOpcodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of MAC Control frames received on this
                interface that contain an opcode that is not
                supported by this device.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCControlInUnknownOpcodes object for 10 Gb/s
                or faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3controlinunknownopcodes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCControlInUnknownOpcodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of MAC Control frames received on this
                interface that contain an opcode that is not
                supported by this device.
                
                This counter is a 64 bit version of
                dot3ControlInUnknownOpcodes.  It should be used
                on interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hccontrolinunknownopcodes',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3ControlEntry',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Controltable' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Controltable',
            False, 
            [
            _MetaInfoClassMember('dot3ControlEntry', REFERENCE_LIST, 'Dot3Controlentry' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Controltable.Dot3Controlentry', 
                [], [], 
                '''                An entry in the table, containing information
                about the MAC Control sublayer on a single
                ethernet-like interface.
                ''',
                'dot3controlentry',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3ControlTable',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseadminmodeEnum' : _MetaInfoEnum('Dot3PauseadminmodeEnum', 'ydk.models.cisco_ios_xe.EtherLike_MIB',
        {
            'disabled':'disabled',
            'enabledXmit':'enabledXmit',
            'enabledRcv':'enabledRcv',
            'enabledXmitAndRcv':'enabledXmitAndRcv',
        }, 'EtherLike-MIB', _yang_ns._namespaces['EtherLike-MIB']),
    'EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseopermodeEnum' : _MetaInfoEnum('Dot3PauseopermodeEnum', 'ydk.models.cisco_ios_xe.EtherLike_MIB',
        {
            'disabled':'disabled',
            'enabledXmit':'enabledXmit',
            'enabledRcv':'enabledRcv',
            'enabledXmitAndRcv':'enabledXmitAndRcv',
        }, 'EtherLike-MIB', _yang_ns._namespaces['EtherLike-MIB']),
    'EtherlikeMib.Dot3Pausetable.Dot3Pauseentry' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Pausetable.Dot3Pauseentry',
            False, 
            [
            _MetaInfoClassMember('dot3StatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'dot3statsindex',
                'EtherLike-MIB', True),
            _MetaInfoClassMember('dot3HCInPauseFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of MAC Control frames received on this
                interface with an opcode indicating the PAUSE
                operation.
                
                This counter does not increment when the
                interface is operating in half-duplex mode.
                
                This counter is a 64 bit version of
                dot3InPauseFrames.  It should be used on
                interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcinpauseframes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCOutPauseFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of MAC Control frames transmitted on
                this interface with an opcode indicating the
                PAUSE operation.
                
                This counter does not increment when the
                interface is operating in half-duplex mode.
                
                This counter is a 64 bit version of
                dot3OutPauseFrames.  It should be used on
                interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcoutpauseframes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3InPauseFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of MAC Control frames received on this
                interface with an opcode indicating the PAUSE
                operation.
                
                This counter does not increment when the
                interface is operating in half-duplex mode.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCInPauseFrames object for 10 Gb/s or
                faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3inpauseframes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3OutPauseFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of MAC Control frames transmitted on
                this interface with an opcode indicating the
                PAUSE operation.
                
                This counter does not increment when the
                interface is operating in half-duplex mode.
                
                For interfaces operating at 10 Gb/s, this
                counter can roll over in less than 5 minutes if
                it is incrementing at its maximum rate.  Since
                that amount of time could be less than a
                management station's poll cycle time, in order
                to avoid a loss of information, a management
                station is advised to poll the
                dot3HCOutPauseFrames object for 10 Gb/s or
                faster interfaces.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3outpauseframes',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3PauseAdminMode', REFERENCE_ENUM_CLASS, 'Dot3PauseadminmodeEnum' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseadminmodeEnum', 
                [], [], 
                '''                This object is used to configure the default
                administrative PAUSE mode for this interface.
                
                This object represents the
                administratively-configured PAUSE mode for this
                interface.  If auto-negotiation is not enabled
                or is not implemented for the active MAU
                attached to this interface, the value of this
                object determines the operational PAUSE mode
                of the interface whenever it is operating in
                full-duplex mode.  In this case, a set to this
                object will force the interface into the
                specified mode.
                
                If auto-negotiation is implemented and enabled
                for the MAU attached to this interface, the
                PAUSE mode for this interface is determined by
                auto-negotiation, and the value of this object
                denotes the mode to which the interface will
                automatically revert if/when auto-negotiation is
                later disabled.  Note that when auto-negotiation
                is running, administrative control of the PAUSE
                mode may be accomplished using the
                ifMauAutoNegCapAdvertisedBits object in the
                MAU-MIB.
                
                Note that the value of this object is ignored
                when the interface is not operating in
                full-duplex mode.
                
                An attempt to set this object to
                'enabledXmit(2)' or 'enabledRcv(3)' will fail
                on interfaces that do not support operation
                at greater than 100 Mb/s.
                ''',
                'dot3pauseadminmode',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3PauseOperMode', REFERENCE_ENUM_CLASS, 'Dot3PauseopermodeEnum' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseopermodeEnum', 
                [], [], 
                '''                This object reflects the PAUSE mode currently
                in use on this interface, as determined by
                either (1) the result of the auto-negotiation
                function or (2) if auto-negotiation is not
                enabled or is not implemented for the active MAU
                attached to this interface, by the value of
                dot3PauseAdminMode.  Interfaces operating at
                100 Mb/s or less will never return
                'enabledXmit(2)' or 'enabledRcv(3)'.  Interfaces
                operating in half-duplex mode will always return
                'disabled(1)'.  Interfaces on which
                auto-negotiation is enabled but not yet
                completed should return the value
                'disabled(1)'.
                ''',
                'dot3pauseopermode',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3PauseEntry',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Pausetable' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Pausetable',
            False, 
            [
            _MetaInfoClassMember('dot3PauseEntry', REFERENCE_LIST, 'Dot3Pauseentry' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Pausetable.Dot3Pauseentry', 
                [], [], 
                '''                An entry in the table, containing information
                about the MAC Control PAUSE function on a single
                ethernet-like interface.
                ''',
                'dot3pauseentry',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3PauseTable',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry',
            False, 
            [
            _MetaInfoClassMember('dot3StatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'dot3statsindex',
                'EtherLike-MIB', True),
            _MetaInfoClassMember('dot3HCStatsAlignmentErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of frames received on a particular
                interface that are not an integral number of
                octets in length and do not pass the FCS check.
                
                The count represented by an instance of this
                object is incremented when the alignmentError
                status is returned by the MAC service to the
                LLC (or other MAC user). Received frames for
                which multiple error conditions pertain are,
                according to the conventions of IEEE 802.3
                Layer Management, counted exclusively according
                to the error status presented to the LLC.
                
                This counter does not increment for group
                encoding schemes greater than 4 bits per group.
                
                This counter is a 64 bit version of
                dot3StatsAlignmentErrors.  It should be used
                on interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcstatsalignmenterrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCStatsFCSErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of frames received on a particular
                interface that are an integral number of octets
                in length but do not pass the FCS check.  This
                count does not include frames received with
                frame-too-long or frame-too-short error.
                
                The count represented by an instance of this
                object is incremented when the frameCheckError
                status is returned by the MAC service to the
                LLC (or other MAC user). Received frames for
                which multiple error conditions pertain are,
                according to the conventions of IEEE 802.3
                Layer Management, counted exclusively according
                to the error status presented to the LLC.
                
                Note:  Coding errors detected by the physical
                layer for speeds above 10 Mb/s will cause the
                frame to fail the FCS check.
                
                This counter is a 64 bit version of
                dot3StatsFCSErrors.  It should be used on
                interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcstatsfcserrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCStatsFrameTooLongs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of frames received on a particular
                interface that exceed the maximum permitted
                frame size.
                
                The count represented by an instance of this
                object is incremented when the frameTooLong
                status is returned by the MAC service to the
                LLC (or other MAC user). Received frames for
                which multiple error conditions pertain are,
                according to the conventions of IEEE 802.3
                Layer Management, counted exclusively according
                to the error status presented to the LLC.
                
                This counter is a 64 bit version of
                dot3StatsFrameTooLongs.  It should be used on
                interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcstatsframetoolongs',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCStatsInternalMacReceiveErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of frames for which reception on a
                particular interface fails due to an internal
                MAC sublayer receive error. A frame is only
                counted by an instance of this object if it is
                not counted by the corresponding instance of
                either the dot3StatsFrameTooLongs object, the
                dot3StatsAlignmentErrors object, or the
                dot3StatsFCSErrors object.
                
                The precise meaning of the count represented by
                an instance of this object is implementation-
                specific.  In particular, an instance of this
                object may represent a count of receive errors
                on a particular interface that are not
                otherwise counted.
                
                This counter is a 64 bit version of
                dot3StatsInternalMacReceiveErrors.  It should be
                used on interfaces operating at 10 Gb/s or
                faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcstatsinternalmacreceiveerrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCStatsInternalMacTransmitErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                A count of frames for which transmission on a
                particular interface fails due to an internal
                MAC sublayer transmit error. A frame is only
                counted by an instance of this object if it is
                not counted by the corresponding instance of
                either the dot3StatsLateCollisions object, the
                dot3StatsExcessiveCollisions object, or the
                dot3StatsCarrierSenseErrors object.
                
                The precise meaning of the count represented by
                an instance of this object is implementation-
                specific.  In particular, an instance of this
                object may represent a count of transmission
                errors on a particular interface that are not
                otherwise counted.
                
                This counter is a 64 bit version of
                dot3StatsInternalMacTransmitErrors.  It should
                be used on interfaces operating at 10 Gb/s or
                faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcstatsinternalmactransmiterrors',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCStatsSymbolErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                For an interface operating at 100 Mb/s, the
                number of times there was an invalid data symbol
                when a valid carrier was present.
                
                For an interface operating in half-duplex mode
                at 1000 Mb/s, the number of times the receiving
                media is non-idle (a carrier event) for a period
                of time equal to or greater than slotTime, and
                during which there was at least one occurrence
                of an event that causes the PHY to indicate
                'Data reception error' or 'carrier extend error'
                on the GMII.
                
                For an interface operating in full-duplex mode
                at 1000 Mb/s, the number of times the receiving
                media is non-idle (a carrier event) for a period
                of time equal to or greater than minFrameSize,
                and during which there was at least one
                occurrence of an event that causes the PHY to
                indicate 'Data reception error' on the GMII.
                
                For an interface operating at 10 Gb/s, the
                number of times the receiving media is non-idle
                (a carrier event) for a period of time equal to
                or greater than minFrameSize, and during which
                there was at least one occurrence of an event
                that causes the PHY to indicate 'Receive Error'
                on the XGMII.
                
                The count represented by an instance of this
                object is incremented at most once per carrier
                event, even if multiple symbol errors occur
                during the carrier event.  This count does
                not increment if a collision is present.
                
                This counter is a 64 bit version of
                dot3StatsSymbolErrors.  It should be used on
                interfaces operating at 10 Gb/s or faster.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management
                system, and at other times as indicated by the
                value of ifCounterDiscontinuityTime.
                ''',
                'dot3hcstatssymbolerrors',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3HCStatsEntry',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib.Dot3Hcstatstable' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib.Dot3Hcstatstable',
            False, 
            [
            _MetaInfoClassMember('dot3HCStatsEntry', REFERENCE_LIST, 'Dot3Hcstatsentry' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry', 
                [], [], 
                '''                An entry containing 64-bit statistics for a
                single ethernet-like interface.
                ''',
                'dot3hcstatsentry',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'dot3HCStatsTable',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
    'EtherlikeMib' : {
        'meta_info' : _MetaInfoClass('EtherlikeMib',
            False, 
            [
            _MetaInfoClassMember('dot3CollTable', REFERENCE_CLASS, 'Dot3Colltable' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Colltable', 
                [], [], 
                '''                A collection of collision histograms for a
                particular set of interfaces.
                ''',
                'dot3colltable',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3ControlTable', REFERENCE_CLASS, 'Dot3Controltable' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Controltable', 
                [], [], 
                '''                A table of descriptive and status information
                about the MAC Control sublayer on the
                ethernet-like interfaces attached to a
                particular system.  There will be one row in
                this table for each ethernet-like interface in
                the system which implements the MAC Control
                sublayer.  If some, but not all, of the
                ethernet-like interfaces in the system implement
                the MAC Control sublayer, there will be fewer
                rows in this table than in the dot3StatsTable.
                ''',
                'dot3controltable',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3HCStatsTable', REFERENCE_CLASS, 'Dot3Hcstatstable' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Hcstatstable', 
                [], [], 
                '''                A table containing 64-bit versions of error
                counters from the dot3StatsTable.  The 32-bit
                versions of these counters may roll over quite
                quickly on higher speed ethernet interfaces.
                The counters that have 64-bit versions in this
                table are the counters that apply to full-duplex
                interfaces, since 10 Gb/s and faster
                ethernet-like interfaces do not support
                half-duplex, and very few 1000 Mb/s
                ethernet-like interfaces support half-duplex.
                
                Entries in this table are recommended for
                interfaces capable of operating at 1000 Mb/s or
                faster, and are required for interfaces capable
                of operating at 10 Gb/s or faster.  Lower speed
                ethernet-like interfaces do not need entries in
                this table, in which case there may be fewer
                entries in this table than in the
                dot3StatsTable. However, implementations
                containing interfaces with a mix of speeds may
                choose to implement entries in this table for
                all ethernet-like interfaces.
                ''',
                'dot3hcstatstable',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3PauseTable', REFERENCE_CLASS, 'Dot3Pausetable' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Pausetable', 
                [], [], 
                '''                A table of descriptive and status information
                about the MAC Control PAUSE function on the
                ethernet-like interfaces attached to a
                particular system. There will be one row in
                this table for each ethernet-like interface in
                the system which supports the MAC Control PAUSE
                function (i.e., the 'pause' bit in the
                corresponding instance of
                dot3ControlFunctionsSupported is set).  If some,
                but not all, of the ethernet-like interfaces in
                the system implement the MAC Control PAUSE
                function (for example, if some interfaces only
                support half-duplex), there will be fewer rows
                in this table than in the dot3StatsTable.
                ''',
                'dot3pausetable',
                'EtherLike-MIB', False),
            _MetaInfoClassMember('dot3StatsTable', REFERENCE_CLASS, 'Dot3Statstable' , 'ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherlikeMib.Dot3Statstable', 
                [], [], 
                '''                Statistics for a collection of ethernet-like
                interfaces attached to a particular system.
                There will be one row in this table for each
                ethernet-like interface in the system.
                ''',
                'dot3statstable',
                'EtherLike-MIB', False),
            ],
            'EtherLike-MIB',
            'EtherLike-MIB',
            _yang_ns._namespaces['EtherLike-MIB'],
        'ydk.models.cisco_ios_xe.EtherLike_MIB'
        ),
    },
}
_meta_table['EtherlikeMib.Dot3Statstable.Dot3Statsentry']['meta_info'].parent =_meta_table['EtherlikeMib.Dot3Statstable']['meta_info']
_meta_table['EtherlikeMib.Dot3Colltable.Dot3Collentry']['meta_info'].parent =_meta_table['EtherlikeMib.Dot3Colltable']['meta_info']
_meta_table['EtherlikeMib.Dot3Controltable.Dot3Controlentry']['meta_info'].parent =_meta_table['EtherlikeMib.Dot3Controltable']['meta_info']
_meta_table['EtherlikeMib.Dot3Pausetable.Dot3Pauseentry']['meta_info'].parent =_meta_table['EtherlikeMib.Dot3Pausetable']['meta_info']
_meta_table['EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry']['meta_info'].parent =_meta_table['EtherlikeMib.Dot3Hcstatstable']['meta_info']
_meta_table['EtherlikeMib.Dot3Statstable']['meta_info'].parent =_meta_table['EtherlikeMib']['meta_info']
_meta_table['EtherlikeMib.Dot3Colltable']['meta_info'].parent =_meta_table['EtherlikeMib']['meta_info']
_meta_table['EtherlikeMib.Dot3Controltable']['meta_info'].parent =_meta_table['EtherlikeMib']['meta_info']
_meta_table['EtherlikeMib.Dot3Pausetable']['meta_info'].parent =_meta_table['EtherlikeMib']['meta_info']
_meta_table['EtherlikeMib.Dot3Hcstatstable']['meta_info'].parent =_meta_table['EtherlikeMib']['meta_info']
