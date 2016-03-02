


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SubscriberMediaType_Enum' : _MetaInfoEnum('SubscriberMediaType_Enum', 'ydk.models.subscriber.CISCO_SUBSCRIBER_IDENTITY_TC_MIB',
        {
            'other':'OTHER',
            'async':'ASYNC',
            'atm':'ATM',
            'ethernet':'ETHERNET',
            'ip':'IP',
            'isdn':'ISDN',
            'mpls':'MPLS',
            'sync':'SYNC',
        }, 'CISCO-SUBSCRIBER-IDENTITY-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-IDENTITY-TC-MIB']),
    'SubscriberProtocolType_Enum' : _MetaInfoEnum('SubscriberProtocolType_Enum', 'ydk.models.subscriber.CISCO_SUBSCRIBER_IDENTITY_TC_MIB',
        {
            'other':'OTHER',
            'atom':'ATOM',
            'ip':'IP',
            'psdn':'PSDN',
            'ppp':'PPP',
            'vpdn':'VPDN',
        }, 'CISCO-SUBSCRIBER-IDENTITY-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-IDENTITY-TC-MIB']),
    'SubSessionIdentity_Enum' : _MetaInfoEnum('SubSessionIdentity_Enum', 'ydk.models.subscriber.CISCO_SUBSCRIBER_IDENTITY_TC_MIB',
        {
            'other':'OTHER',
            'ifIndex':'IFINDEX',
            'subscriberLabel':'SUBSCRIBERLABEL',
            'macAddress':'MACADDRESS',
            'nativeVrf':'NATIVEVRF',
            'nativeIpAddress':'NATIVEIPADDRESS',
            'domainVrf':'DOMAINVRF',
            'domainIpAddress':'DOMAINIPADDRESS',
            'pbhk':'PBHK',
            'remoteId':'REMOTEID',
            'circuitId':'CIRCUITID',
            'nasPort':'NASPORT',
            'domain':'DOMAIN',
            'username':'USERNAME',
            'acctSessionId':'ACCTSESSIONID',
            'dnis':'DNIS',
            'media':'MEDIA',
            'mlpNegotiated':'MLPNEGOTIATED',
            'protocol':'PROTOCOL',
            'serviceName':'SERVICENAME',
            'dhcpClass':'DHCPCLASS',
            'tunnelName':'TUNNELNAME',
        }, 'CISCO-SUBSCRIBER-IDENTITY-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-IDENTITY-TC-MIB']),
}
