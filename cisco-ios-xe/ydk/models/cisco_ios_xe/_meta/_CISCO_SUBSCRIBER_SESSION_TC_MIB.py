


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SubsessiontypeEnum' : _MetaInfoEnum('SubsessiontypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB',
        {
            'all':'all',
            'other':'other',
            'pppSubscriber':'pppSubscriber',
            'pppoeSubscriber':'pppoeSubscriber',
            'l2tpSubscriber':'l2tpSubscriber',
            'l2fSubscriber':'l2fSubscriber',
            'ipInterfaceSubscriber':'ipInterfaceSubscriber',
            'ipPktSubscriber':'ipPktSubscriber',
            'ipDhcpv4Subscriber':'ipDhcpv4Subscriber',
            'ipRadiusSubscriber':'ipRadiusSubscriber',
            'l2MacSubscriber':'l2MacSubscriber',
            'l2Dhcpv4Subscriber':'l2Dhcpv4Subscriber',
            'l2RadiusSubscriber':'l2RadiusSubscriber',
        }, 'CISCO-SUBSCRIBER-SESSION-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-TC-MIB']),
    'SubsessionstateEnum' : _MetaInfoEnum('SubsessionstateEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB',
        {
            'other':'other',
            'pending':'pending',
            'up':'up',
        }, 'CISCO-SUBSCRIBER-SESSION-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-TC-MIB']),
    'SubsessionredundancymodeEnum' : _MetaInfoEnum('SubsessionredundancymodeEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB',
        {
            'none':'none',
            'other':'other',
            'active':'active',
            'standby':'standby',
        }, 'CISCO-SUBSCRIBER-SESSION-TC-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-TC-MIB']),
}
