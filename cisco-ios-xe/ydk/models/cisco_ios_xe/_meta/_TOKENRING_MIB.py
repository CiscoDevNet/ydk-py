


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Dot5Chipsettitms380C16Identity' : {
        'meta_info' : _MetaInfoClass('Dot5Chipsettitms380C16Identity',
            False, 
            [
            ],
            'TOKENRING-MIB',
            'dot5ChipSetTItms380c16',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'Dot5TestinsertfuncIdentity' : {
        'meta_info' : _MetaInfoClass('Dot5TestinsertfuncIdentity',
            False, 
            [
            ],
            'TOKENRING-MIB',
            'dot5TestInsertFunc',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'Dot5TestfullduplexloopbackIdentity' : {
        'meta_info' : _MetaInfoClass('Dot5TestfullduplexloopbackIdentity',
            False, 
            [
            ],
            'TOKENRING-MIB',
            'dot5TestFullDuplexLoopBack',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'Dot5Chipsettitms380Identity' : {
        'meta_info' : _MetaInfoClass('Dot5Chipsettitms380Identity',
            False, 
            [
            ],
            'TOKENRING-MIB',
            'dot5ChipSetTItms380',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'Dot5Chipsetibm16Identity' : {
        'meta_info' : _MetaInfoClass('Dot5Chipsetibm16Identity',
            False, 
            [
            ],
            'TOKENRING-MIB',
            'dot5ChipSetIBM16',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib.Dot5Table.Dot5Entry.Dot5ActmonparticipateEnum' : _MetaInfoEnum('Dot5ActmonparticipateEnum', 'ydk.models.cisco_ios_xe.TOKENRING_MIB',
        {
            'true':'true',
            'false':'false',
        }, 'TOKENRING-MIB', _yang_ns._namespaces['TOKENRING-MIB']),
    'TokenringMib.Dot5Table.Dot5Entry.Dot5CommandsEnum' : _MetaInfoEnum('Dot5CommandsEnum', 'ydk.models.cisco_ios_xe.TOKENRING_MIB',
        {
            'noop':'noop',
            'open':'open',
            'reset':'reset',
            'close':'close',
        }, 'TOKENRING-MIB', _yang_ns._namespaces['TOKENRING-MIB']),
    'TokenringMib.Dot5Table.Dot5Entry.Dot5RingopenstatusEnum' : _MetaInfoEnum('Dot5RingopenstatusEnum', 'ydk.models.cisco_ios_xe.TOKENRING_MIB',
        {
            'noOpen':'noOpen',
            'badParam':'badParam',
            'lobeFailed':'lobeFailed',
            'signalLoss':'signalLoss',
            'insertionTimeout':'insertionTimeout',
            'ringFailed':'ringFailed',
            'beaconing':'beaconing',
            'duplicateMAC':'duplicateMAC',
            'requestFailed':'requestFailed',
            'removeReceived':'removeReceived',
            'open':'open',
        }, 'TOKENRING-MIB', _yang_ns._namespaces['TOKENRING-MIB']),
    'TokenringMib.Dot5Table.Dot5Entry.Dot5RingspeedEnum' : _MetaInfoEnum('Dot5RingspeedEnum', 'ydk.models.cisco_ios_xe.TOKENRING_MIB',
        {
            'unknown':'unknown',
            'oneMegabit':'oneMegabit',
            'fourMegabit':'fourMegabit',
            'sixteenMegabit':'sixteenMegabit',
        }, 'TOKENRING-MIB', _yang_ns._namespaces['TOKENRING-MIB']),
    'TokenringMib.Dot5Table.Dot5Entry.Dot5RingstateEnum' : _MetaInfoEnum('Dot5RingstateEnum', 'ydk.models.cisco_ios_xe.TOKENRING_MIB',
        {
            'opened':'opened',
            'closed':'closed',
            'opening':'opening',
            'closing':'closing',
            'openFailure':'openFailure',
            'ringFailure':'ringFailure',
        }, 'TOKENRING-MIB', _yang_ns._namespaces['TOKENRING-MIB']),
    'TokenringMib.Dot5Table.Dot5Entry' : {
        'meta_info' : _MetaInfoClass('TokenringMib.Dot5Table.Dot5Entry',
            False, 
            [
            _MetaInfoClassMember('dot5IfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object identifies the
                802.5 interface for which this entry
                contains management information.  The
                value of this object for a particular
                interface has the same value as the
                ifIndex object, defined in MIB-II for
                the same interface.
                ''',
                'dot5ifindex',
                'TOKENRING-MIB', True),
            _MetaInfoClassMember('dot5ActMonParticipate', REFERENCE_ENUM_CLASS, 'Dot5ActmonparticipateEnum' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table.Dot5Entry.Dot5ActmonparticipateEnum', 
                [], [], 
                '''                If this object has a value of true(1) then
                this interface will participate in the
                active monitor selection process.  If the
                value is false(2) then it will not.
                Setting this object does not take effect
                until the next Active Monitor election, and
                might not take effect until the next time
                the interface is opened.
                ''',
                'dot5actmonparticipate',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5Commands', REFERENCE_ENUM_CLASS, 'Dot5CommandsEnum' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table.Dot5Entry.Dot5CommandsEnum', 
                [], [], 
                '''                When this object is set to the value of
                open(2), the station should go into the
                open state.  The progress and success of
                the open is given by the values of the
                objects dot5RingState and
                dot5RingOpenStatus.
                    When this object is set to the value
                of reset(3), then the station should do
                a reset.  On a reset, all MIB counters
                should retain their values, if possible.
                Other side affects are dependent on the
                hardware chip set.
                    When this object is set to the value
                of close(4), the station should go into
                the stopped state by removing itself
                from the ring.
                    Setting this object to a value of
                noop(1) has no effect.
                    When read, this object always has a
                value of noop(1).
                    The open(2) and close(4) values
                correspond to the up(1) and down(2) values
                of MIB-II's ifAdminStatus and ifOperStatus,
                i.e., the setting of ifAdminStatus and
                
                
                dot5Commands affects the values of both
                dot5Commands and ifOperStatus.
                ''',
                'dot5commands',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5Functional', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The bit mask of all Token Ring functional
                addresses for which this interface will
                accept frames.
                ''',
                'dot5functional',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5LastBeaconSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of MIB-II's sysUpTime object at which
                the local system last transmitted a Beacon frame
                on this interface.
                ''',
                'dot5lastbeaconsent',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5RingOpenStatus', REFERENCE_ENUM_CLASS, 'Dot5RingopenstatusEnum' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table.Dot5Entry.Dot5RingopenstatusEnum', 
                [], [], 
                '''                This object indicates the success, or the
                reason for failure, of the station's most
                recent attempt to enter the ring.
                ''',
                'dot5ringopenstatus',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5RingSpeed', REFERENCE_ENUM_CLASS, 'Dot5RingspeedEnum' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table.Dot5Entry.Dot5RingspeedEnum', 
                [], [], 
                '''                The ring-speed at the next insertion into
                the ring.  Note that this may or may not be
                different to the current ring-speed which is
                given by MIB-II's ifSpeed.  For interfaces
                which do not support changing ring-speed,
                dot5RingSpeed can only be set to its current
                value.  When dot5RingSpeed has the value
                unknown(1), the ring's actual ring-speed is
                to be used.
                ''',
                'dot5ringspeed',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5RingState', REFERENCE_ENUM_CLASS, 'Dot5RingstateEnum' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table.Dot5Entry.Dot5RingstateEnum', 
                [], [], 
                '''                The current interface state with respect
                to entering or leaving the ring.
                ''',
                'dot5ringstate',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5RingStatus', ATTRIBUTE, 'int' , None, None, 
                [('0', '262143')], [], 
                '''                The current interface status which can
                be used to diagnose fluctuating problems
                that can occur on token rings, after a
                station has successfully been added to
                the ring.
                   Before an open is completed, this
                object has the value for the 'no status'
                condition.  The dot5RingState and
                dot5RingOpenStatus objects provide for
                debugging problems when the station
                can not even enter the ring.
                    The object's value is a sum of
                values, one for each currently applicable
                condition.  The following values are
                defined for various conditions:
                
                        0 = No Problems detected
                       32 = Ring Recovery
                       64 = Single Station
                      256 = Remove Received
                      512 = reserved
                     1024 = Auto-Removal Error
                     2048 = Lobe Wire Fault
                     4096 = Transmit Beacon
                     8192 = Soft Error
                    16384 = Hard Error
                    32768 = Signal Loss
                   131072 = no status, open not completed.
                ''',
                'dot5ringstatus',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5UpStream', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC-address of the up stream neighbor
                station in the ring.
                ''',
                'dot5upstream',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'dot5Entry',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib.Dot5Table' : {
        'meta_info' : _MetaInfoClass('TokenringMib.Dot5Table',
            False, 
            [
            _MetaInfoClassMember('dot5Entry', REFERENCE_LIST, 'Dot5Entry' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table.Dot5Entry', 
                [], [], 
                '''                A list of Token Ring status and parameter
                values for an 802.5 interface.
                ''',
                'dot5entry',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'dot5Table',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib.Dot5Statstable.Dot5Statsentry' : {
        'meta_info' : _MetaInfoClass('TokenringMib.Dot5Statstable.Dot5Statsentry',
            False, 
            [
            _MetaInfoClassMember('dot5StatsIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object identifies the
                802.5 interface for which this entry
                contains management information.  The
                value of this object for a particular
                interface has the same value as MIB-II's
                ifIndex object for the same interface.
                ''',
                'dot5statsifindex',
                'TOKENRING-MIB', True),
            _MetaInfoClassMember('dot5StatsAbortTransErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                transmits an abort delimiter while
                transmitting.
                ''',
                'dot5statsaborttranserrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsACErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                receives an AMP or SMP frame in which A is
                equal to C is equal to 0, and then receives
                another SMP frame with A is equal to C is
                equal to 0 without first receiving an AMP
                frame. It denotes a station that cannot set
                the AC bits properly.
                ''',
                'dot5statsacerrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsBurstErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                detects the absence of transitions for five
                half-bit timers (burst-five error).
                ''',
                'dot5statsbursterrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsFrameCopiedErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                recognizes a frame addressed to its
                specific address and detects that the FS
                field A bits are set to 1 indicating a
                possible line hit or duplicate address.
                ''',
                'dot5statsframecopiederrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsFreqErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the interface has
                detected that the frequency of the
                incoming signal differs from the expected
                frequency by more than that specified by
                the IEEE 802.5 standard.
                ''',
                'dot5statsfreqerrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsHardErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this interface has
                detected an immediately recoverable
                fatal error.  It denotes the number of
                times this interface is either
                transmitting or receiving beacon MAC
                frames.
                ''',
                'dot5statsharderrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsInternalErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                recognizes an internal error.
                ''',
                'dot5statsinternalerrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsLineErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a frame
                or token is copied or repeated by a
                station, the E bit is zero in the frame
                or token and one of the following
                conditions exists: 1) there is a
                non-data bit (J or K bit) between the SD
                and the ED of the frame or token, or
                2) there is an FCS error in the frame.
                ''',
                'dot5statslineerrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsLobeWires', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the interface has
                detected an open or short circuit in the
                lobe data path.  The adapter will be closed
                and dot5RingState will signify this
                condition.
                ''',
                'dot5statslobewires',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsLostFrameErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                is transmitting and its TRR timer expires.
                This condition denotes a condition where a
                transmitting station in strip mode does not
                receive the trailer of the frame before the
                TRR timer goes off.
                ''',
                'dot5statslostframeerrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsReceiveCongestions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                recognizes a frame addressed to its
                specific address, but has no available
                buffer space indicating that the station
                is congested.
                ''',
                'dot5statsreceivecongestions',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsRecoverys', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Claim Token MAC frames
                received or transmitted after the interface
                has received a Ring Purge MAC frame.  This
                counter signifies the number of times the
                ring has been purged and is being recovered
                back into a normal operating state.
                ''',
                'dot5statsrecoverys',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsRemoves', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the interface has
                received a Remove Ring Station MAC frame
                request.  When this frame is received
                the interface will enter the close state
                and dot5RingState will signify this
                condition.
                ''',
                'dot5statsremoves',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsSignalLoss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this interface has
                detected the loss of signal condition from
                the ring.
                ''',
                'dot5statssignalloss',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsSingles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the interface has
                sensed that it is the only station on the
                ring.  This will happen if the interface
                is the first one up on a ring, or if
                there is a hardware problem.
                ''',
                'dot5statssingles',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsSoftErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Soft Errors the interface
                has detected. It directly corresponds to
                the number of Report Error MAC frames
                that this interface has transmitted.
                Soft Errors are those which are
                recoverable by the MAC layer protocols.
                ''',
                'dot5statssofterrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsTokenErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a station
                acting as the active monitor recognizes an
                error condition that needs a token
                transmitted.
                ''',
                'dot5statstokenerrors',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5StatsTransmitBeacons', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this interface has
                transmitted a beacon frame.
                ''',
                'dot5statstransmitbeacons',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'dot5StatsEntry',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib.Dot5Statstable' : {
        'meta_info' : _MetaInfoClass('TokenringMib.Dot5Statstable',
            False, 
            [
            _MetaInfoClassMember('dot5StatsEntry', REFERENCE_LIST, 'Dot5Statsentry' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Statstable.Dot5Statsentry', 
                [], [], 
                '''                An entry contains the 802.5 statistics
                for a particular interface.
                ''',
                'dot5statsentry',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'dot5StatsTable',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib.Dot5Timertable.Dot5Timerentry' : {
        'meta_info' : _MetaInfoClass('TokenringMib.Dot5Timertable.Dot5Timerentry',
            False, 
            [
            _MetaInfoClassMember('dot5TimerIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The value of this object identifies the
                802.5 interface for which this entry
                contains timer values.  The value of
                
                
                this object for a particular interface
                has the same value as MIB-II's ifIndex
                object for the same interface.
                ''',
                'dot5timerifindex',
                'TOKENRING-MIB', True),
            _MetaInfoClassMember('dot5TimerActiveMon', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value used by the active
                monitor to stimulate the enqueuing of an
                AMP PDU for transmission, in units of
                100 micro-seconds.
                ''',
                'dot5timeractivemon',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerBeaconReceive', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value which determines how
                long a station shall receive Beacon
                frames from its downstream neighbor
                before entering the Bypass state, in
                units of 100 micro-seconds.
                ''',
                'dot5timerbeaconreceive',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerBeaconTransmit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value which determines how
                long a station shall remain in the state
                of transmitting Beacon frames before
                entering the Bypass state, in units of
                100 micro-seconds.
                ''',
                'dot5timerbeacontransmit',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerErrorReport', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value which determines how
                often a station shall send a Report Error
                MAC frame to report its error counters,
                in units of 100 micro-seconds.
                ''',
                'dot5timererrorreport',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerHolding', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum period of time a station is
                permitted to transmit frames after capturing
                a token, in units of 100 micro-seconds.
                ''',
                'dot5timerholding',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerNoToken', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value used to recover from
                various-related error situations.
                If N is the maximum number of stations on
                the ring, the value of this timer is
                normally:
                dot5TimerReturnRepeat + N*dot5TimerHolding.
                ''',
                'dot5timernotoken',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerQueuePDU', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value for enqueuing of an SMP
                PDU after reception of an AMP or SMP
                frame in which the A and C bits were
                equal to 0, in units of 100
                micro-seconds.
                ''',
                'dot5timerqueuepdu',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerReturnRepeat', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value used to ensure the
                interface will return to Repeat State, in
                units of 100 micro-seconds.  The value
                should be greater than the maximum ring
                latency.
                ''',
                'dot5timerreturnrepeat',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerStandbyMon', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value used by the stand-by
                monitors to ensure that there is an active
                monitor on the ring and to detect a
                continuous stream of tokens, in units of
                100 micro-seconds.
                ''',
                'dot5timerstandbymon',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerValidTransmit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The time-out value used by the active
                monitor to detect the absence of valid
                transmissions, in units of 100
                micro-seconds.
                ''',
                'dot5timervalidtransmit',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'dot5TimerEntry',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib.Dot5Timertable' : {
        'meta_info' : _MetaInfoClass('TokenringMib.Dot5Timertable',
            False, 
            [
            _MetaInfoClassMember('dot5TimerEntry', REFERENCE_LIST, 'Dot5Timerentry' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Timertable.Dot5Timerentry', 
                [], [], 
                '''                A list of Token Ring timer values for an
                802.5 interface.
                ''',
                'dot5timerentry',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'dot5TimerTable',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
    'TokenringMib' : {
        'meta_info' : _MetaInfoClass('TokenringMib',
            False, 
            [
            _MetaInfoClassMember('dot5StatsTable', REFERENCE_CLASS, 'Dot5Statstable' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Statstable', 
                [], [], 
                '''                A table containing Token Ring statistics,
                one entry per 802.5 interface.
                    All the statistics are defined using
                the syntax Counter32 as 32-bit wrap around
                counters.  Thus, if an interface's
                hardware maintains these statistics in
                16-bit counters, then the agent must read
                the hardware's counters frequently enough
                to prevent loss of significance, in order
                to maintain 32-bit counters in software.
                ''',
                'dot5statstable',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5Table', REFERENCE_CLASS, 'Dot5Table' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Table', 
                [], [], 
                '''                This table contains Token Ring interface
                parameters and state variables, one entry
                per 802.5 interface.
                ''',
                'dot5table',
                'TOKENRING-MIB', False),
            _MetaInfoClassMember('dot5TimerTable', REFERENCE_CLASS, 'Dot5Timertable' , 'ydk.models.cisco_ios_xe.TOKENRING_MIB', 'TokenringMib.Dot5Timertable', 
                [], [], 
                '''                This table contains Token Ring interface
                timer values, one entry per 802.5
                interface.
                ''',
                'dot5timertable',
                'TOKENRING-MIB', False),
            ],
            'TOKENRING-MIB',
            'TOKENRING-MIB',
            _yang_ns._namespaces['TOKENRING-MIB'],
        'ydk.models.cisco_ios_xe.TOKENRING_MIB'
        ),
    },
}
_meta_table['TokenringMib.Dot5Table.Dot5Entry']['meta_info'].parent =_meta_table['TokenringMib.Dot5Table']['meta_info']
_meta_table['TokenringMib.Dot5Statstable.Dot5Statsentry']['meta_info'].parent =_meta_table['TokenringMib.Dot5Statstable']['meta_info']
_meta_table['TokenringMib.Dot5Timertable.Dot5Timerentry']['meta_info'].parent =_meta_table['TokenringMib.Dot5Timertable']['meta_info']
_meta_table['TokenringMib.Dot5Table']['meta_info'].parent =_meta_table['TokenringMib']['meta_info']
_meta_table['TokenringMib.Dot5Statstable']['meta_info'].parent =_meta_table['TokenringMib']['meta_info']
_meta_table['TokenringMib.Dot5Timertable']['meta_info'].parent =_meta_table['TokenringMib']['meta_info']
