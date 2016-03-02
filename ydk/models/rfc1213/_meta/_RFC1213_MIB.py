


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RFC1213MIB.AtTable.AtEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.AtTable.AtEntry',
            False, 
            [
            _MetaInfoClassMember('atIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The interface on which this entry's equivalence
                is effective.  The interface identified by a
                particular value of this index is the same
                interface as identified by the same value of
                ifIndex.
                ''',
                'atifindex',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('atNetAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The NetworkAddress (e.g., the IP address)
                corresponding to the media-dependent `physical'
                address.
                ''',
                'atnetaddress',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('atPhysAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The media-dependent `physical' address.
                
                Setting this object to a null string (one of zero
                length) has the effect of invaliding the
                corresponding entry in the atTable object.  That
                is, it effectively disassociates the interface
                identified with said entry from the mapping
                identified with said entry.  It is an
                implementation-specific matter as to whether the
                agent removes an invalidated entry from the table.
                Accordingly, management stations must be prepared
                to receive tabular information from agents that
                corresponds to entries not currently in use.
                Proper interpretation of such entries requires
                examination of the relevant atPhysAddress object.
                ''',
                'atphysaddress',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'atEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.AtTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.AtTable',
            False, 
            [
            _MetaInfoClassMember('atEntry', REFERENCE_LIST, 'AtEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.AtTable.AtEntry', 
                [], [], 
                '''                Each entry contains one NetworkAddress to
                `physical' address equivalence.
                ''',
                'atentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'atTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Egp' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Egp',
            False, 
            [
            _MetaInfoClassMember('egpAs', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The autonomous system number of this EGP entity.
                ''',
                'egpas',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpInErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP messages received that proved
                to be in error.
                ''',
                'egpinerrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpInMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP messages received without
                error.
                ''',
                'egpinmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpOutErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of locally generated EGP messages not
                sent due to resource limitations within an EGP
                entity.
                ''',
                'egpouterrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpOutMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of locally generated EGP
                messages.
                ''',
                'egpoutmsgs',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'egp',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighEventTrigger_Enum' : _MetaInfoEnum('EgpNeighEventTrigger_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'start':'START',
            'stop':'STOP',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighMode_Enum' : _MetaInfoEnum('EgpNeighMode_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'active':'ACTIVE',
            'passive':'PASSIVE',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighState_Enum' : _MetaInfoEnum('EgpNeighState_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'idle':'IDLE',
            'acquisition':'ACQUISITION',
            'down':'DOWN',
            'up':'UP',
            'cease':'CEASE',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.EgpNeighTable.EgpNeighEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.EgpNeighTable.EgpNeighEntry',
            False, 
            [
            _MetaInfoClassMember('egpNeighAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of this entry's EGP neighbor.
                ''',
                'egpneighaddr',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('egpNeighAs', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The autonomous system of this EGP peer.  Zero
                should be specified if the autonomous system
                number of the neighbor is not yet known.
                ''',
                'egpneighas',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighEventTrigger', REFERENCE_ENUM_CLASS, 'EgpNeighEventTrigger_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighEventTrigger_Enum', 
                [], [], 
                '''                A control variable used to trigger operator-
                initiated Start and Stop events.  When read, this
                variable always returns the most recent value that
                egpNeighEventTrigger was set to.  If it has not
                been set since the last initialization of the
                network management subsystem on the node, it
                returns a value of `stop'.
                
                When set, this variable causes a Start or Stop
                event on the specified neighbor, as specified on
                pages 8-10 of RFC 904.  Briefly, a Start event
                causes an Idle peer to begin neighbor acquisition
                and a non-Idle peer to reinitiate neighbor
                acquisition.  A stop event causes a non-Idle peer
                to return to the Idle state until a Start event
                occurs, either via egpNeighEventTrigger or
                otherwise.
                ''',
                'egpneigheventtrigger',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighInErrMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP-defined error messages received
                from this EGP peer.
                ''',
                'egpneighinerrmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighInErrs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP messages received from this EGP
                peer that proved to be in error (e.g., bad EGP
                checksum).
                ''',
                'egpneighinerrs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighInMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP messages received without error
                from this EGP peer.
                ''',
                'egpneighinmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighIntervalHello', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The interval between EGP Hello command
                retransmissions (in hundredths of a second).  This
                represents the t1 timer as defined in RFC 904.
                ''',
                'egpneighintervalhello',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighIntervalPoll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The interval between EGP poll command
                retransmissions (in hundredths of a second).  This
                represents the t3 timer as defined in RFC 904.
                ''',
                'egpneighintervalpoll',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighMode', REFERENCE_ENUM_CLASS, 'EgpNeighMode_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighMode_Enum', 
                [], [], 
                '''                The polling mode of this EGP entity, either
                passive or active.
                ''',
                'egpneighmode',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighOutErrMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP-defined error messages sent to
                this EGP peer.
                ''',
                'egpneighouterrmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighOutErrs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of locally generated EGP messages not
                sent to this EGP peer due to resource limitations
                within an EGP entity.
                ''',
                'egpneighouterrs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighOutMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of locally generated EGP messages to
                this EGP peer.
                ''',
                'egpneighoutmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighState', REFERENCE_ENUM_CLASS, 'EgpNeighState_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighState_Enum', 
                [], [], 
                '''                The EGP state of the local system with respect to
                this entry's EGP neighbor.  Each EGP state is
                represented by a value that is one greater than
                the numerical value associated with said state in
                RFC 904.
                ''',
                'egpneighstate',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighStateDowns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP state transitions from the UP
                state to any other state with this EGP peer.
                ''',
                'egpneighstatedowns',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighStateUps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of EGP state transitions to the UP
                state with this EGP peer.
                ''',
                'egpneighstateups',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'egpNeighEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.EgpNeighTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.EgpNeighTable',
            False, 
            [
            _MetaInfoClassMember('egpNeighEntry', REFERENCE_LIST, 'EgpNeighEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.EgpNeighTable.EgpNeighEntry', 
                [], [], 
                '''                Information about this entity's relationship with
                a particular EGP neighbor.
                ''',
                'egpneighentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'egpNeighTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Icmp' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Icmp',
            False, 
            [
            _MetaInfoClassMember('icmpInAddrMaskReps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Address Mask Reply messages
                received.
                ''',
                'icmpinaddrmaskreps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInAddrMasks', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Address Mask Request messages
                received.
                ''',
                'icmpinaddrmasks',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInDestUnreachs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Destination Unreachable
                messages received.
                ''',
                'icmpindestunreachs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInEchoReps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Echo Reply messages received.
                ''',
                'icmpinechoreps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInEchos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Echo (request) messages
                received.
                ''',
                'icmpinechos',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP messages which the entity
                received but determined as having ICMP-specific
                errors (bad ICMP checksums, bad length, etc.).
                ''',
                'icmpinerrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of ICMP messages which the
                entity received.  Note that this counter includes
                all those counted by icmpInErrors.
                ''',
                'icmpinmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInParmProbs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Parameter Problem messages
                received.
                ''',
                'icmpinparmprobs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInRedirects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Redirect messages received.
                ''',
                'icmpinredirects',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInSrcQuenchs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Source Quench messages
                received.
                ''',
                'icmpinsrcquenchs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInTimeExcds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Time Exceeded messages
                received.
                ''',
                'icmpintimeexcds',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInTimestampReps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Timestamp Reply messages
                received.
                ''',
                'icmpintimestampreps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpInTimestamps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Timestamp (request) messages
                received.
                ''',
                'icmpintimestamps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutAddrMaskReps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Address Mask Reply messages
                sent.
                ''',
                'icmpoutaddrmaskreps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutAddrMasks', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Address Mask Request messages
                sent.
                ''',
                'icmpoutaddrmasks',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutDestUnreachs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Destination Unreachable
                messages sent.
                ''',
                'icmpoutdestunreachs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutEchoReps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Echo Reply messages sent.
                ''',
                'icmpoutechoreps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutEchos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Echo (request) messages sent.
                ''',
                'icmpoutechos',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP messages which this entity did
                not send due to problems discovered within ICMP
                such as a lack of buffers.  This value should not
                include errors discovered outside the ICMP layer
                such as the inability of IP to route the resultant
                datagram.  In some implementations there may be no
                types of error which contribute to this counter's
                value.
                ''',
                'icmpouterrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of ICMP messages which this
                entity attempted to send.  Note that this counter
                includes all those counted by icmpOutErrors.
                ''',
                'icmpoutmsgs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutParmProbs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Parameter Problem messages
                sent.
                ''',
                'icmpoutparmprobs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutRedirects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Redirect messages sent.  For a
                host, this object will always be zero, since hosts
                do not send redirects.
                ''',
                'icmpoutredirects',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutSrcQuenchs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Source Quench messages sent.
                ''',
                'icmpoutsrcquenchs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutTimeExcds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Time Exceeded messages sent.
                ''',
                'icmpouttimeexcds',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutTimestampReps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Timestamp Reply messages
                sent.
                ''',
                'icmpouttimestampreps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmpOutTimestamps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ICMP Timestamp (request) messages
                sent.
                ''',
                'icmpouttimestamps',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'icmp',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IfTable.IfEntry.IfAdminStatus_Enum' : _MetaInfoEnum('IfAdminStatus_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'testing':'TESTING',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.IfTable.IfEntry.IfOperStatus_Enum' : _MetaInfoEnum('IfOperStatus_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'testing':'TESTING',
            'unknown':'UNKNOWN',
            'dormant':'DORMANT',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.IfTable.IfEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IfTable.IfEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                A unique value for each interface.  Its value
                ranges between 1 and the value of ifNumber.  The
                value for each interface must remain constant at
                least from one re-initialization of the entity's
                network management system to the next re-
                initialization.
                ''',
                'ifindex',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('ifAdminStatus', REFERENCE_ENUM_CLASS, 'IfAdminStatus_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IfTable.IfEntry.IfAdminStatus_Enum', 
                [], [], 
                '''                The desired state of the interface.  The
                testing(3) state indicates that no operational
                packets can be passed.
                ''',
                'ifadminstatus',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A textual string containing information about the
                interface.  This string should include the name of
                the manufacturer, the product name and the version
                of the hardware interface.
                ''',
                'ifdescr',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifInDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of inbound packets which were chosen
                to be discarded even though no errors had been
                detected to prevent their being deliverable to a
                higher-layer protocol.  One possible reason for
                discarding such a packet could be to free up
                buffer space.
                ''',
                'ifindiscards',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifInErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of inbound packets that contained
                errors preventing them from being deliverable to a
                higher-layer protocol.
                ''',
                'ifinerrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifInNUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of non-unicast (i.e., subnetwork-
                broadcast or subnetwork-multicast) packets
                delivered to a higher-layer protocol.
                ''',
                'ifinnucastpkts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received on the
                interface, including framing characters.
                ''',
                'ifinoctets',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifInUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of subnetwork-unicast packets
                delivered to a higher-layer protocol.
                ''',
                'ifinucastpkts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifInUnknownProtos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets received via the interface
                which were discarded because of an unknown or
                unsupported protocol.
                ''',
                'ifinunknownprotos',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time the interface
                entered its current operational state.  If the
                current state was entered prior to the last re-
                initialization of the local network management
                subsystem, then this object contains a zero
                value.
                ''',
                'iflastchange',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifMtu', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The size of the largest datagram which can be
                sent/received on the interface, specified in
                octets.  For interfaces that are used for
                transmitting network datagrams, this is the size
                of the largest network datagram that can be sent
                on the interface.
                ''',
                'ifmtu',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOperStatus', REFERENCE_ENUM_CLASS, 'IfOperStatus_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IfTable.IfEntry.IfOperStatus_Enum', 
                [], [], 
                '''                The current operational state of the interface.
                The testing(3) state indicates that no operational
                packets can be passed.
                ''',
                'ifoperstatus',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOutDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of outbound packets which were chosen
                to be discarded even though no errors had been
                detected to prevent their being transmitted.  One
                possible reason for discarding such a packet could
                be to free up buffer space.
                ''',
                'ifoutdiscards',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOutErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of outbound packets that could not be
                transmitted because of errors.
                ''',
                'ifouterrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOutNUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets that higher-level
                protocols requested be transmitted to a non-
                unicast (i.e., a subnetwork-broadcast or
                subnetwork-multicast) address, including those
                that were discarded or not sent.
                ''',
                'ifoutnucastpkts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets transmitted out of the
                interface, including framing characters.
                ''',
                'ifoutoctets',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOutQLen', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The length of the output packet queue (in
                packets).
                ''',
                'ifoutqlen',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifOutUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets that higher-level
                protocols requested be transmitted to a
                subnetwork-unicast address, including those that
                were discarded or not sent.
                ''',
                'ifoutucastpkts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifPhysAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface's address at the protocol layer
                immediately `below' the network layer in the
                protocol stack.  For interfaces which do not have
                such an address (e.g., a serial line), this object
                should contain an octet string of zero length.
                ''',
                'ifphysaddress',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifSpecific', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A reference to MIB definitions specific to the
                particular media being used to realize the
                interface.  For example, if the interface is
                realized by an ethernet, then the value of this
                object refers to a document defining objects
                specific to ethernet.  If this information is not
                present, its value should be set to the OBJECT
                IDENTIFIER { 0 0 }, which is a syntactically valid
                object identifier, and any conformant
                implementation of ASN.1 and BER must be able to
                generate and recognize this value.
                ''',
                'ifspecific',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifSpeed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                An estimate of the interface's current bandwidth
                in bits per second.  For interfaces which do not
                vary in bandwidth or for those where no accurate
                estimation can be made, this object should contain
                the nominal bandwidth.
                ''',
                'ifspeed',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifType', REFERENCE_ENUM_CLASS, 'IANAifType_Enum' , 'ydk.models.ianaiftype.IANAifType_MIB', 'IANAifType_Enum', 
                [], [], 
                '''                The type of interface.  Additional values for ifType
                are assigned by the Internet Assigned Numbers
                Authority (IANA), through updating the syntax of the
                IANAifType textual convention.
                ''',
                'iftype',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ifEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IfTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IfTable',
            False, 
            [
            _MetaInfoClassMember('ifEntry', REFERENCE_LIST, 'IfEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IfTable.IfEntry', 
                [], [], 
                '''                An interface entry containing objects at the
                subnetwork layer and below for a particular
                interface.
                ''',
                'ifentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ifTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Interfaces' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Interfaces',
            False, 
            [
            _MetaInfoClassMember('ifNumber', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of network interfaces (regardless of
                their current state) present on this system.
                ''',
                'ifnumber',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'interfaces',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Ip.IpForwarding_Enum' : _MetaInfoEnum('IpForwarding_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'forwarding':'FORWARDING',
            'not-forwarding':'NOT_FORWARDING',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.Ip' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Ip',
            False, 
            [
            _MetaInfoClassMember('ipDefaultTTL', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The default value inserted into the Time-To-Live
                field of the IP header of datagrams originated at
                this entity, whenever a TTL value is not supplied
                by the transport layer protocol.
                ''',
                'ipdefaultttl',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipForwarding', REFERENCE_ENUM_CLASS, 'IpForwarding_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Ip.IpForwarding_Enum', 
                [], [], 
                '''                The indication of whether this entity is acting
                as an IP gateway in respect to the forwarding of
                datagrams received by, but not addressed to, this
                entity.  IP gateways forward datagrams.  IP hosts
                do not (except those source-routed via the host).
                
                Note that for some managed nodes, this object may
                take on only a subset of the values possible.
                Accordingly, it is appropriate for an agent to
                return a `badValue' response if a management
                station attempts to change this object to an
                inappropriate value.
                ''',
                'ipforwarding',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of input datagrams for which this
                entity was not their final IP destination, as a
                result of which an attempt was made to find a
                route to forward them to that final destination.
                In entities which do not act as IP Gateways, this
                counter will include only those packets which were
                Source-Routed via this entity, and the Source-
                Route option processing was successful.
                ''',
                'ipforwdatagrams',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipFragCreates', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IP datagram fragments that have
                been generated as a result of fragmentation at
                this entity.
                ''',
                'ipfragcreates',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipFragFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IP datagrams that have been
                discarded because they needed to be fragmented at
                this entity but could not be, e.g., because their
                Don't Fragment flag was set.
                ''',
                'ipfragfails',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipFragOKs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IP datagrams that have been
                successfully fragmented at this entity.
                ''',
                'ipfragoks',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipInAddrErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of input datagrams discarded because
                the IP address in their IP header's destination
                field was not a valid address to be received at
                this entity.  This count includes invalid
                addresses (e.g., 0.0.0.0) and addresses of
                unsupported Classes (e.g., Class E).  For entities
                which are not IP Gateways and therefore do not
                forward datagrams, this counter includes datagrams
                discarded because the destination address was not
                a local address.
                ''',
                'ipinaddrerrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipInDelivers', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of input datagrams successfully
                delivered to IP user-protocols (including ICMP).
                ''',
                'ipindelivers',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipInDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of input IP datagrams for which no
                problems were encountered to prevent their
                continued processing, but which were discarded
                (e.g., for lack of buffer space).  Note that this
                counter does not include any datagrams discarded
                while awaiting re-assembly.
                ''',
                'ipindiscards',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipInHdrErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of input datagrams discarded due to
                errors in their IP headers, including bad
                checksums, version number mismatch, other format
                errors, time-to-live exceeded, errors discovered
                in processing their IP options, etc.
                ''',
                'ipinhdrerrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipInReceives', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of input datagrams received from
                interfaces, including those received in error.
                ''',
                'ipinreceives',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipInUnknownProtos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of locally-addressed datagrams
                received successfully but discarded because of an
                unknown or unsupported protocol.
                ''',
                'ipinunknownprotos',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipOutDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of output IP datagrams for which no
                problem was encountered to prevent their
                transmission to their destination, but which were
                discarded (e.g., for lack of buffer space).  Note
                that this counter would include datagrams counted
                in ipForwDatagrams if any such packets met this
                (discretionary) discard criterion.
                ''',
                'ipoutdiscards',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipOutNoRoutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IP datagrams discarded because no
                route could be found to transmit them to their
                destination.  Note that this counter includes any
                packets counted in ipForwDatagrams which meet this
                `no-route' criterion.  Note that this includes any
                datagrams which a host cannot route because all of
                its default gateways are down.
                ''',
                'ipoutnoroutes',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipOutRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IP datagrams which local IP
                user-protocols (including ICMP) supplied to IP in
                requests for transmission.  Note that this counter
                does not include any datagrams counted in
                ipForwDatagrams.
                ''',
                'ipoutrequests',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipReasmFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of failures detected by the IP re-
                assembly algorithm (for whatever reason: timed
                out, errors, etc).  Note that this is not
                necessarily a count of discarded IP fragments
                since some algorithms (notably the algorithm in
                RFC 815) can lose track of the number of fragments
                by combining them as they are received.
                ''',
                'ipreasmfails',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipReasmOKs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IP datagrams successfully re-
                assembled.
                ''',
                'ipreasmoks',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipReasmReqds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IP fragments received which needed
                to be reassembled at this entity.
                ''',
                'ipreasmreqds',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipReasmTimeout', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of seconds which received
                fragments are held while they are awaiting
                reassembly at this entity.
                ''',
                'ipreasmtimeout',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRoutingDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of routing entries which were chosen
                to be discarded even though they are valid.  One
                possible reason for discarding such an entry could
                be to free-up buffer space for other routing
                entries.
                ''',
                'iproutingdiscards',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ip',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IpAddrTable.IpAddrEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IpAddrTable.IpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ipAdEntAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address to which this entry's addressing
                information pertains.
                ''',
                'ipadentaddr',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('ipAdEntBcastAddr', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The value of the least-significant bit in the IP
                broadcast address used for sending datagrams on
                the (logical) interface associated with the IP
                address of this entry.  For example, when the
                Internet standard all-ones broadcast address is
                used, the value will be 1.  This value applies to
                both the subnet and network broadcasts addresses
                used by the entity on this (logical) interface.
                ''',
                'ipadentbcastaddr',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipAdEntIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The index value which uniquely identifies the
                interface to which this entry is applicable.  The
                interface identified by a particular value of this
                index is the same interface as identified by the
                same value of ifIndex.
                ''',
                'ipadentifindex',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipAdEntNetMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The subnet mask associated with the IP address of
                this entry.  The value of the mask is an IP
                address with all the network bits set to 1 and all
                the hosts bits set to 0.
                ''',
                'ipadentnetmask',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipAdEntReasmMaxSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The size of the largest IP datagram which this
                entity can re-assemble from incoming IP fragmented
                datagrams received on this interface.
                ''',
                'ipadentreasmmaxsize',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ipAddrEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IpAddrTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IpAddrTable',
            False, 
            [
            _MetaInfoClassMember('ipAddrEntry', REFERENCE_LIST, 'IpAddrEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpAddrTable.IpAddrEntry', 
                [], [], 
                '''                The addressing information for one of this
                entity's IP addresses.
                ''',
                'ipaddrentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ipAddrTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry.IpNetToMediaType_Enum' : _MetaInfoEnum('IpNetToMediaType_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'other':'OTHER',
            'invalid':'INVALID',
            'dynamic':'DYNAMIC',
            'static':'STATIC',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry',
            False, 
            [
            _MetaInfoClassMember('ipNetToMediaIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The interface on which this entry's equivalence
                is effective.  The interface identified by a
                particular value of this index is the same
                interface as identified by the same value of
                ifIndex.
                ''',
                'ipnettomediaifindex',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('ipNetToMediaNetAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IpAddress corresponding to the media-
                dependent `physical' address.
                ''',
                'ipnettomedianetaddress',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('ipNetToMediaPhysAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The media-dependent `physical' address.
                ''',
                'ipnettomediaphysaddress',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipNetToMediaType', REFERENCE_ENUM_CLASS, 'IpNetToMediaType_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry.IpNetToMediaType_Enum', 
                [], [], 
                '''                The type of mapping.
                
                Setting this object to the value invalid(2) has
                the effect of invalidating the corresponding entry
                in the ipNetToMediaTable.  That is, it effectively
                disassociates the interface identified with said
                entry from the mapping identified with said entry.
                It is an implementation-specific matter as to
                whether the agent removes an invalidated entry
                from the table.  Accordingly, management stations
                must be prepared to receive tabular information
                from agents that corresponds to entries not
                currently in use.  Proper interpretation of such
                entries requires examination of the relevant
                ipNetToMediaType object.
                ''',
                'ipnettomediatype',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ipNetToMediaEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IpNetToMediaTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IpNetToMediaTable',
            False, 
            [
            _MetaInfoClassMember('ipNetToMediaEntry', REFERENCE_LIST, 'IpNetToMediaEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry', 
                [], [], 
                '''                Each entry contains one IpAddress to `physical'
                address equivalence.
                ''',
                'ipnettomediaentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ipNetToMediaTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteProto_Enum' : _MetaInfoEnum('IpRouteProto_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'other':'OTHER',
            'local':'LOCAL',
            'netmgmt':'NETMGMT',
            'icmp':'ICMP',
            'egp':'EGP',
            'ggp':'GGP',
            'hello':'HELLO',
            'rip':'RIP',
            'is-is':'IS_IS',
            'es-is':'ES_IS',
            'ciscoIgrp':'CISCOIGRP',
            'bbnSpfIgp':'BBNSPFIGP',
            'ospf':'OSPF',
            'bgp':'BGP',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteType_Enum' : _MetaInfoEnum('IpRouteType_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'other':'OTHER',
            'invalid':'INVALID',
            'direct':'DIRECT',
            'indirect':'INDIRECT',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.IpRouteTable.IpRouteEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IpRouteTable.IpRouteEntry',
            False, 
            [
            _MetaInfoClassMember('ipRouteDest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of this route.  An
                entry with a value of 0.0.0.0 is considered a
                default route.  Multiple routes to a single
                destination can appear in the table, but access to
                such multiple entries is dependent on the table-
                access mechanisms defined by the network
                management protocol in use.
                ''',
                'iproutedest',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('ipRouteAge', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of seconds since this route was last
                updated or otherwise determined to be correct.
                Note that no semantics of `too old' can be implied
                except through knowledge of the routing protocol
                by which the route was learned.
                ''',
                'iprouteage',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The index value which uniquely identifies the
                local interface through which the next hop of this
                route should be reached.  The interface identified
                by a particular value of this index is the same
                interface as identified by the same value of
                ifIndex.
                ''',
                'iprouteifindex',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteInfo', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A reference to MIB definitions specific to the
                particular routing protocol which is responsible
                for this route, as determined by the value
                specified in the route's ipRouteProto value.  If
                this information is not present, its value should
                be set to the OBJECT IDENTIFIER { 0 0 }, which is
                a syntactically valid object identifier, and any
                conformant implementation of ASN.1 and BER must be
                able to generate and recognize this value.
                ''',
                'iprouteinfo',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Indicate the mask to be logical-ANDed with the
                destination address before being compared to the
                value in the ipRouteDest field.  For those systems
                that do not support arbitrary subnet masks, an
                agent constructs the value of the ipRouteMask by
                determining whether the value of the correspondent
                ipRouteDest field belong to a class-A, B, or C
                network, and then using one of:
                
                     mask           network
                     255.0.0.0      class-A
                     255.255.0.0    class-B
                     255.255.255.0  class-C
                
                If the value of the ipRouteDest is 0.0.0.0 (a
                default route), then the mask value is also
                0.0.0.0.  It should be noted that all IP routing
                subsystems implicitly use this mechanism.
                ''',
                'iproutemask',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteMetric1', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The primary routing metric for this route.  The
                semantics of this metric are determined by the
                routing-protocol specified in the route's
                ipRouteProto value.  If this metric is not used,
                its value should be set to -1.
                ''',
                'iproutemetric1',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteMetric2', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the
                routing-protocol specified in the route's
                ipRouteProto value.  If this metric is not used,
                its value should be set to -1.
                ''',
                'iproutemetric2',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteMetric3', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the
                routing-protocol specified in the route's
                ipRouteProto value.  If this metric is not used,
                its value should be set to -1.
                ''',
                'iproutemetric3',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteMetric4', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the
                routing-protocol specified in the route's
                ipRouteProto value.  If this metric is not used,
                its value should be set to -1.
                ''',
                'iproutemetric4',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteMetric5', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the
                routing-protocol specified in the route's
                ipRouteProto value.  If this metric is not used,
                its value should be set to -1.
                ''',
                'iproutemetric5',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteNextHop', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the next hop of this route.
                (In the case of a route bound to an interface
                which is realized via a broadcast media, the value
                of this field is the agent's IP address on that
                interface.)
                ''',
                'iproutenexthop',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteProto', REFERENCE_ENUM_CLASS, 'IpRouteProto_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteProto_Enum', 
                [], [], 
                '''                The routing mechanism via which this route was
                learned.  Inclusion of values for gateway routing
                protocols is not intended to imply that hosts
                should support those protocols.
                ''',
                'iprouteproto',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteType', REFERENCE_ENUM_CLASS, 'IpRouteType_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteType_Enum', 
                [], [], 
                '''                The type of route.  Note that the values
                direct(3) and indirect(4) refer to the notion of
                direct and indirect routing in the IP
                architecture.
                
                Setting this object to the value invalid(2) has
                the effect of invalidating the corresponding entry
                in the ipRouteTable object.  That is, it
                effectively disassociates the destination
                identified with said entry from the route
                identified with said entry.  It is an
                implementation-specific matter as to whether the
                agent removes an invalidated entry from the table.
                Accordingly, management stations must be prepared
                to receive tabular information from agents that
                corresponds to entries not currently in use.
                Proper interpretation of such entries requires
                examination of the relevant ipRouteType object.
                ''',
                'iproutetype',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ipRouteEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.IpRouteTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.IpRouteTable',
            False, 
            [
            _MetaInfoClassMember('ipRouteEntry', REFERENCE_LIST, 'IpRouteEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpRouteTable.IpRouteEntry', 
                [], [], 
                '''                A route to a particular destination.
                ''',
                'iprouteentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'ipRouteTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Snmp.SnmpEnableAuthenTraps_Enum' : _MetaInfoEnum('SnmpEnableAuthenTraps_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.Snmp' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Snmp',
            False, 
            [
            _MetaInfoClassMember('snmpEnableAuthenTraps', REFERENCE_ENUM_CLASS, 'SnmpEnableAuthenTraps_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Snmp.SnmpEnableAuthenTraps_Enum', 
                [], [], 
                '''                Indicates whether the SNMP agent process is
                permitted to generate authentication-failure
                traps.  The value of this object overrides any
                configuration information; as such, it provides a
                means whereby all authentication-failure traps may
                be disabled.
                
                Note that it is strongly recommended that this
                object be stored in non-volatile memory so that it
                remains constant between re-initializations of the
                network management system.
                ''',
                'snmpenableauthentraps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInASNParseErrs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of ASN.1 or BER errors
                encountered by the SNMP protocol entity when
                decoding received SNMP Messages.
                ''',
                'snmpinasnparseerrs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInBadCommunityNames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Messages delivered to
                the SNMP protocol entity which used a SNMP
                community name not known to said entity.
                ''',
                'snmpinbadcommunitynames',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInBadCommunityUses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Messages delivered to
                the SNMP protocol entity which represented an SNMP
                operation which was not allowed by the SNMP
                community named in the Message.
                ''',
                'snmpinbadcommunityuses',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInBadValues', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field is
                `badValue'.
                ''',
                'snmpinbadvalues',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInBadVersions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Messages which were
                delivered to the SNMP protocol entity and were for
                an unsupported SNMP version.
                ''',
                'snmpinbadversions',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInGenErrs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field is
                `genErr'.
                ''',
                'snmpingenerrs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInGetNexts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Get-Next PDUs which have
                been accepted and processed by the SNMP protocol
                entity.
                ''',
                'snmpingetnexts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInGetRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Get-Request PDUs which
                have been accepted and processed by the SNMP
                protocol entity.
                ''',
                'snmpingetrequests',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInGetResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Get-Response PDUs which
                have been accepted and processed by the SNMP
                protocol entity.
                ''',
                'snmpingetresponses',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInNoSuchNames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field is
                `noSuchName'.
                ''',
                'snmpinnosuchnames',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of Messages delivered to the
                SNMP entity from the transport service.
                ''',
                'snmpinpkts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInReadOnlys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number valid SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field is
                `readOnly'.  It should be noted that it is a
                protocol error to generate an SNMP PDU which
                contains the value `readOnly' in the error-status
                field, as such this object is provided as a means
                of detecting incorrect implementations of the
                SNMP.
                ''',
                'snmpinreadonlys',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInSetRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Set-Request PDUs which
                have been accepted and processed by the SNMP
                protocol entity.
                ''',
                'snmpinsetrequests',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInTooBigs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field is
                `tooBig'.
                ''',
                'snmpintoobigs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInTotalReqVars', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of MIB objects which have been
                retrieved successfully by the SNMP protocol entity
                as the result of receiving valid SNMP Get-Request
                and Get-Next PDUs.
                ''',
                'snmpintotalreqvars',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInTotalSetVars', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of MIB objects which have been
                altered successfully by the SNMP protocol entity
                as the result of receiving valid SNMP Set-Request
                PDUs.
                ''',
                'snmpintotalsetvars',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpInTraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Trap PDUs which have
                been accepted and processed by the SNMP protocol
                entity.
                ''',
                'snmpintraps',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutBadValues', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                generated by the SNMP protocol entity and for
                which the value of the error-status field is
                `badValue'.
                ''',
                'snmpoutbadvalues',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutGenErrs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                generated by the SNMP protocol entity and for
                which the value of the error-status field is
                `genErr'.
                ''',
                'snmpoutgenerrs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutGetNexts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Get-Next PDUs which have
                been generated by the SNMP protocol entity.
                ''',
                'snmpoutgetnexts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutGetRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Get-Request PDUs which
                have been generated by the SNMP protocol entity.
                ''',
                'snmpoutgetrequests',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutGetResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Get-Response PDUs which
                have been generated by the SNMP protocol entity.
                ''',
                'snmpoutgetresponses',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutNoSuchNames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                generated by the SNMP protocol entity and for
                which the value of the error-status is
                `noSuchName'.
                ''',
                'snmpoutnosuchnames',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Messages which were
                passed from the SNMP protocol entity to the
                transport service.
                ''',
                'snmpoutpkts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutSetRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Set-Request PDUs which
                have been generated by the SNMP protocol entity.
                ''',
                'snmpoutsetrequests',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutTooBigs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP PDUs which were
                generated by the SNMP protocol entity and for
                which the value of the error-status field is
                `tooBig.'
                ''',
                'snmpouttoobigs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmpOutTraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of SNMP Trap PDUs which have
                been generated by the SNMP protocol entity.
                ''',
                'snmpouttraps',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'snmp',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.System' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.System',
            False, 
            [
            _MetaInfoClassMember('sysContact', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The textual identification of the contact person
                for this managed node, together with information
                on how to contact this person.
                ''',
                'syscontact',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('sysDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A textual description of the entity.  This value
                should include the full name and version
                identification of the system's hardware type,
                software operating-system, and networking
                software.  It is mandatory that this only contain
                printable ASCII characters.
                ''',
                'sysdescr',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('sysLocation', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The physical location of this node (e.g.,
                `telephone closet, 3rd floor').
                ''',
                'syslocation',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('sysName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An administratively-assigned name for this
                managed node.  By convention, this is the node's
                fully-qualified domain name.
                ''',
                'sysname',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('sysObjectID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The vendor's authoritative identification of the
                network management subsystem contained in the
                entity.  This value is allocated within the SMI
                enterprises subtree (1.3.6.1.4.1) and provides an
                easy and unambiguous means for determining `what
                kind of box' is being managed.  For example, if
                vendor `Flintstones, Inc.' was assigned the
                subtree 1.3.6.1.4.1.4242, it could assign the
                identifier 1.3.6.1.4.1.4242.1.1 to its `Fred
                Router'.
                ''',
                'sysobjectid',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('sysServices', ATTRIBUTE, 'int' , None, None, 
                [(0, 127)], [], 
                '''                A value which indicates the set of services that
                this entity primarily offers.
                
                The value is a sum.  This sum initially takes the
                value zero, Then, for each layer, L, in the range
                1 through 7, that this node performs transactions
                for, 2 raised to (L - 1) is added to the sum.  For
                example, a node which performs primarily routing
                functions would have a value of 4 (2^(3-1)).  In
                contrast, a node which is a host offering
                application services would have a value of 72
                (2^(4-1) + 2^(7-1)).  Note that in the context of
                the Internet suite of protocols, values should be
                calculated accordingly:
                
                     layer  functionality
                         1  physical (e.g., repeaters)
                         2  datalink/subnetwork (e.g., bridges)
                         3  internet (e.g., IP gateways)
                         4  end-to-end  (e.g., IP hosts)
                         7  applications (e.g., mail relays)
                
                For systems including OSI protocols, layers 5 and
                6 may also be counted.
                ''',
                'sysservices',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('sysUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time (in hundredths of a second) since the
                network management portion of the system was last
                re-initialized.
                ''',
                'sysuptime',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'system',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Tcp.TcpRtoAlgorithm_Enum' : _MetaInfoEnum('TcpRtoAlgorithm_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'other':'OTHER',
            'constant':'CONSTANT',
            'rsre':'RSRE',
            'vanj':'VANJ',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.Tcp' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Tcp',
            False, 
            [
            _MetaInfoClassMember('tcpActiveOpens', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times TCP connections have made a
                direct transition to the SYN-SENT state from the
                CLOSED state.
                ''',
                'tcpactiveopens',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpAttemptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times TCP connections have made a
                direct transition to the CLOSED state from either
                the SYN-SENT state or the SYN-RCVD state, plus the
                number of times TCP connections have made a direct
                transition to the LISTEN state from the SYN-RCVD
                state.
                ''',
                'tcpattemptfails',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpCurrEstab', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of TCP connections for which the
                current state is either ESTABLISHED or CLOSE-
                WAIT.
                ''',
                'tcpcurrestab',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpEstabResets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times TCP connections have made a
                direct transition to the CLOSED state from either
                the ESTABLISHED state or the CLOSE-WAIT state.
                ''',
                'tcpestabresets',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpInErrs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments received in error
                (e.g., bad TCP checksums).
                ''',
                'tcpinerrs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpInSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments received, including
                those received in error.  This count includes
                segments received on currently established
                connections.
                ''',
                'tcpinsegs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpMaxConn', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The limit on the total number of TCP connections
                the entity can support.  In entities where the
                maximum number of connections is dynamic, this
                object should contain the value -1.
                ''',
                'tcpmaxconn',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpOutRsts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of TCP segments sent containing the
                RST flag.
                ''',
                'tcpoutrsts',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpOutSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments sent, including
                those on current connections but excluding those
                containing only retransmitted octets.
                ''',
                'tcpoutsegs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpPassiveOpens', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times TCP connections have made a
                direct transition to the SYN-RCVD state from the
                LISTEN state.
                ''',
                'tcppassiveopens',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpRetransSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments retransmitted - that
                is, the number of TCP segments transmitted
                containing one or more previously transmitted
                octets.
                ''',
                'tcpretranssegs',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpRtoAlgorithm', REFERENCE_ENUM_CLASS, 'TcpRtoAlgorithm_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Tcp.TcpRtoAlgorithm_Enum', 
                [], [], 
                '''                The algorithm used to determine the timeout value
                used for retransmitting unacknowledged octets.
                ''',
                'tcprtoalgorithm',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpRtoMax', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum value permitted by a TCP
                implementation for the retransmission timeout,
                measured in milliseconds.  More refined semantics
                for objects of this type depend upon the algorithm
                used to determine the retransmission timeout.  In
                particular, when the timeout algorithm is rsre(3),
                an object of this type has the semantics of the
                UBOUND quantity described in RFC 793.
                ''',
                'tcprtomax',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpRtoMin', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The minimum value permitted by a TCP
                implementation for the retransmission timeout,
                measured in milliseconds.  More refined semantics
                for objects of this type depend upon the algorithm
                used to determine the retransmission timeout.  In
                particular, when the timeout algorithm is rsre(3),
                an object of this type has the semantics of the
                LBOUND quantity described in RFC 793.
                ''',
                'tcprtomin',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'tcp',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum' : _MetaInfoEnum('TcpConnState_Enum', 'ydk.models.rfc1213.RFC1213_MIB',
        {
            'closed':'CLOSED',
            'listen':'LISTEN',
            'synSent':'SYNSENT',
            'synReceived':'SYNRECEIVED',
            'established':'ESTABLISHED',
            'finWait1':'FINWAIT1',
            'finWait2':'FINWAIT2',
            'closeWait':'CLOSEWAIT',
            'lastAck':'LASTACK',
            'closing':'CLOSING',
            'timeWait':'TIMEWAIT',
            'deleteTCB':'DELETETCB',
        }, 'RFC1213-MIB', _yang_ns._namespaces['RFC1213-MIB']),
    'RFC1213MIB.TcpConnTable.TcpConnEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.TcpConnTable.TcpConnEntry',
            False, 
            [
            _MetaInfoClassMember('tcpConnLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address for this TCP connection.  In
                the case of a connection in the listen state which
                is willing to accept connections for any IP
                interface associated with the node, the value
                0.0.0.0 is used.
                ''',
                'tcpconnlocaladdress',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('tcpConnLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcpconnlocalport',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('tcpConnRemAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The remote IP address for this TCP connection.
                ''',
                'tcpconnremaddress',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('tcpConnRemPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The remote port number for this TCP connection.
                ''',
                'tcpconnremport',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('tcpConnState', REFERENCE_ENUM_CLASS, 'TcpConnState_Enum' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum', 
                [], [], 
                '''                The state of this TCP connection.
                
                The only value which may be set by a management
                station is deleteTCB(12).  Accordingly, it is
                appropriate for an agent to return a `badValue'
                response if a management station attempts to set
                this object to any other value.
                
                If a management station sets this object to the
                value deleteTCB(12), then this has the effect of
                deleting the TCB (as defined in RFC 793) of the
                corresponding connection on the managed node,
                resulting in immediate termination of the
                connection.
                
                As an implementation-specific option, a RST
                segment may be sent from the managed node to the
                other TCP endpoint (note however that RST segments
                are not sent reliably).
                ''',
                'tcpconnstate',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'tcpConnEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.TcpConnTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.TcpConnTable',
            False, 
            [
            _MetaInfoClassMember('tcpConnEntry', REFERENCE_LIST, 'TcpConnEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.TcpConnTable.TcpConnEntry', 
                [], [], 
                '''                Information about a particular current TCP
                connection.  An object of this type is transient,
                in that it ceases to exist when (or soon after)
                the connection makes the transition to the CLOSED
                state.
                ''',
                'tcpconnentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'tcpConnTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.Udp' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.Udp',
            False, 
            [
            _MetaInfoClassMember('udpInDatagrams', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of UDP datagrams delivered to
                UDP users.
                ''',
                'udpindatagrams',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('udpInErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of received UDP datagrams that could
                not be delivered for reasons other than the lack
                of an application at the destination port.
                ''',
                'udpinerrors',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('udpNoPorts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of received UDP datagrams for
                which there was no application at the destination
                port.
                ''',
                'udpnoports',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('udpOutDatagrams', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of UDP datagrams sent from this
                entity.
                ''',
                'udpoutdatagrams',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'udp',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.UdpTable.UdpEntry' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.UdpTable.UdpEntry',
            False, 
            [
            _MetaInfoClassMember('udpLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address for this UDP listener.  In
                the case of a UDP listener which is willing to
                accept datagrams for any IP interface associated
                with the node, the value 0.0.0.0 is used.
                ''',
                'udplocaladdress',
                'RFC1213-MIB', True),
            _MetaInfoClassMember('udpLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The local port number for this UDP listener.
                ''',
                'udplocalport',
                'RFC1213-MIB', True),
            ],
            'RFC1213-MIB',
            'udpEntry',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB.UdpTable' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB.UdpTable',
            False, 
            [
            _MetaInfoClassMember('udpEntry', REFERENCE_LIST, 'UdpEntry' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.UdpTable.UdpEntry', 
                [], [], 
                '''                Information about a particular current UDP
                listener.
                ''',
                'udpentry',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'udpTable',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
    'RFC1213MIB' : {
        'meta_info' : _MetaInfoClass('RFC1213MIB',
            False, 
            [
            _MetaInfoClassMember('atTable', REFERENCE_CLASS, 'AtTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.AtTable', 
                [], [], 
                '''                The Address Translation tables contain the
                NetworkAddress to `physical' address equivalences.
                Some interfaces do not use translation tables for
                determining address equivalences (e.g., DDN-X.25
                has an algorithmic method); if all interfaces are
                of this type, then the Address Translation table
                is empty, i.e., has zero entries.
                ''',
                'attable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egp', REFERENCE_CLASS, 'Egp' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Egp', 
                [], [], 
                '''                ''',
                'egp',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('egpNeighTable', REFERENCE_CLASS, 'EgpNeighTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.EgpNeighTable', 
                [], [], 
                '''                The EGP neighbor table.
                ''',
                'egpneightable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('icmp', REFERENCE_CLASS, 'Icmp' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Icmp', 
                [], [], 
                '''                ''',
                'icmp',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ifTable', REFERENCE_CLASS, 'IfTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IfTable', 
                [], [], 
                '''                A list of interface entries.  The number of
                entries is given by the value of ifNumber.
                ''',
                'iftable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Interfaces', 
                [], [], 
                '''                ''',
                'interfaces',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Ip', 
                [], [], 
                '''                ''',
                'ip',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipAddrTable', REFERENCE_CLASS, 'IpAddrTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpAddrTable', 
                [], [], 
                '''                The table of addressing information relevant to
                this entity's IP addresses.
                ''',
                'ipaddrtable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipNetToMediaTable', REFERENCE_CLASS, 'IpNetToMediaTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpNetToMediaTable', 
                [], [], 
                '''                The IP Address Translation table used for mapping
                from IP addresses to physical addresses.
                ''',
                'ipnettomediatable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('ipRouteTable', REFERENCE_CLASS, 'IpRouteTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.IpRouteTable', 
                [], [], 
                '''                This entity's IP Routing table.
                ''',
                'iproutetable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Snmp', 
                [], [], 
                '''                ''',
                'snmp',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.System', 
                [], [], 
                '''                ''',
                'system',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Tcp', 
                [], [], 
                '''                ''',
                'tcp',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('tcpConnTable', REFERENCE_CLASS, 'TcpConnTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.TcpConnTable', 
                [], [], 
                '''                A table containing TCP connection-specific
                information.
                ''',
                'tcpconntable',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.Udp', 
                [], [], 
                '''                ''',
                'udp',
                'RFC1213-MIB', False),
            _MetaInfoClassMember('udpTable', REFERENCE_CLASS, 'UdpTable' , 'ydk.models.rfc1213.RFC1213_MIB', 'RFC1213MIB.UdpTable', 
                [], [], 
                '''                A table containing UDP listener information.
                ''',
                'udptable',
                'RFC1213-MIB', False),
            ],
            'RFC1213-MIB',
            'RFC1213-MIB',
            _yang_ns._namespaces['RFC1213-MIB'],
        'ydk.models.rfc1213.RFC1213_MIB'
        ),
    },
}
_meta_table['RFC1213MIB.AtTable.AtEntry']['meta_info'].parent =_meta_table['RFC1213MIB.AtTable']['meta_info']
_meta_table['RFC1213MIB.EgpNeighTable.EgpNeighEntry']['meta_info'].parent =_meta_table['RFC1213MIB.EgpNeighTable']['meta_info']
_meta_table['RFC1213MIB.IfTable.IfEntry']['meta_info'].parent =_meta_table['RFC1213MIB.IfTable']['meta_info']
_meta_table['RFC1213MIB.IpAddrTable.IpAddrEntry']['meta_info'].parent =_meta_table['RFC1213MIB.IpAddrTable']['meta_info']
_meta_table['RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry']['meta_info'].parent =_meta_table['RFC1213MIB.IpNetToMediaTable']['meta_info']
_meta_table['RFC1213MIB.IpRouteTable.IpRouteEntry']['meta_info'].parent =_meta_table['RFC1213MIB.IpRouteTable']['meta_info']
_meta_table['RFC1213MIB.TcpConnTable.TcpConnEntry']['meta_info'].parent =_meta_table['RFC1213MIB.TcpConnTable']['meta_info']
_meta_table['RFC1213MIB.UdpTable.UdpEntry']['meta_info'].parent =_meta_table['RFC1213MIB.UdpTable']['meta_info']
_meta_table['RFC1213MIB.AtTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Egp']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.EgpNeighTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Icmp']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.IfTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Interfaces']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Ip']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.IpAddrTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.IpNetToMediaTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.IpRouteTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Snmp']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.System']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Tcp']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.TcpConnTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.Udp']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
_meta_table['RFC1213MIB.UdpTable']['meta_info'].parent =_meta_table['RFC1213MIB']['meta_info']
