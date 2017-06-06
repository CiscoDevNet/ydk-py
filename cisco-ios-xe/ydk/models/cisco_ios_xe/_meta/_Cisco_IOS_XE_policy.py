


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PolicePpsBpsTypeEnum' : _MetaInfoEnum('PolicePpsBpsTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_policy',
        {
            'pps':'pps',
            'bps':'bps',
        }, 'Cisco-IOS-XE-policy', _yang_ns._namespaces['Cisco-IOS-XE-policy']),
    'PrecedenceType2Enum' : _MetaInfoEnum('PrecedenceType2Enum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_policy',
        {
            'rsvp':'rsvp',
        }, 'Cisco-IOS-XE-policy', _yang_ns._namespaces['Cisco-IOS-XE-policy']),
    'ClassNameTypeEnum' : _MetaInfoEnum('ClassNameTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_policy',
        {
            'class-default':'class_default',
        }, 'Cisco-IOS-XE-policy', _yang_ns._namespaces['Cisco-IOS-XE-policy']),
    'PolicePacketsBytesTypeEnum' : _MetaInfoEnum('PolicePacketsBytesTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_policy',
        {
            'packets':'packets',
            'bytes':'bytes',
        }, 'Cisco-IOS-XE-policy', _yang_ns._namespaces['Cisco-IOS-XE-policy']),
    'PolicyActionTypeEnum' : _MetaInfoEnum('PolicyActionTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_policy',
        {
            'bandwidth':'bandwidth',
            'compression':'compression',
            'drop':'drop',
            'estimate':'estimate',
            'fair-queue':'fair_queue',
            'forward':'forward',
            'netflow-sampler':'netflow_sampler',
            'police':'police',
            'priority':'priority',
            'queue-limit':'queue_limit',
            'random-detect':'random_detect',
            'service-policy':'service_policy',
            'set':'set',
            'shape':'shape',
            'trust':'trust',
            'dbl':'dbl',
            'queue-buffers':'queue_buffers',
        }, 'Cisco-IOS-XE-policy', _yang_ns._namespaces['Cisco-IOS-XE-policy']),
}
