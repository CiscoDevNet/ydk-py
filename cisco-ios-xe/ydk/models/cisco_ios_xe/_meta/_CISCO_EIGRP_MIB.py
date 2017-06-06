


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry',
            False, 
            [
            _MetaInfoClassMember('cEigrpVpnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The unique VPN identifier.  This is a unique integer
                relative to all other VPN's defined on the router.  It
                also identifies internally the routing table instance.
                ''',
                'ceigrpvpnid',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpVpnName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name given to the VPN.
                ''',
                'ceigrpvpnname',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpVpnEntry',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrpvpntable' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrpvpntable',
            False, 
            [
            _MetaInfoClassMember('cEigrpVpnEntry', REFERENCE_LIST, 'Ceigrpvpnentry' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry', 
                [], [], 
                '''                Information relating to a single VPN which is configured
                to run EIGRP.
                ''',
                'ceigrpvpnentry',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpVpnTable',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry',
            False, 
            [
            _MetaInfoClassMember('cEigrpVpnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpvpnid',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Autonomous System number which is unique integer
                per VPN.
                ''',
                'ceigrpasnumber',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpAcksRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number packet acknowledgements that have been
                received from all EIGRP neighbors formed on all interfaces
                whose IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpacksrcvd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpAcksSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number packet acknowledgements that have been
                sent to all EIGRP neighbors formed on all interfaces whose
                IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpackssent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpAsRouterId', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The router-id configured or automatically selected for the
                EIGRP AS.   Each EIGRP routing process has a unique
                router-id selected from each autonomous system configured.
                The format is governed by object cEigrpAsRouterIdType.
                ''',
                'ceigrpasrouterid',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpAsRouterIdType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The format of the router-id configured or automatically
                selected for the EIGRP AS.
                ''',
                'ceigrpasrouteridtype',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpHeadSerial', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Routes in a topology table for an AS are assigned serial
                numbers and are sequenced internally as they are inserted
                and deleted.   The serial number of the first route in
                that internal sequence is called the head serial number.
                Each AS has its own topology table, and its own serial
                number space, each of which begins with the value 1.
                A serial number of zero implies that there are no routes
                in the topology.
                ''',
                'ceigrpheadserial',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpHellosRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number Hello packets that have been received
                from all EIGRP neighbors formed on all interfaces whose IP
                addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrphellosrcvd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpHellosSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number Hello packets that have been sent to all
                EIGRP neighbors formed on all interfaces whose IP addresses
                fall under networks configured for the EIGRP AS.
                ''',
                'ceigrphellossent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpInputQDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of EIGRP packets dropped from the input
                queue due to it being full within the AS.
                ''',
                'ceigrpinputqdrops',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpInputQHighMark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The highest number of EIGRP packets in the input queue
                waiting to be processed internally addressed to this
                AS.
                ''',
                'ceigrpinputqhighmark',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpNbrCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of live EIGRP neighbors formed on all
                interfaces whose IP addresses fall under networks configured
                in the EIGRP AS.
                ''',
                'ceigrpnbrcount',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpNextSerial', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The serial number that would be assigned to the next new
                or changed route in the topology table for the AS.
                ''',
                'ceigrpnextserial',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpQueriesRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number alternate route query packets that
                have been received from all EIGRP neighbors formed on
                all interfaces whose IP addresses fall under networks
                configured for the EIGRP AS.
                ''',
                'ceigrpqueriesrcvd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpQueriesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number alternate route query packets that have
                been sent to all EIGRP neighbors formed on all interfaces
                whose IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpqueriessent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRepliesRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number query reply packets that have been
                received from all EIGRP neighbors formed on all interfaces
                whose IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrprepliesrcvd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRepliesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number query reply packets that have been sent
                to all EIGRP neighbors formed on all interfaces whose IP
                addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrprepliessent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpSiaQueriesRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Stuck-In-Active (SIA) query packets
                received from all EIGRP neighbors formed on all interfaces
                whose IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpsiaqueriesrcvd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpSiaQueriesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Stuck-In-Active (SIA) query packets
                sent to all EIGRP neighbors formed on all interfaces whose
                IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpsiaqueriessent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpTopoRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of EIGRP derived routes currently existing
                in the topology table for the AS.
                ''',
                'ceigrptoporoutes',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpUpdatesRcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number routing update packets that have been
                received from all EIGRP neighbors formed on all interfaces
                whose IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpupdatesrcvd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpUpdatesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number routing update packets that have been
                sent to all EIGRP neighbors formed on all interfaces whose
                IP addresses fall under networks configured for the
                EIGRP AS.
                ''',
                'ceigrpupdatessent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpXmitDummies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A dummy is a temporary internal entity used as a place
                holder in the topology table for an AS. They are not
                transmitted in routing updates.  This is the total
                number currently in existence associated with the AS.
                ''',
                'ceigrpxmitdummies',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpXmitPendReplies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When alternate route query packets are sent to adjacent
                EIGRP peers in an AS, replies are expected.   This object
                is the total number of outstanding replies expected to
                queries that have been sent to peers in the current AS.
                It remains at zero most of the time until an EIGRP route
                becomes active.
                ''',
                'ceigrpxmitpendreplies',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpTraffStatsEntry',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrptraffstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrptraffstatstable',
            False, 
            [
            _MetaInfoClassMember('cEigrpTraffStatsEntry', REFERENCE_LIST, 'Ceigrptraffstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry', 
                [], [], 
                '''                The set of statistics and information for a single EIGRP
                Autonomous System.
                ''',
                'ceigrptraffstatsentry',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpTraffStatsTable',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry',
            False, 
            [
            _MetaInfoClassMember('cEigrpVpnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpvpnid',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpasnumber',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpDestNetType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The format of the destination IP network number for
                a single route in the topology table in the AS specified
                in cEigrpDestNet.
                ''',
                'ceigrpdestnettype',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpDestNet', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The destination IP network number for a single route in
                the topology table in the AS.  The format is governed
                by object cEigrpDestNetType.
                ''',
                'ceigrpdestnet',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpDestNetPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The prefix length associated with the destination IP
                network address for a single route in the topology
                table in the AS.  The format is governed by the object
                cEigrpDestNetType.
                ''',
                'ceigrpdestnetprefixlen',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpActive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A value of true(1) indicates the route to the
                destination network has failed and an active (query)
                search for an alternative path is in progress.  A value
                of false(2) indicates the route is stable (passive).
                ''',
                'ceigrpactive',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpDestSuccessors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A successor is the next routing hop for a path to the
                destination IP network number for a single route in the
                topology table in the AS.  There can be several
                potential successors if there are multiple paths to the
                destination.   This is the total number of successors for
                a topology entry.
                ''',
                'ceigrpdestsuccessors',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpDistance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The computed distance to the destination network entry
                from this router.
                ''',
                'ceigrpdistance',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpFdistance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The feasibility (best) distance is the minimum distance
                from this router to the destination IP network in
                this topology entry.  The feasibility distance is
                used in determining the best successor for a path to the
                destination network.
                ''',
                'ceigrpfdistance',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpNextHopAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This is the next hop IP address for the route represented
                by the topology entry.   The next hop is where
                network traffic will be routed to in order to reach
                the destination network for this topology entry.  The
                format is governed by cEigrpNextHopAddressType.
                ''',
                'ceigrpnexthopaddress',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpNextHopAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The format of the next hop IP address for the route
                represented by the topology entry.
                ''',
                'ceigrpnexthopaddresstype',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpNextHopInterface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface through which the next hop IP address
                is reached to send network traffic to the destination
                network represented by the topology entry.
                ''',
                'ceigrpnexthopinterface',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpReportDistance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The computed distance to the destination network in the
                topology entry reported to this router by the originator
                of this route.
                ''',
                'ceigrpreportdistance',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRouteOriginAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                If the origin of the topology route entry is external
                to this router, then this object is the IP address
                of the router from which it originated.  The format 
                is governed by object cEigrpRouteOriginAddrType.
                ''',
                'ceigrprouteoriginaddr',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRouteOriginAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The format of the IP address defined as the origin of
                this topology route entry.
                ''',
                'ceigrprouteoriginaddrtype',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRouteOriginType', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is a text string describing the internal origin
                of the EIGRP route represented by the topology entry.
                ''',
                'ceigrprouteorigintype',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpStuckInActive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A value of true(1) indicates that that this route which is
                in active state (cEigrpActive = true(1)) has not received
                any replies to queries for alternate paths, and a second
                EIGRP route query, called a stuck-in-active query, has
                now been sent.
                ''',
                'ceigrpstuckinactive',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpTopoEntry',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrptopotable' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrptopotable',
            False, 
            [
            _MetaInfoClassMember('cEigrpTopoEntry', REFERENCE_LIST, 'Ceigrptopoentry' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry', 
                [], [], 
                '''                The entry for a single EIGRP topology table in the given
                AS.
                ''',
                'ceigrptopoentry',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpTopoTable',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry',
            False, 
            [
            _MetaInfoClassMember('cEigrpVpnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpvpnid',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpasnumber',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpHandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The unique internal identifier for the peer in the AS.
                This is a unique value among peer entries in a selected
                table.
                ''',
                'ceigrphandle',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count-down timer indicating how much time must
                pass without receiving a hello packet from this
                EIGRP peer before this router declares the peer down.
                A peer declared as down is removed from the table and
                is no longer visible.
                ''',
                'ceigrpholdtime',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpLastSeq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                All transmitted EIGRP packets have a sequence number
                assigned. This is the sequence number of the last EIGRP
                packet sent to this peer.
                ''',
                'ceigrplastseq',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPeerAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The source IP address used by the peer to establish the
                EIGRP adjacency with this router.  The format is
                governed by object cEigrpPeerAddrType.
                ''',
                'ceigrppeeraddr',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPeerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The format of the remote source IP address used by the
                peer to establish the EIGRP adjacency with this router.
                ''',
                'ceigrppeeraddrtype',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPeerIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The ifIndex of the interface on this router through
                which this peer can be reached.
                ''',
                'ceigrppeerifindex',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPktsEnqueued', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of any EIGRP packets currently enqueued
                waiting to be sent to this peer.
                ''',
                'ceigrppktsenqueued',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRetrans', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cumulative number of retransmissions to this peer
                during the period that the peer adjacency has remained
                up.
                ''',
                'ceigrpretrans',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the current unacknowledged packet
                has been retried, i.e. resent to this peer to be
                acknowledged.
                ''',
                'ceigrpretries',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRto', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The computed retransmission timeout for the peer.
                This value is computed over time as packets are sent to
                the peer and acknowledgements are received from it,
                and is the amount of time to wait before resending
                a packet from the retransmission queue to the peer
                when an expected acknowledgement has not been received.
                ''',
                'ceigrprto',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpSrtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The computed smooth round trip time for packets to and
                from the peer.
                ''',
                'ceigrpsrtt',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpUpTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The elapsed time since the EIGRP adjacency was first
                established with the peer.
                ''',
                'ceigrpuptime',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpVersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The EIGRP version information reported by the remote
                peer.
                ''',
                'ceigrpversion',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpPeerEntry',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrppeertable' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrppeertable',
            False, 
            [
            _MetaInfoClassMember('cEigrpPeerEntry', REFERENCE_LIST, 'Ceigrppeerentry' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry', 
                [], [], 
                '''                Statistics and operational parameters for a single peer
                in the AS.
                ''',
                'ceigrppeerentry',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpPeerTable',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry.CeigrpauthmodeEnum' : _MetaInfoEnum('CeigrpauthmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB',
        {
            'none':'none',
            'md5':'md5',
        }, 'CISCO-EIGRP-MIB', _yang_ns._namespaces['CISCO-EIGRP-MIB']),
    'CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry',
            False, 
            [
            _MetaInfoClassMember('cEigrpVpnId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpvpnid',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ceigrpasnumber',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-EIGRP-MIB', True),
            _MetaInfoClassMember('cEigrpAcksSuppressed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of individual EIGRP acknowledgement
                packets that have been suppressed and combined in
                an already enqueued outbound reliable packet on this
                interface.
                ''',
                'ceigrpackssuppressed',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpAuthKeyChain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the authentication key-chain configured
                on this interface.   The key-chain is a reference to
                which set of secret keys are to be accessed in order
                to determine which secret key string to use.  The key
                chain name is not the secret key string password and
                can also be used in other routing protocols, such
                as RIP and ISIS.
                ''',
                'ceigrpauthkeychain',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpAuthMode', REFERENCE_ENUM_CLASS, 'CeigrpauthmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry.CeigrpauthmodeEnum', 
                [], [], 
                '''                The EIGRP authentication mode of the interface.
                none  :  no authentication enabled on the interface
                md5   :  MD5 authentication enabled on the interface
                ''',
                'ceigrpauthmode',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpCRpkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number EIGRP Conditional-Receive packets sent on
                this interface.
                ''',
                'ceigrpcrpkts',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpHelloInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The configured time interval between Hello packet
                transmissions for this interface.
                ''',
                'ceigrphellointerval',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpMcastExcepts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of EIGRP multicast exception
                transmissions that have occurred on this interface.
                ''',
                'ceigrpmcastexcepts',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpMeanSrtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The average of all the computed smooth round trip time
                values for a packet to and from all peers established on
                this interface.
                ''',
                'ceigrpmeansrtt',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpMFlowTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The configured multicast flow control timer value for
                this interface.
                ''',
                'ceigrpmflowtimer',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpOOSrvcd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of out-of-sequence EIGRP packets
                received.
                ''',
                'ceigrpoosrvcd',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPacingReliable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The configured time interval between EIGRP packet
                transmissions on the interface when the reliable transport
                method is used.
                ''',
                'ceigrppacingreliable',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPacingUnreliable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The configured time interval between EIGRP packet
                transmissions on the interface when the unreliable
                transport method is used.
                ''',
                'ceigrppacingunreliable',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPeerCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of EIGRP adjacencies currently formed with
                peers reached through this interface.
                ''',
                'ceigrppeercount',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPendingRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of queued EIGRP routing updates awaiting
                transmission on this interface.
                ''',
                'ceigrppendingroutes',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRetransSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number EIGRP packet retransmissions sent on
                the interface.
                ''',
                'ceigrpretranssent',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRMcasts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of reliable (acknowledgement required)
                EIGRP multicast packets sent on this interface.
                ''',
                'ceigrprmcasts',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpRUcasts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of reliable (acknowledgement required)
                unicast packets sent on this interface.
                ''',
                'ceigrprucasts',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpUMcasts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of unreliable (no acknowledgement
                required) EIGRP multicast packets sent on this
                interface.
                ''',
                'ceigrpumcasts',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpUUcasts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of unreliable (no acknowledgement
                required) EIGRP unicast packets sent on this
                interface.
                ''',
                'ceigrpuucasts',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpXmitNextSerial', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The serial number of the next EIGRP packet that is to
                be queued for transmission on this interface.
                ''',
                'ceigrpxmitnextserial',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpXmitReliableQ', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of EIGRP packets currently waiting in the
                reliable transport (acknowledgement-required) 
                transmission queue to be sent to a peer.
                ''',
                'ceigrpxmitreliableq',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpXmitUnreliableQ', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number EIGRP of packets currently waiting in
                the unreliable transport (no acknowledgement required)
                transmission queue.
                ''',
                'ceigrpxmitunreliableq',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpInterfaceEntry',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib.Ceigrpinterfacetable' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib.Ceigrpinterfacetable',
            False, 
            [
            _MetaInfoClassMember('cEigrpInterfaceEntry', REFERENCE_LIST, 'Ceigrpinterfaceentry' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry', 
                [], [], 
                '''                Information for a single interface running EIGRP in the
                AS and VPN.
                ''',
                'ceigrpinterfaceentry',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'cEigrpInterfaceTable',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
    'CiscoEigrpMib' : {
        'meta_info' : _MetaInfoClass('CiscoEigrpMib',
            False, 
            [
            _MetaInfoClassMember('cEigrpInterfaceTable', REFERENCE_CLASS, 'Ceigrpinterfacetable' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrpinterfacetable', 
                [], [], 
                '''                The table of interfaces over which EIGRP is running, and
                their associated statistics.   This table is independent
                of whether any peer adjacencies have been formed over
                the interfaces or not.   Interfaces running EIGRP are
                determined by whether their assigned IP addresses fall
                within configured EIGRP network statements.
                ''',
                'ceigrpinterfacetable',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpPeerTable', REFERENCE_CLASS, 'Ceigrppeertable' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrppeertable', 
                [], [], 
                '''                The table of established EIGRP peers (neighbors) in the
                selected autonomous system.   Peers are indexed by their
                unique internal handle id, as well as the AS number and
                VPN id.   The peer entry is removed from the table if
                the peer is declared down.
                ''',
                'ceigrppeertable',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpTopoTable', REFERENCE_CLASS, 'Ceigrptopotable' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrptopotable', 
                [], [], 
                '''                The table of EIGRP routes and their associated
                attributes for an Autonomous System (AS) configured
                in a VPN is called a topology table.  All route entries in
                the topology table will be indexed by IP network type,
                IP network number and network mask (prefix) size.
                ''',
                'ceigrptopotable',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpTraffStatsTable', REFERENCE_CLASS, 'Ceigrptraffstatstable' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrptraffstatstable', 
                [], [], 
                '''                Table of EIGRP traffic statistics and information
                associated with all EIGRP autonomous systems.
                ''',
                'ceigrptraffstatstable',
                'CISCO-EIGRP-MIB', False),
            _MetaInfoClassMember('cEigrpVpnTable', REFERENCE_CLASS, 'Ceigrpvpntable' , 'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CiscoEigrpMib.Ceigrpvpntable', 
                [], [], 
                '''                This table contains information on those VPN's configured
                to run EIGRP.  The VPN creation on a router is independent
                of the routing protocol to be used over it.   A VPN is
                given a name and has a dedicated routing table associated
                with it.  This routing table is identified internally
                by a unique integer value.
                ''',
                'ceigrpvpntable',
                'CISCO-EIGRP-MIB', False),
            ],
            'CISCO-EIGRP-MIB',
            'CISCO-EIGRP-MIB',
            _yang_ns._namespaces['CISCO-EIGRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB'
        ),
    },
}
_meta_table['CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry']['meta_info'].parent =_meta_table['CiscoEigrpMib.Ceigrpvpntable']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry']['meta_info'].parent =_meta_table['CiscoEigrpMib.Ceigrptraffstatstable']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry']['meta_info'].parent =_meta_table['CiscoEigrpMib.Ceigrptopotable']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry']['meta_info'].parent =_meta_table['CiscoEigrpMib.Ceigrppeertable']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry']['meta_info'].parent =_meta_table['CiscoEigrpMib.Ceigrpinterfacetable']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrpvpntable']['meta_info'].parent =_meta_table['CiscoEigrpMib']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrptraffstatstable']['meta_info'].parent =_meta_table['CiscoEigrpMib']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrptopotable']['meta_info'].parent =_meta_table['CiscoEigrpMib']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrppeertable']['meta_info'].parent =_meta_table['CiscoEigrpMib']['meta_info']
_meta_table['CiscoEigrpMib.Ceigrpinterfacetable']['meta_info'].parent =_meta_table['CiscoEigrpMib']['meta_info']
