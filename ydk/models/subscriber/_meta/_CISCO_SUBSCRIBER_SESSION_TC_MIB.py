


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SubSessionType_Enum' : _MetaInfoEnum('SubSessionType_Enum', 'ydk.models.subscriber.CISCO_SUBSCRIBER_SESSION_TC_MIB',
        {
            'all':'ALL',
            'other':'OTHER',
            'pppSubscriber':'PPPSUBSCRIBER',
            'pppoeSubscriber':'PPPOESUBSCRIBER',
            'l2tpSubscriber':'L2TPSUBSCRIBER',
            'l2fSubscriber':'L2FSUBSCRIBER',
            'ipInterfaceSubscriber':'IPINTERFACESUBSCRIBER',
            'ipPktSubscriber':'IPPKTSUBSCRIBER',
            'ipDhcpv4Subscriber':'IPDHCPV4SUBSCRIBER',
            'ipRadiusSubscriber':'IPRADIUSSUBSCRIBER',
            'l2MacSubscriber':'L2MACSUBSCRIBER',
            'l2Dhcpv4Subscriber':'L2DHCPV4SUBSCRIBER',
            'l2RadiusSubscriber':'L2RADIUSSUBSCRIBER',
        }, 'CISCO-SUBSCRIBER-SESSION-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-TC-MIB']),
    'SubSessionRedundancyMode_Enum' : _MetaInfoEnum('SubSessionRedundancyMode_Enum', 'ydk.models.subscriber.CISCO_SUBSCRIBER_SESSION_TC_MIB',
        {
            'none':'NONE',
            'other':'OTHER',
            'active':'ACTIVE',
            'standby':'STANDBY',
        }, 'CISCO-SUBSCRIBER-SESSION-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-TC-MIB']),
    'SubSessionState_Enum' : _MetaInfoEnum('SubSessionState_Enum', 'ydk.models.subscriber.CISCO_SUBSCRIBER_SESSION_TC_MIB',
        {
            'other':'OTHER',
            'pending':'PENDING',
            'up':'UP',
        }, 'CISCO-SUBSCRIBER-SESSION-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-TC-MIB']),
}
