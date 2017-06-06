


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SubscribermediatypeEnum' : _MetaInfoEnum('SubscribermediatypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB',
        {
            'other':'other',
            'async':'async',
            'atm':'atm',
            'ethernet':'ethernet',
            'ip':'ip',
            'isdn':'isdn',
            'mpls':'mpls',
            'sync':'sync',
        }, 'CISCO-SUBSCRIBER-IDENTITY-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-IDENTITY-TC-MIB']),
    'SubscriberprotocoltypeEnum' : _MetaInfoEnum('SubscriberprotocoltypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB',
        {
            'other':'other',
            'atom':'atom',
            'ip':'ip',
            'psdn':'psdn',
            'ppp':'ppp',
            'vpdn':'vpdn',
        }, 'CISCO-SUBSCRIBER-IDENTITY-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-IDENTITY-TC-MIB']),
    'SubsessionidentityEnum' : _MetaInfoEnum('SubsessionidentityEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB',
        {
            'other':'other',
            'ifIndex':'ifIndex',
            'subscriberLabel':'subscriberLabel',
            'macAddress':'macAddress',
            'nativeVrf':'nativeVrf',
            'nativeIpAddress':'nativeIpAddress',
            'domainVrf':'domainVrf',
            'domainIpAddress':'domainIpAddress',
            'pbhk':'pbhk',
            'remoteId':'remoteId',
            'circuitId':'circuitId',
            'nasPort':'nasPort',
            'domain':'domain',
            'username':'username',
            'acctSessionId':'acctSessionId',
            'dnis':'dnis',
            'media':'media',
            'mlpNegotiated':'mlpNegotiated',
            'protocol':'protocol',
            'serviceName':'serviceName',
            'dhcpClass':'dhcpClass',
            'tunnelName':'tunnelName',
        }, 'CISCO-SUBSCRIBER-IDENTITY-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-IDENTITY-TC-MIB']),
}
