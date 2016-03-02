""" Cisco_IOS_XR_infra_sla_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SlaBucketsSizeUnitsEnum_Enum(Enum):
    """
    SlaBucketsSizeUnitsEnum_Enum

    Sla buckets size units enum

    """

    """

    Store results as a number of buckets per probe
    \- note that this option has been DEPRECATED

    """
    BUCKETS_PER_PROBE = 0

    """

    Store results as a number of probes per bucket

    """
    PROBES_PER_BUCKET = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaBucketsSizeUnitsEnum_Enum']


class SlaBurstIntervalUnitsEnum_Enum(Enum):
    """
    SlaBurstIntervalUnitsEnum_Enum

    Sla burst interval units enum

    """

    """

    Send one burst per probe

    """
    ONCE = 1

    """

    Send bursts within a probe with an interval
    unit of seconds

    """
    SECONDS = 3

    """

    Send bursts within a probe with an interval
    unit of minutes

    """
    MINUTES = 4

    """

    Send bursts within a probe with an interval
    unit of hours

    """
    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaBurstIntervalUnitsEnum_Enum']


class SlaOnDemandProbeDurationUnitsEnum_Enum(Enum):
    """
    SlaOnDemandProbeDurationUnitsEnum_Enum

    Sla on demand probe duration units enum

    """

    """

    Schedule probes to run with a duration unit of
    seconds

    """
    SECONDS = 3

    """

    Schedule probes to run with a duration unit of
    minutes

    """
    MINUTES = 4

    """

    Schedule probes to run with a duration unit of
    hours

    """
    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandProbeDurationUnitsEnum_Enum']


class SlaOnDemandRepeatIntervalUnitsEnum_Enum(Enum):
    """
    SlaOnDemandRepeatIntervalUnitsEnum_Enum

    Sla on demand repeat interval units enum

    """

    """

    Schedule probes to repeat with an interval unit
    of seconds

    """
    SECONDS = 3

    """

    Schedule probes to repeat with an interval unit
    of minutes

    """
    MINUTES = 4

    """

    Schedule probes to repeat with an interval unit
    of hours

    """
    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandRepeatIntervalUnitsEnum_Enum']


class SlaOnDemandStartMonthEnum_Enum(Enum):
    """
    SlaOnDemandStartMonthEnum_Enum

    Sla on demand start month enum

    """

    """

    January

    """
    JANUARY = 0

    """

    February

    """
    FEBRUARY = 1

    """

    March

    """
    MARCH = 2

    """

    April

    """
    APRIL = 3

    """

    May

    """
    MAY = 4

    """

    June

    """
    JUNE = 5

    """

    July

    """
    JULY = 6

    """

    August

    """
    AUGUST = 7

    """

    September

    """
    SEPTEMBER = 8

    """

    October

    """
    OCTOBER = 9

    """

    November

    """
    NOVEMBER = 10

    """

    December

    """
    DECEMBER = 11


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartMonthEnum_Enum']


class SlaOnDemandStartTimeRelativeUnitsEnum_Enum(Enum):
    """
    SlaOnDemandStartTimeRelativeUnitsEnum_Enum

    Sla on demand start time relative units enum

    """

    """

    Schedule probe to start after a unit of seconds

    """
    SECONDS = 3

    """

    Schedule probe to start after a unit of minutes

    """
    MINUTES = 4

    """

    Schedule probe to start after a unit of hours

    """
    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartTimeRelativeUnitsEnum_Enum']


class SlaOnDemandStartTimeTypesEnum_Enum(Enum):
    """
    SlaOnDemandStartTimeTypesEnum_Enum

    Sla on demand start time types enum

    """

    """

    Start immediately

    """
    NOW = 0

    """

    Start at a specified time

    """
    ABSOLUTE = 1

    """

    Start after a specified period

    """
    RELATIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartTimeTypesEnum_Enum']


class SlaPacketIntervalUnitsEnum_Enum(Enum):
    """
    SlaPacketIntervalUnitsEnum_Enum

    Sla packet interval units enum

    """

    """

    Send one packet per burst

    """
    ONCE = 1

    """

    Send packets with an interval unit of
    milliseconds

    """
    MILLISECONDS = 2

    """

    Send packets with an interval unit of seconds

    """
    SECONDS = 3

    """

    Send packets with an interval unit of minutes

    """
    MINUTES = 4

    """

    Send packets with an interval unit of hours

    """
    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaPacketIntervalUnitsEnum_Enum']


class SlaPaddingPattern_Enum(Enum):
    """
    SlaPaddingPattern_Enum

    Sla padding pattern

    """

    """

    Use an optionally specified hex pattern for
    packet padding

    """
    HEX = 0

    """

    Use a pseudo\-random bit sequence for packet
    padding

    """
    PSEUDO_RANDOM = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaPaddingPattern_Enum']


class SlaProbeDurationUnitsEnum_Enum(Enum):
    """
    SlaProbeDurationUnitsEnum_Enum

    Sla probe duration units enum

    """

    """

    Schedule probes to run with a duration unit of
    seconds

    """
    SECONDS = 3

    """

    Schedule probes to run with a duration unit of
    minutes

    """
    MINUTES = 4

    """

    Schedule probes to run with a duration unit of
    hours

    """
    HOURS = 5

    """

    Schedule probes to run for a duration of 1 day

    """
    DAY = 6

    """

    Schedule probes to run for a duration of 1 week

    """
    WEEK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeDurationUnitsEnum_Enum']


class SlaProbeIntervalDayEnum_Enum(Enum):
    """
    SlaProbeIntervalDayEnum_Enum

    Sla probe interval day enum

    """

    """

    Schedule every Monday

    """
    MONDAY = 1

    """

    Schedule every Tuesday

    """
    TUESDAY = 2

    """

    Schedule every Wednesday

    """
    WEDNESDAY = 3

    """

    Schedule every Thursday

    """
    THURSDAY = 4

    """

    Schedule every Friday

    """
    FRIDAY = 5

    """

    Schedule every Saturday

    """
    SATURDAY = 6

    """

    Schedule every Sunday

    """
    SUNDAY = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeIntervalDayEnum_Enum']


class SlaProbeIntervalUnitsEnum_Enum(Enum):
    """
    SlaProbeIntervalUnitsEnum_Enum

    Sla probe interval units enum

    """

    """

    Schedule probes to run with an interval unit of
    minutes

    """
    MINUTES = 4

    """

    Schedule probes to run with an interval unit of
    hours

    """
    HOURS = 5

    """

    Schedule probes to run every day

    """
    DAY = 6

    """

    Schedule probes to run every week

    """
    WEEK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeIntervalUnitsEnum_Enum']


class SlaSend_Enum(Enum):
    """
    SlaSend_Enum

    Sla send

    """

    """

    Send individual packets

    """
    PACKET = 0

    """

    Send bursts of packets

    """
    BURST = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaSend_Enum']


class SlaStatisticTypeEnum_Enum(Enum):
    """
    SlaStatisticTypeEnum_Enum

    Sla statistic type enum

    """

    """

    Collect round trip delay metric data

    """
    ROUND_TRIP_DELAY = 1

    """

    Collect one way delay source\->dest metric data

    """
    ONE_WAY_DELAY_SD = 2

    """

    Collect one way delay dest\->source metric data

    """
    ONE_WAY_DELAY_DS = 3

    """

    Collect round trip delay metric data

    """
    ROUND_TRIP_JITTER = 4

    """

    Collect one way jitter source\->dest metric data

    """
    ONE_WAY_JITTER_SD = 5

    """

    Collect one way jitter dest\->source metric data

    """
    ONE_WAY_JITTER_DS = 6

    """

    Collect one way loss source\->dest metric data

    """
    ONE_WAY_LOSS_SD = 7

    """

    Collect one way loss dest\->source metric data

    """
    ONE_WAY_LOSS_DS = 8


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaStatisticTypeEnum_Enum']



