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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum

class ClockMechanismType_Enum(Enum):
    """
    ClockMechanismType_Enum

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

    """

    E2E = 1

    P2P = 2

    DISABLED = 254


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockMechanismType_Enum']


class ClockPortState_Enum(Enum):
    """
    ClockPortState_Enum

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

    """

    INITIALIZING = 1

    FAULTY = 2

    DISABLED = 3

    LISTENING = 4

    PREMASTER = 5

    MASTER = 6

    PASSIVE = 7

    UNCALIBRATED = 8

    SLAVE = 9


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockPortState_Enum']


class ClockProfileType_Enum(Enum):
    """
    ClockProfileType_Enum

    Clock Profile used. From [1] section 3.1.30, Profile is the set
    of allowed Precision Time Protocol (PTP) features applicable to
    a device.

    """

    DEFAULT = 1

    TELECOM = 2

    VENDORSPECIFIC = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockProfileType_Enum']


class ClockQualityAccuracyType_Enum(Enum):
    """
    ClockQualityAccuracyType_Enum

    The ClockQuality as specified in section 5.3.7, 7.6.2.5 and
    Table 6 of [1].
    
    The following values are not represented in the enumerated
    values.
    
             0x01\-0x1F Reserved
             0x32\-0x7F Reserved
    
    It is important to note that section 7.1.1 RFC2578 allows for
    gaps and enumerate values to start with zero when indicated by
    the protocol.

    """

    RESERVED00 = 1

    NANOSECOND25 = 32

    NANOSECOND100 = 33

    NANOSECOND250 = 34

    MICROSEC1 = 35

    MICROSEC2DOT5 = 36

    MICROSEC10 = 37

    MICROSEC25 = 38

    MICROSEC100 = 39

    MICROSEC250 = 40

    MILLISEC1 = 41

    MILLISEC2DOT5 = 42

    MILLISEC10 = 43

    MILLISEC25 = 44

    MILLISEC100 = 45

    MILLISEC250 = 46

    SECOND1 = 47

    SECOND10 = 48

    SECONDGREATER10 = 49

    UNKNOWN = 254

    RESERVED255 = 255


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockQualityAccuracyType_Enum']


class ClockRoleType_Enum(Enum):
    """
    ClockRoleType_Enum

    The Clock Role. The protocol generates a Master Slave
    relationship among the clocks in the system.
    
    Clock Role      Value     Description
    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
    Master clock     1        A clock that is the source of
                              time to which all other clocks on
                              that path synchronize.
    
    Slave clock       2       A clock which synchronizes to
                              another clock (master).

    """

    MASTER = 1

    SLAVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockRoleType_Enum']


class ClockStateType_Enum(Enum):
    """
    ClockStateType_Enum

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

    """

    FREERUN = 1

    HOLDOVER = 2

    ACQUIRING = 3

    FREQUENCYLOCKED = 4

    PHASEALIGNED = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockStateType_Enum']


class ClockTimeSourceType_Enum(Enum):
    """
    ClockTimeSourceType_Enum

    The ClockQuality as specified in section 5.3.7, 7.6.2.6 and
    Table 7 of [1].
    
    The following values are not represented in the enumerated
    values.
    
    0xF0\-0xFE  For use by alternate PTP profiles
    0xFF       Reserved
    
    It is important to note that section 7.1.1 RFC2578 allows for
    gaps and enumerate values to start with zero when indicated by
    the protocol.

    """

    ATOMICCLOCK = 16

    GPS = 32

    TERRESTRIALRADIO = 48

    PTP = 64

    NTP = 80

    HANDSET = 96

    OTHER = 144

    INTERNALOSILLATOR = 160


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockTimeSourceType_Enum']


class ClockTxModeType_Enum(Enum):
    """
    ClockTxModeType_Enum

    Transmission mode.
    
    unicast. Using unicast commnuication channel.
    
    multicast. Using Multicast communication channel.
    
    multicast\-mix. Using multicast\-unicast communication channel

    """

    UNICAST = 1

    MULTICAST = 2

    MULTICASTMIX = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockTxModeType_Enum']


class ClockType_Enum(Enum):
    """
    ClockType_Enum

    The clock types as defined in the MIB module description.

    """

    ORDINARYCLOCK = 1

    BOUNDARYCLOCK = 2

    TRANSPARENTCLOCK = 3

    BOUNDARYNODE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['ClockType_Enum']



class CISCOPTPMIB(object):
    """
    
    
    .. attribute:: ciscoptpmibsysteminfo
    
    	
    	**type**\: :py:class:`CiscoPtpMIBSystemInfo <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CiscoPtpMIBSystemInfo>`
    
    .. attribute:: cptpclockcurrentdstable
    
    	Table of information about the PTP clock Current Datasets for all domains
    	**type**\: :py:class:`CPtpClockCurrentDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockCurrentDSTable>`
    
    .. attribute:: cptpclockdefaultdstable
    
    	Table of information about the PTP clock Default Datasets for all domains
    	**type**\: :py:class:`CPtpClockDefaultDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockDefaultDSTable>`
    
    .. attribute:: cptpclocknodetable
    
    	Table of information about the PTP system for a given domain
    	**type**\: :py:class:`CPtpClockNodeTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockNodeTable>`
    
    .. attribute:: cptpclockparentdstable
    
    	Table of information about the PTP clock Parent Datasets for all domains
    	**type**\: :py:class:`CPtpClockParentDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockParentDSTable>`
    
    .. attribute:: cptpclockportassociatetable
    
    	Table of information about a given port's associated ports.  For a master port \- multiple slave ports which have established sessions with the current master port.   For a slave port \- the list of masters available for a given slave port.   Session information (pkts, errors) to be displayed based on availability and scenario
    	**type**\: :py:class:`CPtpClockPortAssociateTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortAssociateTable>`
    
    .. attribute:: cptpclockportdstable
    
    	Table of information about the clock ports dataset for a particular domain
    	**type**\: :py:class:`CPtpClockPortDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortDSTable>`
    
    .. attribute:: cptpclockportrunningtable
    
    	Table of information about the clock ports running dataset for a particular domain
    	**type**\: :py:class:`CPtpClockPortRunningTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortRunningTable>`
    
    .. attribute:: cptpclockporttable
    
    	Table of information about the clock ports for a particular domain
    	**type**\: :py:class:`CPtpClockPortTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTable>`
    
    .. attribute:: cptpclockporttransdstable
    
    	Table of information about the Transparent clock ports running dataset for a particular domain
    	**type**\: :py:class:`CPtpClockPortTransDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTransDSTable>`
    
    .. attribute:: cptpclockrunningtable
    
    	Table of information about the PTP clock Running Datasets for all domains
    	**type**\: :py:class:`CPtpClockRunningTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockRunningTable>`
    
    .. attribute:: cptpclocktimepropertiesdstable
    
    	Table of information about the PTP clock Timeproperties Datasets for all domains
    	**type**\: :py:class:`CPtpClockTimePropertiesDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTimePropertiesDSTable>`
    
    .. attribute:: cptpclocktransdefaultdstable
    
    	Table of information about the PTP Transparent clock Default Datasets for all domains
    	**type**\: :py:class:`CPtpClockTransDefaultDSTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTransDefaultDSTable>`
    
    .. attribute:: cptpsystemdomaintable
    
    	Table of information about the PTP system for all clock modes \-\- ordinary, boundary or transparent
    	**type**\: :py:class:`CPtpSystemDomainTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemDomainTable>`
    
    .. attribute:: cptpsystemtable
    
    	Table of count information about the PTP system for all domains
    	**type**\: :py:class:`CPtpSystemTable <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemTable>`
    
    

    """

    _prefix = 'cisco-ptp'
    _revision = '2011-01-28'

    def __init__(self):
        self.ciscoptpmibsysteminfo = CISCOPTPMIB.CiscoPtpMIBSystemInfo()
        self.ciscoptpmibsysteminfo.parent = self
        self.cptpclockcurrentdstable = CISCOPTPMIB.CPtpClockCurrentDSTable()
        self.cptpclockcurrentdstable.parent = self
        self.cptpclockdefaultdstable = CISCOPTPMIB.CPtpClockDefaultDSTable()
        self.cptpclockdefaultdstable.parent = self
        self.cptpclocknodetable = CISCOPTPMIB.CPtpClockNodeTable()
        self.cptpclocknodetable.parent = self
        self.cptpclockparentdstable = CISCOPTPMIB.CPtpClockParentDSTable()
        self.cptpclockparentdstable.parent = self
        self.cptpclockportassociatetable = CISCOPTPMIB.CPtpClockPortAssociateTable()
        self.cptpclockportassociatetable.parent = self
        self.cptpclockportdstable = CISCOPTPMIB.CPtpClockPortDSTable()
        self.cptpclockportdstable.parent = self
        self.cptpclockportrunningtable = CISCOPTPMIB.CPtpClockPortRunningTable()
        self.cptpclockportrunningtable.parent = self
        self.cptpclockporttable = CISCOPTPMIB.CPtpClockPortTable()
        self.cptpclockporttable.parent = self
        self.cptpclockporttransdstable = CISCOPTPMIB.CPtpClockPortTransDSTable()
        self.cptpclockporttransdstable.parent = self
        self.cptpclockrunningtable = CISCOPTPMIB.CPtpClockRunningTable()
        self.cptpclockrunningtable.parent = self
        self.cptpclocktimepropertiesdstable = CISCOPTPMIB.CPtpClockTimePropertiesDSTable()
        self.cptpclocktimepropertiesdstable.parent = self
        self.cptpclocktransdefaultdstable = CISCOPTPMIB.CPtpClockTransDefaultDSTable()
        self.cptpclocktransdefaultdstable.parent = self
        self.cptpsystemdomaintable = CISCOPTPMIB.CPtpSystemDomainTable()
        self.cptpsystemdomaintable.parent = self
        self.cptpsystemtable = CISCOPTPMIB.CPtpSystemTable()
        self.cptpsystemtable.parent = self


    class CPtpClockCurrentDSTable(object):
        """
        Table of information about the PTP clock Current Datasets for
        all domains.
        
        .. attribute:: cptpclockcurrentdsentry
        
        	An entry in the table, containing information about a single PTP clock Current Datasets for a domain
        	**type**\: list of :py:class:`CPtpClockCurrentDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockCurrentDSTable.CPtpClockCurrentDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockcurrentdsentry = YList()
            self.cptpclockcurrentdsentry.parent = self
            self.cptpclockcurrentdsentry.name = 'cptpclockcurrentdsentry'


        class CPtpClockCurrentDSEntry(object):
            """
            An entry in the table, containing information about a single
            PTP clock Current Datasets for a domain.
            
            .. attribute:: cptpclockcurrentdsclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockcurrentdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockcurrentdsinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockcurrentdsmeanpathdelay
            
            	This object specifies the current clock dataset MeanPathDelay value.  The mean path delay between a pair of ports as measure by the delay request\-response mechanism
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclockcurrentdsoffsetfrommaster
            
            	This object specifies the current clock dataset ClockOffset value. The value of the computation of the offset in time between a slave and a master clock
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclockcurrentdsstepsremoved
            
            	The current clock dataset StepsRemoved value.  This object specifies the distance measured by the number of Boundary clocks between the local clock and the Foreign master as indicated in the stepsRemoved field of Announce messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockcurrentdsclocktypeindex = None
                self.cptpclockcurrentdsdomainindex = None
                self.cptpclockcurrentdsinstanceindex = None
                self.cptpclockcurrentdsmeanpathdelay = None
                self.cptpclockcurrentdsoffsetfrommaster = None
                self.cptpclockcurrentdsstepsremoved = None

            @property
            def _common_path(self):
                if self.cptpclockcurrentdsclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockcurrentdsclocktypeindex is None')
                if self.cptpclockcurrentdsdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockcurrentdsdomainindex is None')
                if self.cptpclockcurrentdsinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockcurrentdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockCurrentDSTable/CISCO-PTP-MIB:cPtpClockCurrentDSEntry[CISCO-PTP-MIB:cPtpClockCurrentDSClockTypeIndex = ' + str(self.cptpclockcurrentdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockCurrentDSDomainIndex = ' + str(self.cptpclockcurrentdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockCurrentDSInstanceIndex = ' + str(self.cptpclockcurrentdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockcurrentdsclocktypeindex is not None:
                    return True

                if self.cptpclockcurrentdsdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockCurrentDSTable.CPtpClockCurrentDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockCurrentDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockcurrentdsentry is not None:
                for child_ref in self.cptpclockcurrentdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockCurrentDSTable']['meta_info']


    class CPtpClockDefaultDSTable(object):
        """
        Table of information about the PTP clock Default Datasets for
        all domains.
        
        .. attribute:: cptpclockdefaultdsentry
        
        	An entry in the table, containing information about a single PTP clock Default Datasets for a domain
        	**type**\: list of :py:class:`CPtpClockDefaultDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockDefaultDSTable.CPtpClockDefaultDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockdefaultdsentry = YList()
            self.cptpclockdefaultdsentry.parent = self
            self.cptpclockdefaultdsentry.name = 'cptpclockdefaultdsentry'


        class CPtpClockDefaultDSEntry(object):
            """
            An entry in the table, containing information about a single
            PTP clock Default Datasets for a domain.
            
            .. attribute:: cptpclockdefaultdsclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockdefaultdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsclockidentity
            
            	This object specifies the default Datasets clock identity
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclockdefaultdspriority1
            
            	This object specifies the default Datasets clock Priority1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockdefaultdspriority2
            
            	This object specifies the default Datasets clock Priority2
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockdefaultdsqualityaccuracy
            
            	This object specifies the default dataset Quality Accurarcy
            	**type**\: :py:class:`ClockQualityAccuracyType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockQualityAccuracyType_Enum>`
            
            .. attribute:: cptpclockdefaultdsqualityclass
            
            	This object specifies the default dataset Quality Class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockdefaultdsqualityoffset
            
            	This object specifies the default dataset Quality offset
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockdefaultdsslaveonly
            
            	Whether the SlaveOnly flag is set
            	**type**\: bool
            
            .. attribute:: cptpclockdefaultdstwostepflag
            
            	This object specifies whether the Two Step process is used
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockdefaultdsclocktypeindex = None
                self.cptpclockdefaultdsdomainindex = None
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
                if self.cptpclockdefaultdsclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockdefaultdsclocktypeindex is None')
                if self.cptpclockdefaultdsdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockdefaultdsdomainindex is None')
                if self.cptpclockdefaultdsinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockdefaultdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockDefaultDSTable/CISCO-PTP-MIB:cPtpClockDefaultDSEntry[CISCO-PTP-MIB:cPtpClockDefaultDSClockTypeIndex = ' + str(self.cptpclockdefaultdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockDefaultDSDomainIndex = ' + str(self.cptpclockdefaultdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockDefaultDSInstanceIndex = ' + str(self.cptpclockdefaultdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockdefaultdsclocktypeindex is not None:
                    return True

                if self.cptpclockdefaultdsdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockDefaultDSTable.CPtpClockDefaultDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockDefaultDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockdefaultdsentry is not None:
                for child_ref in self.cptpclockdefaultdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockDefaultDSTable']['meta_info']


    class CPtpClockNodeTable(object):
        """
        Table of information about the PTP system for a given domain.
        
        .. attribute:: cptpclocknodeentry
        
        	An entry in the table, containing information about a single domain. A entry is added when a new PTP clock domain is configured on the router
        	**type**\: list of :py:class:`CPtpClockNodeEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockNodeTable.CPtpClockNodeEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclocknodeentry = YList()
            self.cptpclocknodeentry.parent = self
            self.cptpclocknodeentry.name = 'cptpclocknodeentry'


        class CPtpClockNodeEntry(object):
            """
            An entry in the table, containing information about a single
            domain. A entry is added when a new PTP clock domain is
            configured on the router.
            
            .. attribute:: cptpclockdomainindex
            
            	This object specifies the  domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockinstanceindex
            
            	This object specifies the instance of the Clock for this clock type for the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockinput1ppsenabled
            
            	This object specifies whether the node is enabled for PTP input clocking using the 1pps interface
            	**type**\: bool
            
            .. attribute:: cptpclockinput1ppsinterface
            
            	This object specifies the 1pps interface used for PTP input clocking
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cptpclockinputfrequencyenabled
            
            	This object specifies whether enabled for Frequency input using the 1.544 Mhz, 2.048 Mhz, or 10Mhz timing interface
            	**type**\: bool
            
            .. attribute:: cptpclockoutput1ppsenabled
            
            	This object specifies whether the node is enabled for PTP input clocking using the 1pps interface
            	**type**\: bool
            
            .. attribute:: cptpclockoutput1ppsinterface
            
            	This object specifies the 1pps interface used for PTP output clocking
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cptpclockoutput1ppsoffsetenabled
            
            	This object specifies whether an offset is configured in order to compensate for a known phase error such as network asymmetry
            	**type**\: bool
            
            .. attribute:: cptpclockoutput1ppsoffsetnegative
            
            	This object specifies whether the added (fixed) offset to the 1pps output is negative or not.  When object returns TRUE the offset is negative and when object returns FALSE the offset is positive
            	**type**\: bool
            
            .. attribute:: cptpclockoutput1ppsoffsetvalue
            
            	This object specifies the fixed offset value configured to be added for the 1pps output
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclocktodenabled
            
            	This object specifies whether the node is enabled for TOD
            	**type**\: bool
            
            .. attribute:: cptpclocktodinterface
            
            	This object specifies the interface used for PTP TOD
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockdomainindex = None
                self.cptpclockinstanceindex = None
                self.cptpclocktypeindex = None
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
                    raise YPYDataValidationError('Key property cptpclockdomainindex is None')
                if self.cptpclockinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockinstanceindex is None')
                if self.cptpclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclocktypeindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockNodeTable/CISCO-PTP-MIB:cPtpClockNodeEntry[CISCO-PTP-MIB:cPtpClockDomainIndex = ' + str(self.cptpclockdomainindex) + '][CISCO-PTP-MIB:cPtpClockInstanceIndex = ' + str(self.cptpclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockTypeIndex = ' + str(self.cptpclocktypeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockdomainindex is not None:
                    return True

                if self.cptpclockinstanceindex is not None:
                    return True

                if self.cptpclocktypeindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockNodeTable.CPtpClockNodeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockNodeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclocknodeentry is not None:
                for child_ref in self.cptpclocknodeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockNodeTable']['meta_info']


    class CPtpClockParentDSTable(object):
        """
        Table of information about the PTP clock Parent Datasets for
        all domains.
        
        .. attribute:: cptpclockparentdsentry
        
        	An entry in the table, containing information about a single PTP clock Parent Datasets for a domain
        	**type**\: list of :py:class:`CPtpClockParentDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockParentDSTable.CPtpClockParentDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockparentdsentry = YList()
            self.cptpclockparentdsentry.parent = self
            self.cptpclockparentdsentry.name = 'cptpclockparentdsentry'


        class CPtpClockParentDSEntry(object):
            """
            An entry in the table, containing information about a single
            PTP clock Parent Datasets for a domain.
            
            .. attribute:: cptpclockparentdsclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockparentdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsclockphchrate
            
            	This object specifies the clock's parent dataset ParentClockPhaseChangeRate value.  This value is an estimate of the parent clocks phase change rate as measured by the slave clock
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockparentdsgmclockidentity
            
            	This object specifies the parent dataset Grandmaster clock identity
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclockparentdsgmclockpriority1
            
            	This object specifies the parent dataset Grandmaster clock priority1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockparentdsgmclockpriority2
            
            	This object specifies the parent dataset grandmaster clock priority2
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockparentdsgmclockqualityaccuracy
            
            	This object specifies the parent dataset grandmaster clock quality accuracy
            	**type**\: :py:class:`ClockQualityAccuracyType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockQualityAccuracyType_Enum>`
            
            .. attribute:: cptpclockparentdsgmclockqualityclass
            
            	This object specifies the parent dataset grandmaster clock quality class
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockparentdsgmclockqualityoffset
            
            	This object specifies the parent dataset grandmaster clock quality offset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclockparentdsoffset
            
            	This object specifies the Parent Dataset ParentOffsetScaledLogVariance value.  This value is the variance of the parent clocks phase as measured by the local clock
            	**type**\: int
            
            	**range:** \-128..127
            
            .. attribute:: cptpclockparentdsparentportidentity
            
            	This object specifies the value of portIdentity of the port on the master that issues the Sync messages used in synchronizing this clock
            	**type**\: str
            
            .. attribute:: cptpclockparentdsparentstats
            
            	This object specifies the Parent Dataset ParentStats value.  This value indicates whether the values of ParentDSOffset and ParentDSClockPhChRate have been measured and are valid. A TRUE value shall indicate valid data
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockparentdsclocktypeindex = None
                self.cptpclockparentdsdomainindex = None
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
                if self.cptpclockparentdsclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockparentdsclocktypeindex is None')
                if self.cptpclockparentdsdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockparentdsdomainindex is None')
                if self.cptpclockparentdsinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockparentdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockParentDSTable/CISCO-PTP-MIB:cPtpClockParentDSEntry[CISCO-PTP-MIB:cPtpClockParentDSClockTypeIndex = ' + str(self.cptpclockparentdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockParentDSDomainIndex = ' + str(self.cptpclockparentdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockParentDSInstanceIndex = ' + str(self.cptpclockparentdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockparentdsclocktypeindex is not None:
                    return True

                if self.cptpclockparentdsdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockParentDSTable.CPtpClockParentDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockParentDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockparentdsentry is not None:
                for child_ref in self.cptpclockparentdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockParentDSTable']['meta_info']


    class CPtpClockPortAssociateTable(object):
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
        	**type**\: list of :py:class:`CPtpClockPortAssociateEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortAssociateTable.CPtpClockPortAssociateEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockportassociateentry = YList()
            self.cptpclockportassociateentry.parent = self
            self.cptpclockportassociateentry.name = 'cptpclockportassociateentry'


        class CPtpClockPortAssociateEntry(object):
            """
            An entry in the table, containing information about a single
            associated port for the given clockport.
            
            .. attribute:: cptpclockportassociateportindex
            
            	This object specifies the associated port's serial number in the current port's context
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportcurrentclockinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportcurrentclocktypeindex
            
            	This object specifies the given port's clock type
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockportcurrentdomainindex
            
            	This object specifies the given port's domain number
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportcurrentportnumberindex
            
            	This object specifies the PTP Port Number for the given port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cptpclockportassociateaddress
            
            	This object specifies the peer port's network address used for PTP communication
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportassociateaddresstype
            
            	This object specifies the peer port's network address type used for PTP communication
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cptpclockportassociateinerrors
            
            	This object specifies the input errors associated with the peer port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockportassociateouterrors
            
            	This object specifies the output errors associated with the peer port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockportassociatepacketsreceived
            
            	The number of packets received from this peer port by the current port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockportassociatepacketssent
            
            	The number of packets sent to this peer port from the current port
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockportassociateportindex = None
                self.cptpclockportcurrentclockinstanceindex = None
                self.cptpclockportcurrentclocktypeindex = None
                self.cptpclockportcurrentdomainindex = None
                self.cptpclockportcurrentportnumberindex = None
                self.cptpclockportassociateaddress = None
                self.cptpclockportassociateaddresstype = None
                self.cptpclockportassociateinerrors = None
                self.cptpclockportassociateouterrors = None
                self.cptpclockportassociatepacketsreceived = None
                self.cptpclockportassociatepacketssent = None

            @property
            def _common_path(self):
                if self.cptpclockportassociateportindex is None:
                    raise YPYDataValidationError('Key property cptpclockportassociateportindex is None')
                if self.cptpclockportcurrentclockinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockportcurrentclockinstanceindex is None')
                if self.cptpclockportcurrentclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockportcurrentclocktypeindex is None')
                if self.cptpclockportcurrentdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockportcurrentdomainindex is None')
                if self.cptpclockportcurrentportnumberindex is None:
                    raise YPYDataValidationError('Key property cptpclockportcurrentportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortAssociateTable/CISCO-PTP-MIB:cPtpClockPortAssociateEntry[CISCO-PTP-MIB:cPtpClockPortAssociatePortIndex = ' + str(self.cptpclockportassociateportindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentClockInstanceIndex = ' + str(self.cptpclockportcurrentclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentClockTypeIndex = ' + str(self.cptpclockportcurrentclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentDomainIndex = ' + str(self.cptpclockportcurrentdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortCurrentPortNumberIndex = ' + str(self.cptpclockportcurrentportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockportassociateportindex is not None:
                    return True

                if self.cptpclockportcurrentclockinstanceindex is not None:
                    return True

                if self.cptpclockportcurrentclocktypeindex is not None:
                    return True

                if self.cptpclockportcurrentdomainindex is not None:
                    return True

                if self.cptpclockportcurrentportnumberindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockPortAssociateTable.CPtpClockPortAssociateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortAssociateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockportassociateentry is not None:
                for child_ref in self.cptpclockportassociateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockPortAssociateTable']['meta_info']


    class CPtpClockPortDSTable(object):
        """
        Table of information about the clock ports dataset for a
        particular domain.
        
        .. attribute:: cptpclockportdsentry
        
        	An entry in the table, containing port dataset information for a single clock port
        	**type**\: list of :py:class:`CPtpClockPortDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortDSTable.CPtpClockPortDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockportdsentry = YList()
            self.cptpclockportdsentry.parent = self
            self.cptpclockportdsentry.name = 'cptpclockportdsentry'


        class CPtpClockPortDSEntry(object):
            """
            An entry in the table, containing port dataset information for
            a single clock port.
            
            .. attribute:: cptpclockportdsclockinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportdsclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockportdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportdsportnumberindex
            
            	This object specifies the PTP portnumber associated with this PTP port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportdsannouncementinterval
            
            	This object specifies the Announce message transmission interval associated with this clock port
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdsannouncercttimeout
            
            	This object specifies the Announce receipt timeout associated with this clock port
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdsdelaymech
            
            	This object specifies the delay mechanism used. If the clock is an end\-to\-end clock, the value of the is e2e, else if the clock is a peer to\-peer clock, the value shall be p2p
            	**type**\: :py:class:`ClockMechanismType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockMechanismType_Enum>`
            
            .. attribute:: cptpclockportdsgrantduration
            
            	This object specifies the grant duration allocated by the master
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclockportdsmindelayreqinterval
            
            	This object specifies the Delay\_Req message transmission interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdsname
            
            	This object specifies the PTP clock port name
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cptpclockportdspeerdelayreqinterval
            
            	This object specifies the Pdelay\_Req message transmission interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdspeermeanpathdelay
            
            	This object specifies the peer meanPathDelay
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclockportdsportidentity
            
            	This object specifies the PTP clock port Identity
            	**type**\: str
            
            .. attribute:: cptpclockportdsptpversion
            
            	This object specifies the PTP version being used
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportdssyncinterval
            
            	This object specifies the Sync message transmission interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockportdsclockinstanceindex = None
                self.cptpclockportdsclocktypeindex = None
                self.cptpclockportdsdomainindex = None
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
                if self.cptpclockportdsclockinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockportdsclockinstanceindex is None')
                if self.cptpclockportdsclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockportdsclocktypeindex is None')
                if self.cptpclockportdsdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockportdsdomainindex is None')
                if self.cptpclockportdsportnumberindex is None:
                    raise YPYDataValidationError('Key property cptpclockportdsportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortDSTable/CISCO-PTP-MIB:cPtpClockPortDSEntry[CISCO-PTP-MIB:cPtpClockPortDSClockInstanceIndex = ' + str(self.cptpclockportdsclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortDSClockTypeIndex = ' + str(self.cptpclockportdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortDSDomainIndex = ' + str(self.cptpclockportdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortDSPortNumberIndex = ' + str(self.cptpclockportdsportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockportdsclockinstanceindex is not None:
                    return True

                if self.cptpclockportdsclocktypeindex is not None:
                    return True

                if self.cptpclockportdsdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockPortDSTable.CPtpClockPortDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockportdsentry is not None:
                for child_ref in self.cptpclockportdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockPortDSTable']['meta_info']


    class CPtpClockPortRunningTable(object):
        """
        Table of information about the clock ports running dataset for
        a particular domain.
        
        .. attribute:: cptpclockportrunningentry
        
        	An entry in the table, containing runing dataset information about a single clock port
        	**type**\: list of :py:class:`CPtpClockPortRunningEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortRunningTable.CPtpClockPortRunningEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockportrunningentry = YList()
            self.cptpclockportrunningentry.parent = self
            self.cptpclockportrunningentry.name = 'cptpclockportrunningentry'


        class CPtpClockPortRunningEntry(object):
            """
            An entry in the table, containing runing dataset information
            about a single clock port.
            
            .. attribute:: cptpclockportrunningclockinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportrunningclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockportrunningdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportrunningportnumberindex
            
            	This object specifies the PTP portnumber associated with this clock port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportrunningencapsulationtype
            
            	This object specifies the type of encapsulation if the interface is adding extra  layers (eg. VLAN, Pseudowire encapsulation...) for the PTP messages
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportrunninginterfaceindex
            
            	This object specifies the interface on the router being used by the PTP Clock for PTP communication
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cptpclockportrunningipversion
            
            	This object specifirst the IP version being used for PTP communication (the mapping used)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockportrunningname
            
            	This object specifies the PTP clock port name
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cptpclockportrunningpacketsreceived
            
            	This object specifies the packets received on the clock port (cummulative)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockportrunningpacketssent
            
            	This object specifies the packets sent on the clock port (cummulative)
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockportrunningrole
            
            	This object specifies the Clock Role
            	**type**\: :py:class:`ClockRoleType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockRoleType_Enum>`
            
            .. attribute:: cptpclockportrunningrxmode
            
            	This object specifie the clock receive mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\: :py:class:`ClockTxModeType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockTxModeType_Enum>`
            
            .. attribute:: cptpclockportrunningstate
            
            	This object specifies the port state returned by PTP engine.  initializing \- In this state a port initializes                its data sets, hardware, and                communication facilities. faulty       \- The fault state of the protocol. disabled     \- The port shall not place any                messages on its communication path. listening    \- The port is waiting for the                announceReceiptTimeout to expire or                to receive an Announce message from                a master. preMaster    \- The port shall behave in all respects                as though it were in the MASTER state                except that it shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, signaling, or                management messages. master       \- The port is behaving as a master port.             passive      \- The port shall not place any                messages on its communication path                except for Pdelay\_Req, Pdelay\_Resp,                Pdelay\_Resp\_Follow\_Up, or signaling                messages, or management messages                that are a required response to                another management message uncalibrated \- The local port is preparing to                synchronize to the master port. slave        \- The port is synchronizing to the                selected master port
            	**type**\: :py:class:`ClockPortState_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockPortState_Enum>`
            
            .. attribute:: cptpclockportrunningtxmode
            
            	This object specifies the clock transmission mode as  unicast\:       Using unicast commnuication channel. multicast\:     Using Multicast communication channel. multicast\-mix\: Using multicast\-unicast communication channel
            	**type**\: :py:class:`ClockTxModeType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockTxModeType_Enum>`
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockportrunningclockinstanceindex = None
                self.cptpclockportrunningclocktypeindex = None
                self.cptpclockportrunningdomainindex = None
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
                if self.cptpclockportrunningclockinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockportrunningclockinstanceindex is None')
                if self.cptpclockportrunningclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockportrunningclocktypeindex is None')
                if self.cptpclockportrunningdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockportrunningdomainindex is None')
                if self.cptpclockportrunningportnumberindex is None:
                    raise YPYDataValidationError('Key property cptpclockportrunningportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortRunningTable/CISCO-PTP-MIB:cPtpClockPortRunningEntry[CISCO-PTP-MIB:cPtpClockPortRunningClockInstanceIndex = ' + str(self.cptpclockportrunningclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortRunningClockTypeIndex = ' + str(self.cptpclockportrunningclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortRunningDomainIndex = ' + str(self.cptpclockportrunningdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortRunningPortNumberIndex = ' + str(self.cptpclockportrunningportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockportrunningclockinstanceindex is not None:
                    return True

                if self.cptpclockportrunningclocktypeindex is not None:
                    return True

                if self.cptpclockportrunningdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockPortRunningTable.CPtpClockPortRunningEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortRunningTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockportrunningentry is not None:
                for child_ref in self.cptpclockportrunningentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockPortRunningTable']['meta_info']


    class CPtpClockPortTable(object):
        """
        Table of information about the clock ports for a particular
        domain.
        
        .. attribute:: cptpclockportentry
        
        	An entry in the table, containing information about a single clock port
        	**type**\: list of :py:class:`CPtpClockPortEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTable.CPtpClockPortEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockportentry = YList()
            self.cptpclockportentry.parent = self
            self.cptpclockportentry.name = 'cptpclockportentry'


        class CPtpClockPortEntry(object):
            """
            An entry in the table, containing information about a single
            clock port.
            
            .. attribute:: cptpclockportclockinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockportdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockporttableportnumberindex
            
            	This object specifies the PTP Portnumber for this port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockportcurrentpeeraddress
            
            	This object specifies the current peer's network address used for PTP communication. Based on the scenario and the setup involved, the values might look like these \- Scenario                   Value \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Single Master          master port Multiple Masters       selected master port Single Slave           slave port Multiple Slaves        <empty>  (In relevant setups, information on available slaves and available masters will be available through  cPtpClockPortAssociateTable)
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cptpclockportcurrentpeeraddresstype
            
            	This object specifies the current peer's network address used for PTP communication. Based on the scenario and the setup involved, the values might look like these \- Scenario                   Value \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Single Master          master port Multiple Masters       selected master port Single Slave           slave port Multiple Slaves        <empty>  (In relevant setups, information on available slaves and available masters will be available through  cPtpClockPortAssociateTable)
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cptpclockportname
            
            	This object specifies the PTP clock port name configured on the router
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cptpclockportnumofassociatedports
            
            	This object specifies \- For a master port \- the number of PTP slave sessions (peers) associated with this PTP port. For a slave port \- the number of masters available to this slave port (might or might not be peered)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclockportrole
            
            	This object describes the current role (slave/master) of the port
            	**type**\: :py:class:`ClockRoleType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockRoleType_Enum>`
            
            .. attribute:: cptpclockportsynconestep
            
            	This object specifies that one\-step clock operation between the PTP master and slave device is enabled
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockportclockinstanceindex = None
                self.cptpclockportclocktypeindex = None
                self.cptpclockportdomainindex = None
                self.cptpclockporttableportnumberindex = None
                self.cptpclockportcurrentpeeraddress = None
                self.cptpclockportcurrentpeeraddresstype = None
                self.cptpclockportname = None
                self.cptpclockportnumofassociatedports = None
                self.cptpclockportrole = None
                self.cptpclockportsynconestep = None

            @property
            def _common_path(self):
                if self.cptpclockportclockinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockportclockinstanceindex is None')
                if self.cptpclockportclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockportclocktypeindex is None')
                if self.cptpclockportdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockportdomainindex is None')
                if self.cptpclockporttableportnumberindex is None:
                    raise YPYDataValidationError('Key property cptpclockporttableportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTable/CISCO-PTP-MIB:cPtpClockPortEntry[CISCO-PTP-MIB:cPtpClockPortClockInstanceIndex = ' + str(self.cptpclockportclockinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortClockTypeIndex = ' + str(self.cptpclockportclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockPortDomainIndex = ' + str(self.cptpclockportdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortTablePortNumberIndex = ' + str(self.cptpclockporttableportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockportclockinstanceindex is not None:
                    return True

                if self.cptpclockportclocktypeindex is not None:
                    return True

                if self.cptpclockportdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockPortTable.CPtpClockPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockportentry is not None:
                for child_ref in self.cptpclockportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockPortTable']['meta_info']


    class CPtpClockPortTransDSTable(object):
        """
        Table of information about the Transparent clock ports running
        dataset for a particular domain.
        
        .. attribute:: cptpclockporttransdsentry
        
        	An entry in the table, containing clock port Transparent dataset information about a single clock port
        	**type**\: list of :py:class:`CPtpClockPortTransDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockPortTransDSTable.CPtpClockPortTransDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockporttransdsentry = YList()
            self.cptpclockporttransdsentry.parent = self
            self.cptpclockporttransdsentry.name = 'cptpclockporttransdsentry'


        class CPtpClockPortTransDSEntry(object):
            """
            An entry in the table, containing clock port Transparent
            dataset information about a single clock port
            
            .. attribute:: cptpclockporttransdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockporttransdsinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockporttransdsportnumberindex
            
            	This object specifies the PTP port number associated with this port
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cptpclockporttransdsfaultyflag
            
            	This object specifies the value TRUE if the port is faulty and FALSE if the port is operating normally
            	**type**\: bool
            
            .. attribute:: cptpclockporttransdslogminpdelayreqint
            
            	This object specifies the value of the logarithm to the base 2 of the minPdelayReqInterval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclockporttransdspeermeanpathdelay
            
            	This object specifies, (if the delayMechanism used is P2P) the value is the estimate of the current one\-way propagation delay, i.e., <meanPathDelay> on the link attached to this port computed using the peer delay mechanism. If the value of the delayMechanism used is E2E, then the value will be zero
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclockporttransdsportidentity
            
            	This object specifies the value of the PortIdentity attribute of the local port
            	**type**\: str
            
            	**range:** 1..255
            
            

            """

            _prefix = 'cisco-ptp'
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
                    raise YPYDataValidationError('Key property cptpclockporttransdsdomainindex is None')
                if self.cptpclockporttransdsinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockporttransdsinstanceindex is None')
                if self.cptpclockporttransdsportnumberindex is None:
                    raise YPYDataValidationError('Key property cptpclockporttransdsportnumberindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTransDSTable/CISCO-PTP-MIB:cPtpClockPortTransDSEntry[CISCO-PTP-MIB:cPtpClockPortTransDSDomainIndex = ' + str(self.cptpclockporttransdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockPortTransDSInstanceIndex = ' + str(self.cptpclockporttransdsinstanceindex) + '][CISCO-PTP-MIB:cPtpClockPortTransDSPortNumberIndex = ' + str(self.cptpclockporttransdsportnumberindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockPortTransDSTable.CPtpClockPortTransDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockPortTransDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockporttransdsentry is not None:
                for child_ref in self.cptpclockporttransdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockPortTransDSTable']['meta_info']


    class CPtpClockRunningTable(object):
        """
        Table of information about the PTP clock Running Datasets for
        all domains.
        
        .. attribute:: cptpclockrunningentry
        
        	An entry in the table, containing information about a single PTP clock running Datasets for a domain
        	**type**\: list of :py:class:`CPtpClockRunningEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockRunningTable.CPtpClockRunningEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclockrunningentry = YList()
            self.cptpclockrunningentry.parent = self
            self.cptpclockrunningentry.name = 'cptpclockrunningentry'


        class CPtpClockRunningEntry(object):
            """
            An entry in the table, containing information about a single
            PTP clock running Datasets for a domain.
            
            .. attribute:: cptpclockrunningclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclockrunningdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockrunninginstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclockrunningpacketsreceived
            
            	This object specifies the total number of all packet Unicast and multicast that have been received for this clock in this domain for this type
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockrunningpacketssent
            
            	This object specifies the total number of all packet Unicast and multicast that have been sent out for this clock in this domain for this type
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cptpclockrunningstate
            
            	This object specifies the Clock state returned by PTP engine which was described earlier.  Freerun state. Applies to a slave device that is not locked to a master. This is the initial state a slave starts out with when it is not getting any PTP packets from the master or because of some other input error (erroneous packets, etc).  Holdover state. In this state the slave device is locked to a master but communication with the master is lost or the timestamps in the ptp packets are incorrect. But since the slave was locked to the master, it can run with the same accuracy for sometime. The slave can continue to operate in this state for some time. If communication with the master is not restored for a while, the device is moved to the FREERUN state.  Acquiring state. The slave device is receiving packets from a master and is trying to acquire a lock.  Freq\_locked state. Slave device is locked to the Master with respect to frequency, but not phase aligned  Phase\_aligned state. Locked to the master with respect to frequency and phase
            	**type**\: :py:class:`ClockStateType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockStateType_Enum>`
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclockrunningclocktypeindex = None
                self.cptpclockrunningdomainindex = None
                self.cptpclockrunninginstanceindex = None
                self.cptpclockrunningpacketsreceived = None
                self.cptpclockrunningpacketssent = None
                self.cptpclockrunningstate = None

            @property
            def _common_path(self):
                if self.cptpclockrunningclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclockrunningclocktypeindex is None')
                if self.cptpclockrunningdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclockrunningdomainindex is None')
                if self.cptpclockrunninginstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclockrunninginstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockRunningTable/CISCO-PTP-MIB:cPtpClockRunningEntry[CISCO-PTP-MIB:cPtpClockRunningClockTypeIndex = ' + str(self.cptpclockrunningclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockRunningDomainIndex = ' + str(self.cptpclockrunningdomainindex) + '][CISCO-PTP-MIB:cPtpClockRunningInstanceIndex = ' + str(self.cptpclockrunninginstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclockrunningclocktypeindex is not None:
                    return True

                if self.cptpclockrunningdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockRunningTable.CPtpClockRunningEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockRunningTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclockrunningentry is not None:
                for child_ref in self.cptpclockrunningentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockRunningTable']['meta_info']


    class CPtpClockTimePropertiesDSTable(object):
        """
        Table of information about the PTP clock Timeproperties
        Datasets for all domains.
        
        .. attribute:: cptpclocktimepropertiesdsentry
        
        	An entry in the table, containing information about a single PTP clock timeproperties Datasets for a domain
        	**type**\: list of :py:class:`CPtpClockTimePropertiesDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTimePropertiesDSTable.CPtpClockTimePropertiesDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclocktimepropertiesdsentry = YList()
            self.cptpclocktimepropertiesdsentry.parent = self
            self.cptpclocktimepropertiesdsentry.name = 'cptpclocktimepropertiesdsentry'


        class CPtpClockTimePropertiesDSEntry(object):
            """
            An entry in the table, containing information about a single
            PTP clock timeproperties Datasets for a domain.
            
            .. attribute:: cptpclocktimepropertiesdsclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpclocktimepropertiesdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktimepropertiesdsinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktimepropertiesdscurrentutcoffset
            
            	This object specifies the timeproperties dataset value of current UTC offset.  In PTP systems whose epoch is the PTP epoch, the value of timePropertiesDS.currentUtcOffset is the offset between TAI and UTC; otherwise the value has no meaning. The value shall be in units of seconds. The initialization value shall be selected as follows\: a) If the timePropertiesDS.ptpTimescale (see 8.2.4.8) is TRUE, the value is the value obtained from a primary reference if the value is known at the time of initialization, else. b) The value shall be the current number of leap seconds (7.2.3) when the node is designed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cptpclocktimepropertiesdscurrentutcoffsetvalid
            
            	This object specifies the timeproperties dataset value of whether current UTC offset is valid
            	**type**\: bool
            
            .. attribute:: cptpclocktimepropertiesdsfreqtraceable
            
            	This object specifies the Frequency Traceable value in the clock Current Dataset
            	**type**\: bool
            
            .. attribute:: cptpclocktimepropertiesdsleap59
            
            	This object specifies the Leap59 value in the clock Current Dataset
            	**type**\: bool
            
            .. attribute:: cptpclocktimepropertiesdsleap61
            
            	This object specifies the Leap61 value in the clock Current Dataset
            	**type**\: bool
            
            .. attribute:: cptpclocktimepropertiesdsptptimescale
            
            	This object specifies the PTP Timescale value in the clock Current Dataset
            	**type**\: bool
            
            .. attribute:: cptpclocktimepropertiesdssource
            
            	This object specifies the Timesource value in the clock Current Dataset
            	**type**\: :py:class:`ClockTimeSourceType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockTimeSourceType_Enum>`
            
            .. attribute:: cptpclocktimepropertiesdstimetraceable
            
            	This object specifies the Timetraceable value in the clock Current Dataset
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpclocktimepropertiesdsclocktypeindex = None
                self.cptpclocktimepropertiesdsdomainindex = None
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
                if self.cptpclocktimepropertiesdsclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpclocktimepropertiesdsclocktypeindex is None')
                if self.cptpclocktimepropertiesdsdomainindex is None:
                    raise YPYDataValidationError('Key property cptpclocktimepropertiesdsdomainindex is None')
                if self.cptpclocktimepropertiesdsinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclocktimepropertiesdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTimePropertiesDSTable/CISCO-PTP-MIB:cPtpClockTimePropertiesDSEntry[CISCO-PTP-MIB:cPtpClockTimePropertiesDSClockTypeIndex = ' + str(self.cptpclocktimepropertiesdsclocktypeindex) + '][CISCO-PTP-MIB:cPtpClockTimePropertiesDSDomainIndex = ' + str(self.cptpclocktimepropertiesdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockTimePropertiesDSInstanceIndex = ' + str(self.cptpclocktimepropertiesdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpclocktimepropertiesdsclocktypeindex is not None:
                    return True

                if self.cptpclocktimepropertiesdsdomainindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockTimePropertiesDSTable.CPtpClockTimePropertiesDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTimePropertiesDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclocktimepropertiesdsentry is not None:
                for child_ref in self.cptpclocktimepropertiesdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockTimePropertiesDSTable']['meta_info']


    class CPtpClockTransDefaultDSTable(object):
        """
        Table of information about the PTP Transparent clock Default
        Datasets for all domains.
        
        .. attribute:: cptpclocktransdefaultdsentry
        
        	An entry in the table, containing information about a single PTP Transparent clock Default Datasets for a domain
        	**type**\: list of :py:class:`CPtpClockTransDefaultDSEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpClockTransDefaultDSTable.CPtpClockTransDefaultDSEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpclocktransdefaultdsentry = YList()
            self.cptpclocktransdefaultdsentry.parent = self
            self.cptpclocktransdefaultdsentry.name = 'cptpclocktransdefaultdsentry'


        class CPtpClockTransDefaultDSEntry(object):
            """
            An entry in the table, containing information about a single
            PTP Transparent clock Default Datasets for a domain.
            
            .. attribute:: cptpclocktransdefaultdsdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktransdefaultdsinstanceindex
            
            	This object specifies the instance of the clock for this clock type in the given domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpclocktransdefaultdsclockidentity
            
            	This object specifies the value of the clockIdentity attribute of the local clock
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cptpclocktransdefaultdsdelay
            
            	This object, if the transparent clock is an end\-to\-end transparent clock, has the value shall be E2E; If the transparent clock is a peer\-to\-peer transparent clock, the value shall be P2P
            	**type**\: :py:class:`ClockMechanismType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockMechanismType_Enum>`
            
            .. attribute:: cptpclocktransdefaultdsnumofports
            
            	This object specifies the number of PTP ports of the device
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpclocktransdefaultdsprimarydomain
            
            	This object specifies the value of the primary syntonization domain. The initialization value shall be 0
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'cisco-ptp'
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
                    raise YPYDataValidationError('Key property cptpclocktransdefaultdsdomainindex is None')
                if self.cptpclocktransdefaultdsinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpclocktransdefaultdsinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTransDefaultDSTable/CISCO-PTP-MIB:cPtpClockTransDefaultDSEntry[CISCO-PTP-MIB:cPtpClockTransDefaultDSDomainIndex = ' + str(self.cptpclocktransdefaultdsdomainindex) + '][CISCO-PTP-MIB:cPtpClockTransDefaultDSInstanceIndex = ' + str(self.cptpclocktransdefaultdsinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpClockTransDefaultDSTable.CPtpClockTransDefaultDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpClockTransDefaultDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpclocktransdefaultdsentry is not None:
                for child_ref in self.cptpclocktransdefaultdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpClockTransDefaultDSTable']['meta_info']


    class CPtpSystemDomainTable(object):
        """
        Table of information about the PTP system for all clock modes
        \-\- ordinary, boundary or transparent.
        
        .. attribute:: cptpsystemdomainentry
        
        	An entry in the table, containing information about a single clock mode for the PTP system. A row entry gets added when PTP clocks are configured on the router
        	**type**\: list of :py:class:`CPtpSystemDomainEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemDomainTable.CPtpSystemDomainEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpsystemdomainentry = YList()
            self.cptpsystemdomainentry.parent = self
            self.cptpsystemdomainentry.name = 'cptpsystemdomainentry'


        class CPtpSystemDomainEntry(object):
            """
            An entry in the table, containing information about a single
            clock mode for the PTP system. A row entry gets added when PTP
            clocks are configured on the router.
            
            .. attribute:: cptpsystemdomainclocktypeindex
            
            	This object specifies the clock type as defined in the Textual convention description
            	**type**\: :py:class:`ClockType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockType_Enum>`
            
            .. attribute:: cptpsystemdomaintotals
            
            	This object specifies the  total number of PTP domains for this particular clock type configured in this node
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ptp'
            _revision = '2011-01-28'

            def __init__(self):
                self.parent = None
                self.cptpsystemdomainclocktypeindex = None
                self.cptpsystemdomaintotals = None

            @property
            def _common_path(self):
                if self.cptpsystemdomainclocktypeindex is None:
                    raise YPYDataValidationError('Key property cptpsystemdomainclocktypeindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemDomainTable/CISCO-PTP-MIB:cPtpSystemDomainEntry[CISCO-PTP-MIB:cPtpSystemDomainClockTypeIndex = ' + str(self.cptpsystemdomainclocktypeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpsystemdomainclocktypeindex is not None:
                    return True

                if self.cptpsystemdomaintotals is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpSystemDomainTable.CPtpSystemDomainEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemDomainTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpsystemdomainentry is not None:
                for child_ref in self.cptpsystemdomainentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpSystemDomainTable']['meta_info']


    class CPtpSystemTable(object):
        """
        Table of count information about the PTP system for all
        domains.
        
        .. attribute:: cptpsystementry
        
        	An entry in the table, containing count information about a single domain. New row entries are added when the PTP clock for this domain is configured, while the unconfiguration of the PTP clock removes it
        	**type**\: list of :py:class:`CPtpSystemEntry <ydk.models.ptp.CISCO_PTP_MIB.CISCOPTPMIB.CPtpSystemTable.CPtpSystemEntry>`
        
        

        """

        _prefix = 'cisco-ptp'
        _revision = '2011-01-28'

        def __init__(self):
            self.parent = None
            self.cptpsystementry = YList()
            self.cptpsystementry.parent = self
            self.cptpsystementry.name = 'cptpsystementry'


        class CPtpSystemEntry(object):
            """
            An entry in the table, containing count information about a
            single domain. New row entries are added when the PTP clock for
            this domain is configured, while the unconfiguration of the PTP
            clock removes it.
            
            .. attribute:: cptpdomainindex
            
            	This object specifies the domain number used to create logical group of PTP devices. The Clock Domain is a logical group of clocks and devices that synchronize with each other using the PTP protocol.   0           Default domain 1           Alternate domain 1 2           Alternate domain 2 3           Alternate domain 3 4 \- 127     User\-defined domains 128 \- 255   Reserved
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpinstanceindex
            
            	This object specifies the instance of the Clock for this domain
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cptpdomainclockportphysicalinterfacestotal
            
            	This object specifies the total number of clock port Physical interfaces configured within a domain instance for PTP communications
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cptpdomainclockportstotal
            
            	This object specifies the total number of clock ports configured within a domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ptp'
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
                    raise YPYDataValidationError('Key property cptpdomainindex is None')
                if self.cptpinstanceindex is None:
                    raise YPYDataValidationError('Key property cptpinstanceindex is None')

                return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemTable/CISCO-PTP-MIB:cPtpSystemEntry[CISCO-PTP-MIB:cPtpDomainIndex = ' + str(self.cptpdomainindex) + '][CISCO-PTP-MIB:cPtpInstanceIndex = ' + str(self.cptpinstanceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cptpdomainindex is not None:
                    return True

                if self.cptpinstanceindex is not None:
                    return True

                if self.cptpdomainclockportphysicalinterfacestotal is not None:
                    return True

                if self.cptpdomainclockportstotal is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
                return meta._meta_table['CISCOPTPMIB.CPtpSystemTable.CPtpSystemEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PTP-MIB:CISCO-PTP-MIB/CISCO-PTP-MIB:cPtpSystemTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpsystementry is not None:
                for child_ref in self.cptpsystementry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CPtpSystemTable']['meta_info']


    class CiscoPtpMIBSystemInfo(object):
        """
        
        
        .. attribute:: cptpsystemprofile
        
        	This object specifies the PTP Profile implemented on the system
        	**type**\: :py:class:`ClockProfileType_Enum <ydk.models.ptp.CISCO_PTP_MIB.ClockProfileType_Enum>`
        
        

        """

        _prefix = 'cisco-ptp'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cptpsystemprofile is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
            return meta._meta_table['CISCOPTPMIB.CiscoPtpMIBSystemInfo']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-PTP-MIB:CISCO-PTP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscoptpmibsysteminfo is not None and self.ciscoptpmibsysteminfo._has_data():
            return True

        if self.ciscoptpmibsysteminfo is not None and self.ciscoptpmibsysteminfo.is_presence():
            return True

        if self.cptpclockcurrentdstable is not None and self.cptpclockcurrentdstable._has_data():
            return True

        if self.cptpclockcurrentdstable is not None and self.cptpclockcurrentdstable.is_presence():
            return True

        if self.cptpclockdefaultdstable is not None and self.cptpclockdefaultdstable._has_data():
            return True

        if self.cptpclockdefaultdstable is not None and self.cptpclockdefaultdstable.is_presence():
            return True

        if self.cptpclocknodetable is not None and self.cptpclocknodetable._has_data():
            return True

        if self.cptpclocknodetable is not None and self.cptpclocknodetable.is_presence():
            return True

        if self.cptpclockparentdstable is not None and self.cptpclockparentdstable._has_data():
            return True

        if self.cptpclockparentdstable is not None and self.cptpclockparentdstable.is_presence():
            return True

        if self.cptpclockportassociatetable is not None and self.cptpclockportassociatetable._has_data():
            return True

        if self.cptpclockportassociatetable is not None and self.cptpclockportassociatetable.is_presence():
            return True

        if self.cptpclockportdstable is not None and self.cptpclockportdstable._has_data():
            return True

        if self.cptpclockportdstable is not None and self.cptpclockportdstable.is_presence():
            return True

        if self.cptpclockportrunningtable is not None and self.cptpclockportrunningtable._has_data():
            return True

        if self.cptpclockportrunningtable is not None and self.cptpclockportrunningtable.is_presence():
            return True

        if self.cptpclockporttable is not None and self.cptpclockporttable._has_data():
            return True

        if self.cptpclockporttable is not None and self.cptpclockporttable.is_presence():
            return True

        if self.cptpclockporttransdstable is not None and self.cptpclockporttransdstable._has_data():
            return True

        if self.cptpclockporttransdstable is not None and self.cptpclockporttransdstable.is_presence():
            return True

        if self.cptpclockrunningtable is not None and self.cptpclockrunningtable._has_data():
            return True

        if self.cptpclockrunningtable is not None and self.cptpclockrunningtable.is_presence():
            return True

        if self.cptpclocktimepropertiesdstable is not None and self.cptpclocktimepropertiesdstable._has_data():
            return True

        if self.cptpclocktimepropertiesdstable is not None and self.cptpclocktimepropertiesdstable.is_presence():
            return True

        if self.cptpclocktransdefaultdstable is not None and self.cptpclocktransdefaultdstable._has_data():
            return True

        if self.cptpclocktransdefaultdstable is not None and self.cptpclocktransdefaultdstable.is_presence():
            return True

        if self.cptpsystemdomaintable is not None and self.cptpsystemdomaintable._has_data():
            return True

        if self.cptpsystemdomaintable is not None and self.cptpsystemdomaintable.is_presence():
            return True

        if self.cptpsystemtable is not None and self.cptpsystemtable._has_data():
            return True

        if self.cptpsystemtable is not None and self.cptpsystemtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ptp._meta import _CISCO_PTP_MIB as meta
        return meta._meta_table['CISCOPTPMIB']['meta_info']


