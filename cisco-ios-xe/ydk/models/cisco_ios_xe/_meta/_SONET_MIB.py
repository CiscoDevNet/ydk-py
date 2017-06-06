


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SonetMib.Sonetmedium.SonetsesthresholdsetEnum' : _MetaInfoEnum('SonetsesthresholdsetEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'other':'other',
            'bellcore1991':'bellcore1991',
            'ansi1993':'ansi1993',
            'itu1995':'itu1995',
            'ansi1997':'ansi1997',
        }, 'SONET-MIB', _yang_ns._namespaces['SONET-MIB']),
    'SonetMib.Sonetmedium' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetmedium',
            False, 
            [
            _MetaInfoClassMember('sonetSESthresholdSet', REFERENCE_ENUM_CLASS, 'SonetsesthresholdsetEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmedium.SonetsesthresholdsetEnum', 
                [], [], 
                '''                An enumerated integer indicating which
                recognized set of SES thresholds that
                the agent uses for determining severely
                errored seconds and unavailable time.
                
                other(1)
                  None of the following.
                
                bellcore1991(2)
                  Bellcore TR-NWT-000253, 1991 [TR253], or
                  ANSI T1M1.3/93-005R2, 1993 [T1M1.3].
                  See also Appendix B.
                
                ansi1993(3)
                  ANSI T1.231, 1993 [T1.231a], or
                  Bellcore GR-253-CORE, Issue 2, 1995 [GR253]
                
                itu1995(4)
                  ITU Recommendation G.826, 1995 [G.826]
                
                ansi1997(5)
                  ANSI T1.231, 1997 [T1.231b]
                
                If a manager changes the value of this
                object then the SES statistics collected
                prior to this change must be invalidated.
                ''',
                'sonetsesthresholdset',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetMedium',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetmediumtable.Sonetmediumentry.SonetmediumlinecodingEnum' : _MetaInfoEnum('SonetmediumlinecodingEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'sonetMediumOther':'sonetMediumOther',
            'sonetMediumB3ZS':'sonetMediumB3ZS',
            'sonetMediumCMI':'sonetMediumCMI',
            'sonetMediumNRZ':'sonetMediumNRZ',
            'sonetMediumRZ':'sonetMediumRZ',
        }, 'SONET-MIB', _yang_ns._namespaces['SONET-MIB']),
    'SonetMib.Sonetmediumtable.Sonetmediumentry.SonetmediumlinetypeEnum' : _MetaInfoEnum('SonetmediumlinetypeEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'sonetOther':'sonetOther',
            'sonetShortSingleMode':'sonetShortSingleMode',
            'sonetLongSingleMode':'sonetLongSingleMode',
            'sonetMultiMode':'sonetMultiMode',
            'sonetCoax':'sonetCoax',
            'sonetUTP':'sonetUTP',
        }, 'SONET-MIB', _yang_ns._namespaces['SONET-MIB']),
    'SonetMib.Sonetmediumtable.Sonetmediumentry.SonetmediumtypeEnum' : _MetaInfoEnum('SonetmediumtypeEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'sonet':'sonet',
            'sdh':'sdh',
        }, 'SONET-MIB', _yang_ns._namespaces['SONET-MIB']),
    'SonetMib.Sonetmediumtable.Sonetmediumentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetmediumtable.Sonetmediumentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetMediumCircuitIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This variable contains the transmission
                vendor's circuit identifier, for the
                purpose of facilitating troubleshooting.
                Note that the circuit identifier, if available,
                is also represented by ifPhysAddress.
                ''',
                'sonetmediumcircuitidentifier',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumInvalidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of intervals in the range from
                0 to sonetMediumValidIntervals for which no
                data is available. This object will typically
                be zero except in cases where the data for some
                intervals are not available (e.g., in proxy
                situations).
                ''',
                'sonetmediuminvalidintervals',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumLineCoding', REFERENCE_ENUM_CLASS, 'SonetmediumlinecodingEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmediumtable.Sonetmediumentry.SonetmediumlinecodingEnum', 
                [], [], 
                '''                This variable describes the line coding for
                this interface. The B3ZS and CMI are used for
                electrical SONET/SDH signals (STS-1 and STS-3).
                The Non-Return to Zero (NRZ) and the Return
                to Zero are used for optical SONET/SDH signals.
                ''',
                'sonetmediumlinecoding',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumLineType', REFERENCE_ENUM_CLASS, 'SonetmediumlinetypeEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmediumtable.Sonetmediumentry.SonetmediumlinetypeEnum', 
                [], [], 
                '''                This variable describes the line type for
                this interface. The line types are
                Short and Long Range
                Single Mode fiber or Multi-Mode fiber interfaces,
                and coax and UTP for electrical interfaces.  The
                value sonetOther should be used when the Line Type is
                not one of the listed values.
                ''',
                'sonetmediumlinetype',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumLoopbackConfig', REFERENCE_BITS, 'Sonetmediumloopbackconfig' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmediumtable.Sonetmediumentry.Sonetmediumloopbackconfig', 
                [], [], 
                '''                The current loopback state of the SONET/SDH interface.  The
                values mean:
                
                  sonetNoLoop
                     Not in the loopback state. A device that is not
                     capable of performing a loopback on this interface
                     shall always return this value.
                
                  sonetFacilityLoop
                     The received signal at this interface is looped back
                     out through the corresponding transmitter in the return
                     direction.
                
                  sonetTerminalLoop
                     The signal that is about to be transmitted is connected
                     to the associated incoming receiver.
                
                  sonetOtherLoop
                     Loopbacks that are not defined here.
                ''',
                'sonetmediumloopbackconfig',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('1', '900')], [], 
                '''                The number of seconds, including partial seconds,
                that have elapsed since the beginning of the current
                measurement period. If, for some reason, such as an
                adjustment in the system's time-of-day clock, the
                current interval exceeds the maximum value, the
                agent will return the maximum value.
                ''',
                'sonetmediumtimeelapsed',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumType', REFERENCE_ENUM_CLASS, 'SonetmediumtypeEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmediumtable.Sonetmediumentry.SonetmediumtypeEnum', 
                [], [], 
                '''                This variable identifies whether a SONET
                or a SDH signal is used across this interface.
                ''',
                'sonetmediumtype',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of previous 15-minute intervals
                for which data was collected.
                A SONET/SDH interface must be capable
                of supporting at least n intervals.
                The minimum value of n is 4.
                The default of n is 32.
                The maximum value of n is 96.
                The value will be <n> unless the measurement was
                (re-)started within the last (<n>*15) minutes, in which
                case the value will be the number of complete 15
                minute intervals for which the agent has at least
                some data. In certain cases (e.g., in the case
                where the agent is a proxy) it is possible that some
                intervals are unavailable.  In this case, this
                interval is the maximum interval number for
                which data is available. 
                ''',
                'sonetmediumvalidintervals',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetMediumEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetmediumtable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetmediumtable',
            False, 
            [
            _MetaInfoClassMember('sonetMediumEntry', REFERENCE_LIST, 'Sonetmediumentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmediumtable.Sonetmediumentry', 
                [], [], 
                '''                An entry in the SONET/SDH Medium table.
                ''',
                'sonetmediumentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetMediumTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetSectionCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH Section in the current 15 minute interval.
                ''',
                'sonetsectioncurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Errored
                Seconds encountered by a SONET/SDH
                Section in the current 15 minute interval.
                ''',
                'sonetsectioncurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionCurrentSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Framing Seconds
                encountered by a SONET/SDH Section in the current
                15 minute interval.
                ''',
                'sonetsectioncurrentsefss',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH Section in the current 15
                minute interval.
                ''',
                'sonetsectioncurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionCurrentStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                This variable indicates the
                status of the interface.
                The sonetSectionCurrentStatus
                is a bit map represented
                as a sum, therefore,
                it can represent multiple defects
                simultaneously.
                The sonetSectionNoDefect should be
                set if and only if
                no other flag is set.
                
                The various bit positions are:
                      1   sonetSectionNoDefect
                      2   sonetSectionLOS
                      4   sonetSectionLOF
                ''',
                'sonetsectioncurrentstatus',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetSectionCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetsectioncurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetsectioncurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetSectionCurrentEntry', REFERENCE_LIST, 'Sonetsectioncurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH Section Current table.
                ''',
                'sonetsectioncurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetSectionCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetSectionIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetsectionintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetSectionIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH Section in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetsectionintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Errored Seconds encountered
                by a SONET/SDH Section in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetsectionintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionIntervalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Framing Seconds
                encountered by a SONET/SDH Section in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetsectionintervalsefss',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH Section in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetsectionintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetsectionintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetSectionIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetsectionintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetsectionintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetSectionIntervalEntry', REFERENCE_LIST, 'Sonetsectionintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH Section Interval table.
                ''',
                'sonetsectionintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetSectionIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetLineCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH Line in the current 15 minute interval.
                ''',
                'sonetlinecurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Errored
                Seconds encountered by a SONET/SDH
                Line in the current 15 minute interval.
                ''',
                'sonetlinecurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH Line in the current 15
                minute
                interval.
                ''',
                'sonetlinecurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineCurrentStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                This variable indicates the
                status of the interface.
                The sonetLineCurrentStatus
                is a bit map represented
                as a sum, therefore,
                it can represent multiple defects
                simultaneously.
                The sonetLineNoDefect should be
                set if and only if
                no other flag is set.
                
                The various bit positions are:
                 1   sonetLineNoDefect
                 2   sonetLineAIS
                 4   sonetLineRDI
                ''',
                'sonetlinecurrentstatus',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds
                encountered by a SONET/SDH Line in the current 15
                minute
                interval.
                ''',
                'sonetlinecurrentuass',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetLineCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetlinecurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetlinecurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetLineCurrentEntry', REFERENCE_LIST, 'Sonetlinecurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH Line Current table.
                ''',
                'sonetlinecurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetLineCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetlineintervaltable.Sonetlineintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetlineintervaltable.Sonetlineintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetLineIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetlineintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetLineIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH Line in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetlineintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Errored Seconds encountered
                by a SONET/SDH Line in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetlineintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH Line in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetlineintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the
                number of Unavailable Seconds
                encountered by a SONET/SDH Line in
                a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetlineintervaluass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetlineintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetLineIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetlineintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetlineintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetLineIntervalEntry', REFERENCE_LIST, 'Sonetlineintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetlineintervaltable.Sonetlineintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH Line Interval table.
                ''',
                'sonetlineintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetLineIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndLineCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Coding Violations reported via
                the far end block error count
                encountered by a
                SONET/SDH Medium/Section/Line
                interface in the current 15 minute interval.
                ''',
                'sonetfarendlinecurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far
                End Errored Seconds encountered by a SONET/SDH
                interface in the current 15 minute interval.
                ''',
                'sonetfarendlinecurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Severely Errored Seconds
                encountered by a SONET/SDH Medium/Section/Line
                interface in the current 15 minute
                interval.
                ''',
                'sonetfarendlinecurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Unavailable Seconds
                encountered by a
                SONET/SDH Medium/Section/Line
                interface in the current 15 minute interval.
                ''',
                'sonetfarendlinecurrentuass',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndLineCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendlinecurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendlinecurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndLineCurrentEntry', REFERENCE_LIST, 'Sonetfarendlinecurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH Far End Line Current table.
                ''',
                'sonetfarendlinecurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndLineCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndLineIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetfarendlineintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndLineIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Coding Violations reported via
                the far end block error count
                encountered by a
                SONET/SDH Line
                interface in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendlineintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Errored Seconds encountered
                by a SONET/SDH Line
                interface in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendlineintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Severely Errored Seconds
                encountered by a SONET/SDH Line
                interface in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendlineintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Unavailable Seconds
                encountered by a
                SONET/SDH Line
                interface in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendlineintervaluass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetfarendlineintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndLineIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendlineintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendlineintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndLineIntervalEntry', REFERENCE_LIST, 'Sonetfarendlineintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH Far
                End Line Interval table.
                ''',
                'sonetfarendlineintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndLineIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CspsignallingtransportmodeEnum' : _MetaInfoEnum('CspsignallingtransportmodeEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'notApplicable':'notApplicable',
            'signallingTransferMode':'signallingTransferMode',
            'clearMode':'clearMode',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CspsonetpathpayloadEnum' : _MetaInfoEnum('CspsonetpathpayloadEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'unequipped':'unequipped',
            'unspecified':'unspecified',
            'ds3':'ds3',
            'vt15vc11':'vt15vc11',
            'vt2vc12':'vt2vc12',
            'atmCell':'atmCell',
            'hdlcFr':'hdlcFr',
            'e3':'e3',
            'vtStructured':'vtStructured',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CsptributarygroupingtypeEnum' : _MetaInfoEnum('CsptributarygroupingtypeEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'notApplicable':'notApplicable',
            'au3Grouping':'au3Grouping',
            'au4Grouping':'au4Grouping',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CsptributarymappingtypeEnum' : _MetaInfoEnum('CsptributarymappingtypeEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'asynchronous':'asynchronous',
            'byteSynchronous':'byteSynchronous',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.SonetpathcurrentwidthEnum' : _MetaInfoEnum('SonetpathcurrentwidthEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'sts1':'sts1',
            'sts3cSTM1':'sts3cSTM1',
            'sts12cSTM4':'sts12cSTM4',
            'sts24c':'sts24c',
            'sts48cSTM16':'sts48cSTM16',
            'sts192cSTM64':'sts192cSTM64',
            'sts768cSTM256':'sts768cSTM256',
        }, 'SONET-MIB', _yang_ns._namespaces['SONET-MIB']),
    'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('cspSignallingTransportMode', REFERENCE_ENUM_CLASS, 'CspsignallingtransportmodeEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CspsignallingtransportmodeEnum', 
                [], [], 
                '''                This object represents the mode used to transport DS0 
                Signalling information for T1 byteSynchronous mapping
                (GR253).
                In signallingTransferMode(2), the robbed-bit signalling 
                is transferred to the VT header. In clearMode(3), only 
                the framing bit is transferred to the VT header.
                         
                The initial value is signallingTransferMode(2) 
                if csTributaryMappingType is byteSynchronous. 
                For asynchronous mapping, it is 
                notApplicable(1).
                
                The value notApplicable(1) can not be set.
                ''',
                'cspsignallingtransportmode',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspSonetPathPayload', REFERENCE_ENUM_CLASS, 'CspsonetpathpayloadEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CspsonetpathpayloadEnum', 
                [], [], 
                '''                Specifies the payload carried by the SONET/SDH Path.
                The payload specification corresponds to C2 (Signal Label)
                overhead byte in SONET/SDH Path Overhead:
                unequipped(1)    : Path is not provisioned to carry any payload.
                unspecified(2)   : Path is carrying an unspecifed payload.
                ds3(3)           : Path is carrying a DS3 path as payload.
                vt15vc11(4)      : Path is carrying SONET-VT1.5/SDH-VC11 payload.
                vt2vc12(5)       : Path is carrying SONET-VT2/SDH-VC12 as payload.
                atmCell(6)       : Path is carrying ATM Cells as payload.
                hdlcFr(7)        : Path is carrying Frame Relay (HDLC) payload.
                e3(8)            : Path is carrying an E3 path as payload.
                vtStructured(9)  : Path is carrying VTGs/TUG3s/TUG2s which may
                                   each carry a different payload. 
                A write operation on this object will result in update to
                C2 overhead byte in the Path Overhead.
                ''',
                'cspsonetpathpayload',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTributaryGroupingType', REFERENCE_ENUM_CLASS, 'CsptributarygroupingtypeEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CsptributarygroupingtypeEnum', 
                [], [], 
                '''                This object represents the method used to group VCs into
                an STM-1 signal. Applicable only to SDH.
                
                au3Grouping: STM1<-AU-3<-TUG-2<-TU-12<-VC12 or
                             STM1<-AU-3<-TUG-2<-TU-11<-VC11.
                
                au4Grouping: STM1<-AU-4<-TUG-3<-TUG-2<-TU-12<-VC12 or
                             STM1<-AU-4<-TUG-3<-TUG-2<-TU-11<-VC11.
                
                The initial value is au3Grouping(2) for SDH and 
                notApplicable(1) for SONET.
                ''',
                'csptributarygroupingtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTributaryMappingType', REFERENCE_ENUM_CLASS, 'CsptributarymappingtypeEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.CsptributarymappingtypeEnum', 
                [], [], 
                '''                This object represents the VT/VC mapping type.
                asynchronous: In this mode, the channel structure of 
                              DS1/E1 is neither visible nor preserved.
                
                byteSynchronous: In this mode, the DS0 signals inside 
                                 the VT/VC can be found and extracted 
                                 from the frame.
                The initial value is asynchronous(1).
                ''',
                'csptributarymappingtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH Path in the current 15 minute interval.
                ''',
                'sonetpathcurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Errored
                Seconds encountered by a SONET/SDH
                Path in the current 15 minute interval.
                ''',
                'sonetpathcurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH Path in the current 15
                minute
                interval.
                ''',
                'sonetpathcurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '62')], [], 
                '''                This variable indicates the
                status of the interface.
                The sonetPathCurrentStatus
                is a bit map represented
                as a sum, therefore,
                it can represent multiple defects
                simultaneously.
                The sonetPathNoDefect should be
                set if and only if
                no other flag is set.
                
                The various bit positions are:
                   1   sonetPathNoDefect
                   2   sonetPathSTSLOP
                   4   sonetPathSTSAIS
                   8   sonetPathSTSRDI
                  16   sonetPathUnequipped
                  32   sonetPathSignalLabelMismatch
                ''',
                'sonetpathcurrentstatus',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds
                encountered by a Path in the current
                15 minute interval.
                ''',
                'sonetpathcurrentuass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentWidth', REFERENCE_ENUM_CLASS, 'SonetpathcurrentwidthEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry.SonetpathcurrentwidthEnum', 
                [], [], 
                '''                A value that indicates the type of the SONET/SDH
                Path.  For SONET, the assigned types are
                the STS-Nc SPEs, where N = 1, 3, 12, 24, 48, 192 and 768.
                STS-1 is equal to 51.84 Mbps.  For SDH, the assigned
                types are the STM-Nc VCs, where N = 1, 4, 16, 64 and 256.
                ''',
                'sonetpathcurrentwidth',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetPathCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetpathcurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetpathcurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetPathCurrentEntry', REFERENCE_LIST, 'Sonetpathcurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH Path Current table.
                ''',
                'sonetpathcurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetPathCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetpathintervaltable.Sonetpathintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetpathintervaltable.Sonetpathintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetPathIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetpathintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetPathIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH Path in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetpathintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Errored Seconds encountered
                by a SONET/SDH Path in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetpathintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH Path in
                a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetpathintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds
                encountered by a Path in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetpathintervaluass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetpathintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetPathIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetpathintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetpathintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetPathIntervalEntry', REFERENCE_LIST, 'Sonetpathintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathintervaltable.Sonetpathintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH Path Interval table.
                ''',
                'sonetpathintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetPathIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndPathCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Coding Violations reported via
                the far end block error count
                encountered by a
                SONET/SDH Path interface in
                the current 15 minute interval.
                ''',
                'sonetfarendpathcurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far
                End Errored Seconds encountered by a SONET/SDH
                interface in the current 15 minute interval.
                ''',
                'sonetfarendpathcurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Severely Errored Seconds
                encountered by a SONET/SDH Path
                interface in the current 15 minute
                interval.
                ''',
                'sonetfarendpathcurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Unavailable Seconds
                encountered by a
                SONET/SDH Path interface in
                the current 15 minute interval.
                ''',
                'sonetfarendpathcurrentuass',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndPathCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendpathcurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendpathcurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndPathCurrentEntry', REFERENCE_LIST, 'Sonetfarendpathcurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH Far End Path Current table.
                ''',
                'sonetfarendpathcurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndPathCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndPathIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetfarendpathintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndPathIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Coding Violations reported via
                the far end block error count
                encountered by a
                SONET/SDH Path interface
                in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendpathintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Errored Seconds encountered
                by a SONET/SDH Path interface in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendpathintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Severely Errored Seconds
                encountered by a SONET/SDH Path interface
                in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendpathintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Unavailable Seconds
                encountered by a
                SONET/SDH Path interface in
                a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendpathintervaluass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetfarendpathintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndPathIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendpathintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendpathintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndPathIntervalEntry', REFERENCE_LIST, 'Sonetfarendpathintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH Far
                End Path Interval table.
                ''',
                'sonetfarendpathintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndPathIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry.SonetvtcurrentwidthEnum' : _MetaInfoEnum('SonetvtcurrentwidthEnum', 'ydk.models.cisco_ios_xe.SONET_MIB',
        {
            'vtWidth15VC11':'vtWidth15VC11',
            'vtWidth2VC12':'vtWidth2VC12',
            'vtWidth3':'vtWidth3',
            'vtWidth6VC2':'vtWidth6VC2',
            'vtWidth6c':'vtWidth6c',
        }, 'SONET-MIB', _yang_ns._namespaces['SONET-MIB']),
    'SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetVTCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH VT in the current 15 minute interval.
                ''',
                'sonetvtcurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Errored
                Seconds encountered by a SONET/SDH
                VT in the current 15 minute interval.
                ''',
                'sonetvtcurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH VT in the current 15 minute
                interval.
                ''',
                'sonetvtcurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTCurrentStatus', ATTRIBUTE, 'int' , None, None, 
                [('1', '126')], [], 
                '''                This variable indicates the
                status of the interface.
                The sonetVTCurrentStatus
                is a bit map represented
                as a sum, therefore,
                it can represent multiple defects
                and failures
                simultaneously.
                The sonetVTNoDefect should be
                set if and only if
                no other flag is set.
                
                The various bit positions are:
                   1   sonetVTNoDefect
                   2   sonetVTLOP
                   4   sonetVTPathAIS
                   8   sonetVTPathRDI
                  16   sonetVTPathRFI
                  32   sonetVTUnequipped
                  64   sonetVTSignalLabelMismatch
                ''',
                'sonetvtcurrentstatus',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds
                encountered by a VT in the current
                15 minute interval.
                ''',
                'sonetvtcurrentuass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTCurrentWidth', REFERENCE_ENUM_CLASS, 'SonetvtcurrentwidthEnum' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry.SonetvtcurrentwidthEnum', 
                [], [], 
                '''                A value that indicates the type of the SONET
                VT and SDH VC.  Assigned widths are
                VT1.5/VC11, VT2/VC12, VT3, VT6/VC2, and VT6c.
                ''',
                'sonetvtcurrentwidth',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetVTCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetvtcurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetvtcurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetVTCurrentEntry', REFERENCE_LIST, 'Sonetvtcurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH VT Current table.
                ''',
                'sonetvtcurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetVTCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetvtintervaltable.Sonetvtintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetvtintervaltable.Sonetvtintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetVTIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetvtintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetVTIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Coding
                Violations encountered by a
                SONET/SDH VT in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetvtintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Errored Seconds encountered
                by a SONET/SDH VT in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetvtintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Severely Errored Seconds
                encountered by a SONET/SDH VT
                in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetvtintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Unavailable Seconds
                encountered by a VT in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetvtintervaluass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetvtintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetVTIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetvtintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetvtintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetVTIntervalEntry', REFERENCE_LIST, 'Sonetvtintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetvtintervaltable.Sonetvtintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH VT Interval table.
                ''',
                'sonetvtintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetVTIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndVTCurrentCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Coding Violations reported via
                the far end block error count
                encountered by a
                SONET/SDH VT interface
                in the current 15 minute interval.
                ''',
                'sonetfarendvtcurrentcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTCurrentESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of Far
                End Errored Seconds encountered by a SONET/SDH
                interface in the current 15 minute interval.
                ''',
                'sonetfarendvtcurrentess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTCurrentSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Severely Errored Seconds
                encountered by a SONET/SDH VT interface
                in the current 15 minute
                interval.
                ''',
                'sonetfarendvtcurrentsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTCurrentUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Unavailable Seconds
                encountered by a
                SONET/SDH VT interface
                in the current 15 minute interval.
                ''',
                'sonetfarendvtcurrentuass',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndVTCurrentEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendvtcurrenttable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendvtcurrenttable',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndVTCurrentEntry', REFERENCE_LIST, 'Sonetfarendvtcurrententry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry', 
                [], [], 
                '''                An entry in the SONET/SDH Far End VT Current table.
                ''',
                'sonetfarendvtcurrententry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndVTCurrentTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndVTIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number between 1 and 96, which identifies the
                interval for which the set of statistics is available.
                The interval identified by 1 is the most recently
                completed 15 minute interval,
                and the interval identified
                by N is the interval immediately preceding the
                one identified
                by N-1.
                ''',
                'sonetfarendvtintervalnumber',
                'SONET-MIB', True),
            _MetaInfoClassMember('sonetFarEndVTIntervalCVs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Coding Violations reported via
                the far end block error count
                encountered by a
                SONET/SDH VT interface in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendvtintervalcvs',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTIntervalESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Errored Seconds encountered
                by a SONET/SDH VT interface
                in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendvtintervaless',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTIntervalSESs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Severely Errored Seconds
                encountered by a SONET/SDH VT interface
                in a particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendvtintervalsess',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTIntervalUASs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The counter associated with the number of
                Far End Unavailable Seconds
                encountered by a
                SONET/SDH VT interface in a
                particular 15-minute interval
                in the past 24 hours.
                ''',
                'sonetfarendvtintervaluass',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this
                interval is valid.
                ''',
                'sonetfarendvtintervalvaliddata',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndVTIntervalEntry',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib.Sonetfarendvtintervaltable' : {
        'meta_info' : _MetaInfoClass('SonetMib.Sonetfarendvtintervaltable',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndVTIntervalEntry', REFERENCE_LIST, 'Sonetfarendvtintervalentry' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry', 
                [], [], 
                '''                An entry in the SONET/SDH Far
                End VT Interval table.
                ''',
                'sonetfarendvtintervalentry',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'sonetFarEndVTIntervalTable',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
    'SonetMib' : {
        'meta_info' : _MetaInfoClass('SonetMib',
            False, 
            [
            _MetaInfoClassMember('sonetFarEndLineCurrentTable', REFERENCE_CLASS, 'Sonetfarendlinecurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendlinecurrenttable', 
                [], [], 
                '''                The SONET/SDH Far End Line Current table.
                ''',
                'sonetfarendlinecurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndLineIntervalTable', REFERENCE_CLASS, 'Sonetfarendlineintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendlineintervaltable', 
                [], [], 
                '''                The SONET/SDH Far End Line Interval table.
                ''',
                'sonetfarendlineintervaltable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathCurrentTable', REFERENCE_CLASS, 'Sonetfarendpathcurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendpathcurrenttable', 
                [], [], 
                '''                The SONET/SDH Far End Path Current table.
                ''',
                'sonetfarendpathcurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndPathIntervalTable', REFERENCE_CLASS, 'Sonetfarendpathintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendpathintervaltable', 
                [], [], 
                '''                The SONET/SDH Far End Path Interval table.
                ''',
                'sonetfarendpathintervaltable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTCurrentTable', REFERENCE_CLASS, 'Sonetfarendvtcurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendvtcurrenttable', 
                [], [], 
                '''                The SONET/SDH Far End VT Current table.
                ''',
                'sonetfarendvtcurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetFarEndVTIntervalTable', REFERENCE_CLASS, 'Sonetfarendvtintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetfarendvtintervaltable', 
                [], [], 
                '''                The SONET/SDH Far End VT Interval table.
                ''',
                'sonetfarendvtintervaltable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineCurrentTable', REFERENCE_CLASS, 'Sonetlinecurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetlinecurrenttable', 
                [], [], 
                '''                The SONET/SDH Line Current table.
                ''',
                'sonetlinecurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetLineIntervalTable', REFERENCE_CLASS, 'Sonetlineintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetlineintervaltable', 
                [], [], 
                '''                The SONET/SDH Line Interval table.
                ''',
                'sonetlineintervaltable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMedium', REFERENCE_CLASS, 'Sonetmedium' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmedium', 
                [], [], 
                '''                ''',
                'sonetmedium',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetMediumTable', REFERENCE_CLASS, 'Sonetmediumtable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetmediumtable', 
                [], [], 
                '''                The SONET/SDH Medium table.
                ''',
                'sonetmediumtable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathCurrentTable', REFERENCE_CLASS, 'Sonetpathcurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathcurrenttable', 
                [], [], 
                '''                The SONET/SDH Path Current table.
                ''',
                'sonetpathcurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetPathIntervalTable', REFERENCE_CLASS, 'Sonetpathintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetpathintervaltable', 
                [], [], 
                '''                The SONET/SDH Path Interval table.
                ''',
                'sonetpathintervaltable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionCurrentTable', REFERENCE_CLASS, 'Sonetsectioncurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetsectioncurrenttable', 
                [], [], 
                '''                The SONET/SDH Section Current table.
                ''',
                'sonetsectioncurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetSectionIntervalTable', REFERENCE_CLASS, 'Sonetsectionintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetsectionintervaltable', 
                [], [], 
                '''                The SONET/SDH Section Interval table.
                ''',
                'sonetsectionintervaltable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTCurrentTable', REFERENCE_CLASS, 'Sonetvtcurrenttable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetvtcurrenttable', 
                [], [], 
                '''                The SONET/SDH VT Current table.
                ''',
                'sonetvtcurrenttable',
                'SONET-MIB', False),
            _MetaInfoClassMember('sonetVTIntervalTable', REFERENCE_CLASS, 'Sonetvtintervaltable' , 'ydk.models.cisco_ios_xe.SONET_MIB', 'SonetMib.Sonetvtintervaltable', 
                [], [], 
                '''                The SONET/SDH VT Interval table.
                ''',
                'sonetvtintervaltable',
                'SONET-MIB', False),
            ],
            'SONET-MIB',
            'SONET-MIB',
            _yang_ns._namespaces['SONET-MIB'],
        'ydk.models.cisco_ios_xe.SONET_MIB'
        ),
    },
}
_meta_table['SonetMib.Sonetmediumtable.Sonetmediumentry']['meta_info'].parent =_meta_table['SonetMib.Sonetmediumtable']['meta_info']
_meta_table['SonetMib.Sonetsectioncurrenttable.Sonetsectioncurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetsectioncurrenttable']['meta_info']
_meta_table['SonetMib.Sonetsectionintervaltable.Sonetsectionintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetsectionintervaltable']['meta_info']
_meta_table['SonetMib.Sonetlinecurrenttable.Sonetlinecurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetlinecurrenttable']['meta_info']
_meta_table['SonetMib.Sonetlineintervaltable.Sonetlineintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetlineintervaltable']['meta_info']
_meta_table['SonetMib.Sonetfarendlinecurrenttable.Sonetfarendlinecurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetfarendlinecurrenttable']['meta_info']
_meta_table['SonetMib.Sonetfarendlineintervaltable.Sonetfarendlineintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetfarendlineintervaltable']['meta_info']
_meta_table['SonetMib.Sonetpathcurrenttable.Sonetpathcurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetpathcurrenttable']['meta_info']
_meta_table['SonetMib.Sonetpathintervaltable.Sonetpathintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetpathintervaltable']['meta_info']
_meta_table['SonetMib.Sonetfarendpathcurrenttable.Sonetfarendpathcurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetfarendpathcurrenttable']['meta_info']
_meta_table['SonetMib.Sonetfarendpathintervaltable.Sonetfarendpathintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetfarendpathintervaltable']['meta_info']
_meta_table['SonetMib.Sonetvtcurrenttable.Sonetvtcurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetvtcurrenttable']['meta_info']
_meta_table['SonetMib.Sonetvtintervaltable.Sonetvtintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetvtintervaltable']['meta_info']
_meta_table['SonetMib.Sonetfarendvtcurrenttable.Sonetfarendvtcurrententry']['meta_info'].parent =_meta_table['SonetMib.Sonetfarendvtcurrenttable']['meta_info']
_meta_table['SonetMib.Sonetfarendvtintervaltable.Sonetfarendvtintervalentry']['meta_info'].parent =_meta_table['SonetMib.Sonetfarendvtintervaltable']['meta_info']
_meta_table['SonetMib.Sonetmedium']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetmediumtable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetsectioncurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetsectionintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetlinecurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetlineintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetfarendlinecurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetfarendlineintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetpathcurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetpathintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetfarendpathcurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetfarendpathintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetvtcurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetvtintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetfarendvtcurrenttable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
_meta_table['SonetMib.Sonetfarendvtintervaltable']['meta_info'].parent =_meta_table['SonetMib']['meta_info']
