


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpaddressstatustcEnum' : _MetaInfoEnum('IpaddressstatustcEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'preferred':'preferred',
            'deprecated':'deprecated',
            'invalid':'invalid',
            'inaccessible':'inaccessible',
            'unknown':'unknown',
            'tentative':'tentative',
            'duplicate':'duplicate',
            'optimistic':'optimistic',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpaddressprefixorigintcEnum' : _MetaInfoEnum('IpaddressprefixorigintcEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'other':'other',
            'manual':'manual',
            'wellknown':'wellknown',
            'dhcp':'dhcp',
            'routeradv':'routeradv',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpaddressorigintcEnum' : _MetaInfoEnum('IpaddressorigintcEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'other':'other',
            'manual':'manual',
            'dhcp':'dhcp',
            'linklayer':'linklayer',
            'random':'random',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ip.IpforwardingEnum' : _MetaInfoEnum('IpforwardingEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'forwarding':'forwarding',
            'notForwarding':'notForwarding',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ip.Ipv6IpforwardingEnum' : _MetaInfoEnum('Ipv6IpforwardingEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'forwarding':'forwarding',
            'notForwarding':'notForwarding',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ip' : {
        'meta_info' : _MetaInfoClass('IpMib.Ip',
            False, 
            [
            _MetaInfoClassMember('ipAddressSpinLock', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                An advisory lock used to allow cooperating SNMP managers to
                coordinate their use of the set operation in creating or
                modifying rows within this table.
                
                In order to use this lock to coordinate the use of set
                operations, managers should first retrieve
                ipAddressTableSpinLock.  They should then determine the
                appropriate row to create or modify.  Finally, they should
                issue the appropriate set command, including the retrieved
                value of ipAddressSpinLock.  If another manager has altered
                the table in the meantime, then the value of
                ipAddressSpinLock will have changed, and the creation will
                fail as it will be specifying an incorrect value for
                ipAddressSpinLock.  It is suggested, but not required, that
                the ipAddressSpinLock be the first var bind for each set of
                objects representing a 'row' in a PDU.
                ''',
                'ipaddressspinlock',
                'IP-MIB', False),
            _MetaInfoClassMember('ipDefaultTTL', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The default value inserted into the Time-To-Live field of
                the IPv4 header of datagrams originated at this entity,
                whenever a TTL value is not supplied by the transport layer
                
                
                protocol.
                
                When this object is written, the entity should save the
                change to non-volatile storage and restore the object from
                non-volatile storage upon re-initialization of the system.
                Note: a stronger requirement is not used because this object
                was previously defined.
                ''',
                'ipdefaultttl',
                'IP-MIB', False),
            _MetaInfoClassMember('ipForwarding', REFERENCE_ENUM_CLASS, 'IpforwardingEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ip.IpforwardingEnum', 
                [], [], 
                '''                The indication of whether this entity is acting as an IPv4
                router in respect to the forwarding of datagrams received
                by, but not addressed to, this entity.  IPv4 routers forward
                datagrams.  IPv4 hosts do not (except those source-routed
                via the host).
                
                When this object is written, the entity should save the
                change to non-volatile storage and restore the object from
                non-volatile storage upon re-initialization of the system.
                Note: a stronger requirement is not used because this object
                was previously defined.
                ''',
                'ipforwarding',
                'IP-MIB', False),
            _MetaInfoClassMember('ipForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input datagrams for which this entity was not
                their final IPv4 destination, as a result of which an
                attempt was made to find a route to forward them to that
                final destination.  In entities which do not act as IPv4
                routers, this counter will include only those packets which
                
                
                were Source-Routed via this entity, and the Source-Route
                option processing was successful.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsInForwDatagrams.
                ''',
                'ipforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipFragCreates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IPv4 datagram fragments that have been
                generated as a result of fragmentation at this entity.
                
                This object has been deprecated as a new IP version neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsOutFragCreates.
                ''',
                'ipfragcreates',
                'IP-MIB', False),
            _MetaInfoClassMember('ipFragFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IPv4 datagrams that have been discarded
                because they needed to be fragmented at this entity but
                could not be, e.g., because their Don't Fragment flag was
                set.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsOutFragFails.
                ''',
                'ipfragfails',
                'IP-MIB', False),
            _MetaInfoClassMember('ipFragOKs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IPv4 datagrams that have been successfully
                fragmented at this entity.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsOutFragOKs.
                ''',
                'ipfragoks',
                'IP-MIB', False),
            _MetaInfoClassMember('ipInAddrErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input datagrams discarded because the IPv4
                address in their IPv4 header's destination field was not a
                valid address to be received at this entity.  This count
                includes invalid addresses (e.g., 0.0.0.0) and addresses of
                unsupported Classes (e.g., Class E).  For entities which are
                not IPv4 routers, and therefore do not forward datagrams,
                this counter includes datagrams discarded because the
                destination address was not a local address.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsInAddrErrors.
                ''',
                'ipinaddrerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('ipInDelivers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input datagrams successfully delivered
                to IPv4 user-protocols (including ICMP).
                
                This object has been deprecated as a new IP version neutral
                table has been added.  It is loosely replaced by
                
                
                ipSystemStatsIndelivers.
                ''',
                'ipindelivers',
                'IP-MIB', False),
            _MetaInfoClassMember('ipInDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IPv4 datagrams for which no problems
                were encountered to prevent their continued processing, but
                which were discarded (e.g., for lack of buffer space).  Note
                that this counter does not include any datagrams discarded
                while awaiting re-assembly.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsInDiscards.
                ''',
                'ipindiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipInHdrErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input datagrams discarded due to errors in
                their IPv4 headers, including bad checksums, version number
                mismatch, other format errors, time-to-live exceeded, errors
                discovered in processing their IPv4 options, etc.
                
                This object has been deprecated as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsInHdrErrors.
                ''',
                'ipinhdrerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('ipInReceives', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input datagrams received from
                interfaces, including those received in error.
                
                This object has been deprecated, as a new IP version-neutral
                
                
                table has been added.  It is loosely replaced by
                ipSystemStatsInRecieves.
                ''',
                'ipinreceives',
                'IP-MIB', False),
            _MetaInfoClassMember('ipInUnknownProtos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of locally-addressed datagrams received
                successfully but discarded because of an unknown or
                unsupported protocol.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsInUnknownProtos.
                ''',
                'ipinunknownprotos',
                'IP-MIB', False),
            _MetaInfoClassMember('ipOutDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of output IPv4 datagrams for which no problem was
                encountered to prevent their transmission to their
                destination, but which were discarded (e.g., for lack of
                buffer space).  Note that this counter would include
                datagrams counted in ipForwDatagrams if any such packets met
                this (discretionary) discard criterion.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsOutDiscards.
                ''',
                'ipoutdiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipOutNoRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IPv4 datagrams discarded because no route
                could be found to transmit them to their destination.  Note
                that this counter includes any packets counted in
                ipForwDatagrams which meet this `no-route' criterion.  Note
                that this includes any datagrams which a host cannot route
                because all of its default routers are down.
                
                This object has been deprecated, as a new IP version-neutral
                
                
                table has been added.  It is loosely replaced by
                ipSystemStatsOutNoRoutes.
                ''',
                'ipoutnoroutes',
                'IP-MIB', False),
            _MetaInfoClassMember('ipOutRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of IPv4 datagrams which local IPv4 user
                protocols (including ICMP) supplied to IPv4 in requests for
                transmission.  Note that this counter does not include any
                datagrams counted in ipForwDatagrams.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsOutRequests.
                ''',
                'ipoutrequests',
                'IP-MIB', False),
            _MetaInfoClassMember('ipReasmFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of failures detected by the IPv4 re-assembly
                algorithm (for whatever reason: timed out, errors, etc).
                Note that this is not necessarily a count of discarded IPv4
                fragments since some algorithms (notably the algorithm in
                RFC 815) can lose track of the number of fragments by
                combining them as they are received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsReasmFails.
                ''',
                'ipreasmfails',
                'IP-MIB', False),
            _MetaInfoClassMember('ipReasmOKs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IPv4 datagrams successfully re-assembled.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsReasmOKs.
                ''',
                'ipreasmoks',
                'IP-MIB', False),
            _MetaInfoClassMember('ipReasmReqds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IPv4 fragments received which needed to be
                reassembled at this entity.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                ipSystemStatsReasmReqds.
                ''',
                'ipreasmreqds',
                'IP-MIB', False),
            _MetaInfoClassMember('ipReasmTimeout', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of seconds that received fragments are
                held while they are awaiting reassembly at this entity.
                ''',
                'ipreasmtimeout',
                'IP-MIB', False),
            _MetaInfoClassMember('ipRoutingDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of routing entries which were chosen to be
                discarded even though they are valid.  One possible reason
                for discarding such an entry could be to free-up buffer
                space for other routing entries.
                
                
                This object was defined in pre-IPv6 versions of the IP MIB.
                It was implicitly IPv4 only, but the original specifications
                did not indicate this protocol restriction.  In order to
                clarify the specifications, this object has been deprecated
                and a similar, but more thoroughly clarified, object has
                been added to the IP-FORWARD-MIB.
                ''',
                'iproutingdiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv4InterfaceTableLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                a row in the ipv4InterfaceTable was added or deleted, or
                when an ipv4InterfaceReasmMaxSize or an
                ipv4InterfaceEnableStatus object was modified.
                
                If new objects are added to the ipv4InterfaceTable that
                require the ipv4InterfaceTableLastChange to be updated when
                they are modified, they must specify that requirement in
                their description clause.
                ''',
                'ipv4interfacetablelastchange',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceTableLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                a row in the ipv6InterfaceTable was added or deleted or when
                an ipv6InterfaceReasmMaxSize, ipv6InterfaceIdentifier,
                ipv6InterfaceEnableStatus, ipv6InterfaceReachableTime,
                ipv6InterfaceRetransmitTime, or ipv6InterfaceForwarding
                object was modified.
                
                If new objects are added to the ipv6InterfaceTable that
                require the ipv6InterfaceTableLastChange to be updated when
                they are modified, they must specify that requirement in
                their description clause.
                ''',
                'ipv6interfacetablelastchange',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6IpDefaultHopLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The default value inserted into the Hop Limit field of the
                IPv6 header of datagrams originated at this entity whenever
                a Hop Limit value is not supplied by the transport layer
                protocol.
                
                When this object is written, the entity SHOULD save the
                change to non-volatile storage and restore the object from
                non-volatile storage upon re-initialization of the system.
                ''',
                'ipv6ipdefaulthoplimit',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6IpForwarding', REFERENCE_ENUM_CLASS, 'Ipv6IpforwardingEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ip.Ipv6IpforwardingEnum', 
                [], [], 
                '''                The indication of whether this entity is acting as an IPv6
                router on any interface in respect to the forwarding of
                datagrams received by, but not addressed to, this entity.
                IPv6 routers forward datagrams.  IPv6 hosts do not (except
                those source-routed via the host).
                
                When this object is written, the entity SHOULD save the
                change to non-volatile storage and restore the object from
                non-volatile storage upon re-initialization of the system.
                ''',
                'ipv6ipforwarding',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertSpinLock', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                An advisory lock used to allow cooperating SNMP managers to
                coordinate their use of the set operation in creating or
                modifying rows within this table.
                
                In order to use this lock to coordinate the use of set
                operations, managers should first retrieve
                ipv6RouterAdvertSpinLock.  They should then determine the
                appropriate row to create or modify.  Finally, they should
                issue the appropriate set command including the retrieved
                value of ipv6RouterAdvertSpinLock.  If another manager has
                altered the table in the meantime, then the value of
                ipv6RouterAdvertSpinLock will have changed and the creation
                will fail as it will be specifying an incorrect value for
                ipv6RouterAdvertSpinLock.  It is suggested, but not
                required, that the ipv6RouterAdvertSpinLock be the first var
                bind for each set of objects representing a 'row' in a PDU.
                ''',
                'ipv6routeradvertspinlock',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ip',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Iptrafficstats' : {
        'meta_info' : _MetaInfoClass('IpMib.Iptrafficstats',
            False, 
            [
            _MetaInfoClassMember('ipIfStatsTableLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                a row in the ipIfStatsTable was added or deleted.
                
                If new objects are added to the ipIfStatsTable that require
                the ipIfStatsTableLastChange to be updated when they are
                modified, they must specify that requirement in their
                description clause.
                ''',
                'ipifstatstablelastchange',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipTrafficStats',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Icmp' : {
        'meta_info' : _MetaInfoClass('IpMib.Icmp',
            False, 
            [
            _MetaInfoClassMember('icmpInAddrMaskReps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Address Mask Reply messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinaddrmaskreps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInAddrMasks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Address Mask Request messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinaddrmasks',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInDestUnreachs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Destination Unreachable messages
                received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpindestunreachs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInEchoReps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Echo Reply messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinechoreps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInEchos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Echo (request) messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinechos',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP messages which the entity received but
                determined as having ICMP-specific errors (bad ICMP
                checksums, bad length, etc.).
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                icmpStatsInErrors.
                ''',
                'icmpinerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInMsgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ICMP messages which the entity received.
                Note that this counter includes all those counted by
                icmpInErrors.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                icmpStatsInMsgs.
                ''',
                'icmpinmsgs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInParmProbs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Parameter Problem messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinparmprobs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInRedirects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Redirect messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinredirects',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInSrcQuenchs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Source Quench messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpinsrcquenchs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInTimeExcds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Time Exceeded messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpintimeexcds',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInTimestampReps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Timestamp Reply messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpintimestampreps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpInTimestamps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Timestamp (request) messages received.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpintimestamps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutAddrMaskReps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Address Mask Reply messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutaddrmaskreps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutAddrMasks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Address Mask Request messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutaddrmasks',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutDestUnreachs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Destination Unreachable messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutdestunreachs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutEchoReps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Echo Reply messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutechoreps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutEchos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Echo (request) messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutechos',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP messages which this entity did not send
                due to problems discovered within ICMP, such as a lack of
                buffers.  This value should not include errors discovered
                outside the ICMP layer, such as the inability of IP to route
                the resultant datagram.  In some implementations, there may
                be no types of error which contribute to this counter's
                value.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                icmpStatsOutErrors.
                ''',
                'icmpouterrors',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutMsgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ICMP messages which this entity
                attempted to send.  Note that this counter includes all
                those counted by icmpOutErrors.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by
                icmpStatsOutMsgs.
                ''',
                'icmpoutmsgs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutParmProbs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Parameter Problem messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutparmprobs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutRedirects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Redirect messages sent.  For a host, this
                object will always be zero, since hosts do not send
                redirects.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutredirects',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutSrcQuenchs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Source Quench messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpoutsrcquenchs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutTimeExcds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Time Exceeded messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpouttimeexcds',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutTimestampReps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Timestamp Reply messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpouttimestampreps',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpOutTimestamps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP Timestamp (request) messages sent.
                
                This object has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by a column in
                the icmpMsgStatsTable.
                ''',
                'icmpouttimestamps',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'icmp',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipaddrtable.Ipaddrentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipaddrtable.Ipaddrentry',
            False, 
            [
            _MetaInfoClassMember('ipAdEntAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address to which this entry's addressing
                information pertains.
                ''',
                'ipadentaddr',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAdEntBcastAddr', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                The value of the least-significant bit in the IPv4 broadcast
                address used for sending datagrams on the (logical)
                interface associated with the IPv4 address of this entry.
                For example, when the Internet standard all-ones broadcast
                address is used, the value will be 1.  This value applies to
                both the subnet and network broadcast addresses used by the
                entity on this (logical) interface.
                ''',
                'ipadentbcastaddr',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAdEntIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value which uniquely identifies the interface to
                which this entry is applicable.  The interface identified by
                a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipadentifindex',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAdEntNetMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The subnet mask associated with the IPv4 address of this
                entry.  The value of the mask is an IPv4 address with all
                the network bits set to 1 and all the hosts bits set to 0.
                ''',
                'ipadentnetmask',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAdEntReasmMaxSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The size of the largest IPv4 datagram which this entity can
                re-assemble from incoming IPv4 fragmented datagrams received
                on this interface.
                ''',
                'ipadentreasmmaxsize',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipAddrEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipaddrtable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipaddrtable',
            False, 
            [
            _MetaInfoClassMember('ipAddrEntry', REFERENCE_LIST, 'Ipaddrentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddrtable.Ipaddrentry', 
                [], [], 
                '''                The addressing information for one of this entity's IPv4
                addresses.
                ''',
                'ipaddrentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipAddrTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipnettomediatable.Ipnettomediaentry.IpnettomediatypeEnum' : _MetaInfoEnum('IpnettomediatypeEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'other':'other',
            'invalid':'invalid',
            'dynamic':'dynamic',
            'static':'static',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipnettomediatable.Ipnettomediaentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipnettomediatable.Ipnettomediaentry',
            False, 
            [
            _MetaInfoClassMember('ipNetToMediaIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The interface on which this entry's equivalence is
                effective.  The interface identified by a particular value
                of this index is the same interface as identified by the
                
                
                same value of the IF-MIB's ifIndex.
                
                This object predates the rule limiting index objects to a
                max access value of 'not-accessible' and so continues to use
                a value of 'read-create'.
                ''',
                'ipnettomediaifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipNetToMediaNetAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IpAddress corresponding to the media-dependent
                `physical' address.
                
                This object predates the rule limiting index objects to a
                max access value of 'not-accessible' and so continues to use
                a value of 'read-create'.
                ''',
                'ipnettomedianetaddress',
                'IP-MIB', True),
            _MetaInfoClassMember('ipNetToMediaPhysAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 65535)], [], 
                '''                The media-dependent `physical' address.  This object should
                return 0 when this entry is in the 'incomplete' state.
                
                As the entries in this table are typically not persistent
                when this object is written the entity should not save the
                change to non-volatile storage.  Note: a stronger
                requirement is not used because this object was previously
                defined.
                ''',
                'ipnettomediaphysaddress',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToMediaType', REFERENCE_ENUM_CLASS, 'IpnettomediatypeEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettomediatable.Ipnettomediaentry.IpnettomediatypeEnum', 
                [], [], 
                '''                The type of mapping.
                
                Setting this object to the value invalid(2) has the effect
                
                
                of invalidating the corresponding entry in the
                ipNetToMediaTable.  That is, it effectively dis-associates
                the interface identified with said entry from the mapping
                identified with said entry.  It is an implementation-
                specific matter as to whether the agent removes an
                invalidated entry from the table.  Accordingly, management
                stations must be prepared to receive tabular information
                from agents that corresponds to entries not currently in
                use.  Proper interpretation of such entries requires
                examination of the relevant ipNetToMediaType object.
                
                As the entries in this table are typically not persistent
                when this object is written the entity should not save the
                change to non-volatile storage.  Note: a stronger
                requirement is not used because this object was previously
                defined.
                ''',
                'ipnettomediatype',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipNetToMediaEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipnettomediatable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipnettomediatable',
            False, 
            [
            _MetaInfoClassMember('ipNetToMediaEntry', REFERENCE_LIST, 'Ipnettomediaentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettomediatable.Ipnettomediaentry', 
                [], [], 
                '''                Each entry contains one IpAddress to `physical' address
                equivalence.
                ''',
                'ipnettomediaentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipNetToMediaTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv4Interfacetable.Ipv4Interfaceentry.Ipv4InterfaceenablestatusEnum' : _MetaInfoEnum('Ipv4InterfaceenablestatusEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'up':'up',
            'down':'down',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipv4Interfacetable.Ipv4Interfaceentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv4Interfacetable.Ipv4Interfaceentry',
            False, 
            [
            _MetaInfoClassMember('ipv4InterfaceIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface to
                which this entry is applicable.  The interface identified by
                a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipv4interfaceifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipv4InterfaceEnableStatus', REFERENCE_ENUM_CLASS, 'Ipv4InterfaceenablestatusEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv4Interfacetable.Ipv4Interfaceentry.Ipv4InterfaceenablestatusEnum', 
                [], [], 
                '''                The indication of whether IPv4 is enabled (up) or disabled
                (down) on this interface.  This object does not affect the
                state of the interface itself, only its connection to an
                IPv4 stack.  The IF-MIB should be used to control the state
                of the interface.
                ''',
                'ipv4interfaceenablestatus',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv4InterfaceReasmMaxSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The size of the largest IPv4 datagram that this entity can
                re-assemble from incoming IPv4 fragmented datagrams received
                on this interface.
                ''',
                'ipv4interfacereasmmaxsize',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv4InterfaceRetransmitTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time between retransmissions of ARP requests to a
                neighbor when resolving the address or when probing the
                reachability of a neighbor.
                ''',
                'ipv4interfaceretransmittime',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv4InterfaceEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv4Interfacetable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv4Interfacetable',
            False, 
            [
            _MetaInfoClassMember('ipv4InterfaceEntry', REFERENCE_LIST, 'Ipv4Interfaceentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv4Interfacetable.Ipv4Interfaceentry', 
                [], [], 
                '''                An entry containing IPv4-specific information for a specific
                interface.
                ''',
                'ipv4interfaceentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv4InterfaceTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceenablestatusEnum' : _MetaInfoEnum('Ipv6InterfaceenablestatusEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'up':'up',
            'down':'down',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceforwardingEnum' : _MetaInfoEnum('Ipv6InterfaceforwardingEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'forwarding':'forwarding',
            'notForwarding':'notForwarding',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipv6Interfacetable.Ipv6Interfaceentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv6Interfacetable.Ipv6Interfaceentry',
            False, 
            [
            _MetaInfoClassMember('ipv6InterfaceIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface to
                which this entry is applicable.  The interface identified by
                a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipv6interfaceifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipv6InterfaceEnableStatus', REFERENCE_ENUM_CLASS, 'Ipv6InterfaceenablestatusEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceenablestatusEnum', 
                [], [], 
                '''                The indication of whether IPv6 is enabled (up) or disabled
                (down) on this interface.  This object does not affect the
                state of the interface itself, only its connection to an
                IPv6 stack.  The IF-MIB should be used to control the state
                of the interface.
                
                When this object is written, the entity SHOULD save the
                change to non-volatile storage and restore the object from
                non-volatile storage upon re-initialization of the system.
                ''',
                'ipv6interfaceenablestatus',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceForwarding', REFERENCE_ENUM_CLASS, 'Ipv6InterfaceforwardingEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceforwardingEnum', 
                [], [], 
                '''                The indication of whether this entity is acting as an IPv6
                router on this interface with respect to the forwarding of
                datagrams received by, but not addressed to, this entity.
                IPv6 routers forward datagrams.  IPv6 hosts do not (except
                those source-routed via the host).
                
                This object is constrained by ipv6IpForwarding and is
                ignored if ipv6IpForwarding is set to notForwarding.  Those
                systems that do not provide per-interface control of the
                forwarding function should set this object to forwarding for
                all interfaces and allow the ipv6IpForwarding object to
                control the forwarding capability.
                
                When this object is written, the entity SHOULD save the
                change to non-volatile storage and restore the object from
                non-volatile storage upon re-initialization of the system.
                ''',
                'ipv6interfaceforwarding',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Interface Identifier for this interface.  The Interface
                Identifier is combined with an address prefix to form an
                interface address.
                
                By default, the Interface Identifier is auto-configured
                according to the rules of the link type to which this
                interface is attached.
                
                
                A zero length identifier may be used where appropriate.  One
                possible example is a loopback interface.
                ''',
                'ipv6interfaceidentifier',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceReachableTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time a neighbor is considered reachable after receiving
                a reachability confirmation.
                ''',
                'ipv6interfacereachabletime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceReasmMaxSize', ATTRIBUTE, 'int' , None, None, 
                [('1500', '65535')], [], 
                '''                The size of the largest IPv6 datagram that this entity can
                re-assemble from incoming IPv6 fragmented datagrams received
                on this interface.
                ''',
                'ipv6interfacereasmmaxsize',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceRetransmitTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time between retransmissions of Neighbor Solicitation
                messages to a neighbor when resolving the address or when
                probing the reachability of a neighbor.
                ''',
                'ipv6interfaceretransmittime',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv6InterfaceEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv6Interfacetable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv6Interfacetable',
            False, 
            [
            _MetaInfoClassMember('ipv6InterfaceEntry', REFERENCE_LIST, 'Ipv6Interfaceentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Interfacetable.Ipv6Interfaceentry', 
                [], [], 
                '''                An entry containing IPv6-specific information for a given
                interface.
                ''',
                'ipv6interfaceentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv6InterfaceTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipsystemstatstable.Ipsystemstatsentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipsystemstatstable.Ipsystemstatsentry',
            False, 
            [
            _MetaInfoClassMember('ipSystemStatsIPVersion', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The IP version of this row.
                ''',
                'ipsystemstatsipversion',
                'IP-MIB', True),
            _MetaInfoClassMember('ipSystemStatsDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                any one or more of this entry's counters suffered a
                discontinuity.
                
                If no such discontinuities have occurred since the last re-
                initialization of the local management subsystem, then this
                object contains a zero value.
                ''',
                'ipsystemstatsdiscontinuitytime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP broadcast datagrams received.  This object
                counts the same datagrams as ipSystemStatsInBcastPkts but
                allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                
                
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcinbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInDelivers', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of datagrams successfully delivered to IP
                user-protocols (including ICMP).  This object counts the
                same packets as ipSystemStatsInDelivers, but allows for
                larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcindelivers',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of input datagrams for which this entity was not
                their final IP destination and for which this entity
                attempted to find a route to forward them to that final
                destination.  This object counts the same packets as
                ipSystemStatsInForwDatagrams, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcinforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received in IP multicast
                datagrams.  This object counts the same octets as
                ipSystemStatsInMcastOctets, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcinmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP multicast datagrams received.  This object
                counts the same datagrams as ipSystemStatsInMcastPkts but
                allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcinmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received in input IP datagrams,
                including those received in error.  This object counts the
                same octets as ipSystemStatsInOctets, but allows for larger
                
                
                values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcinoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCInReceives', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of input IP datagrams received, including
                those received in error.  This object counts the same
                datagrams as ipSystemStatsInReceives, but allows for larger
                values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcinreceives',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP broadcast datagrams transmitted.  This
                object counts the same datagrams as
                ipSystemStatsOutBcastPkts, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcoutbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of datagrams for which this entity was not their
                final IP destination and for which it was successful in
                finding a path to their final destination.  This object
                counts the same packets as ipSystemStatsOutForwDatagrams,
                but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcoutforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets transmitted in IP multicast
                datagrams.  This object counts the same octets as
                ipSystemStatsOutMcastOctets, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcoutmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP multicast datagrams transmitted.  This
                object counts the same datagrams as
                ipSystemStatsOutMcastPkts, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcoutmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets in IP datagrams delivered to the
                lower layers for transmission.  This objects counts the same
                octets as ipSystemStatsOutOctets, but allows for larger
                values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                
                
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcoutoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of IP datagrams that local IP user-
                protocols (including ICMP) supplied to IP in requests for
                transmission.  This object counts the same packets as
                ipSystemStatsOutRequests, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcoutrequests',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsHCOutTransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of IP datagrams that this entity supplied
                to the lower layers for transmission.  This object counts
                the same datagrams as ipSystemStatsOutTransmits, but allows
                for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatshcouttransmits',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInAddrErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded because the IP
                address in their IP header's destination field was not a
                valid address to be received at this entity.  This count
                includes invalid addresses (e.g., ::0).  For entities
                that are not IP routers and therefore do not forward
                
                
                datagrams, this counter includes datagrams discarded
                because the destination address was not a local address.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinaddrerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP broadcast datagrams received.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInDelivers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of datagrams successfully delivered to IP
                user-protocols (including ICMP).
                
                When tracking interface statistics, the counter of the
                interface to which these datagrams were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the datagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsindelivers',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams for which no problems were
                encountered to prevent their continued processing, but
                were discarded (e.g., for lack of buffer space).  Note that
                this counter does not include any datagrams discarded while
                awaiting re-assembly.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsindiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input datagrams for which this entity was not
                their final IP destination and for which this entity
                attempted to find a route to forward them to that final
                destination.  In entities that do not act as IP routers,
                this counter will include only those datagrams that were
                Source-Routed via this entity, and the Source-Route
                processing was successful.
                
                When tracking interface statistics, the counter of the
                incoming interface is incremented for each datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInHdrErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded due to errors in
                their IP headers, including version number mismatch, other
                format errors, hop count exceeded, errors discovered in
                processing their IP options, etc.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinhdrerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets received in IP multicast
                datagrams.  Octets from datagrams counted in
                ipSystemStatsInMcastPkts MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP multicast datagrams received.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInNoRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded because no route
                could be found to transmit them to their destination.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinnoroutes',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets received in input IP datagrams,
                including those received in error.  Octets from datagrams
                counted in ipSystemStatsInReceives MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInReceives', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input IP datagrams received, including
                those received in error.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinreceives',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInTruncatedPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded because the
                datagram frame didn't carry enough data.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsintruncatedpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsInUnknownProtos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of locally-addressed IP datagrams received
                successfully but discarded because of an unknown or
                unsupported protocol.
                
                When tracking interface statistics, the counter of the
                interface to which these datagrams were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the datagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsinunknownprotos',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP broadcast datagrams transmitted.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of output IP datagrams for which no problem was
                encountered to prevent their transmission to their
                destination, but were discarded (e.g., for lack of
                buffer space).  Note that this counter would include
                
                
                datagrams counted in ipSystemStatsOutForwDatagrams if any
                such datagrams met this (discretionary) discard criterion.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutdiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of datagrams for which this entity was not their
                final IP destination and for which it was successful in
                finding a path to their final destination.  In entities
                that do not act as IP routers, this counter will include
                only those datagrams that were Source-Routed via this
                entity, and the Source-Route processing was successful.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                forwarded datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutFragCreates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of output datagram fragments that have been
                generated as a result of IP fragmentation.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutfragcreates',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutFragFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams that have been discarded because
                they needed to be fragmented but could not be.  This
                includes IPv4 packets that have the DF bit set and IPv6
                packets that are being forwarded and exceed the outgoing
                link MTU.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for an unsuccessfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutfragfails',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutFragOKs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams that have been successfully
                fragmented.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutfragoks',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutFragReqds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams that would require fragmentation
                in order to be transmitted.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutfragreqds',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets transmitted in IP multicast
                datagrams.  Octets from datagrams counted in
                
                
                ipSystemStatsOutMcastPkts MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP multicast datagrams transmitted.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutNoRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of locally generated IP datagrams discarded
                because no route could be found to transmit them to their
                destination.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutnoroutes',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets in IP datagrams delivered to the
                lower layers for transmission.  Octets from datagrams
                counted in ipSystemStatsOutTransmits MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of IP datagrams that local IP user-
                protocols (including ICMP) supplied to IP in requests for
                transmission.  Note that this counter does not include any
                datagrams counted in ipSystemStatsOutForwDatagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsoutrequests',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsOutTransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of IP datagrams that this entity supplied
                to the lower layers for transmission.  This includes
                datagrams generated locally and those forwarded by this
                entity.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                
                
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsouttransmits',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsReasmFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of failures detected by the IP re-assembly
                algorithm (for whatever reason: timed out, errors, etc.).
                Note that this is not necessarily a count of discarded IP
                fragments since some algorithms (notably the algorithm in
                RFC 815) can lose track of the number of fragments by
                combining them as they are received.
                
                When tracking interface statistics, the counter of the
                interface to which these fragments were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the fragments.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsreasmfails',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsReasmOKs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams successfully reassembled.
                
                When tracking interface statistics, the counter of the
                interface to which these datagrams were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the datagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsreasmoks',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsReasmReqds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP fragments received that needed to be
                reassembled at this interface.
                
                When tracking interface statistics, the counter of the
                interface to which these fragments were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the fragments.
                
                Discontinuities in the value of this counter can occur at
                
                
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipSystemStatsDiscontinuityTime.
                ''',
                'ipsystemstatsreasmreqds',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsRefreshRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum reasonable polling interval for this entry.
                This object provides an indication of the minimum amount of
                time required to update the counters in this entry.
                ''',
                'ipsystemstatsrefreshrate',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipSystemStatsEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipsystemstatstable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipsystemstatstable',
            False, 
            [
            _MetaInfoClassMember('ipSystemStatsEntry', REFERENCE_LIST, 'Ipsystemstatsentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipsystemstatstable.Ipsystemstatsentry', 
                [], [], 
                '''                A statistics entry containing system-wide objects for a
                particular IP version.
                ''',
                'ipsystemstatsentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipSystemStatsTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipifstatstable.Ipifstatsentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipifstatstable.Ipifstatsentry',
            False, 
            [
            _MetaInfoClassMember('ipIfStatsIPVersion', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The IP version of this row.
                ''',
                'ipifstatsipversion',
                'IP-MIB', True),
            _MetaInfoClassMember('ipIfStatsIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface to
                which this entry is applicable.  The interface identified by
                a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipifstatsifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipIfStatsDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                
                
                any one or more of this entry's counters suffered a
                discontinuity.
                
                If no such discontinuities have occurred since the last re-
                initialization of the local management subsystem, then this
                object contains a zero value.
                ''',
                'ipifstatsdiscontinuitytime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP broadcast datagrams received.  This object
                counts the same datagrams as ipIfStatsInBcastPkts, but
                allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcinbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInDelivers', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of datagrams successfully delivered to IP
                user-protocols (including ICMP).  This object counts the
                same packets as ipIfStatsInDelivers, but allows for larger
                values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcindelivers',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of input datagrams for which this entity was not
                their final IP destination and for which this entity
                attempted to find a route to forward them to that final
                destination.  This object counts the same packets as
                
                
                ipIfStatsInForwDatagrams, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcinforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received in IP multicast
                datagrams.  This object counts the same octets as
                ipIfStatsInMcastOctets, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcinmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP multicast datagrams received.  This object
                counts the same datagrams as ipIfStatsInMcastPkts, but
                allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcinmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received in input IP datagrams,
                including those received in error.  This object counts the
                same octets as ipIfStatsInOctets, but allows for larger
                values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcinoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCInReceives', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of input IP datagrams received, including
                those received in error.  This object counts the same
                datagrams as ipIfStatsInReceives, but allows for larger
                values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcinreceives',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP broadcast datagrams transmitted.  This
                object counts the same datagrams as ipIfStatsOutBcastPkts,
                but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcoutbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of datagrams for which this entity was not their
                final IP destination and for which it was successful in
                finding a path to their final destination.  This object
                counts the same packets as ipIfStatsOutForwDatagrams, but
                allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                
                
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcoutforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets transmitted in IP multicast
                datagrams.  This object counts the same octets as
                ipIfStatsOutMcastOctets, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcoutmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of IP multicast datagrams transmitted.  This
                object counts the same datagrams as ipIfStatsOutMcastPkts,
                but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                
                
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcoutmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets in IP datagrams delivered to the
                lower layers for transmission.  This objects counts the same
                octets as ipIfStatsOutOctets, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcoutoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of IP datagrams that local IP user-
                protocols (including ICMP) supplied to IP in requests for
                transmission.  This object counts the same packets as
                
                
                ipIfStatsOutRequests, but allows for larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcoutrequests',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsHCOutTransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of IP datagrams that this entity supplied
                to the lower layers for transmission.  This object counts
                the same datagrams as ipIfStatsOutTransmits, but allows for
                larger values.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatshcouttransmits',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInAddrErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded because the IP
                address in their IP header's destination field was not a
                valid address to be received at this entity.  This count
                includes invalid addresses (e.g., ::0).  For entities that
                are not IP routers and therefore do not forward datagrams,
                this counter includes datagrams discarded because the
                destination address was not a local address.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinaddrerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP broadcast datagrams received.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInDelivers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of datagrams successfully delivered to IP
                user-protocols (including ICMP).
                
                When tracking interface statistics, the counter of the
                interface to which these datagrams were addressed is
                incremented.  This interface might not be the same as the
                
                
                input interface for some of the datagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsindelivers',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams for which no problems were
                encountered to prevent their continued processing, but
                were discarded (e.g., for lack of buffer space).  Note that
                this counter does not include any datagrams discarded while
                awaiting re-assembly.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsindiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input datagrams for which this entity was not
                their final IP destination and for which this entity
                attempted to find a route to forward them to that final
                destination.  In entities that do not act as IP routers,
                this counter will include only those datagrams that were
                Source-Routed via this entity, and the Source-Route
                processing was successful.
                
                When tracking interface statistics, the counter of the
                incoming interface is incremented for each datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInHdrErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded due to errors in
                their IP headers, including version number mismatch, other
                format errors, hop count exceeded, errors discovered in
                processing their IP options, etc.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinhdrerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets received in IP multicast
                
                
                datagrams.  Octets from datagrams counted in
                ipIfStatsInMcastPkts MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP multicast datagrams received.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInNoRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded because no route
                could be found to transmit them to their destination.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinnoroutes',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets received in input IP datagrams,
                including those received in error.  Octets from datagrams
                counted in ipIfStatsInReceives MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInReceives', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input IP datagrams received, including
                those received in error.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinreceives',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInTruncatedPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input IP datagrams discarded because the
                datagram frame didn't carry enough data.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsintruncatedpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsInUnknownProtos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of locally-addressed IP datagrams received
                successfully but discarded because of an unknown or
                unsupported protocol.
                
                When tracking interface statistics, the counter of the
                interface to which these datagrams were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the datagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                
                
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsinunknownprotos',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutBcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP broadcast datagrams transmitted.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutbcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of output IP datagrams for which no problem was
                encountered to prevent their transmission to their
                destination, but were discarded (e.g., for lack of
                buffer space).  Note that this counter would include
                datagrams counted in ipIfStatsOutForwDatagrams if any such
                datagrams met this (discretionary) discard criterion.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutdiscards',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutForwDatagrams', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of datagrams for which this entity was not their
                final IP destination and for which it was successful in
                finding a path to their final destination.  In entities
                that do not act as IP routers, this counter will include
                only those datagrams that were Source-Routed via this
                entity, and the Source-Route processing was successful.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                forwarded datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutforwdatagrams',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutFragCreates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of output datagram fragments that have been
                generated as a result of IP fragmentation.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutfragcreates',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutFragFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams that have been discarded because
                they needed to be fragmented but could not be.  This
                includes IPv4 packets that have the DF bit set and IPv6
                packets that are being forwarded and exceed the outgoing
                link MTU.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for an unsuccessfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutfragfails',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutFragOKs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams that have been successfully
                fragmented.
                
                When tracking interface statistics, the counter of the
                
                
                outgoing interface is incremented for a successfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutfragoks',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutFragReqds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams that would require fragmentation
                in order to be transmitted.
                
                When tracking interface statistics, the counter of the
                outgoing interface is incremented for a successfully
                fragmented datagram.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutfragreqds',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutMcastOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets transmitted in IP multicast
                datagrams.  Octets from datagrams counted in
                ipIfStatsOutMcastPkts MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutmcastoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutMcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP multicast datagrams transmitted.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutmcastpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets in IP datagrams delivered to the
                lower layers for transmission.  Octets from datagrams
                counted in ipIfStatsOutTransmits MUST be counted here.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutoctets',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of IP datagrams that local IP user-
                protocols (including ICMP) supplied to IP in requests for
                transmission.  Note that this counter does not include any
                datagrams counted in ipIfStatsOutForwDatagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsoutrequests',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsOutTransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of IP datagrams that this entity supplied
                to the lower layers for transmission.  This includes
                datagrams generated locally and those forwarded by this
                entity.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsouttransmits',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsReasmFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of failures detected by the IP re-assembly
                algorithm (for whatever reason: timed out, errors, etc.).
                Note that this is not necessarily a count of discarded IP
                fragments since some algorithms (notably the algorithm in
                RFC 815) can lose track of the number of fragments by
                combining them as they are received.
                
                When tracking interface statistics, the counter of the
                interface to which these fragments were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the fragments.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsreasmfails',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsReasmOKs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP datagrams successfully reassembled.
                
                When tracking interface statistics, the counter of the
                interface to which these datagrams were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the datagrams.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsreasmoks',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsReasmReqds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP fragments received that needed to be
                reassembled at this interface.
                
                When tracking interface statistics, the counter of the
                interface to which these fragments were addressed is
                incremented.  This interface might not be the same as the
                input interface for some of the fragments.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ipIfStatsDiscontinuityTime.
                ''',
                'ipifstatsreasmreqds',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsRefreshRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum reasonable polling interval for this entry.
                This object provides an indication of the minimum amount of
                time required to update the counters in this entry.
                ''',
                'ipifstatsrefreshrate',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipIfStatsEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipifstatstable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipifstatstable',
            False, 
            [
            _MetaInfoClassMember('ipIfStatsEntry', REFERENCE_LIST, 'Ipifstatsentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipifstatstable.Ipifstatsentry', 
                [], [], 
                '''                An interface statistics entry containing objects for a
                particular interface and version of IP.
                ''',
                'ipifstatsentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipIfStatsTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipaddressprefixtable.Ipaddressprefixentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipaddressprefixtable.Ipaddressprefixentry',
            False, 
            [
            _MetaInfoClassMember('ipAddressPrefixIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface on
                which this prefix is configured.  The interface identified
                by a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipaddressprefixifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAddressPrefixType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of ipAddressPrefix.
                ''',
                'ipaddressprefixtype',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAddressPrefixPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address prefix.  The address type of this object is
                specified in ipAddressPrefixType.  The length of this object
                is the standard length for objects of that type (4 or 16
                bytes).  Any bits after ipAddressPrefixLength must be zero.
                
                Implementors need to be aware that, if the size of
                ipAddressPrefixPrefix exceeds 114 octets, then OIDS of
                instances of columns in this row will have more than 128
                sub-identifiers and cannot be accessed using SNMPv1,
                SNMPv2c, or SNMPv3.
                ''',
                'ipaddressprefixprefix',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAddressPrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The prefix length associated with this prefix.
                
                The value 0 has no special meaning for this object.  It
                simply refers to address '::/0'.
                ''',
                'ipaddressprefixlength',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAddressPrefixAdvPreferredLifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining length of time, in seconds, that this prefix
                will continue to be preferred, i.e., time until deprecation.
                
                A value of 4,294,967,295 represents infinity.
                
                The address generated from a deprecated prefix should no
                longer be used as a source address in new communications,
                but packets received on such an interface are processed as
                expected.
                
                The default for IPv4 prefixes is 4,294,967,295 (infinity).
                ''',
                'ipaddressprefixadvpreferredlifetime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressPrefixAdvValidLifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining length of time, in seconds, that this prefix
                will continue to be valid, i.e., time until invalidation.  A
                value of 4,294,967,295 represents infinity.
                
                The address generated from an invalidated prefix should not
                appear as the destination or source address of a packet.
                
                
                The default for IPv4 prefixes is 4,294,967,295 (infinity).
                ''',
                'ipaddressprefixadvvalidlifetime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressPrefixAutonomousFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Autonomous address configuration flag.  When true(1),
                indicates that this prefix can be used for autonomous
                address configuration (i.e., can be used to form a local
                interface address).  If false(2), it is not used to auto-
                configure a local interface address.
                
                The default for IPv4 prefixes is 'false(2)'.
                ''',
                'ipaddressprefixautonomousflag',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressPrefixOnLinkFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object has the value 'true(1)', if this prefix can be
                used for on-link determination; otherwise, the value is
                'false(2)'.
                
                The default for IPv4 prefixes is 'true(1)'.
                ''',
                'ipaddressprefixonlinkflag',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressPrefixOrigin', REFERENCE_ENUM_CLASS, 'IpaddressprefixorigintcEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpaddressprefixorigintcEnum', 
                [], [], 
                '''                The origin of this prefix.
                ''',
                'ipaddressprefixorigin',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipAddressPrefixEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipaddressprefixtable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipaddressprefixtable',
            False, 
            [
            _MetaInfoClassMember('ipAddressPrefixEntry', REFERENCE_LIST, 'Ipaddressprefixentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddressprefixtable.Ipaddressprefixentry', 
                [], [], 
                '''                An entry in the ipAddressPrefixTable.
                ''',
                'ipaddressprefixentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipAddressPrefixTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipaddresstable.Ipaddressentry.IpaddresstypeEnum' : _MetaInfoEnum('IpaddresstypeEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'unicast':'unicast',
            'anycast':'anycast',
            'broadcast':'broadcast',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipaddresstable.Ipaddressentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipaddresstable.Ipaddressentry',
            False, 
            [
            _MetaInfoClassMember('ipAddressAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of ipAddressAddr.
                ''',
                'ipaddressaddrtype',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAddressAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address to which this entry's addressing information
                
                
                pertains.  The address type of this object is specified in
                ipAddressAddrType.
                
                Implementors need to be aware that if the size of
                ipAddressAddr exceeds 116 octets, then OIDS of instances of
                columns in this row will have more than 128 sub-identifiers
                and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'ipaddressaddr',
                'IP-MIB', True),
            _MetaInfoClassMember('ipAddressCreated', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this entry was created.
                If this entry was created prior to the last re-
                initialization of the local network management subsystem,
                then this object contains a zero value.
                ''',
                'ipaddresscreated',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface to
                which this entry is applicable.  The interface identified by
                a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipaddressifindex',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressLastChanged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this entry was last
                updated.  If this entry was updated prior to the last re-
                initialization of the local network management subsystem,
                then this object contains a zero value.
                ''',
                'ipaddresslastchanged',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressOrigin', REFERENCE_ENUM_CLASS, 'IpaddressorigintcEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpaddressorigintcEnum', 
                [], [], 
                '''                The origin of the address.
                ''',
                'ipaddressorigin',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressPrefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A pointer to the row in the prefix table to which this
                address belongs.  May be { 0 0 } if there is no such row.
                ''',
                'ipaddressprefix',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                The RowStatus TC requires that this DESCRIPTION clause
                states under which circumstances other objects in this row
                
                
                can be modified.  The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                
                A conceptual row can not be made active until the
                ipAddressIfIndex has been set to a valid index.
                ''',
                'ipaddressrowstatus',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressStatus', REFERENCE_ENUM_CLASS, 'IpaddressstatustcEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpaddressstatustcEnum', 
                [], [], 
                '''                The status of the address, describing if the address can be
                used for communication.
                
                In the absence of other information, an IPv4 address is
                always preferred(1).
                ''',
                'ipaddressstatus',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  If this object
                has a value of 'permanent', then no other objects are
                required to be able to be modified.
                ''',
                'ipaddressstoragetype',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressType', REFERENCE_ENUM_CLASS, 'IpaddresstypeEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddresstable.Ipaddressentry.IpaddresstypeEnum', 
                [], [], 
                '''                The type of address.  broadcast(3) is not a valid value for
                IPv6 addresses (RFC 3513).
                ''',
                'ipaddresstype',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipAddressEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipaddresstable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipaddresstable',
            False, 
            [
            _MetaInfoClassMember('ipAddressEntry', REFERENCE_LIST, 'Ipaddressentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddresstable.Ipaddressentry', 
                [], [], 
                '''                An address mapping for a particular interface.
                ''',
                'ipaddressentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipAddressTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicalstateEnum' : _MetaInfoEnum('IpnettophysicalstateEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'reachable':'reachable',
            'stale':'stale',
            'delay':'delay',
            'probe':'probe',
            'invalid':'invalid',
            'unknown':'unknown',
            'incomplete':'incomplete',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicaltypeEnum' : _MetaInfoEnum('IpnettophysicaltypeEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'other':'other',
            'invalid':'invalid',
            'dynamic':'dynamic',
            'static':'static',
            'local':'local',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipnettophysicaltable.Ipnettophysicalentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipnettophysicaltable.Ipnettophysicalentry',
            False, 
            [
            _MetaInfoClassMember('ipNetToPhysicalIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface to
                which this entry is applicable.  The interface identified by
                a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipnettophysicalifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipNetToPhysicalNetAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of ipNetToPhysicalNetAddress.
                ''',
                'ipnettophysicalnetaddresstype',
                'IP-MIB', True),
            _MetaInfoClassMember('ipNetToPhysicalNetAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP Address corresponding to the media-dependent
                `physical' address.  The address type of this object is
                specified in ipNetToPhysicalAddressType.
                
                Implementors need to be aware that if the size of
                
                
                ipNetToPhysicalNetAddress exceeds 115 octets, then OIDS of
                instances of columns in this row will have more than 128
                sub-identifiers and cannot be accessed using SNMPv1,
                SNMPv2c, or SNMPv3.
                ''',
                'ipnettophysicalnetaddress',
                'IP-MIB', True),
            _MetaInfoClassMember('ipNetToPhysicalLastUpdated', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this entry was last
                updated.  If this entry was updated prior to the last re-
                initialization of the local network management subsystem,
                then this object contains a zero value.
                ''',
                'ipnettophysicallastupdated',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToPhysicalPhysAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 65535)], [], 
                '''                The media-dependent `physical' address.
                
                As the entries in this table are typically not persistent
                when this object is written the entity SHOULD NOT save the
                change to non-volatile storage.
                ''',
                'ipnettophysicalphysaddress',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToPhysicalRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                The RowStatus TC requires that this DESCRIPTION clause
                states under which circumstances other objects in this row
                can be modified.  The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                
                A conceptual row can not be made active until the
                ipNetToPhysicalPhysAddress object has been set.
                
                Note that if the ipNetToPhysicalType is set to 'invalid',
                the managed node may delete the entry independent of the
                state of this object.
                ''',
                'ipnettophysicalrowstatus',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToPhysicalState', REFERENCE_ENUM_CLASS, 'IpnettophysicalstateEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicalstateEnum', 
                [], [], 
                '''                The Neighbor Unreachability Detection state for the
                interface when the address mapping in this entry is used.
                If Neighbor Unreachability Detection is not in use (e.g. for
                IPv4), this object is always unknown(6).
                ''',
                'ipnettophysicalstate',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToPhysicalType', REFERENCE_ENUM_CLASS, 'IpnettophysicaltypeEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicaltypeEnum', 
                [], [], 
                '''                The type of mapping.
                
                Setting this object to the value invalid(2) has the effect
                of invalidating the corresponding entry in the
                ipNetToPhysicalTable.  That is, it effectively dis-
                associates the interface identified with said entry from the
                mapping identified with said entry.  It is an
                implementation-specific matter as to whether the agent
                
                
                removes an invalidated entry from the table.  Accordingly,
                management stations must be prepared to receive tabular
                information from agents that corresponds to entries not
                currently in use.  Proper interpretation of such entries
                requires examination of the relevant ipNetToPhysicalType
                object.
                
                The 'dynamic(3)' type indicates that the IP address to
                physical addresses mapping has been dynamically resolved
                using e.g., IPv4 ARP or the IPv6 Neighbor Discovery
                protocol.
                
                The 'static(4)' type indicates that the mapping has been
                statically configured.  Both of these refer to entries that
                provide mappings for other entities addresses.
                
                The 'local(5)' type indicates that the mapping is provided
                for an entity's own interface address.
                
                As the entries in this table are typically not persistent
                when this object is written the entity SHOULD NOT save the
                change to non-volatile storage.
                ''',
                'ipnettophysicaltype',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipNetToPhysicalEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipnettophysicaltable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipnettophysicaltable',
            False, 
            [
            _MetaInfoClassMember('ipNetToPhysicalEntry', REFERENCE_LIST, 'Ipnettophysicalentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettophysicaltable.Ipnettophysicalentry', 
                [], [], 
                '''                Each entry contains one IP address to `physical' address
                equivalence.
                ''',
                'ipnettophysicalentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipNetToPhysicalTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry',
            False, 
            [
            _MetaInfoClassMember('ipv6ScopeZoneIndexIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface to
                which these scopes belong.  The interface identified by a
                particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipv6scopezoneindexifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipv6ScopeZoneIndex3', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope 3 on this interface.
                ''',
                'ipv6scopezoneindex3',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndex6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope 6 on this interface.
                ''',
                'ipv6scopezoneindex6',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndex7', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope 7 on this interface.
                ''',
                'ipv6scopezoneindex7',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndex9', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope 9 on this interface.
                ''',
                'ipv6scopezoneindex9',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexA', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope A on this interface.
                ''',
                'ipv6scopezoneindexa',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexAdminLocal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for the admin-local scope on this interface.
                ''',
                'ipv6scopezoneindexadminlocal',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexB', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope B on this interface.
                ''',
                'ipv6scopezoneindexb',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexC', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope C on this interface.
                ''',
                'ipv6scopezoneindexc',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexD', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for scope D on this interface.
                ''',
                'ipv6scopezoneindexd',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexLinkLocal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for the link-local scope on this interface.
                ''',
                'ipv6scopezoneindexlinklocal',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexOrganizationLocal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for the organization-local scope on this
                interface.
                ''',
                'ipv6scopezoneindexorganizationlocal',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexSiteLocal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The zone index for the site-local scope on this interface.
                ''',
                'ipv6scopezoneindexsitelocal',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv6ScopeZoneIndexEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv6Scopezoneindextable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv6Scopezoneindextable',
            False, 
            [
            _MetaInfoClassMember('ipv6ScopeZoneIndexEntry', REFERENCE_LIST, 'Ipv6Scopezoneindexentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry', 
                [], [], 
                '''                Each entry contains the list of scope identifiers on a given
                interface.
                ''',
                'ipv6scopezoneindexentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv6ScopeZoneIndexTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipdefaultroutertable.Ipdefaultrouterentry.IpdefaultrouterpreferenceEnum' : _MetaInfoEnum('IpdefaultrouterpreferenceEnum', 'ydk.models.cisco_ios_xe.IP_MIB',
        {
            'reserved':'reserved',
            'low':'low',
            'medium':'medium',
            'high':'high',
        }, 'IP-MIB', _yang_ns._namespaces['IP-MIB']),
    'IpMib.Ipdefaultroutertable.Ipdefaultrouterentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipdefaultroutertable.Ipdefaultrouterentry',
            False, 
            [
            _MetaInfoClassMember('ipDefaultRouterAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type for this row.
                ''',
                'ipdefaultrouteraddresstype',
                'IP-MIB', True),
            _MetaInfoClassMember('ipDefaultRouterAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of the default router represented by this
                row.  The address type of this object is specified in
                ipDefaultRouterAddressType.
                
                Implementers need to be aware that if the size of
                ipDefaultRouterAddress exceeds 115 octets, then OIDS of
                instances of columns in this row will have more than 128
                sub-identifiers and cannot be accessed using SNMPv1,
                SNMPv2c, or SNMPv3.
                ''',
                'ipdefaultrouteraddress',
                'IP-MIB', True),
            _MetaInfoClassMember('ipDefaultRouterIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface by
                which the router can be reached.  The interface identified
                by a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipdefaultrouterifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipDefaultRouterLifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remaining length of time, in seconds, that this router
                will continue to be useful as a default router.  A value of
                zero indicates that it is no longer useful as a default
                router.  It is left to the implementer of the MIB as to
                whether a router with a lifetime of zero is removed from the
                list.
                
                For IPv6, this value should be extracted from the router
                advertisement messages.
                ''',
                'ipdefaultrouterlifetime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipDefaultRouterPreference', REFERENCE_ENUM_CLASS, 'IpdefaultrouterpreferenceEnum' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipdefaultroutertable.Ipdefaultrouterentry.IpdefaultrouterpreferenceEnum', 
                [], [], 
                '''                An indication of preference given to this router as a
                default router as described in he Default Router
                Preferences document.  Treating the value as a
                2 bit signed integer allows for simple arithmetic
                comparisons.
                
                For IPv4 routers or IPv6 routers that are not using the
                updated router advertisement format, this object is set to
                medium (0).
                ''',
                'ipdefaultrouterpreference',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipDefaultRouterEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipdefaultroutertable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipdefaultroutertable',
            False, 
            [
            _MetaInfoClassMember('ipDefaultRouterEntry', REFERENCE_LIST, 'Ipdefaultrouterentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipdefaultroutertable.Ipdefaultrouterentry', 
                [], [], 
                '''                Each entry contains information about a default router known
                to this entity.
                ''',
                'ipdefaultrouterentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipDefaultRouterTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry',
            False, 
            [
            _MetaInfoClassMember('ipv6RouterAdvertIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index value that uniquely identifies the interface on
                which router advertisements constructed with this
                information will be transmitted.  The interface identified
                by a particular value of this index is the same interface as
                identified by the same value of the IF-MIB's ifIndex.
                ''',
                'ipv6routeradvertifindex',
                'IP-MIB', True),
            _MetaInfoClassMember('ipv6RouterAdvertCurHopLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The default value to be placed in the current hop limit
                field in router advertisements sent from this interface.
                
                
                The value should be set to the current diameter of the
                Internet.
                
                A value of zero in the router advertisement indicates that
                the advertisement isn't specifying a value for curHopLimit.
                
                The default should be set to the value specified in the IANA
                web pages (www.iana.org) at the time of implementation.
                ''',
                'ipv6routeradvertcurhoplimit',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertDefaultLifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('4', '9000')], [], 
                '''                The value to be placed in the router lifetime field of
                router advertisements sent from this interface.  This value
                MUST be either 0 or between ipv6RouterAdvertMaxInterval and
                9000 seconds.
                
                A value of zero indicates that the router is not to be used
                as a default router.
                
                The default is 3 * ipv6RouterAdvertMaxInterval.
                ''',
                'ipv6routeradvertdefaultlifetime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertLinkMTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value to be placed in MTU options sent by the router on
                this interface.
                
                A value of zero indicates that no MTU options are sent.
                ''',
                'ipv6routeradvertlinkmtu',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertManagedFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The true/false value to be placed into the 'managed address
                configuration' flag field in router advertisements sent from
                this interface.
                ''',
                'ipv6routeradvertmanagedflag',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertMaxInterval', ATTRIBUTE, 'int' , None, None, 
                [('4', '1800')], [], 
                '''                The maximum time allowed between sending unsolicited router
                
                
                advertisements from this interface.
                ''',
                'ipv6routeradvertmaxinterval',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertMinInterval', ATTRIBUTE, 'int' , None, None, 
                [('3', '1350')], [], 
                '''                The minimum time allowed between sending unsolicited router
                advertisements from this interface.
                
                The default is 0.33 * ipv6RouterAdvertMaxInterval, however,
                in the case of a low value for ipv6RouterAdvertMaxInterval,
                the minimum value for this object is restricted to 3.
                ''',
                'ipv6routeradvertmininterval',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertOtherConfigFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The true/false value to be placed into the 'other stateful
                configuration' flag field in router advertisements sent from
                this interface.
                ''',
                'ipv6routeradvertotherconfigflag',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertReachableTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                The value to be placed in the reachable time field in router
                advertisement messages sent from this interface.
                
                A value of zero in the router advertisement indicates that
                the advertisement isn't specifying a value for reachable
                time.
                ''',
                'ipv6routeradvertreachabletime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertRetransmitTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value to be placed in the retransmit timer field in
                router advertisements sent from this interface.
                
                A value of zero in the router advertisement indicates that
                the advertisement isn't specifying a value for retrans
                time.
                ''',
                'ipv6routeradvertretransmittime',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                As all objects in this conceptual row have default values, a
                row can be created and made active by setting this object
                appropriately.
                
                The RowStatus TC requires that this DESCRIPTION clause
                states under which circumstances other objects in this row
                can be modified.  The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ipv6routeradvertrowstatus',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertSendAdverts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A flag indicating whether the router sends periodic
                router advertisements and responds to router solicitations
                on this interface.
                ''',
                'ipv6routeradvertsendadverts',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv6RouterAdvertEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Ipv6Routeradverttable' : {
        'meta_info' : _MetaInfoClass('IpMib.Ipv6Routeradverttable',
            False, 
            [
            _MetaInfoClassMember('ipv6RouterAdvertEntry', REFERENCE_LIST, 'Ipv6Routeradvertentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry', 
                [], [], 
                '''                An entry containing information used to construct router
                advertisements.
                
                Information in this table is persistent, and when this
                object is written, the entity SHOULD save the change to
                non-volatile storage.
                ''',
                'ipv6routeradvertentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'ipv6RouterAdvertTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Icmpstatstable.Icmpstatsentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Icmpstatstable.Icmpstatsentry',
            False, 
            [
            _MetaInfoClassMember('icmpStatsIPVersion', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The IP version of the statistics.
                ''',
                'icmpstatsipversion',
                'IP-MIB', True),
            _MetaInfoClassMember('icmpStatsInErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP messages that the entity received but
                determined as having ICMP-specific errors (bad ICMP
                checksums, bad length, etc.).
                ''',
                'icmpstatsinerrors',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpStatsInMsgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ICMP messages that the entity received.
                Note that this counter includes all those counted by
                icmpStatsInErrors.
                ''',
                'icmpstatsinmsgs',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpStatsOutErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ICMP messages that this entity did not send
                due to problems discovered within ICMP, such as a lack of
                buffers.  This value should not include errors discovered
                outside the ICMP layer, such as the inability of IP to route
                the resultant datagram.  In some implementations, there may
                be no types of error that contribute to this counter's
                value.
                ''',
                'icmpstatsouterrors',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpStatsOutMsgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ICMP messages that the entity attempted
                to send.  Note that this counter includes all those counted
                by icmpStatsOutErrors.
                ''',
                'icmpstatsoutmsgs',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'icmpStatsEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Icmpstatstable' : {
        'meta_info' : _MetaInfoClass('IpMib.Icmpstatstable',
            False, 
            [
            _MetaInfoClassMember('icmpStatsEntry', REFERENCE_LIST, 'Icmpstatsentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Icmpstatstable.Icmpstatsentry', 
                [], [], 
                '''                A conceptual row in the icmpStatsTable.
                ''',
                'icmpstatsentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'icmpStatsTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Icmpmsgstatstable.Icmpmsgstatsentry' : {
        'meta_info' : _MetaInfoClass('IpMib.Icmpmsgstatstable.Icmpmsgstatsentry',
            False, 
            [
            _MetaInfoClassMember('icmpMsgStatsIPVersion', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The IP version of the statistics.
                ''',
                'icmpmsgstatsipversion',
                'IP-MIB', True),
            _MetaInfoClassMember('icmpMsgStatsType', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The ICMP type field of the message type being counted by
                this row.
                
                Note that ICMP message types are scoped by the address type
                in use.
                ''',
                'icmpmsgstatstype',
                'IP-MIB', True),
            _MetaInfoClassMember('icmpMsgStatsInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input packets for this AF and type.
                ''',
                'icmpmsgstatsinpkts',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpMsgStatsOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of output packets for this AF and type.
                ''',
                'icmpmsgstatsoutpkts',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'icmpMsgStatsEntry',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib.Icmpmsgstatstable' : {
        'meta_info' : _MetaInfoClass('IpMib.Icmpmsgstatstable',
            False, 
            [
            _MetaInfoClassMember('icmpMsgStatsEntry', REFERENCE_LIST, 'Icmpmsgstatsentry' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Icmpmsgstatstable.Icmpmsgstatsentry', 
                [], [], 
                '''                A conceptual row in the icmpMsgStatsTable.
                
                The system should track each ICMP type value, even if that
                ICMP type is not supported by the system.  However, a
                given row need not be instantiated unless a message of that
                type has been processed, i.e., the row for
                icmpMsgStatsType=X MAY be instantiated before but MUST be
                instantiated after the first message with Type=X is
                received or transmitted.  After receiving or transmitting
                any succeeding messages with Type=X, the relevant counter
                must be incremented.
                ''',
                'icmpmsgstatsentry',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'icmpMsgStatsTable',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
    'IpMib' : {
        'meta_info' : _MetaInfoClass('IpMib',
            False, 
            [
            _MetaInfoClassMember('icmp', REFERENCE_CLASS, 'Icmp' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Icmp', 
                [], [], 
                '''                ''',
                'icmp',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpMsgStatsTable', REFERENCE_CLASS, 'Icmpmsgstatstable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Icmpmsgstatstable', 
                [], [], 
                '''                The table of system-wide per-version, per-message type ICMP
                counters.
                ''',
                'icmpmsgstatstable',
                'IP-MIB', False),
            _MetaInfoClassMember('icmpStatsTable', REFERENCE_CLASS, 'Icmpstatstable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Icmpstatstable', 
                [], [], 
                '''                The table of generic system-wide ICMP counters.
                ''',
                'icmpstatstable',
                'IP-MIB', False),
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ip', 
                [], [], 
                '''                ''',
                'ip',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressPrefixTable', REFERENCE_CLASS, 'Ipaddressprefixtable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddressprefixtable', 
                [], [], 
                '''                This table allows the user to determine the source of an IP
                address or set of IP addresses, and allows other tables to
                share the information via pointer rather than by copying.
                
                For example, when the node configures both a unicast and
                anycast address for a prefix, the ipAddressPrefix objects
                for those addresses will point to a single row in this
                table.
                
                This table primarily provides support for IPv6 prefixes, and
                several of the objects are less meaningful for IPv4.  The
                table continues to allow IPv4 addresses to allow future
                flexibility.  In order to promote a common configuration,
                this document includes suggestions for default values for
                IPv4 prefixes.  Each of these values may be overridden if an
                object is meaningful to the node.
                
                All prefixes used by this entity should be included in this
                table independent of how the entity learned the prefix.
                (This table isn't limited to prefixes learned from router
                
                
                advertisements.)
                ''',
                'ipaddressprefixtable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddressTable', REFERENCE_CLASS, 'Ipaddresstable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddresstable', 
                [], [], 
                '''                This table contains addressing information relevant to the
                entity's interfaces.
                
                This table does not contain multicast address information.
                Tables for such information should be contained in multicast
                specific MIBs, such as RFC 3019.
                
                While this table is writable, the user will note that
                several objects, such as ipAddressOrigin, are not.  The
                intention in allowing a user to write to this table is to
                allow them to add or remove any entry that isn't
                
                
                permanent.  The user should be allowed to modify objects
                and entries when that would not cause inconsistencies
                within the table.  Allowing write access to objects, such
                as ipAddressOrigin, could allow a user to insert an entry
                and then label it incorrectly.
                
                Note well: When including IPv6 link-local addresses in this
                table, the entry must use an InetAddressType of 'ipv6z' in
                order to differentiate between the possible interfaces.
                ''',
                'ipaddresstable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipAddrTable', REFERENCE_CLASS, 'Ipaddrtable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipaddrtable', 
                [], [], 
                '''                The table of addressing information relevant to this
                entity's IPv4 addresses.
                
                This table has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by the
                ipAddressTable although several objects that weren't deemed
                useful weren't carried forward while another
                (ipAdEntReasmMaxSize) was moved to the ipv4InterfaceTable.
                ''',
                'ipaddrtable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipDefaultRouterTable', REFERENCE_CLASS, 'Ipdefaultroutertable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipdefaultroutertable', 
                [], [], 
                '''                The table used to describe the default routers known to this
                
                
                entity.
                ''',
                'ipdefaultroutertable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipIfStatsTable', REFERENCE_CLASS, 'Ipifstatstable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipifstatstable', 
                [], [], 
                '''                The table containing per-interface traffic statistics.  This
                table and the ipSystemStatsTable contain similar objects
                whose difference is in their granularity.  Where this table
                contains per-interface statistics, the ipSystemStatsTable
                contains the same statistics, but counted on a system wide
                basis.
                ''',
                'ipifstatstable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToMediaTable', REFERENCE_CLASS, 'Ipnettomediatable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettomediatable', 
                [], [], 
                '''                The IPv4 Address Translation table used for mapping from
                IPv4 addresses to physical addresses.
                
                This table has been deprecated, as a new IP version-neutral
                table has been added.  It is loosely replaced by the
                ipNetToPhysicalTable.
                ''',
                'ipnettomediatable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipNetToPhysicalTable', REFERENCE_CLASS, 'Ipnettophysicaltable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipnettophysicaltable', 
                [], [], 
                '''                The IP Address Translation table used for mapping from IP
                addresses to physical addresses.
                
                The Address Translation tables contain the IP address to
                'physical' address equivalences.  Some interfaces do not use
                translation tables for determining address equivalences
                (e.g., DDN-X.25 has an algorithmic method); if all
                interfaces are of this type, then the Address Translation
                table is empty, i.e., has zero entries.
                
                While many protocols may be used to populate this table, ARP
                and Neighbor Discovery are the most likely
                options.
                ''',
                'ipnettophysicaltable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipSystemStatsTable', REFERENCE_CLASS, 'Ipsystemstatstable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipsystemstatstable', 
                [], [], 
                '''                The table containing system wide, IP version specific
                traffic statistics.  This table and the ipIfStatsTable
                contain similar objects whose difference is in their
                granularity.  Where this table contains system wide traffic
                statistics, the ipIfStatsTable contains the same statistics
                but counted on a per-interface basis.
                ''',
                'ipsystemstatstable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipTrafficStats', REFERENCE_CLASS, 'Iptrafficstats' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Iptrafficstats', 
                [], [], 
                '''                ''',
                'iptrafficstats',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv4InterfaceTable', REFERENCE_CLASS, 'Ipv4Interfacetable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv4Interfacetable', 
                [], [], 
                '''                The table containing per-interface IPv4-specific
                information.
                ''',
                'ipv4interfacetable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6InterfaceTable', REFERENCE_CLASS, 'Ipv6Interfacetable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Interfacetable', 
                [], [], 
                '''                The table containing per-interface IPv6-specific
                information.
                ''',
                'ipv6interfacetable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6RouterAdvertTable', REFERENCE_CLASS, 'Ipv6Routeradverttable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Routeradverttable', 
                [], [], 
                '''                The table containing information used to construct router
                advertisements.
                ''',
                'ipv6routeradverttable',
                'IP-MIB', False),
            _MetaInfoClassMember('ipv6ScopeZoneIndexTable', REFERENCE_CLASS, 'Ipv6Scopezoneindextable' , 'ydk.models.cisco_ios_xe.IP_MIB', 'IpMib.Ipv6Scopezoneindextable', 
                [], [], 
                '''                The table used to describe IPv6 unicast and multicast scope
                zones.
                
                For those objects that have names rather than numbers, the
                names were chosen to coincide with the names used in the
                IPv6 address architecture document. 
                ''',
                'ipv6scopezoneindextable',
                'IP-MIB', False),
            ],
            'IP-MIB',
            'IP-MIB',
            _yang_ns._namespaces['IP-MIB'],
        'ydk.models.cisco_ios_xe.IP_MIB'
        ),
    },
}
_meta_table['IpMib.Ipaddrtable.Ipaddrentry']['meta_info'].parent =_meta_table['IpMib.Ipaddrtable']['meta_info']
_meta_table['IpMib.Ipnettomediatable.Ipnettomediaentry']['meta_info'].parent =_meta_table['IpMib.Ipnettomediatable']['meta_info']
_meta_table['IpMib.Ipv4Interfacetable.Ipv4Interfaceentry']['meta_info'].parent =_meta_table['IpMib.Ipv4Interfacetable']['meta_info']
_meta_table['IpMib.Ipv6Interfacetable.Ipv6Interfaceentry']['meta_info'].parent =_meta_table['IpMib.Ipv6Interfacetable']['meta_info']
_meta_table['IpMib.Ipsystemstatstable.Ipsystemstatsentry']['meta_info'].parent =_meta_table['IpMib.Ipsystemstatstable']['meta_info']
_meta_table['IpMib.Ipifstatstable.Ipifstatsentry']['meta_info'].parent =_meta_table['IpMib.Ipifstatstable']['meta_info']
_meta_table['IpMib.Ipaddressprefixtable.Ipaddressprefixentry']['meta_info'].parent =_meta_table['IpMib.Ipaddressprefixtable']['meta_info']
_meta_table['IpMib.Ipaddresstable.Ipaddressentry']['meta_info'].parent =_meta_table['IpMib.Ipaddresstable']['meta_info']
_meta_table['IpMib.Ipnettophysicaltable.Ipnettophysicalentry']['meta_info'].parent =_meta_table['IpMib.Ipnettophysicaltable']['meta_info']
_meta_table['IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry']['meta_info'].parent =_meta_table['IpMib.Ipv6Scopezoneindextable']['meta_info']
_meta_table['IpMib.Ipdefaultroutertable.Ipdefaultrouterentry']['meta_info'].parent =_meta_table['IpMib.Ipdefaultroutertable']['meta_info']
_meta_table['IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry']['meta_info'].parent =_meta_table['IpMib.Ipv6Routeradverttable']['meta_info']
_meta_table['IpMib.Icmpstatstable.Icmpstatsentry']['meta_info'].parent =_meta_table['IpMib.Icmpstatstable']['meta_info']
_meta_table['IpMib.Icmpmsgstatstable.Icmpmsgstatsentry']['meta_info'].parent =_meta_table['IpMib.Icmpmsgstatstable']['meta_info']
_meta_table['IpMib.Ip']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Iptrafficstats']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Icmp']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipaddrtable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipnettomediatable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipv4Interfacetable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipv6Interfacetable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipsystemstatstable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipifstatstable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipaddressprefixtable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipaddresstable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipnettophysicaltable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipv6Scopezoneindextable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipdefaultroutertable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Ipv6Routeradverttable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Icmpstatstable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
_meta_table['IpMib.Icmpmsgstatstable']['meta_info'].parent =_meta_table['IpMib']['meta_info']
