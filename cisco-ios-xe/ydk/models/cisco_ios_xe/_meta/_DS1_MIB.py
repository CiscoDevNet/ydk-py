


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1ChannelizationEnum' : _MetaInfoEnum('Dsx1ChannelizationEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'disabled':'disabled',
            'enabledDs0':'enabledDs0',
            'enabledDs1':'enabledDs1',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinecodingEnum' : _MetaInfoEnum('Dsx1LinecodingEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'dsx1JBZS':'dsx1JBZS',
            'dsx1B8ZS':'dsx1B8ZS',
            'dsx1HDB3':'dsx1HDB3',
            'dsx1ZBTSI':'dsx1ZBTSI',
            'dsx1AMI':'dsx1AMI',
            'other':'other',
            'dsx1B6ZS':'dsx1B6ZS',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinestatuschangetrapenableEnum' : _MetaInfoEnum('Dsx1LinestatuschangetrapenableEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinetypeEnum' : _MetaInfoEnum('Dsx1LinetypeEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'other':'other',
            'dsx1ESF':'dsx1ESF',
            'dsx1D4':'dsx1D4',
            'dsx1E1':'dsx1E1',
            'dsx1E1CRC':'dsx1E1CRC',
            'dsx1E1MF':'dsx1E1MF',
            'dsx1E1CRCMF':'dsx1E1CRCMF',
            'dsx1Unframed':'dsx1Unframed',
            'dsx1E1Unframed':'dsx1E1Unframed',
            'dsx1DS2M12':'dsx1DS2M12',
            'dsx2E2':'dsx2E2',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LoopbackconfigEnum' : _MetaInfoEnum('Dsx1LoopbackconfigEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'dsx1NoLoop':'dsx1NoLoop',
            'dsx1PayloadLoop':'dsx1PayloadLoop',
            'dsx1LineLoop':'dsx1LineLoop',
            'dsx1OtherLoop':'dsx1OtherLoop',
            'dsx1InwardLoop':'dsx1InwardLoop',
            'dsx1DualLoop':'dsx1DualLoop',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SendcodeEnum' : _MetaInfoEnum('Dsx1SendcodeEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'dsx1SendNoCode':'dsx1SendNoCode',
            'dsx1SendLineCode':'dsx1SendLineCode',
            'dsx1SendPayloadCode':'dsx1SendPayloadCode',
            'dsx1SendResetCode':'dsx1SendResetCode',
            'dsx1SendQRS':'dsx1SendQRS',
            'dsx1Send511Pattern':'dsx1Send511Pattern',
            'dsx1Send3in24Pattern':'dsx1Send3in24Pattern',
            'dsx1SendOtherTestPattern':'dsx1SendOtherTestPattern',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SignalmodeEnum' : _MetaInfoEnum('Dsx1SignalmodeEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'none':'none',
            'robbedBit':'robbedBit',
            'bitOriented':'bitOriented',
            'messageOriented':'messageOriented',
            'other':'other',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1TransmitclocksourceEnum' : _MetaInfoEnum('Dsx1TransmitclocksourceEnum', 'ydk.models.cisco_ios_xe.DS1_MIB',
        {
            'loopTiming':'loopTiming',
            'localTiming':'localTiming',
            'throughTiming':'throughTiming',
        }, 'DS1-MIB', _yang_ns._namespaces['DS1-MIB']),
    'Ds1Mib.Dsx1Configtable.Dsx1Configentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Configtable.Dsx1Configentry',
            False, 
            [
            _MetaInfoClassMember('dsx1LineIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object should be made equal to ifIndex.  The
                next paragraph describes its previous usage.
                Making the object equal to ifIndex allows proper
                use of ifStackTable and ds0/ds0bundle mibs.
                
                Previously, this object is the identifier of a DS1
                Interface on a managed device.  If there is an
                ifEntry that is directly associated with this and
                only this DS1 interface, it should have the same
                value as ifIndex.  Otherwise, number the
                dsx1LineIndices with an unique identifier
                following the rules of choosing a number that is
                greater than ifNumber and numbering the inside
                interfaces (e.g., equipment side) with even
                numbers and outside interfaces (e.g, network side)
                with odd numbers.
                ''',
                'dsx1lineindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1Channelization', REFERENCE_ENUM_CLASS, 'Dsx1ChannelizationEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1ChannelizationEnum', 
                [], [], 
                '''                Indicates whether this ds1/e1 is channelized or
                unchannelized.  The value of enabledDs0 indicates
                that this is a DS1 channelized into DS0s.  The
                value of enabledDs1 indicated that this is a DS2
                channelized into DS1s.  Setting this value will
                cause the creation or deletion of entries in the
                ifTable for the DS0s that are within the DS1.
                ''',
                'dsx1channelization',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CircuitIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This variable contains the transmission vendor's
                circuit identifier, for the purpose of
                facilitating troubleshooting.
                ''',
                'dsx1circuitidentifier',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1Ds1ChannelNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '28')], [], 
                '''                This variable represents the channel number of
                the DS1/E1 on its parent Ds2/E2 or DS3/E3.  A
                value of 0 indicated this DS1/E1 does not have a
                parent DS3/E3.
                ''',
                'dsx1ds1channelnumber',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1Fdl', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                This bitmap describes the use of  the  facili-
                ties data link, and is the sum of the capabili-
                ties.  Set any bits that are appropriate:
                
                other(1),
                dsx1AnsiT1403(2),
                dsx1Att54016(4),
                dsx1FdlNone(8)
                
                 'other' indicates that a protocol  other  than
                one following is used.
                
                 'dsx1AnsiT1403' refers to the  FDL  exchange
                recommended by ANSI.
                
                 'dsx1Att54016' refers to ESF FDL exchanges.
                
                 'dsx1FdlNone' indicates that the device  does
                not use the FDL.
                ''',
                'dsx1fdl',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This value for this object is equal to the value
                of ifIndex from the Interfaces table of MIB II
                (RFC 1213).
                ''',
                'dsx1ifindex',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1InvalidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of intervals in the range from 0 to
                dsx1ValidIntervals for which no data is
                available.  This object will typically be zero
                except in cases where the data for some intervals
                are not available (e.g., in proxy situations).
                ''',
                'dsx1invalidintervals',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LineCoding', REFERENCE_ENUM_CLASS, 'Dsx1LinecodingEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinecodingEnum', 
                [], [], 
                '''                This variable describes the variety of Zero Code
                Suppression used on this interface, which in turn
                affects a number of its characteristics.
                
                dsx1JBZS refers the Jammed Bit Zero Suppression,
                in which the AT&T specification of at least one
                pulse every 8 bit periods is literally implemented
                by forcing a pulse in bit 8 of each channel.
                Thus, only seven bits per channel, or 1.344 Mbps,
                is available for data.
                
                dsx1B8ZS refers to the use of a specified pattern
                of normal bits and bipolar violations which are
                used to replace a sequence of eight zero bits.
                
                ANSI Clear Channels may use dsx1ZBTSI, or Zero
                Byte Time Slot Interchange.
                
                E1 links, with or without CRC, use dsx1HDB3 or
                dsx1AMI.
                
                dsx1AMI refers to a mode wherein no zero code
                suppression is present and the line encoding does
                not solve the problem directly.  In this
                application, the higher layer must provide data
                which meets or exceeds the pulse density
                requirements, such as inverting HDLC data.
                
                dsx1B6ZS refers to the user of a specifed pattern
                of normal bits and bipolar violations which are
                used to replace a sequence of six zero bits.  Used
                for DS2.
                ''',
                'dsx1linecoding',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LineLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '64000')], [], 
                '''                The length of the ds1 line in meters. This
                objects provides information for line build out
                circuitry.  This object is only useful if the
                interface has configurable line build out
                circuitry.
                ''',
                'dsx1linelength',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LineStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '131071')], [], 
                '''                This variable indicates the Line Status of the
                interface.  It contains loopback, failure,
                received 'alarm' and transmitted 'alarms
                information.
                
                The dsx1LineStatus is a bit map represented as a
                sum, therefore, it can represent multiple failures
                (alarms) and a LoopbackState simultaneously.
                
                dsx1NoAlarm must be set if and only if no other
                flag is set.
                
                If the dsx1loopbackState bit is set, the loopback
                in effect can be determined from the
                dsx1loopbackConfig object.
                The various bit positions are:
                1     dsx1NoAlarm           No alarm present
                2     dsx1RcvFarEndLOF      Far end LOF (a.k.a., Yellow Alarm)
                4     dsx1XmtFarEndLOF      Near end sending LOF Indication
                8     dsx1RcvAIS            Far end sending AIS
                16     dsx1XmtAIS            Near end sending AIS
                32     dsx1LossOfFrame       Near end LOF (a.k.a., Red Alarm)
                64     dsx1LossOfSignal      Near end Loss Of Signal
                128     dsx1LoopbackState     Near end is looped
                256     dsx1T16AIS            E1 TS16 AIS
                512     dsx1RcvFarEndLOMF     Far End Sending TS16 LOMF
                1024     dsx1XmtFarEndLOMF     Near End Sending TS16 LOMF
                2048     dsx1RcvTestCode       Near End detects a test code
                4096     dsx1OtherFailure      any line status not defined here
                8192     dsx1UnavailSigState   Near End in Unavailable Signal
                                 State
                16384     dsx1NetEquipOOS       Carrier Equipment Out of Service
                32768     dsx1RcvPayloadAIS     DS2 Payload AIS
                65536     dsx1Ds2PerfThreshold  DS2 Performance Threshold
                                 Exceeded
                ''',
                'dsx1linestatus',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LineStatusChangeTrapEnable', REFERENCE_ENUM_CLASS, 'Dsx1LinestatuschangetrapenableEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinestatuschangetrapenableEnum', 
                [], [], 
                '''                Indicates whether dsx1LineStatusChange traps
                should be generated for this interface.
                ''',
                'dsx1linestatuschangetrapenable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LineStatusLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of MIB II's sysUpTime object at the
                time this DS1 entered its current line status
                state.  If the current state was entered prior to
                the last re-initialization of the proxy-agent,
                then this object contains a zero value.
                ''',
                'dsx1linestatuslastchange',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LineType', REFERENCE_ENUM_CLASS, 'Dsx1LinetypeEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinetypeEnum', 
                [], [], 
                '''                This variable indicates  the  variety  of  DS1
                Line  implementing  this  circuit.  The type of
                circuit affects the number of bits  per  second
                that  the circuit can reasonably carry, as well
                as the interpretation of the  usage  and  error
                statistics.  The values, in sequence, describe:
                
                TITLE:         SPECIFICATION:
                dsx1ESF         Extended SuperFrame DS1 (T1.107)
                dsx1D4          AT&T D4 format DS1 (T1.107)
                dsx1E1          ITU-T Recommendation G.704
                                 (Table 4a)
                dsx1E1-CRC      ITU-T Recommendation G.704
                                 (Table 4b)
                dsxE1-MF        G.704 (Table 4a) with TS16
                                 multiframing enabled
                dsx1E1-CRC-MF   G.704 (Table 4b) with TS16
                                 multiframing enabled
                dsx1Unframed    DS1 with No Framing
                dsx1E1Unframed  E1 with No Framing (G.703)
                dsx1DS2M12      DS2 frame format (T1.107)
                dsx1E2          E2 frame format (G.704)
                
                For clarification, the capacity for each E1 type
                is as listed below:
                dsx1E1Unframed - E1, no framing = 32 x 64k = 2048k
                dsx1E1 or dsx1E1CRC - E1, with framing,
                   no signalling = 31 x 64k = 1984k
                dsx1E1MF or dsx1E1CRCMF - E1, with framing,
                   signalling = 30 x 64k = 1920k
                
                For further information See ITU-T Recomm G.704
                ''',
                'dsx1linetype',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LoopbackConfig', REFERENCE_ENUM_CLASS, 'Dsx1LoopbackconfigEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LoopbackconfigEnum', 
                [], [], 
                '''                This variable represents the desired loopback
                configuration of the DS1 interface.  Agents
                supporting read/write access should return
                inconsistentValue in response to a requested
                loopback state that the interface does not
                support.  The values mean:
                
                dsx1NoLoop
                 Not in the loopback state.  A device that is not
                capable of performing a loopback on the interface
                shall always return this as its value.
                
                dsx1PayloadLoop
                 The received signal at this interface is looped
                through the device.  Typically the received signal
                is looped back for retransmission after it has
                passed through the device's framing function.
                
                dsx1LineLoop
                 The received signal at this interface does not go
                through the device (minimum penetration) but is
                looped back out.
                
                dsx1OtherLoop
                 Loopbacks that are not defined here.
                
                dsx1InwardLoop
                 The transmitted signal at this interface is
                looped back and received by the same interface.
                What is transmitted onto the line is product
                dependent.
                
                dsx1DualLoop
                 Both dsx1LineLoop and dsx1InwardLoop will be
                active simultaneously.
                ''',
                'dsx1loopbackconfig',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1LoopbackStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '127')], [], 
                '''                This variable represents the current state of the
                loopback on the DS1 interface.  It contains
                information about loopbacks established by a
                manager and remotely from the far end.
                
                The dsx1LoopbackStatus is a bit map represented as
                a sum, therefore is can represent multiple
                loopbacks simultaneously.
                
                The various bit positions are:
                 1  dsx1NoLoopback
                 2  dsx1NearEndPayloadLoopback
                 4  dsx1NearEndLineLoopback
                 8  dsx1NearEndOtherLoopback
                16  dsx1NearEndInwardLoopback
                32  dsx1FarEndPayloadLoopback
                64  dsx1FarEndLineLoopback
                ''',
                'dsx1loopbackstatus',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1SendCode', REFERENCE_ENUM_CLASS, 'Dsx1SendcodeEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SendcodeEnum', 
                [], [], 
                '''                This variable indicates what type of code is
                being sent across the DS1 interface by the device.
                Setting this variable causes the interface to send
                the code requested.  The values mean:
                dsx1SendNoCode
                sending looped or normal data
                
                dsx1SendLineCode
                sending a request for a line loopback
                
                dsx1SendPayloadCode
                sending a request for a payload loopback
                
                dsx1SendResetCode
                sending a loopback termination request
                
                dsx1SendQRS
                sending a Quasi-Random Signal  (QRS)  test
                pattern
                
                dsx1Send511Pattern
                sending a 511 bit fixed test pattern
                
                dsx1Send3in24Pattern
                sending a fixed test pattern of 3 bits set
                in 24
                
                dsx1SendOtherTestPattern
                sending a test pattern  other  than  those
                described by this object
                ''',
                'dsx1sendcode',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1SignalMode', REFERENCE_ENUM_CLASS, 'Dsx1SignalmodeEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SignalmodeEnum', 
                [], [], 
                '''                'none' indicates that no bits are reserved for
                signaling on this channel.
                
                'robbedBit' indicates that DS1 Robbed Bit  Sig-
                naling is in use.
                
                'bitOriented' indicates that E1 Channel  Asso-
                ciated Signaling is in use.
                
                'messageOriented' indicates that Common  Chan-
                nel Signaling is in use either on channel 16 of
                an E1 link or channel 24 of a DS1.
                ''',
                'dsx1signalmode',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '899')], [], 
                '''                The number of seconds that have elapsed since
                the beginning of the near end current error-
                measurement period.  If, for some reason, such
                as an adjustment in the system's time-of-day
                clock, the current interval exceeds the maximum
                value, the agent will return the maximum value.
                ''',
                'dsx1timeelapsed',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TransmitClockSource', REFERENCE_ENUM_CLASS, 'Dsx1TransmitclocksourceEnum' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1TransmitclocksourceEnum', 
                [], [], 
                '''                The source of Transmit Clock.
                'loopTiming' indicates that the recovered re-
                ceive clock is used as the transmit clock.
                
                'localTiming' indicates that a local clock
                source is used or when an external clock is
                attached to the box containing the interface.
                
                'throughTiming' indicates that recovered re-
                ceive clock from another interface is used as
                the transmit clock.
                ''',
                'dsx1transmitclocksource',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1ValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of previous near end intervals for
                which data was collected.  The value will be
                96 unless the interface was brought online within
                the last 24 hours, in which case the value will be
                the number of complete 15 minute near end
                intervals since the interface has been online.  In
                the case where the agent is a proxy, it is
                possible that some intervals are unavailable.  In
                this case, this interval is the maximum interval
                number for which data is available.
                ''',
                'dsx1validintervals',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1ConfigEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Configtable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Configtable',
            False, 
            [
            _MetaInfoClassMember('dsx1ConfigEntry', REFERENCE_LIST, 'Dsx1Configentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable.Dsx1Configentry', 
                [], [], 
                '''                An entry in the DS1 Configuration table.
                ''',
                'dsx1configentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1ConfigTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Currenttable.Dsx1Currententry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Currenttable.Dsx1Currententry',
            False, 
            [
            _MetaInfoClassMember('dsx1CurrentIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies  the
                DS1 interface to which this entry is applicable.
                The interface identified by a particular value of
                this index is the same interface as identified by
                the same value as a dsx1LineIndex object
                instance.
                ''',
                'dsx1currentindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1CurrentBESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Bursty Errored Seconds.
                ''',
                'dsx1currentbess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentCSSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Controlled Slip Seconds.
                ''',
                'dsx1currentcsss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentDMs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Degraded Minutes.
                ''',
                'dsx1currentdms',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Errored Seconds.
                ''',
                'dsx1currentess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentLCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Code Violations (LCVs).
                ''',
                'dsx1currentlcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Errored Seconds.
                ''',
                'dsx1currentless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Path Coding Violations.
                ''',
                'dsx1currentpcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Severely Errored Framing Seconds.
                ''',
                'dsx1currentsefss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Severely Errored Seconds.
                ''',
                'dsx1currentsess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Unavailable Seconds.
                ''',
                'dsx1currentuass',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1CurrentEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Currenttable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Currenttable',
            False, 
            [
            _MetaInfoClassMember('dsx1CurrentEntry', REFERENCE_LIST, 'Dsx1Currententry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Currenttable.Dsx1Currententry', 
                [], [], 
                '''                An entry in the DS1 Current table.
                ''',
                'dsx1currententry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1CurrentTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry',
            False, 
            [
            _MetaInfoClassMember('dsx1IntervalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS1
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is the same interface as identified by the
                same value as a dsx1LineIndex object instance.
                ''',
                'dsx1intervalindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1IntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, where 1 is the most
                recently completed 15 minute interval and 96 is
                the 15 minutes interval completed 23 hours and 45
                minutes prior to interval 1.
                ''',
                'dsx1intervalnumber',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1IntervalBESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Bursty Errored Seconds.
                ''',
                'dsx1intervalbess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalCSSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Controlled Slip Seconds.
                ''',
                'dsx1intervalcsss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalDMs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Degraded Minutes.
                ''',
                'dsx1intervaldms',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Errored Seconds.
                ''',
                'dsx1intervaless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalLCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Code Violations.
                ''',
                'dsx1intervallcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Errored Seconds.
                ''',
                'dsx1intervalless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Path Coding Violations.
                ''',
                'dsx1intervalpcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Severely Errored Framing Seconds.
                ''',
                'dsx1intervalsefss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Severely Errored Seconds.
                ''',
                'dsx1intervalsess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Unavailable Seconds.  This object
                may decrease if the occurance of unavailable
                seconds occurs across an inteval boundary.
                ''',
                'dsx1intervaluass',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'dsx1intervalvaliddata',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1IntervalEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Intervaltable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Intervaltable',
            False, 
            [
            _MetaInfoClassMember('dsx1IntervalEntry', REFERENCE_LIST, 'Dsx1Intervalentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry', 
                [], [], 
                '''                An entry in the DS1 Interval table.
                ''',
                'dsx1intervalentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1IntervalTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Totaltable.Dsx1Totalentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Totaltable.Dsx1Totalentry',
            False, 
            [
            _MetaInfoClassMember('dsx1TotalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS1
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is the same interface as identified by the
                same value as a dsx1LineIndex object instance.
                ''',
                'dsx1totalindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1TotalBESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Bursty Errored Seconds (BESs)
                encountered by a DS1 interface in the previous 24
                hour interval. Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1totalbess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalCSSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Controlled Slip Seconds encountered
                by a DS1 interface in the previous 24 hour
                interval.  Invalid 15 minute intervals count as
                0.
                ''',
                'dsx1totalcsss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalDMs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Degraded Minutes (DMs) encountered
                by a DS1 interface in the previous 24 hour
                interval.  Invalid 15 minute intervals count as
                0.
                ''',
                'dsx1totaldms',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The sum of Errored Seconds encountered by a DS1
                interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx1totaless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalLCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Code Violations (LCVs)
                encountered by a DS1 interface in the current 15
                minute interval.  Invalid 15 minute intervals
                count as 0.
                ''',
                'dsx1totallcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Errored Seconds encountered by
                a DS1 interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx1totalless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Path Coding Violations encountered
                by a DS1 interface in the previous 24 hour
                interval.  Invalid 15 minute intervals count as
                0.
                ''',
                'dsx1totalpcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Severely Errored Framing Seconds
                encountered by a DS1 interface in the previous 24
                hour interval.  Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1totalsefss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Severely Errored Seconds
                encountered by a DS1 interface in the previous 24
                hour interval.  Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1totalsess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Unavailable Seconds encountered by
                a DS1 interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx1totaluass',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1TotalEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Totaltable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Totaltable',
            False, 
            [
            _MetaInfoClassMember('dsx1TotalEntry', REFERENCE_LIST, 'Dsx1Totalentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Totaltable.Dsx1Totalentry', 
                [], [], 
                '''                An entry in the DS1 Total table.
                ''',
                'dsx1totalentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1TotalTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry',
            False, 
            [
            _MetaInfoClassMember('dsx1FarEndCurrentIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS1
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is identical to the interface identified by
                the same value of dsx1LineIndex.
                ''',
                'dsx1farendcurrentindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1FarEndCurrentBESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Bursty Errored Seconds.
                ''',
                'dsx1farendcurrentbess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentCSSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Controlled Slip Seconds.
                ''',
                'dsx1farendcurrentcsss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentDMs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Degraded Minutes.
                ''',
                'dsx1farendcurrentdms',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Errored Seconds.
                ''',
                'dsx1farendcurrentess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Line Errored Seconds.
                ''',
                'dsx1farendcurrentless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Path Coding Violations.
                ''',
                'dsx1farendcurrentpcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Severely Errored Framing
                Seconds.
                ''',
                'dsx1farendcurrentsefss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Severely Errored Seconds.
                ''',
                'dsx1farendcurrentsess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Unavailable Seconds.
                ''',
                'dsx1farendcurrentuass',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndInvalidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of intervals in the range from 0 to
                dsx1FarEndValidIntervals for which no data is
                available.  This object will typically be zero
                except in cases where the data for some intervals
                are not available (e.g., in proxy situations).
                ''',
                'dsx1farendinvalidintervals',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '899')], [], 
                '''                The number of seconds that have elapsed since the
                beginning of the far end current error-measurement
                period.  If, for some reason, such as an
                adjustment in the system's time-of-day clock, the
                current interval exceeds the maximum value, the
                agent will return the maximum value.
                ''',
                'dsx1farendtimeelapsed',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of previous far end intervals for
                which data was collected.  The value will be
                96 unless the interface was brought online within
                the last 24 hours, in which case the value will be
                the number of complete 15 minute far end intervals
                since the interface has been online.
                ''',
                'dsx1farendvalidintervals',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FarEndCurrentEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Farendcurrenttable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Farendcurrenttable',
            False, 
            [
            _MetaInfoClassMember('dsx1FarEndCurrentEntry', REFERENCE_LIST, 'Dsx1Farendcurrententry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry', 
                [], [], 
                '''                An entry in the DS1 Far End Current table.
                ''',
                'dsx1farendcurrententry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FarEndCurrentTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry',
            False, 
            [
            _MetaInfoClassMember('dsx1FarEndIntervalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS1
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is identical to the interface identified by
                the same value of dsx1LineIndex.
                ''',
                'dsx1farendintervalindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1FarEndIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, where 1 is the most
                recently completed 15 minute interval and 96 is
                the 15 minutes interval completed 23 hours and 45
                minutes prior to interval 1.
                ''',
                'dsx1farendintervalnumber',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1FarEndIntervalBESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Bursty Errored Seconds.
                ''',
                'dsx1farendintervalbess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalCSSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Controlled Slip Seconds.
                ''',
                'dsx1farendintervalcsss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalDMs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Degraded Minutes.
                ''',
                'dsx1farendintervaldms',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Errored Seconds.
                ''',
                'dsx1farendintervaless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Line Errored Seconds.
                ''',
                'dsx1farendintervalless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Path Coding Violations.
                ''',
                'dsx1farendintervalpcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Severely Errored Framing
                Seconds.
                ''',
                'dsx1farendintervalsefss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Severely Errored Seconds.
                ''',
                'dsx1farendintervalsess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Unavailable Seconds.
                ''',
                'dsx1farendintervaluass',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'dsx1farendintervalvaliddata',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FarEndIntervalEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Farendintervaltable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Farendintervaltable',
            False, 
            [
            _MetaInfoClassMember('dsx1FarEndIntervalEntry', REFERENCE_LIST, 'Dsx1Farendintervalentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry', 
                [], [], 
                '''                An entry in the DS1 Far End Interval table.
                ''',
                'dsx1farendintervalentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FarEndIntervalTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry',
            False, 
            [
            _MetaInfoClassMember('dsx1FarEndTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS1
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is identical to the interface identified by
                the same value of dsx1LineIndex.
                ''',
                'dsx1farendtotalindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1FarEndTotalBESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Bursty Errored Seconds (BESs)
                encountered by a DS1 interface in the previous 24
                hour interval. Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1farendtotalbess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalCSSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Controlled Slip Seconds
                encountered by a DS1 interface in the previous 24
                hour interval.  Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1farendtotalcsss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalDMs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Degraded Minutes (DMs) encountered
                by a DS1 interface in the previous 24 hour
                interval.  Invalid 15 minute intervals count as
                0.
                ''',
                'dsx1farendtotaldms',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Errored Seconds encountered
                by a DS1 interface in the previous 24 hour
                interval.  Invalid 15 minute intervals count as
                0.
                ''',
                'dsx1farendtotaless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Line Errored Seconds
                encountered by a DS1 interface in the previous 24
                hour interval.  Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1farendtotalless',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Path Coding Violations
                reported via the far end block error count
                encountered by a DS1 interface in the previous 24
                hour interval.  Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1farendtotalpcvs',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Severely Errored Framing
                Seconds encountered by a DS1 interface in the
                previous 24 hour interval. Invalid 15 minute
                intervals count as 0.
                ''',
                'dsx1farendtotalsefss',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Far End Severely Errored Seconds
                encountered by a DS1 interface in the previous 24
                hour interval.  Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx1farendtotalsess',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Unavailable Seconds encountered by
                a DS1 interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx1farendtotaluass',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FarEndTotalEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Farendtotaltable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Farendtotaltable',
            False, 
            [
            _MetaInfoClassMember('dsx1FarEndTotalEntry', REFERENCE_LIST, 'Dsx1Farendtotalentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry', 
                [], [], 
                '''                An entry in the DS1 Far End Total table.
                ''',
                'dsx1farendtotalentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FarEndTotalTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Fractable.Dsx1Fracentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Fractable.Dsx1Fracentry',
            False, 
            [
            _MetaInfoClassMember('dsx1FracIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies  the
                DS1  interface  to which this entry is applicable
                The interface identified by a  particular
                value  of  this  index is the same interface as
                identified by the same value  an  dsx1LineIndex
                object instance.
                ''',
                'dsx1fracindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1FracNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                The channel number for this entry.
                ''',
                'dsx1fracnumber',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1FracIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index value that uniquely identifies an
                interface.  The interface identified by a particular
                value of this index is the same  interface
                as  identified by the same value an ifIndex
                object instance. If no interface is currently using
                a channel, the value should be zero.  If a
                single interface occupies more  than  one  time
                slot,  that ifIndex value will be found in multiple
                time slots.
                ''',
                'dsx1fracifindex',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FracEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Fractable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Fractable',
            False, 
            [
            _MetaInfoClassMember('dsx1FracEntry', REFERENCE_LIST, 'Dsx1Fracentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Fractable.Dsx1Fracentry', 
                [], [], 
                '''                An entry in the DS1 Fractional table.
                ''',
                'dsx1fracentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1FracTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1Ds1ChannelNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '28')], [], 
                '''                ''',
                'dsx1ds1channelnumber',
                'DS1-MIB', True),
            _MetaInfoClassMember('dsx1ChanMappedIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object indicates the ifIndex value assigned
                by the agent for the individual ds1 ifEntry that
                corresponds to the given DS1 channel number
                (specified by the INDEX element
                dsx1Ds1ChannelNumber) of the given channelized
                interface (specified by INDEX element ifIndex).
                ''',
                'dsx1chanmappedifindex',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1ChanMappingEntry',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib.Dsx1Chanmappingtable' : {
        'meta_info' : _MetaInfoClass('Ds1Mib.Dsx1Chanmappingtable',
            False, 
            [
            _MetaInfoClassMember('dsx1ChanMappingEntry', REFERENCE_LIST, 'Dsx1Chanmappingentry' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry', 
                [], [], 
                '''                An entry in the DS1 Channel Mapping table.  There
                is an entry in this table corresponding to each
                ds1 ifEntry within any interface that is
                channelized to the individual ds1 ifEntry level.
                
                This table is intended to facilitate mapping from
                channelized interface / channel number to DS1
                ifEntry.  (e.g. mapping (DS3 ifIndex, DS1 Channel
                Number) -> ifIndex)
                
                While this table provides information that can
                also be found in the ifStackTable and
                dsx1ConfigTable, it provides this same information
                with a single table lookup, rather than by walking
                the ifStackTable to find the various constituent
                ds1 ifTable entries, and testing various
                dsx1ConfigTable entries to check for the entry
                with the applicable DS1 channel number.
                ''',
                'dsx1chanmappingentry',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'dsx1ChanMappingTable',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
    'Ds1Mib' : {
        'meta_info' : _MetaInfoClass('Ds1Mib',
            False, 
            [
            _MetaInfoClassMember('dsx1ChanMappingTable', REFERENCE_CLASS, 'Dsx1Chanmappingtable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Chanmappingtable', 
                [], [], 
                '''                The DS1 Channel Mapping table.  This table maps a
                DS1 channel number on a particular DS3 into an
                ifIndex.  In the presence of DS2s, this table can
                be used to map a DS2 channel number on a DS3 into
                an ifIndex, or used to map a DS1 channel number on
                a DS2 onto an ifIndex.
                ''',
                'dsx1chanmappingtable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1ConfigTable', REFERENCE_CLASS, 'Dsx1Configtable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Configtable', 
                [], [], 
                '''                The DS1 Configuration table.
                ''',
                'dsx1configtable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1CurrentTable', REFERENCE_CLASS, 'Dsx1Currenttable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Currenttable', 
                [], [], 
                '''                The DS1 current table contains various statistics
                being collected for the current 15 minute
                interval.
                ''',
                'dsx1currenttable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndCurrentTable', REFERENCE_CLASS, 'Dsx1Farendcurrenttable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Farendcurrenttable', 
                [], [], 
                '''                The DS1 Far End Current table contains various
                statistics being collected for the current 15
                minute interval.  The statistics are collected
                from the far end messages on the Facilities Data
                Link.  The definitions are the same as described
                for the near-end information.
                ''',
                'dsx1farendcurrenttable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndIntervalTable', REFERENCE_CLASS, 'Dsx1Farendintervaltable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Farendintervaltable', 
                [], [], 
                '''                The DS1 Far End Interval Table contains various
                statistics collected by each DS1 interface over
                the previous 24 hours of operation.  The past 24
                hours are broken into 96 completed 15 minute
                intervals. Each row in this table represents one
                such interval (identified by
                dsx1FarEndIntervalNumber) for one specific
                instance (identified by dsx1FarEndIntervalIndex).
                ''',
                'dsx1farendintervaltable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FarEndTotalTable', REFERENCE_CLASS, 'Dsx1Farendtotaltable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Farendtotaltable', 
                [], [], 
                '''                The DS1 Far End Total Table contains the
                cumulative sum of the various statistics for the
                24 hour period preceding the current interval.
                ''',
                'dsx1farendtotaltable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1FracTable', REFERENCE_CLASS, 'Dsx1Fractable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Fractable', 
                [], [], 
                '''                This table is deprecated in favour of using
                ifStackTable.
                
                The table was mandatory for systems dividing a DS1
                into channels containing different data streams
                that are of local interest.  Systems which are
                indifferent to data content, such as CSUs, need
                not implement it.
                
                The DS1 fractional table identifies which DS1
                channels associated with a CSU are being used to
                support a logical interface, i.e., an entry in the
                interfaces table from the Internet-standard MIB.
                
                For example, consider an application managing a
                North American ISDN Primary Rate link whose
                division is a 384 kbit/s H1 _B_ Channel for Video,
                a second H1 for data to a primary routing peer,
                and 12 64 kbit/s H0 _B_ Channels. Consider that
                some subset of the H0 channels are used for voice
                and the remainder are available for dynamic data
                calls.
                
                We count a total of 14 interfaces multiplexed onto
                the DS1 interface. Six DS1 channels (for the sake
                of the example, channels 1..6) are used for Video,
                six more (7..11 and 13) are used for data, and the
                remaining 12 are are in channels 12 and 14..24.
                
                Let us further imagine that ifIndex 2 is of type
                DS1 and refers to the DS1 interface, and that the
                interfaces layered onto it are numbered 3..16.
                
                We might describe the allocation of channels, in
                the dsx1FracTable, as follows:
                dsx1FracIfIndex.2. 1 = 3  dsx1FracIfIndex.2.13 = 4
                dsx1FracIfIndex.2. 2 = 3  dsx1FracIfIndex.2.14 = 6
                dsx1FracIfIndex.2. 3 = 3  dsx1FracIfIndex.2.15 = 7
                dsx1FracIfIndex.2. 4 = 3  dsx1FracIfIndex.2.16 = 8
                dsx1FracIfIndex.2. 5 = 3  dsx1FracIfIndex.2.17 = 9
                dsx1FracIfIndex.2. 6 = 3  dsx1FracIfIndex.2.18 = 10
                dsx1FracIfIndex.2. 7 = 4  dsx1FracIfIndex.2.19 = 11
                dsx1FracIfIndex.2. 8 = 4  dsx1FracIfIndex.2.20 = 12
                dsx1FracIfIndex.2. 9 = 4  dsx1FracIfIndex.2.21 = 13
                dsx1FracIfIndex.2.10 = 4  dsx1FracIfIndex.2.22 = 14
                dsx1FracIfIndex.2.11 = 4  dsx1FracIfIndex.2.23 = 15
                dsx1FracIfIndex.2.12 = 5  dsx1FracIfIndex.2.24 = 16
                
                For North American (DS1) interfaces, there are 24
                legal channels, numbered 1 through 24.
                
                For G.704 interfaces, there are 31 legal channels,
                numbered 1 through 31.  The channels (1..31)
                correspond directly to the equivalently numbered
                time-slots.
                ''',
                'dsx1fractable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1IntervalTable', REFERENCE_CLASS, 'Dsx1Intervaltable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Intervaltable', 
                [], [], 
                '''                The DS1 Interval Table contains various
                statistics collected by each DS1 Interface over
                the previous 24 hours of operation.  The past 24
                hours are broken into 96 completed 15 minute
                intervals.  Each row in this table represents one
                such interval (identified by dsx1IntervalNumber)
                for one specific instance (identified by
                dsx1IntervalIndex).
                ''',
                'dsx1intervaltable',
                'DS1-MIB', False),
            _MetaInfoClassMember('dsx1TotalTable', REFERENCE_CLASS, 'Dsx1Totaltable' , 'ydk.models.cisco_ios_xe.DS1_MIB', 'Ds1Mib.Dsx1Totaltable', 
                [], [], 
                '''                The DS1 Total Table contains the cumulative sum
                of the various statistics for the 24 hour period
                preceding the current interval.
                ''',
                'dsx1totaltable',
                'DS1-MIB', False),
            ],
            'DS1-MIB',
            'DS1-MIB',
            _yang_ns._namespaces['DS1-MIB'],
        'ydk.models.cisco_ios_xe.DS1_MIB'
        ),
    },
}
_meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Configtable']['meta_info']
_meta_table['Ds1Mib.Dsx1Currenttable.Dsx1Currententry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Currenttable']['meta_info']
_meta_table['Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Intervaltable']['meta_info']
_meta_table['Ds1Mib.Dsx1Totaltable.Dsx1Totalentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Totaltable']['meta_info']
_meta_table['Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Farendcurrenttable']['meta_info']
_meta_table['Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Farendintervaltable']['meta_info']
_meta_table['Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Farendtotaltable']['meta_info']
_meta_table['Ds1Mib.Dsx1Fractable.Dsx1Fracentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Fractable']['meta_info']
_meta_table['Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry']['meta_info'].parent =_meta_table['Ds1Mib.Dsx1Chanmappingtable']['meta_info']
_meta_table['Ds1Mib.Dsx1Configtable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Currenttable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Intervaltable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Totaltable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Farendcurrenttable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Farendintervaltable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Farendtotaltable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Fractable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
_meta_table['Ds1Mib.Dsx1Chanmappingtable']['meta_info'].parent =_meta_table['Ds1Mib']['meta_info']
