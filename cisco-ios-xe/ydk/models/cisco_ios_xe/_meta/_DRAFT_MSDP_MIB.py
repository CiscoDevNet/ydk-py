


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DraftMsdpMib.Msdp' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdp',
            False, 
            [
            _MetaInfoClassMember('msdpCacheLifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The lifetime given to SA cache entries when created
                or refreshed.  A value of 0 means no SA caching is
                done by this MSDP speaker.
                ''',
                'msdpcachelifetime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The state of MSDP on this MSDP speaker - globally
                enabled or disabled.
                ''',
                'msdpenabled',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpNumSACacheEntries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of entries in the SA Cache table.
                ''',
                'msdpnumsacacheentries',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSAHoldDownPeriod', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The number of seconds in the MSDP SA Hold-down
                period
                ''',
                'msdpsaholddownperiod',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdp',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib.Msdprequeststable.Msdprequestsentry' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdprequeststable.Msdprequestsentry',
            False, 
            [
            _MetaInfoClassMember('msdpRequestsGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address that, when combined with the mask
                in this entry, represents the group range for which
                this peer will service MSDP SA Requests.
                ''',
                'msdprequestsgroupaddress',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpRequestsGroupMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The mask that, when combined with the group address
                in this entry, represents the group range for which
                this peer will service MSDP SA Requests.
                ''',
                'msdprequestsgroupmask',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpRequestsPeer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The peer to which MSDP SA Requests for groups
                matching this entry's group range will be sent.  Must
                match the INDEX of a row in the msdpPeerTable.
                ''',
                'msdprequestspeer',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpRequestsStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row, by which new rows may be
                added to the table.
                ''',
                'msdprequestsstatus',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpRequestsEntry',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib.Msdprequeststable' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdprequeststable',
            False, 
            [
            _MetaInfoClassMember('msdpRequestsEntry', REFERENCE_LIST, 'Msdprequestsentry' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdprequeststable.Msdprequestsentry', 
                [], [], 
                '''                An entry (conceptual row) representing a group range
                used when deciding where to send an SA Request
                message.
                ''',
                'msdprequestsentry',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpRequestsTable',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationstateEnum' : _MetaInfoEnum('MsdppeerencapsulationstateEnum', 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB',
        {
            'default':'default',
            'received':'received',
            'advertising':'advertising',
            'sent':'sent',
            'agreed':'agreed',
            'failed':'failed',
        }, 'DRAFT-MSDP-MIB', _yang_ns._namespaces['DRAFT-MSDP-MIB']),
    'DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationtypeEnum' : _MetaInfoEnum('MsdppeerencapsulationtypeEnum', 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB',
        {
            'tcp':'tcp',
            'udp':'udp',
            'gre':'gre',
        }, 'DRAFT-MSDP-MIB', _yang_ns._namespaces['DRAFT-MSDP-MIB']),
    'DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerstateEnum' : _MetaInfoEnum('MsdppeerstateEnum', 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB',
        {
            'inactive':'inactive',
            'listen':'listen',
            'connecting':'connecting',
            'established':'established',
            'disabled':'disabled',
        }, 'DRAFT-MSDP-MIB', _yang_ns._namespaces['DRAFT-MSDP-MIB']),
    'DraftMsdpMib.Msdppeertable.Msdppeerentry' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdppeertable.Msdppeerentry',
            False, 
            [
            _MetaInfoClassMember('msdpPeerRemoteAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the remote MSDP peer.
                ''',
                'msdppeerremoteaddress',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpPeerConnectionAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the state machine has
                transitioned from inactive to connecting.
                ''',
                'msdppeerconnectionattempts',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerConnectRetryInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time interval in seconds for the ConnectRetry timer.
                ''',
                'msdppeerconnectretryinterval',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerDataTtl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The minimum TTL a packet is required to have before
                it may be forwarded using SA encapsulation to this
                peer.
                ''',
                'msdppeerdatattl',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerEncapsulationState', REFERENCE_ENUM_CLASS, 'MsdppeerencapsulationstateEnum' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationstateEnum', 
                [], [], 
                '''                The status of the encapsulation negotiation state
                machine.
                ''',
                'msdppeerencapsulationstate',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerEncapsulationType', REFERENCE_ENUM_CLASS, 'MsdppeerencapsulationtypeEnum' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerencapsulationtypeEnum', 
                [], [], 
                '''                The encapsulation in use when encapsulating data in
                SA messages to this peer.
                ''',
                'msdppeerencapsulationtype',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerFsmEstablishedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This timer indicates how long (in seconds) this peer
                has been in the Established state or how long since
                this peer was last in the Established state.  It is
                set to zero when a new peer is configured or the MSDP
                speaker is booted.
                ''',
                'msdppeerfsmestablishedtime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerFsmEstablishedTransitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of times the MSDP FSM transitioned
                into the established state.
                ''',
                'msdppeerfsmestablishedtransitions',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerHoldTimeConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('3', '65535')], [], 
                '''                Time interval in seconds for the Hold Timer
                configured for this MSDP speaker with this peer.
                ''',
                'msdppeerholdtimeconfigured',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInControlMessages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of MSDP messages received on this
                TCP connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerincontrolmessages',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInDataPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of encapsulated data packets
                received from this peer.  This object should be
                initialized to zero when the connection is
                established.
                ''',
                'msdppeerindatapackets',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInMessageElapsedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Elapsed time in seconds since the last MSDP message
                was received from the peer.  Each time
                msdpPeerInControlMessages is incremented, the value of
                this object is set to zero (0).
                ''',
                'msdppeerinmessageelapsedtime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInNotifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP Notification messages received on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerinnotifications',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInSARequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA-Request messages received on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerinsarequests',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInSAResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA-Response messages received on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerinsaresponses',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInSAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA messages received on this
                connection.  This object should be initialized to zero
                when the connection is established.
                ''',
                'msdppeerinsas',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerKeepAliveConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', '21845')], [], 
                '''                Time interval in seconds for the KeepAlive timer
                configured for this MSDP speaker with this peer.  A
                reasonable maximum value for this timer would be
                configured to be one third of that of
                msdpPeerHoldTimeConfigured.  If the value of this
                object is zero (0), no periodic KEEPALIVE messages are
                sent to the peer after the MSDP connection has been
                established.
                ''',
                'msdppeerkeepaliveconfigured',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerLastError', ATTRIBUTE, 'str' , None, None, 
                [(2, None)], [], 
                '''                The last error code and subcode seen by this peer on
                this connection.  If no error has occurred, this field
                is zero.  Otherwise, the first byte of this two byte
                OCTET STRING contains the error code, and the second
                byte contains the subcode.
                ''',
                'msdppeerlasterror',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address of this entry's MSDP
                connection.
                ''',
                'msdppeerlocaladdress',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port for the TCP connection between the
                MSDP peers.
                ''',
                'msdppeerlocalport',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutControlMessages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of MSDP messages transmitted on this
                TCP connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeeroutcontrolmessages',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutDataPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of encapsulated data packets sent to
                this peer.  This object should be initialized to zero
                when the connection is established.
                ''',
                'msdppeeroutdatapackets',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutNotifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP Notification messages transmitted
                on this connection.  This object should be initialized
                to zero when the connection is established.
                ''',
                'msdppeeroutnotifications',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutSARequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA-Request messages transmitted on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeeroutsarequests',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutSAResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA Response messages transmitted
                on this TCP connection.  This object should be
                initialized to zero when the connection is
                established.
                ''',
                'msdppeeroutsaresponses',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutSAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA messages transmitted on this
                connection.  This object should be initialized to zero
                when the connection is established.
                ''',
                'msdppeeroutsas',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerProcessRequestsFrom', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether or not to process MSDP
                SA Request messages from this peer.  If True(1), MSDP
                SA Request messages from this peer are processed and
                replied to (if appropriate) with SA Response messages.
                If False(2), MSDP SA Request messages from this peer
                are silently ignored.  It defaults to False when
                msdpCacheLifetime is 0 and True when msdpCacheLifetime
                is non-0.
                ''',
                'msdppeerprocessrequestsfrom',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerRemotePort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote port for the TCP connection between the
                MSDP peers.
                ''',
                'msdppeerremoteport',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerRPFFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of RPF failures on SA messages received
                from this peer.
                ''',
                'msdppeerrpffailures',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerSAAdvPeriod', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Time interval in seconds for the
                MinSAAdvertisementInterval MSDP timer.
                ''',
                'msdppeersaadvperiod',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerState', REFERENCE_ENUM_CLASS, 'MsdppeerstateEnum' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdppeertable.Msdppeerentry.MsdppeerstateEnum', 
                [], [], 
                '''                The state of the MSDP TCP connection with this peer.
                ''',
                'msdppeerstate',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The RowStatus object by which peers can be added and
                deleted.  A transition to 'active' will cause the MSDP
                Start Event to be generated.  A transition out of the
                'active' state will cause the MSDP Stop Event to be
                generated.  Care should be used in providing write
                access to this object without adequate
                authentication.
                ''',
                'msdppeerstatus',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpPeerEntry',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib.Msdppeertable' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdppeertable',
            False, 
            [
            _MetaInfoClassMember('msdpPeerEntry', REFERENCE_LIST, 'Msdppeerentry' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdppeertable.Msdppeerentry', 
                [], [], 
                '''                An entry (conceptual row) representing an MSDP peer.
                ''',
                'msdppeerentry',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpPeerTable',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry',
            False, 
            [
            _MetaInfoClassMember('msdpSACacheGroupAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address of the SA Cache entry.
                ''',
                'msdpsacachegroupaddr',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpSACacheSourceAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source address of the SA Cache entry.
                ''',
                'msdpsacachesourceaddr',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpSACacheOriginRP', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the RP which originated the last SA
                message accepted for this entry.
                ''',
                'msdpsacacheoriginrp',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpSACacheExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining before this entry will expire from
                the SA cache.
                ''',
                'msdpsacacheexpirytime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheInDataPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP encapsulated data packets received
                relevant to this cache entry.  This object must be
                initialized to zero when creating a cache entry.
                ''',
                'msdpsacacheindatapackets',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheInSAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MSDP SA messages received relevant to
                this cache entry.  This object must be initialized to
                zero when creating a cache entry.
                ''',
                'msdpsacacheinsas',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACachePeerLearnedFrom', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The peer from which this SA Cache entry was last
                accepted.  This address must correspond to the
                msdpPeerRemoteAddress value for a row in the MSDP Peer
                Table.
                ''',
                'msdpsacachepeerlearnedfrom',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheRPFPeer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The peer from which an SA message corresponding to
                this cache entry would be accepted (i.e. the RPF peer
                for msdpSACacheOriginRP).  This may be different than
                msdpSACachePeerLearnedFrom if this entry was created
                by an MSDP SA-Response.  This address must correspond
                to the msdpPeerRemoteAddress value for a row in the
                MSDP Peer Table.
                ''',
                'msdpsacacherpfpeer',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row in the table.  The only
                allowable actions are to retreive the status, which
                will be `active', or to set the status to `destroy' in
                order to remove this entry from the cache.
                ''',
                'msdpsacachestatus',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time since this entry was placed in the SA
                cache.
                ''',
                'msdpsacacheuptime',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpSACacheEntry',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib.Msdpsacachetable' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib.Msdpsacachetable',
            False, 
            [
            _MetaInfoClassMember('msdpSACacheEntry', REFERENCE_LIST, 'Msdpsacacheentry' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry', 
                [], [], 
                '''                An entry (conceptual row) representing an MSDP SA
                advert.
                ''',
                'msdpsacacheentry',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpSACacheTable',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
    'DraftMsdpMib' : {
        'meta_info' : _MetaInfoClass('DraftMsdpMib',
            False, 
            [
            _MetaInfoClassMember('msdp', REFERENCE_CLASS, 'Msdp' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdp', 
                [], [], 
                '''                ''',
                'msdp',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerTable', REFERENCE_CLASS, 'Msdppeertable' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdppeertable', 
                [], [], 
                '''                The (conceptual) table listing the MSDP speaker's
                peers.
                ''',
                'msdppeertable',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpRequestsTable', REFERENCE_CLASS, 'Msdprequeststable' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdprequeststable', 
                [], [], 
                '''                The (conceptual) table listing group ranges and MSDP
                peers used when deciding where to send an SA Request
                message when required.  If SA Caching is enabled, this
                table may be empty.
                ''',
                'msdprequeststable',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheTable', REFERENCE_CLASS, 'Msdpsacachetable' , 'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB', 'DraftMsdpMib.Msdpsacachetable', 
                [], [], 
                '''                The (conceptual) table listing the MSDP SA
                advertisements currently in the MSDP speaker's cache.
                ''',
                'msdpsacachetable',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'DRAFT-MSDP-MIB',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB'
        ),
    },
}
_meta_table['DraftMsdpMib.Msdprequeststable.Msdprequestsentry']['meta_info'].parent =_meta_table['DraftMsdpMib.Msdprequeststable']['meta_info']
_meta_table['DraftMsdpMib.Msdppeertable.Msdppeerentry']['meta_info'].parent =_meta_table['DraftMsdpMib.Msdppeertable']['meta_info']
_meta_table['DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry']['meta_info'].parent =_meta_table['DraftMsdpMib.Msdpsacachetable']['meta_info']
_meta_table['DraftMsdpMib.Msdp']['meta_info'].parent =_meta_table['DraftMsdpMib']['meta_info']
_meta_table['DraftMsdpMib.Msdprequeststable']['meta_info'].parent =_meta_table['DraftMsdpMib']['meta_info']
_meta_table['DraftMsdpMib.Msdppeertable']['meta_info'].parent =_meta_table['DraftMsdpMib']['meta_info']
_meta_table['DraftMsdpMib.Msdpsacachetable']['meta_info'].parent =_meta_table['DraftMsdpMib']['meta_info']
