


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SlaProbeIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaProbeIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'minutes':'minutes',
            'hours':'hours',
            'day':'day',
            'week':'week',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaPaddingPatternEnum' : _MetaInfoEnum('SlaPaddingPatternEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'hex':'hex',
            'pseudo-random':'pseudo_random',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaBucketsSizeUnitsEnumEnum' : _MetaInfoEnum('SlaBucketsSizeUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'buckets-per-probe':'buckets_per_probe',
            'probes-per-bucket':'probes_per_bucket',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeIntervalDayEnumEnum' : _MetaInfoEnum('SlaProbeIntervalDayEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'monday':'monday',
            'tuesday':'tuesday',
            'wednesday':'wednesday',
            'thursday':'thursday',
            'friday':'friday',
            'saturday':'saturday',
            'sunday':'sunday',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartTimeTypesEnumEnum' : _MetaInfoEnum('SlaOnDemandStartTimeTypesEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'now':'now',
            'absolute':'absolute',
            'relative':'relative',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartMonthEnumEnum' : _MetaInfoEnum('SlaOnDemandStartMonthEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'january':'january',
            'february':'february',
            'march':'march',
            'april':'april',
            'may':'may',
            'june':'june',
            'july':'july',
            'august':'august',
            'september':'september',
            'october':'october',
            'november':'november',
            'december':'december',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaStatisticTypeEnumEnum' : _MetaInfoEnum('SlaStatisticTypeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'round-trip-delay':'round_trip_delay',
            'one-way-delay-sd':'one_way_delay_sd',
            'one-way-delay-ds':'one_way_delay_ds',
            'round-trip-jitter':'round_trip_jitter',
            'one-way-jitter-sd':'one_way_jitter_sd',
            'one-way-jitter-ds':'one_way_jitter_ds',
            'one-way-loss-sd':'one_way_loss_sd',
            'one-way-loss-ds':'one_way_loss_ds',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaPacketIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaPacketIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'once':'once',
            'milliseconds':'milliseconds',
            'seconds':'seconds',
            'minutes':'minutes',
            'hours':'hours',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaBurstIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaBurstIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'once':'once',
            'milliseconds':'milliseconds',
            'seconds':'seconds',
            'minutes':'minutes',
            'hours':'hours',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandStartTimeRelativeUnitsEnumEnum' : _MetaInfoEnum('SlaOnDemandStartTimeRelativeUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'seconds',
            'minutes':'minutes',
            'hours':'hours',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandRepeatIntervalUnitsEnumEnum' : _MetaInfoEnum('SlaOnDemandRepeatIntervalUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'seconds',
            'minutes':'minutes',
            'hours':'hours',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaOnDemandProbeDurationUnitsEnumEnum' : _MetaInfoEnum('SlaOnDemandProbeDurationUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'seconds',
            'minutes':'minutes',
            'hours':'hours',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaSendEnum' : _MetaInfoEnum('SlaSendEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'packet':'packet',
            'burst':'burst',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
    'SlaProbeDurationUnitsEnumEnum' : _MetaInfoEnum('SlaProbeDurationUnitsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_sla_datatypes',
        {
            'seconds':'seconds',
            'minutes':'minutes',
            'hours':'hours',
            'day':'day',
            'week':'week',
        }, 'Cisco-IOS-XR-infra-sla-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-sla-datatypes']),
}
