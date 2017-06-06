


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3ChannelizationEnum' : _MetaInfoEnum('Dsx3ChannelizationEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'disabled':'disabled',
            'enabledDs1':'enabledDs1',
            'enabledDs2':'enabledDs2',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinecodingEnum' : _MetaInfoEnum('Dsx3LinecodingEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'dsx3Other':'dsx3Other',
            'dsx3B3ZS':'dsx3B3ZS',
            'e3HDB3':'e3HDB3',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinestatuschangetrapenableEnum' : _MetaInfoEnum('Dsx3LinestatuschangetrapenableEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinetypeEnum' : _MetaInfoEnum('Dsx3LinetypeEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'dsx3other':'dsx3other',
            'dsx3M23':'dsx3M23',
            'dsx3SYNTRAN':'dsx3SYNTRAN',
            'dsx3CbitParity':'dsx3CbitParity',
            'dsx3ClearChannel':'dsx3ClearChannel',
            'e3other':'e3other',
            'e3Framed':'e3Framed',
            'e3Plcp':'e3Plcp',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LoopbackconfigEnum' : _MetaInfoEnum('Dsx3LoopbackconfigEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'dsx3NoLoop':'dsx3NoLoop',
            'dsx3PayloadLoop':'dsx3PayloadLoop',
            'dsx3LineLoop':'dsx3LineLoop',
            'dsx3OtherLoop':'dsx3OtherLoop',
            'dsx3InwardLoop':'dsx3InwardLoop',
            'dsx3DualLoop':'dsx3DualLoop',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3SendcodeEnum' : _MetaInfoEnum('Dsx3SendcodeEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'dsx3SendNoCode':'dsx3SendNoCode',
            'dsx3SendLineCode':'dsx3SendLineCode',
            'dsx3SendPayloadCode':'dsx3SendPayloadCode',
            'dsx3SendResetCode':'dsx3SendResetCode',
            'dsx3SendDS1LoopCode':'dsx3SendDS1LoopCode',
            'dsx3SendTestPattern':'dsx3SendTestPattern',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3TransmitclocksourceEnum' : _MetaInfoEnum('Dsx3TransmitclocksourceEnum', 'ydk.models.cisco_ios_xe.DS3_MIB',
        {
            'loopTiming':'loopTiming',
            'localTiming':'localTiming',
            'throughTiming':'throughTiming',
        }, 'DS3-MIB', _yang_ns._namespaces['DS3-MIB']),
    'Ds3Mib.Dsx3Configtable.Dsx3Configentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Configtable.Dsx3Configentry',
            False, 
            [
            _MetaInfoClassMember('dsx3LineIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object should be made equal to ifIndex.  The
                next paragraph describes its previous usage.
                Making the object equal to ifIndex allows propoer
                use of ifStackTable.
                
                Previously, this object was the identifier of a
                DS3/E3 Interface on a managed device.  If there is
                an ifEntry that is directly associated with this
                and only this DS3/E3 interface, it should have the
                same value as ifIndex.  Otherwise, number the
                dsx3LineIndices with an unique identifier
                following the rules of choosing a number that is
                greater than ifNumber and numbering the inside
                interfaces (e.g., equipment side) with even
                numbers and outside interfaces (e.g, network side)
                with odd numbers.
                ''',
                'dsx3lineindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3Channelization', REFERENCE_ENUM_CLASS, 'Dsx3ChannelizationEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3ChannelizationEnum', 
                [], [], 
                '''                Indicates whether this ds3/e3 is channelized or
                unchannelized.  The value of enabledDs1 indicates
                that this is a DS3 channelized into DS1s.  The
                value of enabledDs3 indicated that this is a DS3
                channelized into DS2s.  Setting this object will
                cause the creation or deletion of DS2 or DS1
                entries in the ifTable.  
                ''',
                'dsx3channelization',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CircuitIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This variable contains the transmission vendor's
                circuit identifier, for the purpose of
                facilitating troubleshooting.
                ''',
                'dsx3circuitidentifier',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3Ds1ForRemoteLoop', ATTRIBUTE, 'int' , None, None, 
                [('0', '29')], [], 
                '''                Indicates which ds1/e1 on this ds3/e3 will be
                indicated in the remote ds1 loopback request.  A
                value of 0 means no DS1 will be looped.  A value
                of 29 means all ds1s/e1s will be looped.
                ''',
                'dsx3ds1forremoteloop',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This value for this object is equal to the value
                of ifIndex from the Interfaces table of MIB II
                (RFC 1213).
                ''',
                'dsx3ifindex',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3InvalidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of intervals in the range from 0 to
                dsx3ValidIntervals for which no data is
                available.  This object will typically be zero
                except in cases where the data for some intervals
                are not available (e.g., in proxy situations).
                ''',
                'dsx3invalidintervals',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LineCoding', REFERENCE_ENUM_CLASS, 'Dsx3LinecodingEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinecodingEnum', 
                [], [], 
                '''                This variable describes the variety of Zero Code
                Suppression used on this interface, which in turn
                affects a number of its characteristics.
                
                dsx3B3ZS and e3HDB3 refer to the use of specified
                patterns of normal bits and bipolar violations
                which are used to replace sequences of zero bits
                of a specified length.
                ''',
                'dsx3linecoding',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LineLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '64000')], [], 
                '''                The length of the ds3 line in meters.  This
                object provides information for line build out
                circuitry if it exists and can use this object to
                adjust the line build out.
                ''',
                'dsx3linelength',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LineStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                This variable indicates the Line Status of the
                interface.  It contains loopback state information
                and failure state information.  The dsx3LineStatus
                is a bit map represented as a sum, therefore, it
                can represent multiple failures and a loopback
                (see dsx3LoopbackConfig object for the type of
                loopback) simultaneously.  The dsx3NoAlarm must be
                set if and only if no other flag is set.
                
                If the dsx3loopbackState bit is set, the loopback
                in effect can be determined from the
                dsx3loopbackConfig object.
                The various bit positions are:
                1     dsx3NoAlarm         No alarm present
                2     dsx3RcvRAIFailure   Receiving Yellow/Remote
                                 Alarm Indication
                4     dsx3XmitRAIAlarm    Transmitting Yellow/Remote
                                 Alarm Indication
                8     dsx3RcvAIS          Receiving AIS failure state
                16     dsx3XmitAIS         Transmitting AIS
                32     dsx3LOF             Receiving LOF failure state
                64     dsx3LOS             Receiving LOS failure state
                128     dsx3LoopbackState   Looping the received signal
                256     dsx3RcvTestCode     Receiving a Test Pattern
                512     dsx3OtherFailure    any line status not defined
                                 here
                1024     dsx3UnavailSigState Near End in Unavailable Signal
                                 State
                2048     dsx3NetEquipOOS     Carrier Equipment Out of Service
                ''',
                'dsx3linestatus',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LineStatusChangeTrapEnable', REFERENCE_ENUM_CLASS, 'Dsx3LinestatuschangetrapenableEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinestatuschangetrapenableEnum', 
                [], [], 
                '''                Indicates whether dsx3LineStatusChange traps
                should be generated for this interface.
                ''',
                'dsx3linestatuschangetrapenable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LineStatusLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of MIB II's sysUpTime object at the
                time this DS3/E3 entered its current line status
                state.  If the current state was entered prior to
                the last re-initialization of the proxy-agent,
                then this object contains a zero value.
                ''',
                'dsx3linestatuslastchange',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LineType', REFERENCE_ENUM_CLASS, 'Dsx3LinetypeEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinetypeEnum', 
                [], [], 
                '''                This variable indicates the variety of DS3 C-bit
                or E3 application implementing this interface. The
                type of interface affects the interpretation of
                the usage and error statistics.  The rate of DS3
                is 44.736 Mbps and E3 is 34.368 Mbps.  The
                dsx3ClearChannel value means that the C-bits are
                not used except for sending/receiving AIS.
                The values, in sequence, describe:
                
                TITLE:            SPECIFICATION:
                dsx3M23            ANSI T1.107-1988 [9]
                dsx3SYNTRAN        ANSI T1.107-1988 [9]
                dsx3CbitParity     ANSI T1.107a-1990 [9a]
                dsx3ClearChannel   ANSI T1.102-1987 [8]
                e3Framed           CCITT G.751 [12]
                e3Plcp             ETSI T/NA(91)18 [13].
                ''',
                'dsx3linetype',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LoopbackConfig', REFERENCE_ENUM_CLASS, 'Dsx3LoopbackconfigEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LoopbackconfigEnum', 
                [], [], 
                '''                This variable represents the desired loopback
                configuration of the DS3/E3 interface.
                
                The values mean:
                
                dsx3NoLoop
                  Not in the loopback state.  A device that is
                  not capable of performing a loopback on
                  the interface shall always return this as
                  its value.
                
                dsx3PayloadLoop
                  The received signal at this interface is looped
                  through the device.  Typically the received signal
                  is looped back for retransmission after it has
                  passed through the device's framing function.
                
                dsx3LineLoop
                  The received signal at this interface does not
                  go through the device (minimum penetration) but
                  is looped back out.
                
                dsx3OtherLoop
                  Loopbacks that are not defined here.
                
                dsx3InwardLoop
                  The sent signal at this interface is looped back
                  through the device.
                
                dsx3DualLoop
                  Both dsx1LineLoop and dsx1InwardLoop will be
                  active simultaneously.
                ''',
                'dsx3loopbackconfig',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3LoopbackStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '127')], [], 
                '''                This variable represents the current state of the
                loopback on the DS3 interface.  It contains
                information about loopbacks established by a
                manager and remotely from the far end.
                
                The dsx3LoopbackStatus is a bit map represented as
                a sum, therefore is can represent multiple
                loopbacks simultaneously.
                
                The various bit positions are:
                 1  dsx3NoLoopback
                 2  dsx3NearEndPayloadLoopback
                 4  dsx3NearEndLineLoopback
                 8  dsx3NearEndOtherLoopback
                16  dsx3NearEndInwardLoopback
                32  dsx3FarEndPayloadLoopback
                64  dsx3FarEndLineLoopback
                ''',
                'dsx3loopbackstatus',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3SendCode', REFERENCE_ENUM_CLASS, 'Dsx3SendcodeEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3SendcodeEnum', 
                [], [], 
                '''                This variable indicates what type of code is
                being sent across the DS3/E3 interface by the
                device.  (These are optional for E3 interfaces.)
                Setting this variable causes the interface to
                begin sending the code requested.
                The values mean:
                
                   dsx3SendNoCode
                       sending looped or normal data
                
                   dsx3SendLineCode
                       sending a request for a line loopback
                
                   dsx3SendPayloadCode
                       sending a request for a payload loopback
                       (i.e., all DS1/E1s in a DS3/E3 frame)
                
                   dsx3SendResetCode
                       sending a loopback deactivation request
                
                   dsx3SendDS1LoopCode
                       requesting to loopback a particular DS1/E1
                       within a DS3/E3 frame.  The DS1/E1 is
                       indicated in dsx3Ds1ForRemoteLoop.
                
                   dsx3SendTestPattern
                       sending a test pattern.
                ''',
                'dsx3sendcode',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '899')], [], 
                '''                The number of seconds that have elapsed since the
                beginning of the near end current error-
                measurement period.  If, for some reason, such as
                an adjustment in the system's time-of-day clock,
                the current interval exceeds the maximum value,
                the agent will return the maximum value.
                ''',
                'dsx3timeelapsed',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TransmitClockSource', REFERENCE_ENUM_CLASS, 'Dsx3TransmitclocksourceEnum' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3TransmitclocksourceEnum', 
                [], [], 
                '''                The source of Transmit Clock.
                
                loopTiming indicates that the recovered receive clock
                is used as the transmit clock.
                
                localTiming indicates that a local clock source is used
                or that an external clock is attached to the box
                containing the interface.
                
                throughTiming indicates that transmit clock is derived
                from the recovered receive clock of another DS3
                interface.
                ''',
                'dsx3transmitclocksource',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3ValidIntervals', ATTRIBUTE, 'int' , None, None, 
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
                'dsx3validintervals',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3ConfigEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Configtable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Configtable',
            False, 
            [
            _MetaInfoClassMember('dsx3ConfigEntry', REFERENCE_LIST, 'Dsx3Configentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable.Dsx3Configentry', 
                [], [], 
                '''                An entry in the DS3/E3 Configuration table.
                ''',
                'dsx3configentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3ConfigTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Currenttable.Dsx3Currententry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Currenttable.Dsx3Currententry',
            False, 
            [
            _MetaInfoClassMember('dsx3CurrentIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the
                DS3/E3 interface to which this entry is
                applicable.  The interface identified by a
                particular value of this index is the same
                interface as identified by the same value an
                dsx3LineIndex object instance.
                ''',
                'dsx3currentindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3CurrentCCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Coding Violations.
                ''',
                'dsx3currentccvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentCESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Errored Seconds.
                ''',
                'dsx3currentcess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentCSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Severely Errored Seconds.
                ''',
                'dsx3currentcsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentLCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Line
                Coding Violations.
                ''',
                'dsx3currentlcvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Errored Seconds.
                ''',
                'dsx3currentless',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Coding Violations.
                ''',
                'dsx3currentpcvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentPESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Errored Seconds.
                ''',
                'dsx3currentpess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentPSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Severely Errored Seconds.
                ''',
                'dsx3currentpsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Framing Seconds.
                ''',
                'dsx3currentsefss',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds.
                ''',
                'dsx3currentuass',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3CurrentEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Currenttable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Currenttable',
            False, 
            [
            _MetaInfoClassMember('dsx3CurrentEntry', REFERENCE_LIST, 'Dsx3Currententry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Currenttable.Dsx3Currententry', 
                [], [], 
                '''                An entry in the DS3/E3 Current table.
                ''',
                'dsx3currententry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3CurrentTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry',
            False, 
            [
            _MetaInfoClassMember('dsx3IntervalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the
                DS3/E3 interface to which this entry is
                applicable.  The interface identified by a
                particular value of this index is the same
                interface as identified by the same value an
                dsx3LineIndex object instance.
                ''',
                'dsx3intervalindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3IntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, where 1 is the most
                recently completed 15 minute interval and 96 is
                the 15 minutes interval completed 23 hours and 45
                minutes prior to interval 1.
                ''',
                'dsx3intervalnumber',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3IntervalCCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Coding Violations.
                ''',
                'dsx3intervalccvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalCESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Errored Seconds.
                ''',
                'dsx3intervalcess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalCSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Severely Errored Seconds.
                ''',
                'dsx3intervalcsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalLCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Line
                Coding Violations.
                ''',
                'dsx3intervallcvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Errored  Seconds  (BPVs  or
                illegal  zero  sequences).
                ''',
                'dsx3intervalless',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Coding Violations.
                ''',
                'dsx3intervalpcvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalPESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Errored Seconds.
                ''',
                'dsx3intervalpess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalPSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Severely Errored Seconds.
                ''',
                'dsx3intervalpsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Framing Seconds.
                ''',
                'dsx3intervalsefss',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds.  This object may decrease if
                the occurance of unavailable seconds occurs across
                an inteval boundary.
                ''',
                'dsx3intervaluass',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'dsx3intervalvaliddata',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3IntervalEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Intervaltable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Intervaltable',
            False, 
            [
            _MetaInfoClassMember('dsx3IntervalEntry', REFERENCE_LIST, 'Dsx3Intervalentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry', 
                [], [], 
                '''                An entry in the DS3/E3 Interval table.
                ''',
                'dsx3intervalentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3IntervalTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Totaltable.Dsx3Totalentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Totaltable.Dsx3Totalentry',
            False, 
            [
            _MetaInfoClassMember('dsx3TotalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the
                DS3/E3 interface to which this entry is
                applicable.  The interface identified by a
                particular value of this index is the same
                interface as identified by the same value an
                dsx3LineIndex object instance.
                ''',
                'dsx3totalindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3TotalCCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Coding Violations encountered
                by a DS3 interface in the previous 24 hour
                interval. Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totalccvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalCESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Errored Seconds encountered
                by a DS3 interface in the previous 24 hour
                interval. Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totalcess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalCSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of C-bit Severely Errored Seconds
                encountered by a DS3 interface in the previous 24
                hour interval. Invalid 15 minute intervals count
                as 0.
                ''',
                'dsx3totalcsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalLCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Line
                Coding Violations encountered by a DS3/E3
                interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totallcvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalLESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Line Errored  Seconds  (BPVs  or
                illegal  zero  sequences) encountered by a DS3/E3
                interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totalless',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalPCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Coding Violations, encountered by a DS3 interface
                in the previous 24 hour interval. Invalid 15
                minute intervals count as 0.
                ''',
                'dsx3totalpcvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalPESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Errored Seconds, encountered by a DS3 interface in
                the previous 24 hour interval. Invalid 15 minute
                intervals count as 0.
                ''',
                'dsx3totalpess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalPSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of P-bit
                Severely Errored Seconds, encountered by a DS3
                interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totalpsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Framing Seconds, encountered by a
                DS3/E3 interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totalsefss',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds, encountered by a DS3
                interface in the previous 24 hour interval.
                
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3totaluass',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3TotalEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Totaltable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Totaltable',
            False, 
            [
            _MetaInfoClassMember('dsx3TotalEntry', REFERENCE_LIST, 'Dsx3Totalentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Totaltable.Dsx3Totalentry', 
                [], [], 
                '''                An entry in the DS3/E3 Total table.
                ''',
                'dsx3totalentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3TotalTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndLineIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS3
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is the same interface as identified by the
                same value an dsx3LineIndex object instance.
                ''',
                'dsx3farendlineindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FarEndEquipCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                This is the Far End Equipment Identification code
                that describes the specific piece of equipment.
                It is sent within the Path Identification
                Message.
                ''',
                'dsx3farendequipcode',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndFacilityIDCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 38)], [], 
                '''                This code identifies a specific Far End DS3 path.
                It is sent within the Path Identification
                Message.
                ''',
                'dsx3farendfacilityidcode',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndFrameIDCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                This is the Far End Frame Identification code
                that identifies where the equipment is located
                within a building at a given location.  It is sent
                within the Path Identification Message.
                ''',
                'dsx3farendframeidcode',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndLocationIDCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                This is the Far End Location Identification code
                that describes the specific location of the
                equipment.  It is sent within the Path
                Identification Message.
                ''',
                'dsx3farendlocationidcode',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndUnitCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                This is the Far End code that identifies the
                equipment location within a bay.  It is sent
                within the Path Identification Message.
                ''',
                'dsx3farendunitcode',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndConfigEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendconfigtable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendconfigtable',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndConfigEntry', REFERENCE_LIST, 'Dsx3Farendconfigentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry', 
                [], [], 
                '''                An entry in the DS3 Far End Configuration table.
                ''',
                'dsx3farendconfigentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndConfigTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndCurrentIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS3
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is identical to the interface identified by
                the same value of dsx3LineIndex.
                ''',
                'dsx3farendcurrentindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FarEndCurrentCCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Coding Violations reported via the far end
                block error count.
                ''',
                'dsx3farendcurrentccvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndCurrentCESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far Far
                End C-bit Errored Seconds.
                ''',
                'dsx3farendcurrentcess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndCurrentCSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Severely Errored Seconds.
                ''',
                'dsx3farendcurrentcsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                unavailable seconds.
                ''',
                'dsx3farendcurrentuass',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndInvalidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of intervals in the range from 0 to
                dsx3FarEndValidIntervals for which no data is
                available.  This object will typically be zero
                except in cases where the data for some intervals
                are not available (e.g., in proxy situations).
                ''',
                'dsx3farendinvalidintervals',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '899')], [], 
                '''                The number of seconds that have elapsed since the
                beginning of the far end current error-measurement
                period.  If, for some reason, such as an
                adjustment in the system's time-of-day clock, the
                current interval exceeds the maximum value, the
                agent will return the maximum value.
                ''',
                'dsx3farendtimeelapsed',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of previous far end intervals for
                which data was collected.  The value will be
                96 unless the interface was brought online within
                the last 24 hours, in which case the value will be
                the number of complete 15 minute far end intervals
                since the interface has been online.
                ''',
                'dsx3farendvalidintervals',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndCurrentEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendcurrenttable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendcurrenttable',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndCurrentEntry', REFERENCE_LIST, 'Dsx3Farendcurrententry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry', 
                [], [], 
                '''                An entry in the DS3 Far End Current table.
                ''',
                'dsx3farendcurrententry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndCurrentTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndIntervalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS3
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is identical to the interface identified by
                the same value of dsx3LineIndex.
                ''',
                'dsx3farendintervalindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FarEndIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, where 1 is the most
                recently completed 15 minute interval and 96 is
                the 15 minutes interval completed 23 hours and 45
                minutes prior to interval 1.
                ''',
                'dsx3farendintervalnumber',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FarEndIntervalCCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Coding Violations reported via the far end
                block error count.
                ''',
                'dsx3farendintervalccvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndIntervalCESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Errored Seconds encountered by a DS3
                interface in one of the previous 96, individual 15
                minute, intervals. In the case where the agent is
                a proxy and data is not available, return
                noSuchInstance.
                ''',
                'dsx3farendintervalcess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndIntervalCSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Severely Errored Seconds.
                ''',
                'dsx3farendintervalcsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                unavailable seconds.
                ''',
                'dsx3farendintervaluass',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'dsx3farendintervalvaliddata',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndIntervalEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendintervaltable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendintervaltable',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndIntervalEntry', REFERENCE_LIST, 'Dsx3Farendintervalentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry', 
                [], [], 
                '''                An entry in the DS3 Far End Interval table.
                ''',
                'dsx3farendintervalentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndIntervalTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the DS3
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is identical to the interface identified by
                the same value of dsx3LineIndex.
                ''',
                'dsx3farendtotalindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FarEndTotalCCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Coding Violations reported via the far end
                block error count encountered by a DS3 interface
                in the previous 24 hour interval. Invalid 15
                minute intervals count as 0.
                ''',
                'dsx3farendtotalccvs',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndTotalCESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Errored Seconds encountered by a DS3
                interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3farendtotalcess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndTotalCSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                C-bit Severely Errored Seconds encountered by a
                DS3 interface in the previous 24 hour interval.
                Invalid 15 minute intervals count as 0.
                ''',
                'dsx3farendtotalcsess',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndTotalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far End
                unavailable seconds encountered by a DS3 interface
                in the previous 24 hour interval.  Invalid 15
                minute intervals count as 0.
                ''',
                'dsx3farendtotaluass',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndTotalEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Farendtotaltable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Farendtotaltable',
            False, 
            [
            _MetaInfoClassMember('dsx3FarEndTotalEntry', REFERENCE_LIST, 'Dsx3Farendtotalentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry', 
                [], [], 
                '''                An entry in the DS3 Far End Total table.
                ''',
                'dsx3farendtotalentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FarEndTotalTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Fractable.Dsx3Fracentry' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Fractable.Dsx3Fracentry',
            False, 
            [
            _MetaInfoClassMember('dsx3FracIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies  the
                DS3  interface  to which this entry is applicable
                The interface identified by a  particular value
                of  this  index is the same interface as
                identified by the same value  an  dsx3LineIndex
                object instance.
                ''',
                'dsx3fracindex',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FracNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                The channel number for this entry.
                ''',
                'dsx3fracnumber',
                'DS3-MIB', True),
            _MetaInfoClassMember('dsx3FracIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index value that uniquely identifies an
                interface.  The interface identified by a
                particular value of this index is the same
                interface as  identified by the same value an
                ifIndex object instance. If no interface is
                currently using a channel, the value should be
                zero.  If a single interface occupies more  than
                one  time slot,  that ifIndex value will be found
                in multiple time slots.
                ''',
                'dsx3fracifindex',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FracEntry',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib.Dsx3Fractable' : {
        'meta_info' : _MetaInfoClass('Ds3Mib.Dsx3Fractable',
            False, 
            [
            _MetaInfoClassMember('dsx3FracEntry', REFERENCE_LIST, 'Dsx3Fracentry' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Fractable.Dsx3Fracentry', 
                [], [], 
                '''                An entry in the DS3 Fractional table.
                ''',
                'dsx3fracentry',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'dsx3FracTable',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
    'Ds3Mib' : {
        'meta_info' : _MetaInfoClass('Ds3Mib',
            False, 
            [
            _MetaInfoClassMember('dsx3ConfigTable', REFERENCE_CLASS, 'Dsx3Configtable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Configtable', 
                [], [], 
                '''                The DS3/E3 Configuration table.
                ''',
                'dsx3configtable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3CurrentTable', REFERENCE_CLASS, 'Dsx3Currenttable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Currenttable', 
                [], [], 
                '''                The DS3/E3 current table contains various
                statistics being collected for the current 15
                minute interval.
                ''',
                'dsx3currenttable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndConfigTable', REFERENCE_CLASS, 'Dsx3Farendconfigtable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendconfigtable', 
                [], [], 
                '''                The DS3 Far End Configuration Table contains
                configuration information reported in the C-bits
                from the remote end.
                ''',
                'dsx3farendconfigtable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndCurrentTable', REFERENCE_CLASS, 'Dsx3Farendcurrenttable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendcurrenttable', 
                [], [], 
                '''                The DS3 Far End Current table contains various
                statistics being collected for the current 15
                minute interval.  The statistics are collected
                from the far end block error code within the C-
                bits.
                ''',
                'dsx3farendcurrenttable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndIntervalTable', REFERENCE_CLASS, 'Dsx3Farendintervaltable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendintervaltable', 
                [], [], 
                '''                The DS3 Far End Interval Table contains various
                statistics collected by each DS3 interface over
                the previous 24 hours of operation.  The past 24
                hours are broken into 96 completed 15 minute
                intervals.
                ''',
                'dsx3farendintervaltable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FarEndTotalTable', REFERENCE_CLASS, 'Dsx3Farendtotaltable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Farendtotaltable', 
                [], [], 
                '''                The DS3 Far End Total Table contains the
                cumulative sum of the various statistics for the
                24 hour period preceding the current interval.
                ''',
                'dsx3farendtotaltable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3FracTable', REFERENCE_CLASS, 'Dsx3Fractable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Fractable', 
                [], [], 
                '''                This table is deprecated in favour of using
                ifStackTable.
                
                Implementation of this table was optional.  It was
                designed for those systems dividing a DS3/E3 into
                channels containing different data streams that
                are of local interest.
                
                The DS3/E3 fractional table identifies which
                DS3/E3 channels associated with a CSU are being
                used to support a logical interface, i.e., an
                entry in the interfaces table from the Internet-
                standard MIB.
                
                For example, consider a DS3 device with 4 high
                speed links carrying router traffic, a feed for
                voice, a feed for video, and a synchronous channel
                for a non-routed protocol.  We might describe the
                allocation of channels, in the dsx3FracTable, as
                follows:
                dsx3FracIfIndex.2. 1 = 3  dsx3FracIfIndex.2.15 = 4
                dsx3FracIfIndex.2. 2 = 3  dsx3FracIfIndex.2.16 = 6
                dsx3FracIfIndex.2. 3 = 3  dsx3FracIfIndex.2.17 = 6
                dsx3FracIfIndex.2. 4 = 3  dsx3FracIfIndex.2.18 = 6
                dsx3FracIfIndex.2. 5 = 3  dsx3FracIfIndex.2.19 = 6
                dsx3FracIfIndex.2. 6 = 3  dsx3FracIfIndex.2.20 = 6
                dsx3FracIfIndex.2. 7 = 4  dsx3FracIfIndex.2.21 = 6
                dsx3FracIfIndex.2. 8 = 4  dsx3FracIfIndex.2.22 = 6
                dsx3FracIfIndex.2. 9 = 4  dsx3FracIfIndex.2.23 = 6
                dsx3FracIfIndex.2.10 = 4  dsx3FracIfIndex.2.24 = 6
                dsx3FracIfIndex.2.11 = 4  dsx3FracIfIndex.2.25 = 6
                dsx3FracIfIndex.2.12 = 5  dsx3FracIfIndex.2.26 = 6
                dsx3FracIfIndex.2.13 = 5  dsx3FracIfIndex.2.27 = 6
                dsx3FracIfIndex.2.14 = 5  dsx3FracIfIndex.2.28 = 6
                For dsx3M23, dsx3 SYNTRAN, dsx3CbitParity, and
                dsx3ClearChannel  there are 28 legal channels,
                numbered 1 throug h 28.
                
                For e3Framed there are 16 legal channels, numbered
                1 through 16.  The channels (1..16) correspond
                directly to the equivalently numbered time-slots.
                ''',
                'dsx3fractable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3IntervalTable', REFERENCE_CLASS, 'Dsx3Intervaltable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Intervaltable', 
                [], [], 
                '''                The DS3/E3 Interval Table contains various
                statistics collected by each DS3/E3 Interface over
                the previous 24 hours of operation.  The past 24
                hours are broken into 96 completed 15 minute
                intervals.  Each row in this table represents one
                such interval (identified by dsx3IntervalNumber)
                and for one specific interface (identifed by
                dsx3IntervalIndex).
                ''',
                'dsx3intervaltable',
                'DS3-MIB', False),
            _MetaInfoClassMember('dsx3TotalTable', REFERENCE_CLASS, 'Dsx3Totaltable' , 'ydk.models.cisco_ios_xe.DS3_MIB', 'Ds3Mib.Dsx3Totaltable', 
                [], [], 
                '''                The DS3/E3 Total Table contains the cumulative
                sum of the various statistics for the 24 hour
                period preceding the current interval.
                ''',
                'dsx3totaltable',
                'DS3-MIB', False),
            ],
            'DS3-MIB',
            'DS3-MIB',
            _yang_ns._namespaces['DS3-MIB'],
        'ydk.models.cisco_ios_xe.DS3_MIB'
        ),
    },
}
_meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Configtable']['meta_info']
_meta_table['Ds3Mib.Dsx3Currenttable.Dsx3Currententry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Currenttable']['meta_info']
_meta_table['Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Intervaltable']['meta_info']
_meta_table['Ds3Mib.Dsx3Totaltable.Dsx3Totalentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Totaltable']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Farendconfigtable']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Farendcurrenttable']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Farendintervaltable']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Farendtotaltable']['meta_info']
_meta_table['Ds3Mib.Dsx3Fractable.Dsx3Fracentry']['meta_info'].parent =_meta_table['Ds3Mib.Dsx3Fractable']['meta_info']
_meta_table['Ds3Mib.Dsx3Configtable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Currenttable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Intervaltable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Totaltable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendconfigtable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendcurrenttable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendintervaltable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Farendtotaltable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
_meta_table['Ds3Mib.Dsx3Fractable']['meta_info'].parent =_meta_table['Ds3Mib']['meta_info']
