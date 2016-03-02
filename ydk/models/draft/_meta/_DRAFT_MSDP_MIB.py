


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'DRAFTMSDPMIB.Msdp' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.Msdp',
            False, 
            [
            _MetaInfoClassMember('msdpCacheLifetime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The total number of entries in the SA Cache table.
                ''',
                'msdpnumsacacheentries',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSAHoldDownPeriod', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The number of seconds in the MSDP SA Hold-down
                period
                ''',
                'msdpsaholddownperiod',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdp',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry.MsdpPeerEncapsulationState_Enum' : _MetaInfoEnum('MsdpPeerEncapsulationState_Enum', 'ydk.models.draft.DRAFT_MSDP_MIB',
        {
            'default':'DEFAULT',
            'received':'RECEIVED',
            'advertising':'ADVERTISING',
            'sent':'SENT',
            'agreed':'AGREED',
            'failed':'FAILED',
        }, 'DRAFT-MSDP-MIB', _yang_ns._namespaces['DRAFT-MSDP-MIB']),
    'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry.MsdpPeerEncapsulationType_Enum' : _MetaInfoEnum('MsdpPeerEncapsulationType_Enum', 'ydk.models.draft.DRAFT_MSDP_MIB',
        {
            'tcp':'TCP',
            'udp':'UDP',
            'gre':'GRE',
        }, 'DRAFT-MSDP-MIB', _yang_ns._namespaces['DRAFT-MSDP-MIB']),
    'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry.MsdpPeerState_Enum' : _MetaInfoEnum('MsdpPeerState_Enum', 'ydk.models.draft.DRAFT_MSDP_MIB',
        {
            'inactive':'INACTIVE',
            'listen':'LISTEN',
            'connecting':'CONNECTING',
            'established':'ESTABLISHED',
            'disabled':'DISABLED',
        }, 'DRAFT-MSDP-MIB', _yang_ns._namespaces['DRAFT-MSDP-MIB']),
    'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry',
            False, 
            [
            _MetaInfoClassMember('msdpPeerRemoteAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the remote MSDP peer.
                ''',
                'msdppeerremoteaddress',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpPeerConnectionAttempts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the state machine has
                transitioned from inactive to connecting.
                ''',
                'msdppeerconnectionattempts',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerConnectRetryInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time interval in seconds for the ConnectRetry timer.
                ''',
                'msdppeerconnectretryinterval',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerDataTtl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The minimum TTL a packet is required to have before
                it may be forwarded using SA encapsulation to this
                peer.
                ''',
                'msdppeerdatattl',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerEncapsulationState', REFERENCE_ENUM_CLASS, 'MsdpPeerEncapsulationState_Enum' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry.MsdpPeerEncapsulationState_Enum', 
                [], [], 
                '''                The status of the encapsulation negotiation state
                machine.
                ''',
                'msdppeerencapsulationstate',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerEncapsulationType', REFERENCE_ENUM_CLASS, 'MsdpPeerEncapsulationType_Enum' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry.MsdpPeerEncapsulationType_Enum', 
                [], [], 
                '''                The encapsulation in use when encapsulating data in
                SA messages to this peer.
                ''',
                'msdppeerencapsulationtype',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerFsmEstablishedTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This timer indicates how long (in seconds) this peer
                has been in the Established state or how long since
                this peer was last in the Established state.  It is
                set to zero when a new peer is configured or the MSDP
                speaker is booted.
                ''',
                'msdppeerfsmestablishedtime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerFsmEstablishedTransitions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of times the MSDP FSM transitioned
                into the established state.
                ''',
                'msdppeerfsmestablishedtransitions',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerHoldTimeConfigured', ATTRIBUTE, 'int' , None, None, 
                [(0, None), (3, 65535)], [], 
                '''                Time interval in seconds for the Hold Timer
                configured for this MSDP speaker with this peer.
                ''',
                'msdppeerholdtimeconfigured',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInControlMessages', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of MSDP messages received on this
                TCP connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerincontrolmessages',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInDataPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of encapsulated data packets
                received from this peer.  This object should be
                initialized to zero when the connection is
                established.
                ''',
                'msdppeerindatapackets',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInMessageElapsedTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Elapsed time in seconds since the last MSDP message
                was received from the peer.  Each time
                msdpPeerInControlMessages is incremented, the value of
                this object is set to zero (0).
                ''',
                'msdppeerinmessageelapsedtime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInNotifications', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP Notification messages received on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerinnotifications',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInSARequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP SA-Request messages received on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerinsarequests',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInSAResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP SA-Response messages received on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeerinsaresponses',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerInSAs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP SA messages received on this
                connection.  This object should be initialized to zero
                when the connection is established.
                ''',
                'msdppeerinsas',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerKeepAliveConfigured', ATTRIBUTE, 'int' , None, None, 
                [(0, 21845)], [], 
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
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address of this entry's MSDP
                connection.
                ''',
                'msdppeerlocaladdress',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The local port for the TCP connection between the
                MSDP peers.
                ''',
                'msdppeerlocalport',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutControlMessages', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of MSDP messages transmitted on this
                TCP connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeeroutcontrolmessages',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutDataPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of encapsulated data packets sent to
                this peer.  This object should be initialized to zero
                when the connection is established.
                ''',
                'msdppeeroutdatapackets',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutNotifications', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP Notification messages transmitted
                on this connection.  This object should be initialized
                to zero when the connection is established.
                ''',
                'msdppeeroutnotifications',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutSARequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP SA-Request messages transmitted on
                this connection.  This object should be initialized to
                zero when the connection is established.
                ''',
                'msdppeeroutsarequests',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutSAResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP SA Response messages transmitted
                on this TCP connection.  This object should be
                initialized to zero when the connection is
                established.
                ''',
                'msdppeeroutsaresponses',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerOutSAs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                The remote port for the TCP connection between the
                MSDP peers.
                ''',
                'msdppeerremoteport',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerRPFFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of RPF failures on SA messages received
                from this peer.
                ''',
                'msdppeerrpffailures',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerSAAdvPeriod', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                Time interval in seconds for the
                MinSAAdvertisementInterval MSDP timer.
                ''',
                'msdppeersaadvperiod',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerState', REFERENCE_ENUM_CLASS, 'MsdpPeerState_Enum' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry.MsdpPeerState_Enum', 
                [], [], 
                '''                The state of the MSDP TCP connection with this peer.
                ''',
                'msdppeerstate',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
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
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB.MsdpPeerTable' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.MsdpPeerTable',
            False, 
            [
            _MetaInfoClassMember('msdpPeerEntry', REFERENCE_LIST, 'MsdpPeerEntry' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry', 
                [], [], 
                '''                An entry (conceptual row) representing an MSDP peer.
                ''',
                'msdppeerentry',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpPeerTable',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB.MsdpRequestsTable.MsdpRequestsEntry' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.MsdpRequestsTable.MsdpRequestsEntry',
            False, 
            [
            _MetaInfoClassMember('msdpRequestsGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address that, when combined with the mask
                in this entry, represents the group range for which
                this peer will service MSDP SA Requests.
                ''',
                'msdprequestsgroupaddress',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpRequestsGroupMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The mask that, when combined with the group address
                in this entry, represents the group range for which
                this peer will service MSDP SA Requests.
                ''',
                'msdprequestsgroupmask',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpRequestsPeer', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The peer to which MSDP SA Requests for groups
                matching this entry's group range will be sent.  Must
                match the INDEX of a row in the msdpPeerTable.
                ''',
                'msdprequestspeer',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpRequestsStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
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
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB.MsdpRequestsTable' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.MsdpRequestsTable',
            False, 
            [
            _MetaInfoClassMember('msdpRequestsEntry', REFERENCE_LIST, 'MsdpRequestsEntry' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpRequestsTable.MsdpRequestsEntry', 
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
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB.MsdpSACacheTable.MsdpSACacheEntry' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.MsdpSACacheTable.MsdpSACacheEntry',
            False, 
            [
            _MetaInfoClassMember('msdpSACacheGroupAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The group address of the SA Cache entry.
                ''',
                'msdpsacachegroupaddr',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpSACacheOriginRP', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The address of the RP which originated the last SA
                message accepted for this entry.
                ''',
                'msdpsacacheoriginrp',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpSACacheSourceAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source address of the SA Cache entry.
                ''',
                'msdpsacachesourceaddr',
                'DRAFT-MSDP-MIB', True),
            _MetaInfoClassMember('msdpSACacheExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time remaining before this entry will expire from
                the SA cache.
                ''',
                'msdpsacacheexpirytime',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheInDataPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP encapsulated data packets received
                relevant to this cache entry.  This object must be
                initialized to zero when creating a cache entry.
                ''',
                'msdpsacacheindatapackets',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheInSAs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MSDP SA messages received relevant to
                this cache entry.  This object must be initialized to
                zero when creating a cache entry.
                ''',
                'msdpsacacheinsas',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACachePeerLearnedFrom', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The peer from which this SA Cache entry was last
                accepted.  This address must correspond to the
                msdpPeerRemoteAddress value for a row in the MSDP Peer
                Table.
                ''',
                'msdpsacachepeerlearnedfrom',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheRPFPeer', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
            _MetaInfoClassMember('msdpSACacheStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this row in the table.  The only
                allowable actions are to retreive the status, which
                will be `active', or to set the status to `destroy' in
                order to remove this entry from the cache.
                ''',
                'msdpsacachestatus',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time since this entry was placed in the SA
                cache.
                ''',
                'msdpsacacheuptime',
                'DRAFT-MSDP-MIB', False),
            ],
            'DRAFT-MSDP-MIB',
            'msdpSACacheEntry',
            _yang_ns._namespaces['DRAFT-MSDP-MIB'],
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB.MsdpSACacheTable' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB.MsdpSACacheTable',
            False, 
            [
            _MetaInfoClassMember('msdpSACacheEntry', REFERENCE_LIST, 'MsdpSACacheEntry' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpSACacheTable.MsdpSACacheEntry', 
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
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
    'DRAFTMSDPMIB' : {
        'meta_info' : _MetaInfoClass('DRAFTMSDPMIB',
            False, 
            [
            _MetaInfoClassMember('msdp', REFERENCE_CLASS, 'Msdp' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.Msdp', 
                [], [], 
                '''                ''',
                'msdp',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpPeerTable', REFERENCE_CLASS, 'MsdpPeerTable' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpPeerTable', 
                [], [], 
                '''                The (conceptual) table listing the MSDP speaker's
                peers.
                ''',
                'msdppeertable',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpRequestsTable', REFERENCE_CLASS, 'MsdpRequestsTable' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpRequestsTable', 
                [], [], 
                '''                The (conceptual) table listing group ranges and MSDP
                peers used when deciding where to send an SA Request
                message when required.  If SA Caching is enabled, this
                table may be empty.
                ''',
                'msdprequeststable',
                'DRAFT-MSDP-MIB', False),
            _MetaInfoClassMember('msdpSACacheTable', REFERENCE_CLASS, 'MsdpSACacheTable' , 'ydk.models.draft.DRAFT_MSDP_MIB', 'DRAFTMSDPMIB.MsdpSACacheTable', 
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
        'ydk.models.draft.DRAFT_MSDP_MIB'
        ),
    },
}
_meta_table['DRAFTMSDPMIB.MsdpPeerTable.MsdpPeerEntry']['meta_info'].parent =_meta_table['DRAFTMSDPMIB.MsdpPeerTable']['meta_info']
_meta_table['DRAFTMSDPMIB.MsdpRequestsTable.MsdpRequestsEntry']['meta_info'].parent =_meta_table['DRAFTMSDPMIB.MsdpRequestsTable']['meta_info']
_meta_table['DRAFTMSDPMIB.MsdpSACacheTable.MsdpSACacheEntry']['meta_info'].parent =_meta_table['DRAFTMSDPMIB.MsdpSACacheTable']['meta_info']
_meta_table['DRAFTMSDPMIB.Msdp']['meta_info'].parent =_meta_table['DRAFTMSDPMIB']['meta_info']
_meta_table['DRAFTMSDPMIB.MsdpPeerTable']['meta_info'].parent =_meta_table['DRAFTMSDPMIB']['meta_info']
_meta_table['DRAFTMSDPMIB.MsdpRequestsTable']['meta_info'].parent =_meta_table['DRAFTMSDPMIB']['meta_info']
_meta_table['DRAFTMSDPMIB.MsdpSACacheTable']['meta_info'].parent =_meta_table['DRAFTMSDPMIB']['meta_info']
