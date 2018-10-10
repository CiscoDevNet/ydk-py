""" Cisco_IOS_XR_ptp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PtpClockAdvertisementMode(Enum):
    """
    PtpClockAdvertisementMode (Enum Class)

    Ptp clock advertisement mode

    .. data:: Y_1588v2 = 0

    	Use 1588v2 clock selection

    .. data:: telecom_profile = 1

    	Use Telecom Profile clock selection

    """

    Y_1588v2 = Enum.YLeaf(0, "1588v2")

    telecom_profile = Enum.YLeaf(1, "telecom-profile")


class PtpClockId(Enum):
    """
    PtpClockId (Enum Class)

    Ptp clock id

    .. data:: router_mac = 0

    	Use the router's MAC

    .. data:: user_mac = 1

    	Use a user-specified MAC

    .. data:: eui = 2

    	Use a user-specified EUI-64 number

    """

    router_mac = Enum.YLeaf(0, "router-mac")

    user_mac = Enum.YLeaf(1, "user-mac")

    eui = Enum.YLeaf(2, "eui")


class PtpClockOperation(Enum):
    """
    PtpClockOperation (Enum Class)

    Ptp clock operation

    .. data:: two_step = 0

    	Two-step clock operation

    .. data:: one_step = 1

    	One-step clock operation

    """

    two_step = Enum.YLeaf(0, "two-step")

    one_step = Enum.YLeaf(1, "one-step")


class PtpClockProfile(Enum):
    """
    PtpClockProfile (Enum Class)

    Ptp clock profile

    .. data:: default = 0

    	Default clock profile

    .. data:: g82651 = 1

    	G.8265.1 profile

    .. data:: g82751 = 2

    	G.8275.1 profile

    .. data:: g82752 = 3

    	G.8275.2 profile

    """

    default = Enum.YLeaf(0, "default")

    g82651 = Enum.YLeaf(1, "g82651")

    g82751 = Enum.YLeaf(2, "g82751")

    g82752 = Enum.YLeaf(3, "g82752")


class PtpClockSelectionMode(Enum):
    """
    PtpClockSelectionMode (Enum Class)

    Ptp clock selection mode

    .. data:: Y_1588v2 = 0

    	Use 1588v2 clock selection

    .. data:: telecom_profile = 1

    	Use Telecom Profile clock selection

    """

    Y_1588v2 = Enum.YLeaf(0, "1588v2")

    telecom_profile = Enum.YLeaf(1, "telecom-profile")


class PtpDelayAsymmetryUnits(Enum):
    """
    PtpDelayAsymmetryUnits (Enum Class)

    Ptp delay asymmetry units

    .. data:: nanoseconds = 0

    	Nanoseconds

    .. data:: microseconds = 1

    	Microseconds

    .. data:: milliseconds = 2

    	Milliseconds

    """

    nanoseconds = Enum.YLeaf(0, "nanoseconds")

    microseconds = Enum.YLeaf(1, "microseconds")

    milliseconds = Enum.YLeaf(2, "milliseconds")


class PtpEncap(Enum):
    """
    PtpEncap (Enum Class)

    Ptp encap

    .. data:: ethernet = 1

    	Ethernet Encapsulation

    .. data:: ipv4 = 2

    	IPv4 Encapsulation

    .. data:: ipv6 = 3

    	IPv6 Encapsulation

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(3, "ipv6")


class PtpInvalidUnicastGrantRequestResponse(Enum):
    """
    PtpInvalidUnicastGrantRequestResponse (Enum Class)

    Ptp invalid unicast grant request response

    .. data:: reduce = 0

    	Reduce grant parameters

    .. data:: deny = 1

    	Deny grant

    """

    reduce = Enum.YLeaf(0, "reduce")

    deny = Enum.YLeaf(1, "deny")


class PtpPortState(Enum):
    """
    PtpPortState (Enum Class)

    Ptp port state

    .. data:: any = 0

    	Any port state allowed

    .. data:: slave_only = 1

    	Restrict to slave

    .. data:: master_only = 2

    	Restrict to master

    """

    any = Enum.YLeaf(0, "any")

    slave_only = Enum.YLeaf(1, "slave-only")

    master_only = Enum.YLeaf(2, "master-only")


class PtpTelecomClock(Enum):
    """
    PtpTelecomClock (Enum Class)

    Ptp telecom clock

    .. data:: telecom_grandmaster = 0

    	Telecom grandmaster clock

    .. data:: telecom_boundary = 1

    	Telecom boundary clock

    .. data:: telecom_slave = 2

    	Telecom slave clock

    """

    telecom_grandmaster = Enum.YLeaf(0, "telecom-grandmaster")

    telecom_boundary = Enum.YLeaf(1, "telecom-boundary")

    telecom_slave = Enum.YLeaf(2, "telecom-slave")


class PtpTime(Enum):
    """
    PtpTime (Enum Class)

    Ptp time

    .. data:: interval = 0

    	Time interval in seconds

    .. data:: frequency = 1

    	Frequency per second

    """

    interval = Enum.YLeaf(0, "interval")

    frequency = Enum.YLeaf(1, "frequency")


class PtpTimePeriod(Enum):
    """
    PtpTimePeriod (Enum Class)

    Ptp time period

    .. data:: Y_1 = 0

    	One

    .. data:: Y_2 = 1

    	Two

    .. data:: Y_4 = 2

    	Four

    .. data:: Y_8 = 3

    	Eight

    .. data:: Y_16 = 4

    	Sixteen

    .. data:: Y_32 = 5

    	Thirty Two

    .. data:: Y_64 = 6

    	Sixty Four

    .. data:: Y_128 = 7

    	One Hundred and Twenty-Eight

    """

    Y_1 = Enum.YLeaf(0, "1")

    Y_2 = Enum.YLeaf(1, "2")

    Y_4 = Enum.YLeaf(2, "4")

    Y_8 = Enum.YLeaf(3, "8")

    Y_16 = Enum.YLeaf(4, "16")

    Y_32 = Enum.YLeaf(5, "32")

    Y_64 = Enum.YLeaf(6, "64")

    Y_128 = Enum.YLeaf(7, "128")


class PtpTimeSource(Enum):
    """
    PtpTimeSource (Enum Class)

    Ptp time source

    .. data:: unknown = 0

    	Unknown

    .. data:: atomic_clock = 16

    	Atomic Clock

    .. data:: gps = 32

    	GPS

    .. data:: terrestrial_radio = 48

    	Terrestrial Radio

    .. data:: ptp = 64

    	PTP

    .. data:: ntp = 80

    	NTP

    .. data:: hand_set = 96

    	Hand set

    .. data:: other = 144

    	Other

    .. data:: internal_oscillator = 160

    	Internal Oscillator

    """

    unknown = Enum.YLeaf(0, "unknown")

    atomic_clock = Enum.YLeaf(16, "atomic-clock")

    gps = Enum.YLeaf(32, "gps")

    terrestrial_radio = Enum.YLeaf(48, "terrestrial-radio")

    ptp = Enum.YLeaf(64, "ptp")

    ntp = Enum.YLeaf(80, "ntp")

    hand_set = Enum.YLeaf(96, "hand-set")

    other = Enum.YLeaf(144, "other")

    internal_oscillator = Enum.YLeaf(160, "internal-oscillator")


class PtpTimescale(Enum):
    """
    PtpTimescale (Enum Class)

    Ptp timescale

    .. data:: ptp = 0

    	PTP timescale

    .. data:: arb = 1

    	ARB timescale

    """

    ptp = Enum.YLeaf(0, "ptp")

    arb = Enum.YLeaf(1, "arb")


class PtpTransport(Enum):
    """
    PtpTransport (Enum Class)

    Ptp transport

    .. data:: unicast = 0

    	Unicast communication

    .. data:: mixed_mode = 1

    	Mixed-mode communication

    .. data:: multicast = 2

    	Multicast communication

    """

    unicast = Enum.YLeaf(0, "unicast")

    mixed_mode = Enum.YLeaf(1, "mixed-mode")

    multicast = Enum.YLeaf(2, "multicast")



