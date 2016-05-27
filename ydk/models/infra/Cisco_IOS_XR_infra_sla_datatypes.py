""" Cisco_IOS_XR_infra_sla_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SlaBucketsSizeUnitsEnumEnum(Enum):
    """
    SlaBucketsSizeUnitsEnumEnum

    Sla buckets size units enum

    .. data:: BUCKETS_PER_PROBE = 0

    	Store results as a number of buckets per probe

    	- note that this option has been DEPRECATED

    .. data:: PROBES_PER_BUCKET = 1

    	Store results as a number of probes per bucket

    """

    BUCKETS_PER_PROBE = 0

    PROBES_PER_BUCKET = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaBucketsSizeUnitsEnumEnum']


class SlaBurstIntervalUnitsEnumEnum(Enum):
    """
    SlaBurstIntervalUnitsEnumEnum

    Sla burst interval units enum

    .. data:: ONCE = 1

    	Send one burst per probe

    .. data:: SECONDS = 3

    	Send bursts within a probe with an interval

    	unit of seconds

    .. data:: MINUTES = 4

    	Send bursts within a probe with an interval

    	unit of minutes

    .. data:: HOURS = 5

    	Send bursts within a probe with an interval

    	unit of hours

    """

    ONCE = 1

    SECONDS = 3

    MINUTES = 4

    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaBurstIntervalUnitsEnumEnum']


class SlaOnDemandProbeDurationUnitsEnumEnum(Enum):
    """
    SlaOnDemandProbeDurationUnitsEnumEnum

    Sla on demand probe duration units enum

    .. data:: SECONDS = 3

    	Schedule probes to run with a duration unit of

    	seconds

    .. data:: MINUTES = 4

    	Schedule probes to run with a duration unit of

    	minutes

    .. data:: HOURS = 5

    	Schedule probes to run with a duration unit of

    	hours

    """

    SECONDS = 3

    MINUTES = 4

    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandProbeDurationUnitsEnumEnum']


class SlaOnDemandRepeatIntervalUnitsEnumEnum(Enum):
    """
    SlaOnDemandRepeatIntervalUnitsEnumEnum

    Sla on demand repeat interval units enum

    .. data:: SECONDS = 3

    	Schedule probes to repeat with an interval unit

    	of seconds

    .. data:: MINUTES = 4

    	Schedule probes to repeat with an interval unit

    	of minutes

    .. data:: HOURS = 5

    	Schedule probes to repeat with an interval unit

    	of hours

    """

    SECONDS = 3

    MINUTES = 4

    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandRepeatIntervalUnitsEnumEnum']


class SlaOnDemandStartMonthEnumEnum(Enum):
    """
    SlaOnDemandStartMonthEnumEnum

    Sla on demand start month enum

    .. data:: JANUARY = 0

    	January

    .. data:: FEBRUARY = 1

    	February

    .. data:: MARCH = 2

    	March

    .. data:: APRIL = 3

    	April

    .. data:: MAY = 4

    	May

    .. data:: JUNE = 5

    	June

    .. data:: JULY = 6

    	July

    .. data:: AUGUST = 7

    	August

    .. data:: SEPTEMBER = 8

    	September

    .. data:: OCTOBER = 9

    	October

    .. data:: NOVEMBER = 10

    	November

    .. data:: DECEMBER = 11

    	December

    """

    JANUARY = 0

    FEBRUARY = 1

    MARCH = 2

    APRIL = 3

    MAY = 4

    JUNE = 5

    JULY = 6

    AUGUST = 7

    SEPTEMBER = 8

    OCTOBER = 9

    NOVEMBER = 10

    DECEMBER = 11


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartMonthEnumEnum']


class SlaOnDemandStartTimeRelativeUnitsEnumEnum(Enum):
    """
    SlaOnDemandStartTimeRelativeUnitsEnumEnum

    Sla on demand start time relative units enum

    .. data:: SECONDS = 3

    	Schedule probe to start after a unit of seconds

    .. data:: MINUTES = 4

    	Schedule probe to start after a unit of minutes

    .. data:: HOURS = 5

    	Schedule probe to start after a unit of hours

    """

    SECONDS = 3

    MINUTES = 4

    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartTimeRelativeUnitsEnumEnum']


class SlaOnDemandStartTimeTypesEnumEnum(Enum):
    """
    SlaOnDemandStartTimeTypesEnumEnum

    Sla on demand start time types enum

    .. data:: NOW = 0

    	Start immediately

    .. data:: ABSOLUTE = 1

    	Start at a specified time

    .. data:: RELATIVE = 2

    	Start after a specified period

    """

    NOW = 0

    ABSOLUTE = 1

    RELATIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaOnDemandStartTimeTypesEnumEnum']


class SlaPacketIntervalUnitsEnumEnum(Enum):
    """
    SlaPacketIntervalUnitsEnumEnum

    Sla packet interval units enum

    .. data:: ONCE = 1

    	Send one packet per burst

    .. data:: MILLISECONDS = 2

    	Send packets with an interval unit of

    	milliseconds

    .. data:: SECONDS = 3

    	Send packets with an interval unit of seconds

    .. data:: MINUTES = 4

    	Send packets with an interval unit of minutes

    .. data:: HOURS = 5

    	Send packets with an interval unit of hours

    """

    ONCE = 1

    MILLISECONDS = 2

    SECONDS = 3

    MINUTES = 4

    HOURS = 5


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaPacketIntervalUnitsEnumEnum']


class SlaPaddingPatternEnum(Enum):
    """
    SlaPaddingPatternEnum

    Sla padding pattern

    .. data:: HEX = 0

    	Use an optionally specified hex pattern for

    	packet padding

    .. data:: PSEUDO_RANDOM = 1

    	Use a pseudo-random bit sequence for packet

    	padding

    """

    HEX = 0

    PSEUDO_RANDOM = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaPaddingPatternEnum']


class SlaProbeDurationUnitsEnumEnum(Enum):
    """
    SlaProbeDurationUnitsEnumEnum

    Sla probe duration units enum

    .. data:: SECONDS = 3

    	Schedule probes to run with a duration unit of

    	seconds

    .. data:: MINUTES = 4

    	Schedule probes to run with a duration unit of

    	minutes

    .. data:: HOURS = 5

    	Schedule probes to run with a duration unit of

    	hours

    .. data:: DAY = 6

    	Schedule probes to run for a duration of 1 day

    .. data:: WEEK = 7

    	Schedule probes to run for a duration of 1 week

    """

    SECONDS = 3

    MINUTES = 4

    HOURS = 5

    DAY = 6

    WEEK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeDurationUnitsEnumEnum']


class SlaProbeIntervalDayEnumEnum(Enum):
    """
    SlaProbeIntervalDayEnumEnum

    Sla probe interval day enum

    .. data:: MONDAY = 1

    	Schedule every Monday

    .. data:: TUESDAY = 2

    	Schedule every Tuesday

    .. data:: WEDNESDAY = 3

    	Schedule every Wednesday

    .. data:: THURSDAY = 4

    	Schedule every Thursday

    .. data:: FRIDAY = 5

    	Schedule every Friday

    .. data:: SATURDAY = 6

    	Schedule every Saturday

    .. data:: SUNDAY = 7

    	Schedule every Sunday

    """

    MONDAY = 1

    TUESDAY = 2

    WEDNESDAY = 3

    THURSDAY = 4

    FRIDAY = 5

    SATURDAY = 6

    SUNDAY = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeIntervalDayEnumEnum']


class SlaProbeIntervalUnitsEnumEnum(Enum):
    """
    SlaProbeIntervalUnitsEnumEnum

    Sla probe interval units enum

    .. data:: MINUTES = 4

    	Schedule probes to run with an interval unit of

    	minutes

    .. data:: HOURS = 5

    	Schedule probes to run with an interval unit of

    	hours

    .. data:: DAY = 6

    	Schedule probes to run every day

    .. data:: WEEK = 7

    	Schedule probes to run every week

    """

    MINUTES = 4

    HOURS = 5

    DAY = 6

    WEEK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaProbeIntervalUnitsEnumEnum']


class SlaSendEnum(Enum):
    """
    SlaSendEnum

    Sla send

    .. data:: PACKET = 0

    	Send individual packets

    .. data:: BURST = 1

    	Send bursts of packets

    """

    PACKET = 0

    BURST = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaSendEnum']


class SlaStatisticTypeEnumEnum(Enum):
    """
    SlaStatisticTypeEnumEnum

    Sla statistic type enum

    .. data:: ROUND_TRIP_DELAY = 1

    	Collect round trip delay metric data

    .. data:: ONE_WAY_DELAY_SD = 2

    	Collect one way delay source->dest metric data

    .. data:: ONE_WAY_DELAY_DS = 3

    	Collect one way delay dest->source metric data

    .. data:: ROUND_TRIP_JITTER = 4

    	Collect round trip delay metric data

    .. data:: ONE_WAY_JITTER_SD = 5

    	Collect one way jitter source->dest metric data

    .. data:: ONE_WAY_JITTER_DS = 6

    	Collect one way jitter dest->source metric data

    .. data:: ONE_WAY_LOSS_SD = 7

    	Collect one way loss source->dest metric data

    .. data:: ONE_WAY_LOSS_DS = 8

    	Collect one way loss dest->source metric data

    """

    ROUND_TRIP_DELAY = 1

    ONE_WAY_DELAY_SD = 2

    ONE_WAY_DELAY_DS = 3

    ROUND_TRIP_JITTER = 4

    ONE_WAY_JITTER_SD = 5

    ONE_WAY_JITTER_DS = 6

    ONE_WAY_LOSS_SD = 7

    ONE_WAY_LOSS_DS = 8


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_sla_datatypes as meta
        return meta._meta_table['SlaStatisticTypeEnumEnum']



