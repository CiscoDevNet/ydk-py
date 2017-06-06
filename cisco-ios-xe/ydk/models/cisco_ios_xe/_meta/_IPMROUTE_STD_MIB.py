


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpmrouteStdMib.Ipmroute.IpmrouteenableEnum' : _MetaInfoEnum('IpmrouteenableEnum', 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'IPMROUTE-STD-MIB', _yang_ns._namespaces['IPMROUTE-STD-MIB']),
    'IpmrouteStdMib.Ipmroute' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroute',
            False, 
            [
            _MetaInfoClassMember('ipMRouteEnable', REFERENCE_ENUM_CLASS, 'IpmrouteenableEnum' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroute.IpmrouteenableEnum', 
                [], [], 
                '''                The enabled status of IP Multicast routing on this router.
                ''',
                'ipmrouteenable',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteEntryCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of rows in the ipMRouteTable.  This can be used
                to monitor the multicast routing table size.
                ''',
                'ipmrouteentrycount',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRoute',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmroutetable.Ipmrouteentry.IpmrouterttypeEnum' : _MetaInfoEnum('IpmrouterttypeEnum', 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB',
        {
            'unicast':'unicast',
            'multicast':'multicast',
        }, 'IPMROUTE-STD-MIB', _yang_ns._namespaces['IPMROUTE-STD-MIB']),
    'IpmrouteStdMib.Ipmroutetable.Ipmrouteentry' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroutetable.Ipmrouteentry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteGroup', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP multicast group address for which this entry
                contains multicast routing information.
                ''',
                'ipmroutegroup',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The network address which when combined with the
                corresponding value of ipMRouteSourceMask identifies the
                sources for which this entry contains multicast routing
                information.
                ''',
                'ipmroutesource',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteSourceMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The network mask which when combined with the corresponding
                value of ipMRouteSource identifies the sources for which
                this entry contains multicast routing information.
                ''',
                'ipmroutesourcemask',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ciscoIpMRouteBps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bits per second forwarded by this router.  This is the
                sum of all forwarded bits during a 1 second interval.  At
                the end of each second the field is cleared. This object
                has been superseded by ciscoIpMRouteBps2 (which is the
                64-bit version of this object).
                ''',
                'ciscoipmroutebps',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteBps2', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bits per second forwarded by this router. This is the sum
                of all forwarded bits during a 1 second interval. At the
                end of each second the field is cleared.
                ''',
                'ciscoipmroutebps2',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteConnectedFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicating whether there is a directly connected
                member for a group attached to the router.
                ''',
                'ciscoipmrouteconnectedflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteDifferentInIfPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets which this router has received from
                these sources and addressed to this multicast group
                address, which were not received from the interface
                indicated by ipMRouteInIfIndex. This object is a 64-bit
                version of ipMRouteDifferentInIfPackets.
                ''',
                'ciscoipmroutedifferentinifpkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteInLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Incoming interface's limit for rate limiting data
                traffic, in Kbps. Replaced by ciscoIpMRouteInLimit2.
                ''',
                'ciscoipmrouteinlimit',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteInLimit2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming interface's limit for rate limiting data
                traffic, in Kbps.
                ''',
                'ciscoipmrouteinlimit2',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteJoinFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicates whether this route is created due to
                SPT threshold.
                ''',
                'ciscoipmroutejoinflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteLastUsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                How long has it been since the last multicast packet was
                fastswitched.
                ''',
                'ciscoipmroutelastused',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteLocalFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicating whether local system is a member of a
                group on any interface.
                ''',
                'ciscoipmroutelocalflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteMetric', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Metric - The best metric heard from Assert messages. This
                object has been replaced by ciscoIpMRouteMetric2 in order
                to correctly represent a 32-bit unsigned metric value.
                ''',
                'ciscoipmroutemetric',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteMetric2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Metric - The best metric heard from Assert messages.
                ''',
                'ciscoipmroutemetric2',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteMetricPreference', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Metric Preference - The best metric preference heard from
                Assert messages.
                ''',
                'ciscoipmroutemetricpreference',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteMsdpFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicates whether this route is learned via
                MSDP.
                ''',
                'ciscoipmroutemsdpflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets contained in IP datagrams which were
                received from these sources and addressed to this multicast
                group address, and which were forwarded by this
                router. This object is a 64-bit version of
                ipMRouteOctets.
                ''',
                'ciscoipmrouteoctets',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRoutePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets which this router has received from
                these sources and addressed to this multicast group
                address. This object is a 64-bit version of ipMRoutePkts.
                ''',
                'ciscoipmroutepkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteProxyJoinFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicates whether to send join for this entry.
                ''',
                'ciscoipmrouteproxyjoinflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRoutePruneFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicates whether this route is pruned. A pruned
                route is one that has an empty outgoing interface list or
                all interfaces are in Pruned state. A multicast packet
                that matches a pruned route doesn't get forwarded.
                ''',
                'ciscoipmroutepruneflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteRegisterFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicates whether to send registers for the
                entry. A first hop router directly connected to a
                multicast source host, as well as a border router on the
                boundary of two domains running different multicast
                routing protocols, encapsulates packets to be sent on the
                shared tree. This is done until the RP sends Joins back to
                this router.
                ''',
                'ciscoipmrouteregisterflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteRpFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicating whether there is a Prune state for
                this source along the shared tree.
                ''',
                'ciscoipmrouterpflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteSparseFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicating PIM multicast routing protocol
                sparse-mode (versus dense-mode).  In sparse-mode, packets
                are forwarded only out interfaces that have been joined.
                In dense-mode, they are forwarded out all interfaces that
                have not been pruned.
                ''',
                'ciscoipmroutesparseflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteSptFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean, indicating whether data is being received on the
                SPT tree, ie the Shortest Path Tree.
                ''',
                'ciscoipmroutesptflag',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ipMRouteDifferentInIfPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which this router has received from
                these sources and addressed to this multicast group address,
                which were dropped because they were not received on the
                interface indicated by ipMRouteInIfIndex.  Packets which are
                not subject to an incoming interface check (e.g., using CBT)
                are not counted.
                ''',
                'ipmroutedifferentinifpackets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum amount of time remaining before this entry will
                be aged out.  The value 0 indicates that the entry is not
                subject to aging.
                ''',
                'ipmrouteexpirytime',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteHCOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets contained in IP datagrams which were
                received from these sources and addressed to this multicast
                group address, and which were forwarded by this router.
                This object is a 64-bit version of ipMRouteOctets.
                ''',
                'ipmroutehcoctets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The value of ifIndex for the interface on which IP
                datagrams sent by these sources to this multicast address
                are received.  A value of 0 indicates that datagrams are not
                subject to an incoming interface check, but may be accepted
                on multiple interfaces (e.g., in CBT).
                ''',
                'ipmrouteinifindex',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets contained in IP datagrams which were
                received from these sources and addressed to this multicast
                group address, and which were forwarded by this router.
                ''',
                'ipmrouteoctets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRoutePkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which this router has received from
                these sources and addressed to this multicast group
                address.
                ''',
                'ipmroutepkts',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteProtocol', REFERENCE_ENUM_CLASS, 'IanaipmrouteprotocolEnum' , 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB', 'IanaipmrouteprotocolEnum', 
                [], [], 
                '''                The multicast routing protocol via which this multicast
                forwarding entry was learned.
                ''',
                'ipmrouteprotocol',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteRtAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address portion of the route used to find the upstream
                or parent interface for this multicast forwarding entry.
                ''',
                'ipmroutertaddress',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteRtMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The mask associated with the route used to find the upstream
                or parent interface for this multicast forwarding entry.
                ''',
                'ipmroutertmask',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteRtProto', REFERENCE_ENUM_CLASS, 'IanaiprouteprotocolEnum' , 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB', 'IanaiprouteprotocolEnum', 
                [], [], 
                '''                The routing mechanism via which the route used to find the
                upstream or parent interface for this multicast forwarding
                entry was learned.  Inclusion of values for routing
                protocols is not intended to imply that those protocols need
                be supported.
                ''',
                'ipmroutertproto',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteRtType', REFERENCE_ENUM_CLASS, 'IpmrouterttypeEnum' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutetable.Ipmrouteentry.IpmrouterttypeEnum', 
                [], [], 
                '''                The reason the given route was placed in the (logical)
                multicast Routing Information Base (RIB).  A value of
                unicast means that the route would normally be placed only
                in the unicast RIB, but was placed in the multicast RIB
                (instead or in addition) due to local configuration, such as
                when running PIM over RIP.  A value of multicast means that
                
                
                
                
                
                the route was explicitly added to the multicast RIB by the
                routing protocol, such as DVMRP or Multiprotocol BGP.
                ''',
                'ipmrouterttype',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteUpstreamNeighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the upstream neighbor (e.g., RPF neighbor)
                from which IP datagrams from these sources to this multicast
                address are received, or 0.0.0.0 if the upstream neighbor is
                unknown (e.g., in CBT).
                ''',
                'ipmrouteupstreamneighbor',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time since the multicast routing information
                represented by this entry was learned by the router.
                ''',
                'ipmrouteuptime',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteEntry',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmroutetable' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroutetable',
            False, 
            [
            _MetaInfoClassMember('ipMRouteEntry', REFERENCE_LIST, 'Ipmrouteentry' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutetable.Ipmrouteentry', 
                [], [], 
                '''                An entry (conceptual row) containing the multicast routing
                information for IP datagrams from a particular source and
                addressed to a particular IP multicast group address.
                Discontinuities in counters in this entry can be detected by
                observing the value of ipMRouteUpTime.
                ''',
                'ipmrouteentry',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteTable',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry.IpmroutenexthopstateEnum' : _MetaInfoEnum('IpmroutenexthopstateEnum', 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB',
        {
            'pruned':'pruned',
            'forwarding':'forwarding',
        }, 'IPMROUTE-STD-MIB', _yang_ns._namespaces['IPMROUTE-STD-MIB']),
    'IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteNextHopGroup', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP multicast group for which this entry specifies a
                next-hop on an outgoing interface.
                ''',
                'ipmroutenexthopgroup',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopSource', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The network address which when combined with the
                corresponding value of ipMRouteNextHopSourceMask identifies
                the sources for which this entry specifies a next-hop on an
                outgoing interface.
                ''',
                'ipmroutenexthopsource',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopSourceMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The network mask which when combined with the corresponding
                value of ipMRouteNextHopSource identifies the sources for
                which this entry specifies a next-hop on an outgoing
                interface.
                ''',
                'ipmroutenexthopsourcemask',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value of the interface for the outgoing
                interface for this next-hop.
                ''',
                'ipmroutenexthopifindex',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the next-hop specific to this entry.  For
                most interfaces, this is identical to ipMRouteNextHopGroup.
                NBMA interfaces, however, may have multiple next-hop
                addresses out a single outgoing interface.
                ''',
                'ipmroutenexthopaddress',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ciscoIpMRouteNextHopMacHdr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The data link mac address header for a multicast
                datagram. Used by IP multicast fastswitching.
                ''',
                'ciscoipmroutenexthopmachdr',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteNextHopOutLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An outgoing interface's limit for rate limiting data
                traffic, in Kbps.
                ''',
                'ciscoipmroutenexthopoutlimit',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteNextHopPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets which have been forwarded using
                this route. This object is a 64-bit version of
                ipMRouteNextHopPkts.
                ''',
                'ciscoipmroutenexthoppkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopClosestMemberHops', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The minimum number of hops between this router and any
                member of this IP multicast group reached via this next-hop
                on this outgoing interface.  Any IP multicast datagrams for
                the group which have a TTL less than this number of hops
                will not be forwarded to this next-hop.
                ''',
                'ipmroutenexthopclosestmemberhops',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum amount of time remaining before this entry will
                be aged out.  If ipMRouteNextHopState is pruned(1), the
                remaining time until the prune expires and the state reverts
                to forwarding(2).  Otherwise, the remaining time until this
                entry is removed from the table.  The time remaining may be
                copied from ipMRouteExpiryTime if the protocol in use for
                this entry does not specify next-hop timers.  The value 0
                
                
                
                
                
                indicates that the entry is not subject to aging.
                ''',
                'ipmroutenexthopexpirytime',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which have been forwarded using this
                route.
                ''',
                'ipmroutenexthoppkts',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopProtocol', REFERENCE_ENUM_CLASS, 'IanaipmrouteprotocolEnum' , 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB', 'IanaipmrouteprotocolEnum', 
                [], [], 
                '''                The routing mechanism via which this next-hop was learned.
                ''',
                'ipmroutenexthopprotocol',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopState', REFERENCE_ENUM_CLASS, 'IpmroutenexthopstateEnum' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry.IpmroutenexthopstateEnum', 
                [], [], 
                '''                An indication of whether the outgoing interface and next-
                hop represented by this entry is currently being used to
                forward IP datagrams.  The value 'forwarding' indicates it
                is currently being used; the value 'pruned' indicates it is
                not.
                ''',
                'ipmroutenexthopstate',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time since the multicast routing information
                represented by this entry was learned by the router.
                ''',
                'ipmroutenexthopuptime',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteNextHopEntry',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmroutenexthoptable' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroutenexthoptable',
            False, 
            [
            _MetaInfoClassMember('ipMRouteNextHopEntry', REFERENCE_LIST, 'Ipmroutenexthopentry' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry', 
                [], [], 
                '''                An entry (conceptual row) in the list of next-hops on
                outgoing interfaces to which IP multicast datagrams from
                particular sources to a IP multicast group address are
                routed.  Discontinuities in counters in this entry can be
                detected by observing the value of ipMRouteUpTime.
                ''',
                'ipmroutenexthopentry',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteNextHopTable',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteInterfaceIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value of the interface for which this entry
                contains information.
                ''',
                'ipmrouteinterfaceifindex',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ciscoIpMRouteIfHCInMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of multicast packets that have arrived on the
                interface. This object is a 64-bit version of
                ciscoIpMRouteIfInMcastPkts
                ''',
                'ciscoipmrouteifhcinmcastpkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteIfHCOutMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of multicast packets that have been sent on
                the interface. This object is a 64-bit version of
                ciscoIpMRouteIfOutMcastPkts
                ''',
                'ciscoipmrouteifhcoutmcastpkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteIfInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets of multicast packets that have
                arrived on the interface. This object is a 64-bit version
                of ipMRouteInterfaceInMcastOctets.
                ''',
                'ciscoipmrouteifinmcastoctets',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteIfInMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of multicast packets that have arrived on the
                interface.
                ''',
                'ciscoipmrouteifinmcastpkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteIfOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets of multicast packets that have been
                sent on the interface. This object is a 64-bit version of
                ipMRouteInterfaceOutMcastOctets.
                ''',
                'ciscoipmrouteifoutmcastoctets',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ciscoIpMRouteIfOutMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of multicast packets that have been sent on
                the interface.
                ''',
                'ciscoipmrouteifoutmcastpkts',
                'CISCO-IPMROUTE-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceHCInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets of multicast packets that have arrived
                on the interface, including framing characters.  This object
                is a 64-bit version of ipMRouteInterfaceInMcastOctets.  It
                is similar to ifHCInOctets in the Interfaces MIB, except
                that only multicast packets are counted.
                ''',
                'ipmrouteinterfacehcinmcastoctets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceHCOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets of multicast packets that have been
                
                
                
                
                
                sent on the interface.  This object is a 64-bit version of
                ipMRouteInterfaceOutMcastOctets.
                ''',
                'ipmrouteinterfacehcoutmcastoctets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets of multicast packets that have arrived
                on the interface, including framing characters.  This object
                is similar to ifInOctets in the Interfaces MIB, except that
                only multicast packets are counted.
                ''',
                'ipmrouteinterfaceinmcastoctets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets of multicast packets that have been
                sent on the interface.
                ''',
                'ipmrouteinterfaceoutmcastoctets',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceProtocol', REFERENCE_ENUM_CLASS, 'IanaipmrouteprotocolEnum' , 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB', 'IanaipmrouteprotocolEnum', 
                [], [], 
                '''                The routing protocol running on this interface.
                ''',
                'ipmrouteinterfaceprotocol',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceRateLimit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The rate-limit, in kilobits per second, of forwarded
                multicast traffic on the interface.  A rate-limit of 0
                indicates that no rate limiting is done.
                ''',
                'ipmrouteinterfaceratelimit',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceTtl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The datagram TTL threshold for the interface. Any IP
                multicast datagrams with a TTL less than this threshold will
                not be forwarded out the interface. The default value of 0
                means all multicast packets are forwarded out the
                interface.
                ''',
                'ipmrouteinterfacettl',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteInterfaceEntry',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmrouteinterfacetable' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmrouteinterfacetable',
            False, 
            [
            _MetaInfoClassMember('ipMRouteInterfaceEntry', REFERENCE_LIST, 'Ipmrouteinterfaceentry' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry', 
                [], [], 
                '''                An entry (conceptual row) containing the multicast routing
                information for a particular interface.
                ''',
                'ipmrouteinterfaceentry',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteInterfaceTable',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteBoundaryIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The IfIndex value for the interface to which this boundary
                applies.  Packets with a destination address in the
                associated address/mask range will not be forwarded out this
                interface.
                ''',
                'ipmrouteboundaryifindex',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteBoundaryAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address which when combined with the
                corresponding value of ipMRouteBoundaryAddressMask
                identifies the group range for which the scoped boundary
                exists.  Scoped addresses must come from the range 239.x.x.x
                as specified in RFC 2365.
                ''',
                'ipmrouteboundaryaddress',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteBoundaryAddressMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address mask which when combined with the
                corresponding value of ipMRouteBoundaryAddress identifies
                the group range for which the scoped boundary exists.
                ''',
                'ipmrouteboundaryaddressmask',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteBoundaryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row, by which new entries may be
                created, or old entries deleted from this table.
                ''',
                'ipmrouteboundarystatus',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteBoundaryEntry',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmrouteboundarytable' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmrouteboundarytable',
            False, 
            [
            _MetaInfoClassMember('ipMRouteBoundaryEntry', REFERENCE_LIST, 'Ipmrouteboundaryentry' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry', 
                [], [], 
                '''                An entry (conceptual row) in the ipMRouteBoundaryTable
                representing a scoped boundary.
                ''',
                'ipmrouteboundaryentry',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteBoundaryTable',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteScopeNameAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address which when combined with the
                corresponding value of ipMRouteScopeNameAddressMask
                identifies the group range associated with the multicast
                scope.  Scoped addresses must come from the range
                239.x.x.x.
                ''',
                'ipmroutescopenameaddress',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteScopeNameAddressMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address mask which when combined with the
                corresponding value of ipMRouteScopeNameAddress identifies
                the group range associated with the multicast scope.
                ''',
                'ipmroutescopenameaddressmask',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteScopeNameLanguage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The RFC 1766-style language tag associated with the scope
                name.
                ''',
                'ipmroutescopenamelanguage',
                'IPMROUTE-STD-MIB', True),
            _MetaInfoClassMember('ipMRouteScopeNameDefault', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, indicates a preference that the name in the
                following language should be used by applications if no name
                is available in a desired language.
                ''',
                'ipmroutescopenamedefault',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteScopeNameStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row, by which new entries may be
                created, or old entries deleted from this table.
                ''',
                'ipmroutescopenamestatus',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteScopeNameString', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The textual name associated with the multicast scope.  The
                value of this object should be suitable for displaying to
                end-users, such as when allocating a multicast address in
                this scope.  When no name is specified, the default value of
                this object should be the string 239.x.x.x/y with x and y
                replaced appropriately to describe the address and mask
                length associated with the scope.
                ''',
                'ipmroutescopenamestring',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteScopeNameEntry',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib.Ipmroutescopenametable' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib.Ipmroutescopenametable',
            False, 
            [
            _MetaInfoClassMember('ipMRouteScopeNameEntry', REFERENCE_LIST, 'Ipmroutescopenameentry' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry', 
                [], [], 
                '''                An entry (conceptual row) in the ipMRouteScopeNameTable
                representing a multicast scope name.
                ''',
                'ipmroutescopenameentry',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'ipMRouteScopeNameTable',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
    'IpmrouteStdMib' : {
        'meta_info' : _MetaInfoClass('IpmrouteStdMib',
            False, 
            [
            _MetaInfoClassMember('ipMRoute', REFERENCE_CLASS, 'Ipmroute' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroute', 
                [], [], 
                '''                ''',
                'ipmroute',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteBoundaryTable', REFERENCE_CLASS, 'Ipmrouteboundarytable' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmrouteboundarytable', 
                [], [], 
                '''                The (conceptual) table listing the router's scoped
                multicast address boundaries.
                ''',
                'ipmrouteboundarytable',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteInterfaceTable', REFERENCE_CLASS, 'Ipmrouteinterfacetable' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmrouteinterfacetable', 
                [], [], 
                '''                The (conceptual) table containing multicast routing
                information specific to interfaces.
                ''',
                'ipmrouteinterfacetable',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteNextHopTable', REFERENCE_CLASS, 'Ipmroutenexthoptable' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutenexthoptable', 
                [], [], 
                '''                The (conceptual) table containing information on the next-
                hops on outgoing interfaces for routing IP multicast
                datagrams.  Each entry is one of a list of next-hops on
                outgoing interfaces for particular sources sending to a
                particular multicast group address.
                ''',
                'ipmroutenexthoptable',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteScopeNameTable', REFERENCE_CLASS, 'Ipmroutescopenametable' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutescopenametable', 
                [], [], 
                '''                The (conceptual) table listing the multicast scope names.
                ''',
                'ipmroutescopenametable',
                'IPMROUTE-STD-MIB', False),
            _MetaInfoClassMember('ipMRouteTable', REFERENCE_CLASS, 'Ipmroutetable' , 'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB', 'IpmrouteStdMib.Ipmroutetable', 
                [], [], 
                '''                The (conceptual) table containing multicast routing
                information for IP datagrams sent by particular sources to
                the IP multicast groups known to this router.
                ''',
                'ipmroutetable',
                'IPMROUTE-STD-MIB', False),
            ],
            'IPMROUTE-STD-MIB',
            'IPMROUTE-STD-MIB',
            _yang_ns._namespaces['IPMROUTE-STD-MIB'],
        'ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB'
        ),
    },
}
_meta_table['IpmrouteStdMib.Ipmroutetable.Ipmrouteentry']['meta_info'].parent =_meta_table['IpmrouteStdMib.Ipmroutetable']['meta_info']
_meta_table['IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry']['meta_info'].parent =_meta_table['IpmrouteStdMib.Ipmroutenexthoptable']['meta_info']
_meta_table['IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry']['meta_info'].parent =_meta_table['IpmrouteStdMib.Ipmrouteinterfacetable']['meta_info']
_meta_table['IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry']['meta_info'].parent =_meta_table['IpmrouteStdMib.Ipmrouteboundarytable']['meta_info']
_meta_table['IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry']['meta_info'].parent =_meta_table['IpmrouteStdMib.Ipmroutescopenametable']['meta_info']
_meta_table['IpmrouteStdMib.Ipmroute']['meta_info'].parent =_meta_table['IpmrouteStdMib']['meta_info']
_meta_table['IpmrouteStdMib.Ipmroutetable']['meta_info'].parent =_meta_table['IpmrouteStdMib']['meta_info']
_meta_table['IpmrouteStdMib.Ipmroutenexthoptable']['meta_info'].parent =_meta_table['IpmrouteStdMib']['meta_info']
_meta_table['IpmrouteStdMib.Ipmrouteinterfacetable']['meta_info'].parent =_meta_table['IpmrouteStdMib']['meta_info']
_meta_table['IpmrouteStdMib.Ipmrouteboundarytable']['meta_info'].parent =_meta_table['IpmrouteStdMib']['meta_info']
_meta_table['IpmrouteStdMib.Ipmroutescopenametable']['meta_info'].parent =_meta_table['IpmrouteStdMib']['meta_info']
