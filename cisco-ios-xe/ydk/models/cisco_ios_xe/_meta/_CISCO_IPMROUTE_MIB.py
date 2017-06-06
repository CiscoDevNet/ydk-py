


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpmrouteMib.Ciscoipmroute' : {
        'meta_info' : _MetaInfoClass('CiscoIpmrouteMib.Ciscoipmroute',
            False, 
            [
            _MetaInfoClassMember('ciscoIpMRouteNumberOfEntries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maintains a count of the number of entries in the
                ipMRouteTable.
                ''',
                'ciscoipmroutenumberofentries',
                'CISCO-IPMROUTE-MIB', False),
            ],
            'CISCO-IPMROUTE-MIB',
            'ciscoIpMRoute',
            _yang_ns._namespaces['CISCO-IPMROUTE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB'
        ),
    },
    'CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry',
            False, 
            [
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatGroupAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Multicast group address used to receive heartbeat
                packets.
                ''',
                'ciscoipmrouteheartbeatgroupaddr',
                'CISCO-IPMROUTE-MIB', True),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatAlertTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which a missing IP multicast heartbeat condition occured
                for the group address specified in this entry.  If no such
                condition have occurred since the last re-initialization
                of the local management subsystem, then this object
                contains a zero value.
                ''',
                'ciscoipmrouteheartbeatalerttime',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of time intervals where multicast packets were
                received in the last ciscoIpMRouteHeartBeatWindowSize
                intervals.
                ''',
                'ciscoipmrouteheartbeatcount',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatInterval', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Number of seconds in which a Cisco multicast router
                expects a valid heartBeat packet from a source.  This
                value must be a multiple of 10.
                ''',
                'ciscoipmrouteheartbeatinterval',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatMinimum', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The minimal number of heartbeat packets expected in the
                last ciscoIpMRouteHeartBeatWindowSize intervals. If
                ciscoIpMRouteHeartBeatCount falls below this value, an
                SNMP trap/notification, if configured, will be sent to the
                NMS.
                ''',
                'ciscoipmrouteheartbeatminimum',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatSourceAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address of the last multicast heartbeat packet
                received.
                ''',
                'ciscoipmrouteheartbeatsourceaddr',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create a new row or delete an
                existing row in this table.
                ''',
                'ciscoipmrouteheartbeatstatus',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatWindowSize', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Number of ciscoIpMRouteHeartBeatInterval intervals a
                Cisco multicast router waits before checking if expected
                number of heartbeat packets are received or not.
                ''',
                'ciscoipmrouteheartbeatwindowsize',
                'CISCO-IPMROUTE-MIB', False),
            ],
            'CISCO-IPMROUTE-MIB',
            'ciscoIpMRouteHeartBeatEntry',
            _yang_ns._namespaces['CISCO-IPMROUTE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB'
        ),
    },
    'CiscoIpmrouteMib.Ciscoipmrouteheartbeattable' : {
        'meta_info' : _MetaInfoClass('CiscoIpmrouteMib.Ciscoipmrouteheartbeattable',
            False, 
            [
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatEntry', REFERENCE_LIST, 'Ciscoipmrouteheartbeatentry' , 'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB', 'CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry', 
                [], [], 
                '''                An entry (conceptual row) representing a set of IP
                Multicast heartbeat parameters.
                ''',
                'ciscoipmrouteheartbeatentry',
                'CISCO-IPMROUTE-MIB', False),
            ],
            'CISCO-IPMROUTE-MIB',
            'ciscoIpMRouteHeartBeatTable',
            _yang_ns._namespaces['CISCO-IPMROUTE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB'
        ),
    },
    'CiscoIpmrouteMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpmrouteMib',
            False, 
            [
            _MetaInfoClassMember('ciscoIpMRoute', REFERENCE_CLASS, 'Ciscoipmroute' , 'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB', 'CiscoIpmrouteMib.Ciscoipmroute', 
                [], [], 
                '''                ''',
                'ciscoipmroute',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteHeartBeatTable', REFERENCE_CLASS, 'Ciscoipmrouteheartbeattable' , 'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB', 'CiscoIpmrouteMib.Ciscoipmrouteheartbeattable', 
                [], [], 
                '''                The (conceptual) table listing sets of IP Multicast
                heartbeat parameters.  If no IP Multicast heartbeat is
                configured, this table would be empty.
                ''',
                'ciscoipmrouteheartbeattable',
                'CISCO-IPMROUTE-MIB', False),
            ],
            'CISCO-IPMROUTE-MIB',
            'CISCO-IPMROUTE-MIB',
            _yang_ns._namespaces['CISCO-IPMROUTE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB'
        ),
    },
}
_meta_table['CiscoIpmrouteMib.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry']['meta_info'].parent =_meta_table['CiscoIpmrouteMib.Ciscoipmrouteheartbeattable']['meta_info']
_meta_table['CiscoIpmrouteMib.Ciscoipmroute']['meta_info'].parent =_meta_table['CiscoIpmrouteMib']['meta_info']
_meta_table['CiscoIpmrouteMib.Ciscoipmrouteheartbeattable']['meta_info'].parent =_meta_table['CiscoIpmrouteMib']['meta_info']
