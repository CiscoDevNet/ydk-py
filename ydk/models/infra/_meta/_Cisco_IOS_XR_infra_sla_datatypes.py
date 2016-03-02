


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SlaBurstIntervalUnitsEnum_Enum' : _MetaInfoEnum('SlaBurstIntervalUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'once':'ONCE',
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartTimeTypesEnum_Enum' : _MetaInfoEnum('SlaOnDemandStartTimeTypesEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'now':'NOW',
            'absolute':'ABSOLUTE',
            'relative':'RELATIVE',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaPacketIntervalUnitsEnum_Enum' : _MetaInfoEnum('SlaPacketIntervalUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'once':'ONCE',
            'milliseconds':'MILLISECONDS',
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandProbeDurationUnitsEnum_Enum' : _MetaInfoEnum('SlaOnDemandProbeDurationUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartMonthEnum_Enum' : _MetaInfoEnum('SlaOnDemandStartMonthEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
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
    'SlaOnDemandRepeatIntervalUnitsEnum_Enum' : _MetaInfoEnum('SlaOnDemandRepeatIntervalUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaBucketsSizeUnitsEnum_Enum' : _MetaInfoEnum('SlaBucketsSizeUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'buckets-per-probe':'BUCKETS_PER_PROBE',
            'probes-per-bucket':'PROBES_PER_BUCKET',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeIntervalUnitsEnum_Enum' : _MetaInfoEnum('SlaProbeIntervalUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'minutes':'MINUTES',
            'hours':'HOURS',
            'day':'DAY',
            'week':'WEEK',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeDurationUnitsEnum_Enum' : _MetaInfoEnum('SlaProbeDurationUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
            'day':'DAY',
            'week':'WEEK',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeIntervalDayEnum_Enum' : _MetaInfoEnum('SlaProbeIntervalDayEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'monday':'MONDAY',
            'tuesday':'TUESDAY',
            'wednesday':'WEDNESDAY',
            'thursday':'THURSDAY',
            'friday':'FRIDAY',
            'saturday':'SATURDAY',
            'sunday':'SUNDAY',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartTimeRelativeUnitsEnum_Enum' : _MetaInfoEnum('SlaOnDemandStartTimeRelativeUnitsEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'SECONDS',
            'minutes':'MINUTES',
            'hours':'HOURS',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaStatisticTypeEnum_Enum' : _MetaInfoEnum('SlaStatisticTypeEnum_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
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
    'SlaPaddingPattern_Enum' : _MetaInfoEnum('SlaPaddingPattern_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'hex':'HEX',
            'pseudo-random':'PSEUDO_RANDOM',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaSend_Enum' : _MetaInfoEnum('SlaSend_Enum', 'ydk.models.infra.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'packet':'PACKET',
            'burst':'BURST',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
}
