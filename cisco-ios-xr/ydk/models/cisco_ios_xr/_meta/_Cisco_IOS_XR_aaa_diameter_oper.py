


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DisconnectCauseEnum' : _MetaInfoEnum('DisconnectCauseEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper',
        {
            'reboot':'reboot',
            'busy':'busy',
            'do-not-wait-to-talk':'do_not_wait_to_talk',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper']),
    'PeerEnum' : _MetaInfoEnum('PeerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper',
        {
            'undefined':'undefined',
            'server':'server',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper']),
    'PeerStateValueEnum' : _MetaInfoEnum('PeerStateValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper',
        {
            'state-none':'state_none',
            'closed':'closed',
            'wait-connection-ack':'wait_connection_ack',
            'wait-cea':'wait_cea',
            'state-open':'state_open',
            'closing':'closing',
            'suspect':'suspect',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper']),
    'WhoInitiatedDisconnectEnum' : _MetaInfoEnum('WhoInitiatedDisconnectEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper',
        {
            'none':'none',
            'host':'host',
            'peer':'peer',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper']),
    'ProtocolTypeValueEnum' : _MetaInfoEnum('ProtocolTypeValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper',
        {
            'protocol-none':'protocol_none',
            'tcp':'tcp',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper']),
    'SecurityTypeValueEnum' : _MetaInfoEnum('SecurityTypeValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper',
        {
            'security-type-none':'security_type_none',
            'type':'type',
            'ipsec':'ipsec',
        }, 'Cisco-IOS-XR-aaa-diameter-oper', _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper']),
}
