


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CbgpsafiEnum' : _MetaInfoEnum('CbgpsafiEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'unicastAndMulticast':'unicastAndMulticast',
            'vpn':'vpn',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgpglobal' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgpglobal',
            False, 
            [
            _MetaInfoClassMember('cbgpLocalAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local autonomous system (AS) number.
                ''',
                'cbgplocalas',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpNotifsEnable', REFERENCE_BITS, 'Cbgpnotifsenable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgpglobal.Cbgpnotifsenable', 
                [], [], 
                '''                Indicates whether the specific notifications are
                enabled. 
                If notifsEnable(0) bit is set to 1,
                then the notifications defined in
                ciscoBgp4NotificationsGroup1 are enabled; 
                If notifsPeer2Enable(1) bit is set to 1,
                then the notifications defined in
                ciscoBgp4Peer2NotificationsGroup are enabled.
                ''',
                'cbgpnotifsenable',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpGlobal',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteatomicaggregateEnum' : _MetaInfoEnum('CbgprouteatomicaggregateEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'lessSpecificRouteNotSelected':'lessSpecificRouteNotSelected',
            'lessSpecificRouteSelected':'lessSpecificRouteSelected',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteoriginEnum' : _MetaInfoEnum('CbgprouteoriginEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'igp':'igp',
            'egp':'egp',
            'incomplete':'incomplete',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry',
            False, 
            [
            _MetaInfoClassMember('cbgpRouteAfi', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Represents Address Family Identifier(AFI) of the
                Network Layer protocol associated with the route.
                An implementation is only required to support IPv4
                unicast and VPNv4 (Value - 1) address families.
                ''',
                'cbgprouteafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpRouteSafi', REFERENCE_ENUM_CLASS, 'CbgpsafiEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpsafiEnum', 
                [], [], 
                '''                Represents Subsequent Address Family Identifier(SAFI)
                of the route. It gives additional information about
                the type of the route. An implementation is only 
                required to support IPv4 unicast(Value - 1) and VPNv4(
                Value - 128) address families.
                ''',
                'cbgproutesafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpRoutePeerType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Represents the type of Network Layer address stored
                in cbgpRoutePeer. An implementation is only required
                to support IPv4 address type(Value - 1).
                ''',
                'cbgproutepeertype',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpRoutePeer', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Network Layer address of the peer where the route
                information was learned. An implementation is only 
                required to support an IPv4 peer.
                ''',
                'cbgproutepeer',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpRouteAddrPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A Network Address prefix in the Network Layer
                Reachability Information field of BGP UPDATE message.
                This object is a Network Address containing the prefix
                with length specified by cbgpRouteAddrPrefixLen. Any
                bits beyond the length specified by
                cbgpRouteAddrPrefixLen are zeroed.
                ''',
                'cbgprouteaddrprefix',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpRouteAddrPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                Length in bits of the Network Address prefix in the
                Network Layer Reachability Information field.
                ''',
                'cbgprouteaddrprefixlen',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpRouteAggregatorAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Network Layer address of the last BGP4 speaker
                that performed route aggregation.  A value of all zeros
                indicates the absence of this attribute.
                ''',
                'cbgprouteaggregatoraddr',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteAggregatorAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Represents the type of Network Layer address stored
                in cbgpRouteAggregatorAddr.
                ''',
                'cbgprouteaggregatoraddrtype',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteAggregatorAS', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The AS number of the last BGP4 speaker that performed
                route aggregation.  A value of zero (0) indicates the 
                absence of this attribute.
                ''',
                'cbgprouteaggregatoras',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteASPathSegment', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The sequence of AS path segments.  Each AS
                path segment is represented by a triple
                <type, length, value>.
                
                The type is a 1-octet field which has two
                possible values:
                1  AS_SET: unordered set of ASs a route in the 
                          UPDATE message has traversed
                2  AS_SEQUENCE: ordered set of ASs a route in the
                               UPDATE message has traversed.
                
                The length is a 1-octet field containing the
                number of ASs in the value field.
                
                The value field contains one or more AS
                numbers, each AS is represented in the octet
                string as a pair of octets according to the
                following algorithm:
                
                first-byte-of-pair = ASNumber / 256;
                second-byte-of-pair = ASNumber & 255;
                ''',
                'cbgprouteaspathsegment',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteAtomicAggregate', REFERENCE_ENUM_CLASS, 'CbgprouteatomicaggregateEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteatomicaggregateEnum', 
                [], [], 
                '''                Whether or not the local system has selected a less
                specific route without selecting a more specific
                route.
                ''',
                'cbgprouteatomicaggregate',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteBest', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether or not this route was chosen
                as the best BGP4 route.
                ''',
                'cbgproutebest',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteLocalPref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The degree of preference calculated by the local BGP4
                speaker for the route. The value of this object is 
                irrelevant if the value of cbgpRouteLocalPrefPresent 
                is false(2).
                ''',
                'cbgproutelocalpref',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteLocalPrefPresent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the presence/absence of LOCAL_PREF
                attribute for the route.
                ''',
                'cbgproutelocalprefpresent',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteMedPresent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the presence/absence of MULTI_EXIT_DISC
                attribute for the route.
                ''',
                'cbgproutemedpresent',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteMultiExitDisc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This metric is used to discriminate between multiple
                exit points to an adjacent autonomous system.  The
                value of this object is irrelevant if the value of
                of cbgpRouteMedPresent is false(2).
                ''',
                'cbgproutemultiexitdisc',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteNextHop', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Network Layer address of the border router
                that should be used for the destination network.
                ''',
                'cbgproutenexthop',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteOrigin', REFERENCE_ENUM_CLASS, 'CbgprouteoriginEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteoriginEnum', 
                [], [], 
                '''                The ultimate origin of the route information.
                ''',
                'cbgprouteorigin',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteUnknownAttr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                One or more path attributes not understood by this
                BGP4 speaker.  Size zero (0) indicates the absence of
                such attribute(s).  Octets beyond the maximum size, if
                any, are not recorded by this object.  
                
                Each path attribute is a triple <attribute type,
                attribute length, attribute value> of variable length.
                Attribute Type is a two-octet field that consists of
                the Attribute Flags octet followed by the Attribute
                Type Code octet.  If the Extended Length bit of the 
                Attribute Flags octet is set to 0, the third octet of 
                the Path Attribute contains the length of the
                attribute data in octets.  If the Extended Length bit 
                of the Attribute Flags octet is set to 1, then the
                third and the fourth octets of the path attribute 
                contain the length of the attribute data in octets.
                The remaining octets of the Path Attribute represent 
                the attribute value and are interpreted according to 
                the Attribute Flags and the Attribute Type Code.
                ''',
                'cbgprouteunknownattr',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpRouteEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgproutetable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgproutetable',
            False, 
            [
            _MetaInfoClassMember('cbgpRouteEntry', REFERENCE_LIST, 'Cbgprouteentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry', 
                [], [], 
                '''                Information about a path to a network received from
                a peer.
                ''',
                'cbgprouteentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpRouteTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry.CbgppeercapcodeEnum' : _MetaInfoEnum('CbgppeercapcodeEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'multiProtocol':'multiProtocol',
            'routeRefresh':'routeRefresh',
            'gracefulRestart':'gracefulRestart',
            'routeRefreshOld':'routeRefreshOld',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry',
            False, 
            [
            _MetaInfoClassMember('bgpPeerRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'bgppeerremoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerCapCode', REFERENCE_ENUM_CLASS, 'CbgppeercapcodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry.CbgppeercapcodeEnum', 
                [], [], 
                '''                The BGP Capability Advertisement Capability Code.
                ''',
                'cbgppeercapcode',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerCapIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Multiple instances of a given capability may be
                sent by a BGP speaker.  This variable is used
                to index them.
                ''',
                'cbgppeercapindex',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerCapValue', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The value of the announced capability. This
                MIB object value is organized as given below,
                    Capability : Route Refresh Capability
                                 Null string
                    Capability : Multiprotocol Extensions
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                    Capability : Graceful Restart
                      +----------------------------------+
                      | Restart Flags (4 bits)           |
                      +----------------------------------+
                      | Restart Time in seconds (12 bits)|
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                      | Flags for Address Family (8 bits)|
                      +----------------------------------+
                      | ...                              |
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                      | Flags for Address Family (8 bits)|
                      +----------------------------------+
                ''',
                'cbgppeercapvalue',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeerCapsEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeercapstable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeercapstable',
            False, 
            [
            _MetaInfoClassMember('cbgpPeerCapsEntry', REFERENCE_LIST, 'Cbgppeercapsentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry', 
                [], [], 
                '''                Each entry represents a capability received from a
                peer with a particular code and an index. When a 
                capability is received multiple times with different
                values during a BGP connection establishment, 
                corresponding entries are differentiated with indices.
                ''',
                'cbgppeercapsentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeerCapsTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry',
            False, 
            [
            _MetaInfoClassMember('bgpPeerRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'bgppeerremoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerAddrFamilyAfi', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The AFI index of the entry. An implementation
                is only required to support IPv4 unicast and 
                VPNv4 (Value - 1) address families.
                ''',
                'cbgppeeraddrfamilyafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerAddrFamilySafi', REFERENCE_ENUM_CLASS, 'CbgpsafiEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpsafiEnum', 
                [], [], 
                '''                The SAFI index of the entry. An implementation
                is only required to support IPv4 unicast(Value 
                - 1) and VPNv4( Value - 128) address families.
                ''',
                'cbgppeeraddrfamilysafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerAddrFamilyName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Implementation specific Address Family name.
                ''',
                'cbgppeeraddrfamilyname',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeerAddrFamilyEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeeraddrfamilytable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeeraddrfamilytable',
            False, 
            [
            _MetaInfoClassMember('cbgpPeerAddrFamilyEntry', REFERENCE_LIST, 'Cbgppeeraddrfamilyentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry', 
                [], [], 
                '''                An entry is identified by an AFI/SAFI pair and
                peer address. It contains names associated with
                an address family.
                ''',
                'cbgppeeraddrfamilyentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeerAddrFamilyTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry',
            False, 
            [
            _MetaInfoClassMember('bgpPeerRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'bgppeerremoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerAddrFamilyAfi', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cbgppeeraddrfamilyafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerAddrFamilySafi', REFERENCE_ENUM_CLASS, 'CbgpsafiEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpsafiEnum', 
                [], [], 
                '''                ''',
                'cbgppeeraddrfamilysafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeerAcceptedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accepted route prefixes on this connection,
                which belong to an address family.
                ''',
                'cbgppeeracceptedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerAdvertisedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix,
                which belongs to an address family is advertised
                on this connection. It is initialized to zero when 
                the connection is undergone a hard reset.
                ''',
                'cbgppeeradvertisedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerDeniedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix, which
                belongs to an address family, received on this 
                connection is denied. It is initialized to zero when 
                the connection is undergone a hard reset.
                ''',
                'cbgppeerdeniedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixAdminLimit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Max number of route prefixes accepted for an address
                family on this connection.
                ''',
                'cbgppeerprefixadminlimit',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixClearThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Prefix threshold value (%) for an address family
                on this connection at which SNMP clear notification
                is generated if prefix threshold notification is
                already generated.
                ''',
                'cbgppeerprefixclearthreshold',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Prefix threshold value (%) for an address family
                on this connection at which warning message stating
                the prefix count is crossed the threshold or 
                corresponding SNMP notification is generated.
                ''',
                'cbgppeerprefixthreshold',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerSuppressedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix,
                which belongs to an address family is suppressed
                from being sent on this connection. It is 
                initialized to zero when the connection is undergone
                a hard reset.
                ''',
                'cbgppeersuppressedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerWithdrawnPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix,
                which belongs to an address family, is withdrawn on
                this connection. It is initialized to zero when the
                connection is undergone a hard reset.
                ''',
                'cbgppeerwithdrawnprefixes',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeerAddrFamilyPrefixEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable',
            False, 
            [
            _MetaInfoClassMember('cbgpPeerAddrFamilyPrefixEntry', REFERENCE_LIST, 'Cbgppeeraddrfamilyprefixentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry', 
                [], [], 
                '''                An entry is identified by an AFI/SAFI pair and
                peer address. It contains information associated 
                with route prefixes belonging to an address family.
                ''',
                'cbgppeeraddrfamilyprefixentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeerAddrFamilyPrefixTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2AdminstatusEnum' : _MetaInfoEnum('Cbgppeer2AdminstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'stop':'stop',
            'start':'start',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2PrevstateEnum' : _MetaInfoEnum('Cbgppeer2PrevstateEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'none':'none',
            'idle':'idle',
            'connect':'connect',
            'active':'active',
            'opensent':'opensent',
            'openconfirm':'openconfirm',
            'established':'established',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2StateEnum' : _MetaInfoEnum('Cbgppeer2StateEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'idle':'idle',
            'connect':'connect',
            'active':'active',
            'opensent':'opensent',
            'openconfirm':'openconfirm',
            'established':'established',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2Type', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Represents the type of Peer address stored
                in cbgpPeer2Entry.
                ''',
                'cbgppeer2type',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2RemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The remote IP address of this entry's BGP
                peer.
                ''',
                'cbgppeer2remoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AdminStatus', REFERENCE_ENUM_CLASS, 'Cbgppeer2AdminstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2AdminstatusEnum', 
                [], [], 
                '''                The desired state of the BGP connection.
                A transition from 'stop' to 'start' will cause
                the BGP Manual Start Event to be generated.
                A transition from 'start' to 'stop' will cause
                the BGP Manual Stop Event to be generated.
                This parameter can be used to restart BGP peer
                connections.  Care should be used in providing
                write access to this object without adequate
                authentication.
                ''',
                'cbgppeer2adminstatus',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2ConnectRetryInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval (in seconds) for the
                ConnectRetry timer.  The suggested value
                for this timer is 120 seconds.
                ''',
                'cbgppeer2connectretryinterval',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2FsmEstablishedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This timer indicates how long (in
                seconds) this peer has been in the
                established state or how long
                since this peer was last in the
                established state.  It is set to zero when
                a new peer is configured or when the router is
                booted.
                ''',
                'cbgppeer2fsmestablishedtime',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2FsmEstablishedTransitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times the BGP FSM
                transitioned into the established state
                for this peer.
                ''',
                'cbgppeer2fsmestablishedtransitions',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2HoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('3', '65535')], [], 
                '''                Time interval (in seconds) for the Hold
                Timer established with the peer.  The
                value of this object is calculated by this
                BGP speaker, using the smaller of the
                values in cbgpPeer2HoldTimeConfigured and the
                Hold Time received in the OPEN message.
                
                This value must be at least three seconds
                if it is not zero (0).
                
                If the Hold Timer has not been established
                with the peer this object MUST have a value
                of zero (0).
                
                If the cbgpPeer2HoldTimeConfigured object has
                a value of (0), then this object MUST have a
                value of (0).
                ''',
                'cbgppeer2holdtime',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2HoldTimeConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('3', '65535')], [], 
                '''                Time interval (in seconds) for the Hold Time
                configured for this BGP speaker with this
                peer.  This value is placed in an OPEN
                message sent to this peer by this BGP
                speaker, and is compared with the Hold
                Time field in an OPEN message received
                from the peer when determining the Hold
                Time (cbgpPeer2HoldTime) with the peer.
                This value must not be less than three
                seconds if it is not zero (0).  If it is
                zero (0), the Hold Time is NOT to be
                established with the peer.  The suggested
                value for this timer is 90 seconds.
                ''',
                'cbgppeer2holdtimeconfigured',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2InTotalMessages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of messages received
                from the remote peer on this connection.
                ''',
                'cbgppeer2intotalmessages',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2InUpdateElapsedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Elapsed time (in seconds) since the last BGP
                UPDATE message was received from the peer.
                Each time cbgpPeer2InUpdates is incremented,
                the value of this object is set to zero (0).
                ''',
                'cbgppeer2inupdateelapsedtime',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2InUpdates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of BGP UPDATE messages
                received on this connection.
                ''',
                'cbgppeer2inupdates',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2KeepAlive', ATTRIBUTE, 'int' , None, None, 
                [('0', '21845')], [], 
                '''                Time interval (in seconds) for the KeepAlive
                timer established with the peer.  The value
                of this object is calculated by this BGP
                speaker such that, when compared with
                cbgpPeer2HoldTime, it has the same proportion
                that cbgpPeer2KeepAliveConfigured has,
                compared with cbgpPeer2HoldTimeConfigured.
                
                If the KeepAlive timer has not been established
                with the peer, this object MUST have a value
                of zero (0).
                
                If the of cbgpPeer2KeepAliveConfigured object
                has a value of (0), then this object MUST have
                a value of (0).
                ''',
                'cbgppeer2keepalive',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2KeepAliveConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', '21845')], [], 
                '''                Time interval (in seconds) for the
                KeepAlive timer configured for this BGP
                speaker with this peer.  The value of this
                object will only determine the
                KEEPALIVE messages' frequency relative to
                the value specified in
                cbgpPeer2HoldTimeConfigured; the actual
                time interval for the KEEPALIVE messages is
                indicated by cbgpPeer2KeepAlive.  A
                reasonable maximum value for this timer
                would be one third of that of
                cbgpPeer2HoldTimeConfigured.
                If the value of this object is zero (0),
                no periodical KEEPALIVE messages are sent
                to the peer after the BGP connection has
                been established.  The suggested value for
                this timer is 30 seconds.
                ''',
                'cbgppeer2keepaliveconfigured',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2LastError', ATTRIBUTE, 'str' , None, None, 
                [(2, None)], [], 
                '''                The last error code and subcode seen by this
                peer on this connection.  If no error has
                occurred, this field is zero.  Otherwise, the
                first byte of this two byte OCTET STRING
                contains the error code, and the second byte
                contains the subcode.
                ''',
                'cbgppeer2lasterror',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2LastErrorTxt', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Implementation specific error description for
                bgpPeerLastErrorReceived.
                ''',
                'cbgppeer2lasterrortxt',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2LocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The local IP address of this entry's BGP
                connection.
                ''',
                'cbgppeer2localaddr',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2LocalAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local AS number for this session.
                ''',
                'cbgppeer2localas',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2LocalIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The BGP Identifier of this entry's BGP peer.
                ''',
                'cbgppeer2localidentifier',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2LocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port for the TCP connection between
                the BGP peers.
                ''',
                'cbgppeer2localport',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2MinASOriginationInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval (in seconds) for the
                MinASOriginationInterval timer.
                The suggested value for this timer is 15
                seconds.
                ''',
                'cbgppeer2minasoriginationinterval',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2MinRouteAdvertisementInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval (in seconds) for the
                MinRouteAdvertisementInterval timer.
                The suggested value for this timer is 30
                seconds for EBGP connections and 5
                seconds for IBGP connections.
                ''',
                'cbgppeer2minrouteadvertisementinterval',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2NegotiatedVersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The negotiated version of BGP running between
                the two peers.
                
                This entry MUST be zero (0) unless the
                cbgpPeer2State is in the openconfirm or the
                established state.
                
                Note that legal values for this object are
                between 0 and 255.
                ''',
                'cbgppeer2negotiatedversion',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2OutTotalMessages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of messages transmitted to
                the remote peer on this connection.
                ''',
                'cbgppeer2outtotalmessages',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2OutUpdates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of BGP UPDATE messages
                transmitted on this connection.
                ''',
                'cbgppeer2outupdates',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2PrevState', REFERENCE_ENUM_CLASS, 'Cbgppeer2PrevstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2PrevstateEnum', 
                [], [], 
                '''                The BGP peer connection previous state.
                ''',
                'cbgppeer2prevstate',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2RemoteAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remote autonomous system number received in
                the BGP OPEN message.
                ''',
                'cbgppeer2remoteas',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2RemoteIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The BGP Identifier of this entry's BGP peer.
                This entry MUST be 0.0.0.0 unless the
                cbgpPeer2State is in the openconfirm or the
                established state.
                ''',
                'cbgppeer2remoteidentifier',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2RemotePort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote port for the TCP connection
                between the BGP peers.  Note that the
                objects cbgpPeer2LocalAddr,
                cbgpPeer2LocalPort, cbgpPeer2RemoteAddr, and
                cbgpPeer2RemotePort provide the appropriate
                reference to the standard MIB TCP
                connection table.
                ''',
                'cbgppeer2remoteport',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2State', REFERENCE_ENUM_CLASS, 'Cbgppeer2StateEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2StateEnum', 
                [], [], 
                '''                The BGP peer connection state.
                ''',
                'cbgppeer2state',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2Entry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Table' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Table',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2Entry', REFERENCE_LIST, 'Cbgppeer2Entry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry', 
                [], [], 
                '''                Entry containing information about the
                connection with a BGP peer.
                ''',
                'cbgppeer2entry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2Table',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry.Cbgppeer2CapcodeEnum' : _MetaInfoEnum('Cbgppeer2CapcodeEnum', 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB',
        {
            'multiProtocol':'multiProtocol',
            'routeRefresh':'routeRefresh',
            'gracefulRestart':'gracefulRestart',
            'fourByteAs':'fourByteAs',
            'addPath':'addPath',
            'routeRefreshOld':'routeRefreshOld',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2Type', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cbgppeer2type',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2RemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'cbgppeer2remoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2CapCode', REFERENCE_ENUM_CLASS, 'Cbgppeer2CapcodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry.Cbgppeer2CapcodeEnum', 
                [], [], 
                '''                The BGP Capability Advertisement Capability Code.
                ''',
                'cbgppeer2capcode',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2CapIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Multiple instances of a given capability may be
                sent by a BGP speaker.  This variable is used
                to index them.
                ''',
                'cbgppeer2capindex',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2CapValue', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The value of the announced capability. This
                MIB object value is organized as given below,
                    Capability : Route Refresh Capability
                                 4-Byte AS Capability
                                 Null string
                    Capability : Multiprotocol Extensions
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                    Capability : Graceful Restart
                      +----------------------------------+
                      | Restart Flags (4 bits)           |
                      +----------------------------------+
                      | Restart Time in seconds (12 bits)|
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                      | Flags for Address Family (8 bits)|
                      +----------------------------------+
                      | ...                              |
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                      | Flags for Address Family (8 bits)|
                      +----------------------------------+
                    Capability : Additional Paths
                      +----------------------------------+
                      | AFI(16 bits)                     |
                      +----------------------------------+
                      | SAFI (8 bits)                    |
                      +----------------------------------+
                      | Send/Receive (8 bits)            |
                      +----------------------------------+
                ''',
                'cbgppeer2capvalue',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2CapsEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Capstable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Capstable',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2CapsEntry', REFERENCE_LIST, 'Cbgppeer2Capsentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry', 
                [], [], 
                '''                Each entry represents a capability received from a
                peer with a particular code and an index. When a
                capability is received multiple times with different
                values during a BGP connection establishment,
                corresponding entries are differentiated with indices.
                ''',
                'cbgppeer2capsentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2CapsTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2Type', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cbgppeer2type',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2RemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'cbgppeer2remoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AddrFamilyAfi', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The AFI index of the entry. An implementation
                is only required to support IPv4 unicast and
                VPNv4 (Value - 1) address families.
                ''',
                'cbgppeer2addrfamilyafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AddrFamilySafi', REFERENCE_ENUM_CLASS, 'CbgpsafiEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpsafiEnum', 
                [], [], 
                '''                The SAFI index of the entry. An implementation
                is only required to support IPv4 unicast(Value
                - 1) and VPNv4( Value - 128) address families.
                ''',
                'cbgppeer2addrfamilysafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AddrFamilyName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Implementation specific Address Family name.
                ''',
                'cbgppeer2addrfamilyname',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2AddrFamilyEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Addrfamilytable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Addrfamilytable',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2AddrFamilyEntry', REFERENCE_LIST, 'Cbgppeer2Addrfamilyentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry', 
                [], [], 
                '''                An entry is identified by an AFI/SAFI pair and
                peer address. It contains names associated with
                an address family.
                ''',
                'cbgppeer2addrfamilyentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2AddrFamilyTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2Type', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cbgppeer2type',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2RemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'cbgppeer2remoteaddr',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AddrFamilyAfi', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'cbgppeer2addrfamilyafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AddrFamilySafi', REFERENCE_ENUM_CLASS, 'CbgpsafiEnum' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpsafiEnum', 
                [], [], 
                '''                ''',
                'cbgppeer2addrfamilysafi',
                'CISCO-BGP4-MIB', True),
            _MetaInfoClassMember('cbgpPeer2AcceptedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accepted route prefixes on this connection,
                which belong to an address family.
                ''',
                'cbgppeer2acceptedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2AdvertisedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix,
                which belongs to an address family is advertised
                on this connection. It is initialized to zero when
                the connection is undergone a hard reset.
                ''',
                'cbgppeer2advertisedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2DeniedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix, which
                belongs to an address family, received on this
                connection is denied. It is initialized to zero when
                the connection is undergone a hard reset.
                ''',
                'cbgppeer2deniedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2PrefixAdminLimit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Max number of route prefixes accepted for an address
                family on this connection.
                ''',
                'cbgppeer2prefixadminlimit',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2PrefixClearThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Prefix threshold value (%) for an address family
                on this connection at which SNMP clear notification
                is generated if prefix threshold notification is
                already generated.
                ''',
                'cbgppeer2prefixclearthreshold',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2PrefixThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Prefix threshold value (%) for an address family
                on this connection at which warning message stating
                the prefix count is crossed the threshold or
                corresponding SNMP notification is generated.
                ''',
                'cbgppeer2prefixthreshold',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2SuppressedPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix,
                which belongs to an address family is suppressed
                from being sent on this connection. It is
                initialized to zero when the connection is undergone
                a hard reset.
                ''',
                'cbgppeer2suppressedprefixes',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2WithdrawnPrefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter is incremented when a route prefix,
                which belongs to an address family, is withdrawn on
                this connection. It is initialized to zero when the
                connection is undergone a hard reset.
                ''',
                'cbgppeer2withdrawnprefixes',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2AddrFamilyPrefixEntry',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable',
            False, 
            [
            _MetaInfoClassMember('cbgpPeer2AddrFamilyPrefixEntry', REFERENCE_LIST, 'Cbgppeer2Addrfamilyprefixentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry', 
                [], [], 
                '''                An entry is identified by an AFI/SAFI pair and
                peer address. It contains information associated
                with route prefixes belonging to an address family.
                ''',
                'cbgppeer2addrfamilyprefixentry',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'cbgpPeer2AddrFamilyPrefixTable',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
    'CiscoBgp4Mib' : {
        'meta_info' : _MetaInfoClass('CiscoBgp4Mib',
            False, 
            [
            _MetaInfoClassMember('cbgpGlobal', REFERENCE_CLASS, 'Cbgpglobal' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgpglobal', 
                [], [], 
                '''                ''',
                'cbgpglobal',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2AddrFamilyPrefixTable', REFERENCE_CLASS, 'Cbgppeer2Addrfamilyprefixtable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable', 
                [], [], 
                '''                This table contains prefix related information
                related to address families supported by a peer.
                Supported address families of a peer are known
                during BGP connection establishment. When a new
                supported address family is known, this table
                is updated with a new entry. When an address
                family is not supported any more, corresponding
                entry is deleted from the table.
                ''',
                'cbgppeer2addrfamilyprefixtable',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2AddrFamilyTable', REFERENCE_CLASS, 'Cbgppeer2Addrfamilytable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Addrfamilytable', 
                [], [], 
                '''                This table contains information related to
                address families supported by a peer. Supported
                address families of a peer are known during BGP
                connection establishment. When a new supported
                address family is known, this table is updated
                with a new entry. When an address family is not
                supported any more, corresponding entry is deleted
                from the table.
                ''',
                'cbgppeer2addrfamilytable',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2CapsTable', REFERENCE_CLASS, 'Cbgppeer2Capstable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Capstable', 
                [], [], 
                '''                This table contains the capabilities that are
                supported by a peer. Capabilities of a peer are
                received during BGP connection establishment.
                Values corresponding to each received capability
                are stored in this table. When a new capability
                is received, this table is updated with a new
                entry. When an existing capability is not received
                during the latest connection establishment, the
                corresponding entry is deleted from the table.
                ''',
                'cbgppeer2capstable',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeer2Table', REFERENCE_CLASS, 'Cbgppeer2Table' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeer2Table', 
                [], [], 
                '''                BGP peer table.  This table contains,
                one entry per BGP peer, information about
                the connections with BGP peers.
                ''',
                'cbgppeer2table',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerAddrFamilyPrefixTable', REFERENCE_CLASS, 'Cbgppeeraddrfamilyprefixtable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable', 
                [], [], 
                '''                This table contains prefix related information
                related to address families supported by a peer. 
                Supported address families of a peer are known 
                during BGP connection establishment. When a new 
                supported address family is known, this table 
                is updated with a new entry. When an address 
                family is not supported any more, corresponding 
                entry is deleted from the table.
                ''',
                'cbgppeeraddrfamilyprefixtable',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerAddrFamilyTable', REFERENCE_CLASS, 'Cbgppeeraddrfamilytable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeeraddrfamilytable', 
                [], [], 
                '''                This table contains information related to
                address families supported by a peer. Supported
                address families of a peer are known during BGP 
                connection establishment. When a new supported 
                address family is known, this table is updated 
                with a new entry. When an address family is not 
                supported any more, corresponding entry is deleted 
                from the table.
                ''',
                'cbgppeeraddrfamilytable',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerCapsTable', REFERENCE_CLASS, 'Cbgppeercapstable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgppeercapstable', 
                [], [], 
                '''                This table contains the capabilities that are
                supported by a peer. Capabilities of a peer are 
                received during BGP connection establishment.
                Values corresponding to each received capability
                are stored in this table. When a new capability 
                is received, this table is updated with a new 
                entry. When an existing capability is not received 
                during the latest connection establishment, the 
                corresponding entry is deleted from the table.
                ''',
                'cbgppeercapstable',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpRouteTable', REFERENCE_CLASS, 'Cbgproutetable' , 'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CiscoBgp4Mib.Cbgproutetable', 
                [], [], 
                '''                This table contains information about routes to
                destination networks from all BGP4 peers.  Since 
                BGP4 can carry routes for multiple Network Layer 
                protocols, this table has the Address Family 
                Identifier(AFI) of the Network Layer protocol as the 
                first index. Further for a given AFI, routes carried
                by BGP4 are distinguished based on Subsequent Address 
                Family Identifiers(SAFI).  Hence that is used as the
                second index.  Conceptually there is a separate Loc-RIB
                maintained by the BGP speaker for each combination of 
                AFI and SAFI supported by it.
                ''',
                'cbgproutetable',
                'CISCO-BGP4-MIB', False),
            ],
            'CISCO-BGP4-MIB',
            'CISCO-BGP4-MIB',
            _yang_ns._namespaces['CISCO-BGP4-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP4_MIB'
        ),
    },
}
_meta_table['CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgproutetable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeercapstable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilytable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeer2Table']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeer2Capstable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilytable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry']['meta_info'].parent =_meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgpglobal']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgproutetable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeercapstable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilytable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Table']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Capstable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilytable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
_meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable']['meta_info'].parent =_meta_table['CiscoBgp4Mib']['meta_info']
