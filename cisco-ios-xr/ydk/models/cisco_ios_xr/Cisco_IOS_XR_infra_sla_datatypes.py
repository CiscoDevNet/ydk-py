""" Cisco_IOS_XR_infra_sla_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SlaBucketsSizeUnitsEnumEnum(Enum):
    """
    SlaBucketsSizeUnitsEnumEnum

    Sla buckets size units enum

    .. data:: buckets_per_probe = 0

    	Store results as a number of buckets per probe

    	- note that this option has been DEPRECATED

    .. data:: probes_per_bucket = 1

    	Store results as a number of probes per bucket

    """

    buckets_per_probe = 0

    probes_per_bucket = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaBucketsSizeUnitsEnumEnum']


class SlaBurstIntervalUnitsEnumEnum(Enum):
    """
    SlaBurstIntervalUnitsEnumEnum

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

    once = 1

    milliseconds = 2

    seconds = 3

    minutes = 4

    hours = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaBurstIntervalUnitsEnumEnum']


class SlaOnDemandProbeDurationUnitsEnumEnum(Enum):
    """
    SlaOnDemandProbeDurationUnitsEnumEnum

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

    seconds = 3

    minutes = 4

    hours = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandProbeDurationUnitsEnumEnum']


class SlaOnDemandRepeatIntervalUnitsEnumEnum(Enum):
    """
    SlaOnDemandRepeatIntervalUnitsEnumEnum

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

    seconds = 3

    minutes = 4

    hours = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandRepeatIntervalUnitsEnumEnum']


class SlaOnDemandStartMonthEnumEnum(Enum):
    """
    SlaOnDemandStartMonthEnumEnum

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

    january = 0

    february = 1

    march = 2

    april = 3

    may = 4

    june = 5

    july = 6

    august = 7

    september = 8

    october = 9

    november = 10

    december = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartMonthEnumEnum']


class SlaOnDemandStartTimeRelativeUnitsEnumEnum(Enum):
    """
    SlaOnDemandStartTimeRelativeUnitsEnumEnum

    Sla on demand start time relative units enum

    .. data:: seconds = 3

    	Schedule probe to start after a unit of seconds

    .. data:: minutes = 4

    	Schedule probe to start after a unit of minutes

    .. data:: hours = 5

    	Schedule probe to start after a unit of hours

    """

    seconds = 3

    minutes = 4

    hours = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartTimeRelativeUnitsEnumEnum']


class SlaOnDemandStartTimeTypesEnumEnum(Enum):
    """
    SlaOnDemandStartTimeTypesEnumEnum

    Sla on demand start time types enum

    .. data:: now = 0

    	Start immediately

    .. data:: absolute = 1

    	Start at a specified time

    .. data:: relative = 2

    	Start after a specified period

    """

    now = 0

    absolute = 1

    relative = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartTimeTypesEnumEnum']


class SlaPacketIntervalUnitsEnumEnum(Enum):
    """
    SlaPacketIntervalUnitsEnumEnum

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

    once = 1

    milliseconds = 2

    seconds = 3

    minutes = 4

    hours = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaPacketIntervalUnitsEnumEnum']


class SlaPaddingPatternEnum(Enum):
    """
    SlaPaddingPatternEnum

    Sla padding pattern

    .. data:: hex = 0

    	Use an optionally specified hex pattern for

    	packet padding

    .. data:: pseudo_random = 1

    	Use a pseudo-random bit sequence for packet

    	padding

    """

    hex = 0

    pseudo_random = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaPaddingPatternEnum']


class SlaProbeDurationUnitsEnumEnum(Enum):
    """
    SlaProbeDurationUnitsEnumEnum

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

    seconds = 3

    minutes = 4

    hours = 5

    day = 6

    week = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeDurationUnitsEnumEnum']


class SlaProbeIntervalDayEnumEnum(Enum):
    """
    SlaProbeIntervalDayEnumEnum

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

    monday = 1

    tuesday = 2

    wednesday = 3

    thursday = 4

    friday = 5

    saturday = 6

    sunday = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeIntervalDayEnumEnum']


class SlaProbeIntervalUnitsEnumEnum(Enum):
    """
    SlaProbeIntervalUnitsEnumEnum

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

    minutes = 4

    hours = 5

    day = 6

    week = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeIntervalUnitsEnumEnum']


class SlaSendEnum(Enum):
    """
    SlaSendEnum

    Sla send

    .. data:: packet = 0

    	Send individual packets

    .. data:: burst = 1

    	Send bursts of packets

    """

    packet = 0

    burst = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaSendEnum']


class SlaStatisticTypeEnumEnum(Enum):
    """
    SlaStatisticTypeEnumEnum

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

    round_trip_delay = 1

    one_way_delay_sd = 2

    one_way_delay_ds = 3

    round_trip_jitter = 4

    one_way_jitter_sd = 5

    one_way_jitter_ds = 6

    one_way_loss_sd = 7

    one_way_loss_ds = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaStatisticTypeEnumEnum']



