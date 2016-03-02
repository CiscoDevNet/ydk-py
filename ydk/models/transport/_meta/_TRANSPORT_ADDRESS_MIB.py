


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TransportAddressType_Enum' : _MetaInfoEnum('TransportAddressType_Enum', 'ydk.models.transport.TRANSPORT_ADDRESS_MIB',
        {
            'unknown':'UNKNOWN',
            'udpIpv4':'UDPIPV4',
            'udpIpv6':'UDPIPV6',
            'udpIpv4z':'UDPIPV4Z',
            'udpIpv6z':'UDPIPV6Z',
            'tcpIpv4':'TCPIPV4',
            'tcpIpv6':'TCPIPV6',
            'tcpIpv4z':'TCPIPV4Z',
            'tcpIpv6z':'TCPIPV6Z',
            'sctpIpv4':'SCTPIPV4',
            'sctpIpv6':'SCTPIPV6',
            'sctpIpv4z':'SCTPIPV4Z',
            'sctpIpv6z':'SCTPIPV6Z',
            'local':'LOCAL',
            'udpDns':'UDPDNS',
            'tcpDns':'TCPDNS',
            'sctpDns':'SCTPDNS',
        }, 'TRANSPORT-ADDRESS-MIB', _yang_ns._namespaces['TRANSPORT-ADDRESS-MIB']),
}
