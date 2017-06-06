


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Bgp4Mib.Bgp' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgp',
            False, 
            [
            _MetaInfoClassMember('bgpIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The BGP Identifier of local system.
                ''',
                'bgpidentifier',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpLocalAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local autonomous system number.
                ''',
                'bgplocalas',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpVersion', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Vector of supported BGP protocol version
                numbers.  Each peer negotiates the version
                from this vector.  Versions are identified
                via the string of bits contained within this
                object.  The first octet contains bits 0 to
                7, the second octet contains bits 8 to 15,
                and so on, with the most significant bit
                referring to the lowest bit number in the
                octet (e.g., the MSB of the first octet
                refers to bit 0).  If a bit, i, is present
                and set, then the version (i+1) of the BGP
                is supported.
                ''',
                'bgpversion',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgp',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeeradminstatusEnum' : _MetaInfoEnum('BgppeeradminstatusEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'stop':'stop',
            'start':'start',
        }, 'BGP4-MIB', _yang_ns._namespaces['BGP4-MIB']),
    'Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeerstateEnum' : _MetaInfoEnum('BgppeerstateEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'idle':'idle',
            'connect':'connect',
            'active':'active',
            'opensent':'opensent',
            'openconfirm':'openconfirm',
            'established':'established',
        }, 'BGP4-MIB', _yang_ns._namespaces['BGP4-MIB']),
    'Bgp4Mib.Bgppeertable.Bgppeerentry.CbgppeerprevstateEnum' : _MetaInfoEnum('CbgppeerprevstateEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'none':'none',
            'idle':'idle',
            'connect':'connect',
            'active':'active',
            'opensent':'opensent',
            'openconfirm':'openconfirm',
            'established':'established',
        }, 'CISCO-BGP4-MIB', _yang_ns._namespaces['CISCO-BGP4-MIB']),
    'Bgp4Mib.Bgppeertable.Bgppeerentry' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgppeertable.Bgppeerentry',
            False, 
            [
            _MetaInfoClassMember('bgpPeerRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The remote IP address of this entry's BGP
                peer.
                ''',
                'bgppeerremoteaddr',
                'BGP4-MIB', True),
            _MetaInfoClassMember('bgpPeerAdminStatus', REFERENCE_ENUM_CLASS, 'BgppeeradminstatusEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeeradminstatusEnum', 
                [], [], 
                '''                The desired state of the BGP connection.
                A transition from 'stop' to 'start' will
                cause the BGP Start Event to be generated.
                A transition from 'start' to 'stop' will
                cause the BGP Stop Event to be generated.
                This parameter can be used to restart BGP
                peer connections.  Care should be used in
                providing write access to this object
                without adequate authentication.
                ''',
                'bgppeeradminstatus',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerConnectRetryInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval in seconds for the
                ConnectRetry timer.  The suggested value
                for this timer is 120 seconds.
                ''',
                'bgppeerconnectretryinterval',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerFsmEstablishedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This timer indicates how long (in
                seconds) this peer has been in the
                Established state or how long
                since this peer was last in the
                Established state.  It is set to zero when
                a new peer is configured or the router is
                booted.
                ''',
                'bgppeerfsmestablishedtime',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerFsmEstablishedTransitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times the BGP FSM
                transitioned into the established state.
                ''',
                'bgppeerfsmestablishedtransitions',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('3', '65535')], [], 
                '''                Time interval in seconds for the Hold
                Timer established with the peer.  The
                value of this object is calculated by this
                BGP speaker by using the smaller of the
                value in bgpPeerHoldTimeConfigured and the
                Hold Time received in the OPEN message.
                This value must be at lease three seconds
                if it is not zero (0) in which case the
                Hold Timer has not been established with
                the peer, or, the value of
                bgpPeerHoldTimeConfigured is zero (0).
                ''',
                'bgppeerholdtime',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerHoldTimeConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('3', '65535')], [], 
                '''                Time interval in seconds for the Hold Time
                configured for this BGP speaker with this
                peer.  This value is placed in an OPEN
                message sent to this peer by this BGP
                speaker, and is compared with the Hold
                Time field in an OPEN message received
                from the peer when determining the Hold
                Time (bgpPeerHoldTime) with the peer.
                This value must not be less than three
                seconds if it is not zero (0) in which
                case the Hold Time is NOT to be
                established with the peer.  The suggested
                value for this timer is 90 seconds.
                ''',
                'bgppeerholdtimeconfigured',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The BGP Identifier of this entry's BGP
                peer.
                ''',
                'bgppeeridentifier',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerInTotalMessages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of messages received
                from the remote peer on this connection.
                This object should be initialized to zero
                when the connection is established.
                ''',
                'bgppeerintotalmessages',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerInUpdateElapsedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Elapsed time in seconds since the last BGP
                UPDATE message was received from the peer.
                Each time bgpPeerInUpdates is incremented,
                the value of this object is set to zero
                (0).
                ''',
                'bgppeerinupdateelapsedtime',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerInUpdates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of BGP UPDATE messages
                received on this connection.  This object
                should be initialized to zero (0) when the
                connection is established.
                ''',
                'bgppeerinupdates',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerKeepAlive', ATTRIBUTE, 'int' , None, None, 
                [('0', '21845')], [], 
                '''                Time interval in seconds for the KeepAlive
                timer established with the peer.  The value
                of this object is calculated by this BGP
                speaker such that, when compared with
                bgpPeerHoldTime, it has the same
                proportion as what
                bgpPeerKeepAliveConfigured has when
                compared with bgpPeerHoldTimeConfigured.
                If the value of this object is zero (0),
                it indicates that the KeepAlive timer has
                not been established with the peer, or,
                the value of bgpPeerKeepAliveConfigured is
                zero (0).
                ''',
                'bgppeerkeepalive',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerKeepAliveConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', '21845')], [], 
                '''                Time interval in seconds for the
                KeepAlive timer configured for this BGP
                speaker with this peer.  The value of this
                object will only determine the
                KEEPALIVE messages' frequency relative to
                the value specified in
                bgpPeerHoldTimeConfigured; the actual
                time interval for the KEEPALIVE messages
                is indicated by bgpPeerKeepAlive.  A
                reasonable maximum value for this timer
                would be configured to be one
                third of that of
                bgpPeerHoldTimeConfigured.
                If the value of this object is zero (0),
                no periodical KEEPALIVE messages are sent
                to the peer after the BGP connection has
                been established.  The suggested value for
                this timer is 30 seconds.
                ''',
                'bgppeerkeepaliveconfigured',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerLastError', ATTRIBUTE, 'str' , None, None, 
                [(2, None)], [], 
                '''                The last error code and subcode seen by this
                peer on this connection.  If no error has
                occurred, this field is zero.  Otherwise, the
                first byte of this two byte OCTET STRING
                contains the error code, and the second byte
                contains the subcode.
                ''',
                'bgppeerlasterror',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address of this entry's BGP
                connection.
                ''',
                'bgppeerlocaladdr',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port for the TCP connection
                between the BGP peers.
                ''',
                'bgppeerlocalport',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerMinASOriginationInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval in seconds for the
                MinASOriginationInterval timer.
                The suggested value for this timer is 15
                seconds.
                ''',
                'bgppeerminasoriginationinterval',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerMinRouteAdvertisementInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval in seconds for the
                MinRouteAdvertisementInterval timer.
                The suggested value for this timer is 30
                seconds.
                ''',
                'bgppeerminrouteadvertisementinterval',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerNegotiatedVersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The negotiated version of BGP running
                between the two peers.
                ''',
                'bgppeernegotiatedversion',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerOutTotalMessages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of messages transmitted to
                the remote peer on this connection.  This
                object should be initialized to zero when
                the connection is established.
                ''',
                'bgppeerouttotalmessages',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerOutUpdates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of BGP UPDATE messages
                transmitted on this connection.  This
                object should be initialized to zero (0)
                when the connection is established.
                ''',
                'bgppeeroutupdates',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerRemoteAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote autonomous system number.
                ''',
                'bgppeerremoteas',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerRemotePort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote port for the TCP connection
                between the BGP peers.  Note that the
                objects bgpPeerLocalAddr,
                bgpPeerLocalPort, bgpPeerRemoteAddr and
                bgpPeerRemotePort provide the appropriate
                reference to the standard MIB TCP
                connection table.
                ''',
                'bgppeerremoteport',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerState', REFERENCE_ENUM_CLASS, 'BgppeerstateEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgppeertable.Bgppeerentry.BgppeerstateEnum', 
                [], [], 
                '''                The BGP peer connection state.
                ''',
                'bgppeerstate',
                'BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerLastErrorTxt', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Implementation specific error description for
                bgpPeerLastErrorReceived.
                ''',
                'cbgppeerlasterrortxt',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixAccepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Route prefixes received on this connnection,
                which are accepted after applying filters. Possible
                filters are route maps, prefix lists, distributed
                lists, etc.
                ''',
                'cbgppeerprefixaccepted',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixAdvertised', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Counter which gets incremented when a route prefix
                is advertised on this connection. This object is
                initialized to zero when the peer is configured or 
                the router is rebooted
                ''',
                'cbgppeerprefixadvertised',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixDenied', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Counter which gets incremented when a route prefix
                received on this connection is denied  or when a route
                prefix is denied during soft reset of this connection
                if 'soft-reconfiguration' is on . This object is 
                initialized to zero when the peer is  configured or
                the router is rebooted
                ''',
                'cbgppeerprefixdenied',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixLimit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Max number of route prefixes accepted on this
                connection
                ''',
                'cbgppeerprefixlimit',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixSuppressed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Counter which gets incremented when a route prefix
                is suppressed from being sent on this connection. This 
                object is initialized to zero when the peer is 
                configured or the router is rebooted
                ''',
                'cbgppeerprefixsuppressed',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrefixWithdrawn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Counter which gets incremented when a route prefix
                is withdrawn on this connection. This object is
                initialized to zero when the peer is configured or
                the router is rebooted
                ''',
                'cbgppeerprefixwithdrawn',
                'CISCO-BGP4-MIB', False),
            _MetaInfoClassMember('cbgpPeerPrevState', REFERENCE_ENUM_CLASS, 'CbgppeerprevstateEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgppeertable.Bgppeerentry.CbgppeerprevstateEnum', 
                [], [], 
                '''                The BGP peer connection previous state.
                ''',
                'cbgppeerprevstate',
                'CISCO-BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgpPeerEntry',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib.Bgppeertable' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgppeertable',
            False, 
            [
            _MetaInfoClassMember('bgpPeerEntry', REFERENCE_LIST, 'Bgppeerentry' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgppeertable.Bgppeerentry', 
                [], [], 
                '''                Entry containing information about the
                connection with a BGP peer.
                ''',
                'bgppeerentry',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgpPeerTable',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry.BgppathattroriginEnum' : _MetaInfoEnum('BgppathattroriginEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'igp':'igp',
            'egp':'egp',
            'incomplete':'incomplete',
        }, 'BGP4-MIB', _yang_ns._namespaces['BGP4-MIB']),
    'Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry',
            False, 
            [
            _MetaInfoClassMember('bgpPathAttrDestNetwork', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the destination network.
                ''',
                'bgppathattrdestnetwork',
                'BGP4-MIB', True),
            _MetaInfoClassMember('bgpPathAttrPeer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the peer where the path
                information was learned.
                ''',
                'bgppathattrpeer',
                'BGP4-MIB', True),
            _MetaInfoClassMember('bgpPathAttrASPath', ATTRIBUTE, 'str' , None, None, 
                [(2, 255)], [], 
                '''                The set of ASs that must be traversed to
                reach the network.  This object is
                probably best represented as SEQUENCE OF
                INTEGER.  For SMI compatibility, though,
                it is represented as OCTET STRING.  Each
                AS is represented as a pair of octets
                according to the following algorithm:
                
                    first-byte-of-pair = ASNumber / 256;
                    second-byte-of-pair = ASNumber & 255;
                ''',
                'bgppathattraspath',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPathAttrInterASMetric', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The optional inter-AS metric.  If this
                attribute has not been provided for this
                route, the value for this object is 0.
                ''',
                'bgppathattrinterasmetric',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPathAttrNextHop', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the border router that
                should be used for the destination
                network.
                ''',
                'bgppathattrnexthop',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPathAttrOrigin', REFERENCE_ENUM_CLASS, 'BgppathattroriginEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry.BgppathattroriginEnum', 
                [], [], 
                '''                The ultimate origin of the path information.
                ''',
                'bgppathattrorigin',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgpPathAttrEntry',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib.Bgprcvdpathattrtable' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgprcvdpathattrtable',
            False, 
            [
            _MetaInfoClassMember('bgpPathAttrEntry', REFERENCE_LIST, 'Bgppathattrentry' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry', 
                [], [], 
                '''                Information about a path to a network.
                ''',
                'bgppathattrentry',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgpRcvdPathAttrTable',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattratomicaggregateEnum' : _MetaInfoEnum('Bgp4PathattratomicaggregateEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'lessSpecificRrouteNotSelected':'lessSpecificRrouteNotSelected',
            'lessSpecificRouteSelected':'lessSpecificRouteSelected',
        }, 'BGP4-MIB', _yang_ns._namespaces['BGP4-MIB']),
    'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattrbestEnum' : _MetaInfoEnum('Bgp4PathattrbestEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'false':'false',
            'true':'true',
        }, 'BGP4-MIB', _yang_ns._namespaces['BGP4-MIB']),
    'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattroriginEnum' : _MetaInfoEnum('Bgp4PathattroriginEnum', 'ydk.models.cisco_ios_xe.BGP4_MIB',
        {
            'igp':'igp',
            'egp':'egp',
            'incomplete':'incomplete',
        }, 'BGP4-MIB', _yang_ns._namespaces['BGP4-MIB']),
    'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry',
            False, 
            [
            _MetaInfoClassMember('bgp4PathAttrIpAddrPrefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address prefix in the Network Layer
                Reachability Information field.  This object
                is an IP address containing the prefix with
                length specified by
                bgp4PathAttrIpAddrPrefixLen.
                Any bits beyond the length specified by
                bgp4PathAttrIpAddrPrefixLen are zeroed.
                ''',
                'bgp4pathattripaddrprefix',
                'BGP4-MIB', True),
            _MetaInfoClassMember('bgp4PathAttrIpAddrPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Length in bits of the IP address prefix
                in the Network Layer Reachability
                Information field.
                ''',
                'bgp4pathattripaddrprefixlen',
                'BGP4-MIB', True),
            _MetaInfoClassMember('bgp4PathAttrPeer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the peer where the path
                information was learned.
                ''',
                'bgp4pathattrpeer',
                'BGP4-MIB', True),
            _MetaInfoClassMember('bgp4PathAttrAggregatorAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the last BGP4 speaker
                that performed route aggregation.  A value
                of 0.0.0.0 indicates the absence of this
                attribute.
                ''',
                'bgp4pathattraggregatoraddr',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrAggregatorAS', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The AS number of the last BGP4 speaker that
                performed route aggregation.  A value of
                zero (0) indicates the absence of this
                attribute.
                ''',
                'bgp4pathattraggregatoras',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrASPathSegment', ATTRIBUTE, 'str' , None, None, 
                [(2, 255)], [], 
                '''                The sequence of AS path segments.  Each AS
                path segment is represented by a triple
                <type, length, value>.
                
                The type is a 1-octet field which has two
                possible values:
                     1      AS_SET: unordered set of ASs a
                                 route in the UPDATE
                                 message has traversed
                     2      AS_SEQUENCE: ordered set of ASs
                                 a route in the UPDATE
                                 message has traversed.
                
                The length is a 1-octet field containing the
                number of ASs in the value field.
                
                The value field contains one or more AS
                numbers, each AS is represented in the octet
                string as a pair of octets according to the
                following algorithm:
                
                    first-byte-of-pair = ASNumber / 256;
                    second-byte-of-pair = ASNumber & 255;
                ''',
                'bgp4pathattraspathsegment',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrAtomicAggregate', REFERENCE_ENUM_CLASS, 'Bgp4PathattratomicaggregateEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattratomicaggregateEnum', 
                [], [], 
                '''                Whether or not the local system has
                selected a less specific route without
                selecting a more specific route.
                ''',
                'bgp4pathattratomicaggregate',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrBest', REFERENCE_ENUM_CLASS, 'Bgp4PathattrbestEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattrbestEnum', 
                [], [], 
                '''                An indication of whether or not this route
                was chosen as the best BGP4 route.
                ''',
                'bgp4pathattrbest',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrCalcLocalPref', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The degree of preference calculated by the
                receiving BGP4 speaker for an advertised
                route.  A value of -1 indicates the
                absence of this attribute.
                ''',
                'bgp4pathattrcalclocalpref',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrLocalPref', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The originating BGP4 speaker's degree of
                preference for an advertised route.  A
                value of -1 indicates the absence of this
                attribute.
                ''',
                'bgp4pathattrlocalpref',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrMultiExitDisc', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                This metric is used to discriminate
                between multiple exit points to an
                adjacent autonomous system.  A value of -1
                indicates the absence of this attribute.
                ''',
                'bgp4pathattrmultiexitdisc',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrNextHop', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the border router that
                should be used for the destination
                network.
                ''',
                'bgp4pathattrnexthop',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrOrigin', REFERENCE_ENUM_CLASS, 'Bgp4PathattroriginEnum' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry.Bgp4PathattroriginEnum', 
                [], [], 
                '''                The ultimate origin of the path
                information.
                ''',
                'bgp4pathattrorigin',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrUnknown', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                One or more path attributes not understood
                by this BGP4 speaker.  Size zero (0)
                indicates the absence of such
                attribute(s).  Octets beyond the maximum
                size, if any, are not recorded by this
                object.
                ''',
                'bgp4pathattrunknown',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgp4PathAttrEntry',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib.Bgp4Pathattrtable' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib.Bgp4Pathattrtable',
            False, 
            [
            _MetaInfoClassMember('bgp4PathAttrEntry', REFERENCE_LIST, 'Bgp4Pathattrentry' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry', 
                [], [], 
                '''                Information about a path to a network.
                ''',
                'bgp4pathattrentry',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'bgp4PathAttrTable',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
    'Bgp4Mib' : {
        'meta_info' : _MetaInfoClass('Bgp4Mib',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgp', 
                [], [], 
                '''                ''',
                'bgp',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgp4PathAttrTable', REFERENCE_CLASS, 'Bgp4Pathattrtable' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgp4Pathattrtable', 
                [], [], 
                '''                The BGP-4 Received Path Attribute Table
                contains information about paths to
                destination networks received from all
                BGP4 peers.
                ''',
                'bgp4pathattrtable',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpPeerTable', REFERENCE_CLASS, 'Bgppeertable' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgppeertable', 
                [], [], 
                '''                BGP peer table.  This table contains,
                one entry per BGP peer, information about
                the connections with BGP peers.
                ''',
                'bgppeertable',
                'BGP4-MIB', False),
            _MetaInfoClassMember('bgpRcvdPathAttrTable', REFERENCE_CLASS, 'Bgprcvdpathattrtable' , 'ydk.models.cisco_ios_xe.BGP4_MIB', 'Bgp4Mib.Bgprcvdpathattrtable', 
                [], [], 
                '''                The BGP Received Path Attribute Table
                contains information about paths to
                destination networks received from all
                peers running BGP version 3 or less.
                ''',
                'bgprcvdpathattrtable',
                'BGP4-MIB', False),
            ],
            'BGP4-MIB',
            'BGP4-MIB',
            _yang_ns._namespaces['BGP4-MIB'],
        'ydk.models.cisco_ios_xe.BGP4_MIB'
        ),
    },
}
_meta_table['Bgp4Mib.Bgppeertable.Bgppeerentry']['meta_info'].parent =_meta_table['Bgp4Mib.Bgppeertable']['meta_info']
_meta_table['Bgp4Mib.Bgprcvdpathattrtable.Bgppathattrentry']['meta_info'].parent =_meta_table['Bgp4Mib.Bgprcvdpathattrtable']['meta_info']
_meta_table['Bgp4Mib.Bgp4Pathattrtable.Bgp4Pathattrentry']['meta_info'].parent =_meta_table['Bgp4Mib.Bgp4Pathattrtable']['meta_info']
_meta_table['Bgp4Mib.Bgp']['meta_info'].parent =_meta_table['Bgp4Mib']['meta_info']
_meta_table['Bgp4Mib.Bgppeertable']['meta_info'].parent =_meta_table['Bgp4Mib']['meta_info']
_meta_table['Bgp4Mib.Bgprcvdpathattrtable']['meta_info'].parent =_meta_table['Bgp4Mib']['meta_info']
_meta_table['Bgp4Mib.Bgp4Pathattrtable']['meta_info'].parent =_meta_table['Bgp4Mib']['meta_info']
