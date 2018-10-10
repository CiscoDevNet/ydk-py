""" Cisco_IOS_XR_infra_sla_datatypes 

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



class SlaActionTypeEnum(Enum):
    """
    SlaActionTypeEnum (Enum Class)

    Sla action type enum

    .. data:: log = 0

    	Emit a syslog when the threshold is crossed

    """

    log = Enum.YLeaf(0, "log")


class SlaBucketsSizeUnitsEnum(Enum):
    """
    SlaBucketsSizeUnitsEnum (Enum Class)

    Sla buckets size units enum

    .. data:: buckets_per_probe = 0

    	Store results as a number of buckets per probe

    	- note that this option has been DEPRECATED

    .. data:: probes_per_bucket = 1

    	Store results as a number of probes per bucket

    """

    buckets_per_probe = Enum.YLeaf(0, "buckets-per-probe")

    probes_per_bucket = Enum.YLeaf(1, "probes-per-bucket")


class SlaBurstIntervalUnitsEnum(Enum):
    """
    SlaBurstIntervalUnitsEnum (Enum Class)

    Sla burst interval units enum

    .. data:: once = 1

    	Send one burst per probe

    .. data:: milliseconds = 2

    	Send bursts within a probe with an interval

    	unit of milliseconds

    .. data:: seconds = 3

    	Send bursts within a probe with an interval

    	unit of seconds

    .. data:: minutes = 4

    	Send bursts within a probe with an interval

    	unit of minutes

    .. data:: hours = 5

    	Send bursts within a probe with an interval

    	unit of hours

    """

    once = Enum.YLeaf(1, "once")

    milliseconds = Enum.YLeaf(2, "milliseconds")

    seconds = Enum.YLeaf(3, "seconds")

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")


class SlaOnDemandProbeDurationUnitsEnum(Enum):
    """
    SlaOnDemandProbeDurationUnitsEnum (Enum Class)

    Sla on demand probe duration units enum

    .. data:: seconds = 3

    	Schedule probes to run with a duration unit of

    	seconds

    .. data:: minutes = 4

    	Schedule probes to run with a duration unit of

    	minutes

    .. data:: hours = 5

    	Schedule probes to run with a duration unit of

    	hours

    """

    seconds = Enum.YLeaf(3, "seconds")

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")


class SlaOnDemandRepeatIntervalUnitsEnum(Enum):
    """
    SlaOnDemandRepeatIntervalUnitsEnum (Enum Class)

    Sla on demand repeat interval units enum

    .. data:: seconds = 3

    	Schedule probes to repeat with an interval unit

    	of seconds

    .. data:: minutes = 4

    	Schedule probes to repeat with an interval unit

    	of minutes

    .. data:: hours = 5

    	Schedule probes to repeat with an interval unit

    	of hours

    """

    seconds = Enum.YLeaf(3, "seconds")

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")


class SlaOnDemandStartMonthEnum(Enum):
    """
    SlaOnDemandStartMonthEnum (Enum Class)

    Sla on demand start month enum

    .. data:: january = 0

    	January

    .. data:: february = 1

    	February

    .. data:: march = 2

    	March

    .. data:: april = 3

    	April

    .. data:: may = 4

    	May

    .. data:: june = 5

    	June

    .. data:: july = 6

    	July

    .. data:: august = 7

    	August

    .. data:: september = 8

    	September

    .. data:: october = 9

    	October

    .. data:: november = 10

    	November

    .. data:: december = 11

    	December

    """

    january = Enum.YLeaf(0, "january")

    february = Enum.YLeaf(1, "february")

    march = Enum.YLeaf(2, "march")

    april = Enum.YLeaf(3, "april")

    may = Enum.YLeaf(4, "may")

    june = Enum.YLeaf(5, "june")

    july = Enum.YLeaf(6, "july")

    august = Enum.YLeaf(7, "august")

    september = Enum.YLeaf(8, "september")

    october = Enum.YLeaf(9, "october")

    november = Enum.YLeaf(10, "november")

    december = Enum.YLeaf(11, "december")


class SlaOnDemandStartTimeRelativeUnitsEnum(Enum):
    """
    SlaOnDemandStartTimeRelativeUnitsEnum (Enum Class)

    Sla on demand start time relative units enum

    .. data:: seconds = 3

    	Schedule probe to start after a unit of seconds

    .. data:: minutes = 4

    	Schedule probe to start after a unit of minutes

    .. data:: hours = 5

    	Schedule probe to start after a unit of hours

    """

    seconds = Enum.YLeaf(3, "seconds")

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")


class SlaOnDemandStartTimeTypesEnum(Enum):
    """
    SlaOnDemandStartTimeTypesEnum (Enum Class)

    Sla on demand start time types enum

    .. data:: now = 0

    	Start immediately

    .. data:: absolute = 1

    	Start at a specified time

    .. data:: relative = 2

    	Start after a specified period

    """

    now = Enum.YLeaf(0, "now")

    absolute = Enum.YLeaf(1, "absolute")

    relative = Enum.YLeaf(2, "relative")


class SlaPacketIntervalUnitsEnum(Enum):
    """
    SlaPacketIntervalUnitsEnum (Enum Class)

    Sla packet interval units enum

    .. data:: once = 1

    	Send one packet per burst

    .. data:: milliseconds = 2

    	Send packets with an interval unit of

    	milliseconds

    .. data:: seconds = 3

    	Send packets with an interval unit of seconds

    .. data:: minutes = 4

    	Send packets with an interval unit of minutes

    .. data:: hours = 5

    	Send packets with an interval unit of hours

    """

    once = Enum.YLeaf(1, "once")

    milliseconds = Enum.YLeaf(2, "milliseconds")

    seconds = Enum.YLeaf(3, "seconds")

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")


class SlaPaddingPattern(Enum):
    """
    SlaPaddingPattern (Enum Class)

    Sla padding pattern

    .. data:: hex = 0

    	Use an optionally specified hex pattern for

    	packet padding

    .. data:: pseudo_random = 1

    	Use a pseudo-random bit sequence for packet

    	padding

    """

    hex = Enum.YLeaf(0, "hex")

    pseudo_random = Enum.YLeaf(1, "pseudo-random")


class SlaProbeDurationUnitsEnum(Enum):
    """
    SlaProbeDurationUnitsEnum (Enum Class)

    Sla probe duration units enum

    .. data:: seconds = 3

    	Schedule probes to run with a duration unit of

    	seconds

    .. data:: minutes = 4

    	Schedule probes to run with a duration unit of

    	minutes

    .. data:: hours = 5

    	Schedule probes to run with a duration unit of

    	hours

    .. data:: day = 6

    	Schedule probes to run for a duration of 1 day

    .. data:: week = 7

    	Schedule probes to run for a duration of 1 week

    """

    seconds = Enum.YLeaf(3, "seconds")

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")

    day = Enum.YLeaf(6, "day")

    week = Enum.YLeaf(7, "week")


class SlaProbeIntervalDayEnum(Enum):
    """
    SlaProbeIntervalDayEnum (Enum Class)

    Sla probe interval day enum

    .. data:: monday = 1

    	Schedule every Monday

    .. data:: tuesday = 2

    	Schedule every Tuesday

    .. data:: wednesday = 3

    	Schedule every Wednesday

    .. data:: thursday = 4

    	Schedule every Thursday

    .. data:: friday = 5

    	Schedule every Friday

    .. data:: saturday = 6

    	Schedule every Saturday

    .. data:: sunday = 7

    	Schedule every Sunday

    """

    monday = Enum.YLeaf(1, "monday")

    tuesday = Enum.YLeaf(2, "tuesday")

    wednesday = Enum.YLeaf(3, "wednesday")

    thursday = Enum.YLeaf(4, "thursday")

    friday = Enum.YLeaf(5, "friday")

    saturday = Enum.YLeaf(6, "saturday")

    sunday = Enum.YLeaf(7, "sunday")


class SlaProbeIntervalUnitsEnum(Enum):
    """
    SlaProbeIntervalUnitsEnum (Enum Class)

    Sla probe interval units enum

    .. data:: minutes = 4

    	Schedule probes to run with an interval unit of

    	minutes

    .. data:: hours = 5

    	Schedule probes to run with an interval unit of

    	hours

    .. data:: day = 6

    	Schedule probes to run every day

    .. data:: week = 7

    	Schedule probes to run every week

    """

    minutes = Enum.YLeaf(4, "minutes")

    hours = Enum.YLeaf(5, "hours")

    day = Enum.YLeaf(6, "day")

    week = Enum.YLeaf(7, "week")


class SlaSend(Enum):
    """
    SlaSend (Enum Class)

    Sla send

    .. data:: packet = 0

    	Send individual packets

    .. data:: burst = 1

    	Send bursts of packets

    """

    packet = Enum.YLeaf(0, "packet")

    burst = Enum.YLeaf(1, "burst")


class SlaStatisticTypeEnum(Enum):
    """
    SlaStatisticTypeEnum (Enum Class)

    Sla statistic type enum

    .. data:: round_trip_delay = 1

    	Collect round trip delay metric data

    .. data:: one_way_delay_sd = 2

    	Collect one way delay source->dest metric data

    .. data:: one_way_delay_ds = 3

    	Collect one way delay dest->source metric data

    .. data:: round_trip_jitter = 4

    	Collect round trip delay metric data

    .. data:: one_way_jitter_sd = 5

    	Collect one way jitter source->dest metric data

    .. data:: one_way_jitter_ds = 6

    	Collect one way jitter dest->source metric data

    .. data:: one_way_loss_sd = 7

    	Collect one way loss source->dest metric data

    .. data:: one_way_loss_ds = 8

    	Collect one way loss dest->source metric data

    """

    round_trip_delay = Enum.YLeaf(1, "round-trip-delay")

    one_way_delay_sd = Enum.YLeaf(2, "one-way-delay-sd")

    one_way_delay_ds = Enum.YLeaf(3, "one-way-delay-ds")

    round_trip_jitter = Enum.YLeaf(4, "round-trip-jitter")

    one_way_jitter_sd = Enum.YLeaf(5, "one-way-jitter-sd")

    one_way_jitter_ds = Enum.YLeaf(6, "one-way-jitter-ds")

    one_way_loss_sd = Enum.YLeaf(7, "one-way-loss-sd")

    one_way_loss_ds = Enum.YLeaf(8, "one-way-loss-ds")


class SlaThresholdConditionEnum(Enum):
    """
    SlaThresholdConditionEnum (Enum Class)

    Sla threshold condition enum

    .. data:: max = 0

    	Threshold is breached when the maximum value

    	crosses the configured threshold value

    .. data:: mean = 1

    	Threshold is breached when the mean value

    	crosses the configured threshold value

    .. data:: sample_count = 2

    	Threshold is breached when the sample count in

    	bins in and above a certain bin number crosses

    	the configured sample count

    """

    max = Enum.YLeaf(0, "max")

    mean = Enum.YLeaf(1, "mean")

    sample_count = Enum.YLeaf(2, "sample-count")


class SlaThresholdTypeEnum(Enum):
    """
    SlaThresholdTypeEnum (Enum Class)

    Sla threshold type enum

    .. data:: stateless = 1

    	Stateless threshold

    """

    stateless = Enum.YLeaf(1, "stateless")



