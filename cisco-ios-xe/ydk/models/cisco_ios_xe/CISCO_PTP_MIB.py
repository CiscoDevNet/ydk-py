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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Clockmechanismtype(Enum):
    """
    Clockmechanismtype

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


class Clockportstate(Enum):
    """
    Clockportstate

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


class Clockprofiletype(Enum):
    """
    Clockprofiletype

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


class Clockqualityaccuracytype(Enum):
    """
    Clockqualityaccuracytype

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


class Clockroletype(Enum):
    """
    Clockroletype

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


class Clockstatetype(Enum):
    """
    Clockstatetype

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


class Clocktimesourcetype(Enum):
    """
    Clocktimesourcetype

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


class Clocktxmodetype(Enum):
    """
    Clocktxmodetype

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


class Clocktype(Enum):
    """
    Clocktype

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



class CiscoPtpMib(Entity):
    """
    
    
    .. attribute:: ciscoptpmibsysteminfo
    
    	
    	**type**\:   :py:class:`Ciscoptpmibsysteminfo <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Ciscoptpmibsysteminfo>`
    
    .. attribute:: cptpclockcurrentdstable
    
    	Table of information about the PTP clock Current Datasets for all domains
    	**type**\:   :py:class:`Cptpclockcurrentdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockcurrentdstable>`
    
    .. attribute:: cptpclockdefaultdstable
    
    	Table of information about the PTP clock Default Datasets for all domains
    	**type**\:   :py:class:`Cptpclockdefaultdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockdefaultdstable>`
    
    .. attribute:: cptpclocknodetable
    
    	Table of information about the PTP system for a given domain
    	**type**\:   :py:class:`Cptpclocknodetable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocknodetable>`
    
    .. attribute:: cptpclockparentdstable
    
    	Table of information about the PTP clock Parent Datasets for all domains
    	**type**\:   :py:class:`Cptpclockparentdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockparentdstable>`
    
    .. attribute:: cptpclockportassociatetable
    
    	Table of information about a given port's associated ports.  For a master port \- multiple slave ports which have established sessions with the current master port.   For a slave port \- the list of masters available for a given slave port.   Session information (pkts, errors) to be displayed based on availability and scenario
    	**type**\:   :py:class:`Cptpclockportassociatetable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockportassociatetable>`
    
    .. attribute:: cptpclockportdstable
    
    	Table of information about the clock ports dataset for a particular domain
    	**type**\:   :py:class:`Cptpclockportdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockportdstable>`
    
    .. attribute:: cptpclockportrunningtable
    
    	Table of information about the clock ports running dataset for a particular domain
    	**type**\:   :py:class:`Cptpclockportrunningtable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockportrunningtable>`
    
    .. attribute:: cptpclockporttable
    
    	Table of information about the clock ports for a particular domain
    	**type**\:   :py:class:`Cptpclockporttable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockporttable>`
    
    .. attribute:: cptpclockporttransdstable
    
    	Table of information about the Transparent clock ports running dataset for a particular domain
    	**type**\:   :py:class:`Cptpclockporttransdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockporttransdstable>`
    
    .. attribute:: cptpclockrunningtable
    
    	Table of information about the PTP clock Running Datasets for all domains
    	**type**\:   :py:class:`Cptpclockrunningtable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockrunningtable>`
    
    .. attribute:: cptpclocktimepropertiesdstable
    
    	Table of information about the PTP clock Timeproperties Datasets for all domains
    	**type**\:   :py:class:`Cptpclocktimepropertiesdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocktimepropertiesdstable>`
    
    .. attribute:: cptpclocktransdefaultdstable
    
    	Table of information about the PTP Transparent clock Default Datasets for all domains
    	**type**\:   :py:class:`Cptpclocktransdefaultdstable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocktransdefaultdstable>`
    
    .. attribute:: cptpsystemdomaintable
    
    	Table of information about the PTP system for all clock modes \-\- ordinary, boundary or transparent
    	**type**\:   :py:class:`Cptpsystemdomaintable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpsystemdomaintable>`
    
    .. attribute:: cptpsystemtable
    
    	Table of count information about the PTP system for all domains
    	**type**\:   :py:class:`Cptpsystemtable <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpsystemtable>`
    
    

    """

    _prefix = 'CISCO-PTP-MIB'
    _revision = '2011-01-28'

    def __init__(self):
        super(CiscoPtpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PTP-MIB"
        self.yang_parent_name = "CISCO-PTP-MIB"

        self.ciscoptpmibsysteminfo = CiscoPtpMib.Ciscoptpmibsysteminfo()
        self.ciscoptpmibsysteminfo.parent = self
        self._children_name_map["ciscoptpmibsysteminfo"] = "ciscoPtpMIBSystemInfo"
        self._children_yang_names.add("ciscoPtpMIBSystemInfo")

        self.cptpclockcurrentdstable = CiscoPtpMib.Cptpclockcurrentdstable()
        self.cptpclockcurrentdstable.parent = self
        self._children_name_map["cptpclockcurrentdstable"] = "cPtpClockCurrentDSTable"
        self._children_yang_names.add("cPtpClockCurrentDSTable")

        self.cptpclockdefaultdstable = CiscoPtpMib.Cptpclockdefaultdstable()
        self.cptpclockdefaultdstable.parent = self
        self._children_name_map["cptpclockdefaultdstable"] = "cPtpClockDefaultDSTable"
        self._children_yang_names.add("cPtpClockDefaultDSTable")

        self.cptpclocknodetable = CiscoPtpMib.Cptpclocknodetable()
        self.cptpclocknodetable.parent = self
        self._children_name_map["cptpclocknodetable"] = "cPtpClockNodeTable"
        self._children_yang_names.add("cPtpClockNodeTable")

        self.cptpclockparentdstable = CiscoPtpMib.Cptpclockparentdstable()
        self.cptpclockparentdstable.parent = self
        self._children_name_map["cptpclockparentdstable"] = "cPtpClockParentDSTable"
        self._children_yang_names.add("cPtpClockParentDSTable")

        self.cptpclockportassociatetable = CiscoPtpMib.Cptpclockportassociatetable()
        self.cptpclockportassociatetable.parent = self
        self._children_name_map["cptpclockportassociatetable"] = "cPtpClockPortAssociateTable"
        self._children_yang_names.add("cPtpClockPortAssociateTable")

        self.cptpclockportdstable = CiscoPtpMib.Cptpclockportdstable()
        self.cptpclockportdstable.parent = self
        self._children_name_map["cptpclockportdstable"] = "cPtpClockPortDSTable"
        self._children_yang_names.add("cPtpClockPortDSTable")

        self.cptpclockportrunningtable = CiscoPtpMib.Cptpclockportrunningtable()
        self.cptpclockportrunningtable.parent = self
        self._children_name_map["cptpclockportrunningtable"] = "cPtpClockPortRunningTable"
        self._children_yang_names.add("cPtpClockPortRunningTable")

        self.cptpclockporttable = CiscoPtpMib.Cptpclockporttable()
        self.cptpclockporttable.parent = self
        self._children_name_map["cptpclockporttable"] = "cPtpClockPortTable"
        self._children_yang_names.add("cPtpClockPortTable")

        self.cptpclockporttransdstable = CiscoPtpMib.Cptpclockporttransdstable()
        self.cptpclockporttransdstable.parent = self
        self._children_name_map["cptpclockporttransdstable"] = "cPtpClockPortTransDSTable"
        self._children_yang_names.add("cPtpClockPortTransDSTable")

        self.cptpclockrunningtable = CiscoPtpMib.Cptpclockrunningtable()
        self.cptpclockrunningtable.parent = self
        self._children_name_map["cptpclockrunningtable"] = "cPtpClockRunningTable"
        self._children_yang_names.add("cPtpClockRunningTable")

        self.cptpclocktimepropertiesdstable = CiscoPtpMib.Cptpclocktimepropertiesdstable()
        self.cptpclocktimepropertiesdstable.parent = self
        self._children_name_map["cptpclocktimepropertiesdstable"] = "cPtpClockTimePropertiesDSTable"
        self._children_yang_names.add("cPtpClockTimePropertiesDSTable")

        self.cptpclocktransdefaultdstable = CiscoPtpMib.Cptpclocktransdefaultdstable()
        self.cptpclocktransdefaultdstable.parent = self
        self._children_name_map["cptpclocktransdefaultdstable"] = "cPtpClockTransDefaultDSTable"
        self._children_yang_names.add("cPtpClockTransDefaultDSTable")

        self.cptpsystemdomaintable = CiscoPtpMib.Cptpsystemdomaintable()
        self.cptpsystemdomaintable.parent = self
        self._children_name_map["cptpsystemdomaintable"] = "cPtpSystemDomainTable"
        self._children_yang_names.add("cPtpSystemDomainTable")

        self.cptpsystemtable = CiscoPtpMib.Cptpsystemtable()
        self.cptpsystemtable.parent = self
        self._children_name_map["cptpsystemtable"] = "cPtpSystemTable"
        self._children_yang_names.add("cPtpSystemTable")


    class Ciscoptpmibsysteminfo(Entity):
        """
        
        
        .. attribute:: cptpsystemprofile
        
        	This object specifies the PTP Profile implemented on the system
        	**type**\:   :py:class:`Clockprofiletype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockprofiletype>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Ciscoptpmibsysteminfo, self).__init__()

            self.yang_name = "ciscoPtpMIBSystemInfo"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpsystemprofile = YLeaf(YType.enumeration, "cPtpSystemProfile")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cptpsystemprofile") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Ciscoptpmibsysteminfo, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Ciscoptpmibsysteminfo, self).__setattr__(name, value)

        def has_data(self):
            return self.cptpsystemprofile.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cptpsystemprofile.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoPtpMIBSystemInfo" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cptpsystemprofile.is_set or self.cptpsystemprofile.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cptpsystemprofile.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpSystemProfile"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cPtpSystemProfile"):
                self.cptpsystemprofile = value
                self.cptpsystemprofile.value_namespace = name_space
                self.cptpsystemprofile.value_namespace_prefix = name_space_prefix


    class Cptpsystemtable(Entity):
        """
        Table of count information about the PTP system for all
        domains.
        
        .. attribute:: cptpsystementry
        
        	An entry in the table, containing count information about a single domain. New row entries are added when the PTP clock for this domain is configured, while the unconfiguration of the PTP clock removes it
        	**type**\: list of    :py:class:`Cptpsystementry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpsystemtable.Cptpsystementry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpsystemtable, self).__init__()

            self.yang_name = "cPtpSystemTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpsystementry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpsystemtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpsystemtable, self).__setattr__(name, value)


        class Cptpsystementry(Entity):
            """
            An entry in the table, containing count information about a
            single domain. New row entries are added when the PTP clock for
            this domain is configured, while the unconfiguration of the PTP
            clock removes it.
            
            .. attribute:: cptpdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices. The Clock Domain is a logical group of clocks and devices that synchronize with each other using the PTP protocol.   0           Default domain 1           Alternate domain 1 2           Alternate domain 2 3           Alternate domain 3 4 \- 127     User\-defined domains 128 \- 255   Reserved
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpinstanceindex  <key>
            
            	This object specifies the instance of the Clock for this domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpdomainclockportphysicalinterfacestotal
            
            	This object specifies the total number of clock port Physical interfaces configured within a domain instance for PTP communications
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: physical ports
            
            .. attribute:: cptpdomainclockportstotal
            
            	This object specifies the total number of clock ports configured within a domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: ptp ports
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpsystemtable.Cptpsystementry, self).__init__()

                self.yang_name = "cPtpSystemEntry"
                self.yang_parent_name = "cPtpSystemTable"

                self.cptpdomainindex = YLeaf(YType.uint32, "cPtpDomainIndex")

                self.cptpinstanceindex = YLeaf(YType.uint32, "cPtpInstanceIndex")

                self.cptpdomainclockportphysicalinterfacestotal = YLeaf(YType.uint32, "cPtpDomainClockPortPhysicalInterfacesTotal")

                self.cptpdomainclockportstotal = YLeaf(YType.uint32, "cPtpDomainClockPortsTotal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpdomainindex",
                                "cptpinstanceindex",
                                "cptpdomainclockportphysicalinterfacestotal",
                                "cptpdomainclockportstotal") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpsystemtable.Cptpsystementry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpsystemtable.Cptpsystementry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpdomainindex.is_set or
                    self.cptpinstanceindex.is_set or
                    self.cptpdomainclockportphysicalinterfacestotal.is_set or
                    self.cptpdomainclockportstotal.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpdomainindex.yfilter != YFilter.not_set or
                    self.cptpinstanceindex.yfilter != YFilter.not_set or
                    self.cptpdomainclockportphysicalinterfacestotal.yfilter != YFilter.not_set or
                    self.cptpdomainclockportstotal.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpSystemEntry" + "[cPtpDomainIndex='" + self.cptpdomainindex.get() + "']" + "[cPtpInstanceIndex='" + self.cptpinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpSystemTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpdomainindex.is_set or self.cptpdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpdomainindex.get_name_leafdata())
                if (self.cptpinstanceindex.is_set or self.cptpinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpinstanceindex.get_name_leafdata())
                if (self.cptpdomainclockportphysicalinterfacestotal.is_set or self.cptpdomainclockportphysicalinterfacestotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpdomainclockportphysicalinterfacestotal.get_name_leafdata())
                if (self.cptpdomainclockportstotal.is_set or self.cptpdomainclockportstotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpdomainclockportstotal.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpDomainIndex" or name == "cPtpInstanceIndex" or name == "cPtpDomainClockPortPhysicalInterfacesTotal" or name == "cPtpDomainClockPortsTotal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpDomainIndex"):
                    self.cptpdomainindex = value
                    self.cptpdomainindex.value_namespace = name_space
                    self.cptpdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpInstanceIndex"):
                    self.cptpinstanceindex = value
                    self.cptpinstanceindex.value_namespace = name_space
                    self.cptpinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpDomainClockPortPhysicalInterfacesTotal"):
                    self.cptpdomainclockportphysicalinterfacestotal = value
                    self.cptpdomainclockportphysicalinterfacestotal.value_namespace = name_space
                    self.cptpdomainclockportphysicalinterfacestotal.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpDomainClockPortsTotal"):
                    self.cptpdomainclockportstotal = value
                    self.cptpdomainclockportstotal.value_namespace = name_space
                    self.cptpdomainclockportstotal.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpsystementry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpsystementry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpSystemTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpSystemEntry"):
                for c in self.cptpsystementry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpsystemtable.Cptpsystementry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpsystementry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpSystemEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpsystemdomaintable(Entity):
        """
        Table of information about the PTP system for all clock modes
        \-\- ordinary, boundary or transparent.
        
        .. attribute:: cptpsystemdomainentry
        
        	An entry in the table, containing information about a single clock mode for the PTP system. A row entry gets added when PTP clocks are configured on the router
        	**type**\: list of    :py:class:`Cptpsystemdomainentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpsystemdomaintable, self).__init__()

            self.yang_name = "cPtpSystemDomainTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpsystemdomainentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpsystemdomaintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpsystemdomaintable, self).__setattr__(name, value)


        class Cptpsystemdomainentry(Entity):
            """
            An entry in the table, containing information about a single
            clock mode for the PTP system. A row entry gets added when PTP
            clocks are configured on the router.
            
            .. attribute:: cptpsystemdomainclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpsystemdomaintotals
            
            	This object specifies the  total number of PTP domains for this particular clock type configured in this node
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: domains
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry, self).__init__()

                self.yang_name = "cPtpSystemDomainEntry"
                self.yang_parent_name = "cPtpSystemDomainTable"

                self.cptpsystemdomainclocktypeindex = YLeaf(YType.enumeration, "cPtpSystemDomainClockTypeIndex")

                self.cptpsystemdomaintotals = YLeaf(YType.uint32, "cPtpSystemDomainTotals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpsystemdomainclocktypeindex",
                                "cptpsystemdomaintotals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpsystemdomainclocktypeindex.is_set or
                    self.cptpsystemdomaintotals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpsystemdomainclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpsystemdomaintotals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpSystemDomainEntry" + "[cPtpSystemDomainClockTypeIndex='" + self.cptpsystemdomainclocktypeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpSystemDomainTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpsystemdomainclocktypeindex.is_set or self.cptpsystemdomainclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpsystemdomainclocktypeindex.get_name_leafdata())
                if (self.cptpsystemdomaintotals.is_set or self.cptpsystemdomaintotals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpsystemdomaintotals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpSystemDomainClockTypeIndex" or name == "cPtpSystemDomainTotals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpSystemDomainClockTypeIndex"):
                    self.cptpsystemdomainclocktypeindex = value
                    self.cptpsystemdomainclocktypeindex.value_namespace = name_space
                    self.cptpsystemdomainclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpSystemDomainTotals"):
                    self.cptpsystemdomaintotals = value
                    self.cptpsystemdomaintotals.value_namespace = name_space
                    self.cptpsystemdomaintotals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpsystemdomainentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpsystemdomainentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpSystemDomainTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpSystemDomainEntry"):
                for c in self.cptpsystemdomainentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpsystemdomainentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpSystemDomainEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclocknodetable(Entity):
        """
        Table of information about the PTP system for a given domain.
        
        .. attribute:: cptpclocknodeentry
        
        	An entry in the table, containing information about a single domain. A entry is added when a new PTP clock domain is configured on the router
        	**type**\: list of    :py:class:`Cptpclocknodeentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclocknodetable, self).__init__()

            self.yang_name = "cPtpClockNodeTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclocknodeentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclocknodetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclocknodetable, self).__setattr__(name, value)


        class Cptpclocknodeentry(Entity):
            """
            An entry in the table, containing information about a single
            domain. A entry is added when a new PTP clock domain is
            configured on the router.
            
            .. attribute:: cptpclockdomainindex  <key>
            
            	This object specifies the  domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockinstanceindex  <key>
            
            	This object specifies the instance of the Clock for this clock type for the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockinput1ppsenabled
            
            	This object specifies whether the node is enabled for PTP input clocking using the 1pps interface
            	**type**\:  bool
            
            .. attribute:: cptpclockinput1ppsinterface
            
            	This object specifies the 1pps interface used for PTP input clocking
            	**type**\:  str
            
            .. attribute:: cptpclockinputfrequencyenabled
            
            	This object specifies whether enabled for Frequency input using the 1.544 Mhz, 2.048 Mhz, or 10Mhz timing interface
            	**type**\:  bool
            
            .. attribute:: cptpclockoutput1ppsenabled
            
            	This object specifies whether the node is enabled for PTP input clocking using the 1pps interface
            	**type**\:  bool
            
            .. attribute:: cptpclockoutput1ppsinterface
            
            	This object specifies the 1pps interface used for PTP output clocking
            	**type**\:  str
            
            .. attribute:: cptpclockoutput1ppsoffsetenabled
            
            	This object specifies whether an offset is configured in order to compensate for a known phase error such as network asymmetry
            	**type**\:  bool
            
            .. attribute:: cptpclockoutput1ppsoffsetnegative
            
            	This object specifies whether the added (fixed) offset to the 1pps output is negative or not.  When object returns TRUE the offset is negative and when object returns FALSE the offset is positive
            	**type**\:  bool
            
            .. attribute:: cptpclockoutput1ppsoffsetvalue
            
            	This object specifies the fixed offset value configured to be added for the 1pps output
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclocktodenabled
            
            	This object specifies whether the node is enabled for TOD
            	**type**\:  bool
            
            .. attribute:: cptpclocktodinterface
            
            	This object specifies the interface used for PTP TOD
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry, self).__init__()

                self.yang_name = "cPtpClockNodeEntry"
                self.yang_parent_name = "cPtpClockNodeTable"

                self.cptpclockdomainindex = YLeaf(YType.uint32, "cPtpClockDomainIndex")

                self.cptpclocktypeindex = YLeaf(YType.enumeration, "cPtpClockTypeIndex")

                self.cptpclockinstanceindex = YLeaf(YType.uint32, "cPtpClockInstanceIndex")

                self.cptpclockinput1ppsenabled = YLeaf(YType.boolean, "cPtpClockInput1ppsEnabled")

                self.cptpclockinput1ppsinterface = YLeaf(YType.str, "cPtpClockInput1ppsInterface")

                self.cptpclockinputfrequencyenabled = YLeaf(YType.boolean, "cPtpClockInputFrequencyEnabled")

                self.cptpclockoutput1ppsenabled = YLeaf(YType.boolean, "cPtpClockOutput1ppsEnabled")

                self.cptpclockoutput1ppsinterface = YLeaf(YType.str, "cPtpClockOutput1ppsInterface")

                self.cptpclockoutput1ppsoffsetenabled = YLeaf(YType.boolean, "cPtpClockOutput1ppsOffsetEnabled")

                self.cptpclockoutput1ppsoffsetnegative = YLeaf(YType.boolean, "cPtpClockOutput1ppsOffsetNegative")

                self.cptpclockoutput1ppsoffsetvalue = YLeaf(YType.uint32, "cPtpClockOutput1ppsOffsetValue")

                self.cptpclocktodenabled = YLeaf(YType.boolean, "cPtpClockTODEnabled")

                self.cptpclocktodinterface = YLeaf(YType.str, "cPtpClockTODInterface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockdomainindex",
                                "cptpclocktypeindex",
                                "cptpclockinstanceindex",
                                "cptpclockinput1ppsenabled",
                                "cptpclockinput1ppsinterface",
                                "cptpclockinputfrequencyenabled",
                                "cptpclockoutput1ppsenabled",
                                "cptpclockoutput1ppsinterface",
                                "cptpclockoutput1ppsoffsetenabled",
                                "cptpclockoutput1ppsoffsetnegative",
                                "cptpclockoutput1ppsoffsetvalue",
                                "cptpclocktodenabled",
                                "cptpclocktodinterface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockdomainindex.is_set or
                    self.cptpclocktypeindex.is_set or
                    self.cptpclockinstanceindex.is_set or
                    self.cptpclockinput1ppsenabled.is_set or
                    self.cptpclockinput1ppsinterface.is_set or
                    self.cptpclockinputfrequencyenabled.is_set or
                    self.cptpclockoutput1ppsenabled.is_set or
                    self.cptpclockoutput1ppsinterface.is_set or
                    self.cptpclockoutput1ppsoffsetenabled.is_set or
                    self.cptpclockoutput1ppsoffsetnegative.is_set or
                    self.cptpclockoutput1ppsoffsetvalue.is_set or
                    self.cptpclocktodenabled.is_set or
                    self.cptpclocktodinterface.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockdomainindex.yfilter != YFilter.not_set or
                    self.cptpclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockinput1ppsenabled.yfilter != YFilter.not_set or
                    self.cptpclockinput1ppsinterface.yfilter != YFilter.not_set or
                    self.cptpclockinputfrequencyenabled.yfilter != YFilter.not_set or
                    self.cptpclockoutput1ppsenabled.yfilter != YFilter.not_set or
                    self.cptpclockoutput1ppsinterface.yfilter != YFilter.not_set or
                    self.cptpclockoutput1ppsoffsetenabled.yfilter != YFilter.not_set or
                    self.cptpclockoutput1ppsoffsetnegative.yfilter != YFilter.not_set or
                    self.cptpclockoutput1ppsoffsetvalue.yfilter != YFilter.not_set or
                    self.cptpclocktodenabled.yfilter != YFilter.not_set or
                    self.cptpclocktodinterface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockNodeEntry" + "[cPtpClockDomainIndex='" + self.cptpclockdomainindex.get() + "']" + "[cPtpClockTypeIndex='" + self.cptpclocktypeindex.get() + "']" + "[cPtpClockInstanceIndex='" + self.cptpclockinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockNodeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockdomainindex.is_set or self.cptpclockdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdomainindex.get_name_leafdata())
                if (self.cptpclocktypeindex.is_set or self.cptpclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktypeindex.get_name_leafdata())
                if (self.cptpclockinstanceindex.is_set or self.cptpclockinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockinstanceindex.get_name_leafdata())
                if (self.cptpclockinput1ppsenabled.is_set or self.cptpclockinput1ppsenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockinput1ppsenabled.get_name_leafdata())
                if (self.cptpclockinput1ppsinterface.is_set or self.cptpclockinput1ppsinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockinput1ppsinterface.get_name_leafdata())
                if (self.cptpclockinputfrequencyenabled.is_set or self.cptpclockinputfrequencyenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockinputfrequencyenabled.get_name_leafdata())
                if (self.cptpclockoutput1ppsenabled.is_set or self.cptpclockoutput1ppsenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockoutput1ppsenabled.get_name_leafdata())
                if (self.cptpclockoutput1ppsinterface.is_set or self.cptpclockoutput1ppsinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockoutput1ppsinterface.get_name_leafdata())
                if (self.cptpclockoutput1ppsoffsetenabled.is_set or self.cptpclockoutput1ppsoffsetenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockoutput1ppsoffsetenabled.get_name_leafdata())
                if (self.cptpclockoutput1ppsoffsetnegative.is_set or self.cptpclockoutput1ppsoffsetnegative.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockoutput1ppsoffsetnegative.get_name_leafdata())
                if (self.cptpclockoutput1ppsoffsetvalue.is_set or self.cptpclockoutput1ppsoffsetvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockoutput1ppsoffsetvalue.get_name_leafdata())
                if (self.cptpclocktodenabled.is_set or self.cptpclocktodenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktodenabled.get_name_leafdata())
                if (self.cptpclocktodinterface.is_set or self.cptpclocktodinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktodinterface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockDomainIndex" or name == "cPtpClockTypeIndex" or name == "cPtpClockInstanceIndex" or name == "cPtpClockInput1ppsEnabled" or name == "cPtpClockInput1ppsInterface" or name == "cPtpClockInputFrequencyEnabled" or name == "cPtpClockOutput1ppsEnabled" or name == "cPtpClockOutput1ppsInterface" or name == "cPtpClockOutput1ppsOffsetEnabled" or name == "cPtpClockOutput1ppsOffsetNegative" or name == "cPtpClockOutput1ppsOffsetValue" or name == "cPtpClockTODEnabled" or name == "cPtpClockTODInterface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockDomainIndex"):
                    self.cptpclockdomainindex = value
                    self.cptpclockdomainindex.value_namespace = name_space
                    self.cptpclockdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTypeIndex"):
                    self.cptpclocktypeindex = value
                    self.cptpclocktypeindex.value_namespace = name_space
                    self.cptpclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockInstanceIndex"):
                    self.cptpclockinstanceindex = value
                    self.cptpclockinstanceindex.value_namespace = name_space
                    self.cptpclockinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockInput1ppsEnabled"):
                    self.cptpclockinput1ppsenabled = value
                    self.cptpclockinput1ppsenabled.value_namespace = name_space
                    self.cptpclockinput1ppsenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockInput1ppsInterface"):
                    self.cptpclockinput1ppsinterface = value
                    self.cptpclockinput1ppsinterface.value_namespace = name_space
                    self.cptpclockinput1ppsinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockInputFrequencyEnabled"):
                    self.cptpclockinputfrequencyenabled = value
                    self.cptpclockinputfrequencyenabled.value_namespace = name_space
                    self.cptpclockinputfrequencyenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockOutput1ppsEnabled"):
                    self.cptpclockoutput1ppsenabled = value
                    self.cptpclockoutput1ppsenabled.value_namespace = name_space
                    self.cptpclockoutput1ppsenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockOutput1ppsInterface"):
                    self.cptpclockoutput1ppsinterface = value
                    self.cptpclockoutput1ppsinterface.value_namespace = name_space
                    self.cptpclockoutput1ppsinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockOutput1ppsOffsetEnabled"):
                    self.cptpclockoutput1ppsoffsetenabled = value
                    self.cptpclockoutput1ppsoffsetenabled.value_namespace = name_space
                    self.cptpclockoutput1ppsoffsetenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockOutput1ppsOffsetNegative"):
                    self.cptpclockoutput1ppsoffsetnegative = value
                    self.cptpclockoutput1ppsoffsetnegative.value_namespace = name_space
                    self.cptpclockoutput1ppsoffsetnegative.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockOutput1ppsOffsetValue"):
                    self.cptpclockoutput1ppsoffsetvalue = value
                    self.cptpclockoutput1ppsoffsetvalue.value_namespace = name_space
                    self.cptpclockoutput1ppsoffsetvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTODEnabled"):
                    self.cptpclocktodenabled = value
                    self.cptpclocktodenabled.value_namespace = name_space
                    self.cptpclocktodenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTODInterface"):
                    self.cptpclocktodinterface = value
                    self.cptpclocktodinterface.value_namespace = name_space
                    self.cptpclocktodinterface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclocknodeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclocknodeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockNodeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockNodeEntry"):
                for c in self.cptpclocknodeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclocknodeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockNodeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockcurrentdstable(Entity):
        """
        Table of information about the PTP clock Current Datasets for
        all domains.
        
        .. attribute:: cptpclockcurrentdsentry
        
        	An entry in the table, containing information about a single PTP clock Current Datasets for a domain
        	**type**\: list of    :py:class:`Cptpclockcurrentdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockcurrentdstable, self).__init__()

            self.yang_name = "cPtpClockCurrentDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockcurrentdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockcurrentdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockcurrentdstable, self).__setattr__(name, value)


        class Cptpclockcurrentdsentry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock Current Datasets for a domain.
            
            .. attribute:: cptpclockcurrentdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockcurrentdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockcurrentdsinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockcurrentdsmeanpathdelay
            
            	This object specifies the current clock dataset MeanPathDelay value.  The mean path delay between a pair of ports as measure by the delay request\-response mechanism
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cptpclockcurrentdsoffsetfrommaster
            
            	This object specifies the current clock dataset ClockOffset value. The value of the computation of the offset in time between a slave and a master clock
            	**type**\:  str
            
            	**length:** 1..255
            
            	**units**\: Time Interval
            
            .. attribute:: cptpclockcurrentdsstepsremoved
            
            	The current clock dataset StepsRemoved value.  This object specifies the distance measured by the number of Boundary clocks between the local clock and the Foreign master as indicated in the stepsRemoved field of Announce messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: steps
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry, self).__init__()

                self.yang_name = "cPtpClockCurrentDSEntry"
                self.yang_parent_name = "cPtpClockCurrentDSTable"

                self.cptpclockcurrentdsdomainindex = YLeaf(YType.uint32, "cPtpClockCurrentDSDomainIndex")

                self.cptpclockcurrentdsclocktypeindex = YLeaf(YType.enumeration, "cPtpClockCurrentDSClockTypeIndex")

                self.cptpclockcurrentdsinstanceindex = YLeaf(YType.uint32, "cPtpClockCurrentDSInstanceIndex")

                self.cptpclockcurrentdsmeanpathdelay = YLeaf(YType.str, "cPtpClockCurrentDSMeanPathDelay")

                self.cptpclockcurrentdsoffsetfrommaster = YLeaf(YType.str, "cPtpClockCurrentDSOffsetFromMaster")

                self.cptpclockcurrentdsstepsremoved = YLeaf(YType.uint32, "cPtpClockCurrentDSStepsRemoved")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockcurrentdsdomainindex",
                                "cptpclockcurrentdsclocktypeindex",
                                "cptpclockcurrentdsinstanceindex",
                                "cptpclockcurrentdsmeanpathdelay",
                                "cptpclockcurrentdsoffsetfrommaster",
                                "cptpclockcurrentdsstepsremoved") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockcurrentdsdomainindex.is_set or
                    self.cptpclockcurrentdsclocktypeindex.is_set or
                    self.cptpclockcurrentdsinstanceindex.is_set or
                    self.cptpclockcurrentdsmeanpathdelay.is_set or
                    self.cptpclockcurrentdsoffsetfrommaster.is_set or
                    self.cptpclockcurrentdsstepsremoved.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockcurrentdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockcurrentdsclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockcurrentdsinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockcurrentdsmeanpathdelay.yfilter != YFilter.not_set or
                    self.cptpclockcurrentdsoffsetfrommaster.yfilter != YFilter.not_set or
                    self.cptpclockcurrentdsstepsremoved.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockCurrentDSEntry" + "[cPtpClockCurrentDSDomainIndex='" + self.cptpclockcurrentdsdomainindex.get() + "']" + "[cPtpClockCurrentDSClockTypeIndex='" + self.cptpclockcurrentdsclocktypeindex.get() + "']" + "[cPtpClockCurrentDSInstanceIndex='" + self.cptpclockcurrentdsinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockCurrentDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockcurrentdsdomainindex.is_set or self.cptpclockcurrentdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockcurrentdsdomainindex.get_name_leafdata())
                if (self.cptpclockcurrentdsclocktypeindex.is_set or self.cptpclockcurrentdsclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockcurrentdsclocktypeindex.get_name_leafdata())
                if (self.cptpclockcurrentdsinstanceindex.is_set or self.cptpclockcurrentdsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockcurrentdsinstanceindex.get_name_leafdata())
                if (self.cptpclockcurrentdsmeanpathdelay.is_set or self.cptpclockcurrentdsmeanpathdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockcurrentdsmeanpathdelay.get_name_leafdata())
                if (self.cptpclockcurrentdsoffsetfrommaster.is_set or self.cptpclockcurrentdsoffsetfrommaster.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockcurrentdsoffsetfrommaster.get_name_leafdata())
                if (self.cptpclockcurrentdsstepsremoved.is_set or self.cptpclockcurrentdsstepsremoved.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockcurrentdsstepsremoved.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockCurrentDSDomainIndex" or name == "cPtpClockCurrentDSClockTypeIndex" or name == "cPtpClockCurrentDSInstanceIndex" or name == "cPtpClockCurrentDSMeanPathDelay" or name == "cPtpClockCurrentDSOffsetFromMaster" or name == "cPtpClockCurrentDSStepsRemoved"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockCurrentDSDomainIndex"):
                    self.cptpclockcurrentdsdomainindex = value
                    self.cptpclockcurrentdsdomainindex.value_namespace = name_space
                    self.cptpclockcurrentdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockCurrentDSClockTypeIndex"):
                    self.cptpclockcurrentdsclocktypeindex = value
                    self.cptpclockcurrentdsclocktypeindex.value_namespace = name_space
                    self.cptpclockcurrentdsclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockCurrentDSInstanceIndex"):
                    self.cptpclockcurrentdsinstanceindex = value
                    self.cptpclockcurrentdsinstanceindex.value_namespace = name_space
                    self.cptpclockcurrentdsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockCurrentDSMeanPathDelay"):
                    self.cptpclockcurrentdsmeanpathdelay = value
                    self.cptpclockcurrentdsmeanpathdelay.value_namespace = name_space
                    self.cptpclockcurrentdsmeanpathdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockCurrentDSOffsetFromMaster"):
                    self.cptpclockcurrentdsoffsetfrommaster = value
                    self.cptpclockcurrentdsoffsetfrommaster.value_namespace = name_space
                    self.cptpclockcurrentdsoffsetfrommaster.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockCurrentDSStepsRemoved"):
                    self.cptpclockcurrentdsstepsremoved = value
                    self.cptpclockcurrentdsstepsremoved.value_namespace = name_space
                    self.cptpclockcurrentdsstepsremoved.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockcurrentdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockcurrentdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockCurrentDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockCurrentDSEntry"):
                for c in self.cptpclockcurrentdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockcurrentdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockCurrentDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockparentdstable(Entity):
        """
        Table of information about the PTP clock Parent Datasets for
        all domains.
        
        .. attribute:: cptpclockparentdsentry
        
        	An entry in the table, containing information about a single PTP clock Parent Datasets for a domain
        	**type**\: list of    :py:class:`Cptpclockparentdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockparentdstable, self).__init__()

            self.yang_name = "cPtpClockParentDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockparentdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockparentdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockparentdstable, self).__setattr__(name, value)


        class Cptpclockparentdsentry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock Parent Datasets for a domain.
            
            .. attribute:: cptpclockparentdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockparentdsinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsclockphchrate
            
            	This object specifies the clock's parent dataset ParentClockPhaseChangeRate value.  This value is an estimate of the parent clocks phase change rate as measured by the slave clock
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockparentdsgmclockidentity
            
            	This object specifies the parent dataset Grandmaster clock identity
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cptpclockparentdsgmclockpriority1
            
            	This object specifies the parent dataset Grandmaster clock priority1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockparentdsgmclockpriority2
            
            	This object specifies the parent dataset grandmaster clock priority2
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockparentdsgmclockqualityaccuracy
            
            	This object specifies the parent dataset grandmaster clock quality accuracy
            	**type**\:   :py:class:`Clockqualityaccuracytype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockqualityaccuracytype>`
            
            .. attribute:: cptpclockparentdsgmclockqualityclass
            
            	This object specifies the parent dataset grandmaster clock quality class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsgmclockqualityoffset
            
            	This object specifies the parent dataset grandmaster clock quality offset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclockparentdsoffset
            
            	This object specifies the Parent Dataset ParentOffsetScaledLogVariance value.  This value is the variance of the parent clocks phase as measured by the local clock
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: cptpclockparentdsparentportidentity
            
            	This object specifies the value of portIdentity of the port on the master that issues the Sync messages used in synchronizing this clock
            	**type**\:  str
            
            .. attribute:: cptpclockparentdsparentstats
            
            	This object specifies the Parent Dataset ParentStats value.  This value indicates whether the values of ParentDSOffset and ParentDSClockPhChRate have been measured and are valid. A TRUE value shall indicate valid data
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry, self).__init__()

                self.yang_name = "cPtpClockParentDSEntry"
                self.yang_parent_name = "cPtpClockParentDSTable"

                self.cptpclockparentdsdomainindex = YLeaf(YType.uint32, "cPtpClockParentDSDomainIndex")

                self.cptpclockparentdsclocktypeindex = YLeaf(YType.enumeration, "cPtpClockParentDSClockTypeIndex")

                self.cptpclockparentdsinstanceindex = YLeaf(YType.uint32, "cPtpClockParentDSInstanceIndex")

                self.cptpclockparentdsclockphchrate = YLeaf(YType.int32, "cPtpClockParentDSClockPhChRate")

                self.cptpclockparentdsgmclockidentity = YLeaf(YType.str, "cPtpClockParentDSGMClockIdentity")

                self.cptpclockparentdsgmclockpriority1 = YLeaf(YType.int32, "cPtpClockParentDSGMClockPriority1")

                self.cptpclockparentdsgmclockpriority2 = YLeaf(YType.int32, "cPtpClockParentDSGMClockPriority2")

                self.cptpclockparentdsgmclockqualityaccuracy = YLeaf(YType.enumeration, "cPtpClockParentDSGMClockQualityAccuracy")

                self.cptpclockparentdsgmclockqualityclass = YLeaf(YType.uint32, "cPtpClockParentDSGMClockQualityClass")

                self.cptpclockparentdsgmclockqualityoffset = YLeaf(YType.uint32, "cPtpClockParentDSGMClockQualityOffset")

                self.cptpclockparentdsoffset = YLeaf(YType.int32, "cPtpClockParentDSOffset")

                self.cptpclockparentdsparentportidentity = YLeaf(YType.str, "cPtpClockParentDSParentPortIdentity")

                self.cptpclockparentdsparentstats = YLeaf(YType.boolean, "cPtpClockParentDSParentStats")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockparentdsdomainindex",
                                "cptpclockparentdsclocktypeindex",
                                "cptpclockparentdsinstanceindex",
                                "cptpclockparentdsclockphchrate",
                                "cptpclockparentdsgmclockidentity",
                                "cptpclockparentdsgmclockpriority1",
                                "cptpclockparentdsgmclockpriority2",
                                "cptpclockparentdsgmclockqualityaccuracy",
                                "cptpclockparentdsgmclockqualityclass",
                                "cptpclockparentdsgmclockqualityoffset",
                                "cptpclockparentdsoffset",
                                "cptpclockparentdsparentportidentity",
                                "cptpclockparentdsparentstats") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockparentdsdomainindex.is_set or
                    self.cptpclockparentdsclocktypeindex.is_set or
                    self.cptpclockparentdsinstanceindex.is_set or
                    self.cptpclockparentdsclockphchrate.is_set or
                    self.cptpclockparentdsgmclockidentity.is_set or
                    self.cptpclockparentdsgmclockpriority1.is_set or
                    self.cptpclockparentdsgmclockpriority2.is_set or
                    self.cptpclockparentdsgmclockqualityaccuracy.is_set or
                    self.cptpclockparentdsgmclockqualityclass.is_set or
                    self.cptpclockparentdsgmclockqualityoffset.is_set or
                    self.cptpclockparentdsoffset.is_set or
                    self.cptpclockparentdsparentportidentity.is_set or
                    self.cptpclockparentdsparentstats.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockparentdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockparentdsclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockparentdsinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockparentdsclockphchrate.yfilter != YFilter.not_set or
                    self.cptpclockparentdsgmclockidentity.yfilter != YFilter.not_set or
                    self.cptpclockparentdsgmclockpriority1.yfilter != YFilter.not_set or
                    self.cptpclockparentdsgmclockpriority2.yfilter != YFilter.not_set or
                    self.cptpclockparentdsgmclockqualityaccuracy.yfilter != YFilter.not_set or
                    self.cptpclockparentdsgmclockqualityclass.yfilter != YFilter.not_set or
                    self.cptpclockparentdsgmclockqualityoffset.yfilter != YFilter.not_set or
                    self.cptpclockparentdsoffset.yfilter != YFilter.not_set or
                    self.cptpclockparentdsparentportidentity.yfilter != YFilter.not_set or
                    self.cptpclockparentdsparentstats.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockParentDSEntry" + "[cPtpClockParentDSDomainIndex='" + self.cptpclockparentdsdomainindex.get() + "']" + "[cPtpClockParentDSClockTypeIndex='" + self.cptpclockparentdsclocktypeindex.get() + "']" + "[cPtpClockParentDSInstanceIndex='" + self.cptpclockparentdsinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockParentDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockparentdsdomainindex.is_set or self.cptpclockparentdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsdomainindex.get_name_leafdata())
                if (self.cptpclockparentdsclocktypeindex.is_set or self.cptpclockparentdsclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsclocktypeindex.get_name_leafdata())
                if (self.cptpclockparentdsinstanceindex.is_set or self.cptpclockparentdsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsinstanceindex.get_name_leafdata())
                if (self.cptpclockparentdsclockphchrate.is_set or self.cptpclockparentdsclockphchrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsclockphchrate.get_name_leafdata())
                if (self.cptpclockparentdsgmclockidentity.is_set or self.cptpclockparentdsgmclockidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsgmclockidentity.get_name_leafdata())
                if (self.cptpclockparentdsgmclockpriority1.is_set or self.cptpclockparentdsgmclockpriority1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsgmclockpriority1.get_name_leafdata())
                if (self.cptpclockparentdsgmclockpriority2.is_set or self.cptpclockparentdsgmclockpriority2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsgmclockpriority2.get_name_leafdata())
                if (self.cptpclockparentdsgmclockqualityaccuracy.is_set or self.cptpclockparentdsgmclockqualityaccuracy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsgmclockqualityaccuracy.get_name_leafdata())
                if (self.cptpclockparentdsgmclockqualityclass.is_set or self.cptpclockparentdsgmclockqualityclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsgmclockqualityclass.get_name_leafdata())
                if (self.cptpclockparentdsgmclockqualityoffset.is_set or self.cptpclockparentdsgmclockqualityoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsgmclockqualityoffset.get_name_leafdata())
                if (self.cptpclockparentdsoffset.is_set or self.cptpclockparentdsoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsoffset.get_name_leafdata())
                if (self.cptpclockparentdsparentportidentity.is_set or self.cptpclockparentdsparentportidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsparentportidentity.get_name_leafdata())
                if (self.cptpclockparentdsparentstats.is_set or self.cptpclockparentdsparentstats.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockparentdsparentstats.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockParentDSDomainIndex" or name == "cPtpClockParentDSClockTypeIndex" or name == "cPtpClockParentDSInstanceIndex" or name == "cPtpClockParentDSClockPhChRate" or name == "cPtpClockParentDSGMClockIdentity" or name == "cPtpClockParentDSGMClockPriority1" or name == "cPtpClockParentDSGMClockPriority2" or name == "cPtpClockParentDSGMClockQualityAccuracy" or name == "cPtpClockParentDSGMClockQualityClass" or name == "cPtpClockParentDSGMClockQualityOffset" or name == "cPtpClockParentDSOffset" or name == "cPtpClockParentDSParentPortIdentity" or name == "cPtpClockParentDSParentStats"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockParentDSDomainIndex"):
                    self.cptpclockparentdsdomainindex = value
                    self.cptpclockparentdsdomainindex.value_namespace = name_space
                    self.cptpclockparentdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSClockTypeIndex"):
                    self.cptpclockparentdsclocktypeindex = value
                    self.cptpclockparentdsclocktypeindex.value_namespace = name_space
                    self.cptpclockparentdsclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSInstanceIndex"):
                    self.cptpclockparentdsinstanceindex = value
                    self.cptpclockparentdsinstanceindex.value_namespace = name_space
                    self.cptpclockparentdsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSClockPhChRate"):
                    self.cptpclockparentdsclockphchrate = value
                    self.cptpclockparentdsclockphchrate.value_namespace = name_space
                    self.cptpclockparentdsclockphchrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSGMClockIdentity"):
                    self.cptpclockparentdsgmclockidentity = value
                    self.cptpclockparentdsgmclockidentity.value_namespace = name_space
                    self.cptpclockparentdsgmclockidentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSGMClockPriority1"):
                    self.cptpclockparentdsgmclockpriority1 = value
                    self.cptpclockparentdsgmclockpriority1.value_namespace = name_space
                    self.cptpclockparentdsgmclockpriority1.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSGMClockPriority2"):
                    self.cptpclockparentdsgmclockpriority2 = value
                    self.cptpclockparentdsgmclockpriority2.value_namespace = name_space
                    self.cptpclockparentdsgmclockpriority2.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSGMClockQualityAccuracy"):
                    self.cptpclockparentdsgmclockqualityaccuracy = value
                    self.cptpclockparentdsgmclockqualityaccuracy.value_namespace = name_space
                    self.cptpclockparentdsgmclockqualityaccuracy.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSGMClockQualityClass"):
                    self.cptpclockparentdsgmclockqualityclass = value
                    self.cptpclockparentdsgmclockqualityclass.value_namespace = name_space
                    self.cptpclockparentdsgmclockqualityclass.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSGMClockQualityOffset"):
                    self.cptpclockparentdsgmclockqualityoffset = value
                    self.cptpclockparentdsgmclockqualityoffset.value_namespace = name_space
                    self.cptpclockparentdsgmclockqualityoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSOffset"):
                    self.cptpclockparentdsoffset = value
                    self.cptpclockparentdsoffset.value_namespace = name_space
                    self.cptpclockparentdsoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSParentPortIdentity"):
                    self.cptpclockparentdsparentportidentity = value
                    self.cptpclockparentdsparentportidentity.value_namespace = name_space
                    self.cptpclockparentdsparentportidentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockParentDSParentStats"):
                    self.cptpclockparentdsparentstats = value
                    self.cptpclockparentdsparentstats.value_namespace = name_space
                    self.cptpclockparentdsparentstats.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockparentdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockparentdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockParentDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockParentDSEntry"):
                for c in self.cptpclockparentdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockparentdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockParentDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockdefaultdstable(Entity):
        """
        Table of information about the PTP clock Default Datasets for
        all domains.
        
        .. attribute:: cptpclockdefaultdsentry
        
        	An entry in the table, containing information about a single PTP clock Default Datasets for a domain
        	**type**\: list of    :py:class:`Cptpclockdefaultdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockdefaultdstable, self).__init__()

            self.yang_name = "cPtpClockDefaultDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockdefaultdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockdefaultdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockdefaultdstable, self).__setattr__(name, value)


        class Cptpclockdefaultdsentry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock Default Datasets for a domain.
            
            .. attribute:: cptpclockdefaultdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockdefaultdsinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsclockidentity
            
            	This object specifies the default Datasets clock identity
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cptpclockdefaultdspriority1
            
            	This object specifies the default Datasets clock Priority1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockdefaultdspriority2
            
            	This object specifies the default Datasets clock Priority2
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockdefaultdsqualityaccuracy
            
            	This object specifies the default dataset Quality Accurarcy
            	**type**\:   :py:class:`Clockqualityaccuracytype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockqualityaccuracytype>`
            
            .. attribute:: cptpclockdefaultdsqualityclass
            
            	This object specifies the default dataset Quality Class
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsqualityoffset
            
            	This object specifies the default dataset Quality offset
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockdefaultdsslaveonly
            
            	Whether the SlaveOnly flag is set
            	**type**\:  bool
            
            .. attribute:: cptpclockdefaultdstwostepflag
            
            	This object specifies whether the Two Step process is used
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry, self).__init__()

                self.yang_name = "cPtpClockDefaultDSEntry"
                self.yang_parent_name = "cPtpClockDefaultDSTable"

                self.cptpclockdefaultdsdomainindex = YLeaf(YType.uint32, "cPtpClockDefaultDSDomainIndex")

                self.cptpclockdefaultdsclocktypeindex = YLeaf(YType.enumeration, "cPtpClockDefaultDSClockTypeIndex")

                self.cptpclockdefaultdsinstanceindex = YLeaf(YType.uint32, "cPtpClockDefaultDSInstanceIndex")

                self.cptpclockdefaultdsclockidentity = YLeaf(YType.str, "cPtpClockDefaultDSClockIdentity")

                self.cptpclockdefaultdspriority1 = YLeaf(YType.int32, "cPtpClockDefaultDSPriority1")

                self.cptpclockdefaultdspriority2 = YLeaf(YType.int32, "cPtpClockDefaultDSPriority2")

                self.cptpclockdefaultdsqualityaccuracy = YLeaf(YType.enumeration, "cPtpClockDefaultDSQualityAccuracy")

                self.cptpclockdefaultdsqualityclass = YLeaf(YType.uint32, "cPtpClockDefaultDSQualityClass")

                self.cptpclockdefaultdsqualityoffset = YLeaf(YType.int32, "cPtpClockDefaultDSQualityOffset")

                self.cptpclockdefaultdsslaveonly = YLeaf(YType.boolean, "cPtpClockDefaultDSSlaveOnly")

                self.cptpclockdefaultdstwostepflag = YLeaf(YType.boolean, "cPtpClockDefaultDSTwoStepFlag")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockdefaultdsdomainindex",
                                "cptpclockdefaultdsclocktypeindex",
                                "cptpclockdefaultdsinstanceindex",
                                "cptpclockdefaultdsclockidentity",
                                "cptpclockdefaultdspriority1",
                                "cptpclockdefaultdspriority2",
                                "cptpclockdefaultdsqualityaccuracy",
                                "cptpclockdefaultdsqualityclass",
                                "cptpclockdefaultdsqualityoffset",
                                "cptpclockdefaultdsslaveonly",
                                "cptpclockdefaultdstwostepflag") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockdefaultdsdomainindex.is_set or
                    self.cptpclockdefaultdsclocktypeindex.is_set or
                    self.cptpclockdefaultdsinstanceindex.is_set or
                    self.cptpclockdefaultdsclockidentity.is_set or
                    self.cptpclockdefaultdspriority1.is_set or
                    self.cptpclockdefaultdspriority2.is_set or
                    self.cptpclockdefaultdsqualityaccuracy.is_set or
                    self.cptpclockdefaultdsqualityclass.is_set or
                    self.cptpclockdefaultdsqualityoffset.is_set or
                    self.cptpclockdefaultdsslaveonly.is_set or
                    self.cptpclockdefaultdstwostepflag.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsclockidentity.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdspriority1.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdspriority2.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsqualityaccuracy.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsqualityclass.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsqualityoffset.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdsslaveonly.yfilter != YFilter.not_set or
                    self.cptpclockdefaultdstwostepflag.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockDefaultDSEntry" + "[cPtpClockDefaultDSDomainIndex='" + self.cptpclockdefaultdsdomainindex.get() + "']" + "[cPtpClockDefaultDSClockTypeIndex='" + self.cptpclockdefaultdsclocktypeindex.get() + "']" + "[cPtpClockDefaultDSInstanceIndex='" + self.cptpclockdefaultdsinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockDefaultDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockdefaultdsdomainindex.is_set or self.cptpclockdefaultdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsdomainindex.get_name_leafdata())
                if (self.cptpclockdefaultdsclocktypeindex.is_set or self.cptpclockdefaultdsclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsclocktypeindex.get_name_leafdata())
                if (self.cptpclockdefaultdsinstanceindex.is_set or self.cptpclockdefaultdsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsinstanceindex.get_name_leafdata())
                if (self.cptpclockdefaultdsclockidentity.is_set or self.cptpclockdefaultdsclockidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsclockidentity.get_name_leafdata())
                if (self.cptpclockdefaultdspriority1.is_set or self.cptpclockdefaultdspriority1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdspriority1.get_name_leafdata())
                if (self.cptpclockdefaultdspriority2.is_set or self.cptpclockdefaultdspriority2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdspriority2.get_name_leafdata())
                if (self.cptpclockdefaultdsqualityaccuracy.is_set or self.cptpclockdefaultdsqualityaccuracy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsqualityaccuracy.get_name_leafdata())
                if (self.cptpclockdefaultdsqualityclass.is_set or self.cptpclockdefaultdsqualityclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsqualityclass.get_name_leafdata())
                if (self.cptpclockdefaultdsqualityoffset.is_set or self.cptpclockdefaultdsqualityoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsqualityoffset.get_name_leafdata())
                if (self.cptpclockdefaultdsslaveonly.is_set or self.cptpclockdefaultdsslaveonly.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdsslaveonly.get_name_leafdata())
                if (self.cptpclockdefaultdstwostepflag.is_set or self.cptpclockdefaultdstwostepflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockdefaultdstwostepflag.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockDefaultDSDomainIndex" or name == "cPtpClockDefaultDSClockTypeIndex" or name == "cPtpClockDefaultDSInstanceIndex" or name == "cPtpClockDefaultDSClockIdentity" or name == "cPtpClockDefaultDSPriority1" or name == "cPtpClockDefaultDSPriority2" or name == "cPtpClockDefaultDSQualityAccuracy" or name == "cPtpClockDefaultDSQualityClass" or name == "cPtpClockDefaultDSQualityOffset" or name == "cPtpClockDefaultDSSlaveOnly" or name == "cPtpClockDefaultDSTwoStepFlag"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockDefaultDSDomainIndex"):
                    self.cptpclockdefaultdsdomainindex = value
                    self.cptpclockdefaultdsdomainindex.value_namespace = name_space
                    self.cptpclockdefaultdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSClockTypeIndex"):
                    self.cptpclockdefaultdsclocktypeindex = value
                    self.cptpclockdefaultdsclocktypeindex.value_namespace = name_space
                    self.cptpclockdefaultdsclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSInstanceIndex"):
                    self.cptpclockdefaultdsinstanceindex = value
                    self.cptpclockdefaultdsinstanceindex.value_namespace = name_space
                    self.cptpclockdefaultdsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSClockIdentity"):
                    self.cptpclockdefaultdsclockidentity = value
                    self.cptpclockdefaultdsclockidentity.value_namespace = name_space
                    self.cptpclockdefaultdsclockidentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSPriority1"):
                    self.cptpclockdefaultdspriority1 = value
                    self.cptpclockdefaultdspriority1.value_namespace = name_space
                    self.cptpclockdefaultdspriority1.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSPriority2"):
                    self.cptpclockdefaultdspriority2 = value
                    self.cptpclockdefaultdspriority2.value_namespace = name_space
                    self.cptpclockdefaultdspriority2.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSQualityAccuracy"):
                    self.cptpclockdefaultdsqualityaccuracy = value
                    self.cptpclockdefaultdsqualityaccuracy.value_namespace = name_space
                    self.cptpclockdefaultdsqualityaccuracy.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSQualityClass"):
                    self.cptpclockdefaultdsqualityclass = value
                    self.cptpclockdefaultdsqualityclass.value_namespace = name_space
                    self.cptpclockdefaultdsqualityclass.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSQualityOffset"):
                    self.cptpclockdefaultdsqualityoffset = value
                    self.cptpclockdefaultdsqualityoffset.value_namespace = name_space
                    self.cptpclockdefaultdsqualityoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSSlaveOnly"):
                    self.cptpclockdefaultdsslaveonly = value
                    self.cptpclockdefaultdsslaveonly.value_namespace = name_space
                    self.cptpclockdefaultdsslaveonly.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockDefaultDSTwoStepFlag"):
                    self.cptpclockdefaultdstwostepflag = value
                    self.cptpclockdefaultdstwostepflag.value_namespace = name_space
                    self.cptpclockdefaultdstwostepflag.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockdefaultdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockdefaultdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockDefaultDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockDefaultDSEntry"):
                for c in self.cptpclockdefaultdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockdefaultdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockDefaultDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockrunningtable(Entity):
        """
        Table of information about the PTP clock Running Datasets for
        all domains.
        
        .. attribute:: cptpclockrunningentry
        
        	An entry in the table, containing information about a single PTP clock running Datasets for a domain
        	**type**\: list of    :py:class:`Cptpclockrunningentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockrunningtable, self).__init__()

            self.yang_name = "cPtpClockRunningTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockrunningentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockrunningtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockrunningtable, self).__setattr__(name, value)


        class Cptpclockrunningentry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock running Datasets for a domain.
            
            .. attribute:: cptpclockrunningdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockrunningclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockrunninginstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockrunningpacketsreceived
            
            	This object specifies the total number of all packet Unicast and multicast that have been received for this clock in this domain for this type
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockrunningpacketssent
            
            	This object specifies the total number of all packet Unicast and multicast that have been sent out for this clock in this domain for this type
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockrunningstate
            
            	This object specifies the Clock state returned by PTP engine which was described earlier.  Freerun state. Applies to a slave device that is not locked to a master. This is the initial state a slave starts out with when it is not getting any PTP packets from the master or because of some other input error (erroneous packets, etc).  Holdover state. In this state the slave device is locked to a master but communication with the master is lost or the timestamps in the ptp packets are incorrect. But since the slave was locked to the master, it can run with the same accuracy for sometime. The slave can continue to operate in this state for some time. If communication with the master is not restored for a while, the device is moved to the FREERUN state.  Acquiring state. The slave device is receiving packets from a master and is trying to acquire a lock.  Freq\_locked state. Slave device is locked to the Master with respect to frequency, but not phase aligned  Phase\_aligned state. Locked to the master with respect to frequency and phase
            	**type**\:   :py:class:`Clockstatetype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockstatetype>`
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry, self).__init__()

                self.yang_name = "cPtpClockRunningEntry"
                self.yang_parent_name = "cPtpClockRunningTable"

                self.cptpclockrunningdomainindex = YLeaf(YType.uint32, "cPtpClockRunningDomainIndex")

                self.cptpclockrunningclocktypeindex = YLeaf(YType.enumeration, "cPtpClockRunningClockTypeIndex")

                self.cptpclockrunninginstanceindex = YLeaf(YType.uint32, "cPtpClockRunningInstanceIndex")

                self.cptpclockrunningpacketsreceived = YLeaf(YType.uint64, "cPtpClockRunningPacketsReceived")

                self.cptpclockrunningpacketssent = YLeaf(YType.uint64, "cPtpClockRunningPacketsSent")

                self.cptpclockrunningstate = YLeaf(YType.enumeration, "cPtpClockRunningState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockrunningdomainindex",
                                "cptpclockrunningclocktypeindex",
                                "cptpclockrunninginstanceindex",
                                "cptpclockrunningpacketsreceived",
                                "cptpclockrunningpacketssent",
                                "cptpclockrunningstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockrunningdomainindex.is_set or
                    self.cptpclockrunningclocktypeindex.is_set or
                    self.cptpclockrunninginstanceindex.is_set or
                    self.cptpclockrunningpacketsreceived.is_set or
                    self.cptpclockrunningpacketssent.is_set or
                    self.cptpclockrunningstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockrunningdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockrunningclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockrunninginstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockrunningpacketsreceived.yfilter != YFilter.not_set or
                    self.cptpclockrunningpacketssent.yfilter != YFilter.not_set or
                    self.cptpclockrunningstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockRunningEntry" + "[cPtpClockRunningDomainIndex='" + self.cptpclockrunningdomainindex.get() + "']" + "[cPtpClockRunningClockTypeIndex='" + self.cptpclockrunningclocktypeindex.get() + "']" + "[cPtpClockRunningInstanceIndex='" + self.cptpclockrunninginstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockRunningTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockrunningdomainindex.is_set or self.cptpclockrunningdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockrunningdomainindex.get_name_leafdata())
                if (self.cptpclockrunningclocktypeindex.is_set or self.cptpclockrunningclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockrunningclocktypeindex.get_name_leafdata())
                if (self.cptpclockrunninginstanceindex.is_set or self.cptpclockrunninginstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockrunninginstanceindex.get_name_leafdata())
                if (self.cptpclockrunningpacketsreceived.is_set or self.cptpclockrunningpacketsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockrunningpacketsreceived.get_name_leafdata())
                if (self.cptpclockrunningpacketssent.is_set or self.cptpclockrunningpacketssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockrunningpacketssent.get_name_leafdata())
                if (self.cptpclockrunningstate.is_set or self.cptpclockrunningstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockrunningstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockRunningDomainIndex" or name == "cPtpClockRunningClockTypeIndex" or name == "cPtpClockRunningInstanceIndex" or name == "cPtpClockRunningPacketsReceived" or name == "cPtpClockRunningPacketsSent" or name == "cPtpClockRunningState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockRunningDomainIndex"):
                    self.cptpclockrunningdomainindex = value
                    self.cptpclockrunningdomainindex.value_namespace = name_space
                    self.cptpclockrunningdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockRunningClockTypeIndex"):
                    self.cptpclockrunningclocktypeindex = value
                    self.cptpclockrunningclocktypeindex.value_namespace = name_space
                    self.cptpclockrunningclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockRunningInstanceIndex"):
                    self.cptpclockrunninginstanceindex = value
                    self.cptpclockrunninginstanceindex.value_namespace = name_space
                    self.cptpclockrunninginstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockRunningPacketsReceived"):
                    self.cptpclockrunningpacketsreceived = value
                    self.cptpclockrunningpacketsreceived.value_namespace = name_space
                    self.cptpclockrunningpacketsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockRunningPacketsSent"):
                    self.cptpclockrunningpacketssent = value
                    self.cptpclockrunningpacketssent.value_namespace = name_space
                    self.cptpclockrunningpacketssent.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockRunningState"):
                    self.cptpclockrunningstate = value
                    self.cptpclockrunningstate.value_namespace = name_space
                    self.cptpclockrunningstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockrunningentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockrunningentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockRunningTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockRunningEntry"):
                for c in self.cptpclockrunningentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockrunningentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockRunningEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclocktimepropertiesdstable(Entity):
        """
        Table of information about the PTP clock Timeproperties
        Datasets for all domains.
        
        .. attribute:: cptpclocktimepropertiesdsentry
        
        	An entry in the table, containing information about a single PTP clock timeproperties Datasets for a domain
        	**type**\: list of    :py:class:`Cptpclocktimepropertiesdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclocktimepropertiesdstable, self).__init__()

            self.yang_name = "cPtpClockTimePropertiesDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclocktimepropertiesdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclocktimepropertiesdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclocktimepropertiesdstable, self).__setattr__(name, value)


        class Cptpclocktimepropertiesdsentry(Entity):
            """
            An entry in the table, containing information about a single
            PTP clock timeproperties Datasets for a domain.
            
            .. attribute:: cptpclocktimepropertiesdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktimepropertiesdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclocktimepropertiesdsinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktimepropertiesdscurrentutcoffset
            
            	This object specifies the timeproperties dataset value of current UTC offset.  In PTP systems whose epoch is the PTP epoch, the value of timePropertiesDS.currentUtcOffset is the offset between TAI and UTC; otherwise the value has no meaning. The value shall be in units of seconds. The initialization value shall be selected as follows\: a) If the timePropertiesDS.ptpTimescale (see 8.2.4.8) is TRUE, the value is the value obtained from a primary reference if the value is known at the time of initialization, else. b) The value shall be the current number of leap seconds (7.2.3) when the node is designed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclocktimepropertiesdscurrentutcoffsetvalid
            
            	This object specifies the timeproperties dataset value of whether current UTC offset is valid
            	**type**\:  bool
            
            .. attribute:: cptpclocktimepropertiesdsfreqtraceable
            
            	This object specifies the Frequency Traceable value in the clock Current Dataset
            	**type**\:  bool
            
            .. attribute:: cptpclocktimepropertiesdsleap59
            
            	This object specifies the Leap59 value in the clock Current Dataset
            	**type**\:  bool
            
            .. attribute:: cptpclocktimepropertiesdsleap61
            
            	This object specifies the Leap61 value in the clock Current Dataset
            	**type**\:  bool
            
            .. attribute:: cptpclocktimepropertiesdsptptimescale
            
            	This object specifies the PTP Timescale value in the clock Current Dataset
            	**type**\:  bool
            
            .. attribute:: cptpclocktimepropertiesdssource
            
            	This object specifies the Timesource value in the clock Current Dataset
            	**type**\:   :py:class:`Clocktimesourcetype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktimesourcetype>`
            
            .. attribute:: cptpclocktimepropertiesdstimetraceable
            
            	This object specifies the Timetraceable value in the clock Current Dataset
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry, self).__init__()

                self.yang_name = "cPtpClockTimePropertiesDSEntry"
                self.yang_parent_name = "cPtpClockTimePropertiesDSTable"

                self.cptpclocktimepropertiesdsdomainindex = YLeaf(YType.uint32, "cPtpClockTimePropertiesDSDomainIndex")

                self.cptpclocktimepropertiesdsclocktypeindex = YLeaf(YType.enumeration, "cPtpClockTimePropertiesDSClockTypeIndex")

                self.cptpclocktimepropertiesdsinstanceindex = YLeaf(YType.uint32, "cPtpClockTimePropertiesDSInstanceIndex")

                self.cptpclocktimepropertiesdscurrentutcoffset = YLeaf(YType.int32, "cPtpClockTimePropertiesDSCurrentUTCOffset")

                self.cptpclocktimepropertiesdscurrentutcoffsetvalid = YLeaf(YType.boolean, "cPtpClockTimePropertiesDSCurrentUTCOffsetValid")

                self.cptpclocktimepropertiesdsfreqtraceable = YLeaf(YType.boolean, "cPtpClockTimePropertiesDSFreqTraceable")

                self.cptpclocktimepropertiesdsleap59 = YLeaf(YType.boolean, "cPtpClockTimePropertiesDSLeap59")

                self.cptpclocktimepropertiesdsleap61 = YLeaf(YType.boolean, "cPtpClockTimePropertiesDSLeap61")

                self.cptpclocktimepropertiesdsptptimescale = YLeaf(YType.boolean, "cPtpClockTimePropertiesDSPTPTimescale")

                self.cptpclocktimepropertiesdssource = YLeaf(YType.enumeration, "cPtpClockTimePropertiesDSSource")

                self.cptpclocktimepropertiesdstimetraceable = YLeaf(YType.boolean, "cPtpClockTimePropertiesDSTimeTraceable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclocktimepropertiesdsdomainindex",
                                "cptpclocktimepropertiesdsclocktypeindex",
                                "cptpclocktimepropertiesdsinstanceindex",
                                "cptpclocktimepropertiesdscurrentutcoffset",
                                "cptpclocktimepropertiesdscurrentutcoffsetvalid",
                                "cptpclocktimepropertiesdsfreqtraceable",
                                "cptpclocktimepropertiesdsleap59",
                                "cptpclocktimepropertiesdsleap61",
                                "cptpclocktimepropertiesdsptptimescale",
                                "cptpclocktimepropertiesdssource",
                                "cptpclocktimepropertiesdstimetraceable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclocktimepropertiesdsdomainindex.is_set or
                    self.cptpclocktimepropertiesdsclocktypeindex.is_set or
                    self.cptpclocktimepropertiesdsinstanceindex.is_set or
                    self.cptpclocktimepropertiesdscurrentutcoffset.is_set or
                    self.cptpclocktimepropertiesdscurrentutcoffsetvalid.is_set or
                    self.cptpclocktimepropertiesdsfreqtraceable.is_set or
                    self.cptpclocktimepropertiesdsleap59.is_set or
                    self.cptpclocktimepropertiesdsleap61.is_set or
                    self.cptpclocktimepropertiesdsptptimescale.is_set or
                    self.cptpclocktimepropertiesdssource.is_set or
                    self.cptpclocktimepropertiesdstimetraceable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdscurrentutcoffset.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdscurrentutcoffsetvalid.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsfreqtraceable.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsleap59.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsleap61.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdsptptimescale.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdssource.yfilter != YFilter.not_set or
                    self.cptpclocktimepropertiesdstimetraceable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockTimePropertiesDSEntry" + "[cPtpClockTimePropertiesDSDomainIndex='" + self.cptpclocktimepropertiesdsdomainindex.get() + "']" + "[cPtpClockTimePropertiesDSClockTypeIndex='" + self.cptpclocktimepropertiesdsclocktypeindex.get() + "']" + "[cPtpClockTimePropertiesDSInstanceIndex='" + self.cptpclocktimepropertiesdsinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockTimePropertiesDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclocktimepropertiesdsdomainindex.is_set or self.cptpclocktimepropertiesdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsdomainindex.get_name_leafdata())
                if (self.cptpclocktimepropertiesdsclocktypeindex.is_set or self.cptpclocktimepropertiesdsclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsclocktypeindex.get_name_leafdata())
                if (self.cptpclocktimepropertiesdsinstanceindex.is_set or self.cptpclocktimepropertiesdsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsinstanceindex.get_name_leafdata())
                if (self.cptpclocktimepropertiesdscurrentutcoffset.is_set or self.cptpclocktimepropertiesdscurrentutcoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdscurrentutcoffset.get_name_leafdata())
                if (self.cptpclocktimepropertiesdscurrentutcoffsetvalid.is_set or self.cptpclocktimepropertiesdscurrentutcoffsetvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdscurrentutcoffsetvalid.get_name_leafdata())
                if (self.cptpclocktimepropertiesdsfreqtraceable.is_set or self.cptpclocktimepropertiesdsfreqtraceable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsfreqtraceable.get_name_leafdata())
                if (self.cptpclocktimepropertiesdsleap59.is_set or self.cptpclocktimepropertiesdsleap59.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsleap59.get_name_leafdata())
                if (self.cptpclocktimepropertiesdsleap61.is_set or self.cptpclocktimepropertiesdsleap61.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsleap61.get_name_leafdata())
                if (self.cptpclocktimepropertiesdsptptimescale.is_set or self.cptpclocktimepropertiesdsptptimescale.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdsptptimescale.get_name_leafdata())
                if (self.cptpclocktimepropertiesdssource.is_set or self.cptpclocktimepropertiesdssource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdssource.get_name_leafdata())
                if (self.cptpclocktimepropertiesdstimetraceable.is_set or self.cptpclocktimepropertiesdstimetraceable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktimepropertiesdstimetraceable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockTimePropertiesDSDomainIndex" or name == "cPtpClockTimePropertiesDSClockTypeIndex" or name == "cPtpClockTimePropertiesDSInstanceIndex" or name == "cPtpClockTimePropertiesDSCurrentUTCOffset" or name == "cPtpClockTimePropertiesDSCurrentUTCOffsetValid" or name == "cPtpClockTimePropertiesDSFreqTraceable" or name == "cPtpClockTimePropertiesDSLeap59" or name == "cPtpClockTimePropertiesDSLeap61" or name == "cPtpClockTimePropertiesDSPTPTimescale" or name == "cPtpClockTimePropertiesDSSource" or name == "cPtpClockTimePropertiesDSTimeTraceable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockTimePropertiesDSDomainIndex"):
                    self.cptpclocktimepropertiesdsdomainindex = value
                    self.cptpclocktimepropertiesdsdomainindex.value_namespace = name_space
                    self.cptpclocktimepropertiesdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSClockTypeIndex"):
                    self.cptpclocktimepropertiesdsclocktypeindex = value
                    self.cptpclocktimepropertiesdsclocktypeindex.value_namespace = name_space
                    self.cptpclocktimepropertiesdsclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSInstanceIndex"):
                    self.cptpclocktimepropertiesdsinstanceindex = value
                    self.cptpclocktimepropertiesdsinstanceindex.value_namespace = name_space
                    self.cptpclocktimepropertiesdsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSCurrentUTCOffset"):
                    self.cptpclocktimepropertiesdscurrentutcoffset = value
                    self.cptpclocktimepropertiesdscurrentutcoffset.value_namespace = name_space
                    self.cptpclocktimepropertiesdscurrentutcoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSCurrentUTCOffsetValid"):
                    self.cptpclocktimepropertiesdscurrentutcoffsetvalid = value
                    self.cptpclocktimepropertiesdscurrentutcoffsetvalid.value_namespace = name_space
                    self.cptpclocktimepropertiesdscurrentutcoffsetvalid.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSFreqTraceable"):
                    self.cptpclocktimepropertiesdsfreqtraceable = value
                    self.cptpclocktimepropertiesdsfreqtraceable.value_namespace = name_space
                    self.cptpclocktimepropertiesdsfreqtraceable.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSLeap59"):
                    self.cptpclocktimepropertiesdsleap59 = value
                    self.cptpclocktimepropertiesdsleap59.value_namespace = name_space
                    self.cptpclocktimepropertiesdsleap59.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSLeap61"):
                    self.cptpclocktimepropertiesdsleap61 = value
                    self.cptpclocktimepropertiesdsleap61.value_namespace = name_space
                    self.cptpclocktimepropertiesdsleap61.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSPTPTimescale"):
                    self.cptpclocktimepropertiesdsptptimescale = value
                    self.cptpclocktimepropertiesdsptptimescale.value_namespace = name_space
                    self.cptpclocktimepropertiesdsptptimescale.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSSource"):
                    self.cptpclocktimepropertiesdssource = value
                    self.cptpclocktimepropertiesdssource.value_namespace = name_space
                    self.cptpclocktimepropertiesdssource.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTimePropertiesDSTimeTraceable"):
                    self.cptpclocktimepropertiesdstimetraceable = value
                    self.cptpclocktimepropertiesdstimetraceable.value_namespace = name_space
                    self.cptpclocktimepropertiesdstimetraceable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclocktimepropertiesdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclocktimepropertiesdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockTimePropertiesDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockTimePropertiesDSEntry"):
                for c in self.cptpclocktimepropertiesdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclocktimepropertiesdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockTimePropertiesDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclocktransdefaultdstable(Entity):
        """
        Table of information about the PTP Transparent clock Default
        Datasets for all domains.
        
        .. attribute:: cptpclocktransdefaultdsentry
        
        	An entry in the table, containing information about a single PTP Transparent clock Default Datasets for a domain
        	**type**\: list of    :py:class:`Cptpclocktransdefaultdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclocktransdefaultdstable, self).__init__()

            self.yang_name = "cPtpClockTransDefaultDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclocktransdefaultdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclocktransdefaultdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclocktransdefaultdstable, self).__setattr__(name, value)


        class Cptpclocktransdefaultdsentry(Entity):
            """
            An entry in the table, containing information about a single
            PTP Transparent clock Default Datasets for a domain.
            
            .. attribute:: cptpclocktransdefaultdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktransdefaultdsinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktransdefaultdsclockidentity
            
            	This object specifies the value of the clockIdentity attribute of the local clock
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cptpclocktransdefaultdsdelay
            
            	This object, if the transparent clock is an end\-to\-end transparent clock, has the value shall be E2E; If the transparent clock is a peer\-to\-peer transparent clock, the value shall be P2P
            	**type**\:   :py:class:`Clockmechanismtype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockmechanismtype>`
            
            .. attribute:: cptpclocktransdefaultdsnumofports
            
            	This object specifies the number of PTP ports of the device
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclocktransdefaultdsprimarydomain
            
            	This object specifies the value of the primary syntonization domain. The initialization value shall be 0
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry, self).__init__()

                self.yang_name = "cPtpClockTransDefaultDSEntry"
                self.yang_parent_name = "cPtpClockTransDefaultDSTable"

                self.cptpclocktransdefaultdsdomainindex = YLeaf(YType.uint32, "cPtpClockTransDefaultDSDomainIndex")

                self.cptpclocktransdefaultdsinstanceindex = YLeaf(YType.uint32, "cPtpClockTransDefaultDSInstanceIndex")

                self.cptpclocktransdefaultdsclockidentity = YLeaf(YType.str, "cPtpClockTransDefaultDSClockIdentity")

                self.cptpclocktransdefaultdsdelay = YLeaf(YType.enumeration, "cPtpClockTransDefaultDSDelay")

                self.cptpclocktransdefaultdsnumofports = YLeaf(YType.uint32, "cPtpClockTransDefaultDSNumOfPorts")

                self.cptpclocktransdefaultdsprimarydomain = YLeaf(YType.int32, "cPtpClockTransDefaultDSPrimaryDomain")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclocktransdefaultdsdomainindex",
                                "cptpclocktransdefaultdsinstanceindex",
                                "cptpclocktransdefaultdsclockidentity",
                                "cptpclocktransdefaultdsdelay",
                                "cptpclocktransdefaultdsnumofports",
                                "cptpclocktransdefaultdsprimarydomain") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclocktransdefaultdsdomainindex.is_set or
                    self.cptpclocktransdefaultdsinstanceindex.is_set or
                    self.cptpclocktransdefaultdsclockidentity.is_set or
                    self.cptpclocktransdefaultdsdelay.is_set or
                    self.cptpclocktransdefaultdsnumofports.is_set or
                    self.cptpclocktransdefaultdsprimarydomain.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclocktransdefaultdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclocktransdefaultdsinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclocktransdefaultdsclockidentity.yfilter != YFilter.not_set or
                    self.cptpclocktransdefaultdsdelay.yfilter != YFilter.not_set or
                    self.cptpclocktransdefaultdsnumofports.yfilter != YFilter.not_set or
                    self.cptpclocktransdefaultdsprimarydomain.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockTransDefaultDSEntry" + "[cPtpClockTransDefaultDSDomainIndex='" + self.cptpclocktransdefaultdsdomainindex.get() + "']" + "[cPtpClockTransDefaultDSInstanceIndex='" + self.cptpclocktransdefaultdsinstanceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockTransDefaultDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclocktransdefaultdsdomainindex.is_set or self.cptpclocktransdefaultdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktransdefaultdsdomainindex.get_name_leafdata())
                if (self.cptpclocktransdefaultdsinstanceindex.is_set or self.cptpclocktransdefaultdsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktransdefaultdsinstanceindex.get_name_leafdata())
                if (self.cptpclocktransdefaultdsclockidentity.is_set or self.cptpclocktransdefaultdsclockidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktransdefaultdsclockidentity.get_name_leafdata())
                if (self.cptpclocktransdefaultdsdelay.is_set or self.cptpclocktransdefaultdsdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktransdefaultdsdelay.get_name_leafdata())
                if (self.cptpclocktransdefaultdsnumofports.is_set or self.cptpclocktransdefaultdsnumofports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktransdefaultdsnumofports.get_name_leafdata())
                if (self.cptpclocktransdefaultdsprimarydomain.is_set or self.cptpclocktransdefaultdsprimarydomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclocktransdefaultdsprimarydomain.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockTransDefaultDSDomainIndex" or name == "cPtpClockTransDefaultDSInstanceIndex" or name == "cPtpClockTransDefaultDSClockIdentity" or name == "cPtpClockTransDefaultDSDelay" or name == "cPtpClockTransDefaultDSNumOfPorts" or name == "cPtpClockTransDefaultDSPrimaryDomain"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockTransDefaultDSDomainIndex"):
                    self.cptpclocktransdefaultdsdomainindex = value
                    self.cptpclocktransdefaultdsdomainindex.value_namespace = name_space
                    self.cptpclocktransdefaultdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTransDefaultDSInstanceIndex"):
                    self.cptpclocktransdefaultdsinstanceindex = value
                    self.cptpclocktransdefaultdsinstanceindex.value_namespace = name_space
                    self.cptpclocktransdefaultdsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTransDefaultDSClockIdentity"):
                    self.cptpclocktransdefaultdsclockidentity = value
                    self.cptpclocktransdefaultdsclockidentity.value_namespace = name_space
                    self.cptpclocktransdefaultdsclockidentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTransDefaultDSDelay"):
                    self.cptpclocktransdefaultdsdelay = value
                    self.cptpclocktransdefaultdsdelay.value_namespace = name_space
                    self.cptpclocktransdefaultdsdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTransDefaultDSNumOfPorts"):
                    self.cptpclocktransdefaultdsnumofports = value
                    self.cptpclocktransdefaultdsnumofports.value_namespace = name_space
                    self.cptpclocktransdefaultdsnumofports.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockTransDefaultDSPrimaryDomain"):
                    self.cptpclocktransdefaultdsprimarydomain = value
                    self.cptpclocktransdefaultdsprimarydomain.value_namespace = name_space
                    self.cptpclocktransdefaultdsprimarydomain.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclocktransdefaultdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclocktransdefaultdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockTransDefaultDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockTransDefaultDSEntry"):
                for c in self.cptpclocktransdefaultdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclocktransdefaultdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockTransDefaultDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockporttable(Entity):
        """
        Table of information about the clock ports for a particular
        domain.
        
        .. attribute:: cptpclockportentry
        
        	An entry in the table, containing information about a single clock port
        	**type**\: list of    :py:class:`Cptpclockportentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockporttable.Cptpclockportentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockporttable, self).__init__()

            self.yang_name = "cPtpClockPortTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockportentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockporttable, self).__setattr__(name, value)


        class Cptpclockportentry(Entity):
            """
            An entry in the table, containing information about a single
            clock port.
            
            .. attribute:: cptpclockportdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockportclockinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockporttableportnumberindex  <key>
            
            	This object specifies the PTP Portnumber for this port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportcurrentpeeraddress
            
            	This object specifies the current peer's network address used for PTP communication. Based on the scenario and the setup involved, the values might look like these \- Scenario                   Value \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Single Master          master port Multiple Masters       selected master port Single Slave           slave port Multiple Slaves        <empty>  (In relevant setups, information on available slaves and available masters will be available through  cPtpClockPortAssociateTable)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cptpclockportcurrentpeeraddresstype
            
            	This object specifies the current peer's network address used for PTP communication. Based on the scenario and the setup involved, the values might look like these \- Scenario                   Value \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Single Master          master port Multiple Masters       selected master port Single Slave           slave port Multiple Slaves        <empty>  (In relevant setups, information on available slaves and available masters will be available through  cPtpClockPortAssociateTable)
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cptpclockportname
            
            	This object specifies the PTP clock port name configured on the router
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cptpclockportnumofassociatedports
            
            	This object specifies \- For a master port \- the number of PTP slave sessions (peers) associated with this PTP port. For a slave port \- the number of masters available to this slave port (might or might not be peered)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclockportrole
            
            	This object describes the current role (slave/master) of the port
            	**type**\:   :py:class:`Clockroletype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockroletype>`
            
            .. attribute:: cptpclockportsynconestep
            
            	This object specifies that one\-step clock operation between the PTP master and slave device is enabled
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockporttable.Cptpclockportentry, self).__init__()

                self.yang_name = "cPtpClockPortEntry"
                self.yang_parent_name = "cPtpClockPortTable"

                self.cptpclockportdomainindex = YLeaf(YType.uint32, "cPtpClockPortDomainIndex")

                self.cptpclockportclocktypeindex = YLeaf(YType.enumeration, "cPtpClockPortClockTypeIndex")

                self.cptpclockportclockinstanceindex = YLeaf(YType.uint32, "cPtpClockPortClockInstanceIndex")

                self.cptpclockporttableportnumberindex = YLeaf(YType.uint32, "cPtpClockPortTablePortNumberIndex")

                self.cptpclockportcurrentpeeraddress = YLeaf(YType.str, "cPtpClockPortCurrentPeerAddress")

                self.cptpclockportcurrentpeeraddresstype = YLeaf(YType.enumeration, "cPtpClockPortCurrentPeerAddressType")

                self.cptpclockportname = YLeaf(YType.str, "cPtpClockPortName")

                self.cptpclockportnumofassociatedports = YLeaf(YType.uint32, "cPtpClockPortNumOfAssociatedPorts")

                self.cptpclockportrole = YLeaf(YType.enumeration, "cPtpClockPortRole")

                self.cptpclockportsynconestep = YLeaf(YType.boolean, "cPtpClockPortSyncOneStep")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockportdomainindex",
                                "cptpclockportclocktypeindex",
                                "cptpclockportclockinstanceindex",
                                "cptpclockporttableportnumberindex",
                                "cptpclockportcurrentpeeraddress",
                                "cptpclockportcurrentpeeraddresstype",
                                "cptpclockportname",
                                "cptpclockportnumofassociatedports",
                                "cptpclockportrole",
                                "cptpclockportsynconestep") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockporttable.Cptpclockportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockporttable.Cptpclockportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockportdomainindex.is_set or
                    self.cptpclockportclocktypeindex.is_set or
                    self.cptpclockportclockinstanceindex.is_set or
                    self.cptpclockporttableportnumberindex.is_set or
                    self.cptpclockportcurrentpeeraddress.is_set or
                    self.cptpclockportcurrentpeeraddresstype.is_set or
                    self.cptpclockportname.is_set or
                    self.cptpclockportnumofassociatedports.is_set or
                    self.cptpclockportrole.is_set or
                    self.cptpclockportsynconestep.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockportdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockportclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockportclockinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockporttableportnumberindex.yfilter != YFilter.not_set or
                    self.cptpclockportcurrentpeeraddress.yfilter != YFilter.not_set or
                    self.cptpclockportcurrentpeeraddresstype.yfilter != YFilter.not_set or
                    self.cptpclockportname.yfilter != YFilter.not_set or
                    self.cptpclockportnumofassociatedports.yfilter != YFilter.not_set or
                    self.cptpclockportrole.yfilter != YFilter.not_set or
                    self.cptpclockportsynconestep.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockPortEntry" + "[cPtpClockPortDomainIndex='" + self.cptpclockportdomainindex.get() + "']" + "[cPtpClockPortClockTypeIndex='" + self.cptpclockportclocktypeindex.get() + "']" + "[cPtpClockPortClockInstanceIndex='" + self.cptpclockportclockinstanceindex.get() + "']" + "[cPtpClockPortTablePortNumberIndex='" + self.cptpclockporttableportnumberindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockportdomainindex.is_set or self.cptpclockportdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdomainindex.get_name_leafdata())
                if (self.cptpclockportclocktypeindex.is_set or self.cptpclockportclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportclocktypeindex.get_name_leafdata())
                if (self.cptpclockportclockinstanceindex.is_set or self.cptpclockportclockinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportclockinstanceindex.get_name_leafdata())
                if (self.cptpclockporttableportnumberindex.is_set or self.cptpclockporttableportnumberindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttableportnumberindex.get_name_leafdata())
                if (self.cptpclockportcurrentpeeraddress.is_set or self.cptpclockportcurrentpeeraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportcurrentpeeraddress.get_name_leafdata())
                if (self.cptpclockportcurrentpeeraddresstype.is_set or self.cptpclockportcurrentpeeraddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportcurrentpeeraddresstype.get_name_leafdata())
                if (self.cptpclockportname.is_set or self.cptpclockportname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportname.get_name_leafdata())
                if (self.cptpclockportnumofassociatedports.is_set or self.cptpclockportnumofassociatedports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportnumofassociatedports.get_name_leafdata())
                if (self.cptpclockportrole.is_set or self.cptpclockportrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrole.get_name_leafdata())
                if (self.cptpclockportsynconestep.is_set or self.cptpclockportsynconestep.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportsynconestep.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockPortDomainIndex" or name == "cPtpClockPortClockTypeIndex" or name == "cPtpClockPortClockInstanceIndex" or name == "cPtpClockPortTablePortNumberIndex" or name == "cPtpClockPortCurrentPeerAddress" or name == "cPtpClockPortCurrentPeerAddressType" or name == "cPtpClockPortName" or name == "cPtpClockPortNumOfAssociatedPorts" or name == "cPtpClockPortRole" or name == "cPtpClockPortSyncOneStep"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockPortDomainIndex"):
                    self.cptpclockportdomainindex = value
                    self.cptpclockportdomainindex.value_namespace = name_space
                    self.cptpclockportdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortClockTypeIndex"):
                    self.cptpclockportclocktypeindex = value
                    self.cptpclockportclocktypeindex.value_namespace = name_space
                    self.cptpclockportclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortClockInstanceIndex"):
                    self.cptpclockportclockinstanceindex = value
                    self.cptpclockportclockinstanceindex.value_namespace = name_space
                    self.cptpclockportclockinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTablePortNumberIndex"):
                    self.cptpclockporttableportnumberindex = value
                    self.cptpclockporttableportnumberindex.value_namespace = name_space
                    self.cptpclockporttableportnumberindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortCurrentPeerAddress"):
                    self.cptpclockportcurrentpeeraddress = value
                    self.cptpclockportcurrentpeeraddress.value_namespace = name_space
                    self.cptpclockportcurrentpeeraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortCurrentPeerAddressType"):
                    self.cptpclockportcurrentpeeraddresstype = value
                    self.cptpclockportcurrentpeeraddresstype.value_namespace = name_space
                    self.cptpclockportcurrentpeeraddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortName"):
                    self.cptpclockportname = value
                    self.cptpclockportname.value_namespace = name_space
                    self.cptpclockportname.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortNumOfAssociatedPorts"):
                    self.cptpclockportnumofassociatedports = value
                    self.cptpclockportnumofassociatedports.value_namespace = name_space
                    self.cptpclockportnumofassociatedports.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRole"):
                    self.cptpclockportrole = value
                    self.cptpclockportrole.value_namespace = name_space
                    self.cptpclockportrole.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortSyncOneStep"):
                    self.cptpclockportsynconestep = value
                    self.cptpclockportsynconestep.value_namespace = name_space
                    self.cptpclockportsynconestep.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockPortEntry"):
                for c in self.cptpclockportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockporttable.Cptpclockportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockportdstable(Entity):
        """
        Table of information about the clock ports dataset for a
        particular domain.
        
        .. attribute:: cptpclockportdsentry
        
        	An entry in the table, containing port dataset information for a single clock port
        	**type**\: list of    :py:class:`Cptpclockportdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockportdstable, self).__init__()

            self.yang_name = "cPtpClockPortDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockportdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockportdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockportdstable, self).__setattr__(name, value)


        class Cptpclockportdsentry(Entity):
            """
            An entry in the table, containing port dataset information for
            a single clock port.
            
            .. attribute:: cptpclockportdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockportdsclockinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportdsportnumberindex  <key>
            
            	This object specifies the PTP portnumber associated with this PTP port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportdsannouncementinterval
            
            	This object specifies the Announce message transmission interval associated with this clock port
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdsannouncercttimeout
            
            	This object specifies the Announce receipt timeout associated with this clock port
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdsdelaymech
            
            	This object specifies the delay mechanism used. If the clock is an end\-to\-end clock, the value of the is e2e, else if the clock is a peer to\-peer clock, the value shall be p2p
            	**type**\:   :py:class:`Clockmechanismtype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockmechanismtype>`
            
            .. attribute:: cptpclockportdsgrantduration
            
            	This object specifies the grant duration allocated by the master
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclockportdsmindelayreqinterval
            
            	This object specifies the Delay\_Req message transmission interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdsname
            
            	This object specifies the PTP clock port name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cptpclockportdspeerdelayreqinterval
            
            	This object specifies the Pdelay\_Req message transmission interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdspeermeanpathdelay
            
            	This object specifies the peer meanPathDelay
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cptpclockportdsportidentity
            
            	This object specifies the PTP clock port Identity
            	**type**\:  str
            
            .. attribute:: cptpclockportdsptpversion
            
            	This object specifies the PTP version being used
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdssyncinterval
            
            	This object specifies the Sync message transmission interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry, self).__init__()

                self.yang_name = "cPtpClockPortDSEntry"
                self.yang_parent_name = "cPtpClockPortDSTable"

                self.cptpclockportdsdomainindex = YLeaf(YType.uint32, "cPtpClockPortDSDomainIndex")

                self.cptpclockportdsclocktypeindex = YLeaf(YType.enumeration, "cPtpClockPortDSClockTypeIndex")

                self.cptpclockportdsclockinstanceindex = YLeaf(YType.uint32, "cPtpClockPortDSClockInstanceIndex")

                self.cptpclockportdsportnumberindex = YLeaf(YType.uint32, "cPtpClockPortDSPortNumberIndex")

                self.cptpclockportdsannouncementinterval = YLeaf(YType.int32, "cPtpClockPortDSAnnouncementInterval")

                self.cptpclockportdsannouncercttimeout = YLeaf(YType.int32, "cPtpClockPortDSAnnounceRctTimeout")

                self.cptpclockportdsdelaymech = YLeaf(YType.enumeration, "cPtpClockPortDSDelayMech")

                self.cptpclockportdsgrantduration = YLeaf(YType.uint32, "cPtpClockPortDSGrantDuration")

                self.cptpclockportdsmindelayreqinterval = YLeaf(YType.int32, "cPtpClockPortDSMinDelayReqInterval")

                self.cptpclockportdsname = YLeaf(YType.str, "cPtpClockPortDSName")

                self.cptpclockportdspeerdelayreqinterval = YLeaf(YType.int32, "cPtpClockPortDSPeerDelayReqInterval")

                self.cptpclockportdspeermeanpathdelay = YLeaf(YType.str, "cPtpClockPortDSPeerMeanPathDelay")

                self.cptpclockportdsportidentity = YLeaf(YType.str, "cPtpClockPortDSPortIdentity")

                self.cptpclockportdsptpversion = YLeaf(YType.int32, "cPtpClockPortDSPTPVersion")

                self.cptpclockportdssyncinterval = YLeaf(YType.int32, "cPtpClockPortDSSyncInterval")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockportdsdomainindex",
                                "cptpclockportdsclocktypeindex",
                                "cptpclockportdsclockinstanceindex",
                                "cptpclockportdsportnumberindex",
                                "cptpclockportdsannouncementinterval",
                                "cptpclockportdsannouncercttimeout",
                                "cptpclockportdsdelaymech",
                                "cptpclockportdsgrantduration",
                                "cptpclockportdsmindelayreqinterval",
                                "cptpclockportdsname",
                                "cptpclockportdspeerdelayreqinterval",
                                "cptpclockportdspeermeanpathdelay",
                                "cptpclockportdsportidentity",
                                "cptpclockportdsptpversion",
                                "cptpclockportdssyncinterval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockportdsdomainindex.is_set or
                    self.cptpclockportdsclocktypeindex.is_set or
                    self.cptpclockportdsclockinstanceindex.is_set or
                    self.cptpclockportdsportnumberindex.is_set or
                    self.cptpclockportdsannouncementinterval.is_set or
                    self.cptpclockportdsannouncercttimeout.is_set or
                    self.cptpclockportdsdelaymech.is_set or
                    self.cptpclockportdsgrantduration.is_set or
                    self.cptpclockportdsmindelayreqinterval.is_set or
                    self.cptpclockportdsname.is_set or
                    self.cptpclockportdspeerdelayreqinterval.is_set or
                    self.cptpclockportdspeermeanpathdelay.is_set or
                    self.cptpclockportdsportidentity.is_set or
                    self.cptpclockportdsptpversion.is_set or
                    self.cptpclockportdssyncinterval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockportdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockportdsclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockportdsclockinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockportdsportnumberindex.yfilter != YFilter.not_set or
                    self.cptpclockportdsannouncementinterval.yfilter != YFilter.not_set or
                    self.cptpclockportdsannouncercttimeout.yfilter != YFilter.not_set or
                    self.cptpclockportdsdelaymech.yfilter != YFilter.not_set or
                    self.cptpclockportdsgrantduration.yfilter != YFilter.not_set or
                    self.cptpclockportdsmindelayreqinterval.yfilter != YFilter.not_set or
                    self.cptpclockportdsname.yfilter != YFilter.not_set or
                    self.cptpclockportdspeerdelayreqinterval.yfilter != YFilter.not_set or
                    self.cptpclockportdspeermeanpathdelay.yfilter != YFilter.not_set or
                    self.cptpclockportdsportidentity.yfilter != YFilter.not_set or
                    self.cptpclockportdsptpversion.yfilter != YFilter.not_set or
                    self.cptpclockportdssyncinterval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockPortDSEntry" + "[cPtpClockPortDSDomainIndex='" + self.cptpclockportdsdomainindex.get() + "']" + "[cPtpClockPortDSClockTypeIndex='" + self.cptpclockportdsclocktypeindex.get() + "']" + "[cPtpClockPortDSClockInstanceIndex='" + self.cptpclockportdsclockinstanceindex.get() + "']" + "[cPtpClockPortDSPortNumberIndex='" + self.cptpclockportdsportnumberindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockportdsdomainindex.is_set or self.cptpclockportdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsdomainindex.get_name_leafdata())
                if (self.cptpclockportdsclocktypeindex.is_set or self.cptpclockportdsclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsclocktypeindex.get_name_leafdata())
                if (self.cptpclockportdsclockinstanceindex.is_set or self.cptpclockportdsclockinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsclockinstanceindex.get_name_leafdata())
                if (self.cptpclockportdsportnumberindex.is_set or self.cptpclockportdsportnumberindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsportnumberindex.get_name_leafdata())
                if (self.cptpclockportdsannouncementinterval.is_set or self.cptpclockportdsannouncementinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsannouncementinterval.get_name_leafdata())
                if (self.cptpclockportdsannouncercttimeout.is_set or self.cptpclockportdsannouncercttimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsannouncercttimeout.get_name_leafdata())
                if (self.cptpclockportdsdelaymech.is_set or self.cptpclockportdsdelaymech.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsdelaymech.get_name_leafdata())
                if (self.cptpclockportdsgrantduration.is_set or self.cptpclockportdsgrantduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsgrantduration.get_name_leafdata())
                if (self.cptpclockportdsmindelayreqinterval.is_set or self.cptpclockportdsmindelayreqinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsmindelayreqinterval.get_name_leafdata())
                if (self.cptpclockportdsname.is_set or self.cptpclockportdsname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsname.get_name_leafdata())
                if (self.cptpclockportdspeerdelayreqinterval.is_set or self.cptpclockportdspeerdelayreqinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdspeerdelayreqinterval.get_name_leafdata())
                if (self.cptpclockportdspeermeanpathdelay.is_set or self.cptpclockportdspeermeanpathdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdspeermeanpathdelay.get_name_leafdata())
                if (self.cptpclockportdsportidentity.is_set or self.cptpclockportdsportidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsportidentity.get_name_leafdata())
                if (self.cptpclockportdsptpversion.is_set or self.cptpclockportdsptpversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdsptpversion.get_name_leafdata())
                if (self.cptpclockportdssyncinterval.is_set or self.cptpclockportdssyncinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportdssyncinterval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockPortDSDomainIndex" or name == "cPtpClockPortDSClockTypeIndex" or name == "cPtpClockPortDSClockInstanceIndex" or name == "cPtpClockPortDSPortNumberIndex" or name == "cPtpClockPortDSAnnouncementInterval" or name == "cPtpClockPortDSAnnounceRctTimeout" or name == "cPtpClockPortDSDelayMech" or name == "cPtpClockPortDSGrantDuration" or name == "cPtpClockPortDSMinDelayReqInterval" or name == "cPtpClockPortDSName" or name == "cPtpClockPortDSPeerDelayReqInterval" or name == "cPtpClockPortDSPeerMeanPathDelay" or name == "cPtpClockPortDSPortIdentity" or name == "cPtpClockPortDSPTPVersion" or name == "cPtpClockPortDSSyncInterval"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockPortDSDomainIndex"):
                    self.cptpclockportdsdomainindex = value
                    self.cptpclockportdsdomainindex.value_namespace = name_space
                    self.cptpclockportdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSClockTypeIndex"):
                    self.cptpclockportdsclocktypeindex = value
                    self.cptpclockportdsclocktypeindex.value_namespace = name_space
                    self.cptpclockportdsclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSClockInstanceIndex"):
                    self.cptpclockportdsclockinstanceindex = value
                    self.cptpclockportdsclockinstanceindex.value_namespace = name_space
                    self.cptpclockportdsclockinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSPortNumberIndex"):
                    self.cptpclockportdsportnumberindex = value
                    self.cptpclockportdsportnumberindex.value_namespace = name_space
                    self.cptpclockportdsportnumberindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSAnnouncementInterval"):
                    self.cptpclockportdsannouncementinterval = value
                    self.cptpclockportdsannouncementinterval.value_namespace = name_space
                    self.cptpclockportdsannouncementinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSAnnounceRctTimeout"):
                    self.cptpclockportdsannouncercttimeout = value
                    self.cptpclockportdsannouncercttimeout.value_namespace = name_space
                    self.cptpclockportdsannouncercttimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSDelayMech"):
                    self.cptpclockportdsdelaymech = value
                    self.cptpclockportdsdelaymech.value_namespace = name_space
                    self.cptpclockportdsdelaymech.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSGrantDuration"):
                    self.cptpclockportdsgrantduration = value
                    self.cptpclockportdsgrantduration.value_namespace = name_space
                    self.cptpclockportdsgrantduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSMinDelayReqInterval"):
                    self.cptpclockportdsmindelayreqinterval = value
                    self.cptpclockportdsmindelayreqinterval.value_namespace = name_space
                    self.cptpclockportdsmindelayreqinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSName"):
                    self.cptpclockportdsname = value
                    self.cptpclockportdsname.value_namespace = name_space
                    self.cptpclockportdsname.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSPeerDelayReqInterval"):
                    self.cptpclockportdspeerdelayreqinterval = value
                    self.cptpclockportdspeerdelayreqinterval.value_namespace = name_space
                    self.cptpclockportdspeerdelayreqinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSPeerMeanPathDelay"):
                    self.cptpclockportdspeermeanpathdelay = value
                    self.cptpclockportdspeermeanpathdelay.value_namespace = name_space
                    self.cptpclockportdspeermeanpathdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSPortIdentity"):
                    self.cptpclockportdsportidentity = value
                    self.cptpclockportdsportidentity.value_namespace = name_space
                    self.cptpclockportdsportidentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSPTPVersion"):
                    self.cptpclockportdsptpversion = value
                    self.cptpclockportdsptpversion.value_namespace = name_space
                    self.cptpclockportdsptpversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortDSSyncInterval"):
                    self.cptpclockportdssyncinterval = value
                    self.cptpclockportdssyncinterval.value_namespace = name_space
                    self.cptpclockportdssyncinterval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockportdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockportdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockPortDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockPortDSEntry"):
                for c in self.cptpclockportdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockportdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockPortDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockportrunningtable(Entity):
        """
        Table of information about the clock ports running dataset for
        a particular domain.
        
        .. attribute:: cptpclockportrunningentry
        
        	An entry in the table, containing runing dataset information about a single clock port
        	**type**\: list of    :py:class:`Cptpclockportrunningentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockportrunningtable, self).__init__()

            self.yang_name = "cPtpClockPortRunningTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockportrunningentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockportrunningtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockportrunningtable, self).__setattr__(name, value)


        class Cptpclockportrunningentry(Entity):
            """
            An entry in the table, containing runing dataset information
            about a single clock port.
            
            .. attribute:: cptpclockportrunningdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportrunningclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockportrunningclockinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportrunningportnumberindex  <key>
            
            	This object specifies the PTP portnumber associated with this clock port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportrunningencapsulationtype
            
            	This object specifies the type of encapsulation if the interface is adding extra  layers (eg. VLAN, Pseudowire encapsulation...) for the PTP messages
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportrunninginterfaceindex
            
            	This object specifies the interface on the router being used by the PTP Clock for PTP communication
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cptpclockportrunningipversion
            
            	This object specifirst the IP version being used for PTP communication (the mapping used)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportrunningname
            
            	This object specifies the PTP clock port name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cptpclockportrunningpacketsreceived
            
            	This object specifies the packets received on the clock port (cummulative)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cptpclockportrunningpacketssent
            
            	This object specifies the packets sent on the clock port (cummulative)
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cptpclockportrunningrole
            
            	This object specifies the Clock Role
            	**type**\:   :py:class:`Clockroletype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockroletype>`
            
            .. attribute:: cptpclockportrunningrxmode
            
            	This object specifie the clock receive mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\:   :py:class:`Clocktxmodetype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktxmodetype>`
            
            .. attribute:: cptpclockportrunningstate
            
            	This object specifies the port state returned by PTP engine.  initializing \- In this state a port initializes                its data sets, hardware, and                communication facilities. faulty       \- The fault state of the protocol. disabled     \- The port shall not place any                messages on its communication path. listening    \- The port is waiting for the                announceReceiptTimeout to expire or                to receive an Announce message from                a master. preMaster    \- The port shall behave in all respects                as though it were in the MASTER state                except that it shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, signaling, or                management messages. master       \- The port is behaving as a master port.             passive      \- The port shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, or signaling                messages, or management messages                that are a required response to                another management message uncalibrated \- The local port is preparing to                synchronize to the master port. slave        \- The port is synchronizing to the                selected master port
            	**type**\:   :py:class:`Clockportstate <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clockportstate>`
            
            .. attribute:: cptpclockportrunningtxmode
            
            	This object specifies the clock transmission mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\:   :py:class:`Clocktxmodetype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktxmodetype>`
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry, self).__init__()

                self.yang_name = "cPtpClockPortRunningEntry"
                self.yang_parent_name = "cPtpClockPortRunningTable"

                self.cptpclockportrunningdomainindex = YLeaf(YType.uint32, "cPtpClockPortRunningDomainIndex")

                self.cptpclockportrunningclocktypeindex = YLeaf(YType.enumeration, "cPtpClockPortRunningClockTypeIndex")

                self.cptpclockportrunningclockinstanceindex = YLeaf(YType.uint32, "cPtpClockPortRunningClockInstanceIndex")

                self.cptpclockportrunningportnumberindex = YLeaf(YType.uint32, "cPtpClockPortRunningPortNumberIndex")

                self.cptpclockportrunningencapsulationtype = YLeaf(YType.int32, "cPtpClockPortRunningEncapsulationType")

                self.cptpclockportrunninginterfaceindex = YLeaf(YType.int32, "cPtpClockPortRunningInterfaceIndex")

                self.cptpclockportrunningipversion = YLeaf(YType.int32, "cPtpClockPortRunningIPversion")

                self.cptpclockportrunningname = YLeaf(YType.str, "cPtpClockPortRunningName")

                self.cptpclockportrunningpacketsreceived = YLeaf(YType.uint64, "cPtpClockPortRunningPacketsReceived")

                self.cptpclockportrunningpacketssent = YLeaf(YType.uint64, "cPtpClockPortRunningPacketsSent")

                self.cptpclockportrunningrole = YLeaf(YType.enumeration, "cPtpClockPortRunningRole")

                self.cptpclockportrunningrxmode = YLeaf(YType.enumeration, "cPtpClockPortRunningRxMode")

                self.cptpclockportrunningstate = YLeaf(YType.enumeration, "cPtpClockPortRunningState")

                self.cptpclockportrunningtxmode = YLeaf(YType.enumeration, "cPtpClockPortRunningTxMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockportrunningdomainindex",
                                "cptpclockportrunningclocktypeindex",
                                "cptpclockportrunningclockinstanceindex",
                                "cptpclockportrunningportnumberindex",
                                "cptpclockportrunningencapsulationtype",
                                "cptpclockportrunninginterfaceindex",
                                "cptpclockportrunningipversion",
                                "cptpclockportrunningname",
                                "cptpclockportrunningpacketsreceived",
                                "cptpclockportrunningpacketssent",
                                "cptpclockportrunningrole",
                                "cptpclockportrunningrxmode",
                                "cptpclockportrunningstate",
                                "cptpclockportrunningtxmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockportrunningdomainindex.is_set or
                    self.cptpclockportrunningclocktypeindex.is_set or
                    self.cptpclockportrunningclockinstanceindex.is_set or
                    self.cptpclockportrunningportnumberindex.is_set or
                    self.cptpclockportrunningencapsulationtype.is_set or
                    self.cptpclockportrunninginterfaceindex.is_set or
                    self.cptpclockportrunningipversion.is_set or
                    self.cptpclockportrunningname.is_set or
                    self.cptpclockportrunningpacketsreceived.is_set or
                    self.cptpclockportrunningpacketssent.is_set or
                    self.cptpclockportrunningrole.is_set or
                    self.cptpclockportrunningrxmode.is_set or
                    self.cptpclockportrunningstate.is_set or
                    self.cptpclockportrunningtxmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockportrunningdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockportrunningclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockportrunningclockinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockportrunningportnumberindex.yfilter != YFilter.not_set or
                    self.cptpclockportrunningencapsulationtype.yfilter != YFilter.not_set or
                    self.cptpclockportrunninginterfaceindex.yfilter != YFilter.not_set or
                    self.cptpclockportrunningipversion.yfilter != YFilter.not_set or
                    self.cptpclockportrunningname.yfilter != YFilter.not_set or
                    self.cptpclockportrunningpacketsreceived.yfilter != YFilter.not_set or
                    self.cptpclockportrunningpacketssent.yfilter != YFilter.not_set or
                    self.cptpclockportrunningrole.yfilter != YFilter.not_set or
                    self.cptpclockportrunningrxmode.yfilter != YFilter.not_set or
                    self.cptpclockportrunningstate.yfilter != YFilter.not_set or
                    self.cptpclockportrunningtxmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockPortRunningEntry" + "[cPtpClockPortRunningDomainIndex='" + self.cptpclockportrunningdomainindex.get() + "']" + "[cPtpClockPortRunningClockTypeIndex='" + self.cptpclockportrunningclocktypeindex.get() + "']" + "[cPtpClockPortRunningClockInstanceIndex='" + self.cptpclockportrunningclockinstanceindex.get() + "']" + "[cPtpClockPortRunningPortNumberIndex='" + self.cptpclockportrunningportnumberindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortRunningTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockportrunningdomainindex.is_set or self.cptpclockportrunningdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningdomainindex.get_name_leafdata())
                if (self.cptpclockportrunningclocktypeindex.is_set or self.cptpclockportrunningclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningclocktypeindex.get_name_leafdata())
                if (self.cptpclockportrunningclockinstanceindex.is_set or self.cptpclockportrunningclockinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningclockinstanceindex.get_name_leafdata())
                if (self.cptpclockportrunningportnumberindex.is_set or self.cptpclockportrunningportnumberindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningportnumberindex.get_name_leafdata())
                if (self.cptpclockportrunningencapsulationtype.is_set or self.cptpclockportrunningencapsulationtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningencapsulationtype.get_name_leafdata())
                if (self.cptpclockportrunninginterfaceindex.is_set or self.cptpclockportrunninginterfaceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunninginterfaceindex.get_name_leafdata())
                if (self.cptpclockportrunningipversion.is_set or self.cptpclockportrunningipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningipversion.get_name_leafdata())
                if (self.cptpclockportrunningname.is_set or self.cptpclockportrunningname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningname.get_name_leafdata())
                if (self.cptpclockportrunningpacketsreceived.is_set or self.cptpclockportrunningpacketsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningpacketsreceived.get_name_leafdata())
                if (self.cptpclockportrunningpacketssent.is_set or self.cptpclockportrunningpacketssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningpacketssent.get_name_leafdata())
                if (self.cptpclockportrunningrole.is_set or self.cptpclockportrunningrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningrole.get_name_leafdata())
                if (self.cptpclockportrunningrxmode.is_set or self.cptpclockportrunningrxmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningrxmode.get_name_leafdata())
                if (self.cptpclockportrunningstate.is_set or self.cptpclockportrunningstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningstate.get_name_leafdata())
                if (self.cptpclockportrunningtxmode.is_set or self.cptpclockportrunningtxmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportrunningtxmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockPortRunningDomainIndex" or name == "cPtpClockPortRunningClockTypeIndex" or name == "cPtpClockPortRunningClockInstanceIndex" or name == "cPtpClockPortRunningPortNumberIndex" or name == "cPtpClockPortRunningEncapsulationType" or name == "cPtpClockPortRunningInterfaceIndex" or name == "cPtpClockPortRunningIPversion" or name == "cPtpClockPortRunningName" or name == "cPtpClockPortRunningPacketsReceived" or name == "cPtpClockPortRunningPacketsSent" or name == "cPtpClockPortRunningRole" or name == "cPtpClockPortRunningRxMode" or name == "cPtpClockPortRunningState" or name == "cPtpClockPortRunningTxMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockPortRunningDomainIndex"):
                    self.cptpclockportrunningdomainindex = value
                    self.cptpclockportrunningdomainindex.value_namespace = name_space
                    self.cptpclockportrunningdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningClockTypeIndex"):
                    self.cptpclockportrunningclocktypeindex = value
                    self.cptpclockportrunningclocktypeindex.value_namespace = name_space
                    self.cptpclockportrunningclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningClockInstanceIndex"):
                    self.cptpclockportrunningclockinstanceindex = value
                    self.cptpclockportrunningclockinstanceindex.value_namespace = name_space
                    self.cptpclockportrunningclockinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningPortNumberIndex"):
                    self.cptpclockportrunningportnumberindex = value
                    self.cptpclockportrunningportnumberindex.value_namespace = name_space
                    self.cptpclockportrunningportnumberindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningEncapsulationType"):
                    self.cptpclockportrunningencapsulationtype = value
                    self.cptpclockportrunningencapsulationtype.value_namespace = name_space
                    self.cptpclockportrunningencapsulationtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningInterfaceIndex"):
                    self.cptpclockportrunninginterfaceindex = value
                    self.cptpclockportrunninginterfaceindex.value_namespace = name_space
                    self.cptpclockportrunninginterfaceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningIPversion"):
                    self.cptpclockportrunningipversion = value
                    self.cptpclockportrunningipversion.value_namespace = name_space
                    self.cptpclockportrunningipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningName"):
                    self.cptpclockportrunningname = value
                    self.cptpclockportrunningname.value_namespace = name_space
                    self.cptpclockportrunningname.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningPacketsReceived"):
                    self.cptpclockportrunningpacketsreceived = value
                    self.cptpclockportrunningpacketsreceived.value_namespace = name_space
                    self.cptpclockportrunningpacketsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningPacketsSent"):
                    self.cptpclockportrunningpacketssent = value
                    self.cptpclockportrunningpacketssent.value_namespace = name_space
                    self.cptpclockportrunningpacketssent.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningRole"):
                    self.cptpclockportrunningrole = value
                    self.cptpclockportrunningrole.value_namespace = name_space
                    self.cptpclockportrunningrole.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningRxMode"):
                    self.cptpclockportrunningrxmode = value
                    self.cptpclockportrunningrxmode.value_namespace = name_space
                    self.cptpclockportrunningrxmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningState"):
                    self.cptpclockportrunningstate = value
                    self.cptpclockportrunningstate.value_namespace = name_space
                    self.cptpclockportrunningstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortRunningTxMode"):
                    self.cptpclockportrunningtxmode = value
                    self.cptpclockportrunningtxmode.value_namespace = name_space
                    self.cptpclockportrunningtxmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockportrunningentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockportrunningentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockPortRunningTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockPortRunningEntry"):
                for c in self.cptpclockportrunningentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockportrunningentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockPortRunningEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockporttransdstable(Entity):
        """
        Table of information about the Transparent clock ports running
        dataset for a particular domain.
        
        .. attribute:: cptpclockporttransdsentry
        
        	An entry in the table, containing clock port Transparent dataset information about a single clock port
        	**type**\: list of    :py:class:`Cptpclockporttransdsentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockporttransdstable, self).__init__()

            self.yang_name = "cPtpClockPortTransDSTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockporttransdsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockporttransdstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockporttransdstable, self).__setattr__(name, value)


        class Cptpclockporttransdsentry(Entity):
            """
            An entry in the table, containing clock port Transparent
            dataset information about a single clock port
            
            .. attribute:: cptpclockporttransdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockporttransdsinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockporttransdsportnumberindex  <key>
            
            	This object specifies the PTP port number associated with this port
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockporttransdsfaultyflag
            
            	This object specifies the value TRUE if the port is faulty and FALSE if the port is operating normally
            	**type**\:  bool
            
            .. attribute:: cptpclockporttransdslogminpdelayreqint
            
            	This object specifies the value of the logarithm to the base 2 of the minPdelayReqInterval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockporttransdspeermeanpathdelay
            
            	This object specifies, (if the delayMechanism used is P2P) the value is the estimate of the current one\-way propagation delay, i.e., <meanPathDelay> on the link attached to this port computed using the peer delay mechanism. If the value of the delayMechanism used is E2E, then the value will be zero
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cptpclockporttransdsportidentity
            
            	This object specifies the value of the PortIdentity attribute of the local port
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry, self).__init__()

                self.yang_name = "cPtpClockPortTransDSEntry"
                self.yang_parent_name = "cPtpClockPortTransDSTable"

                self.cptpclockporttransdsdomainindex = YLeaf(YType.uint32, "cPtpClockPortTransDSDomainIndex")

                self.cptpclockporttransdsinstanceindex = YLeaf(YType.uint32, "cPtpClockPortTransDSInstanceIndex")

                self.cptpclockporttransdsportnumberindex = YLeaf(YType.uint32, "cPtpClockPortTransDSPortNumberIndex")

                self.cptpclockporttransdsfaultyflag = YLeaf(YType.boolean, "cPtpClockPortTransDSFaultyFlag")

                self.cptpclockporttransdslogminpdelayreqint = YLeaf(YType.int32, "cPtpClockPortTransDSlogMinPdelayReqInt")

                self.cptpclockporttransdspeermeanpathdelay = YLeaf(YType.str, "cPtpClockPortTransDSPeerMeanPathDelay")

                self.cptpclockporttransdsportidentity = YLeaf(YType.str, "cPtpClockPortTransDSPortIdentity")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockporttransdsdomainindex",
                                "cptpclockporttransdsinstanceindex",
                                "cptpclockporttransdsportnumberindex",
                                "cptpclockporttransdsfaultyflag",
                                "cptpclockporttransdslogminpdelayreqint",
                                "cptpclockporttransdspeermeanpathdelay",
                                "cptpclockporttransdsportidentity") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockporttransdsdomainindex.is_set or
                    self.cptpclockporttransdsinstanceindex.is_set or
                    self.cptpclockporttransdsportnumberindex.is_set or
                    self.cptpclockporttransdsfaultyflag.is_set or
                    self.cptpclockporttransdslogminpdelayreqint.is_set or
                    self.cptpclockporttransdspeermeanpathdelay.is_set or
                    self.cptpclockporttransdsportidentity.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockporttransdsdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockporttransdsinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockporttransdsportnumberindex.yfilter != YFilter.not_set or
                    self.cptpclockporttransdsfaultyflag.yfilter != YFilter.not_set or
                    self.cptpclockporttransdslogminpdelayreqint.yfilter != YFilter.not_set or
                    self.cptpclockporttransdspeermeanpathdelay.yfilter != YFilter.not_set or
                    self.cptpclockporttransdsportidentity.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockPortTransDSEntry" + "[cPtpClockPortTransDSDomainIndex='" + self.cptpclockporttransdsdomainindex.get() + "']" + "[cPtpClockPortTransDSInstanceIndex='" + self.cptpclockporttransdsinstanceindex.get() + "']" + "[cPtpClockPortTransDSPortNumberIndex='" + self.cptpclockporttransdsportnumberindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortTransDSTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockporttransdsdomainindex.is_set or self.cptpclockporttransdsdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdsdomainindex.get_name_leafdata())
                if (self.cptpclockporttransdsinstanceindex.is_set or self.cptpclockporttransdsinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdsinstanceindex.get_name_leafdata())
                if (self.cptpclockporttransdsportnumberindex.is_set or self.cptpclockporttransdsportnumberindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdsportnumberindex.get_name_leafdata())
                if (self.cptpclockporttransdsfaultyflag.is_set or self.cptpclockporttransdsfaultyflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdsfaultyflag.get_name_leafdata())
                if (self.cptpclockporttransdslogminpdelayreqint.is_set or self.cptpclockporttransdslogminpdelayreqint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdslogminpdelayreqint.get_name_leafdata())
                if (self.cptpclockporttransdspeermeanpathdelay.is_set or self.cptpclockporttransdspeermeanpathdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdspeermeanpathdelay.get_name_leafdata())
                if (self.cptpclockporttransdsportidentity.is_set or self.cptpclockporttransdsportidentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockporttransdsportidentity.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockPortTransDSDomainIndex" or name == "cPtpClockPortTransDSInstanceIndex" or name == "cPtpClockPortTransDSPortNumberIndex" or name == "cPtpClockPortTransDSFaultyFlag" or name == "cPtpClockPortTransDSlogMinPdelayReqInt" or name == "cPtpClockPortTransDSPeerMeanPathDelay" or name == "cPtpClockPortTransDSPortIdentity"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockPortTransDSDomainIndex"):
                    self.cptpclockporttransdsdomainindex = value
                    self.cptpclockporttransdsdomainindex.value_namespace = name_space
                    self.cptpclockporttransdsdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTransDSInstanceIndex"):
                    self.cptpclockporttransdsinstanceindex = value
                    self.cptpclockporttransdsinstanceindex.value_namespace = name_space
                    self.cptpclockporttransdsinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTransDSPortNumberIndex"):
                    self.cptpclockporttransdsportnumberindex = value
                    self.cptpclockporttransdsportnumberindex.value_namespace = name_space
                    self.cptpclockporttransdsportnumberindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTransDSFaultyFlag"):
                    self.cptpclockporttransdsfaultyflag = value
                    self.cptpclockporttransdsfaultyflag.value_namespace = name_space
                    self.cptpclockporttransdsfaultyflag.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTransDSlogMinPdelayReqInt"):
                    self.cptpclockporttransdslogminpdelayreqint = value
                    self.cptpclockporttransdslogminpdelayreqint.value_namespace = name_space
                    self.cptpclockporttransdslogminpdelayreqint.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTransDSPeerMeanPathDelay"):
                    self.cptpclockporttransdspeermeanpathdelay = value
                    self.cptpclockporttransdspeermeanpathdelay.value_namespace = name_space
                    self.cptpclockporttransdspeermeanpathdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortTransDSPortIdentity"):
                    self.cptpclockporttransdsportidentity = value
                    self.cptpclockporttransdsportidentity.value_namespace = name_space
                    self.cptpclockporttransdsportidentity.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockporttransdsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockporttransdsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockPortTransDSTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockPortTransDSEntry"):
                for c in self.cptpclockporttransdsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockporttransdsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockPortTransDSEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cptpclockportassociatetable(Entity):
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
        	**type**\: list of    :py:class:`Cptpclockportassociateentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            super(CiscoPtpMib.Cptpclockportassociatetable, self).__init__()

            self.yang_name = "cPtpClockPortAssociateTable"
            self.yang_parent_name = "CISCO-PTP-MIB"

            self.cptpclockportassociateentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoPtpMib.Cptpclockportassociatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPtpMib.Cptpclockportassociatetable, self).__setattr__(name, value)


        class Cptpclockportassociateentry(Entity):
            """
            An entry in the table, containing information about a single
            associated port for the given clockport.
            
            .. attribute:: cptpclockportcurrentdomainindex  <key>
            
            	This object specifies the given port's domain number
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportcurrentclocktypeindex  <key>
            
            	This object specifies the given port's clock type
            	**type**\:   :py:class:`Clocktype <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.Clocktype>`
            
            .. attribute:: cptpclockportcurrentclockinstanceindex  <key>
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportcurrentportnumberindex  <key>
            
            	This object specifies the PTP Port Number for the given port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cptpclockportassociateportindex  <key>
            
            	This object specifies the associated port's serial number in the current port's context
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportassociateaddress
            
            	This object specifies the peer port's network address used for PTP communication
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cptpclockportassociateaddresstype
            
            	This object specifies the peer port's network address type used for PTP communication
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cptpclockportassociateinerrors
            
            	This object specifies the input errors associated with the peer port
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cptpclockportassociateouterrors
            
            	This object specifies the output errors associated with the peer port
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cptpclockportassociatepacketsreceived
            
            	The number of packets received from this peer port by the current port
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cptpclockportassociatepacketssent
            
            	The number of packets sent to this peer port from the current port
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                super(CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry, self).__init__()

                self.yang_name = "cPtpClockPortAssociateEntry"
                self.yang_parent_name = "cPtpClockPortAssociateTable"

                self.cptpclockportcurrentdomainindex = YLeaf(YType.uint32, "cPtpClockPortCurrentDomainIndex")

                self.cptpclockportcurrentclocktypeindex = YLeaf(YType.enumeration, "cPtpClockPortCurrentClockTypeIndex")

                self.cptpclockportcurrentclockinstanceindex = YLeaf(YType.uint32, "cPtpClockPortCurrentClockInstanceIndex")

                self.cptpclockportcurrentportnumberindex = YLeaf(YType.uint32, "cPtpClockPortCurrentPortNumberIndex")

                self.cptpclockportassociateportindex = YLeaf(YType.uint32, "cPtpClockPortAssociatePortIndex")

                self.cptpclockportassociateaddress = YLeaf(YType.str, "cPtpClockPortAssociateAddress")

                self.cptpclockportassociateaddresstype = YLeaf(YType.enumeration, "cPtpClockPortAssociateAddressType")

                self.cptpclockportassociateinerrors = YLeaf(YType.uint64, "cPtpClockPortAssociateInErrors")

                self.cptpclockportassociateouterrors = YLeaf(YType.uint64, "cPtpClockPortAssociateOutErrors")

                self.cptpclockportassociatepacketsreceived = YLeaf(YType.uint64, "cPtpClockPortAssociatePacketsReceived")

                self.cptpclockportassociatepacketssent = YLeaf(YType.uint64, "cPtpClockPortAssociatePacketsSent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cptpclockportcurrentdomainindex",
                                "cptpclockportcurrentclocktypeindex",
                                "cptpclockportcurrentclockinstanceindex",
                                "cptpclockportcurrentportnumberindex",
                                "cptpclockportassociateportindex",
                                "cptpclockportassociateaddress",
                                "cptpclockportassociateaddresstype",
                                "cptpclockportassociateinerrors",
                                "cptpclockportassociateouterrors",
                                "cptpclockportassociatepacketsreceived",
                                "cptpclockportassociatepacketssent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cptpclockportcurrentdomainindex.is_set or
                    self.cptpclockportcurrentclocktypeindex.is_set or
                    self.cptpclockportcurrentclockinstanceindex.is_set or
                    self.cptpclockportcurrentportnumberindex.is_set or
                    self.cptpclockportassociateportindex.is_set or
                    self.cptpclockportassociateaddress.is_set or
                    self.cptpclockportassociateaddresstype.is_set or
                    self.cptpclockportassociateinerrors.is_set or
                    self.cptpclockportassociateouterrors.is_set or
                    self.cptpclockportassociatepacketsreceived.is_set or
                    self.cptpclockportassociatepacketssent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cptpclockportcurrentdomainindex.yfilter != YFilter.not_set or
                    self.cptpclockportcurrentclocktypeindex.yfilter != YFilter.not_set or
                    self.cptpclockportcurrentclockinstanceindex.yfilter != YFilter.not_set or
                    self.cptpclockportcurrentportnumberindex.yfilter != YFilter.not_set or
                    self.cptpclockportassociateportindex.yfilter != YFilter.not_set or
                    self.cptpclockportassociateaddress.yfilter != YFilter.not_set or
                    self.cptpclockportassociateaddresstype.yfilter != YFilter.not_set or
                    self.cptpclockportassociateinerrors.yfilter != YFilter.not_set or
                    self.cptpclockportassociateouterrors.yfilter != YFilter.not_set or
                    self.cptpclockportassociatepacketsreceived.yfilter != YFilter.not_set or
                    self.cptpclockportassociatepacketssent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cPtpClockPortAssociateEntry" + "[cPtpClockPortCurrentDomainIndex='" + self.cptpclockportcurrentdomainindex.get() + "']" + "[cPtpClockPortCurrentClockTypeIndex='" + self.cptpclockportcurrentclocktypeindex.get() + "']" + "[cPtpClockPortCurrentClockInstanceIndex='" + self.cptpclockportcurrentclockinstanceindex.get() + "']" + "[cPtpClockPortCurrentPortNumberIndex='" + self.cptpclockportcurrentportnumberindex.get() + "']" + "[cPtpClockPortAssociatePortIndex='" + self.cptpclockportassociateportindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/cPtpClockPortAssociateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cptpclockportcurrentdomainindex.is_set or self.cptpclockportcurrentdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportcurrentdomainindex.get_name_leafdata())
                if (self.cptpclockportcurrentclocktypeindex.is_set or self.cptpclockportcurrentclocktypeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportcurrentclocktypeindex.get_name_leafdata())
                if (self.cptpclockportcurrentclockinstanceindex.is_set or self.cptpclockportcurrentclockinstanceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportcurrentclockinstanceindex.get_name_leafdata())
                if (self.cptpclockportcurrentportnumberindex.is_set or self.cptpclockportcurrentportnumberindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportcurrentportnumberindex.get_name_leafdata())
                if (self.cptpclockportassociateportindex.is_set or self.cptpclockportassociateportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociateportindex.get_name_leafdata())
                if (self.cptpclockportassociateaddress.is_set or self.cptpclockportassociateaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociateaddress.get_name_leafdata())
                if (self.cptpclockportassociateaddresstype.is_set or self.cptpclockportassociateaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociateaddresstype.get_name_leafdata())
                if (self.cptpclockportassociateinerrors.is_set or self.cptpclockportassociateinerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociateinerrors.get_name_leafdata())
                if (self.cptpclockportassociateouterrors.is_set or self.cptpclockportassociateouterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociateouterrors.get_name_leafdata())
                if (self.cptpclockportassociatepacketsreceived.is_set or self.cptpclockportassociatepacketsreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociatepacketsreceived.get_name_leafdata())
                if (self.cptpclockportassociatepacketssent.is_set or self.cptpclockportassociatepacketssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cptpclockportassociatepacketssent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cPtpClockPortCurrentDomainIndex" or name == "cPtpClockPortCurrentClockTypeIndex" or name == "cPtpClockPortCurrentClockInstanceIndex" or name == "cPtpClockPortCurrentPortNumberIndex" or name == "cPtpClockPortAssociatePortIndex" or name == "cPtpClockPortAssociateAddress" or name == "cPtpClockPortAssociateAddressType" or name == "cPtpClockPortAssociateInErrors" or name == "cPtpClockPortAssociateOutErrors" or name == "cPtpClockPortAssociatePacketsReceived" or name == "cPtpClockPortAssociatePacketsSent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cPtpClockPortCurrentDomainIndex"):
                    self.cptpclockportcurrentdomainindex = value
                    self.cptpclockportcurrentdomainindex.value_namespace = name_space
                    self.cptpclockportcurrentdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortCurrentClockTypeIndex"):
                    self.cptpclockportcurrentclocktypeindex = value
                    self.cptpclockportcurrentclocktypeindex.value_namespace = name_space
                    self.cptpclockportcurrentclocktypeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortCurrentClockInstanceIndex"):
                    self.cptpclockportcurrentclockinstanceindex = value
                    self.cptpclockportcurrentclockinstanceindex.value_namespace = name_space
                    self.cptpclockportcurrentclockinstanceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortCurrentPortNumberIndex"):
                    self.cptpclockportcurrentportnumberindex = value
                    self.cptpclockportcurrentportnumberindex.value_namespace = name_space
                    self.cptpclockportcurrentportnumberindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociatePortIndex"):
                    self.cptpclockportassociateportindex = value
                    self.cptpclockportassociateportindex.value_namespace = name_space
                    self.cptpclockportassociateportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociateAddress"):
                    self.cptpclockportassociateaddress = value
                    self.cptpclockportassociateaddress.value_namespace = name_space
                    self.cptpclockportassociateaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociateAddressType"):
                    self.cptpclockportassociateaddresstype = value
                    self.cptpclockportassociateaddresstype.value_namespace = name_space
                    self.cptpclockportassociateaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociateInErrors"):
                    self.cptpclockportassociateinerrors = value
                    self.cptpclockportassociateinerrors.value_namespace = name_space
                    self.cptpclockportassociateinerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociateOutErrors"):
                    self.cptpclockportassociateouterrors = value
                    self.cptpclockportassociateouterrors.value_namespace = name_space
                    self.cptpclockportassociateouterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociatePacketsReceived"):
                    self.cptpclockportassociatepacketsreceived = value
                    self.cptpclockportassociatepacketsreceived.value_namespace = name_space
                    self.cptpclockportassociatepacketsreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "cPtpClockPortAssociatePacketsSent"):
                    self.cptpclockportassociatepacketssent = value
                    self.cptpclockportassociatepacketssent.value_namespace = name_space
                    self.cptpclockportassociatepacketssent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cptpclockportassociateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cptpclockportassociateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cPtpClockPortAssociateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cPtpClockPortAssociateEntry"):
                for c in self.cptpclockportassociateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cptpclockportassociateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cPtpClockPortAssociateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciscoptpmibsysteminfo is not None and self.ciscoptpmibsysteminfo.has_data()) or
            (self.cptpclockcurrentdstable is not None and self.cptpclockcurrentdstable.has_data()) or
            (self.cptpclockdefaultdstable is not None and self.cptpclockdefaultdstable.has_data()) or
            (self.cptpclocknodetable is not None and self.cptpclocknodetable.has_data()) or
            (self.cptpclockparentdstable is not None and self.cptpclockparentdstable.has_data()) or
            (self.cptpclockportassociatetable is not None and self.cptpclockportassociatetable.has_data()) or
            (self.cptpclockportdstable is not None and self.cptpclockportdstable.has_data()) or
            (self.cptpclockportrunningtable is not None and self.cptpclockportrunningtable.has_data()) or
            (self.cptpclockporttable is not None and self.cptpclockporttable.has_data()) or
            (self.cptpclockporttransdstable is not None and self.cptpclockporttransdstable.has_data()) or
            (self.cptpclockrunningtable is not None and self.cptpclockrunningtable.has_data()) or
            (self.cptpclocktimepropertiesdstable is not None and self.cptpclocktimepropertiesdstable.has_data()) or
            (self.cptpclocktransdefaultdstable is not None and self.cptpclocktransdefaultdstable.has_data()) or
            (self.cptpsystemdomaintable is not None and self.cptpsystemdomaintable.has_data()) or
            (self.cptpsystemtable is not None and self.cptpsystemtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscoptpmibsysteminfo is not None and self.ciscoptpmibsysteminfo.has_operation()) or
            (self.cptpclockcurrentdstable is not None and self.cptpclockcurrentdstable.has_operation()) or
            (self.cptpclockdefaultdstable is not None and self.cptpclockdefaultdstable.has_operation()) or
            (self.cptpclocknodetable is not None and self.cptpclocknodetable.has_operation()) or
            (self.cptpclockparentdstable is not None and self.cptpclockparentdstable.has_operation()) or
            (self.cptpclockportassociatetable is not None and self.cptpclockportassociatetable.has_operation()) or
            (self.cptpclockportdstable is not None and self.cptpclockportdstable.has_operation()) or
            (self.cptpclockportrunningtable is not None and self.cptpclockportrunningtable.has_operation()) or
            (self.cptpclockporttable is not None and self.cptpclockporttable.has_operation()) or
            (self.cptpclockporttransdstable is not None and self.cptpclockporttransdstable.has_operation()) or
            (self.cptpclockrunningtable is not None and self.cptpclockrunningtable.has_operation()) or
            (self.cptpclocktimepropertiesdstable is not None and self.cptpclocktimepropertiesdstable.has_operation()) or
            (self.cptpclocktransdefaultdstable is not None and self.cptpclocktransdefaultdstable.has_operation()) or
            (self.cptpsystemdomaintable is not None and self.cptpsystemdomaintable.has_operation()) or
            (self.cptpsystemtable is not None and self.cptpsystemtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-PTP-MIB:CISCO-PTP-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "ciscoPtpMIBSystemInfo"):
            if (self.ciscoptpmibsysteminfo is None):
                self.ciscoptpmibsysteminfo = CiscoPtpMib.Ciscoptpmibsysteminfo()
                self.ciscoptpmibsysteminfo.parent = self
                self._children_name_map["ciscoptpmibsysteminfo"] = "ciscoPtpMIBSystemInfo"
            return self.ciscoptpmibsysteminfo

        if (child_yang_name == "cPtpClockCurrentDSTable"):
            if (self.cptpclockcurrentdstable is None):
                self.cptpclockcurrentdstable = CiscoPtpMib.Cptpclockcurrentdstable()
                self.cptpclockcurrentdstable.parent = self
                self._children_name_map["cptpclockcurrentdstable"] = "cPtpClockCurrentDSTable"
            return self.cptpclockcurrentdstable

        if (child_yang_name == "cPtpClockDefaultDSTable"):
            if (self.cptpclockdefaultdstable is None):
                self.cptpclockdefaultdstable = CiscoPtpMib.Cptpclockdefaultdstable()
                self.cptpclockdefaultdstable.parent = self
                self._children_name_map["cptpclockdefaultdstable"] = "cPtpClockDefaultDSTable"
            return self.cptpclockdefaultdstable

        if (child_yang_name == "cPtpClockNodeTable"):
            if (self.cptpclocknodetable is None):
                self.cptpclocknodetable = CiscoPtpMib.Cptpclocknodetable()
                self.cptpclocknodetable.parent = self
                self._children_name_map["cptpclocknodetable"] = "cPtpClockNodeTable"
            return self.cptpclocknodetable

        if (child_yang_name == "cPtpClockParentDSTable"):
            if (self.cptpclockparentdstable is None):
                self.cptpclockparentdstable = CiscoPtpMib.Cptpclockparentdstable()
                self.cptpclockparentdstable.parent = self
                self._children_name_map["cptpclockparentdstable"] = "cPtpClockParentDSTable"
            return self.cptpclockparentdstable

        if (child_yang_name == "cPtpClockPortAssociateTable"):
            if (self.cptpclockportassociatetable is None):
                self.cptpclockportassociatetable = CiscoPtpMib.Cptpclockportassociatetable()
                self.cptpclockportassociatetable.parent = self
                self._children_name_map["cptpclockportassociatetable"] = "cPtpClockPortAssociateTable"
            return self.cptpclockportassociatetable

        if (child_yang_name == "cPtpClockPortDSTable"):
            if (self.cptpclockportdstable is None):
                self.cptpclockportdstable = CiscoPtpMib.Cptpclockportdstable()
                self.cptpclockportdstable.parent = self
                self._children_name_map["cptpclockportdstable"] = "cPtpClockPortDSTable"
            return self.cptpclockportdstable

        if (child_yang_name == "cPtpClockPortRunningTable"):
            if (self.cptpclockportrunningtable is None):
                self.cptpclockportrunningtable = CiscoPtpMib.Cptpclockportrunningtable()
                self.cptpclockportrunningtable.parent = self
                self._children_name_map["cptpclockportrunningtable"] = "cPtpClockPortRunningTable"
            return self.cptpclockportrunningtable

        if (child_yang_name == "cPtpClockPortTable"):
            if (self.cptpclockporttable is None):
                self.cptpclockporttable = CiscoPtpMib.Cptpclockporttable()
                self.cptpclockporttable.parent = self
                self._children_name_map["cptpclockporttable"] = "cPtpClockPortTable"
            return self.cptpclockporttable

        if (child_yang_name == "cPtpClockPortTransDSTable"):
            if (self.cptpclockporttransdstable is None):
                self.cptpclockporttransdstable = CiscoPtpMib.Cptpclockporttransdstable()
                self.cptpclockporttransdstable.parent = self
                self._children_name_map["cptpclockporttransdstable"] = "cPtpClockPortTransDSTable"
            return self.cptpclockporttransdstable

        if (child_yang_name == "cPtpClockRunningTable"):
            if (self.cptpclockrunningtable is None):
                self.cptpclockrunningtable = CiscoPtpMib.Cptpclockrunningtable()
                self.cptpclockrunningtable.parent = self
                self._children_name_map["cptpclockrunningtable"] = "cPtpClockRunningTable"
            return self.cptpclockrunningtable

        if (child_yang_name == "cPtpClockTimePropertiesDSTable"):
            if (self.cptpclocktimepropertiesdstable is None):
                self.cptpclocktimepropertiesdstable = CiscoPtpMib.Cptpclocktimepropertiesdstable()
                self.cptpclocktimepropertiesdstable.parent = self
                self._children_name_map["cptpclocktimepropertiesdstable"] = "cPtpClockTimePropertiesDSTable"
            return self.cptpclocktimepropertiesdstable

        if (child_yang_name == "cPtpClockTransDefaultDSTable"):
            if (self.cptpclocktransdefaultdstable is None):
                self.cptpclocktransdefaultdstable = CiscoPtpMib.Cptpclocktransdefaultdstable()
                self.cptpclocktransdefaultdstable.parent = self
                self._children_name_map["cptpclocktransdefaultdstable"] = "cPtpClockTransDefaultDSTable"
            return self.cptpclocktransdefaultdstable

        if (child_yang_name == "cPtpSystemDomainTable"):
            if (self.cptpsystemdomaintable is None):
                self.cptpsystemdomaintable = CiscoPtpMib.Cptpsystemdomaintable()
                self.cptpsystemdomaintable.parent = self
                self._children_name_map["cptpsystemdomaintable"] = "cPtpSystemDomainTable"
            return self.cptpsystemdomaintable

        if (child_yang_name == "cPtpSystemTable"):
            if (self.cptpsystemtable is None):
                self.cptpsystemtable = CiscoPtpMib.Cptpsystemtable()
                self.cptpsystemtable.parent = self
                self._children_name_map["cptpsystemtable"] = "cPtpSystemTable"
            return self.cptpsystemtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoPtpMIBSystemInfo" or name == "cPtpClockCurrentDSTable" or name == "cPtpClockDefaultDSTable" or name == "cPtpClockNodeTable" or name == "cPtpClockParentDSTable" or name == "cPtpClockPortAssociateTable" or name == "cPtpClockPortDSTable" or name == "cPtpClockPortRunningTable" or name == "cPtpClockPortTable" or name == "cPtpClockPortTransDSTable" or name == "cPtpClockRunningTable" or name == "cPtpClockTimePropertiesDSTable" or name == "cPtpClockTransDefaultDSTable" or name == "cPtpSystemDomainTable" or name == "cPtpSystemTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoPtpMib()
        return self._top_entity

