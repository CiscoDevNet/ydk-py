


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpslareactvarEnum' : _MetaInfoEnum('IpslareactvarEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB',
        {
            'rtt':'rtt',
            'jitterSDAvg':'jitterSDAvg',
            'jitterDSAvg':'jitterDSAvg',
            'packetLossSD':'packetLossSD',
            'packetLossDS':'packetLossDS',
            'mos':'mos',
            'timeout':'timeout',
            'connectionLoss':'connectionLoss',
            'verifyError':'verifyError',
            'jitterAvg':'jitterAvg',
            'icpif':'icpif',
            'packetMIA':'packetMIA',
            'packetLateArrival':'packetLateArrival',
            'packetOutOfSequence':'packetOutOfSequence',
            'maxOfPositiveSD':'maxOfPositiveSD',
            'maxOfNegativeSD':'maxOfNegativeSD',
            'maxOfPositiveDS':'maxOfPositiveDS',
            'maxOfNegativeDS':'maxOfNegativeDS',
            'successivePacketLoss':'successivePacketLoss',
            'maxOfLatencyDS':'maxOfLatencyDS',
            'maxOfLatencySD':'maxOfLatencySD',
            'latencyDSAvg':'latencyDSAvg',
            'latencySDAvg':'latencySDAvg',
            'packetLoss':'packetLoss',
        }, 'CISCO-IPSLA-TC-MIB', _yang_ns._namespaces['CISCO-IPSLA-TC-MIB']),
    'IpslaopertypeEnum' : _MetaInfoEnum('IpslaopertypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB',
        {
            'icmpEcho':'icmpEcho',
            'udpEcho':'udpEcho',
            'tcpConnect':'tcpConnect',
            'udpJitter':'udpJitter',
            'icmpJitter':'icmpJitter',
        }, 'CISCO-IPSLA-TC-MIB', _yang_ns._namespaces['CISCO-IPSLA-TC-MIB']),
    'IpslacodectypeEnum' : _MetaInfoEnum('IpslacodectypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB',
        {
            'notApplicable':'notApplicable',
            'g711ulaw':'g711ulaw',
            'g711alaw':'g711alaw',
            'g729a':'g729a',
        }, 'CISCO-IPSLA-TC-MIB', _yang_ns._namespaces['CISCO-IPSLA-TC-MIB']),
}
