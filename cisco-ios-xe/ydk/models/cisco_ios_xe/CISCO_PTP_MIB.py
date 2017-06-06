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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ClockmechanismtypeEnum(Enum):
    """
    ClockmechanismtypeEnum

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

    e2e = 1

    p2p = 2

    disabled = 254


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockmechanismtypeEnum']


class ClockportstateEnum(Enum):
    """
    ClockportstateEnum

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

    initializing = 1

    faulty = 2

    disabled = 3

    listening = 4

    preMaster = 5

    master = 6

    passive = 7

    uncalibrated = 8

    slave = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockportstateEnum']


class ClockprofiletypeEnum(Enum):
    """
    ClockprofiletypeEnum

    Clock Profile used. From [1] section 3.1.30, Profile is the set

    of allowed Precision Time Protocol (PTP) features applicable to

    a device.

    .. data:: default = 1

    .. data:: telecom = 2

    .. data:: vendorspecific = 3

    """

    default = 1

    telecom = 2

    vendorspecific = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockprofiletypeEnum']


class ClockqualityaccuracytypeEnum(Enum):
    """
    ClockqualityaccuracytypeEnum

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

    reserved00 = 1

    nanoSecond25 = 32

    nanoSecond100 = 33

    nanoSecond250 = 34

    microSec1 = 35

    microSec2dot5 = 36

    microSec10 = 37

    microSec25 = 38

    microSec100 = 39

    microSec250 = 40

    milliSec1 = 41

    milliSec2dot5 = 42

    milliSec10 = 43

    milliSec25 = 44

    milliSec100 = 45

    milliSec250 = 46

    second1 = 47

    second10 = 48

    secondGreater10 = 49

    unknown = 254

    reserved255 = 255


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockqualityaccuracytypeEnum']


class ClockroletypeEnum(Enum):
    """
    ClockroletypeEnum

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

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockroletypeEnum']


class ClockstatetypeEnum(Enum):
    """
    ClockstatetypeEnum

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

    freerun = 1

    holdover = 2

    acquiring = 3

    frequencyLocked = 4

    phaseAligned = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockstatetypeEnum']


class ClocktimesourcetypeEnum(Enum):
    """
    ClocktimesourcetypeEnum

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

    atomicClock = 16

    gps = 32

    terrestrialRadio = 48

    ptp = 64

    ntp = 80

    handSet = 96

    other = 144

    internalOsillator = 160


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClocktimesourcetypeEnum']


class ClocktxmodetypeEnum(Enum):
    """
    ClocktxmodetypeEnum

    Transmission mode.

    unicast. Using unicast commnuication channel.

    multicast. Using Multicast communication channel.

    multicast\-mix. Using multicast\-unicast communication channel

    .. data:: unicast = 1

    .. data:: multicast = 2

    .. data:: multicastmix = 3

    """

    unicast = 1

    multicast = 2

    multicastmix = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClocktxmodetypeEnum']


class ClocktypeEnum(Enum):
    """
    ClocktypeEnum

    The clock types as defined in the MIB module description.

    .. data:: ordinaryClock = 1

    .. data:: boundaryClock = 2

    .. data:: transparentClock = 3

    .. data:: boundaryNode = 4

    """

    ordinaryClock = 1

    boundaryClock = 2

    transparentClock = 3

    boundaryNode = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClocktypeEnum']



class CiscoPtpMib(object):
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
        self.ciscoptpmibsysteminfo = CiscoPtpMib.Ciscoptpmibsysteminfo()
        self.ciscoptpmibsysteminfo.parent = self
        self.cptpclockcurrentdstable = CiscoPtpMib.Cptpclockcurrentdstable()
        self.cptpclockcurrentdstable.parent = self
        self.cptpclockdefaultdstable = CiscoPtpMib.Cptpclockdefaultdstable()
        self.cptpclockdefaultdstable.parent = self
        self.cptpclocknodetable = CiscoPtpMib.Cptpclocknodetable()
        self.cptpclocknodetable.parent = self
        self.cptpclockparentdstable = CiscoPtpMib.Cptpclockparentdstable()
        self.cptpclockparentdstable.parent = self
        self.cptpclockportassociatetable = CiscoPtpMib.Cptpclockportassociatetable()
        self.cptpclockportassociatetable.parent = self
        self.cptpclockportdstable = CiscoPtpMib.Cptpclockportdstable()
        self.cptpclockportdstable.parent = self
        self.cptpclockportrunningtable = CiscoPtpMib.Cptpclockportrunningtable()
        self.cptpclockportrunningtable.parent = self
        self.cptpclockporttable = CiscoPtpMib.Cptpclockporttable()
        self.cptpclockporttable.parent = self
        self.cptpclockporttransdstable = CiscoPtpMib.Cptpclockporttransdstable()
        self.cptpclockporttransdstable.parent = self
        self.cptpclockrunningtable = CiscoPtpMib.Cptpclockrunningtable()
        self.cptpclockrunningtable.parent = self
        self.cptpclocktimepropertiesdstable = CiscoPtpMib.Cptpclocktimepropertiesdstable()
        self.cptpclocktimepropertiesdstable.parent = self
        self.cptpclocktransdefaultdstable = CiscoPtpMib.Cptpclocktransdefaultdstable()
        self.cptpclocktransdefaultdstable.parent = self
        self.cptpsystemdomaintable = CiscoPtpMib.Cptpsystemdomaintable()
        self.cptpsystemdomaintable.parent = self
        self.cptpsystemtable = CiscoPtpMib.Cptpsystemtable()
        self.cptpsystemtable.parent = self


    class Ciscoptpmibsysteminfo(object):
        """
        
        
        .. attribute:: cptpsystemprofile
        
        	This object specifies the PTP Profile implemented on the system
        	**type**\:   :py:class:`ClockprofiletypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockprofiletypeEnum>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpsystemprofile = None

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:ciscoPtpMIBSystemInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpsystemprofile is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Ciscoptpmibsysteminfo']['meta_info']


    class Cptpsystemtable(object):
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
            self.parent = None
            self.cptpsystementry = YList()
            self.cptpsystementry.parent = self
            self.cptpsystementry.name = 'cptpsystementry'


        class Cptpsystementry(object):
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
                self.parent = None
                self.cptpdomainindex = None
                self.cptpinstanceindex = None
                self.cptpdomainclockportphysicalinterfacestotal = None
                self.cptpdomainclockportstotal = None

            @property
            def _common_path(self):
                if self.cptpdomainindex is None:
                    raise YPYModelError('Key property cptpdomainindex is None')
                if self.cptpinstanceindex is None:
                    raise YPYModelError('Key property cptpinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemTable/CISCO-PTP-MIB:cPtpSystemEntry[CISCO-PTP-MIB:cPtpDomainIndex = ' + str(self.cptpdomainindex) + '][CISCO-PTP-MIB:cPtpInstanceIndex = ' + str(self.cptpinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpdomainindex is not None:
                    return True

                if self.cptpinstanceindex is not None:
                    return True

                if self.cptpdomainclockportphysicalinterfacestotal is not None:
                    return True

                if self.cptpdomainclockportstotal is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpsystemtable.Cptpsystementry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpsystementry is not None:
                for child_ref in self.cptpsystementry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpsystemtable']['meta_info']


    class Cptpsystemdomaintable(object):
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
            self.parent = None
            self.cptpsystemdomainentry = YList()
            self.cptpsystemdomainentry.parent = self
            self.cptpsystemdomainentry.name = 'cptpsystemdomainentry'


        class Cptpsystemdomainentry(object):
            """
            An entry in the table, containing information about a single
            clock mode for the PTP system. A row entry gets added when PTP
            clocks are configured on the router.
            
            .. attribute:: cptpsystemdomainclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
            .. attribute:: cptpsystemdomaintotals
            
            	This object specifies the  total number of PTP domains for this particular clock type configured in this node
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: domains
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpsystemdomainclocktypeindex = None
                self.cptpsystemdomaintotals = None

            @property
            def _common_path(self):
                if self.cptpsystemdomainclocktypeindex is None:
                    raise YPYModelError('Key property cptpsystemdomainclocktypeindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemDomainTable/CISCO-PTP-MIB:cPtpSystemDomainEntry[CISCO-PTP-MIB:cPtpSystemDomainClockTypeIndex = ' + str(self.cptpsystemdomainclocktypeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpsystemdomainclocktypeindex is not None:
                    return True

                if self.cptpsystemdomaintotals is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemDomainTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpsystemdomainentry is not None:
                for child_ref in self.cptpsystemdomainentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpsystemdomaintable']['meta_info']


    class Cptpclocknodetable(object):
        """
        Table of information about the PTP system for a given domain.
        
        .. attribute:: cptpclocknodeentry
        
        	An entry in the table, containing information about a single domain. A entry is added when a new PTP clock domain is configured on the router
        	**type**\: list of    :py:class:`Cptpclocknodeentry <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry>`
        
        

        """

        _prefix = 'CISCO-PTP-MIB'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclocknodeentry = YList()
            self.cptpclocknodeentry.parent = self
            self.cptpclocknodeentry.name = 'cptpclocknodeentry'


        class Cptpclocknodeentry(object):
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
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
                self.parent = None
                self.cptpclockdomainindex = None
                self.cptpclocktypeindex = None
                self.cptpclockinstanceindex = None
                self.cptpclockinput1ppsenabled = None
                self.cptpclockinput1ppsinterface = None
                self.cptpclockinputfrequencyenabled = None
                self.cptpclockoutput1ppsenabled = None
                self.cptpclockoutput1ppsinterface = None
                self.cptpclockoutput1ppsoffsetenabled = None
                self.cptpclockoutput1ppsoffsetnegative = None
                self.cptpclockoutput1ppsoffsetvalue = None
                self.cptpclocktodenabled = None
                self.cptpclocktodinterface = None

            @property
            def _common_path(self):
                if self.cptpclockdomainindex is None:
                    raise YPYModelError('Key property cptpclockdomainindex is None')
                if self.cptpclocktypeindex is None:
                    raise YPYModelError('Key property cptpclocktypeindex is None')
                if self.cptpclockinstanceindex is None:
                    raise YPYModelError('Key property cptpclockinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockNodeTable/CISCO-PTP-MIB:cPtpClockNodeEntry[CISCO-PTP-MIB:cPtpClockDomainIndex = ' + str(self.cptpclockdomainindex) + '][CISCO-PTP-MIB:cPtpClockTypeIndex = ' + str(self.cptpclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockInstanceIndex = ' + str(self.cptpclockinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockdomainindex is not None:
                    return True

                if self.cptpclocktypeindex is not None:
                    return True

                if self.cptpclockinstanceindex is not None:
                    return True

                if self.cptpclockinput1ppsenabled is not None:
                    return True

                if self.cptpclockinput1ppsinterface is not None:
                    return True

                if self.cptpclockinputfrequencyenabled is not None:
                    return True

                if self.cptpclockoutput1ppsenabled is not None:
                    return True

                if self.cptpclockoutput1ppsinterface is not None:
                    return True

                if self.cptpclockoutput1ppsoffsetenabled is not None:
                    return True

                if self.cptpclockoutput1ppsoffsetnegative is not None:
                    return True

                if self.cptpclockoutput1ppsoffsetvalue is not None:
                    return True

                if self.cptpclocktodenabled is not None:
                    return True

                if self.cptpclocktodinterface is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockNodeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclocknodeentry is not None:
                for child_ref in self.cptpclocknodeentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclocknodetable']['meta_info']


    class Cptpclockcurrentdstable(object):
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
            self.parent = None
            self.cptpclockcurrentdsentry = YList()
            self.cptpclockcurrentdsentry.parent = self
            self.cptpclockcurrentdsentry.name = 'cptpclockcurrentdsentry'


        class Cptpclockcurrentdsentry(object):
            """
            An entry in the table, containing information about a single
            PTP clock Current Datasets for a domain.
            
            .. attribute:: cptpclockcurrentdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockcurrentdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
                self.parent = None
                self.cptpclockcurrentdsdomainindex = None
                self.cptpclockcurrentdsclocktypeindex = None
                self.cptpclockcurrentdsinstanceindex = None
                self.cptpclockcurrentdsmeanpathdelay = None
                self.cptpclockcurrentdsoffsetfrommaster = None
                self.cptpclockcurrentdsstepsremoved = None

            @property
            def _common_path(self):
                if self.cptpclockcurrentdsdomainindex is None:
                    raise YPYModelError('Key property cptpclockcurrentdsdomainindex is None')
                if self.cptpclockcurrentdsclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockcurrentdsclocktypeindex is None')
                if self.cptpclockcurrentdsinstanceindex is None:
                    raise YPYModelError('Key property cptpclockcurrentdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockCurrentDSTable/CISCO-PTP-MIB:cPtpClockCurrentDSEntry[CISCO-PTP-MIB:cPtpClockCurrentDSDomainIndex = ' + str(self.cptpclockcurrentdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockCurrentDSClockTypeIndex = ' + str(self.cptpclockcurrentdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockCurrentDSInstanceIndex = ' + str(self.cptpclockcurrentdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockcurrentdsdomainindex is not None:
                    return True

                if self.cptpclockcurrentdsclocktypeindex is not None:
                    return True

                if self.cptpclockcurrentdsinstanceindex is not None:
                    return True

                if self.cptpclockcurrentdsmeanpathdelay is not None:
                    return True

                if self.cptpclockcurrentdsoffsetfrommaster is not None:
                    return True

                if self.cptpclockcurrentdsstepsremoved is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockCurrentDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockcurrentdsentry is not None:
                for child_ref in self.cptpclockcurrentdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockcurrentdstable']['meta_info']


    class Cptpclockparentdstable(object):
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
            self.parent = None
            self.cptpclockparentdsentry = YList()
            self.cptpclockparentdsentry.parent = self
            self.cptpclockparentdsentry.name = 'cptpclockparentdsentry'


        class Cptpclockparentdsentry(object):
            """
            An entry in the table, containing information about a single
            PTP clock Parent Datasets for a domain.
            
            .. attribute:: cptpclockparentdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`ClockqualityaccuracytypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockqualityaccuracytypeEnum>`
            
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
                self.parent = None
                self.cptpclockparentdsdomainindex = None
                self.cptpclockparentdsclocktypeindex = None
                self.cptpclockparentdsinstanceindex = None
                self.cptpclockparentdsclockphchrate = None
                self.cptpclockparentdsgmclockidentity = None
                self.cptpclockparentdsgmclockpriority1 = None
                self.cptpclockparentdsgmclockpriority2 = None
                self.cptpclockparentdsgmclockqualityaccuracy = None
                self.cptpclockparentdsgmclockqualityclass = None
                self.cptpclockparentdsgmclockqualityoffset = None
                self.cptpclockparentdsoffset = None
                self.cptpclockparentdsparentportidentity = None
                self.cptpclockparentdsparentstats = None

            @property
            def _common_path(self):
                if self.cptpclockparentdsdomainindex is None:
                    raise YPYModelError('Key property cptpclockparentdsdomainindex is None')
                if self.cptpclockparentdsclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockparentdsclocktypeindex is None')
                if self.cptpclockparentdsinstanceindex is None:
                    raise YPYModelError('Key property cptpclockparentdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockParentDSTable/CISCO-PTP-MIB:cPtpClockParentDSEntry[CISCO-PTP-MIB:cPtpClockParentDSDomainIndex = ' + str(self.cptpclockparentdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockParentDSClockTypeIndex = ' + str(self.cptpclockparentdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockParentDSInstanceIndex = ' + str(self.cptpclockparentdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockparentdsdomainindex is not None:
                    return True

                if self.cptpclockparentdsclocktypeindex is not None:
                    return True

                if self.cptpclockparentdsinstanceindex is not None:
                    return True

                if self.cptpclockparentdsclockphchrate is not None:
                    return True

                if self.cptpclockparentdsgmclockidentity is not None:
                    return True

                if self.cptpclockparentdsgmclockpriority1 is not None:
                    return True

                if self.cptpclockparentdsgmclockpriority2 is not None:
                    return True

                if self.cptpclockparentdsgmclockqualityaccuracy is not None:
                    return True

                if self.cptpclockparentdsgmclockqualityclass is not None:
                    return True

                if self.cptpclockparentdsgmclockqualityoffset is not None:
                    return True

                if self.cptpclockparentdsoffset is not None:
                    return True

                if self.cptpclockparentdsparentportidentity is not None:
                    return True

                if self.cptpclockparentdsparentstats is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockParentDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockparentdsentry is not None:
                for child_ref in self.cptpclockparentdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockparentdstable']['meta_info']


    class Cptpclockdefaultdstable(object):
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
            self.parent = None
            self.cptpclockdefaultdsentry = YList()
            self.cptpclockdefaultdsentry.parent = self
            self.cptpclockdefaultdsentry.name = 'cptpclockdefaultdsentry'


        class Cptpclockdefaultdsentry(object):
            """
            An entry in the table, containing information about a single
            PTP clock Default Datasets for a domain.
            
            .. attribute:: cptpclockdefaultdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`ClockqualityaccuracytypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockqualityaccuracytypeEnum>`
            
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
                self.parent = None
                self.cptpclockdefaultdsdomainindex = None
                self.cptpclockdefaultdsclocktypeindex = None
                self.cptpclockdefaultdsinstanceindex = None
                self.cptpclockdefaultdsclockidentity = None
                self.cptpclockdefaultdspriority1 = None
                self.cptpclockdefaultdspriority2 = None
                self.cptpclockdefaultdsqualityaccuracy = None
                self.cptpclockdefaultdsqualityclass = None
                self.cptpclockdefaultdsqualityoffset = None
                self.cptpclockdefaultdsslaveonly = None
                self.cptpclockdefaultdstwostepflag = None

            @property
            def _common_path(self):
                if self.cptpclockdefaultdsdomainindex is None:
                    raise YPYModelError('Key property cptpclockdefaultdsdomainindex is None')
                if self.cptpclockdefaultdsclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockdefaultdsclocktypeindex is None')
                if self.cptpclockdefaultdsinstanceindex is None:
                    raise YPYModelError('Key property cptpclockdefaultdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockDefaultDSTable/CISCO-PTP-MIB:cPtpClockDefaultDSEntry[CISCO-PTP-MIB:cPtpClockDefaultDSDomainIndex = ' + str(self.cptpclockdefaultdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockDefaultDSClockTypeIndex = ' + str(self.cptpclockdefaultdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockDefaultDSInstanceIndex = ' + str(self.cptpclockdefaultdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockdefaultdsdomainindex is not None:
                    return True

                if self.cptpclockdefaultdsclocktypeindex is not None:
                    return True

                if self.cptpclockdefaultdsinstanceindex is not None:
                    return True

                if self.cptpclockdefaultdsclockidentity is not None:
                    return True

                if self.cptpclockdefaultdspriority1 is not None:
                    return True

                if self.cptpclockdefaultdspriority2 is not None:
                    return True

                if self.cptpclockdefaultdsqualityaccuracy is not None:
                    return True

                if self.cptpclockdefaultdsqualityclass is not None:
                    return True

                if self.cptpclockdefaultdsqualityoffset is not None:
                    return True

                if self.cptpclockdefaultdsslaveonly is not None:
                    return True

                if self.cptpclockdefaultdstwostepflag is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockDefaultDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockdefaultdsentry is not None:
                for child_ref in self.cptpclockdefaultdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockdefaultdstable']['meta_info']


    class Cptpclockrunningtable(object):
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
            self.parent = None
            self.cptpclockrunningentry = YList()
            self.cptpclockrunningentry.parent = self
            self.cptpclockrunningentry.name = 'cptpclockrunningentry'


        class Cptpclockrunningentry(object):
            """
            An entry in the table, containing information about a single
            PTP clock running Datasets for a domain.
            
            .. attribute:: cptpclockrunningdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockrunningclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`ClockstatetypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockstatetypeEnum>`
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockrunningdomainindex = None
                self.cptpclockrunningclocktypeindex = None
                self.cptpclockrunninginstanceindex = None
                self.cptpclockrunningpacketsreceived = None
                self.cptpclockrunningpacketssent = None
                self.cptpclockrunningstate = None

            @property
            def _common_path(self):
                if self.cptpclockrunningdomainindex is None:
                    raise YPYModelError('Key property cptpclockrunningdomainindex is None')
                if self.cptpclockrunningclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockrunningclocktypeindex is None')
                if self.cptpclockrunninginstanceindex is None:
                    raise YPYModelError('Key property cptpclockrunninginstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockRunningTable/CISCO-PTP-MIB:cPtpClockRunningEntry[CISCO-PTP-MIB:cPtpClockRunningDomainIndex = ' + str(self.cptpclockrunningdomainindex) + '][CISCO-PTP-MIB:cPtpClockRunningClockTypeIndex = ' + str(self.cptpclockrunningclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockRunningInstanceIndex = ' + str(self.cptpclockrunninginstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockrunningdomainindex is not None:
                    return True

                if self.cptpclockrunningclocktypeindex is not None:
                    return True

                if self.cptpclockrunninginstanceindex is not None:
                    return True

                if self.cptpclockrunningpacketsreceived is not None:
                    return True

                if self.cptpclockrunningpacketssent is not None:
                    return True

                if self.cptpclockrunningstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockRunningTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockrunningentry is not None:
                for child_ref in self.cptpclockrunningentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockrunningtable']['meta_info']


    class Cptpclocktimepropertiesdstable(object):
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
            self.parent = None
            self.cptpclocktimepropertiesdsentry = YList()
            self.cptpclocktimepropertiesdsentry.parent = self
            self.cptpclocktimepropertiesdsentry.name = 'cptpclocktimepropertiesdsentry'


        class Cptpclocktimepropertiesdsentry(object):
            """
            An entry in the table, containing information about a single
            PTP clock timeproperties Datasets for a domain.
            
            .. attribute:: cptpclocktimepropertiesdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktimepropertiesdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`ClocktimesourcetypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktimesourcetypeEnum>`
            
            .. attribute:: cptpclocktimepropertiesdstimetraceable
            
            	This object specifies the Timetraceable value in the clock Current Dataset
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclocktimepropertiesdsdomainindex = None
                self.cptpclocktimepropertiesdsclocktypeindex = None
                self.cptpclocktimepropertiesdsinstanceindex = None
                self.cptpclocktimepropertiesdscurrentutcoffset = None
                self.cptpclocktimepropertiesdscurrentutcoffsetvalid = None
                self.cptpclocktimepropertiesdsfreqtraceable = None
                self.cptpclocktimepropertiesdsleap59 = None
                self.cptpclocktimepropertiesdsleap61 = None
                self.cptpclocktimepropertiesdsptptimescale = None
                self.cptpclocktimepropertiesdssource = None
                self.cptpclocktimepropertiesdstimetraceable = None

            @property
            def _common_path(self):
                if self.cptpclocktimepropertiesdsdomainindex is None:
                    raise YPYModelError('Key property cptpclocktimepropertiesdsdomainindex is None')
                if self.cptpclocktimepropertiesdsclocktypeindex is None:
                    raise YPYModelError('Key property cptpclocktimepropertiesdsclocktypeindex is None')
                if self.cptpclocktimepropertiesdsinstanceindex is None:
                    raise YPYModelError('Key property cptpclocktimepropertiesdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTimePropertiesDSTable/CISCO-PTP-MIB:cPtpClockTimePropertiesDSEntry[CISCO-PTP-MIB:cPtpClockTimePropertiesDSDomainIndex = ' + str(self.cptpclocktimepropertiesdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockTimePropertiesDSClockTypeIndex = ' + str(self.cptpclocktimepropertiesdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockTimePropertiesDSInstanceIndex = ' + str(self.cptpclocktimepropertiesdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclocktimepropertiesdsdomainindex is not None:
                    return True

                if self.cptpclocktimepropertiesdsclocktypeindex is not None:
                    return True

                if self.cptpclocktimepropertiesdsinstanceindex is not None:
                    return True

                if self.cptpclocktimepropertiesdscurrentutcoffset is not None:
                    return True

                if self.cptpclocktimepropertiesdscurrentutcoffsetvalid is not None:
                    return True

                if self.cptpclocktimepropertiesdsfreqtraceable is not None:
                    return True

                if self.cptpclocktimepropertiesdsleap59 is not None:
                    return True

                if self.cptpclocktimepropertiesdsleap61 is not None:
                    return True

                if self.cptpclocktimepropertiesdsptptimescale is not None:
                    return True

                if self.cptpclocktimepropertiesdssource is not None:
                    return True

                if self.cptpclocktimepropertiesdstimetraceable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTimePropertiesDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclocktimepropertiesdsentry is not None:
                for child_ref in self.cptpclocktimepropertiesdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclocktimepropertiesdstable']['meta_info']


    class Cptpclocktransdefaultdstable(object):
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
            self.parent = None
            self.cptpclocktransdefaultdsentry = YList()
            self.cptpclocktransdefaultdsentry.parent = self
            self.cptpclocktransdefaultdsentry.name = 'cptpclocktransdefaultdsentry'


        class Cptpclocktransdefaultdsentry(object):
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
            	**type**\:   :py:class:`ClockmechanismtypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockmechanismtypeEnum>`
            
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
                self.parent = None
                self.cptpclocktransdefaultdsdomainindex = None
                self.cptpclocktransdefaultdsinstanceindex = None
                self.cptpclocktransdefaultdsclockidentity = None
                self.cptpclocktransdefaultdsdelay = None
                self.cptpclocktransdefaultdsnumofports = None
                self.cptpclocktransdefaultdsprimarydomain = None

            @property
            def _common_path(self):
                if self.cptpclocktransdefaultdsdomainindex is None:
                    raise YPYModelError('Key property cptpclocktransdefaultdsdomainindex is None')
                if self.cptpclocktransdefaultdsinstanceindex is None:
                    raise YPYModelError('Key property cptpclocktransdefaultdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTransDefaultDSTable/CISCO-PTP-MIB:cPtpClockTransDefaultDSEntry[CISCO-PTP-MIB:cPtpClockTransDefaultDSDomainIndex = ' + str(self.cptpclocktransdefaultdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockTransDefaultDSInstanceIndex = ' + str(self.cptpclocktransdefaultdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclocktransdefaultdsdomainindex is not None:
                    return True

                if self.cptpclocktransdefaultdsinstanceindex is not None:
                    return True

                if self.cptpclocktransdefaultdsclockidentity is not None:
                    return True

                if self.cptpclocktransdefaultdsdelay is not None:
                    return True

                if self.cptpclocktransdefaultdsnumofports is not None:
                    return True

                if self.cptpclocktransdefaultdsprimarydomain is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTransDefaultDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclocktransdefaultdsentry is not None:
                for child_ref in self.cptpclocktransdefaultdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclocktransdefaultdstable']['meta_info']


    class Cptpclockporttable(object):
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
            self.parent = None
            self.cptpclockportentry = YList()
            self.cptpclockportentry.parent = self
            self.cptpclockportentry.name = 'cptpclockportentry'


        class Cptpclockportentry(object):
            """
            An entry in the table, containing information about a single
            clock port.
            
            .. attribute:: cptpclockportdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`ClockroletypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockroletypeEnum>`
            
            .. attribute:: cptpclockportsynconestep
            
            	This object specifies that one\-step clock operation between the PTP master and slave device is enabled
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockportdomainindex = None
                self.cptpclockportclocktypeindex = None
                self.cptpclockportclockinstanceindex = None
                self.cptpclockporttableportnumberindex = None
                self.cptpclockportcurrentpeeraddress = None
                self.cptpclockportcurrentpeeraddresstype = None
                self.cptpclockportname = None
                self.cptpclockportnumofassociatedports = None
                self.cptpclockportrole = None
                self.cptpclockportsynconestep = None

            @property
            def _common_path(self):
                if self.cptpclockportdomainindex is None:
                    raise YPYModelError('Key property cptpclockportdomainindex is None')
                if self.cptpclockportclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockportclocktypeindex is None')
                if self.cptpclockportclockinstanceindex is None:
                    raise YPYModelError('Key property cptpclockportclockinstanceindex is None')
                if self.cptpclockporttableportnumberindex is None:
                    raise YPYModelError('Key property cptpclockporttableportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTable/CISCO-PTP-MIB:cPtpClockPortEntry[CISCO-PTP-MIB:cPtpClockPortDomainIndex = ' + str(self.cptpclockportdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortClockTypeIndex = ' + str(self.cptpclockportclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortClockInstanceIndex = ' + str(self.cptpclockportclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortTablePortNumberIndex = ' + str(self.cptpclockporttableportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockportdomainindex is not None:
                    return True

                if self.cptpclockportclocktypeindex is not None:
                    return True

                if self.cptpclockportclockinstanceindex is not None:
                    return True

                if self.cptpclockporttableportnumberindex is not None:
                    return True

                if self.cptpclockportcurrentpeeraddress is not None:
                    return True

                if self.cptpclockportcurrentpeeraddresstype is not None:
                    return True

                if self.cptpclockportname is not None:
                    return True

                if self.cptpclockportnumofassociatedports is not None:
                    return True

                if self.cptpclockportrole is not None:
                    return True

                if self.cptpclockportsynconestep is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockporttable.Cptpclockportentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockportentry is not None:
                for child_ref in self.cptpclockportentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockporttable']['meta_info']


    class Cptpclockportdstable(object):
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
            self.parent = None
            self.cptpclockportdsentry = YList()
            self.cptpclockportdsentry.parent = self
            self.cptpclockportdsentry.name = 'cptpclockportdsentry'


        class Cptpclockportdsentry(object):
            """
            An entry in the table, containing port dataset information for
            a single clock port.
            
            .. attribute:: cptpclockportdsdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportdsclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`ClockmechanismtypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockmechanismtypeEnum>`
            
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
                self.parent = None
                self.cptpclockportdsdomainindex = None
                self.cptpclockportdsclocktypeindex = None
                self.cptpclockportdsclockinstanceindex = None
                self.cptpclockportdsportnumberindex = None
                self.cptpclockportdsannouncementinterval = None
                self.cptpclockportdsannouncercttimeout = None
                self.cptpclockportdsdelaymech = None
                self.cptpclockportdsgrantduration = None
                self.cptpclockportdsmindelayreqinterval = None
                self.cptpclockportdsname = None
                self.cptpclockportdspeerdelayreqinterval = None
                self.cptpclockportdspeermeanpathdelay = None
                self.cptpclockportdsportidentity = None
                self.cptpclockportdsptpversion = None
                self.cptpclockportdssyncinterval = None

            @property
            def _common_path(self):
                if self.cptpclockportdsdomainindex is None:
                    raise YPYModelError('Key property cptpclockportdsdomainindex is None')
                if self.cptpclockportdsclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockportdsclocktypeindex is None')
                if self.cptpclockportdsclockinstanceindex is None:
                    raise YPYModelError('Key property cptpclockportdsclockinstanceindex is None')
                if self.cptpclockportdsportnumberindex is None:
                    raise YPYModelError('Key property cptpclockportdsportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortDSTable/CISCO-PTP-MIB:cPtpClockPortDSEntry[CISCO-PTP-MIB:cPtpClockPortDSDomainIndex = ' + str(self.cptpclockportdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortDSClockTypeIndex = ' + str(self.cptpclockportdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortDSClockInstanceIndex = ' + str(self.cptpclockportdsclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortDSPortNumberIndex = ' + str(self.cptpclockportdsportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockportdsdomainindex is not None:
                    return True

                if self.cptpclockportdsclocktypeindex is not None:
                    return True

                if self.cptpclockportdsclockinstanceindex is not None:
                    return True

                if self.cptpclockportdsportnumberindex is not None:
                    return True

                if self.cptpclockportdsannouncementinterval is not None:
                    return True

                if self.cptpclockportdsannouncercttimeout is not None:
                    return True

                if self.cptpclockportdsdelaymech is not None:
                    return True

                if self.cptpclockportdsgrantduration is not None:
                    return True

                if self.cptpclockportdsmindelayreqinterval is not None:
                    return True

                if self.cptpclockportdsname is not None:
                    return True

                if self.cptpclockportdspeerdelayreqinterval is not None:
                    return True

                if self.cptpclockportdspeermeanpathdelay is not None:
                    return True

                if self.cptpclockportdsportidentity is not None:
                    return True

                if self.cptpclockportdsptpversion is not None:
                    return True

                if self.cptpclockportdssyncinterval is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockportdsentry is not None:
                for child_ref in self.cptpclockportdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockportdstable']['meta_info']


    class Cptpclockportrunningtable(object):
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
            self.parent = None
            self.cptpclockportrunningentry = YList()
            self.cptpclockportrunningentry.parent = self
            self.cptpclockportrunningentry.name = 'cptpclockportrunningentry'


        class Cptpclockportrunningentry(object):
            """
            An entry in the table, containing runing dataset information
            about a single clock port.
            
            .. attribute:: cptpclockportrunningdomainindex  <key>
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportrunningclocktypeindex  <key>
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`ClockroletypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockroletypeEnum>`
            
            .. attribute:: cptpclockportrunningrxmode
            
            	This object specifie the clock receive mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\:   :py:class:`ClocktxmodetypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktxmodetypeEnum>`
            
            .. attribute:: cptpclockportrunningstate
            
            	This object specifies the port state returned by PTP engine.  initializing \- In this state a port initializes                its data sets, hardware, and                communication facilities. faulty       \- The fault state of the protocol. disabled     \- The port shall not place any                messages on its communication path. listening    \- The port is waiting for the                announceReceiptTimeout to expire or                to receive an Announce message from                a master. preMaster    \- The port shall behave in all respects                as though it were in the MASTER state                except that it shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, signaling, or                management messages. master       \- The port is behaving as a master port.             passive      \- The port shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, or signaling                messages, or management messages                that are a required response to                another management message uncalibrated \- The local port is preparing to                synchronize to the master port. slave        \- The port is synchronizing to the                selected master port
            	**type**\:   :py:class:`ClockportstateEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClockportstateEnum>`
            
            .. attribute:: cptpclockportrunningtxmode
            
            	This object specifies the clock transmission mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\:   :py:class:`ClocktxmodetypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktxmodetypeEnum>`
            
            

            """

            _prefix = 'CISCO-PTP-MIB'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockportrunningdomainindex = None
                self.cptpclockportrunningclocktypeindex = None
                self.cptpclockportrunningclockinstanceindex = None
                self.cptpclockportrunningportnumberindex = None
                self.cptpclockportrunningencapsulationtype = None
                self.cptpclockportrunninginterfaceindex = None
                self.cptpclockportrunningipversion = None
                self.cptpclockportrunningname = None
                self.cptpclockportrunningpacketsreceived = None
                self.cptpclockportrunningpacketssent = None
                self.cptpclockportrunningrole = None
                self.cptpclockportrunningrxmode = None
                self.cptpclockportrunningstate = None
                self.cptpclockportrunningtxmode = None

            @property
            def _common_path(self):
                if self.cptpclockportrunningdomainindex is None:
                    raise YPYModelError('Key property cptpclockportrunningdomainindex is None')
                if self.cptpclockportrunningclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockportrunningclocktypeindex is None')
                if self.cptpclockportrunningclockinstanceindex is None:
                    raise YPYModelError('Key property cptpclockportrunningclockinstanceindex is None')
                if self.cptpclockportrunningportnumberindex is None:
                    raise YPYModelError('Key property cptpclockportrunningportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortRunningTable/CISCO-PTP-MIB:cPtpClockPortRunningEntry[CISCO-PTP-MIB:cPtpClockPortRunningDomainIndex = ' + str(self.cptpclockportrunningdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortRunningClockTypeIndex = ' + str(self.cptpclockportrunningclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortRunningClockInstanceIndex = ' + str(self.cptpclockportrunningclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortRunningPortNumberIndex = ' + str(self.cptpclockportrunningportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockportrunningdomainindex is not None:
                    return True

                if self.cptpclockportrunningclocktypeindex is not None:
                    return True

                if self.cptpclockportrunningclockinstanceindex is not None:
                    return True

                if self.cptpclockportrunningportnumberindex is not None:
                    return True

                if self.cptpclockportrunningencapsulationtype is not None:
                    return True

                if self.cptpclockportrunninginterfaceindex is not None:
                    return True

                if self.cptpclockportrunningipversion is not None:
                    return True

                if self.cptpclockportrunningname is not None:
                    return True

                if self.cptpclockportrunningpacketsreceived is not None:
                    return True

                if self.cptpclockportrunningpacketssent is not None:
                    return True

                if self.cptpclockportrunningrole is not None:
                    return True

                if self.cptpclockportrunningrxmode is not None:
                    return True

                if self.cptpclockportrunningstate is not None:
                    return True

                if self.cptpclockportrunningtxmode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortRunningTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockportrunningentry is not None:
                for child_ref in self.cptpclockportrunningentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockportrunningtable']['meta_info']


    class Cptpclockporttransdstable(object):
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
            self.parent = None
            self.cptpclockporttransdsentry = YList()
            self.cptpclockporttransdsentry.parent = self
            self.cptpclockporttransdsentry.name = 'cptpclockporttransdsentry'


        class Cptpclockporttransdsentry(object):
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
                self.parent = None
                self.cptpclockporttransdsdomainindex = None
                self.cptpclockporttransdsinstanceindex = None
                self.cptpclockporttransdsportnumberindex = None
                self.cptpclockporttransdsfaultyflag = None
                self.cptpclockporttransdslogminpdelayreqint = None
                self.cptpclockporttransdspeermeanpathdelay = None
                self.cptpclockporttransdsportidentity = None

            @property
            def _common_path(self):
                if self.cptpclockporttransdsdomainindex is None:
                    raise YPYModelError('Key property cptpclockporttransdsdomainindex is None')
                if self.cptpclockporttransdsinstanceindex is None:
                    raise YPYModelError('Key property cptpclockporttransdsinstanceindex is None')
                if self.cptpclockporttransdsportnumberindex is None:
                    raise YPYModelError('Key property cptpclockporttransdsportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTransDSTable/CISCO-PTP-MIB:cPtpClockPortTransDSEntry[CISCO-PTP-MIB:cPtpClockPortTransDSDomainIndex = ' + str(self.cptpclockporttransdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortTransDSInstanceIndex = ' + str(self.cptpclockporttransdsinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortTransDSPortNumberIndex = ' + str(self.cptpclockporttransdsportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockporttransdsdomainindex is not None:
                    return True

                if self.cptpclockporttransdsinstanceindex is not None:
                    return True

                if self.cptpclockporttransdsportnumberindex is not None:
                    return True

                if self.cptpclockporttransdsfaultyflag is not None:
                    return True

                if self.cptpclockporttransdslogminpdelayreqint is not None:
                    return True

                if self.cptpclockporttransdspeermeanpathdelay is not None:
                    return True

                if self.cptpclockporttransdsportidentity is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTransDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockporttransdsentry is not None:
                for child_ref in self.cptpclockporttransdsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockporttransdstable']['meta_info']


    class Cptpclockportassociatetable(object):
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
            self.parent = None
            self.cptpclockportassociateentry = YList()
            self.cptpclockportassociateentry.parent = self
            self.cptpclockportassociateentry.name = 'cptpclockportassociateentry'


        class Cptpclockportassociateentry(object):
            """
            An entry in the table, containing information about a single
            associated port for the given clockport.
            
            .. attribute:: cptpclockportcurrentdomainindex  <key>
            
            	This object specifies the given port's domain number
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportcurrentclocktypeindex  <key>
            
            	This object specifies the given port's clock type
            	**type**\:   :py:class:`ClocktypeEnum <ydk.models.cisco_ios_xe.CISCO_PTP_MIB.ClocktypeEnum>`
            
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
                self.parent = None
                self.cptpclockportcurrentdomainindex = None
                self.cptpclockportcurrentclocktypeindex = None
                self.cptpclockportcurrentclockinstanceindex = None
                self.cptpclockportcurrentportnumberindex = None
                self.cptpclockportassociateportindex = None
                self.cptpclockportassociateaddress = None
                self.cptpclockportassociateaddresstype = None
                self.cptpclockportassociateinerrors = None
                self.cptpclockportassociateouterrors = None
                self.cptpclockportassociatepacketsreceived = None
                self.cptpclockportassociatepacketssent = None

            @property
            def _common_path(self):
                if self.cptpclockportcurrentdomainindex is None:
                    raise YPYModelError('Key property cptpclockportcurrentdomainindex is None')
                if self.cptpclockportcurrentclocktypeindex is None:
                    raise YPYModelError('Key property cptpclockportcurrentclocktypeindex is None')
                if self.cptpclockportcurrentclockinstanceindex is None:
                    raise YPYModelError('Key property cptpclockportcurrentclockinstanceindex is None')
                if self.cptpclockportcurrentportnumberindex is None:
                    raise YPYModelError('Key property cptpclockportcurrentportnumberindex is None')
                if self.cptpclockportassociateportindex is None:
                    raise YPYModelError('Key property cptpclockportassociateportindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortAssociateTable/CISCO-PTP-MIB:cPtpClockPortAssociateEntry[CISCO-PTP-MIB:cPtpClockPortCurrentDomainIndex = ' + str(self.cptpclockportcurrentdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentClockTypeIndex = ' + str(self.cptpclockportcurrentclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentClockInstanceIndex = ' + str(self.cptpclockportcurrentclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentPortNumberIndex = ' + str(self.cptpclockportcurrentportnumberindex) + '][CISCO-PTP-MIB:cPtpClockPortAssociatePortIndex = ' + str(self.cptpclockportassociateportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cptpclockportcurrentdomainindex is not None:
                    return True

                if self.cptpclockportcurrentclocktypeindex is not None:
                    return True

                if self.cptpclockportcurrentclockinstanceindex is not None:
                    return True

                if self.cptpclockportcurrentportnumberindex is not None:
                    return True

                if self.cptpclockportassociateportindex is not None:
                    return True

                if self.cptpclockportassociateaddress is not None:
                    return True

                if self.cptpclockportassociateaddresstype is not None:
                    return True

                if self.cptpclockportassociateinerrors is not None:
                    return True

                if self.cptpclockportassociateouterrors is not None:
                    return True

                if self.cptpclockportassociatepacketsreceived is not None:
                    return True

                if self.cptpclockportassociatepacketssent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortAssociateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cptpclockportassociateentry is not None:
                for child_ref in self.cptpclockportassociateentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CiscoPtpMib.Cptpclockportassociatetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-PTP-MIB:CISCO-PTP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscoptpmibsysteminfo is not None and self.ciscoptpmibsysteminfo._has_data():
            return True

        if self.cptpclockcurrentdstable is not None and self.cptpclockcurrentdstable._has_data():
            return True

        if self.cptpclockdefaultdstable is not None and self.cptpclockdefaultdstable._has_data():
            return True

        if self.cptpclocknodetable is not None and self.cptpclocknodetable._has_data():
            return True

        if self.cptpclockparentdstable is not None and self.cptpclockparentdstable._has_data():
            return True

        if self.cptpclockportassociatetable is not None and self.cptpclockportassociatetable._has_data():
            return True

        if self.cptpclockportdstable is not None and self.cptpclockportdstable._has_data():
            return True

        if self.cptpclockportrunningtable is not None and self.cptpclockportrunningtable._has_data():
            return True

        if self.cptpclockporttable is not None and self.cptpclockporttable._has_data():
            return True

        if self.cptpclockporttransdstable is not None and self.cptpclockporttransdstable._has_data():
            return True

        if self.cptpclockrunningtable is not None and self.cptpclockrunningtable._has_data():
            return True

        if self.cptpclocktimepropertiesdstable is not None and self.cptpclocktimepropertiesdstable._has_data():
            return True

        if self.cptpclocktransdefaultdstable is not None and self.cptpclocktransdefaultdstable._has_data():
            return True

        if self.cptpsystemdomaintable is not None and self.cptpsystemdomaintable._has_data():
            return True

        if self.cptpsystemtable is not None and self.cptpsystemtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['CiscoPtpMib']['meta_info']


