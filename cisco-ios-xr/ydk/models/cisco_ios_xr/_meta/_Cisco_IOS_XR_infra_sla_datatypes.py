


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SlaBurstIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaBurstIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'once':'ONCE',
            'milliseconds':'MILLISECONDS',
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartTimeTypesEnumEnum' : _MetaInfoEnum('SlaOnDemandStartTimeTypesEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'now':'NOW',
            'absolute':'ABSOLUTE',
            'relative':'RELATIVE',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaPacketIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaPacketIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'once':'ONCE',
            'milliseconds':'MILLISECONDS',
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandProbeDurationUnitsEnumEnum' : _MetaInfoEnum('SlaOnDemandProbeDurationUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartMonthEnumEnum' : _MetaInfoEnum('SlaOnDemandStartMonthEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'january':'JANUARY',
            'february':'FEBRUARY',
            'march':'MARCH',
            'april':'APRIL',
            'may':'MAY',
            'june':'JUNE',
            'july':'JULY',
            'august':'AUGUST',
            'september':'SEPTEMBER',
            'october':'OCTOBER',
            'november':'NOVEMBER',
            'december':'DECEMBER',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandRepeatIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaOnDemandRepeatIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaBucketsSizeUnitsEnumEnum' : _MetaInfoEnum('SlaBucketsSizeUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'buckets-per-probe':'BUCKETS_PER_PROBE',
            'probes-per-bucket':'PROBES_PER_BUCKET',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaProbeIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'minutes':'MINUTES',
            'hours':'HOURS',
            'day':'DAY',
            'week':'WEEK',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeDurationUnitsEnumEnum' : _MetaInfoEnum('SlaProbeDurationUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
            'day':'DAY',
            'week':'WEEK',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeIntervalDayEnumEnum' : _MetaInfoEnum('SlaProbeIntervalDayEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'monday':'MONDAY',
            'tuesday':'TUESDAY',
            'wednesday':'WEDNESDAY',
            'thursday':'THURSDAY',
            'friday':'FRIDAY',
            'saturday':'SATURDAY',
            'sunday':'SUNDAY',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartTimeRelativeUnitsEnumEnum' : _MetaInfoEnum('SlaOnDemandStartTimeRelativeUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaStatisticTypeEnumEnum' : _MetaInfoEnum('SlaStatisticTypeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'round-trip-delay':'ROUND_TRIP_DELAY',
            'one-way-delay-sd':'ONE_WAY_DELAY_SD',
            'one-way-delay-ds':'ONE_WAY_DELAY_DS',
            'round-trip-jitter':'ROUND_TRIP_JITTER',
            'one-way-jitter-sd':'ONE_WAY_JITTER_SD',
            'one-way-jitter-ds':'ONE_WAY_JITTER_DS',
            'one-way-loss-sd':'ONE_WAY_LOSS_SD',
            'one-way-loss-ds':'ONE_WAY_LOSS_DS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaPaddingPatternEnum' : _MetaInfoEnum('SlaPaddingPatternEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'hex':'HEX',
            'pseudo-random':'PSEUDO_RANDOM',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaSendEnum' : _MetaInfoEnum('SlaSendEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'packet':'PACKET',
            'burst':'BURST',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
}
