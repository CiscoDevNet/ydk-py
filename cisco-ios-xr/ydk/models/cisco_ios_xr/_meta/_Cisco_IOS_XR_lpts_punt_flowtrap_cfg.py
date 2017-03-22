


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LptsPuntFlowtrapProtoIdEnum' : _MetaInfoEnum('LptsPuntFlowtrapProtoIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg',
        {
            'arp':'arp',
            'icmp':'icmp',
            'dhcp':'dhcp',
            'pppoe':'pppoe',
            'ppp':'ppp',
            'igmp':'igmp',
            'ipv4':'ipv4',
            'l2tp':'l2tp',
            'unclassified':'unclassified',
            'ospf':'ospf',
            'bgp':'bgp',
            'default':'default',
        }, 'Cisco-IOS-XR-lpts-punt-flowtrap-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lpts-punt-flowtrap-cfg']),
}
