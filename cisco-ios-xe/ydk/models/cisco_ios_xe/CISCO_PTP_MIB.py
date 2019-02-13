""" CISCO_PTP_MIB 

The MIB module for PTPv2 (IEEE1588 \- 2008)

Overview of PTPv2 (IEEE 1588\-2008)

This IEEE standard defines a protocol enabling precise
synchronization of clocks in measurement and control systems
implemented with packet\-based networks, the IEEE Standard PTPv2
1588 (2008). This MIB does not address the standard IEEE
1588 (2002). The protocol is applicable to network elements
communicating using IP. The protocol enables heterogeneous
systems that include clocks of various inherent precision,
resolution, and stability to synchronize to a grandmaster
clock.
The protocol supports system\-wide synchronization accuracy in
the sub\-microsecond range with minimal network and local clock
computing resources. The standard uses UDP/IP. It includes
formal mechanisms for message extensions, higher sampling
rates, correction for asymmetry, a clock type to reduce error
accumulation in large topologies, and specifications on how to
incorporate the resulting additional data into the
synchronization protocol. The standard defines conformance and
management capability also.

MIB description

This MIB is to support the Precision Timing Protocol (PTP)
feature of Cisco System devices.

Acronyms\:
         ARB       arbitrary
         BMC       best master clock
         CAN       Controller Area Network
         CP        Communication Profile
                   [according to IEC 61784\-1\:200710]
         CPF       Communication Profile Family
                   [according to IEC 61784\-1\:2007]
         DS        Differentiated Service
         E2E       End\-to\-End
         E2ETC     End\-to\-End Transparent Clock
         EUI       Extended Unique Identifier.
         FFO       Fractional Frequency Offset
         GPS       Global Positioning System
         IANA      Internet Assigned Numbers Authority
         ICV       Integrity Check Value
         ID        Identification
         IPv4      Internet Protocol version 4
         IPv6      Internet Protocol version 6
         JD        Julian Date
         JDN       Julian Day Number
         MAC       Media Access Control
                   [according to IEEE Std 802.3\-2005]
         MJD       Modified Julian Day
         NIST      National Institute of Standards and
Technology                    (see www.nist.gov)
         NTP       Network Time Protocol (see IETF RFC 1305
[B7])
         OUI       Organizational Unique Identifier(allocated
by
the IEEE)
         P2P       Peer\-to\-Peer
         P2PTC     Peer\-To\-Peer Transparent Clock
         PHY       physical layer [according to IEEE Std
802.3\-2005]
         POSIX     Portable Operating System Interface
                   (see ISO/IEC 9945\:2003)
         PPS       Pulse per Second
         PTP       Precision Time Protocol
         SA        Security Associations
         SNTP      Simple Network Time Protocol
         SOF       Start of Frame
         TAI       International Atomic Time
         TC        Traffic Class
         TC        Transparent Clock
         TLV       Type, Length, Value [according to IEEE Std
802.1AB]
         ToD       Time of Day Synchronization
         ToS       Type of Service
         UCMM      UnConnect Message Manager
         UDP/IP    User Datagram Protocol
         UTC       Coordinated Universal Time

References\:
   [1]  Precision clock synchronization protocol for networked
measurement and control systems \- IEC 61588 IEEE 1588(tm)
Edition 2.0 2009\-02


Definitions from [1] section 3.1

Accuracy\:
The mean of the time or frequency error between the clock under
test and a perfect reference clock, over an ensemble of
measurements.  Stability is a measure of how the mean varies
with respect to variables such as time, temperature, and so on.

The precision is a measure of the deviation of the error from
the mean.

Atomic process\:
A process is atomic if the values of all inputs to the process
are not permitted to change until all of the results of the
process are instantiated, and the outputs of the process are
not visible to other processes until the processing of each
output is complete.

Boundary clock\:
A clock that has multiple Precision Time Protocol(PTP) ports in
a domain and maintains the timescale used in the domain.  It
may serve as the source of time, i.e., be a master clock, and
may synchronize to another clock, i.e., be a slave clock.

Boundary node clock\:
A clock that has multiple Precision Time Protocol(PTP) ports in
a domain and maintains the timescale used in the domain. It
differs from the boundary clock in that the clock roles can
change.

Clock\:
A node participating in the Precision Time Protocol (PTP) that
is capable of providing a measurement of the passage of time
since a defined epoch.

Domain\:
A logical grouping of clocks that synchronize to each other
using the protocol, but that are not necessarily synchronized
to clocks in another domain.

End\-to\-end transparent clock\:
A transparent clock that supports the use of the end\-to\-end
delay measurement mechanism between slave clocks and the master
clock.  Each node must measure the residence time of PTP event
messages and accumulate it in Correction Field.

Epoch\:
The origin of a timescale.

Event\:
An abstraction of the mechanism by which signals or conditions
are generated and represented.

Foreign master\:
An ordinary or boundary clock sending Announce messages to
another clock that is not the current master recognized by the
other clock.

Grandmaster clock\:
Within a domain, a clock that is the ultimate source of time
for clock synchronization using the protocol.

Holdover\:
A clock previously synchronized/syntonized to another clock
(normally a primary reference or a master clock) but now
free\-running based on its own internal oscillator, whose
frequency is being adjusted using data acquired while it had
been synchronized/syntonized to the other clock.  It is said to
be in holdover or in the holdover mode, as long as it is within
its accuracy requirements.

Link\:
A network segment between two Precision Time Protocol ports
supporting the peer delay mechanism of this standard.  The peer
delay mechanism is designed to measure the propagation time
over such a link.

Management node\:
A device that configures and monitors clocks.

Master clock\:
In the context of a single Precision Time Protocol
communication path, a clock that is the source of time to which
all other clocks on that path synchronize.

Message timestamp point\:
A point within a Precision Time Protocol event message serving
as a reference point in the message.  A timestamp is defined by
the instant a message timestamp point passes the reference
plane of a clock.

Multicast communication\:
A communication model in which each Precision Time Protocol
message sent from any PTP port is capable of being received and
processed by all PTP ports on the same PTP communication path.

Node\:
A device that can issue or receive Precision Time Protocol
communications on a network.

One\-step clock\:
A clock that provides time information using a single event
message.

On\-pass support\:
Indicates that each node in the synchronization chain from
master to slave can support IEEE\-1588.

Ordinary clock\:
A clock that has a single Precision Time Protocol port in a
domain and maintains the timescale used in the domain.  It may
serve as a source of time, i.e., be a master clock, or may
synchronize to another clock, i.e., be a slave clock.

Parent clock\:
The master clock to which a clock is synchronized.


Peer\-to\-peer transparent clock\:
A transparent clock that, in addition to providing Precision
Time Protocol event transit time information, also provides
corrections for the propagation delay of the link connected to
the port receiving the PTP event message.  In the presence of
peer\-to\-peer transparent clocks, delay measurements between
slave clocks and the master clock are performed using the
peer\-to\-peer delay measurement mechanism.


Phase change rate\:
The observed rate of change in the measured time with respect
to the reference time.  The phase change rate is equal to the
fractional frequency offset between the measured frequency and
the reference frequency.

PortNumber\:
An index identifying a specific Precision Time Protocol port on
a PTP node.

Primary reference\:
A source of time and or frequency that is traceable to
international standards.

Profile\:
The set of allowed Precision Time Protocol features applicable
to a device.

Precision Time Protocol communication\:
Information used in the operation of the protocol, transmitted
in a PTP message over a PTP communication path.

Precision Time Protocol communication path\: The signaling path
portion of a particular network enabling direct communication
among ordinary and boundary clocks.

Precision Time Protocol node\:
PTP ordinary, boundary, or transparent clock or a device that
generates or parses PTP messages.

Precision Time Protocol port\:
A logical access point of a clock for PTP communications to the
communications network.

Recognized standard time source\:
A recognized standard time source is a source external to
Precision Time Protocol that provides time and/or frequency as
appropriate that is traceable to the international standards
laboratories maintaining clocks that form the basis for the
International Atomic Time and Universal Coordinated Time
timescales.  Examples of these are Global Positioning System,
NTP, and National Institute of Standards and Technology (NIST)
timeservers.

Requestor\:
The port implementing the peer\-to\-peer delay mechanism that
initiates the mechanism by sending a Pdelay\_Req message.

Responder\:
The port responding to the receipt of a Pdelay\_Req message as
part of the operation of the peer\-to\-peer delay mechanism.

Synchronized clocks\:
Two clocks are synchronized to a specified uncertainty if they
have the same  epoch and their measurements of the time of a
single event at an arbitrary time differ by no more than that
uncertainty.

Syntonized clocks\:
Two clocks are syntonized if the duration of the second is the
same on both, which means the time as measured by each advances
at the same rate. They may or may not share the same epoch.

Time of Day\:


Timeout\:
A mechanism for terminating requested activity that, at least
from the requester's perspective, does not complete within the
specified time.

Timescale\:
A linear measure of time from an epoch.

Traceability\:
A property of the result of a measurement or the value of a
standard whereby it can be related to stated references,
usually national or international standards, through an unbroken
chain of comparisons all having stated uncertainties.

Translation device\:
A boundary clock or, in some cases, a transparent clock that
translates the protocol messages between regions implementing
different transport and messaging protocols, between different
versions of IEEE Std 1588\-2008/IEC 61588\:2009, or different
Precision Time Protocol profiles.

transparent clock\:
A device that measures the time taken for a Precision Time
Protocol event message to transit the device and provides this
information to clocks receiving this PTP event message.

Two\-step clock\:
A clock that provides time information using the combination of
an event message and a subsequent general message.

The below table specifies the object formats of the various
textual conventions used.

Data type mapping     Textual Convention  SYNTAX
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
5.3.2 TimeInterval    ClockTimeInterval   OCTET
STRING(SIZE(1..255))
5.3.3 Timestamp       ClockTimestamp      OCTET STRING(SIZE(6))
5.3.4 ClockIdentity   ClockIdentity       OCTET
STRING(SIZE(1..255))
5.3.5 PortIdentity    ClockPortNumber     INTEGER(1..65535)
5.3.7 ClockQuality    ClockQualityClassType

Simple master\-slave hierarchy [1] section 6.6.2.4

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
  \- Ordinary    \-
  \- Clock(1)    \-
  \- GrandMaster \-
  \-\-\-\-\-\-\-M\-\-\-\-\-\-\-
         \|
         1
         \|
  \-\-\-\-\-\-\-S\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
  \- Boundary                            \-
  \- Clock(1)                            \-
  \-\-\-\-\-\-\-\-\-\-\-\-\-\-M\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-M\-\-\-\-\-
                \|                  \|
                2                  3
                \|                  \|
           \-\-\-\-\-S\-\-\-\-\-\-     \-\-\-\-\-\-\-S\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
           \- Ordinary \-     \- Boundary               \-
           \- Clock(2) \-     \- Clock(2)               \-
           \-\-\-\-\-\-\-\-\-\-\-\-     \-\-\-\-\-M\-\-\-\-\-\-\-\-\-\-\-\-\-M\-\-\-\-\-\-
                                 \|             \|
                                 4             5
                                 \|             \|
                            \-\-\-\-\-S\-\-\-\-\-\-  \-\-\-\-\-S\-\-\-\-\-\-
                            \- Ordinary \-  \- Ordinary \-
                            \- Clock(3) \-  \- Clock(4) \-
                            \-\-\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-

  Grandmaster

  Boundary Clock(0\-N)   Ordinary Clocks(0\-N)
  Ordinary Clocks(0\-N)


 Relationship cardinality
    PTP system 1 \: N PTP Clock
    PTP Clock 1 \: 1 Domain
    PTP Clock 1 \: N PTP Ports
    PTP Port N \: N Physical Port (interface in IF\-MIB)

Transparent clock diagram from section 6.7.1.3 of [1]


          +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
          \|     Boundary clock \- 1     \|
          +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
          \|                       \|
          \|                       \|
  +\-\- A \-\-+                       B
  \|                               \|
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+           \|
\|   Ordinary clock \- 1\|           \|
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+           \|
                                  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+                  \|      End\-to\-end      \|
\|  Ordinary    \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|  transparent clock\-  \|
\|  clock 1\-1   \|                  \|       1 \- 1          \|
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+                  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
                                   \|
                                   \|
                                   C
                                   \|
                                   \|
                                  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+                  \|      End\-to\-end      \|
\|  Ordinary    \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|  transparent clock\-  \|
\|  clock 1\-2   \|                  \|       1 \- 2          \|
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-+                  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+


The MIB refers to the sections of the IEEE 1588 standard for
reference. Throughout the MIB various secions from the standard
are referenced

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ClockMechanismType(Enum):
    """
    ClockMechanismType (Enum Class)

    The clock type based on whether End to End or peer to peer

    mechanisms are used. The mechanism used to calculate the Mean

    Path Delay as indicated in Table 9 of IEEE 1588\-2008.

    Delay mechanism       Value(hex) Specification

    E2E                    01        The port is configured to use

                                     the delay request\-response

                                     mechanism.

    P2P                    02        The port is configured to use

                                     the peer delay mechanism.

    DISABLED               FE        The port does not implement

                                     the delay mechanism.

    .. data:: e2e = 1

    .. data:: p2p = 2

    .. data:: disabled = 254

    """

    e2e = Enum.YLeaf(1, "e2e")

    p2p = Enum.YLeaf(2, "p2p")

    disabled = Enum.YLeaf(254, "disabled")


class ClockPortState(Enum):
    """
    ClockPortState (Enum Class)

    This is the value of the current state of the protocol engine

    associated with this port.

    Port state      Value     Description

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

    initializing      1       In this state a port initializes

                              its data sets, hardware, and

                              communication facilities.

    faulty            2       The fault state of the protocol.

    disabled          3       The port shall not place any

                              messages on its communication path.

    listening         4       The port is waiting for the

                              announceReceiptTimeout to expire or

                              to receive an Announce message from

                              a master.

    preMaster         5       The port shall behave in all respects

                              as though it were in the MASTER state

                              except that it shall not place any

                              messages on its communication path

                              except for Pdelay\_Req, Pdelay\_Resp,

                              Pdelay\_Resp\_Follow\_Up, signaling, or

                              management messages.

    master            6       The port is behaving as a master

                              port. 

    passive           7       The port shall not place any

                              messages on its communication path

                              except for Pdelay\_Req, Pdelay\_Resp,

                              Pdelay\_Resp\_Follow\_Up, or signaling

                              messages, or management messages

                              that are a required response to

                              another management message

    uncalibrated      8       The local port is preparing to

                              synchronize to the master port.

    slave             9       The port is synchronizing to the

                              selected master port.

    .. data:: initializing = 1

    .. data:: faulty = 2

    .. data:: disabled = 3

    .. data:: listening = 4

    .. data:: preMaster = 5

    .. data:: master = 6

    .. data:: passive = 7

    .. data:: uncalibrated = 8

    .. data:: slave = 9

    """

    initializing = Enum.YLeaf(1, "initializing")

    faulty = Enum.YLeaf(2, "faulty")

    disabled = Enum.YLeaf(3, "disabled")

    listening = Enum.YLeaf(4, "listening")

    preMaster = Enum.YLeaf(5, "preMaster")

    master = Enum.YLeaf(6, "master")

    passive = Enum.YLeaf(7, "passive")

    uncalibrated = Enum.YLeaf(8, "uncalibrated")

    slave = Enum.YLeaf(9, "slave")


class ClockProfileType(Enum):
    """
    ClockProfileType (Enum Class)

    Clock Profile used. From [1] section 3.1.30, Profile is the set

    of allowed Precision Time Protocol (PTP) features applicable to

    a device.

    .. data:: default = 1

    .. data:: telecom = 2

    .. data:: vendorspecific = 3

    """

    default = Enum.YLeaf(1, "default")

    telecom = Enum.YLeaf(2, "telecom")

    vendorspecific = Enum.YLeaf(3, "vendorspecific")


class ClockQualityAccuracyType(Enum):
    """
    ClockQualityAccuracyType (Enum Class)

    The ClockQuality as specified in section 5.3.7, 7.6.2.5 and

    Table 6 of [1].

    The following values are not represented in the enumerated

    values.

             0x01\-0x1F Reserved

             0x32\-0x7F Reserved

    It is important to note that section 7.1.1 RFC2578 allows for

    gaps and enumerate values to start with zero when indicated by

    the protocol.

    .. data:: reserved00 = 1

    .. data:: nanoSecond25 = 32

    .. data:: nanoSecond100 = 33

    .. data:: nanoSecond250 = 34

    .. data:: microSec1 = 35

    .. data:: microSec2dot5 = 36

    .. data:: microSec10 = 37

    .. data:: microSec25 = 38

    .. data:: microSec100 = 39

    .. data:: microSec250 = 40

    .. data:: milliSec1 = 41

    .. data:: milliSec2dot5 = 42

    .. data:: milliSec10 = 43

    .. data:: milliSec25 = 44

    .. data:: milliSec100 = 45

    .. data:: milliSec250 = 46

    .. data:: second1 = 47

    .. data:: second10 = 48

    .. data:: secondGreater10 = 49

    .. data:: unknown = 254

    .. data:: reserved255 = 255

    """

    reserved00 = Enum.YLeaf(1, "reserved00")

    nanoSecond25 = Enum.YLeaf(32, "nanoSecond25")

    nanoSecond100 = Enum.YLeaf(33, "nanoSecond100")

    nanoSecond250 = Enum.YLeaf(34, "nanoSecond250")

    microSec1 = Enum.YLeaf(35, "microSec1")

    microSec2dot5 = Enum.YLeaf(36, "microSec2dot5")

    microSec10 = Enum.YLeaf(37, "microSec10")

    microSec25 = Enum.YLeaf(38, "microSec25")

    microSec100 = Enum.YLeaf(39, "microSec100")

    microSec250 = Enum.YLeaf(40, "microSec250")

    milliSec1 = Enum.YLeaf(41, "milliSec1")

    milliSec2dot5 = Enum.YLeaf(42, "milliSec2dot5")

    milliSec10 = Enum.YLeaf(43, "milliSec10")

    milliSec25 = Enum.YLeaf(44, "milliSec25")

    milliSec100 = Enum.YLeaf(45, "milliSec100")

    milliSec250 = Enum.YLeaf(46, "milliSec250")

    second1 = Enum.YLeaf(47, "second1")

    second10 = Enum.YLeaf(48, "second10")

    secondGreater10 = Enum.YLeaf(49, "secondGreater10")

    unknown = Enum.YLeaf(254, "unknown")

    reserved255 = Enum.YLeaf(255, "reserved255")


class ClockRoleType(Enum):
    """
    ClockRoleType (Enum Class)

    The Clock Role. The protocol generates a Master Slave

    relationship among the clocks in the system.

    Clock Role      Value     Description

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

    Master clock     1        A clock that is the source of

                              time to which all other clocks on

                              that path synchronize.

    Slave clock       2       A clock which synchronizes to

                              another clock (master).

    .. data:: master = 1

    .. data:: slave = 2

    """

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class ClockStateType(Enum):
    """
    ClockStateType (Enum Class)

    The clock state returned by PTP engine.

    Clock State      Value   Description

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

    Freerun state       1   Applies to a slave device that is not

                            locked to a master. This is the initial

                            state a slave starts out with when it

                            is not getting any PTP packets from the

                            master or because of some other input

                            error (erroneous packets, etc).

    Holdover state      2  In this state the slave device is

                            locked to a master but communication

                            with the master is lost or the

                            timestamps in the ptp packets are

                            incorrect. But since the slave was

                            locked to the master, it can run with

                            the same accuracy for sometime. The

                            slave can continue to operate in this

                            state for some time. If communication

                            with the master is not restored for a

                            while, the device is moved to the

                            FREERUN state.

    Acquiring state     3   The slave device is receiving packets

                            from a master and is trying to acquire

                            a lock.

    Freq\_locked state   4   Slave device is locked to the Master

                            with respect to frequency, but not phase

                            aligned

    Phase\_aligned state 5   Locked to the master with respect to

                            frequency and phase.

    .. data:: freerun = 1

    .. data:: holdover = 2

    .. data:: acquiring = 3

    .. data:: frequencyLocked = 4

    .. data:: phaseAligned = 5

    """

    freerun = Enum.YLeaf(1, "freerun")

    holdover = Enum.YLeaf(2, "holdover")

    acquiring = Enum.YLeaf(3, "acquiring")

    frequencyLocked = Enum.YLeaf(4, "frequencyLocked")

    phaseAligned = Enum.YLeaf(5, "phaseAligned")


class ClockTimeSourceType(Enum):
    """
    ClockTimeSourceType (Enum Class)

    The ClockQuality as specified in section 5.3.7, 7.6.2.6 and

    Table 7 of [1].

    The following values are not represented in the enumerated

    values.

    0xF0\-0xFE  For use by alternate PTP profiles

    0xFF       Reserved

    It is important to note that section 7.1.1 RFC2578 allows for

    gaps and enumerate values to start with zero when indicated by

    the protocol.

    .. data:: atomicClock = 16

    .. data:: gps = 32

    .. data:: terrestrialRadio = 48

    .. data:: ptp = 64

    .. data:: ntp = 80

    .. data:: handSet = 96

    .. data:: other = 144

    .. data:: internalOsillator = 160

    """

    atomicClock = Enum.YLeaf(16, "atomicClock")

    gps = Enum.YLeaf(32, "gps")

    terrestrialRadio = Enum.YLeaf(48, "terrestrialRadio")

    ptp = Enum.YLeaf(64, "ptp")

    ntp = Enum.YLeaf(80, "ntp")

    handSet = Enum.YLeaf(96, "handSet")

    other = Enum.YLeaf(144, "other")

    internalOsillator = Enum.YLeaf(160, "internalOsillator")


class ClockTxModeType(Enum):
    """
    ClockTxModeType (Enum Class)

    Transmission mode.

    unicast. Using unicast commnuication channel.

    multicast. Using Multicast communication channel.

    multicast\-mix. Using multicast\-unicast communication channel

    .. data:: unicast = 1

    .. data:: multicast = 2

    .. data:: multicastmix = 3

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    multicastmix = Enum.YLeaf(3, "multicastmix")


class ClockType(Enum):
    """
    ClockType (Enum Class)

    The clock types as defined in the MIB module description.

    .. data:: ordinaryClock = 1

    .. data:: boundaryClock = 2

    .. data:: transparentClock = 3

    .. data:: boundaryNode = 4

    """

    ordinaryClock = Enum.YLeaf(1, "ordinaryClock")

    boundaryClock = Enum.YLeaf(2, "boundaryClock")

    transparentClock = Enum.YLeaf(3, "transparentClock")

    boundaryNode = Enum.YLeaf(4, "boundaryNode")



class CISCOPTPMIB(Entity):
    """
    
    
    .. attribute:: ciscoptpmibsysteminfo
    
    	
    	**type**\:  :py:class:`CiscoPtpMIBSystemInfo <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CiscoPtpMIBSystemInfo>`
    
    	**config**\: False
    
    .. attribute:: cptpsystemtable
    
    	Table of count information about the PTP system for all domains
    	**type**\:  :py:class:`CPtpSystemTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemTable>`
    
    	**config**\: False
    
    .. attribute:: cptpsystemdomaintable
    
    	Table of information about the PTP system for all clock modes \-\- ordinary, boundary or transparent
    	**type**\:  :py:class:`CPtpSystemDomainTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemDomainTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclocknodetable
    
    	Table of information about the PTP system for a given domain
    	**type**\:  :py:class:`CPtpClockNodeTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockNodeTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockcurrentdstable
    
    	Table of information about the PTP clock Current Datasets for all domains
    	**type**\:  :py:class:`CPtpClockCurrentDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockCurrentDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockparentdstable
    
    	Table of information about the PTP clock Parent Datasets for all domains
    	**type**\:  :py:class:`CPtpClockParentDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockParentDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockdefaultdstable
    
    	Table of information about the PTP clock Default Datasets for all domains
    	**type**\:  :py:class:`CPtpClockDefaultDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockDefaultDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockrunningtable
    
    	Table of information about the PTP clock Running Datasets for all domains
    	**type**\:  :py:class:`CPtpClockRunningTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockRunningTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclocktimepropertiesdstable
    
    	Table of information about the PTP clock Timeproperties Datasets for all domains
    	**type**\:  :py:class:`CPtpClockTimePropertiesDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTimePropertiesDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclocktransdefaultdstable
    
    	Table of information about the PTP Transparent clock Default Datasets for all domains
    	**type**\:  :py:class:`CPtpClockTransDefaultDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTransDefaultDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockporttable
    
    	Table of information about the clock ports for a particular domain
    	**type**\:  :py:class:`CPtpClockPortTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockportdstable
    
    	Table of information about the clock ports dataset for a particular domain
    	**type**\:  :py:class:`CPtpClockPortDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockportrunningtable
    
    	Table of information about the clock ports running dataset for a particular domain
    	**type**\:  :py:class:`CPtpClockPortRunningTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortRunningTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockporttransdstable
    
    	Table of information about the Transparent clock ports running dataset for a particular domain
    	**type**\:  :py:class:`CPtpClockPortTransDSTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTransDSTable>`
    
    	**config**\: False
    
    .. attribute:: cptpclockportassociatetable
    
    	Table of information about a given port's associated ports.  For a master port \- multiple slave ports which have established sessions with the current master port.   For a slave port \- the list of masters available for a given slave port.   Session information (pkts, errors) to be displayed based on availability and scenario
    	**type**\:  :py:class:`CPtpClockPortAssociateTable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortAssociateTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-PTP-MIB'
    _revision = '2011-01-28'

    def __init__(self):
        super(CISCOPTPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PTP-MIB"
        self.yang_parent_name = "CISCO-PTP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ciscoPtpMIBSystemInfo", ("ciscoptpmibsysteminfo", CISCOPTPMIB.CiscoPtpMIBSystemInfo)), ("cPtpSystemTable", ("cptpsystemtable", CISCOPTPMIB.CPtpSystemTable)), ("cPtpSystemDomainTable", ("cptpsystemdomaintable", CISCOPTPMIB.CPtpSystemDomainTable)), ("cPtpClockNodeTable", ("cptpclocknodetable", CISCOPTPMIB.CPtpClockNodeTable)), ("cPtpClockCurrentDSTable", ("cptpclockcurrentdstable", CISCOPTPMIB.CPtpClockCurrentDSTable)), ("cPtpClockParentDSTable", ("cptpclockparentdstable", CISCOPTPMIB.CPtpClockParentDSTable)), ("cPtpClockDefaultDSTable", ("cptpclockdefaultdstable", CISCOPTPMIB.CPtpClockDefaultDSTable)), ("cPtpClockRunningTable", ("cptpclockrunningtable", CISCOPTPMIB.CPtpClockRunningTable)), ("cPtpClockTimePropertiesDSTable", ("cptpclocktimepropertiesdstable", CISCOPTPMIB.CPtpClockTimePropertiesDSTable)), ("cPtpClockTransDefaultDSTable", ("cptpclocktransdefaultdstable", CISCOPTPMIB.CPtpClockTransDefaultDSTable)), ("cPtpClockPortTable", ("cptpclockporttable", CISCOPTPMIB.CPtpClockPortTable)), ("cPtpClockPortDSTable", ("cptpclockportdstable", CISCOPTPMIB.CPtpClockPortDSTable)), ("cPtpClockPortRunningTable", ("cptpclockportrunningtable", CISCOPTPMIB.CPtpClockPortRunningTable)), ("cPtpClockPortTransDSTable", ("cptpclockporttransdstable", CISCOPTPMIB.CPtpClockPortTransDSTable)), ("cPtpClockPortAssociateTable", ("cptpclockportassociatetable", CISCOPTPMIB.CPtpClockPortAssociateTable))])
        self._leafs = OrderedDict()

        self.ciscoptpmibsysteminfo = CISCOPTPMIB.CiscoPtpMIBSystemInfo()
        self.ciscoptpmibsysteminfo.parent = self
        self._children_name_map["ciscoptpmibsysteminfo"] = "ciscoPtpMIBSystemInfo"

        self.cptpsystemtable = CISCOPTPMIB.CPtpSystemTable()
        self.cptpsystemtable.parent = self
        self._children_name_map["cptpsystemtable"] = "cPtpSystemTable"

        self.cptpsystemdomaintable = CISCOPTPMIB.CPtpSystemDomainTable()
        self.cptpsystemdomaintable.parent = self
        self._children_name_map["cptpsystemdomaintable"] = "cPtpSystemDomainTable"

        self.cptpclocknodetable = CISCOPTPMIB.CPtpClockNodeTable()
        self.cptpclocknodetable.parent = self
        self._children_name_map["cptpclocknodetable"] = "cPtpClockNodeTable"

        self.cptpclockcurrentdstable = CISCOPTPMIB.CPtpClockCurrentDSTable()
        self.cptpclockcurrentdstable.parent = self
        self._children_name_map["cptpclockcurrentdstable"] = "cPtpClockCurrentDSTable"

        self.cptpclockparentdstable = CISCOPTPMIB.CPtpClockParentDSTable()
        self.cptpclockparentdstable.parent = self
        self._children_name_map["cptpclockparentdstable"] = "cPtpClockParentDSTable"

        self.cptpclockdefaultdstable = CISCOPTPMIB.CPtpClockDefaultDSTable()
        self.cptpclockdefaultdstable.parent = self
        self._children_name_map["cptpclockdefaultdstable"] = "cPtpClockDefaultDSTable"

        self.cptpclockrunningtable = CISCOPTPMIB.CPtpClockRunningTable()
        self.cptpclockrunningtable.parent = self
        self._children_name_map["cptpclockrunningtable"] = "cPtpClockRunningTable"

        self.cptpclocktimepropertiesdstable = CISCOPTPMIB.CPtpClockTimePropertiesDSTable()
        self.cptpclocktimepropertiesdstable.parent = self
        self._children_name_map["cptpclocktimepropertiesdstable"] = "cPtpClockTimePropertiesDSTable"

        self.cptpclocktransdefaultdstable = CISCOPTPMIB.CPtpClockTransDefaultDSTable()
        self.cptpclocktransdefaultdstable.parent = self
        self._children_name_map["cptpclocktransdefaultdstable"] = "cPtpClockTransDefaultDSTable"

        self.cptpclockporttable = CISCOPTPMIB.CPtpClockPortTable()
        self.cptpclockporttable.parent = self
        self._children_name_map["cptpclockporttable"] = "cPtpClockPortTable"

        self.cptpclockportdstable = CISCOPTPMIB.CPtpClockPortDSTable()
        self.cptpclockportdstable.parent = self
        self._children_name_map["cptpclockportdstable"] = "cPtpClockPortDSTable"

        self.cptpclockportrunningtable = CISCOPTPMIB.CPtpClockPortRunningTable()
        self.cptpclockportrunningtable.parent = self
        self._children_name_map["cptpclockportrunningtable"] = "cPtpClockPortRunningTable"

        self.cptpclockporttransdstable = CISCOPTPMIB.CPtpClockPortTransDSTable()
        self.cptpclockporttransdstable.parent = self
        self._children_name_map["cptpclockporttransdstable"] = "cPtpClockPortTransDSTable"

        self.cptpclockportassociatetable = CISCOPTPMIB.CPtpClockPortAssociateTable()
        self.cptpclockportassociatetable.parent = self
        self._children_name_map["cptpclockportassociatetable"] = "cPtpClockPortAssociateTable"
        self._segment_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOPTPMIB, [], name, value)


    class CiscoPtpMIBSystemInfo(Entity):
        """
        
        
        .. attribute:: cptpsystemprofile
        
        	This object specifies the PTP Profile implemented on the system
        	**type**\:  :py:class:`ClockProfileType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockProfileType>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CiscoPtpMIBSystemInfo, self).__init__()

            self.yang_name = "ciscoPtpMIBSystemInfo"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cptpsystemprofile', (YLeaf(YType.enumeration, 'cPtpSystemProfile'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockProfileType', '')])),
            ])
            self.cptpsystemprofile = None
            self._segment_path = lambda: "ciscoPtpMIBSystemInfo"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CiscoPtpMIBSystemInfo, ['cptpsystemprofile'], name, value)



    class CPtpSystemTable(Entity):
        """
        Table of count information about the PTP system for all
        domains.
        
        .. attribute:: cptpsystementry
        
        	An entry in the table, containing count information about a single domain. New row entries are added when the PTP clock for this domain is configured, while the unconfiguration of the PTP clock removes it
        	**type**\: list of  		 :py:class:`CPtpSystemEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemTable.CPtpSystemEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpSystemTable, self).__init__()

            self.yang_name = "cPtpSystemTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpSystemEntry", ("cptpsystementry", CISCOPTPMIB.CPtpSystemTable.CPtpSystemEntry))])
            self._leafs = OrderedDict()

            self.cptpsystementry = YList(self)
            self._segment_path = lambda: "cPtpSystemTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpSystemTable, [], name, value)


        class CPtpSystemEntry(Entity):
            """
            An entry in the table, containing count information about a
            single domain. New row entries are added when the PTP clock for
            this domain is configured, while the unconfiguration of the PTP
            clock removes it.
            
            .. attribute:: cptpdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices. The Clock Domain is a logical group of clocks and devices that synchronize with each other using the PTP protocol.   0           Default domain 1           Alternate domain 1 2           Alternate domain 2 3           Alternate domain 3 4 \- 127     User\-defined domains 128 \- 255   Reserved
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpinstanceindex  (key)
            
            	This object specifies the instance of the Clock for this domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpdomainclockportstotal
            
            	This object specifies the total number of clock ports configured within a domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: ptp ports
            
            .. attribute:: cptpdomainclockportphysicalinterfacestotal
            
            	This object specifies the total number of clock port Physical interfaces configured within a domain instance for PTP communications
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: physical ports
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpSystemTable.CPtpSystemEntry, self).__init__()

                self.yang_name = "cPtpSystemEntry"
                self.yang_parent_name = "cPtpSystemTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpdomainindex','cptpinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpdomainindex', (YLeaf(YType.uint32, 'cPtpDomainIndex'), ['int'])),
                    ('cptpinstanceindex', (YLeaf(YType.uint32, 'cPtpInstanceIndex'), ['int'])),
                    ('cptpdomainclockportstotal', (YLeaf(YType.uint32, 'cPtpDomainClockPortsTotal'), ['int'])),
                    ('cptpdomainclockportphysicalinterfacestotal', (YLeaf(YType.uint32, 'cPtpDomainClockPortPhysicalInterfacesTotal'), ['int'])),
                ])
                self.cptpdomainindex = None
                self.cptpinstanceindex = None
                self.cptpdomainclockportstotal = None
                self.cptpdomainclockportphysicalinterfacestotal = None
                self._segment_path = lambda: "cPtpSystemEntry" + "[cPtpDomainIndex='" + str(self.cptpdomainindex) + "']" + "[cPtpInstanceIndex='" + str(self.cptpinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpSystemTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpSystemTable.CPtpSystemEntry, ['cptpdomainindex', 'cptpinstanceindex', 'cptpdomainclockportstotal', 'cptpdomainclockportphysicalinterfacestotal'], name, value)




    class CPtpSystemDomainTable(Entity):
        """
        Table of information about the PTP system for all clock modes
        \-\- ordinary, boundary or transparent.
        
        .. attribute:: cptpsystemdomainentry
        
        	An entry in the table, containing information about a single clock mode for the PTP system. A row entry gets added when PTP clocks are configured on the router
        	**type**\: list of  		 :py:class:`CPtpSystemDomainEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemDomainTable.CPtpSystemDomainEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpSystemDomainTable, self).__init__()

            self.yang_name = "cPtpSystemDomainTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpSystemDomainEntry", ("cptpsystemdomainentry", CISCOPTPMIB.CPtpSystemDomainTable.CPtpSystemDomainEntry))])
            self._leafs = OrderedDict()

            self.cptpsystemdomainentry = YList(self)
            self._segment_path = lambda: "cPtpSystemDomainTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpSystemDomainTable, [], name, value)


        class CPtpSystemDomainEntry(Entity):
            """
            An entry in the table, containing information about a single
            clock mode for the PTP system. A row entry gets added when PTP
            clocks are configured on the router.
            
            .. attribute:: cptpsystemdomainclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpsystemdomaintotals
            
            	This object specifies the  total number of PTP domains for this particular clock type configured in this node
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: domains
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpSystemDomainTable.CPtpSystemDomainEntry, self).__init__()

                self.yang_name = "cPtpSystemDomainEntry"
                self.yang_parent_name = "cPtpSystemDomainTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpsystemdomainclocktypeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpsystemdomainclocktypeindex', (YLeaf(YType.enumeration, 'cPtpSystemDomainClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpsystemdomaintotals', (YLeaf(YType.uint32, 'cPtpSystemDomainTotals'), ['int'])),
                ])
                self.cptpsystemdomainclocktypeindex = None
                self.cptpsystemdomaintotals = None
                self._segment_path = lambda: "cPtpSystemDomainEntry" + "[cPtpSystemDomainClockTypeIndex='" + str(self.cptpsystemdomainclocktypeindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpSystemDomainTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpSystemDomainTable.CPtpSystemDomainEntry, ['cptpsystemdomainclocktypeindex', 'cptpsystemdomaintotals'], name, value)




    class CPtpClockNodeTable(Entity):
        """
        Table of information about the PTP system for a given domain.
        
        .. attribute:: cptpclocknodeentry
        
        	An entry in the table, containing information about a single domain. A entry is added when a new PTP clock domain is configured on the router
        	**type**\: list of  		 :py:class:`CPtpClockNodeEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockNodeTable.CPtpClockNodeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockNodeTable, self).__init__()

            self.yang_name = "cPtpClockNodeTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockNodeEntry", ("cptpclocknodeentry", CISCOPTPMIB.CPtpClockNodeTable.CPtpClockNodeEntry))])
            self._leafs = OrderedDict()

            self.cptpclocknodeentry = YList(self)
            self._segment_path = lambda: "cPtpClockNodeTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockNodeTable, [], name, value)


        class CPtpClockNodeEntry(Entity):
            """
            An entry in the table, containing information about a single
            domain. A entry is added when a new PTP clock domain is
            configured on the router.
            
            .. attribute:: cptpclockdomainindex  (key)
            
            	This object specifies the  domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockinstanceindex  (key)
            
            	This object specifies the instance of the Clock for this clock type for the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockinput1ppsenabled
            
            	This object specifies whether the node is enabled for PTP input clocking using the 1pps interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockinputfrequencyenabled
            
            	This object specifies whether enabled for Frequency input using the 1.544 Mhz, 2.048 Mhz, or 10Mhz timing interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktodenabled
            
            	This object specifies whether the node is enabled for TOD
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockoutput1ppsenabled
            
            	This object specifies whether the node is enabled for PTP input clocking using the 1pps interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockoutput1ppsoffsetenabled
            
            	This object specifies whether an offset is configured in order to compensate for a known phase error such as network asymmetry
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockoutput1ppsoffsetvalue
            
            	This object specifies the fixed offset value configured to be added for the 1pps output
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cptpclockoutput1ppsoffsetnegative
            
            	This object specifies whether the added (fixed) offset to the 1pps output is negative or not.  When object returns TRUE the offset is negative and when object returns FALSE the offset is positive
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockinput1ppsinterface
            
            	This object specifies the 1pps interface used for PTP input clocking
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cptpclockoutput1ppsinterface
            
            	This object specifies the 1pps interface used for PTP output clocking
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cptpclocktodinterface
            
            	This object specifies the interface used for PTP TOD
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockNodeTable.CPtpClockNodeEntry, self).__init__()

                self.yang_name = "cPtpClockNodeEntry"
                self.yang_parent_name = "cPtpClockNodeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockdomainindex','cptpclocktypeindex','cptpclockinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockdomainindex', (YLeaf(YType.uint32, 'cPtpClockDomainIndex'), ['int'])),
                    ('cptpclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockinstanceindex', (YLeaf(YType.uint32, 'cPtpClockInstanceIndex'), ['int'])),
                    ('cptpclockinput1ppsenabled', (YLeaf(YType.boolean, 'cPtpClockInput1ppsEnabled'), ['bool'])),
                    ('cptpclockinputfrequencyenabled', (YLeaf(YType.boolean, 'cPtpClockInputFrequencyEnabled'), ['bool'])),
                    ('cptpclocktodenabled', (YLeaf(YType.boolean, 'cPtpClockTODEnabled'), ['bool'])),
                    ('cptpclockoutput1ppsenabled', (YLeaf(YType.boolean, 'cPtpClockOutput1ppsEnabled'), ['bool'])),
                    ('cptpclockoutput1ppsoffsetenabled', (YLeaf(YType.boolean, 'cPtpClockOutput1ppsOffsetEnabled'), ['bool'])),
                    ('cptpclockoutput1ppsoffsetvalue', (YLeaf(YType.uint32, 'cPtpClockOutput1ppsOffsetValue'), ['int'])),
                    ('cptpclockoutput1ppsoffsetnegative', (YLeaf(YType.boolean, 'cPtpClockOutput1ppsOffsetNegative'), ['bool'])),
                    ('cptpclockinput1ppsinterface', (YLeaf(YType.str, 'cPtpClockInput1ppsInterface'), ['str'])),
                    ('cptpclockoutput1ppsinterface', (YLeaf(YType.str, 'cPtpClockOutput1ppsInterface'), ['str'])),
                    ('cptpclocktodinterface', (YLeaf(YType.str, 'cPtpClockTODInterface'), ['str'])),
                ])
                self.cptpclockdomainindex = None
                self.cptpclocktypeindex = None
                self.cptpclockinstanceindex = None
                self.cptpclockinput1ppsenabled = None
                self.cptpclockinputfrequencyenabled = None
                self.cptpclocktodenabled = None
                self.cptpclockoutput1ppsenabled = None
                self.cptpclockoutput1ppsoffsetenabled = None
                self.cptpclockoutput1ppsoffsetvalue = None
                self.cptpclockoutput1ppsoffsetnegative = None
                self.cptpclockinput1ppsinterface = None
                self.cptpclockoutput1ppsinterface = None
                self.cptpclocktodinterface = None
                self._segment_path = lambda: "cPtpClockNodeEntry" + "[cPtpClockDomainIndex='" + str(self.cptpclockdomainindex) + "']" + "[cPtpClockTypeIndex='" + str(self.cptpclocktypeindex) + "']" + "[cPtpClockInstanceIndex='" + str(self.cptpclockinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockNodeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockNodeTable.CPtpClockNodeEntry, ['cptpclockdomainindex', 'cptpclocktypeindex', 'cptpclockinstanceindex', 'cptpclockinput1ppsenabled', 'cptpclockinputfrequencyenabled', 'cptpclocktodenabled', 'cptpclockoutput1ppsenabled', 'cptpclockoutput1ppsoffsetenabled', 'cptpclockoutput1ppsoffsetvalue', 'cptpclockoutput1ppsoffsetnegative', 'cptpclockinput1ppsinterface', 'cptpclockoutput1ppsinterface', 'cptpclocktodinterface'], name, value)




    class CPtpClockCurrentDSTable(Entity):
        """
        Table of information about the PTP clock Current Datasets for
        all domains.
        
        .. attribute:: cptpclockcurrentdsentry
        
        	An entry in the table, containing information about a single PTP clock Current Datasets for a domain
        	**type**\: list of  		 :py:class:`CPtpClockCurrentDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockCurrentDSTable.CPtpClockCurrentDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockCurrentDSTable, self).__init__()

            self.yang_name = "cPtpClockCurrentDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockCurrentDSEntry", ("cptpclockcurrentdsentry", CISCOPTPMIB.CPtpClockCurrentDSTable.CPtpClockCurrentDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclockcurrentdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockCurrentDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockCurrentDSTable, [], name, value)


        class CPtpClockCurrentDSEntry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock Current Datasets for a domain.
            
            .. attribute:: cptpclockcurrentdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockcurrentdsclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockcurrentdsinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockcurrentdsstepsremoved
            
            	The current clock dataset StepsRemoved value.  This object specifies the distance measured by the number of Boundary clocks between the local clock and the Foreign master as indicated in the stepsRemoved field of Announce messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: steps
            
            .. attribute:: cptpclockcurrentdsoffsetfrommaster
            
            	This object specifies the current clock dataset ClockOffset value. The value of the computation of the offset in time between a slave and a master clock
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            	**units**\: Time Interval
            
            .. attribute:: cptpclockcurrentdsmeanpathdelay
            
            	This object specifies the current clock dataset MeanPathDelay value.  The mean path delay between a pair of ports as measure by the delay request\-response mechanism
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockCurrentDSTable.CPtpClockCurrentDSEntry, self).__init__()

                self.yang_name = "cPtpClockCurrentDSEntry"
                self.yang_parent_name = "cPtpClockCurrentDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockcurrentdsdomainindex','cptpclockcurrentdsclocktypeindex','cptpclockcurrentdsinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockcurrentdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockCurrentDSDomainIndex'), ['int'])),
                    ('cptpclockcurrentdsclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockCurrentDSClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockcurrentdsinstanceindex', (YLeaf(YType.uint32, 'cPtpClockCurrentDSInstanceIndex'), ['int'])),
                    ('cptpclockcurrentdsstepsremoved', (YLeaf(YType.uint32, 'cPtpClockCurrentDSStepsRemoved'), ['int'])),
                    ('cptpclockcurrentdsoffsetfrommaster', (YLeaf(YType.str, 'cPtpClockCurrentDSOffsetFromMaster'), ['str'])),
                    ('cptpclockcurrentdsmeanpathdelay', (YLeaf(YType.str, 'cPtpClockCurrentDSMeanPathDelay'), ['str'])),
                ])
                self.cptpclockcurrentdsdomainindex = None
                self.cptpclockcurrentdsclocktypeindex = None
                self.cptpclockcurrentdsinstanceindex = None
                self.cptpclockcurrentdsstepsremoved = None
                self.cptpclockcurrentdsoffsetfrommaster = None
                self.cptpclockcurrentdsmeanpathdelay = None
                self._segment_path = lambda: "cPtpClockCurrentDSEntry" + "[cPtpClockCurrentDSDomainIndex='" + str(self.cptpclockcurrentdsdomainindex) + "']" + "[cPtpClockCurrentDSClockTypeIndex='" + str(self.cptpclockcurrentdsclocktypeindex) + "']" + "[cPtpClockCurrentDSInstanceIndex='" + str(self.cptpclockcurrentdsinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockCurrentDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockCurrentDSTable.CPtpClockCurrentDSEntry, ['cptpclockcurrentdsdomainindex', 'cptpclockcurrentdsclocktypeindex', 'cptpclockcurrentdsinstanceindex', 'cptpclockcurrentdsstepsremoved', 'cptpclockcurrentdsoffsetfrommaster', 'cptpclockcurrentdsmeanpathdelay'], name, value)




    class CPtpClockParentDSTable(Entity):
        """
        Table of information about the PTP clock Parent Datasets for
        all domains.
        
        .. attribute:: cptpclockparentdsentry
        
        	An entry in the table, containing information about a single PTP clock Parent Datasets for a domain
        	**type**\: list of  		 :py:class:`CPtpClockParentDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockParentDSTable.CPtpClockParentDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockParentDSTable, self).__init__()

            self.yang_name = "cPtpClockParentDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockParentDSEntry", ("cptpclockparentdsentry", CISCOPTPMIB.CPtpClockParentDSTable.CPtpClockParentDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclockparentdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockParentDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockParentDSTable, [], name, value)


        class CPtpClockParentDSEntry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock Parent Datasets for a domain.
            
            .. attribute:: cptpclockparentdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsparentportidentity
            
            	This object specifies the value of portIdentity of the port on the master that issues the Sync messages used in synchronizing this clock
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsparentstats
            
            	This object specifies the Parent Dataset ParentStats value.  This value indicates whether the values of ParentDSOffset and ParentDSClockPhChRate have been measured and are valid. A TRUE value shall indicate valid data
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsoffset
            
            	This object specifies the Parent Dataset ParentOffsetScaledLogVariance value.  This value is the variance of the parent clocks phase as measured by the local clock
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsclockphchrate
            
            	This object specifies the clock's parent dataset ParentClockPhaseChangeRate value.  This value is an estimate of the parent clocks phase change rate as measured by the slave clock
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsgmclockidentity
            
            	This object specifies the parent dataset Grandmaster clock identity
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsgmclockpriority1
            
            	This object specifies the parent dataset Grandmaster clock priority1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsgmclockpriority2
            
            	This object specifies the parent dataset grandmaster clock priority2
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsgmclockqualityclass
            
            	This object specifies the parent dataset grandmaster clock quality class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsgmclockqualityaccuracy
            
            	This object specifies the parent dataset grandmaster clock quality accuracy
            	**type**\:  :py:class:`ClockQualityAccuracyType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockQualityAccuracyType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockparentdsgmclockqualityoffset
            
            	This object specifies the parent dataset grandmaster clock quality offset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockParentDSTable.CPtpClockParentDSEntry, self).__init__()

                self.yang_name = "cPtpClockParentDSEntry"
                self.yang_parent_name = "cPtpClockParentDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockparentdsdomainindex','cptpclockparentdsclocktypeindex','cptpclockparentdsinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockparentdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockParentDSDomainIndex'), ['int'])),
                    ('cptpclockparentdsclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockParentDSClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockparentdsinstanceindex', (YLeaf(YType.uint32, 'cPtpClockParentDSInstanceIndex'), ['int'])),
                    ('cptpclockparentdsparentportidentity', (YLeaf(YType.str, 'cPtpClockParentDSParentPortIdentity'), ['str'])),
                    ('cptpclockparentdsparentstats', (YLeaf(YType.boolean, 'cPtpClockParentDSParentStats'), ['bool'])),
                    ('cptpclockparentdsoffset', (YLeaf(YType.int32, 'cPtpClockParentDSOffset'), ['int'])),
                    ('cptpclockparentdsclockphchrate', (YLeaf(YType.int32, 'cPtpClockParentDSClockPhChRate'), ['int'])),
                    ('cptpclockparentdsgmclockidentity', (YLeaf(YType.str, 'cPtpClockParentDSGMClockIdentity'), ['str'])),
                    ('cptpclockparentdsgmclockpriority1', (YLeaf(YType.int32, 'cPtpClockParentDSGMClockPriority1'), ['int'])),
                    ('cptpclockparentdsgmclockpriority2', (YLeaf(YType.int32, 'cPtpClockParentDSGMClockPriority2'), ['int'])),
                    ('cptpclockparentdsgmclockqualityclass', (YLeaf(YType.uint32, 'cPtpClockParentDSGMClockQualityClass'), ['int'])),
                    ('cptpclockparentdsgmclockqualityaccuracy', (YLeaf(YType.enumeration, 'cPtpClockParentDSGMClockQualityAccuracy'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockQualityAccuracyType', '')])),
                    ('cptpclockparentdsgmclockqualityoffset', (YLeaf(YType.uint32, 'cPtpClockParentDSGMClockQualityOffset'), ['int'])),
                ])
                self.cptpclockparentdsdomainindex = None
                self.cptpclockparentdsclocktypeindex = None
                self.cptpclockparentdsinstanceindex = None
                self.cptpclockparentdsparentportidentity = None
                self.cptpclockparentdsparentstats = None
                self.cptpclockparentdsoffset = None
                self.cptpclockparentdsclockphchrate = None
                self.cptpclockparentdsgmclockidentity = None
                self.cptpclockparentdsgmclockpriority1 = None
                self.cptpclockparentdsgmclockpriority2 = None
                self.cptpclockparentdsgmclockqualityclass = None
                self.cptpclockparentdsgmclockqualityaccuracy = None
                self.cptpclockparentdsgmclockqualityoffset = None
                self._segment_path = lambda: "cPtpClockParentDSEntry" + "[cPtpClockParentDSDomainIndex='" + str(self.cptpclockparentdsdomainindex) + "']" + "[cPtpClockParentDSClockTypeIndex='" + str(self.cptpclockparentdsclocktypeindex) + "']" + "[cPtpClockParentDSInstanceIndex='" + str(self.cptpclockparentdsinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockParentDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockParentDSTable.CPtpClockParentDSEntry, ['cptpclockparentdsdomainindex', 'cptpclockparentdsclocktypeindex', 'cptpclockparentdsinstanceindex', 'cptpclockparentdsparentportidentity', 'cptpclockparentdsparentstats', 'cptpclockparentdsoffset', 'cptpclockparentdsclockphchrate', 'cptpclockparentdsgmclockidentity', 'cptpclockparentdsgmclockpriority1', 'cptpclockparentdsgmclockpriority2', 'cptpclockparentdsgmclockqualityclass', 'cptpclockparentdsgmclockqualityaccuracy', 'cptpclockparentdsgmclockqualityoffset'], name, value)




    class CPtpClockDefaultDSTable(Entity):
        """
        Table of information about the PTP clock Default Datasets for
        all domains.
        
        .. attribute:: cptpclockdefaultdsentry
        
        	An entry in the table, containing information about a single PTP clock Default Datasets for a domain
        	**type**\: list of  		 :py:class:`CPtpClockDefaultDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockDefaultDSTable.CPtpClockDefaultDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockDefaultDSTable, self).__init__()

            self.yang_name = "cPtpClockDefaultDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockDefaultDSEntry", ("cptpclockdefaultdsentry", CISCOPTPMIB.CPtpClockDefaultDSTable.CPtpClockDefaultDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclockdefaultdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockDefaultDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockDefaultDSTable, [], name, value)


        class CPtpClockDefaultDSEntry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock Default Datasets for a domain.
            
            .. attribute:: cptpclockdefaultdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdstwostepflag
            
            	This object specifies whether the Two Step process is used
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsclockidentity
            
            	This object specifies the default Datasets clock identity
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdspriority1
            
            	This object specifies the default Datasets clock Priority1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdspriority2
            
            	This object specifies the default Datasets clock Priority2
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsslaveonly
            
            	Whether the SlaveOnly flag is set
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsqualityclass
            
            	This object specifies the default dataset Quality Class
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsqualityaccuracy
            
            	This object specifies the default dataset Quality Accurarcy
            	**type**\:  :py:class:`ClockQualityAccuracyType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockQualityAccuracyType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockdefaultdsqualityoffset
            
            	This object specifies the default dataset Quality offset
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockDefaultDSTable.CPtpClockDefaultDSEntry, self).__init__()

                self.yang_name = "cPtpClockDefaultDSEntry"
                self.yang_parent_name = "cPtpClockDefaultDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockdefaultdsdomainindex','cptpclockdefaultdsclocktypeindex','cptpclockdefaultdsinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockdefaultdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockDefaultDSDomainIndex'), ['int'])),
                    ('cptpclockdefaultdsclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockDefaultDSClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockdefaultdsinstanceindex', (YLeaf(YType.uint32, 'cPtpClockDefaultDSInstanceIndex'), ['int'])),
                    ('cptpclockdefaultdstwostepflag', (YLeaf(YType.boolean, 'cPtpClockDefaultDSTwoStepFlag'), ['bool'])),
                    ('cptpclockdefaultdsclockidentity', (YLeaf(YType.str, 'cPtpClockDefaultDSClockIdentity'), ['str'])),
                    ('cptpclockdefaultdspriority1', (YLeaf(YType.int32, 'cPtpClockDefaultDSPriority1'), ['int'])),
                    ('cptpclockdefaultdspriority2', (YLeaf(YType.int32, 'cPtpClockDefaultDSPriority2'), ['int'])),
                    ('cptpclockdefaultdsslaveonly', (YLeaf(YType.boolean, 'cPtpClockDefaultDSSlaveOnly'), ['bool'])),
                    ('cptpclockdefaultdsqualityclass', (YLeaf(YType.uint32, 'cPtpClockDefaultDSQualityClass'), ['int'])),
                    ('cptpclockdefaultdsqualityaccuracy', (YLeaf(YType.enumeration, 'cPtpClockDefaultDSQualityAccuracy'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockQualityAccuracyType', '')])),
                    ('cptpclockdefaultdsqualityoffset', (YLeaf(YType.int32, 'cPtpClockDefaultDSQualityOffset'), ['int'])),
                ])
                self.cptpclockdefaultdsdomainindex = None
                self.cptpclockdefaultdsclocktypeindex = None
                self.cptpclockdefaultdsinstanceindex = None
                self.cptpclockdefaultdstwostepflag = None
                self.cptpclockdefaultdsclockidentity = None
                self.cptpclockdefaultdspriority1 = None
                self.cptpclockdefaultdspriority2 = None
                self.cptpclockdefaultdsslaveonly = None
                self.cptpclockdefaultdsqualityclass = None
                self.cptpclockdefaultdsqualityaccuracy = None
                self.cptpclockdefaultdsqualityoffset = None
                self._segment_path = lambda: "cPtpClockDefaultDSEntry" + "[cPtpClockDefaultDSDomainIndex='" + str(self.cptpclockdefaultdsdomainindex) + "']" + "[cPtpClockDefaultDSClockTypeIndex='" + str(self.cptpclockdefaultdsclocktypeindex) + "']" + "[cPtpClockDefaultDSInstanceIndex='" + str(self.cptpclockdefaultdsinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockDefaultDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockDefaultDSTable.CPtpClockDefaultDSEntry, ['cptpclockdefaultdsdomainindex', 'cptpclockdefaultdsclocktypeindex', 'cptpclockdefaultdsinstanceindex', 'cptpclockdefaultdstwostepflag', 'cptpclockdefaultdsclockidentity', 'cptpclockdefaultdspriority1', 'cptpclockdefaultdspriority2', 'cptpclockdefaultdsslaveonly', 'cptpclockdefaultdsqualityclass', 'cptpclockdefaultdsqualityaccuracy', 'cptpclockdefaultdsqualityoffset'], name, value)




    class CPtpClockRunningTable(Entity):
        """
        Table of information about the PTP clock Running Datasets for
        all domains.
        
        .. attribute:: cptpclockrunningentry
        
        	An entry in the table, containing information about a single PTP clock running Datasets for a domain
        	**type**\: list of  		 :py:class:`CPtpClockRunningEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockRunningTable.CPtpClockRunningEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockRunningTable, self).__init__()

            self.yang_name = "cPtpClockRunningTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockRunningEntry", ("cptpclockrunningentry", CISCOPTPMIB.CPtpClockRunningTable.CPtpClockRunningEntry))])
            self._leafs = OrderedDict()

            self.cptpclockrunningentry = YList(self)
            self._segment_path = lambda: "cPtpClockRunningTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockRunningTable, [], name, value)


        class CPtpClockRunningEntry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock running Datasets for a domain.
            
            .. attribute:: cptpclockrunningdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockrunningclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockrunninginstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockrunningstate
            
            	This object specifies the Clock state returned by PTP engine which was described earlier.  Freerun state. Applies to a slave device that is not locked to a master. This is the initial state a slave starts out with when it is not getting any PTP packets from the master or because of some other input error (erroneous packets, etc).  Holdover state. In this state the slave device is locked to a master but communication with the master is lost or the timestamps in the ptp packets are incorrect. But since the slave was locked to the master, it can run with the same accuracy for sometime. The slave can continue to operate in this state for some time. If communication with the master is not restored for a while, the device is moved to the FREERUN state.  Acquiring state. The slave device is receiving packets from a master and is trying to acquire a lock.  Freq\_locked state. Slave device is locked to the Master with respect to frequency, but not phase aligned  Phase\_aligned state. Locked to the master with respect to frequency and phase
            	**type**\:  :py:class:`ClockStateType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockStateType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockrunningpacketssent
            
            	This object specifies the total number of all packet Unicast and multicast that have been sent out for this clock in this domain for this type
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cptpclockrunningpacketsreceived
            
            	This object specifies the total number of all packet Unicast and multicast that have been received for this clock in this domain for this type
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockRunningTable.CPtpClockRunningEntry, self).__init__()

                self.yang_name = "cPtpClockRunningEntry"
                self.yang_parent_name = "cPtpClockRunningTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockrunningdomainindex','cptpclockrunningclocktypeindex','cptpclockrunninginstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockrunningdomainindex', (YLeaf(YType.uint32, 'cPtpClockRunningDomainIndex'), ['int'])),
                    ('cptpclockrunningclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockRunningClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockrunninginstanceindex', (YLeaf(YType.uint32, 'cPtpClockRunningInstanceIndex'), ['int'])),
                    ('cptpclockrunningstate', (YLeaf(YType.enumeration, 'cPtpClockRunningState'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockStateType', '')])),
                    ('cptpclockrunningpacketssent', (YLeaf(YType.uint64, 'cPtpClockRunningPacketsSent'), ['int'])),
                    ('cptpclockrunningpacketsreceived', (YLeaf(YType.uint64, 'cPtpClockRunningPacketsReceived'), ['int'])),
                ])
                self.cptpclockrunningdomainindex = None
                self.cptpclockrunningclocktypeindex = None
                self.cptpclockrunninginstanceindex = None
                self.cptpclockrunningstate = None
                self.cptpclockrunningpacketssent = None
                self.cptpclockrunningpacketsreceived = None
                self._segment_path = lambda: "cPtpClockRunningEntry" + "[cPtpClockRunningDomainIndex='" + str(self.cptpclockrunningdomainindex) + "']" + "[cPtpClockRunningClockTypeIndex='" + str(self.cptpclockrunningclocktypeindex) + "']" + "[cPtpClockRunningInstanceIndex='" + str(self.cptpclockrunninginstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockRunningTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockRunningTable.CPtpClockRunningEntry, ['cptpclockrunningdomainindex', 'cptpclockrunningclocktypeindex', 'cptpclockrunninginstanceindex', 'cptpclockrunningstate', 'cptpclockrunningpacketssent', 'cptpclockrunningpacketsreceived'], name, value)




    class CPtpClockTimePropertiesDSTable(Entity):
        """
        Table of information about the PTP clock Timeproperties
        Datasets for all domains.
        
        .. attribute:: cptpclocktimepropertiesdsentry
        
        	An entry in the table, containing information about a single PTP clock timeproperties Datasets for a domain
        	**type**\: list of  		 :py:class:`CPtpClockTimePropertiesDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTimePropertiesDSTable.CPtpClockTimePropertiesDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockTimePropertiesDSTable, self).__init__()

            self.yang_name = "cPtpClockTimePropertiesDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockTimePropertiesDSEntry", ("cptpclocktimepropertiesdsentry", CISCOPTPMIB.CPtpClockTimePropertiesDSTable.CPtpClockTimePropertiesDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclocktimepropertiesdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockTimePropertiesDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockTimePropertiesDSTable, [], name, value)


        class CPtpClockTimePropertiesDSEntry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock timeproperties Datasets for a domain.
            
            .. attribute:: cptpclocktimepropertiesdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdsclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdsinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdscurrentutcoffsetvalid
            
            	This object specifies the timeproperties dataset value of whether current UTC offset is valid
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdscurrentutcoffset
            
            	This object specifies the timeproperties dataset value of current UTC offset.  In PTP systems whose epoch is the PTP epoch, the value of timePropertiesDS.currentUtcOffset is the offset between TAI and UTC; otherwise the value has no meaning. The value shall be in units of seconds. The initialization value shall be selected as follows\: a) If the timePropertiesDS.ptpTimescale (see 8.2.4.8) is TRUE, the value is the value obtained from a primary reference if the value is known at the time of initialization, else. b) The value shall be the current number of leap seconds (7.2.3) when the node is designed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdsleap59
            
            	This object specifies the Leap59 value in the clock Current Dataset
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdsleap61
            
            	This object specifies the Leap61 value in the clock Current Dataset
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdstimetraceable
            
            	This object specifies the Timetraceable value in the clock Current Dataset
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdsfreqtraceable
            
            	This object specifies the Frequency Traceable value in the clock Current Dataset
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdsptptimescale
            
            	This object specifies the PTP Timescale value in the clock Current Dataset
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclocktimepropertiesdssource
            
            	This object specifies the Timesource value in the clock Current Dataset
            	**type**\:  :py:class:`ClockTimeSourceType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockTimeSourceType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockTimePropertiesDSTable.CPtpClockTimePropertiesDSEntry, self).__init__()

                self.yang_name = "cPtpClockTimePropertiesDSEntry"
                self.yang_parent_name = "cPtpClockTimePropertiesDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclocktimepropertiesdsdomainindex','cptpclocktimepropertiesdsclocktypeindex','cptpclocktimepropertiesdsinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclocktimepropertiesdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockTimePropertiesDSDomainIndex'), ['int'])),
                    ('cptpclocktimepropertiesdsclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockTimePropertiesDSClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclocktimepropertiesdsinstanceindex', (YLeaf(YType.uint32, 'cPtpClockTimePropertiesDSInstanceIndex'), ['int'])),
                    ('cptpclocktimepropertiesdscurrentutcoffsetvalid', (YLeaf(YType.boolean, 'cPtpClockTimePropertiesDSCurrentUTCOffsetValid'), ['bool'])),
                    ('cptpclocktimepropertiesdscurrentutcoffset', (YLeaf(YType.int32, 'cPtpClockTimePropertiesDSCurrentUTCOffset'), ['int'])),
                    ('cptpclocktimepropertiesdsleap59', (YLeaf(YType.boolean, 'cPtpClockTimePropertiesDSLeap59'), ['bool'])),
                    ('cptpclocktimepropertiesdsleap61', (YLeaf(YType.boolean, 'cPtpClockTimePropertiesDSLeap61'), ['bool'])),
                    ('cptpclocktimepropertiesdstimetraceable', (YLeaf(YType.boolean, 'cPtpClockTimePropertiesDSTimeTraceable'), ['bool'])),
                    ('cptpclocktimepropertiesdsfreqtraceable', (YLeaf(YType.boolean, 'cPtpClockTimePropertiesDSFreqTraceable'), ['bool'])),
                    ('cptpclocktimepropertiesdsptptimescale', (YLeaf(YType.boolean, 'cPtpClockTimePropertiesDSPTPTimescale'), ['bool'])),
                    ('cptpclocktimepropertiesdssource', (YLeaf(YType.enumeration, 'cPtpClockTimePropertiesDSSource'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockTimeSourceType', '')])),
                ])
                self.cptpclocktimepropertiesdsdomainindex = None
                self.cptpclocktimepropertiesdsclocktypeindex = None
                self.cptpclocktimepropertiesdsinstanceindex = None
                self.cptpclocktimepropertiesdscurrentutcoffsetvalid = None
                self.cptpclocktimepropertiesdscurrentutcoffset = None
                self.cptpclocktimepropertiesdsleap59 = None
                self.cptpclocktimepropertiesdsleap61 = None
                self.cptpclocktimepropertiesdstimetraceable = None
                self.cptpclocktimepropertiesdsfreqtraceable = None
                self.cptpclocktimepropertiesdsptptimescale = None
                self.cptpclocktimepropertiesdssource = None
                self._segment_path = lambda: "cPtpClockTimePropertiesDSEntry" + "[cPtpClockTimePropertiesDSDomainIndex='" + str(self.cptpclocktimepropertiesdsdomainindex) + "']" + "[cPtpClockTimePropertiesDSClockTypeIndex='" + str(self.cptpclocktimepropertiesdsclocktypeindex) + "']" + "[cPtpClockTimePropertiesDSInstanceIndex='" + str(self.cptpclocktimepropertiesdsinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockTimePropertiesDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockTimePropertiesDSTable.CPtpClockTimePropertiesDSEntry, ['cptpclocktimepropertiesdsdomainindex', 'cptpclocktimepropertiesdsclocktypeindex', 'cptpclocktimepropertiesdsinstanceindex', 'cptpclocktimepropertiesdscurrentutcoffsetvalid', 'cptpclocktimepropertiesdscurrentutcoffset', 'cptpclocktimepropertiesdsleap59', 'cptpclocktimepropertiesdsleap61', 'cptpclocktimepropertiesdstimetraceable', 'cptpclocktimepropertiesdsfreqtraceable', 'cptpclocktimepropertiesdsptptimescale', 'cptpclocktimepropertiesdssource'], name, value)




    class CPtpClockTransDefaultDSTable(Entity):
        """
        Table of information about the PTP Transparent clock Default
        Datasets for all domains.
        
        .. attribute:: cptpclocktransdefaultdsentry
        
        	An entry in the table, containing information about a single PTP Transparent clock Default Datasets for a domain
        	**type**\: list of  		 :py:class:`CPtpClockTransDefaultDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTransDefaultDSTable.CPtpClockTransDefaultDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockTransDefaultDSTable, self).__init__()

            self.yang_name = "cPtpClockTransDefaultDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockTransDefaultDSEntry", ("cptpclocktransdefaultdsentry", CISCOPTPMIB.CPtpClockTransDefaultDSTable.CPtpClockTransDefaultDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclocktransdefaultdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockTransDefaultDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockTransDefaultDSTable, [], name, value)


        class CPtpClockTransDefaultDSEntry(Entity):
            """
            An entry in the table, containing information about a single
            PTP Transparent clock Default Datasets for a domain.
            
            .. attribute:: cptpclocktransdefaultdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclocktransdefaultdsinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclocktransdefaultdsclockidentity
            
            	This object specifies the value of the clockIdentity attribute of the local clock
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cptpclocktransdefaultdsnumofports
            
            	This object specifies the number of PTP ports of the device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cptpclocktransdefaultdsdelay
            
            	This object, if the transparent clock is an end\-to\-end transparent clock, has the value shall be E2E; If the transparent clock is a peer\-to\-peer transparent clock, the value shall be P2P
            	**type**\:  :py:class:`ClockMechanismType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockMechanismType>`
            
            	**config**\: False
            
            .. attribute:: cptpclocktransdefaultdsprimarydomain
            
            	This object specifies the value of the primary syntonization domain. The initialization value shall be 0
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockTransDefaultDSTable.CPtpClockTransDefaultDSEntry, self).__init__()

                self.yang_name = "cPtpClockTransDefaultDSEntry"
                self.yang_parent_name = "cPtpClockTransDefaultDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclocktransdefaultdsdomainindex','cptpclocktransdefaultdsinstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclocktransdefaultdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockTransDefaultDSDomainIndex'), ['int'])),
                    ('cptpclocktransdefaultdsinstanceindex', (YLeaf(YType.uint32, 'cPtpClockTransDefaultDSInstanceIndex'), ['int'])),
                    ('cptpclocktransdefaultdsclockidentity', (YLeaf(YType.str, 'cPtpClockTransDefaultDSClockIdentity'), ['str'])),
                    ('cptpclocktransdefaultdsnumofports', (YLeaf(YType.uint32, 'cPtpClockTransDefaultDSNumOfPorts'), ['int'])),
                    ('cptpclocktransdefaultdsdelay', (YLeaf(YType.enumeration, 'cPtpClockTransDefaultDSDelay'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockMechanismType', '')])),
                    ('cptpclocktransdefaultdsprimarydomain', (YLeaf(YType.int32, 'cPtpClockTransDefaultDSPrimaryDomain'), ['int'])),
                ])
                self.cptpclocktransdefaultdsdomainindex = None
                self.cptpclocktransdefaultdsinstanceindex = None
                self.cptpclocktransdefaultdsclockidentity = None
                self.cptpclocktransdefaultdsnumofports = None
                self.cptpclocktransdefaultdsdelay = None
                self.cptpclocktransdefaultdsprimarydomain = None
                self._segment_path = lambda: "cPtpClockTransDefaultDSEntry" + "[cPtpClockTransDefaultDSDomainIndex='" + str(self.cptpclocktransdefaultdsdomainindex) + "']" + "[cPtpClockTransDefaultDSInstanceIndex='" + str(self.cptpclocktransdefaultdsinstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockTransDefaultDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockTransDefaultDSTable.CPtpClockTransDefaultDSEntry, ['cptpclocktransdefaultdsdomainindex', 'cptpclocktransdefaultdsinstanceindex', 'cptpclocktransdefaultdsclockidentity', 'cptpclocktransdefaultdsnumofports', 'cptpclocktransdefaultdsdelay', 'cptpclocktransdefaultdsprimarydomain'], name, value)




    class CPtpClockPortTable(Entity):
        """
        Table of information about the clock ports for a particular
        domain.
        
        .. attribute:: cptpclockportentry
        
        	An entry in the table, containing information about a single clock port
        	**type**\: list of  		 :py:class:`CPtpClockPortEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTable.CPtpClockPortEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockPortTable, self).__init__()

            self.yang_name = "cPtpClockPortTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockPortEntry", ("cptpclockportentry", CISCOPTPMIB.CPtpClockPortTable.CPtpClockPortEntry))])
            self._leafs = OrderedDict()

            self.cptpclockportentry = YList(self)
            self._segment_path = lambda: "cPtpClockPortTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockPortTable, [], name, value)


        class CPtpClockPortEntry(Entity):
            """
            An entry in the table, containing information about a single
            clock port.
            
            .. attribute:: cptpclockportdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportclockinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockporttableportnumberindex  (key)
            
            	This object specifies the PTP Portnumber for this port
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: cptpclockportname
            
            	This object specifies the PTP clock port name configured on the router
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cptpclockportrole
            
            	This object describes the current role (slave/master) of the port
            	**type**\:  :py:class:`ClockRoleType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockRoleType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportsynconestep
            
            	This object specifies that one\-step clock operation between the PTP master and slave device is enabled
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockportcurrentpeeraddresstype
            
            	This object specifies the current peer's network address used for PTP communication. Based on the scenario and the setup involved, the values might look like these \- Scenario                   Value \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Single Master          master port Multiple Masters       selected master port Single Slave           slave port Multiple Slaves        <empty>  (In relevant setups, information on available slaves and available masters will be available through  cPtpClockPortAssociateTable)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportcurrentpeeraddress
            
            	This object specifies the current peer's network address used for PTP communication. Based on the scenario and the setup involved, the values might look like these \- Scenario                   Value \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Single Master          master port Multiple Masters       selected master port Single Slave           slave port Multiple Slaves        <empty>  (In relevant setups, information on available slaves and available masters will be available through  cPtpClockPortAssociateTable)
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportnumofassociatedports
            
            	This object specifies \- For a master port \- the number of PTP slave sessions (peers) associated with this PTP port. For a slave port \- the number of masters available to this slave port (might or might not be peered)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockPortTable.CPtpClockPortEntry, self).__init__()

                self.yang_name = "cPtpClockPortEntry"
                self.yang_parent_name = "cPtpClockPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockportdomainindex','cptpclockportclocktypeindex','cptpclockportclockinstanceindex','cptpclockporttableportnumberindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockportdomainindex', (YLeaf(YType.uint32, 'cPtpClockPortDomainIndex'), ['int'])),
                    ('cptpclockportclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockPortClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockportclockinstanceindex', (YLeaf(YType.uint32, 'cPtpClockPortClockInstanceIndex'), ['int'])),
                    ('cptpclockporttableportnumberindex', (YLeaf(YType.uint32, 'cPtpClockPortTablePortNumberIndex'), ['int'])),
                    ('cptpclockportname', (YLeaf(YType.str, 'cPtpClockPortName'), ['str'])),
                    ('cptpclockportrole', (YLeaf(YType.enumeration, 'cPtpClockPortRole'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockRoleType', '')])),
                    ('cptpclockportsynconestep', (YLeaf(YType.boolean, 'cPtpClockPortSyncOneStep'), ['bool'])),
                    ('cptpclockportcurrentpeeraddresstype', (YLeaf(YType.enumeration, 'cPtpClockPortCurrentPeerAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cptpclockportcurrentpeeraddress', (YLeaf(YType.str, 'cPtpClockPortCurrentPeerAddress'), ['str'])),
                    ('cptpclockportnumofassociatedports', (YLeaf(YType.uint32, 'cPtpClockPortNumOfAssociatedPorts'), ['int'])),
                ])
                self.cptpclockportdomainindex = None
                self.cptpclockportclocktypeindex = None
                self.cptpclockportclockinstanceindex = None
                self.cptpclockporttableportnumberindex = None
                self.cptpclockportname = None
                self.cptpclockportrole = None
                self.cptpclockportsynconestep = None
                self.cptpclockportcurrentpeeraddresstype = None
                self.cptpclockportcurrentpeeraddress = None
                self.cptpclockportnumofassociatedports = None
                self._segment_path = lambda: "cPtpClockPortEntry" + "[cPtpClockPortDomainIndex='" + str(self.cptpclockportdomainindex) + "']" + "[cPtpClockPortClockTypeIndex='" + str(self.cptpclockportclocktypeindex) + "']" + "[cPtpClockPortClockInstanceIndex='" + str(self.cptpclockportclockinstanceindex) + "']" + "[cPtpClockPortTablePortNumberIndex='" + str(self.cptpclockporttableportnumberindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockPortTable.CPtpClockPortEntry, ['cptpclockportdomainindex', 'cptpclockportclocktypeindex', 'cptpclockportclockinstanceindex', 'cptpclockporttableportnumberindex', 'cptpclockportname', 'cptpclockportrole', 'cptpclockportsynconestep', 'cptpclockportcurrentpeeraddresstype', 'cptpclockportcurrentpeeraddress', 'cptpclockportnumofassociatedports'], name, value)




    class CPtpClockPortDSTable(Entity):
        """
        Table of information about the clock ports dataset for a
        particular domain.
        
        .. attribute:: cptpclockportdsentry
        
        	An entry in the table, containing port dataset information for a single clock port
        	**type**\: list of  		 :py:class:`CPtpClockPortDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortDSTable.CPtpClockPortDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockPortDSTable, self).__init__()

            self.yang_name = "cPtpClockPortDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockPortDSEntry", ("cptpclockportdsentry", CISCOPTPMIB.CPtpClockPortDSTable.CPtpClockPortDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclockportdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockPortDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockPortDSTable, [], name, value)


        class CPtpClockPortDSEntry(Entity):
            """
            An entry in the table, containing port dataset information for
            a single clock port.
            
            .. attribute:: cptpclockportdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsclockinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsportnumberindex  (key)
            
            	This object specifies the PTP portnumber associated with this PTP port
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsname
            
            	This object specifies the PTP clock port name
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsportidentity
            
            	This object specifies the PTP clock port Identity
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsannouncementinterval
            
            	This object specifies the Announce message transmission interval associated with this clock port
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsannouncercttimeout
            
            	This object specifies the Announce receipt timeout associated with this clock port
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportdssyncinterval
            
            	This object specifies the Sync message transmission interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsmindelayreqinterval
            
            	This object specifies the Delay\_Req message transmission interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportdspeerdelayreqinterval
            
            	This object specifies the Pdelay\_Req message transmission interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsdelaymech
            
            	This object specifies the delay mechanism used. If the clock is an end\-to\-end clock, the value of the is e2e, else if the clock is a peer to\-peer clock, the value shall be p2p
            	**type**\:  :py:class:`ClockMechanismType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockMechanismType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportdspeermeanpathdelay
            
            	This object specifies the peer meanPathDelay
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsgrantduration
            
            	This object specifies the grant duration allocated by the master
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cptpclockportdsptpversion
            
            	This object specifies the PTP version being used
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockPortDSTable.CPtpClockPortDSEntry, self).__init__()

                self.yang_name = "cPtpClockPortDSEntry"
                self.yang_parent_name = "cPtpClockPortDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockportdsdomainindex','cptpclockportdsclocktypeindex','cptpclockportdsclockinstanceindex','cptpclockportdsportnumberindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockportdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockPortDSDomainIndex'), ['int'])),
                    ('cptpclockportdsclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockPortDSClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockportdsclockinstanceindex', (YLeaf(YType.uint32, 'cPtpClockPortDSClockInstanceIndex'), ['int'])),
                    ('cptpclockportdsportnumberindex', (YLeaf(YType.uint32, 'cPtpClockPortDSPortNumberIndex'), ['int'])),
                    ('cptpclockportdsname', (YLeaf(YType.str, 'cPtpClockPortDSName'), ['str'])),
                    ('cptpclockportdsportidentity', (YLeaf(YType.str, 'cPtpClockPortDSPortIdentity'), ['str'])),
                    ('cptpclockportdsannouncementinterval', (YLeaf(YType.int32, 'cPtpClockPortDSAnnouncementInterval'), ['int'])),
                    ('cptpclockportdsannouncercttimeout', (YLeaf(YType.int32, 'cPtpClockPortDSAnnounceRctTimeout'), ['int'])),
                    ('cptpclockportdssyncinterval', (YLeaf(YType.int32, 'cPtpClockPortDSSyncInterval'), ['int'])),
                    ('cptpclockportdsmindelayreqinterval', (YLeaf(YType.int32, 'cPtpClockPortDSMinDelayReqInterval'), ['int'])),
                    ('cptpclockportdspeerdelayreqinterval', (YLeaf(YType.int32, 'cPtpClockPortDSPeerDelayReqInterval'), ['int'])),
                    ('cptpclockportdsdelaymech', (YLeaf(YType.enumeration, 'cPtpClockPortDSDelayMech'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockMechanismType', '')])),
                    ('cptpclockportdspeermeanpathdelay', (YLeaf(YType.str, 'cPtpClockPortDSPeerMeanPathDelay'), ['str'])),
                    ('cptpclockportdsgrantduration', (YLeaf(YType.uint32, 'cPtpClockPortDSGrantDuration'), ['int'])),
                    ('cptpclockportdsptpversion', (YLeaf(YType.int32, 'cPtpClockPortDSPTPVersion'), ['int'])),
                ])
                self.cptpclockportdsdomainindex = None
                self.cptpclockportdsclocktypeindex = None
                self.cptpclockportdsclockinstanceindex = None
                self.cptpclockportdsportnumberindex = None
                self.cptpclockportdsname = None
                self.cptpclockportdsportidentity = None
                self.cptpclockportdsannouncementinterval = None
                self.cptpclockportdsannouncercttimeout = None
                self.cptpclockportdssyncinterval = None
                self.cptpclockportdsmindelayreqinterval = None
                self.cptpclockportdspeerdelayreqinterval = None
                self.cptpclockportdsdelaymech = None
                self.cptpclockportdspeermeanpathdelay = None
                self.cptpclockportdsgrantduration = None
                self.cptpclockportdsptpversion = None
                self._segment_path = lambda: "cPtpClockPortDSEntry" + "[cPtpClockPortDSDomainIndex='" + str(self.cptpclockportdsdomainindex) + "']" + "[cPtpClockPortDSClockTypeIndex='" + str(self.cptpclockportdsclocktypeindex) + "']" + "[cPtpClockPortDSClockInstanceIndex='" + str(self.cptpclockportdsclockinstanceindex) + "']" + "[cPtpClockPortDSPortNumberIndex='" + str(self.cptpclockportdsportnumberindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockPortDSTable.CPtpClockPortDSEntry, ['cptpclockportdsdomainindex', 'cptpclockportdsclocktypeindex', 'cptpclockportdsclockinstanceindex', 'cptpclockportdsportnumberindex', 'cptpclockportdsname', 'cptpclockportdsportidentity', 'cptpclockportdsannouncementinterval', 'cptpclockportdsannouncercttimeout', 'cptpclockportdssyncinterval', 'cptpclockportdsmindelayreqinterval', 'cptpclockportdspeerdelayreqinterval', 'cptpclockportdsdelaymech', 'cptpclockportdspeermeanpathdelay', 'cptpclockportdsgrantduration', 'cptpclockportdsptpversion'], name, value)




    class CPtpClockPortRunningTable(Entity):
        """
        Table of information about the clock ports running dataset for
        a particular domain.
        
        .. attribute:: cptpclockportrunningentry
        
        	An entry in the table, containing runing dataset information about a single clock port
        	**type**\: list of  		 :py:class:`CPtpClockPortRunningEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortRunningTable.CPtpClockPortRunningEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockPortRunningTable, self).__init__()

            self.yang_name = "cPtpClockPortRunningTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockPortRunningEntry", ("cptpclockportrunningentry", CISCOPTPMIB.CPtpClockPortRunningTable.CPtpClockPortRunningEntry))])
            self._leafs = OrderedDict()

            self.cptpclockportrunningentry = YList(self)
            self._segment_path = lambda: "cPtpClockPortRunningTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockPortRunningTable, [], name, value)


        class CPtpClockPortRunningEntry(Entity):
            """
            An entry in the table, containing runing dataset information
            about a single clock port.
            
            .. attribute:: cptpclockportrunningdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningclocktypeindex  (key)
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningclockinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningportnumberindex  (key)
            
            	This object specifies the PTP portnumber associated with this clock port
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningname
            
            	This object specifies the PTP clock port name
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningstate
            
            	This object specifies the port state returned by PTP engine.  initializing \- In this state a port initializes                its data sets, hardware, and                communication facilities. faulty       \- The fault state of the protocol. disabled     \- The port shall not place any                messages on its communication path. listening    \- The port is waiting for the                announceReceiptTimeout to expire or                to receive an Announce message from                a master. preMaster    \- The port shall behave in all respects                as though it were in the MASTER state                except that it shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, signaling, or                management messages. master       \- The port is behaving as a master port.             passive      \- The port shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, or signaling                messages, or management messages                that are a required response to                another management message uncalibrated \- The local port is preparing to                synchronize to the master port. slave        \- The port is synchronizing to the                selected master port
            	**type**\:  :py:class:`ClockPortState <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockPortState>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningrole
            
            	This object specifies the Clock Role
            	**type**\:  :py:class:`ClockRoleType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockRoleType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunninginterfaceindex
            
            	This object specifies the interface on the router being used by the PTP Clock for PTP communication
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningipversion
            
            	This object specifirst the IP version being used for PTP communication (the mapping used)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningencapsulationtype
            
            	This object specifies the type of encapsulation if the interface is adding extra  layers (eg. VLAN, Pseudowire encapsulation...) for the PTP messages
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningtxmode
            
            	This object specifies the clock transmission mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\:  :py:class:`ClockTxModeType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockTxModeType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningrxmode
            
            	This object specifie the clock receive mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\:  :py:class:`ClockTxModeType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockTxModeType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportrunningpacketsreceived
            
            	This object specifies the packets received on the clock port (cummulative)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cptpclockportrunningpacketssent
            
            	This object specifies the packets sent on the clock port (cummulative)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockPortRunningTable.CPtpClockPortRunningEntry, self).__init__()

                self.yang_name = "cPtpClockPortRunningEntry"
                self.yang_parent_name = "cPtpClockPortRunningTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockportrunningdomainindex','cptpclockportrunningclocktypeindex','cptpclockportrunningclockinstanceindex','cptpclockportrunningportnumberindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockportrunningdomainindex', (YLeaf(YType.uint32, 'cPtpClockPortRunningDomainIndex'), ['int'])),
                    ('cptpclockportrunningclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockPortRunningClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockportrunningclockinstanceindex', (YLeaf(YType.uint32, 'cPtpClockPortRunningClockInstanceIndex'), ['int'])),
                    ('cptpclockportrunningportnumberindex', (YLeaf(YType.uint32, 'cPtpClockPortRunningPortNumberIndex'), ['int'])),
                    ('cptpclockportrunningname', (YLeaf(YType.str, 'cPtpClockPortRunningName'), ['str'])),
                    ('cptpclockportrunningstate', (YLeaf(YType.enumeration, 'cPtpClockPortRunningState'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockPortState', '')])),
                    ('cptpclockportrunningrole', (YLeaf(YType.enumeration, 'cPtpClockPortRunningRole'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockRoleType', '')])),
                    ('cptpclockportrunninginterfaceindex', (YLeaf(YType.int32, 'cPtpClockPortRunningInterfaceIndex'), ['int'])),
                    ('cptpclockportrunningipversion', (YLeaf(YType.int32, 'cPtpClockPortRunningIPversion'), ['int'])),
                    ('cptpclockportrunningencapsulationtype', (YLeaf(YType.int32, 'cPtpClockPortRunningEncapsulationType'), ['int'])),
                    ('cptpclockportrunningtxmode', (YLeaf(YType.enumeration, 'cPtpClockPortRunningTxMode'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockTxModeType', '')])),
                    ('cptpclockportrunningrxmode', (YLeaf(YType.enumeration, 'cPtpClockPortRunningRxMode'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockTxModeType', '')])),
                    ('cptpclockportrunningpacketsreceived', (YLeaf(YType.uint64, 'cPtpClockPortRunningPacketsReceived'), ['int'])),
                    ('cptpclockportrunningpacketssent', (YLeaf(YType.uint64, 'cPtpClockPortRunningPacketsSent'), ['int'])),
                ])
                self.cptpclockportrunningdomainindex = None
                self.cptpclockportrunningclocktypeindex = None
                self.cptpclockportrunningclockinstanceindex = None
                self.cptpclockportrunningportnumberindex = None
                self.cptpclockportrunningname = None
                self.cptpclockportrunningstate = None
                self.cptpclockportrunningrole = None
                self.cptpclockportrunninginterfaceindex = None
                self.cptpclockportrunningipversion = None
                self.cptpclockportrunningencapsulationtype = None
                self.cptpclockportrunningtxmode = None
                self.cptpclockportrunningrxmode = None
                self.cptpclockportrunningpacketsreceived = None
                self.cptpclockportrunningpacketssent = None
                self._segment_path = lambda: "cPtpClockPortRunningEntry" + "[cPtpClockPortRunningDomainIndex='" + str(self.cptpclockportrunningdomainindex) + "']" + "[cPtpClockPortRunningClockTypeIndex='" + str(self.cptpclockportrunningclocktypeindex) + "']" + "[cPtpClockPortRunningClockInstanceIndex='" + str(self.cptpclockportrunningclockinstanceindex) + "']" + "[cPtpClockPortRunningPortNumberIndex='" + str(self.cptpclockportrunningportnumberindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortRunningTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockPortRunningTable.CPtpClockPortRunningEntry, ['cptpclockportrunningdomainindex', 'cptpclockportrunningclocktypeindex', 'cptpclockportrunningclockinstanceindex', 'cptpclockportrunningportnumberindex', 'cptpclockportrunningname', 'cptpclockportrunningstate', 'cptpclockportrunningrole', 'cptpclockportrunninginterfaceindex', 'cptpclockportrunningipversion', 'cptpclockportrunningencapsulationtype', 'cptpclockportrunningtxmode', 'cptpclockportrunningrxmode', 'cptpclockportrunningpacketsreceived', 'cptpclockportrunningpacketssent'], name, value)




    class CPtpClockPortTransDSTable(Entity):
        """
        Table of information about the Transparent clock ports running
        dataset for a particular domain.
        
        .. attribute:: cptpclockporttransdsentry
        
        	An entry in the table, containing clock port Transparent dataset information about a single clock port
        	**type**\: list of  		 :py:class:`CPtpClockPortTransDSEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTransDSTable.CPtpClockPortTransDSEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockPortTransDSTable, self).__init__()

            self.yang_name = "cPtpClockPortTransDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockPortTransDSEntry", ("cptpclockporttransdsentry", CISCOPTPMIB.CPtpClockPortTransDSTable.CPtpClockPortTransDSEntry))])
            self._leafs = OrderedDict()

            self.cptpclockporttransdsentry = YList(self)
            self._segment_path = lambda: "cPtpClockPortTransDSTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockPortTransDSTable, [], name, value)


        class CPtpClockPortTransDSEntry(Entity):
            """
            An entry in the table, containing clock port Transparent
            dataset information about a single clock port
            
            .. attribute:: cptpclockporttransdsdomainindex  (key)
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockporttransdsinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockporttransdsportnumberindex  (key)
            
            	This object specifies the PTP port number associated with this port
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: cptpclockporttransdsportidentity
            
            	This object specifies the value of the PortIdentity attribute of the local port
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cptpclockporttransdslogminpdelayreqint
            
            	This object specifies the value of the logarithm to the base 2 of the minPdelayReqInterval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cptpclockporttransdsfaultyflag
            
            	This object specifies the value TRUE if the port is faulty and FALSE if the port is operating normally
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cptpclockporttransdspeermeanpathdelay
            
            	This object specifies, (if the delayMechanism used is P2P) the value is the estimate of the current one\-way propagation delay, i.e., <meanPathDelay> on the link attached to this port computed using the peer delay mechanism. If the value of the delayMechanism used is E2E, then the value will be zero
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockPortTransDSTable.CPtpClockPortTransDSEntry, self).__init__()

                self.yang_name = "cPtpClockPortTransDSEntry"
                self.yang_parent_name = "cPtpClockPortTransDSTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockporttransdsdomainindex','cptpclockporttransdsinstanceindex','cptpclockporttransdsportnumberindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockporttransdsdomainindex', (YLeaf(YType.uint32, 'cPtpClockPortTransDSDomainIndex'), ['int'])),
                    ('cptpclockporttransdsinstanceindex', (YLeaf(YType.uint32, 'cPtpClockPortTransDSInstanceIndex'), ['int'])),
                    ('cptpclockporttransdsportnumberindex', (YLeaf(YType.uint32, 'cPtpClockPortTransDSPortNumberIndex'), ['int'])),
                    ('cptpclockporttransdsportidentity', (YLeaf(YType.str, 'cPtpClockPortTransDSPortIdentity'), ['str'])),
                    ('cptpclockporttransdslogminpdelayreqint', (YLeaf(YType.int32, 'cPtpClockPortTransDSlogMinPdelayReqInt'), ['int'])),
                    ('cptpclockporttransdsfaultyflag', (YLeaf(YType.boolean, 'cPtpClockPortTransDSFaultyFlag'), ['bool'])),
                    ('cptpclockporttransdspeermeanpathdelay', (YLeaf(YType.str, 'cPtpClockPortTransDSPeerMeanPathDelay'), ['str'])),
                ])
                self.cptpclockporttransdsdomainindex = None
                self.cptpclockporttransdsinstanceindex = None
                self.cptpclockporttransdsportnumberindex = None
                self.cptpclockporttransdsportidentity = None
                self.cptpclockporttransdslogminpdelayreqint = None
                self.cptpclockporttransdsfaultyflag = None
                self.cptpclockporttransdspeermeanpathdelay = None
                self._segment_path = lambda: "cPtpClockPortTransDSEntry" + "[cPtpClockPortTransDSDomainIndex='" + str(self.cptpclockporttransdsdomainindex) + "']" + "[cPtpClockPortTransDSInstanceIndex='" + str(self.cptpclockporttransdsinstanceindex) + "']" + "[cPtpClockPortTransDSPortNumberIndex='" + str(self.cptpclockporttransdsportnumberindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortTransDSTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockPortTransDSTable.CPtpClockPortTransDSEntry, ['cptpclockporttransdsdomainindex', 'cptpclockporttransdsinstanceindex', 'cptpclockporttransdsportnumberindex', 'cptpclockporttransdsportidentity', 'cptpclockporttransdslogminpdelayreqint', 'cptpclockporttransdsfaultyflag', 'cptpclockporttransdspeermeanpathdelay'], name, value)




    class CPtpClockPortAssociateTable(Entity):
        """
        Table of information about a given port's associated ports.
        
        For a master port \- multiple slave ports which have established
        sessions with the current master port.  
        For a slave port \- the list of masters available for a given
        slave port. 
        
        Session information (pkts, errors) to be displayed based on
        availability and scenario.
        
        .. attribute:: cptpclockportassociateentry
        
        	An entry in the table, containing information about a single associated port for the given clockport
        	**type**\: list of  		 :py:class:`CPtpClockPortAssociateEntry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortAssociateTable.CPtpClockPortAssociateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CISCOPTPMIB.CPtpClockPortAssociateTable, self).__init__()

            self.yang_name = "cPtpClockPortAssociateTable"
            self.yang_parent_name = "CISCO-PTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cPtpClockPortAssociateEntry", ("cptpclockportassociateentry", CISCOPTPMIB.CPtpClockPortAssociateTable.CPtpClockPortAssociateEntry))])
            self._leafs = OrderedDict()

            self.cptpclockportassociateentry = YList(self)
            self._segment_path = lambda: "cPtpClockPortAssociateTable"
            self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPTPMIB.CPtpClockPortAssociateTable, [], name, value)


        class CPtpClockPortAssociateEntry(Entity):
            """
            An entry in the table, containing information about a single
            associated port for the given clockport.
            
            .. attribute:: cptpclockportcurrentdomainindex  (key)
            
            	This object specifies the given port's domain number
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportcurrentclocktypeindex  (key)
            
            	This object specifies the given port's clock type
            	**type**\:  :py:class:`ClockType <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportcurrentclockinstanceindex  (key)
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportcurrentportnumberindex  (key)
            
            	This object specifies the PTP Port Number for the given port
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cptpclockportassociateportindex  (key)
            
            	This object specifies the associated port's serial number in the current port's context
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: cptpclockportassociateaddresstype
            
            	This object specifies the peer port's network address type used for PTP communication
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cptpclockportassociateaddress
            
            	This object specifies the peer port's network address used for PTP communication
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cptpclockportassociatepacketssent
            
            	The number of packets sent to this peer port from the current port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cptpclockportassociatepacketsreceived
            
            	The number of packets received from this peer port by the current port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cptpclockportassociateinerrors
            
            	This object specifies the input errors associated with the peer port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cptpclockportassociateouterrors
            
            	This object specifies the output errors associated with the peer port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CISCOPTPMIB.CPtpClockPortAssociateTable.CPtpClockPortAssociateEntry, self).__init__()

                self.yang_name = "cPtpClockPortAssociateEntry"
                self.yang_parent_name = "cPtpClockPortAssociateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cptpclockportcurrentdomainindex','cptpclockportcurrentclocktypeindex','cptpclockportcurrentclockinstanceindex','cptpclockportcurrentportnumberindex','cptpclockportassociateportindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cptpclockportcurrentdomainindex', (YLeaf(YType.uint32, 'cPtpClockPortCurrentDomainIndex'), ['int'])),
                    ('cptpclockportcurrentclocktypeindex', (YLeaf(YType.enumeration, 'cPtpClockPortCurrentClockTypeIndex'), [('ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockType', '')])),
                    ('cptpclockportcurrentclockinstanceindex', (YLeaf(YType.uint32, 'cPtpClockPortCurrentClockInstanceIndex'), ['int'])),
                    ('cptpclockportcurrentportnumberindex', (YLeaf(YType.uint32, 'cPtpClockPortCurrentPortNumberIndex'), ['int'])),
                    ('cptpclockportassociateportindex', (YLeaf(YType.uint32, 'cPtpClockPortAssociatePortIndex'), ['int'])),
                    ('cptpclockportassociateaddresstype', (YLeaf(YType.enumeration, 'cPtpClockPortAssociateAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cptpclockportassociateaddress', (YLeaf(YType.str, 'cPtpClockPortAssociateAddress'), ['str'])),
                    ('cptpclockportassociatepacketssent', (YLeaf(YType.uint64, 'cPtpClockPortAssociatePacketsSent'), ['int'])),
                    ('cptpclockportassociatepacketsreceived', (YLeaf(YType.uint64, 'cPtpClockPortAssociatePacketsReceived'), ['int'])),
                    ('cptpclockportassociateinerrors', (YLeaf(YType.uint64, 'cPtpClockPortAssociateInErrors'), ['int'])),
                    ('cptpclockportassociateouterrors', (YLeaf(YType.uint64, 'cPtpClockPortAssociateOutErrors'), ['int'])),
                ])
                self.cptpclockportcurrentdomainindex = None
                self.cptpclockportcurrentclocktypeindex = None
                self.cptpclockportcurrentclockinstanceindex = None
                self.cptpclockportcurrentportnumberindex = None
                self.cptpclockportassociateportindex = None
                self.cptpclockportassociateaddresstype = None
                self.cptpclockportassociateaddress = None
                self.cptpclockportassociatepacketssent = None
                self.cptpclockportassociatepacketsreceived = None
                self.cptpclockportassociateinerrors = None
                self.cptpclockportassociateouterrors = None
                self._segment_path = lambda: "cPtpClockPortAssociateEntry" + "[cPtpClockPortCurrentDomainIndex='" + str(self.cptpclockportcurrentdomainindex) + "']" + "[cPtpClockPortCurrentClockTypeIndex='" + str(self.cptpclockportcurrentclocktypeindex) + "']" + "[cPtpClockPortCurrentClockInstanceIndex='" + str(self.cptpclockportcurrentclockinstanceindex) + "']" + "[cPtpClockPortCurrentPortNumberIndex='" + str(self.cptpclockportcurrentportnumberindex) + "']" + "[cPtpClockPortAssociatePortIndex='" + str(self.cptpclockportassociateportindex) + "']"
                self._absolute_path = lambda: "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortAssociateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPTPMIB.CPtpClockPortAssociateTable.CPtpClockPortAssociateEntry, ['cptpclockportcurrentdomainindex', 'cptpclockportcurrentclocktypeindex', 'cptpclockportcurrentclockinstanceindex', 'cptpclockportcurrentportnumberindex', 'cptpclockportassociateportindex', 'cptpclockportassociateaddresstype', 'cptpclockportassociateaddress', 'cptpclockportassociatepacketssent', 'cptpclockportassociatepacketsreceived', 'cptpclockportassociateinerrors', 'cptpclockportassociateouterrors'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOPTPMIB()
        return self._top_entity



